import copy
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from build_data import validate
from content_pipeline import load_content, identities, guard_identities

class ImportChecks(unittest.TestCase):
    def setUp(self):self.data,self.plan,self.batches=load_content()
    def test_full_content_passes(self):
        validate(self.data)
        self.assertEqual(len(self.data['words']),347)
        self.assertEqual(sum(len(w['senses']) for w in self.data['words']),686)
        self.assertEqual(sum(len(w['examples']) for w in self.data['words']),639)
        self.assertEqual(sum(s['ready'] for w in self.data['words'] for s in w['senses']),478)
        self.assertEqual(len(self.batches[1][1]['words']),60)
        self.assertEqual(len(self.batches[2][1]['words']),85)
        self.assertEqual(len(self.batches[3][1]['words']),104)
        self.assertEqual(len(self.batches[4][1]['words']),76)
    def test_seventh_batch_is_small_sample_and_sixth_remains_unpublished(self):
        batch_ids=[batch['id'] for batch,part in self.batches]
        self.assertNotIn('batch-006',batch_ids)
        seventh=next(part for batch,part in self.batches if batch['id']=='batch-007')
        self.assertEqual([(w['id'],w['spelling']) for w in seventh['words']],
                         [('w1000','coordinate'),('w1001','subordinate')])
        self.assertEqual(sum(len(w['senses']) for w in seventh['words']),6)
        self.assertEqual(sum(len(w['examples']) for w in seventh['words']),4)
        self.assertEqual(sum(s['ready'] for w in seventh['words'] for s in w['senses']),4)
        self.assertFalse(any(w['spelling']=='origin' for w in self.data['words']))
    def test_duplicate_id_rejected(self):
        self.data['words'][20]['id']=self.data['words'][0]['id']
        with self.assertRaises(ValueError):validate(self.data)
    def test_duplicate_spelling_case_rejected(self):
        self.data['words'][20]['spelling']=' ACTION '
        with self.assertRaises(ValueError):validate(self.data)
    def test_broken_example_association_rejected(self):
        self.data['words'][20]['examples'][0]['sense_id']='missing'
        with self.assertRaises(ValueError):validate(self.data)
    def test_wrong_target_offsets_rejected(self):
        self.data['words'][20]['examples'][0]['target_start']=0
        with self.assertRaises(ValueError):validate(self.data)
    def test_pending_only_cannot_be_ready(self):
        w=next(w for w in self.data['words'] if w['spelling']=='steer')
        w['senses'][0]['ready']=True
        with self.assertRaises(ValueError):validate(self.data)
    def test_old_ids_not_repurposed_or_removed(self):
        old=identities(json.loads((ROOT/'content/sample.json').read_text(encoding='utf-8')))
        new=identities(self.data);guard_identities(old,new)
        bad=copy.deepcopy(new);bad['s0001-01']=['sense','w0021']
        with self.assertRaises(ValueError):guard_identities(old,bad)
        bad=copy.deepcopy(new);del bad['e0001-01']
        with self.assertRaises(ValueError):guard_identities(old,bad)

if __name__=='__main__':unittest.main()
