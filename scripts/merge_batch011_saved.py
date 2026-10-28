"""Save source-ordered eleventh-batch data and resumable checkpoints."""
import importlib
import json
import os
from pathlib import Path
from build_data import validate
from transcription_helpers import Transcription

ROOT = Path(__file__).resolve().parents[1]
PARTS = [('batch011_pages175_179',179), ('batch011_pages180_184',184),
         ('batch011_pages185_189',189), ('batch011_pages190_194',194)]

def save(name,data):
    path=ROOT/name
    stage=path.with_suffix(path.suffix+'.staging')
    stage.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    os.replace(stage,path)

def merge():
    plan=json.loads((ROOT/'content/import-plan.json').read_text(encoding='utf-8'))
    if any(b['id']=='batch-011' and b['status'] in ('imported','partially_imported') for b in plan['approved_batches']):
        raise SystemExit('batch-011 has published data; preserve its checkpoint.')
    t=Transcription(); associated=[]; merged=[]; saved={}
    result=dict(format_version=1,content_version='batch-011-v1',source_id='src-0001',
        method='manual_visual_transcription',words=[],
        policy='第十一批从PDF175 opportunity开始；完成范围见检查点。ID从w2104起，第九批w1309起保留续接。人工视觉转录，词义为编辑拆分，音标未外部核对，疑点不学习。')
    for name,end in PARTS:
        if not (ROOT/'scripts'/(name+'.py')).exists():
            break
        module=importlib.import_module(name)
        module.append(t,associated)
        through=module.COMPLETE_THROUGH
        assert through<=end
        result['words']=t.words
        validate(result)
        assert [w['id'] for w in t.words]==[f'w{i:04}' for i in range(2104,2104+len(t.words))]
        assert all(175<=p<=195 for w in t.words for p in w['pdf_pages'])
        assert all(175<=i['pdf_page']<=195 for i in associated)
        merged.append(name); saved[name]=through
        save('content/drafts/batch-011.json',result)
        save('content/drafts/batch-011-associated.json',dict(method='manual_visual_transcription',items=associated))
        save('content/drafts/batch-011-checkpoint.json',dict(
            status='ready_for_review' if through==194 else 'draft',completed_pages=list(range(175,through+1)),
            words=len(t.words),last_word=t.words[-1]['spelling'],start_id='w2104',
            context_pages_reviewed=sorted({p for w in t.words for p in w['pdf_pages'] if p>through}),
            next_word=module.NEXT_WORD,next_pdf_page=module.NEXT_PAGE,next_id=f'w{2104+len(t.words):04}',
            continuations=[],merged_parts=merged.copy(),saved_part_pages=saved.copy(),
            note='仅保存已完成段，尚未发布；第九批153–154页仍未导入，w1309起保留，不复用。'))
        print(f'Saved through PDF{through}: {len(t.words)} words; next {module.NEXT_WORD}.',flush=True)
        if through<end:
            break
    return result

if __name__=='__main__':
    merge()
