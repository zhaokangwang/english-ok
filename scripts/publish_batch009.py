"""Register the saved portion of batch009, retaining the explicit unfinished pages."""
import hashlib
import json
import os
import shutil
import sys
from pathlib import Path
from build_data import validate
from content_pipeline import load_content, identities, guard_identities

ROOT = Path(__file__).resolve().parents[1]
BACKUP = ROOT/'runtime/pre-batch009-20261027'

def read(name):
    return json.loads((ROOT/name).read_text(encoding='utf-8'))

def write(name, data):
    path = ROOT/name
    stage = path.with_suffix(path.suffix+'.staging')
    stage.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    os.replace(stage,path)

def backup():
    manifest = BACKUP/'sha256.json'
    if manifest.exists():
        saved = json.loads(manifest.read_text(encoding='utf-8'))
        for name, digest in saved.items():
            assert hashlib.sha256((BACKUP/name).read_bytes()).hexdigest()==digest
        return
    assert read('content/import-plan.json')['content_version']=='vocabulary-0.8.0'
    files = list((ROOT/'content').rglob('*.json'))
    files += list((ROOT/'docs').glob('*.md'))+list((ROOT/'docs').glob('*.json'))
    files += list((ROOT/'web/data').glob('*'))+[ROOT/'README.md']
    checksums = {}
    for source in files:
        if not source.is_file():
            continue
        name = source.relative_to(ROOT).as_posix()
        target = BACKUP/name
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,target)
        checksums[name] = hashlib.sha256(target.read_bytes()).hexdigest()
    manifest.write_text(json.dumps(checksums,indent=2)+'\n',encoding='utf-8')
    print(f'Saved pre-batch009 rollback copy ({len(checksums)} files).')

def publish():
    old, plan, _ = load_content()
    if any(b['id']=='batch-009' for b in plan['approved_batches']):
        raise SystemExit('batch-009 already registered; preserve its published checkpoint.')
    assert len(old['words'])==644 and plan['content_version']=='vocabulary-0.8.0'
    draft = read('content/drafts/batch-009.json')
    checkpoint = read('content/drafts/batch-009-checkpoint.json')
    assert checkpoint['status']=='draft' and not checkpoint['continuations']
    assert checkpoint['completed_pages']==list(range(135,153))
    assert checkpoint['next_word']=='compatible' and checkpoint['next_pdf_page']==153
    words = draft['words']
    assert len(words)==checkpoint['words']==93
    assert (words[0]['id'],words[0]['spelling'])==('w1216','personality')
    assert words[-1]['spelling']=='pioneer' and words[-1]['pdf_pages']==[152,153]
    assert [w['id'] for w in words]==[f'w{i:04}' for i in range(1216,1216+len(words))]
    assert not any(w['spelling'] in ('temper','compatible','asset','upset') for w in words)
    fourth = [w for w in words if w['book_unit_id']=='unit-004']
    fifth = [w for w in words if w['book_unit_id']=='unit-005']
    assert words==fourth+fifth
    assert fourth[-1]['spelling']=='strap' and fourth[-1]['pdf_pages']==[144]
    assert fifth[0]['spelling']=='merit' and min(fifth[0]['pdf_pages'])==146
    assert all(max(w['pdf_pages'])<=144 for w in fourth)
    assert all(min(w['pdf_pages'])>=146 for w in fifth)
    candidate = dict(old,words=old['words']+words)
    validate(candidate)
    guard_identities(identities(old),identities(candidate))
    units = read('content/units.json')
    by_id = {u['id']:u for u in units['units']}
    assert len(by_id['unit-003']['word_ids'])==164 and not by_id['unit-003']['complete']
    assert len(by_id['unit-004']['word_ids'])==135 and 'unit-005' not in by_id
    fifth_unit = dict(id='unit-005',title='第五单元',subtitle='merit ～ cognitive',
                      sort_order=5,complete=False,word_ids=[])
    units['units'].append(fifth_unit); by_id['unit-005']=fifth_unit
    for word in words:
        by_id[word['book_unit_id']]['word_ids'].append(word['id'])
    by_id['unit-004']['complete']=True
    assigned = [wid for u in units['units'] for wid in u['word_ids']]
    assert len(assigned)==len(set(assigned)) and set(assigned)=={w['id'] for w in candidate['words']}
    units['note'] = f'前两单元345主词完整；第三单元164词仍缺第六批23词；第四单元{len(by_id["unit-004"]["word_ids"])}主词已完整；第五单元{len(fifth)}词，尚未完整覆盖。'
    pending = [w['spelling'] for w in words if any(e['review_status']=='pending' for e in w['examples'])]
    entry = dict(id='batch-009',file='content/batches/batch-009.json',
        associated_file='content/batches/batch-009-associated.json',owner_pages=[135,154],
        context_pages=[134,155],status='partially_imported',imported_word_ids=[w['id'] for w in words],
        reviewed_pdf_pages=list(range(135,154)),unprocessed_owner_pages=[153,154],
        coverage=f'仅导入已保存的PDF135 personality至152 pioneer共{len(words)}个新主词，pioneer续文读至153。135–144收尾第四单元，145为第五单元扉页，146 merit起属于第五单元。153–154起始主词未导入，下一词compatible153。',
        quality_notes=[
            '人工视觉转录；保留源释义、完整例句与原译，词义为编辑拆分，音标未外部核对。',
            '待核实例句涉及：'+'、'.join(pending)+'；原文原译保留，不进入学习队列。',
            '派生及关联例句另存associated文件，不混入主词数量或独立学习卡。',
            '第四单元incline至strap的主词覆盖完成；第五单元未收尾。第三单元保留第六批23词缺口及其ID。',
            '153页转录阶段收到stream disconnected before completion: regurg plugin blocked the output stream；只发布已经完整保存的内容，不重试被拦截输出。',
            '所有旧身份保留，个人学习库不受词库构建影响；队列和备份兼容性另由自动测试验证。'])
    plan['approved_batches'].append(entry)
    plan['content_version']='vocabulary-0.9.0'
    plan['note']='第九批部分导入135–152页93词；153–154尚未保存。第四单元完整、第五单元部分导入。续接第九批从153页compatible、w1309开始，第六批23词缺口保留。未来范围暂定。'
    backup()
    assert not (ROOT/'content/transcripts/batch-009-initial.json').exists()
    write('content/transcripts/batch-009-initial.json',draft)
    write('content/drafts/batch-009-unprocessed.json',dict(
        batch_id='batch-009',status='unprocessed',owner_pages=[153,154],
        next_word='compatible',next_pdf_page=153,next_id='w1309',
        last_saved_headword='pioneer',last_completed_pdf_page=152,
        error='stream disconnected before completion: regurg plugin blocked the output stream.',
        note='中断发生在继续转录153页的输出阶段；可见工具记录未显示具体被拦截调用，不能确定是哪一个词或句子触发。仅已保存135–152页主词发布，未重试153–154文本。'))
    write(entry['file'],draft)
    write(entry['associated_file'],read('content/drafts/batch-009-associated.json'))
    write('content/units.json',units)
    write('content/import-plan.json',plan)
    print(f'Registered partial batch009: {len(words)} new words; pages153–154 remain unfinished; old 644 identities preserved.')

if __name__=='__main__':
    backup() if '--backup-only' in sys.argv else publish()
