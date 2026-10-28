"""Merge and register a reviewed transcription batch from a JSON configuration.

Usage: python scripts/import_batch.py merge --config scripts/batch013-config.json
Actions: merge (save each complete part), check, backup, publish. Publication only
registers content; run build_data.py separately to rebuild the public artifacts.
"""
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import tempfile

from build_data import validate
from content_pipeline import guard_identities, identities, load_content
from transcription_helpers import Transcription

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def number(value):
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    require(isinstance(value, str) and re.fullmatch(r'w\d{4,}', value), 'Invalid word ID')
    return int(value[1:])


def encoded(data):
    return (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def digest(data):
    return hashlib.sha256(data).hexdigest()


class BatchImport:
    def __init__(self, config, root=None):
        self.root = Path(ROOT if root is None else root).resolve()
        self.config = copy.deepcopy(config)
        self.batch = config['batch_id']
        require(re.fullmatch(r'batch-\d{3,}', self.batch), 'Invalid batch_id')
        self.start = number(config['start_id'])
        self.lo, self.hi = config['owner_pages']
        self.context_lo, self.context_hi = config['context_pages']
        require(1 <= self.context_lo <= self.lo <= self.hi <= self.context_hi, 'Invalid page bounds')
        previous = self.lo - 1
        for part in config['parts']:
            require(re.fullmatch(r'[A-Za-z_]\w*', part['module']), 'Invalid part module')
            require(previous < part['end_page'] <= self.hi, 'Part boundaries must increase')
            previous = part['end_page']
        require(previous == self.hi, 'Parts must cover the owner-page boundary')
        self.paths = {
            'draft': f'content/drafts/{self.batch}.json',
            'associated': f'content/drafts/{self.batch}-associated.json',
            'checkpoint': f'content/drafts/{self.batch}-checkpoint.json',
            'published': f'content/batches/{self.batch}.json',
            'published_associated': f'content/batches/{self.batch}-associated.json',
            'initial': f'content/transcripts/{self.batch}-initial.json',
            'initial_associated': f'content/transcripts/{self.batch}-associated-initial.json',
        }

    def path(self, name):
        path = (self.root / name).resolve()
        require(path.is_relative_to(self.root), f'Path outside workspace: {name}')
        return path

    def read(self, name):
        return json.loads(self.path(name).read_text(encoding='utf-8'))

    def write(self, name, data, replace=True):
        path = self.path(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, staging = tempfile.mkstemp(prefix=path.name + '.', suffix='.staging', dir=path.parent)
        try:
            with os.fdopen(fd, 'wb') as stream:
                stream.write(encoded(data))
                stream.flush()
                os.fsync(stream.fileno())
            if replace:
                os.replace(staging, path)
            else:
                # Link atomically, refusing to replace an initial transcript or backup.
                os.link(staging, path)
        finally:
            Path(staging).unlink(missing_ok=True)

    def unpublished(self, plan):
        require(not any(b['id'] == self.batch for b in plan['approved_batches']),
                f'{self.batch} already registered; preserve its published checkpoint')

    def validate_words(self, data, associated):
        words = data['words']
        validate(data)
        require([w['id'] for w in words] == [f'w{i:04}' for i in range(self.start, self.start + len(words))],
                'Batch word IDs must be continuous from start_id')
        offset = self.config.get('printed_page_offset', 8)
        for word in words:
            pages = word['pdf_pages']
            require(all(isinstance(p, int) and self.context_lo <= p <= self.context_hi for p in pages),
                    f'Word page outside context: {word["id"]}')
            require(self.lo <= min(pages) <= self.hi, f'Headword outside owner pages: {word["id"]}')
            require(word['printed_pages'] == [f'{p-offset:03}' for p in pages], 'Wrong printed word pages')
            matches = [r['unit_id'] for r in self.config['unit_ranges']
                       if r['owner_pages'][0] <= min(pages) <= r['owner_pages'][1]]
            require(len(matches) == 1, f'Owner page needs exactly one unit: {word["id"]}')
            require(word.get('book_unit_id', matches[0]) == matches[0], f'Conflicting unit: {word["id"]}')
            word['book_unit_id'] = matches[0]
            for example in word['examples']:
                require(example['pdf_page'] in pages and example['printed_page'] == f'{example["pdf_page"]-offset:03}',
                        f'Wrong example page: {example["id"]}')
            for related in word['related']:
                require(self.context_lo <= related['pdf_page'] <= self.context_hi, 'Related page outside context')
        require(all(isinstance(i['pdf_page'], int) and self.context_lo <= i['pdf_page'] <= self.context_hi
                    for i in associated['items']), 'Associated page outside context')

    def merge(self):
        self.unpublished(self.read('content/import-plan.json'))
        t, associated, merged, saved = Transcription(), [], [], {}
        method = self.config.get('method', 'manual_visual_transcription')
        result = dict(format_version=1, content_version=self.config.get('draft_content_version', self.batch + '-v1'),
                      source_id=self.config['source_id'], method=method, words=t.words,
                      policy=self.config.get('policy', '人工视觉转录；词义为编辑拆分，疑点不学习。'))
        previous = self.lo - 1
        for part in self.config['parts']:
            module_path = self.path('scripts/' + part['module'] + '.py')
            if not module_path.exists():
                break
            spec = importlib.util.spec_from_file_location(part['module'], module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            prior_words, prior_associated = copy.deepcopy(t.words), copy.deepcopy(associated)
            module.append(t, associated)
            require(t.words[:len(prior_words)] == prior_words and associated[:len(prior_associated)] == prior_associated,
                    'A part changed previously completed material')
            through = module.COMPLETE_THROUGH
            require(previous < through <= part['end_page'], 'Invalid COMPLETE_THROUGH')
            require(t.words, 'Cannot checkpoint an empty batch')
            material = dict(method=method, items=associated)
            self.validate_words(result, material)
            require(all(min(w['pdf_pages']) <= through for w in t.words), 'Headword beyond completed pages')
            require(module.NEXT_PAGE >= through and module.NEXT_WORD, 'Invalid next-headword boundary')
            merged.append(part['module'])
            saved[part['module']] = through
            cp = dict(status='ready_for_review' if through == self.hi else 'draft',
                      completed_pages=list(range(self.lo, through + 1)), words=len(t.words),
                      last_word=t.words[-1]['spelling'], start_id=f'w{self.start:04}',
                      context_pages_reviewed=sorted({p for w in t.words for p in w['pdf_pages'] if p > through}),
                      next_word=module.NEXT_WORD, next_pdf_page=module.NEXT_PAGE,
                      next_id=f'w{self.start+len(t.words):04}', continuations=[],
                      merged_parts=merged.copy(), saved_part_pages=saved.copy(),
                      note=self.config.get('checkpoint_note', '仅保存已完成段，尚未发布。'),
                      sha256={self.paths['draft']: digest(encoded(result)),
                              self.paths['associated']: digest(encoded(material))})
            self.write(self.paths['draft'], result)
            self.write(self.paths['associated'], material)
            # Commit the checkpoint last; hashes detect interrupted multi-file saves.
            self.write(self.paths['checkpoint'], cp)
            print(f'Saved {self.batch} through PDF{through}: {len(t.words)} words; next {module.NEXT_WORD}.', flush=True)
            if through < part['end_page']:
                break
            previous = through
        return result

    def check(self):
        old, plan, _ = load_content()
        self.unpublished(plan)
        require(plan['content_version'] == self.config['previous_content_version'], 'Unexpected previous content version')
        require(len(old['words']) == self.config['expected_old_words'], 'Unexpected previous word count')
        require(plan['source_id'] == self.config['source_id'], 'Source mismatch')
        for batch_id, fields in self.config.get('preserve_batches', {}).items():
            batch = next((b for b in plan['approved_batches'] if b['id'] == batch_id), None)
            require(batch is not None and all(batch.get(k) == v for k, v in fields.items()),
                    f'Historical batch changed: {batch_id}')
        draft, associated, cp = (self.read(self.paths[key]) for key in ('draft', 'associated', 'checkpoint'))
        require(cp['status'] == 'ready_for_review' and not cp['continuations'], 'Draft is incomplete')
        require(cp['completed_pages'] == list(range(self.lo, self.hi + 1)), 'Incomplete owner pages')
        require(cp['merged_parts'] == [p['module'] for p in self.config['parts']], 'Incomplete part list')
        require(cp['saved_part_pages'] == {p['module']: p['end_page'] for p in self.config['parts']}, 'Incomplete part checkpoints')
        for key in ('draft', 'associated'):
            name = self.paths[key]
            require(cp.get('sha256', {}).get(name) == digest(self.path(name).read_bytes()), 'Checkpoint file hash mismatch')
        self.validate_words(draft, associated)
        require(draft['source_id'] == self.config['source_id'] and draft['format_version'] == 1, 'Draft source/format mismatch')
        method = self.config.get('method', 'manual_visual_transcription')
        require(draft['method'] == associated['method'] == method, 'Draft method mismatch')
        words = draft['words']
        require(words and len(words) == cp['words'] and words[-1]['spelling'] == cp['last_word'], 'Checkpoint word count/boundary mismatch')
        require(cp['start_id'] == f'w{self.start:04}' and cp['next_id'] == f'w{self.start+len(words):04}', 'Checkpoint ID mismatch')
        if 'expected_words' in self.config:
            require(len(words) == self.config['expected_words'], 'Unexpected batch word count')
        for label, word in [('first', words[0]), ('last', words[-1])]:
            require(all(word.get(k) == v for k, v in self.config.get('expected_' + label, {}).items()),
                    f'Unexpected {label} word')
        if 'expected_next' in self.config:
            nxt = self.config['expected_next']
            require((cp['next_word'], cp['next_pdf_page']) == (nxt['word'], nxt['page']), 'Unexpected next word')
        candidate = dict(old, words=old['words'] + words)
        validate(candidate)
        guard_identities(identities(old), identities(candidate))
        for lo, hi in self.config.get('reserved_id_ranges', []):
            require(not any(number(lo) <= number(w['id']) <= number(hi) for w in candidate['words']),
                    f'Reserved ID range reused: {lo}–{hi}')
        units = self.read('content/units.json')
        by_id = {u['id']: u for u in units['units']}
        require(len(by_id) == len(units['units']), 'Duplicate unit IDs')
        old_assignments = {wid: u['id'] for u in units['units'] for wid in u['word_ids']}
        require(len(old_assignments) == sum(len(u['word_ids']) for u in units['units'])
                and set(old_assignments) == {w['id'] for w in old['words']}, 'Invalid previous unit assignments')
        for unit in self.config.get('units', {}).get('new', []):
            require(unit['id'] not in by_id and not unit.get('word_ids'), 'New unit already exists or contains word IDs')
            unit = dict(unit, word_ids=[])
            units['units'].append(unit)
            by_id[unit['id']] = unit
        for word in words:
            require(word['book_unit_id'] in by_id, f'Unknown unit: {word["book_unit_id"]}')
            by_id[word['book_unit_id']]['word_ids'].append(word['id'])
        for unit_id, complete in self.config.get('units', {}).get('complete', {}).items():
            require(unit_id in by_id and isinstance(complete, bool), 'Invalid unit completion setting')
            by_id[unit_id]['complete'] = complete
        if 'note' in self.config.get('units', {}):
            units['note'] = self.config['units']['note']
        assigned = [wid for u in units['units'] for wid in u['word_ids']]
        require(len(assigned) == len(set(assigned)) and set(assigned) == {w['id'] for w in candidate['words']},
                'Each word must belong to exactly one unit')
        require(all(next(u['id'] for u in units['units'] if wid in u['word_ids']) == uid
                    for wid, uid in old_assignments.items()), 'Previous unit assignments changed')
        entry = dict(id=self.batch, file=self.paths['published'], associated_file=self.paths['published_associated'],
                     owner_pages=[self.lo, self.hi], context_pages=[self.context_lo, self.context_hi], status='imported',
                     imported_word_ids=[w['id'] for w in words],
                     reviewed_pdf_pages=self.config.get('reviewed_pdf_pages', sorted(set(range(self.lo, self.hi + 1))
                         | {p for w in words for p in w['pdf_pages']} | {i['pdf_page'] for i in associated['items']})),
                     coverage=self.config['coverage'], quality_notes=self.config.get('quality_notes', []))
        plan['approved_batches'].append(entry)
        plan['content_version'] = self.config['content_version']
        if 'plan_note' in self.config:
            plan['note'] = self.config['plan_note']
        for key in ('published', 'published_associated', 'initial', 'initial_associated'):
            require(not self.path(self.paths[key]).exists(), f'Refusing to overwrite {self.paths[key]}')
        return draft, associated, units, plan

    def backup(self):
        directory = self.path(self.config['backup_dir'])
        require(not any(directory.is_relative_to(self.path(p)) for p in ('content', 'docs', 'web')),
                'Backup must be outside content, docs and web')
        manifest = directory / 'sha256.json'
        if manifest.exists():
            saved = json.loads(manifest.read_text(encoding='utf-8'))
            # Earlier batches and pre-transcription snapshots used a plain path/hash map.
            files = saved.get('files', saved)
            if 'files' in saved:
                require(saved['batch_id'] == self.batch and saved['content_version'] == self.config['previous_content_version'],
                        'Backup belongs to another batch/version')
            require('content/import-plan.json' in files and 'content/units.json' in files, 'Incomplete backup manifest')
            for name, checksum in files.items():
                target = (directory / name).resolve()
                require(target.is_relative_to(directory) and digest(target.read_bytes()) == checksum, f'Backup changed: {name}')
            old_plan = json.loads((directory / 'content/import-plan.json').read_text(encoding='utf-8'))
            require(old_plan['content_version'] == self.config['previous_content_version'], 'Wrong backup content version')
            return saved
        require(self.read('content/import-plan.json')['content_version'] == self.config['previous_content_version'],
                'Cannot create a pre-import backup after the version changed')
        directory.mkdir(parents=True, exist_ok=False)
        sources = list(self.path('content').rglob('*.json'))
        sources += list(self.path('docs').glob('*.md')) + list(self.path('docs').glob('*.json'))
        sources += list(self.path('web/data').glob('*')) + [self.path('README.md')]
        checksums = {}
        for source in sources:
            if not source.is_file():
                continue
            name = source.relative_to(self.root).as_posix()
            target = directory / name
            target.parent.mkdir(parents=True, exist_ok=True)
            data = source.read_bytes()
            with target.open('xb') as stream:
                stream.write(data)
            checksums[name] = digest(data)
        saved = dict(format_version=1, batch_id=self.batch, content_version=self.config['previous_content_version'], files=checksums)
        self.write((manifest.relative_to(self.root)).as_posix(), saved, replace=False)
        print(f'Saved immutable pre-{self.batch} rollback copy ({len(checksums)} files).', flush=True)
        return saved

    def publish(self):
        draft, associated, units, plan = self.check()
        self.backup()
        for key, data in [('initial', draft), ('initial_associated', associated),
                          ('published', draft), ('published_associated', associated)]:
            self.write(self.paths[key], data, replace=False)
        self.write('content/units.json', units)
        self.write('content/import-plan.json', plan)
        print(f'Registered {self.batch}: {len(draft["words"])} new words; previous identities and gaps preserved.', flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('merge', 'check', 'backup', 'publish'))
    parser.add_argument('--config', required=True, type=Path)
    args = parser.parse_args()
    runner = BatchImport(json.loads(args.config.read_text(encoding='utf-8')))
    try:
        getattr(runner, args.action)()
    except (ValueError, FileExistsError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()
