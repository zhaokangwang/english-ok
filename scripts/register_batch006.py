"""Register reviewed batch006 material with its missing source range recorded."""
import json
import shutil
from pathlib import Path
from build_data import validate
from content_pipeline import load_content, identities, guard_identities

ROOT = Path(__file__).resolve().parents[1]

def read(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))

def write(name, data):
    (ROOT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def register():
    old, plan, _ = load_content()
    if any(b['id'] == 'batch-006' for b in plan['approved_batches']):
        raise SystemExit('batch-006 already registered; do not rerun the one-time registrar.')
    draft = read('content/drafts/batch-006.json')
    checkpoint = read('content/drafts/batch-006-checkpoint.json')
    assert checkpoint['status'] == 'ready_for_partial_import'
    assert checkpoint['missing_word_ids'] == [f'w{i:04}' for i in range(380,403)]
    assert draft['words'][0]['id'] == 'w0346' and draft['words'][0]['spelling'] == 'origin'
    assert draft['words'][-1]['spelling'] == 'senator'
    assert len(draft['words']) == checkpoint['words'] == 83
    sixth_ids = [w['id'] for w in draft['words']]
    assert not set(identities(old)) & set(identities(draft))
    assert max(sixth_ids) < 'w1000'
    combined = dict(old, words=old['words'] + draft['words'])
    validate(combined)
    guard_identities(identities(old), identities(combined))
    expected_seventh = [('w1000', 'coordinate'), ('w1001', 'subordinate')]
    assert [(w['id'], w['spelling']) for w in combined['words'] if w['id'] >= 'w1000'] == expected_seventh
    units = read('content/units.json')
    third = next(u for u in units['units'] if u['id'] == 'unit-003')
    assert third['word_ids'] == ['w1000', 'w1001']
    third.update(word_ids=sixth_ids + third['word_ids'], complete=False)
    units['note'] = '前两单元345主词已收录；第三单元含第六批83词和第七批2词；第六批23词缺口及第三单元其余内容尚未完成。'
    assigned = [wid for unit in units['units'] for wid in unit['word_ids']]
    assert len(assigned) == len(set(assigned)) and set(assigned) == {w['id'] for w in combined['words']}
    pending = [w['spelling'] for w in draft['words'] if any(e['review_status'] == 'pending' for e in w['examples'])]
    entry = dict(id='batch-006', file='content/batches/batch-006.json',
        associated_file='content/batches/batch-006-associated.json', owner_pages=[75, 94],
        context_pages=[75, 95], status='partially_imported', imported_word_ids=sixth_ids,
        missing_word_ids=checkpoint['missing_word_ids'],
        missing_file='content/drafts/batch-006-missing.json',
        coverage='仅已保存的origin至hinder、inherit至senator共83词；obstacle至heritage共23词（PDF81末及82–85页，heritage续至86）缺失。末词senator续至95页。第六批尚未完成。',
        quality_notes=[
            '人工视觉转录；词义为编辑拆分；音标及原书真题出处未作外部复核。',
            '82–85页转录再次出现regurg输出流错误，仅发布已保存并核对的内容，未编补缺口。',
            '待核实例句涉及：' + '、'.join(pending) + '；保留原文与原译，不进入学习队列。',
            '派生和固定搭配独立保存；第三单元后半尚未完成，complete=false。',
            '保留第七批w1000/w1001及所有先前身份，不重编号或覆盖旧学习记录。'])
    plan['approved_batches'].append(entry)
    plan['approved_batches'].sort(key=lambda b: b['id'])
    plan['content_version'] = 'vocabulary-0.6.0'
    seventh = next(b for b in plan['approved_batches'] if b['id'] == 'batch-007')
    seventh['coverage'] = '仅PDF95的coordinate、subordinate两个主词已试导入；该页其他词及第七批余页未处理，下一词cancel仍在95页。'
    plan['note'] = '第六批部分导入83词，仍缺23词；第七批仅2词小样本。未来页范围暂定，不代表全书完整覆盖。'
    for filename in ('batch-006.json', 'batch-006-associated.json'):
        dest = ROOT / 'content/batches' / filename
        if dest.exists():
            raise SystemExit(f'Refusing to overwrite {dest}')
        shutil.copy2(ROOT / 'content/drafts' / filename, dest)
    snapshot = ROOT / 'content/transcripts/batch-006-initial.json'
    assert not snapshot.exists()
    shutil.copy2(ROOT / 'content/drafts/batch-006.json', snapshot)
    write('content/import-plan.json', plan)
    write('content/units.json', units)
    print(f'Registered {len(sixth_ids)} sixth-batch words; prior 347 identities preserved.')

if __name__ == '__main__':
    register()
