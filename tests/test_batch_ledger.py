import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from build_data import write_ledger


class LedgerChecks(unittest.TestCase):
    def test_partial_out_of_order_import_preserves_gap_and_planned_ranges(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'content').mkdir()
            (root / 'docs').mkdir()
            existing = [dict(id=f'batch-{n:03}', owner_pages=[a, b],
                context_pages=[a - 1, b + 1], status='planned_unreviewed')
                for n, a, b in [(6, 75, 94), (7, 95, 114), (8, 115, 134)]]
            (root / 'content/batch-ledger.json').write_text(json.dumps(dict(batches=existing)), encoding='utf-8')
            partial = dict(existing[1], status='partially_imported', coverage='Two words on PDF95 only.')
            plan = dict(source_id='src-0001', source_sha256='test', approved_batches=[partial])
            with patch('build_data.ROOT', root):
                write_ledger(plan)
                first = (root / 'content/batch-ledger.json').read_bytes()
                write_ledger(plan)
            self.assertEqual(first, (root / 'content/batch-ledger.json').read_bytes())
            batches = {b['id']: b for b in json.loads(first)['batches']}
            self.assertEqual(batches['batch-006'], existing[0])
            self.assertEqual(batches['batch-007'], partial)
            self.assertEqual(batches['batch-008'], existing[2])
            self.assertEqual(batches['batch-009']['owner_pages'], [135, 154])
            self.assertIn('部分导入', (root / 'docs/batch-plan.md').read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
