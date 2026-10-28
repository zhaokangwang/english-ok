"""Register reviewed batch008, preserving old content and a local rollback copy."""
import hashlib
import json
import os
import shutil
import sys
from pathlib import Path
from build_data import validate
from content_pipeline import load_content, identities, guard_identities

ROOT = Path(__file__).resolve().parents[1]
BACKUP = ROOT / 'runtime/pre-batch008-20261026'

def read(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))

def write(name, data):
    path = ROOT / name
    stage = path.with_suffix(path.suffix + '.staging')
    stage.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.replace(stage, path)

def backup():
    manifest = BACKUP / 'sha256.json'
    if manifest.exists():
        saved = json.loads(manifest.read_text(encoding='utf-8'))
        for name, digest in saved.items():
            assert hashlib.sha256((BACKUP / name).read_bytes()).hexdigest() == digest
        return
    assert read('content/import-plan.json')['content_version'] == 'vocabulary-0.7.0'
    files = list((ROOT / 'content').rglob('*.json'))
    files += list((ROOT / 'docs').glob('*.md')) + list((ROOT / 'docs').glob('*.json'))
    files += list((ROOT / 'web/data').glob('*')) + [ROOT / 'README.md']
    checksums = {}
    for source in files:
        if not source.is_file():
            continue
        name = source.relative_to(ROOT).as_posix()
        target = BACKUP / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        checksums[name] = hashlib.sha256(target.read_bytes()).hexdigest()
    manifest.write_text(json.dumps(checksums, indent=2) + '\n', encoding='utf-8')
    print(f'Saved pre-batch008 rollback copy ({len(checksums)} files).')

def publish():
    old, plan, _ = load_content()
    if any(b['id'] == 'batch-008' for b in plan['approved_batches']):
        raise SystemExit('batch-008 already registered; preserve the published input and checkpoint.')
    assert len(old['words']) == 533 and plan['content_version'] == 'vocabulary-0.7.0'
    draft = read('content/drafts/batch-008.json')
    checkpoint = read('content/drafts/batch-008-checkpoint.json')
    assert checkpoint['status'] == 'ready_for_review' and not checkpoint['continuations']
    assert checkpoint['completed_pages'] == list(range(115, 135))
    assert checkpoint['next_word'] == 'personality' and checkpoint['next_pdf_page'] == 135
    words = draft['words']
    assert len(words) == checkpoint['words']
    assert words[0]['id'] == 'w1105' and words[0]['spelling'] == 'spot'
    assert words[-1]['spelling'] == 'temper' and words[-1]['pdf_pages'] == [134]
    assert [w['id'] for w in words] == [f'w{i:04}' for i in range(1105, 1105 + len(words))]
    assert all(w['book_unit_id'] == 'unit-004' for w in words)
    assert not any(w['spelling'] in ('detect', 'personality') for w in words)
    candidate = dict(old, words=old['words'] + words)
    validate(candidate)
    guard_identities(identities(old), identities(candidate))
    units = read('content/units.json')
    by_id = {u['id']: u for u in units['units']}
    assert len(by_id['unit-003']['word_ids']) == 164 and not by_id['unit-003']['complete']
    assert len(by_id['unit-004']['word_ids']) == 24
    by_id['unit-004']['word_ids'].extend(w['id'] for w in words)
    by_id['unit-004']['complete'] = False
    assigned = [wid for unit in units['units'] for wid in unit['word_ids']]
    assert len(assigned) == len(set(assigned)) and set(assigned) == {w['id'] for w in candidate['words']}
    units['note'] = f'前两单元345主词完整；第三单元164词仍缺第六批23词；第四单元{24+len(words)}词，尚未完整覆盖。'
    pending = [w['spelling'] for w in words if any(e['review_status'] == 'pending' for e in w['examples'])]
    entry = dict(id='batch-008', file='content/batches/batch-008.json',
        associated_file='content/batches/batch-008-associated.json', owner_pages=[115,134],
        context_pages=[114,135], status='imported', imported_word_ids=[w['id'] for w in words],
        reviewed_pdf_pages=list(range(115,136)),
        coverage=f'PDF115 spot至134 temper共{len(words)}个新主词；均属于第四单元。115页detect已归第七批，不重复；135页核对下一词personality，尚未导入。',
        quality_notes=[
            '人工视觉转录；保留源释义、完整例句与原译，词义为编辑拆分，音标未外部核对。',
            '待核实例句涉及：'+'、'.join(pending)+'；保留原文原译但不进入学习队列。',
            '派生和关联例句另存associated文件，不计为新增主词或独立学习卡。',
            '第六批23词缺口及其保留ID不变；第三、四单元均complete=false。',
            '所有旧身份保留；学习队列、进度和备份兼容性另由自动测试验证。'])
    plan['approved_batches'].append(entry)
    plan['content_version'] = 'vocabulary-0.8.0'
    plan['note'] = '第六批部分导入83词仍缺23词；第八批115–134页主词已完成，下一批从135页personality开始。未来范围暂定。'
    backup()
    assert not (ROOT / 'content/transcripts/batch-008-initial.json').exists()
    write('content/transcripts/batch-008-initial.json', draft)
    write(entry['file'], draft)
    write(entry['associated_file'], read('content/drafts/batch-008-associated.json'))
    write('content/units.json', units)
    write('content/import-plan.json', plan)
    print(f'Registered batch-008: {len(words)} additions; all 533 prior word identities preserved.')

if __name__ == '__main__':
    backup() if '--backup-only' in sys.argv else publish()
