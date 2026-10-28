import copy
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from build_data import validate
from content_pipeline import load_content, identities, guard_identities

def historical_unit_state(unit,last_id):
    kept=[wid for wid in unit['word_ids'] if wid<=last_id]
    complete=unit['complete'] and len(kept)==len(unit['word_ids'])
    return len(kept),complete

class ImportChecks(unittest.TestCase):
    def setUp(self):self.data,self.plan,self.batches=load_content()
    def test_full_content_passes(self):
        validate(self.data)
        # Retain exact historical totals when later approved batches are appended.
        snapshot=[w for batch,part in self.batches if batch['id']<='batch-012' for w in part['words']]
        self.assertEqual(len(snapshot),1051)
        self.assertEqual(sum(len(w['senses']) for w in snapshot),2281)
        self.assertEqual(sum(len(w['examples']) for w in snapshot),1972)
        self.assertEqual(sum(s['ready'] for w in snapshot for s in w['senses']),1456)
        self.assertEqual(sum(e['review_status']=='pending' for w in snapshot for e in w['examples']),86)
        self.assertEqual(len(self.batches[1][1]['words']),60)
        self.assertEqual(len(self.batches[2][1]['words']),85)
        self.assertEqual(len(self.batches[3][1]['words']),104)
        self.assertEqual(len(self.batches[4][1]['words']),76)
    def test_seventh_batch_complete_import_keeps_sample_ids_and_page_boundary(self):
        batch,seventh=next((batch,part) for batch,part in self.batches if batch['id']=='batch-007')
        self.assertEqual(batch['status'],'imported')
        self.assertEqual([w['id'] for w in seventh['words']],[f'w{i:04}' for i in range(1000,1105)])
        self.assertEqual([(w['id'],w['spelling']) for w in seventh['words'][:2]],
                         [('w1000','coordinate'),('w1001','subordinate')])
        self.assertEqual(sum(len(w['senses']) for w in seventh['words'][:2]),6)
        self.assertEqual(sum(len(w['examples']) for w in seventh['words'][:2]),4)
        self.assertEqual(sum(s['ready'] for w in seventh['words'][:2] for s in w['senses']),4)
        self.assertEqual(sum(len(w['senses']) for w in seventh['words']),229)
        self.assertEqual(sum(len(w['examples']) for w in seventh['words']),204)
        self.assertEqual(sum(s['ready'] for w in seventh['words'] for s in w['senses']),152)
        self.assertEqual(sum(e['review_status']=='pending' for w in seventh['words'] for e in w['examples']),12)
        self.assertEqual(seventh['words'][-1]['spelling'],'detect')
        self.assertEqual(seventh['words'][-1]['pdf_pages'],[114,115])
        self.assertFalse(any(w['spelling']=='spot' for w in seventh['words']))
    def test_eighth_batch_range_counts_and_boundary(self):
        batch,eighth=next((batch,part) for batch,part in self.batches if batch['id']=='batch-008')
        self.assertEqual(batch['status'],'imported')
        self.assertEqual([w['id'] for w in eighth['words']],[f'w{i:04}' for i in range(1105,1216)])
        self.assertEqual((eighth['words'][0]['spelling'],eighth['words'][0]['pdf_pages']),('spot',[115]))
        self.assertEqual((eighth['words'][-1]['spelling'],eighth['words'][-1]['pdf_pages']),('temper',[134]))
        self.assertEqual(sum(len(w['senses']) for w in eighth['words']),245)
        self.assertEqual(sum(len(w['examples']) for w in eighth['words']),206)
        self.assertEqual(sum(s['ready'] for w in eighth['words'] for s in w['senses']),146)
        self.assertTrue(all(w['book_unit_id']=='unit-004' for w in eighth['words']))
        self.assertFalse(any(w['spelling'] in ('detect','personality') for w in eighth['words']))
    def test_eighth_batch_cross_page_entries_keep_full_source_pages(self):
        eighth=next(part for batch,part in self.batches if batch['id']=='batch-008')
        words={w['spelling']:w for w in eighth['words']}
        for spelling,pages in [('senseless',[116,117]),('specialise',[119,120]),
                               ('phenomenon',[124,125]),('physical',[126,127]),
                               ('respond',[129,130]),('phase',[130,131]),('approximate',[133,134])]:
            self.assertEqual(words[spelling]['pdf_pages'],pages)
        self.assertEqual({e['pdf_page'] for e in words['specialise']['examples']},{120})
        self.assertEqual({e['pdf_page'] for e in words['respond']['examples']},{130})
        self.assertEqual({r['pdf_page'] for r in words['respond']['related']},{130})
    def test_eighth_batch_pending_examples_do_not_make_senses_ready(self):
        eighth=next(part for batch,part in self.batches if batch['id']=='batch-008')
        pending=[e for w in eighth['words'] for e in w['examples'] if e['review_status']=='pending']
        self.assertEqual(len(pending),11)
        for w in eighth['words']:
            for s in w['senses']:
                checked=any(e['sense_id']==s['id'] and e['review_status']=='visual_checked' for e in w['examples'])
                self.assertEqual(s['ready'],checked)
        for spelling in ('release','vigorous'):
            word=next(w for w in eighth['words'] if w['spelling']==spelling)
            self.assertTrue(word['examples'])
            self.assertTrue(all(e['review_status']=='pending' for e in word['examples']))
            self.assertFalse(any(s['ready'] for s in word['senses']))
    def test_eighth_batch_preserves_all_previous_identities_and_sixth_gap(self):
        previous={'words':[w for batch,part in self.batches if batch['id']<'batch-008' for w in part['words']]}
        self.assertEqual(len(previous['words']),533)
        guard_identities(identities(previous),identities(self.data))
        self.assertFalse(any('w0380'<=w['id']<='w0402' for w in self.data['words']))
    def test_ninth_batch_partial_range_counts_and_boundary(self):
        batch,ninth=next((batch,part) for batch,part in self.batches if batch['id']=='batch-009')
        self.assertEqual(batch['status'],'partially_imported')
        self.assertEqual([w['id'] for w in ninth['words']],[f'w{i:04}' for i in range(1216,1309)])
        self.assertEqual((ninth['words'][0]['spelling'],ninth['words'][0]['pdf_pages']),('personality',[135]))
        self.assertEqual((ninth['words'][-1]['spelling'],ninth['words'][-1]['pdf_pages']),('pioneer',[152,153]))
        self.assertEqual(sum(len(w['senses']) for w in ninth['words']),216)
        self.assertEqual(sum(len(w['examples']) for w in ninth['words']),181)
        self.assertEqual(sum(s['ready'] for w in ninth['words'] for s in w['senses']),135)
        self.assertFalse(any(w['spelling'] in ('temper','compatible','upset') for w in ninth['words']))
    def test_ninth_batch_unit_boundary_and_cross_page_entries(self):
        ninth=next(part for batch,part in self.batches if batch['id']=='batch-009')
        words={w['spelling']:w for w in ninth['words']}
        self.assertEqual(sum(w['book_unit_id']=='unit-004' for w in ninth['words']),54)
        self.assertEqual(sum(w['book_unit_id']=='unit-005' for w in ninth['words']),39)
        self.assertEqual((words['strap']['id'],words['strap']['pdf_pages']),('w1269',[144]))
        self.assertEqual((words['merit']['id'],words['merit']['pdf_pages']),('w1270',[146]))
        self.assertFalse(any(145 in w['pdf_pages'] for w in ninth['words']))
        for spelling,pages in [('calculate',[135,136]),('yield',[136,137]),
                               ('sweep',[139,140]),('rebel',[143,144]),('violate',[146,147]),
                               ('qualify',[149,150]),('ornament',[150,151]),('productive',[151,152])]:
            self.assertEqual(words[spelling]['pdf_pages'],pages)
    def test_ninth_batch_pending_and_associated_material_are_separate(self):
        batch,ninth=next((batch,part) for batch,part in self.batches if batch['id']=='batch-009')
        pending=[e['id'] for w in ninth['words'] for e in w['examples'] if e['review_status']=='pending']
        self.assertEqual(pending,['e1230-01','e1249-02','e1263-02','e1270-02','e1286-02'])
        associated=json.loads((ROOT/batch['associated_file']).read_text(encoding='utf-8'))
        self.assertEqual(len(associated['items']),23)
        self.assertFalse(any(w['spelling']=='qualified' for w in ninth['words']))
        self.assertTrue(any(item['word']=='qualified' and item['pdf_page']==150 for item in associated['items']))
    def test_ninth_batch_keeps_previous_identities_and_sixth_gap(self):
        previous={'words':[w for batch,part in self.batches if batch['id']<'batch-009' for w in part['words']]}
        self.assertEqual(len(previous['words']),644)
        guard_identities(identities(previous),identities(self.data))
        self.assertFalse(any('w0380'<=w['id']<='w0402' for w in self.data['words']))
    def test_tenth_batch_range_counts_and_boundary(self):
        batch,tenth=next((batch,part) for batch,part in self.batches if batch['id']=='batch-010')
        self.assertEqual(batch['status'],'imported')
        self.assertEqual([w['id'] for w in tenth['words']],[f'w{i:04}' for i in range(2000,2104)])
        self.assertEqual((tenth['words'][0]['spelling'],tenth['words'][0]['pdf_pages']),('upset',[155]))
        self.assertEqual((tenth['words'][-1]['spelling'],tenth['words'][-1]['pdf_pages']),('occasion',[174,175]))
        self.assertEqual(sum(len(w['senses']) for w in tenth['words']),225)
        self.assertEqual(sum(len(w['examples']) for w in tenth['words']),191)
        self.assertEqual(sum(s['ready'] for w in tenth['words'] for s in w['senses']),143)
        self.assertFalse(any(w['spelling'] in ('asset','opportunity') for w in tenth['words']))
    def test_tenth_batch_unit_boundary_keeps_fifth_incomplete(self):
        tenth=next(part for batch,part in self.batches if batch['id']=='batch-010')
        words={w['spelling']:w for w in tenth['words']}
        self.assertEqual(sum(w['book_unit_id']=='unit-005' for w in tenth['words']),81)
        self.assertEqual(sum(w['book_unit_id']=='unit-006' for w in tenth['words']),23)
        self.assertEqual((words['cognitive']['id'],words['cognitive']['pdf_pages']),('w2080',[169]))
        self.assertEqual((words['extinguish']['id'],words['extinguish']['pdf_pages']),('w2081',[171]))
        self.assertFalse(any(170 in w['pdf_pages'] for w in tenth['words']))
        units={u['id']:u for u in json.loads((ROOT/'content/units.json').read_text(encoding='utf-8'))['units']}
        for unit,count,complete in [('unit-003',164,False),('unit-004',189,True),
                                    ('unit-005',120,False),('unit-006',23,False)]:
            self.assertEqual(historical_unit_state(units[unit],'w2103'),(count,complete))
        for spelling,pages in [('handle',[155,156]),('ethic',[158,159]),('incredible',[159,160]),
                               ('approve',[160,161]),('deteriorate',[164,165]),('abolish',[165,166]),
                               ('sting',[171,172]),('involve',[173,174]),('occasion',[174,175])]:
            self.assertEqual(words[spelling]['pdf_pages'],pages)
    def test_tenth_batch_pending_and_quarantined_material_are_excluded(self):
        batch,tenth=next((batch,part) for batch,part in self.batches if batch['id']=='batch-010')
        pending=[e['id'] for w in tenth['words'] for e in w['examples'] if e['review_status']=='pending']
        self.assertEqual(pending,['e2015-01','e2027-02','e2056-01','e2063-01','e2064-02',
                                  'e2066-02','e2071-02','e2097-02','e2101-02'])
        for word in tenth['words']:
            for sense in word['senses']:
                checked=any(e['sense_id']==sense['id'] and e['review_status']=='visual_checked' for e in word['examples'])
                self.assertEqual(sense['ready'],checked)
        associated=json.loads((ROOT/batch['associated_file']).read_text(encoding='utf-8'))['items']
        self.assertEqual(len(associated),36)
        self.assertEqual([(i['word'],i['pdf_page']) for i in associated if i.get('status')=='quarantined'],
                         [('strike',160),('disapprove',161)])
        self.assertEqual(len(next(w for w in tenth['words'] if w['spelling']=='strike')['examples']),1)
        self.assertFalse(any(w['spelling']=='disapprove' for w in tenth['words']))
    def test_tenth_batch_preserves_previous_identities_and_both_gaps(self):
        previous={'words':[w for batch,part in self.batches if batch['id']<'batch-010' for w in part['words']]}
        self.assertEqual(len(previous['words']),737)
        guard_identities(identities(previous),identities(self.data))
        self.assertFalse(any('w0380'<=w['id']<='w0402' or 'w1309'<=w['id']<'w2000' for w in self.data['words']))
        ninth=next(batch for batch,_ in self.batches if batch['id']=='batch-009')
        self.assertEqual((ninth['status'],ninth['unprocessed_owner_pages']),('partially_imported',[153,154]))
    def test_eleventh_batch_range_counts_and_boundary(self):
        batch,eleventh=next((batch,part) for batch,part in self.batches if batch['id']=='batch-011')
        self.assertEqual(batch['status'],'imported')
        self.assertEqual([w['id'] for w in eleventh['words']],[f'w{i:04}' for i in range(2104,2213)])
        self.assertEqual((eleventh['words'][0]['spelling'],eleventh['words'][0]['pdf_pages']),('opportunity',[175]))
        self.assertEqual((eleventh['words'][-1]['spelling'],eleventh['words'][-1]['pdf_pages']),('confuse',[194]))
        self.assertEqual(sum(len(w['senses']) for w in eleventh['words']),267)
        self.assertEqual(sum(len(w['examples']) for w in eleventh['words']),212)
        self.assertEqual(sum(s['ready'] for w in eleventh['words'] for s in w['senses']),157)
        self.assertFalse(any(w['spelling'] in ('occasion','refuse') for w in eleventh['words']))
    def test_eleventh_batch_cross_page_material_and_unit_ownership(self):
        eleventh=next(part for batch,part in self.batches if batch['id']=='batch-011')
        words={w['spelling']:w for w in eleventh['words']}
        self.assertTrue(all(w['book_unit_id']=='unit-006' for w in eleventh['words']))
        for spelling,pages in [('severe',[175,176]),('grip',[177,178]),('heighten',[179,180]),
                               ('nourish',[184,185]),('illuminate',[185,186]),('dignity',[186,187]),
                               ('flame',[189,190]),('flatter',[189,190]),('fiction',[190,191]),
                               ('ascertain',[192,193]),('compound',[193,194])]:
            self.assertEqual(words[spelling]['pdf_pages'],pages)
        units={u['id']:u for u in json.loads((ROOT/'content/units.json').read_text(encoding='utf-8'))['units']}
        for unit,count,complete in [('unit-003',164,False),('unit-004',189,True),
                                    ('unit-005',120,False),('unit-006',132,False)]:
            self.assertEqual(historical_unit_state(units[unit],'w2212'),(count,complete))
    def test_eleventh_batch_pending_and_quarantined_material_are_excluded(self):
        batch,eleventh=next((batch,part) for batch,part in self.batches if batch['id']=='batch-011')
        pending=[e['id'] for w in eleventh['words'] for e in w['examples'] if e['review_status']=='pending']
        self.assertEqual(pending,['e2120-02','e2125-01','e2129-01','e2132-02','e2151-01','e2151-02',
                                  'e2153-02','e2177-01','e2177-02','e2182-02','e2184-02','e2192-01'])
        for spelling in ('pollute','orient'):
            word=next(w for w in eleventh['words'] if w['spelling']==spelling)
            self.assertTrue(word['examples'])
            self.assertTrue(all(e['review_status']=='pending' for e in word['examples']))
            self.assertFalse(any(s['ready'] for s in word['senses']))
        associated=json.loads((ROOT/batch['associated_file']).read_text(encoding='utf-8'))['items']
        self.assertEqual(len(associated),28)
        self.assertEqual([(i['word'],i['pdf_page']) for i in associated if i.get('status')=='quarantined'],
                         [('non-durable',183)])
        self.assertFalse(any(w['spelling']=='non-durable' for w in eleventh['words']))
    def test_eleventh_batch_preserves_previous_identities_and_both_gaps(self):
        previous={'words':[w for batch,part in self.batches if batch['id']<'batch-011' for w in part['words']]}
        self.assertEqual(len(previous['words']),841)
        guard_identities(identities(previous),identities(self.data))
        self.assertFalse(any('w0380'<=w['id']<='w0402' or 'w1309'<=w['id']<'w2000' for w in self.data['words']))
        ninth=next(batch for batch,_ in self.batches if batch['id']=='batch-009')
        self.assertEqual((ninth['status'],ninth['unprocessed_owner_pages']),('partially_imported',[153,154]))
    def test_twelfth_batch_range_counts_and_boundary(self):
        batch,twelfth=next((batch,part) for batch,part in self.batches if batch['id']=='batch-012')
        self.assertEqual(batch['status'],'imported')
        self.assertEqual([w['id'] for w in twelfth['words']],[f'w{i:04}' for i in range(2213,2314)])
        self.assertEqual((twelfth['words'][0]['spelling'],twelfth['words'][0]['pdf_pages']),('refuse',[195]))
        self.assertEqual((twelfth['words'][-1]['spelling'],twelfth['words'][-1]['pdf_pages']),('alleviate',[214,215]))
        self.assertEqual(sum(len(w['senses']) for w in twelfth['words']),250)
        self.assertEqual(sum(len(w['examples']) for w in twelfth['words']),193)
        self.assertEqual(sum(s['ready'] for w in twelfth['words'] for s in w['senses']),139)
        self.assertFalse(any(w['spelling'] in ('confuse','ease') for w in twelfth['words']))
    def test_twelfth_batch_unit_boundary_and_cross_page_material(self):
        twelfth=next(part for batch,part in self.batches if batch['id']=='batch-012')
        words={w['spelling']:w for w in twelfth['words']}
        self.assertEqual(sum(w['book_unit_id']=='unit-006' for w in twelfth['words']),33)
        self.assertEqual(sum(w['book_unit_id']=='unit-007' for w in twelfth['words']),68)
        self.assertEqual((words['policy']['id'],words['policy']['pdf_pages']),('w2245',[201]))
        self.assertEqual((words['facility']['id'],words['facility']['pdf_pages']),('w2246',[203]))
        self.assertFalse(any(202 in w['pdf_pages'] for w in twelfth['words']))
        for spelling,pages in [('contemporary',[195,196]),('reform',[196,197]),('hammer',[199,200]),
                               ('artifact',[203,204]),('infect',[204,205]),('handicap',[205,206]),
                               ('loan',[207,208]),('paralyse',[208,209]),('utmost',[209,210]),
                               ('survive',[211,212]),('inhabit',[212,213]),('alleviate',[214,215])]:
            self.assertEqual(words[spelling]['pdf_pages'],pages)
        units={u['id']:u for u in json.loads((ROOT/'content/units.json').read_text(encoding='utf-8'))['units']}
        for unit,count,complete in [('unit-003',164,False),('unit-004',189,True),('unit-005',120,False),
                                    ('unit-006',165,True),('unit-007',68,False)]:
            self.assertEqual(historical_unit_state(units[unit],'w2313'),(count,complete))
    def test_twelfth_batch_pending_material_stays_out_of_learning(self):
        batch,twelfth=next((batch,part) for batch,part in self.batches if batch['id']=='batch-012')
        pending=[e['id'] for w in twelfth['words'] for e in w['examples'] if e['review_status']=='pending']
        self.assertEqual(pending,['e2214-02','e2216-01','e2241-02','e2243-01','e2245-02',
                                  'e2251-02','e2264-02','e2279-02','e2284-02','e2286-02',
                                  'e2290-01','e2295-02','e2296-02','e2306-02','e2312-02'])
        for word in twelfth['words']:
            for sense in word['senses']:
                checked=any(e['sense_id']==sense['id'] and e['review_status']=='visual_checked' for e in word['examples'])
                self.assertEqual(sense['ready'],checked)
        associated=json.loads((ROOT/batch['associated_file']).read_text(encoding='utf-8'))['items']
        self.assertEqual(len(associated),23)
        self.assertFalse(any(i.get('status')=='quarantined' for i in associated))
    def test_twelfth_batch_preserves_previous_identities_and_both_gaps(self):
        previous={'words':[w for batch,part in self.batches if batch['id']<'batch-012' for w in part['words']]}
        self.assertEqual(len(previous['words']),950)
        guard_identities(identities(previous),identities(self.data))
        self.assertFalse(any('w0380'<=w['id']<='w0402' or 'w1309'<=w['id']<'w2000' for w in self.data['words']))
        ninth=next(batch for batch,_ in self.batches if batch['id']=='batch-009')
        self.assertEqual((ninth['status'],ninth['unprocessed_owner_pages']),('partially_imported',[153,154]))
    def test_sixth_batch_partial_import_keeps_unprocessed_ids_reserved(self):
        batch,sixth=next((batch,part) for batch,part in self.batches if batch['id']=='batch-006')
        self.assertEqual(batch['status'],'partially_imported')
        self.assertEqual(len(sixth['words']),83)
        self.assertEqual(sum(len(w['senses']) for w in sixth['words']),169)
        self.assertEqual(sum(len(w['examples']) for w in sixth['words']),150)
        self.assertEqual(sum(s['ready'] for w in sixth['words'] for s in w['senses']),110)
        self.assertEqual(sum(e['review_status']=='pending' for w in sixth['words'] for e in w['examples']),3)
        expected_ids=[f'w{i:04}' for i in range(346,380)]+[f'w{i:04}' for i in range(403,452)]
        self.assertEqual([w['id'] for w in sixth['words']],expected_ids)
        self.assertEqual(sixth['words'][0]['spelling'],'origin')
        self.assertEqual(sixth['words'][-1]['spelling'],'senator')
        self.assertFalse(any(w['spelling'] in ('obstacle','hamper') for w in self.data['words']))
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
