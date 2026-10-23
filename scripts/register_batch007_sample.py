"""Register the reviewed PDF95 two-word pilot while leaving batch006 unpublished."""
import json
import shutil
from pathlib import Path
from build_data import validate
from content_pipeline import load_content, identities, guard_identities

ROOT = Path(__file__).resolve().parents[1]
def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))
def write(path, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

data, plan, _ = load_content()
if any(b['id'] == 'batch-007' for b in plan['approved_batches']):
    raise SystemExit('batch-007 is already registered; do not rerun this one-time script.')
sample = read('content/drafts/batch-007.json')
assert [(w['id'], w['spelling']) for w in sample['words']] == [
    ('w1000', 'coordinate'), ('w1001', 'subordinate')]
draft006 = read('content/drafts/batch-006.json')
assert not set(identities(sample)) & set(identities(draft006))
candidate = dict(data, words=data['words'] + sample['words'])
validate(candidate)
guard_identities(identities(data), identities(candidate))
assert not {w['id'] for w in draft006['words']} & {w['id'] for w in candidate['words']}

units = read('content/units.json')
assert not any(u['id'] == 'unit-003' for u in units['units'])
units['units'].append(dict(id='unit-003', title='第三单元', subtitle='origin ～ principle',
    sort_order=3, complete=False, word_ids=['w1000', 'w1001']))
units['note'] = '前两单元345主词已收录；第三单元仅试导入PDF95两个词，第六批与第七批其余内容均未完成。'
assigned = [wid for u in units['units'] for wid in u['word_ids']]
assert len(assigned) == len(set(assigned)) and set(assigned) == {w['id'] for w in candidate['words']}

entry = dict(id='batch-007', file='content/batches/batch-007.json',
    associated_file='content/batches/batch-007-associated.json',
    owner_pages=[95, 114], context_pages=[94, 115], status='partially_imported',
    imported_word_ids=['w1000', 'w1001'], reviewed_pdf_pages=[95],
    coverage='仅PDF95的coordinate、subordinate两个主词试导入；该页其他词及第七批余页未处理，下一词cancel仍在95页。第六批保留未导入缺口。',
    quality_notes=['两词完整内容在PDF95；4条例句对应4个可学习词义，另外2个词义缺例句不入队。',
        '第三单元仅有这2词，complete=false；音标未外部词典复核。',
        'ID从w1000开始，保留第六批草稿w0346起的身份；ID空隙不代表已导入词条。'])
plan['content_version'] = 'vocabulary-0.5.1'
plan['approved_batches'].append(entry)
plan['note'] = '允许保留批次缺口及部分导入；batch-006仍为未发布草稿，batch-007仅2词小样本，不代表95–114页已完成。'
ledger = read('content/batch-ledger.json')
for b in ledger['batches']:
    if b['id'] == 'batch-006':
        b.update(status='draft', coverage='仅76–81页34词草稿，未进入正式词库。')
for filename in ('batch-007.json', 'batch-007-associated.json'):
    destination = ROOT / 'content/batches' / filename
    if destination.exists():
        raise SystemExit(f'Refusing to overwrite {destination}')
    shutil.copy2(ROOT / 'content/drafts' / filename, destination)
snapshot = ROOT / 'content/transcripts/batch-007-initial.json'
assert not snapshot.exists()
shutil.copy2(ROOT / 'content/drafts/batch-007.json', snapshot)
write('content/import-plan.json', plan)
write('content/units.json', units)
write('content/batch-ledger.json', ledger)
print('Registered batch-007 two-word pilot; batch-006 remains unpublished. Ready to build.')
