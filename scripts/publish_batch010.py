"""Register reviewed batch010 without consuming IDs reserved for batch009."""
import hashlib
import json
import os
import shutil
import sys
from pathlib import Path
from build_data import validate
from content_pipeline import load_content, identities, guard_identities

ROOT=Path(__file__).resolve().parents[1]
BACKUP=ROOT/'runtime/pre-batch010-20261027'

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
    assert read('content/import-plan.json')['content_version']=='vocabulary-0.9.0'
    files=list((ROOT/'content').rglob('*.json'))
    files+=list((ROOT/'docs').glob('*.md'))+list((ROOT/'docs').glob('*.json'))
    files+=list((ROOT/'web/data').glob('*'))+[ROOT/'README.md']
    checksums={}
    for source in files:
        if not source.is_file():
            continue
        name=source.relative_to(ROOT).as_posix(); target=BACKUP/name
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,target)
        checksums[name]=hashlib.sha256(target.read_bytes()).hexdigest()
    manifest.write_text(json.dumps(checksums,indent=2)+'\n',encoding='utf-8')
    print(f'Saved pre-batch010 rollback copy ({len(checksums)} files).')

def publish():
    old,plan,_=load_content()
    if any(b['id']=='batch-010' for b in plan['approved_batches']):
        raise SystemExit('batch-010 already registered; preserve its published checkpoint.')
    assert len(old['words'])==737 and plan['content_version']=='vocabulary-0.9.0'
    ninth=next(b for b in plan['approved_batches'] if b['id']=='batch-009')
    assert ninth['status']=='partially_imported' and ninth['unprocessed_owner_pages']==[153,154]
    draft=read('content/drafts/batch-010.json'); cp=read('content/drafts/batch-010-checkpoint.json')
    assert cp['status']=='ready_for_review' and not cp['continuations']
    assert cp['completed_pages']==list(range(155,175))
    assert (cp['next_word'],cp['next_pdf_page'])==('opportunity',175)
    words=draft['words']; assert len(words)==cp['words']==104
    assert (words[0]['id'],words[0]['spelling'],words[0]['pdf_pages'])==('w2000','upset',[155])
    assert (words[-1]['id'],words[-1]['spelling'],words[-1]['pdf_pages'])==('w2103','occasion',[174,175])
    assert [w['id'] for w in words]==[f'w{i:04}' for i in range(2000,2104)]
    assert not any(w['spelling'] in ('asset','compatible','opportunity') for w in words)
    fifth=[w for w in words if w['book_unit_id']=='unit-005']
    sixth=[w for w in words if w['book_unit_id']=='unit-006']
    assert words==fifth+sixth and (len(fifth),len(sixth))==(81,23)
    assert fifth[-1]['spelling']=='cognitive' and fifth[-1]['pdf_pages']==[169]
    assert sixth[0]['spelling']=='extinguish' and min(sixth[0]['pdf_pages'])==171
    assert all(max(w['pdf_pages'])<=169 for w in fifth)
    assert all(min(w['pdf_pages'])>=171 for w in sixth)
    candidate=dict(old,words=old['words']+words)
    validate(candidate); guard_identities(identities(old),identities(candidate))
    units=read('content/units.json'); by_id={u['id']:u for u in units['units']}
    assert len(by_id['unit-005']['word_ids'])==39 and not by_id['unit-005']['complete']
    assert len(by_id['unit-004']['word_ids'])==189 and by_id['unit-004']['complete']
    assert len(by_id['unit-003']['word_ids'])==164 and not by_id['unit-003']['complete']
    assert 'unit-006' not in by_id
    sixth_unit=dict(id='unit-006',title='第六单元',subtitle='extinguish ～ policy',sort_order=6,complete=False,word_ids=[])
    units['units'].append(sixth_unit); by_id['unit-006']=sixth_unit
    for w in words:
        by_id[w['book_unit_id']]['word_ids'].append(w['id'])
    by_id['unit-005']['complete']=False
    assigned=[wid for u in units['units'] for wid in u['word_ids']]
    assert len(assigned)==len(set(assigned)) and set(assigned)=={w['id'] for w in candidate['words']}
    units['note']='第一、二、四单元主词完整；第三单元164词仍缺第六批23词；第五单元120词，仍缺第九批153–154页主词；第六单元23词尚未完整。'
    pending=[w['spelling'] for w in words if any(e['review_status']=='pending' for e in w['examples'])]
    entry=dict(id='batch-010',file='content/batches/batch-010.json',
        associated_file='content/batches/batch-010-associated.json',owner_pages=[155,174],context_pages=[154,175],
        status='imported',imported_word_ids=[w['id'] for w in words],reviewed_pdf_pages=list(range(155,176)),
        id_allocation=dict(first='w2000',last='w2103',note='第九批从w1309起的续接ID不复用；本批另起w2000。'),
        coverage='PDF155 upset至174 occasion共104个新主词；155–169收尾第五单元正文，170为第六单元扉页，171 extinguish起属于第六单元。occasion关联资料续175，下一词opportunity尚未导入。',
        quality_notes=[
            '人工视觉转录；完整源释义、例句和原译保留，词义为编辑拆分，音标未外部核对。',
            '待核实例句涉及：'+'、'.join(pending)+'；原文原译保留，不进入学习队列。',
            'strike下不含目标词的例句、approve下的disapprove反义例句在关联资料中隔离；forge释义一处字形疑点留注，无对应例句的该义不入队。',
            '第五单元正文收尾但第九批153–154主词仍缺，complete=false；第六单元目前23词，complete=false；第六批23词缺口不变。',
            '旧737词身份及单元归属保留；本批ID从w2000开始，给第九批w1309起的续接保留空间。',
            '个人学习库不受内容构建影响；队列、进度和备份兼容性另由自动测试验证。'])
    plan['approved_batches'].append(entry); plan['content_version']='vocabulary-0.10.0'
    plan['note']='第十批155–174页104词已完成，下一批从175页opportunity开始。第六批23词及第九批153–154页缺口保留；第九批续接仍从compatible153/w1309开始。未来范围暂定。'
    backup()
    assert not (ROOT/'content/transcripts/batch-010-initial.json').exists()
    write('content/transcripts/batch-010-initial.json',draft)
    write('content/transcripts/batch-010-associated-initial.json',read('content/drafts/batch-010-associated.json'))
    write(entry['file'],draft); write(entry['associated_file'],read('content/drafts/batch-010-associated.json'))
    write('content/units.json',units); write('content/import-plan.json',plan)
    print('Registered batch010: 104 new words; old737 identities and both unfinished ranges preserved.')

if __name__=='__main__':
    backup() if '--backup-only' in sys.argv else publish()
