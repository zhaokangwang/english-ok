"""Merge source-ordered eighth-batch parts and save resumable checkpoints."""
import importlib
import json
import os
from pathlib import Path
from build_data import validate
from transcription_helpers import Transcription

ROOT=Path(__file__).resolve().parents[1]
DRAFT=ROOT/'content/drafts'
PARTS=[('batch008_pages115_119',119),('batch008_pages120_124',124),
       ('batch008_pages125_129',129),('batch008_pages130_134',134)]
def read(path):
    return json.loads(path.read_text(encoding='utf-8'))
def save(path,data):
    stage=path.with_suffix(path.suffix+'.staging')
    stage.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    os.replace(stage,path)
def merge():
    plan=read(ROOT/'content/import-plan.json')
    if any(b['id']=='batch-008' and b['status']=='imported' for b in plan['approved_batches']):
        raise SystemExit('batch-008 is already complete; preserve its published checkpoint.')
    t=Transcription(); associated=[]; merged=[]
    result=dict(format_version=1,content_version='batch-008-v1',source_id='src-0001',
        method='manual_visual_transcription',words=[],
        policy='第八批从PDF115 spot开始；实际完成范围见检查点。人工视觉转录；词义为编辑拆分，音标未外部核对，疑点不学习。')
    for name,end in PARTS:
        if not (ROOT/'scripts'/(name+'.py')).exists():
            break
        module=importlib.import_module(name)
        module.append(t,associated)
        through=module.COMPLETE_THROUGH
        assert through<=end
        result['words']=t.words
        validate(result)
        assert [w['id'] for w in t.words]==[f'w{i:04}' for i in range(1105,1105+len(t.words))]
        assert all(115<=p<=135 for w in t.words for p in w['pdf_pages'])
        assert all(115<=item['pdf_page']<=135 for item in associated)
        merged.append(name)
        save(DRAFT/'batch-008.json',result)
        save(DRAFT/'batch-008-associated.json',dict(method='manual_visual_transcription',items=associated))
        save(DRAFT/'batch-008-checkpoint.json',dict(status='ready_for_review' if through==134 else 'draft',
            completed_pages=list(range(115,through+1)),words=len(t.words),last_word=t.words[-1]['spelling'],
            context_pages_reviewed=sorted({p for w in t.words for p in w['pdf_pages'] if p>through}),
            next_word=module.NEXT_WORD,next_pdf_page=module.NEXT_PAGE,next_id=f'w{1105+len(t.words):04}',
            continuations=[],merged_parts=merged.copy(),note='只保存已完成段，尚未发布；不重复导入第七批detect。'))
        print(f'Saved through PDF{through}: {len(t.words)} words; next {module.NEXT_WORD}.',flush=True)
        if through<end:
            break
    return result
if __name__=='__main__':
    merge()
