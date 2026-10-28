"""Compare a published batch with its immutable pre-import baseline."""
import argparse
import hashlib
import json
import sqlite3
from pathlib import Path
from import_batch import BatchImport, require

ROOT = Path(__file__).resolve().parents[1]


def audit(config):
    task = BatchImport(config)
    baseline = task.path(config['backup_dir'])
    manifest = json.loads((baseline / 'sha256.json').read_text(encoding='utf-8'))
    files = manifest.get('files', manifest)
    preserved = []
    generated = {'content/import-plan.json', 'content/units.json', 'content/id-registry.json',
                 'content/source-manifest.json', 'content/batch-ledger.json'}
    for name, checksum in files.items():
        saved = (baseline / name).resolve()
        require(saved.is_relative_to(baseline), 'Invalid baseline path')
        require(hashlib.sha256(saved.read_bytes()).hexdigest() == checksum, f'Baseline changed: {name}')
        if (name.startswith('content/') and name not in generated) or name == 'web/data/learning.sqlite':
            require(hashlib.sha256(task.path(name).read_bytes()).hexdigest() == checksum,
                    f'Previous content changed: {name}')
            preserved.append(name)
    old_plan = json.loads((baseline / 'content/import-plan.json').read_text(encoding='utf-8'))
    plan = task.read('content/import-plan.json')
    require(old_plan['content_version'] == config['previous_content_version'], 'Wrong baseline version')
    require(plan['content_version'] == config['content_version'], 'Wrong published version')
    require(plan['approved_batches'][:-1] == old_plan['approved_batches'], 'Previous batches changed')
    require(plan['approved_batches'][-1]['id'] == task.batch, 'Wrong latest batch')
    draft = task.read(task.paths['draft'])
    associated = task.read(task.paths['associated'])
    task.validate_words(draft, associated)
    require(draft == task.read(task.paths['published']), 'Draft differs from published batch')
    require(associated == task.read(task.paths['published_associated']), 'Associated draft differs')
    cp = task.read(task.paths['checkpoint'])
    require(cp['words'] == len(draft['words']), 'Checkpoint word count differs')
    require(cp['next_id'] == f'w{task.start+len(draft["words"]):04}', 'Checkpoint next ID differs')
    for key in ('draft', 'associated'):
        path = task.paths[key]
        require(cp['sha256'][path] == hashlib.sha256(task.path(path).read_bytes()).hexdigest(),
                'Checkpoint content hash differs')
    old = sqlite3.connect((baseline / 'web/data/vocabulary.sqlite').as_uri() + '?mode=ro', uri=True)
    current = sqlite3.connect(task.path('web/data/vocabulary.sqlite').as_uri() + '?mode=ro', uri=True)
    try:
        require(current.execute('PRAGMA integrity_check').fetchall() == [('ok',)], 'SQLite integrity failure')
        require(not current.execute('PRAGMA foreign_key_check').fetchall(), 'Foreign-key violation')
        unchanged = {}
        for table in ('words', 'senses', 'examples', 'related_words', 'unit_words', 'sources'):
            before = set(old.execute(f'SELECT * FROM {table}').fetchall())
            after = set(current.execute(f'SELECT * FROM {table}').fetchall())
            require(before <= after, f'Previous full rows changed: {table}')
            unchanged[table] = len(before)
        allowed = config.get('units', {}).get('complete', {})
        now_units = {r[0]: r for r in current.execute('SELECT * FROM units')}
        for row in old.execute('SELECT * FROM units'):
            expected = row[:-1] + (int(allowed.get(row[0], row[-1])),)
            require(now_units.get(row[0]) == expected, f'Previous unit changed unexpectedly: {row[0]}')
        require(current.execute("SELECT value FROM metadata WHERE key='content_version'").fetchone()[0]
                == config['content_version'], 'SQLite version differs')
        for lo, hi in config.get('reserved_id_ranges', []):
            require(not current.execute('SELECT id FROM words WHERE id BETWEEN ? AND ?', (lo, hi)).fetchall(),
                    'Reserved gap ID reused')
        before_count = old.execute('SELECT count(*) FROM words').fetchone()[0]
        after_count = current.execute('SELECT count(*) FROM words').fetchone()[0]
        require(before_count == config['expected_old_words'], 'Wrong previous word count')
        require(after_count == before_count + len(draft['words']), 'Wrong published word delta')
        counts = dict(words=after_count,
                      senses=current.execute('SELECT count(*) FROM senses').fetchone()[0],
                      examples=current.execute('SELECT count(*) FROM examples').fetchone()[0],
                      ready_senses=current.execute('SELECT count(*) FROM senses WHERE ready=1').fetchone()[0],
                      pending_examples=current.execute("SELECT count(*) FROM examples WHERE review_status='pending'").fetchone()[0])
        catalog = task.read('web/data/catalog.json')
        require(all(catalog.get(k) == v for k, v in counts.items()), 'Catalog totals differ')
    finally:
        old.close()
        current.close()
    result = dict(batch_id=task.batch, content_version=config['content_version'],
                  unchanged_rows=unchanged, unchanged_files=preserved, totals=counts,
                  integrity_check='ok', foreign_key_violations=0)
    task.write(config['backup_dir'] + '/post-audit.json', result)
    print(json.dumps(dict(batch_id=task.batch, totals=counts, unchanged_rows=unchanged,
                          unchanged_files=len(preserved), integrity_check='ok',
                          foreign_key_violations=0), ensure_ascii=False))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True)
    args = parser.parse_args()
    audit(json.loads(Path(args.config).read_text(encoding='utf-8')))
