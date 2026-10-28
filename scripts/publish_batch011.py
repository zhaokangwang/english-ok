"""Register reviewed batch011, preserving old data and both unfinished ranges."""
import hashlib
import json
import os
import shutil
import sys
from pathlib import Path
from build_data import validate
from content_pipeline import load_content,identities,guard_identities

ROOT=Path(__file__).resolve().parents[1]
BACKUP=ROOT/'runtime/pre-batch011-20261027'

def read(name):
    return json.loads((ROOT/name).read_text(encoding='utf-8'))

def write(name,data):
    path=ROOT/name; stage=path.with_suffix(path.suffix+'.staging')
    stage.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    os.replace(stage,path)

def backup():
    manifest=BACKUP/'sha256.json'
    if manifest.exists():
        for name,digest in json.loads(manifest.read_text(encoding='utf-8')).items():
            assert hashlib.sha256((BACKUP/name).read_bytes()).hexdigest()==digest
        return
    assert read('content/import-plan.json')['content_version']=='vocabulary-0.10.0'
    files=list((ROOT/'content').rglob('*.json'))
    files+=list((ROOT/'docs').glob('*.md'))+list((ROOT/'docs').glob('*.json'))
    files+=list((ROOT/'web/data').glob('*'))+[ROOT/'README.md']
    checksums={}
    for source in files:
        if not source.is_file():
            continue
        name=source.relative_to(ROOT).as_posix(); target=BACKUP/name
        target.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(source,target)
        checksums[name]=hashlib.sha256(target.read_bytes()).hexdigest()
    manifest.write_text(json.dumps(checksums,indent=2)+'\n',encoding='utf-8')
    print(f'Saved pre-batch011 rollback copy ({len(checksums)} files).')

def publish():
    old,plan,_=load_content()
    if any(b['id']=='batch-011' for b in plan['approved_batches']):
        raise SystemExit('batch-011 already registered; preserve its published checkpoint.')
    assert len(old['words'])==841 and plan['content_version']=='vocabulary-0.10.0'
    ninth=next(b for b in plan['approved_batches'] if b['id']=='batch-009')
    assert ninth['status']=='partially_imported' and ninth['unprocessed_owner_pages']==[153,154]
    draft=read('content/drafts/batch-011.json'); cp=read('content/drafts/batch-011-checkpoint.json')
    assert cp['status']=='ready_for_review' and not cp['continuations']
    assert cp['completed_pages']==list(range(175,195))
    assert (cp['next_word'],cp['next_pdf_page'])==('refuse',195)
    words=draft['words']; assert len(words)==cp['words']==109
    assert (words[0]['id'],words[0]['spelling'],words[0]['pdf_pages'])==('w2104','opportunity',[175])
    assert (words[-1]['id'],words[-1]['spelling'],words[-1]['pdf_pages'])==('w2212','confuse',[194])
    assert [w['id'] for w in words]==[f'w{i:04}' for i in range(2104,2104+len(words))]
    assert all(w['book_unit_id']=='unit-006' for w in words)
    assert not any(w['spelling'] in ('occasion','refuse','compatible','asset') for w in words)
    candidate=dict(old,words=old['words']+words)
    validate(candidate); guard_identities(identities(old),identities(candidate))
    units=read('content/units.json'); by_id={u['id']:u for u in units['units']}
    assert len(by_id['unit-006']['word_ids'])==23 and not by_id['unit-006']['complete']
    assert len(by_id['unit-005']['word_ids'])==120 and not by_id['unit-005']['complete']
    assert len(by_id['unit-004']['word_ids'])==189 and by_id['unit-004']['complete']
    assert len(by_id['unit-003']['word_ids'])==164 and not by_id['unit-003']['complete']
    by_id['unit-006']['word_ids'].extend(w['id'] for w in words)
    assigned=[wid for u in units['units'] for wid in u['word_ids']]
    assert len(assigned)==len(set(assigned)) and set(assigned)=={w['id'] for w in candidate['words']}
    units['note']=f'第一、二、四单元主词完整；第三单元164词仍缺第六批23词；第五单元120词仍缺第九批153–154页；第六单元{23+len(words)}词，正文尚未收尾。'
    pending=[w['spelling'] for w in words if any(e['review_status']=='pending' for e in w['examples'])]
    entry=dict(id='batch-011',file='content/batches/batch-011.json',
        associated_file='content/batches/batch-011-associated.json',owner_pages=[175,194],context_pages=[174,195],
        status='imported',imported_word_ids=[w['id'] for w in words],reviewed_pdf_pages=list(range(175,196)),
        coverage=f'PDF175 opportunity至194 confuse共{len(words)}个新主词，均属于第六单元；175上方occasion关联资料已属第十批，不重复导入。下一词refuse在195页，尚未导入。',
        quality_notes=[
            '人工视觉转录；保留完整源释义、例句及原译，词义为编辑拆分，音标未外部核对。',
            '待核实例句涉及：'+'、'.join(pending)+'；原文原译保留，不进入学习队列。',
            '派生关联例句另存associated，不混入主词数量；原书字形或释义疑点保留说明。',
            '第六单元尚未收尾，complete=false；第五单元仍因第九批153–154页缺口不完整；第六批23词缺口不变。',
            '旧841词身份及单元归属保留；第九批续接仍为compatible153/w1309，本批不复用该范围。',
            '个人学习库不受内容构建影响；队列、进度和备份兼容性另由自动测试验证。'])
    plan['approved_batches'].append(entry); plan['content_version']='vocabulary-0.11.0'
    plan['note']='第十一批175–194页主词已完成，下一批从195页refuse开始。第六批23词及第九批153–154页缺口保留；第九批续接仍为compatible153/w1309。未来范围暂定。'
    backup()
    assert not (ROOT/'content/transcripts/batch-011-initial.json').exists()
    write('content/transcripts/batch-011-initial.json',draft)
    write('content/transcripts/batch-011-associated-initial.json',read('content/drafts/batch-011-associated.json'))
    write(entry['file'],draft); write(entry['associated_file'],read('content/drafts/batch-011-associated.json'))
    write('content/units.json',units); write('content/import-plan.json',plan)
    print(f'Registered batch011: {len(words)} new words; all old841 identities and both gaps preserved.')

if __name__=='__main__':
    backup() if '--backup-only' in sys.argv else publish()
