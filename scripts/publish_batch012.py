"""Register reviewed batch012 and the sixth/seventh book-unit boundary."""
import hashlib
import json
import os
import shutil
import sys
from pathlib import Path
from build_data import validate
from content_pipeline import load_content,identities,guard_identities

ROOT=Path(__file__).resolve().parents[1]
BACKUP=ROOT/'runtime/pre-batch012-20261027'

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
    assert read('content/import-plan.json')['content_version']=='vocabulary-0.11.0'
    files=list((ROOT/'content').rglob('*.json'))
    files+=list((ROOT/'docs').glob('*.md'))+list((ROOT/'docs').glob('*.json'))
    files+=list((ROOT/'web/data').glob('*'))+[ROOT/'README.md']; checksums={}
    for source in files:
        if not source.is_file():
            continue
        name=source.relative_to(ROOT).as_posix(); target=BACKUP/name
        target.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(source,target)
        checksums[name]=hashlib.sha256(target.read_bytes()).hexdigest()
    manifest.write_text(json.dumps(checksums,indent=2)+'\n',encoding='utf-8')
    print(f'Saved pre-batch012 rollback copy ({len(checksums)} files).')

def publish():
    old,plan,_=load_content()
    if any(b['id']=='batch-012' for b in plan['approved_batches']):
        raise SystemExit('batch-012 already registered; preserve its published checkpoint.')
    assert len(old['words'])==950 and plan['content_version']=='vocabulary-0.11.0'
    ninth=next(b for b in plan['approved_batches'] if b['id']=='batch-009')
    assert ninth['status']=='partially_imported' and ninth['unprocessed_owner_pages']==[153,154]
    draft=read('content/drafts/batch-012.json'); cp=read('content/drafts/batch-012-checkpoint.json')
    assert cp['status']=='ready_for_review' and not cp['continuations']
    assert cp['completed_pages']==list(range(195,215))
    assert (cp['next_word'],cp['next_pdf_page'])==('ease',215)
    words=draft['words']; assert len(words)==cp['words']==101
    assert (words[0]['id'],words[0]['spelling'],words[0]['pdf_pages'])==('w2213','refuse',[195])
    assert (words[-1]['id'],words[-1]['spelling'],words[-1]['pdf_pages'])==('w2313','alleviate',[214,215])
    assert [w['id'] for w in words]==[f'w{i:04}' for i in range(2213,2213+len(words))]
    assert not any(w['spelling'] in ('confuse','ease','compatible','asset') for w in words)
    sixth=[w for w in words if w['book_unit_id']=='unit-006']
    seventh=[w for w in words if w['book_unit_id']=='unit-007']
    assert words==sixth+seventh and (len(sixth),len(seventh))==(33,68)
    assert sixth[-1]['spelling']=='policy' and sixth[-1]['pdf_pages']==[201]
    assert seventh[0]['spelling']=='facility' and min(seventh[0]['pdf_pages'])==203
    assert all(max(w['pdf_pages'])<=201 for w in sixth)
    assert all(min(w['pdf_pages'])>=203 for w in seventh)
    candidate=dict(old,words=old['words']+words)
    validate(candidate); guard_identities(identities(old),identities(candidate))
    units=read('content/units.json'); by_id={u['id']:u for u in units['units']}
    assert len(by_id['unit-006']['word_ids'])==132 and not by_id['unit-006']['complete']
    assert len(by_id['unit-005']['word_ids'])==120 and not by_id['unit-005']['complete']
    assert 'unit-007' not in by_id
    new_unit=dict(id='unit-007',title='第七单元',subtitle='facility ～ instrument',sort_order=7,complete=False,word_ids=[])
    units['units'].append(new_unit); by_id['unit-007']=new_unit
    for w in words:
        by_id[w['book_unit_id']]['word_ids'].append(w['id'])
    by_id['unit-006']['complete']=True
    assert len(by_id['unit-006']['word_ids'])==165
    assigned=[wid for u in units['units'] for wid in u['word_ids']]
    assert len(assigned)==len(set(assigned)) and set(assigned)=={w['id'] for w in candidate['words']}
    units['note']=f'第一、二、四、六单元主词完整；第三单元164词仍缺第六批23词；第五单元120词仍缺第九批153–154页；第七单元{len(seventh)}词尚未收尾。'
    pending=[w['spelling'] for w in words if any(e['review_status']=='pending' for e in w['examples'])]
    entry=dict(id='batch-012',file='content/batches/batch-012.json',
        associated_file='content/batches/batch-012-associated.json',owner_pages=[195,214],context_pages=[194,215],
        status='imported',imported_word_ids=[w['id'] for w in words],reviewed_pdf_pages=list(range(195,216)),
        coverage=f'PDF195 refuse至214 alleviate共{len(words)}个新主词。195–201收尾第六单元，202为第七单元扉页，203 facility起属于第七单元；alleviate续文读至215，下一词ease尚未导入。',
        quality_notes=[
            '人工视觉转录；完整源释义、例句和原译保留，词义为编辑拆分，音标未外部核对。',
            '待核实例句涉及：'+'、'.join(pending)+'；原文原译保留，不进入学习队列。',
            '派生和关联资料另存associated，不混入主词数量或独立学习卡。',
            '第六单元extinguish至policy共165主词覆盖完成；第七单元未收尾。第六批23词及第九批153–154页缺口保留。',
            '所有旧950词身份及单元归属保留；第九批续接仍为compatible153/w1309。',
            '个人学习库不受内容构建影响；队列、进度和备份兼容性另由自动测试验证。'])
    plan['approved_batches'].append(entry); plan['content_version']='vocabulary-0.12.0'
    plan['note']='第十二批195–214页主词已完成，下一批从215页ease开始。第六单元主词完整，第七单元部分导入；第六批23词及第九批153–154页缺口保留。未来范围暂定。'
    backup()
    assert not (ROOT/'content/transcripts/batch-012-initial.json').exists()
    write('content/transcripts/batch-012-initial.json',draft)
    write('content/transcripts/batch-012-associated-initial.json',read('content/drafts/batch-012-associated.json'))
    write(entry['file'],draft); write(entry['associated_file'],read('content/drafts/batch-012-associated.json'))
    write('content/units.json',units); write('content/import-plan.json',plan)
    print(f'Registered batch012: {len(words)} new words; old950 identities and both gaps preserved.')

if __name__=='__main__':
    backup() if '--backup-only' in sys.argv else publish()
