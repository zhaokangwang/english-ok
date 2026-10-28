"""Regression tests for the reusable importer, using small isolated content trees."""
import copy
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import content_pipeline
from import_batch import BatchImport, encoded
from transcription_helpers import Transcription


def word(n, spelling, page, unit='unit-old'):
    t = Transcription()
    t.add(n, spelling, '', 'n. 原释义', page, '原分组', [('n.', '释义')],
          [(0, 'A ' + spelling + '.', '原译', spelling, '', page)])
    t.words[0]['book_unit_id'] = unit
    return t.words[0]


class GenericImportChecks(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.addCleanup(patch.stopall)
        patch.object(content_pipeline, 'ROOT', self.root).start()
        self.config = dict(
            batch_id='batch-013', source_id='src-test', start_id=2314,
            owner_pages=[215, 216], context_pages=[214, 217],
            previous_content_version='vocabulary-0.12.0', content_version='vocabulary-0.13.0',
            expected_old_words=1, parts=[dict(module='part_one', end_page=215), dict(module='part_two', end_page=216)],
            unit_ranges=[dict(owner_pages=[215, 215], unit_id='unit-old'),
                         dict(owner_pages=[216, 216], unit_id='unit-new')],
            units=dict(new=[dict(id='unit-new', title='新单元', subtitle='', sort_order=2, complete=False)],
                       complete={'unit-old': True}),
            expected_first=dict(id='w2314', spelling='ease', pdf_pages=[215]),
            expected_last=dict(id='w2315', spelling='last', pdf_pages=[216, 217]),
            expected_next=dict(word='next', page=217), expected_words=2,
            preserve_batches={'batch-009': dict(status='partially_imported', unprocessed_owner_pages=[153, 154])},
            reserved_id_ranges=[['w1309', 'w1999']], coverage='测试页界',
            backup_dir='runtime/pre-batch013-test')
        self.runner = BatchImport(self.config, self.root)
        old = dict(format_version=1, source_id='src-test', content_version='old', words=[word(1, 'old', 153)])
        self.save('content/sample.json', old)
        self.save('content/batches/batch-009.json', old)
        self.save('content/batches/batch-009-associated.json', dict(items=[]))
        self.save('content/import-plan.json', dict(source_id='src-test', content_version='vocabulary-0.12.0', approved_batches=[
            dict(id='batch-009', file='content/batches/batch-009.json', associated_file='content/batches/batch-009-associated.json',
                 context_pages=[152, 154], status='partially_imported', unprocessed_owner_pages=[153, 154])]))
        self.save('content/units.json', dict(units=[dict(id='unit-old', title='旧单元', subtitle='', sort_order=1,
                                                        complete=False, word_ids=['w0001'])]))
        self.part('part_one', 215, word(2314, 'ease', 215), 'last', 216)
        last = word(2315, 'last', 216, 'unit-new')
        last['pdf_pages'] = [216, 217]
        last['printed_pages'] = ['208', '209']
        self.part('part_two', 216, last, 'next', 217)

    def save(self, name, data):
        target = self.root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(encoded(data))

    def part(self, module, through, record, nxt, page):
        path = self.root / 'scripts' / (module + '.py')
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text('import json\nCOMPLETE_THROUGH=' + str(through) + '\nNEXT_WORD=' + repr(nxt)
                        + '\nNEXT_PAGE=' + str(page) + '\ndef append(t, associated):\n    t.words.append(json.loads('
                        + repr(json.dumps(record, ensure_ascii=False)) + '))\n', encoding='utf-8')

    def merge(self):
        with redirect_stdout(io.StringIO()):
            return self.runner.merge()

    def test_failed_part_preserves_last_valid_checkpoint_and_rerun_finishes(self):
        bad = word(2316, 'bad-id', 216, 'unit-new')
        self.part('part_two', 216, bad, 'next', 217)
        with self.assertRaisesRegex(ValueError, 'continuous'):
            self.merge()
        cp = self.runner.read(self.runner.paths['checkpoint'])
        self.assertEqual((cp['completed_pages'], cp['next_id'], cp['words']), ([215], 'w2315', 1))
        self.assertEqual(len(self.runner.read(self.runner.paths['draft'])['words']), 1)
        self.part('part_two', 216, word(2315, 'last', 216, 'unit-new'), 'next', 217)
        self.merge()
        self.assertEqual(self.runner.read(self.runner.paths['checkpoint'])['status'], 'ready_for_review')

    def test_pages_and_unit_mapping_are_enforced_before_saving(self):
        self.part('part_one', 215, word(2314, 'outside', 218), 'last', 216)
        with self.assertRaisesRegex(ValueError, 'outside context'):
            self.merge()
        self.assertFalse((self.root / self.runner.paths['checkpoint']).exists())
        self.part('part_one', 215, word(2314, 'ease', 215, 'wrong-unit'), 'last', 216)
        with self.assertRaisesRegex(ValueError, 'Conflicting unit'):
            self.merge()

    def test_modified_draft_and_reserved_ids_block_registration(self):
        self.merge()
        draft = self.runner.read(self.runner.paths['draft'])
        draft['words'][0]['spelling'] = 'changed'
        self.save(self.runner.paths['draft'], draft)
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            self.runner.check()
        self.merge()
        self.runner.config['reserved_id_ranges'] = [['w2314', 'w2315']]
        with self.assertRaisesRegex(ValueError, 'Reserved ID range'):
            self.runner.check()
        self.assertFalse((self.root / self.runner.paths['initial']).exists())

    def test_backup_is_immutable_and_detects_corruption(self):
        with redirect_stdout(io.StringIO()):
            saved = self.runner.backup()
        name = 'content/import-plan.json'
        original = (self.root / self.config['backup_dir'] / name).read_bytes()
        changed = self.runner.read(name)
        changed['note'] = 'later draft work'
        self.save(name, changed)
        self.assertEqual(self.runner.backup(), saved)
        self.assertEqual((self.root / self.config['backup_dir'] / name).read_bytes(), original)
        (self.root / self.config['backup_dir'] / name).write_bytes(b'corrupt')
        with self.assertRaisesRegex(ValueError, 'Backup changed'):
            self.runner.backup()

    def test_publish_preserves_old_batch_units_and_initial_transcript(self):
        self.runner.config['method'] = 'local_ocr_with_visual_review'
        self.merge()
        old_plan = copy.deepcopy(self.runner.read('content/import-plan.json')['approved_batches'])
        old_batch = (self.root / 'content/batches/batch-009.json').read_bytes()
        with redirect_stdout(io.StringIO()):
            self.runner.publish()
        plan = self.runner.read('content/import-plan.json')
        self.assertEqual(plan['approved_batches'][:-1], old_plan)
        self.assertEqual((self.root / 'content/batches/batch-009.json').read_bytes(), old_batch)
        self.assertEqual(plan['content_version'], 'vocabulary-0.13.0')
        self.assertEqual(self.runner.read(self.runner.paths['published'])['method'], 'local_ocr_with_visual_review')
        self.assertEqual(plan['approved_batches'][-1]['imported_word_ids'], ['w2314', 'w2315'])
        units = self.runner.read('content/units.json')['units']
        self.assertEqual([(u['id'], u['word_ids'], u['complete']) for u in units],
                         [('unit-old', ['w0001', 'w2314'], True), ('unit-new', ['w2315'], False)])
        initial = (self.root / self.runner.paths['initial']).read_bytes()
        self.assertEqual(initial, (self.root / self.runner.paths['published']).read_bytes())
        with self.assertRaisesRegex(ValueError, 'already registered'):
            self.runner.publish()
        with self.assertRaisesRegex(ValueError, 'already registered'):
            self.merge()
        self.assertEqual((self.root / self.runner.paths['initial']).read_bytes(), initial)

    def test_existing_plain_checksum_backup_remains_usable_without_rewriting(self):
        with redirect_stdout(io.StringIO()):
            saved = self.runner.backup()
        manifest = self.config['backup_dir'] + '/sha256.json'
        self.save(manifest, saved['files'])
        before = (self.root / manifest).read_bytes()
        self.assertEqual(self.runner.backup(), saved['files'])
        self.assertEqual((self.root / manifest).read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
