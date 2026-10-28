"""Save source-ordered ninth-batch data with resumable, gap-free checkpoints."""
import importlib
import json
import os
from pathlib import Path
from build_data import validate
from transcription_helpers import Transcription

ROOT = Path(__file__).resolve().parents[1]
PARTS = [('batch009_pages135_139',139), ('batch009_pages140_144',144),
         ('batch009_pages145_149',149), ('batch009_pages150_154',154)]

def save(name, data):
    path = ROOT / name
    stage = path.with_suffix(path.suffix+'.staging')
    stage.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    os.replace(stage, path)

def merge():
    plan = json.loads((ROOT/'content/import-plan.json').read_text(encoding='utf-8'))
    if any(b['id']=='batch-009' and b['status'] in ('imported','partially_imported') for b in plan['approved_batches']):
        raise SystemExit('batch-009 has published data; preserve its checkpoint and use an explicit continuation workflow.')
    t = Transcription(); associated = []; merged = []
    result = dict(format_version=1, content_version='batch-009-v1', source_id='src-0001',
        method='manual_visual_transcription', words=[],
        policy='第九批从PDF135 personality开始；完成范围以检查点为准。人工视觉转录，词义为编辑拆分，音标未外部核对，疑点不学习。')
    for name, end in PARTS:
        if not (ROOT/'scripts'/(name+'.py')).exists():
            break
        module = importlib.import_module(name)
        module.append(t, associated)
        through = module.COMPLETE_THROUGH
        assert through <= end
        result['words'] = t.words
        validate(result)
        assert [w['id'] for w in t.words] == [f'w{i:04}' for i in range(1216,1216+len(t.words))]
        assert all(135<=p<=155 for w in t.words for p in w['pdf_pages'])
        assert all(135<=item['pdf_page']<=155 for item in associated)
        merged.append(name)
        save('content/drafts/batch-009.json', result)
        save('content/drafts/batch-009-associated.json', dict(method='manual_visual_transcription',items=associated))
        save('content/drafts/batch-009-checkpoint.json', dict(
            status='ready_for_review' if through==154 else 'draft', completed_pages=list(range(135,through+1)),
            words=len(t.words), last_word=t.words[-1]['spelling'],
            context_pages_reviewed=sorted({p for w in t.words for p in w['pdf_pages'] if p>through}),
            next_word=module.NEXT_WORD,next_pdf_page=module.NEXT_PAGE,next_id=f'w{1216+len(t.words):04}',
            continuations=[],merged_parts=merged.copy(),note='按页保存草稿，尚未发布；第八批temper不重复导入。'))
        print(f'Saved through PDF{through}: {len(t.words)} words; next {module.NEXT_WORD}.',flush=True)
        if through < end:
            break
    return result

if __name__=='__main__':
    merge()
