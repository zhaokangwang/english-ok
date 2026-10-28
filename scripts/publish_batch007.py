"""Register the reviewed continuation of batch007 while preserving existing IDs."""
import json
import os
from pathlib import Path
from build_data import validate
from content_pipeline import load_content, identities, guard_identities

ROOT = Path(__file__).resolve().parents[1]

def read(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))

def write(name, data):
    path = ROOT / name
    stage = path.with_suffix(path.suffix + '.staging')
    stage.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.replace(stage, path)

def publish():
    old, plan, _ = load_content()
    entry = next(b for b in plan['approved_batches'] if b['id'] == 'batch-007')
    if entry['status'] == 'imported':
        raise SystemExit('batch-007 is already registered as complete; do not rerun this registrar.')
    draft = read('content/drafts/batch-007.json')
    checkpoint = read('content/drafts/batch-007-checkpoint.json')
    assert checkpoint['status'] == 'ready_for_review' and not checkpoint['continuations']
    assert checkpoint['completed_pages'] == list(range(95,115))
    assert checkpoint['next_word'] == 'spot' and checkpoint['next_pdf_page'] == 115
    assert len(draft['words']) == checkpoint['words'] == 105
    assert [(w['id'],w['spelling']) for w in draft['words'][:2]] == [('w1000','coordinate'),('w1001','subordinate')]
    assert draft['words'][-1]['id'] == 'w1104' and draft['words'][-1]['spelling'] == 'detect'
    prior_seventh = read(entry['file'])
    replaced_ids = {w['id'] for w in prior_seventh['words']}
    candidate = dict(old, words=[w for w in old['words'] if w['id'] not in replaced_ids] + draft['words'])
    validate(candidate)
    guard_identities(identities(old), identities(candidate))
    units = read('content/units.json')
    for unit in units['units']:
        unit['word_ids'] = [wid for wid in unit['word_ids'] if wid not in replaced_ids]
    by_id = {u['id']:u for u in units['units']}
    if 'unit-004' not in by_id:
        fourth = dict(id='unit-004', title='第四单元', subtitle='incline ～ strap',
                      sort_order=4, complete=False, word_ids=[])
        units['units'].append(fourth)
        by_id[fourth['id']] = fourth
    for word in draft['words']:
        unit_id = word['book_unit_id']
        assert unit_id in ('unit-003','unit-004')
        by_id[unit_id]['word_ids'].append(word['id'])
    by_id['unit-003']['complete'] = False
    by_id['unit-004']['complete'] = False
    assert len(by_id['unit-003']['word_ids']) == 164
    assert len(by_id['unit-004']['word_ids']) == 24
    assigned = [wid for unit in units['units'] for wid in unit['word_ids']]
    assert len(assigned) == len(set(assigned)) and set(assigned) == {w['id'] for w in candidate['words']}
    units['note'] = '前两单元345主词完整；第三单元164词仍缺第六批23词；第四单元24词，均尚未完整覆盖。'
    pending = [w['spelling'] for w in draft['words'] if any(e['review_status']=='pending' for e in w['examples'])]
    entry.update(status='imported', imported_word_ids=[w['id'] for w in draft['words']],
        reviewed_pdf_pages=list(range(95,116)),
        coverage='PDF95 coordinate至114 detect共105主词（含此前2词），本轮新增103词。95–109为第三单元收尾，110为第四单元扉页，111–114为第四单元正文；detect续文读至115，下一词spot尚未导入。',
        quality_notes=[
            '人工视觉转录；源释义、完整例句和原译均保留，词义为编辑拆分，音标未外部复核。',
            '待核实例句涉及：'+'、'.join(pending)+'；保留原文原译但不进入学习队列。',
            'motivate原书motive拼写疑点、acquaintance原译疑点隔离于关联资料。',
            '第三单元仍保留第六批23词缺口，complete=false；第四单元只收录24词，complete=false。',
            'w1000/w1001及所有已发布身份保留；学习队列和备份兼容性需通过验证后确认。'])
    plan['content_version'] = 'vocabulary-0.7.0'
    plan['note'] = '第六批部分导入83词仍缺23词；第七批95–114页主词已完成，下批从115页spot开始。未来范围暂定。'
    snapshot = ROOT / 'content/transcripts/batch-007-continuation-initial.json'
    if snapshot.exists():
        assert read('content/transcripts/batch-007-continuation-initial.json') == draft
    else:
        write('content/transcripts/batch-007-continuation-initial.json', draft)
    write('content/batches/batch-007.json', draft)
    write('content/batches/batch-007-associated.json', read('content/drafts/batch-007-associated.json'))
    write('content/units.json', units)
    write('content/import-plan.json', plan)
    print('Registered full batch-007: 105 words, 103 additions; all prior identities preserved.')

if __name__ == '__main__':
    publish()
