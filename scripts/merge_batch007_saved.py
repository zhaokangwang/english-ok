"""Resume the seventh batch in source order, saving a checkpoint after every part."""
import importlib
import json
import os
from pathlib import Path
from build_data import validate
from content_pipeline import identities, guard_identities
from transcription_helpers import Transcription

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / 'content/drafts'
PARTS = [('batch007_pages095_099', 99), ('batch007_pages100_104', 104),
         ('batch007_pages105_109', 109), ('batch007_pages110_114', 114)]

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def save(path, data):
    stage = path.with_suffix(path.suffix + '.staging')
    stage.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.replace(stage, path)

def merge():
    plan = read(ROOT / 'content/import-plan.json')
    if any(b['id']=='batch-007' and b['status']=='imported' for b in plan['approved_batches']):
        raise SystemExit('batch-007 is already complete; preserve its published checkpoint.')
    result = read(ROOT / 'content/transcripts/batch-007-initial.json')
    assert [(w['id'], w['spelling']) for w in result['words']] == [('w1000','coordinate'), ('w1001','subordinate')]
    old = read(ROOT / 'content/batches/batch-007.json')
    result['content_version'] = 'batch-007-v2'
    result['policy'] = '第七批PDF95–114，按保存检查点记录实际完成范围；不重编号已导入词；人工视觉转录，疑点待核对，音标未外部复核。'
    t = Transcription()
    t.words = result['words']
    for w in t.words:
        w['book_unit_id'] = 'unit-003'
        w['notes'] = ['此词此前作为第七批两词小样本导入；音标未外部词典复核。'
                      if note.startswith('第七批小样本：') else note for note in w['notes']]
    associated = []
    merged = []
    for name, end in PARTS:
        module_path = ROOT / 'scripts' / (name + '.py')
        if not module_path.exists():
            break
        module = importlib.import_module(name)
        module.append(t, associated)
        through = module.COMPLETE_THROUGH
        assert through <= end
        result['words'] = t.words
        if through == 114:
            result['policy'] = '第七批PDF95 coordinate至114 detect共105主词，末词续至115；第三单元收尾及第四单元开头。人工视觉转录，词义为编辑拆分，音标未外部核对，疑点单独保留不学习。'
        validate(result)
        assert [w['id'] for w in t.words] == [f'w{i:04}' for i in range(1000, 1000+len(t.words))]
        assert all(95 <= p <= 115 for w in t.words for p in w['pdf_pages'])
        assert all(95 <= a['pdf_page'] <= 115 for a in associated)
        merged.append(name)
        save(DRAFT / 'batch-007.json', result)
        save(DRAFT / 'batch-007-associated.json', dict(method='manual_visual_transcription', items=associated))
        save(DRAFT / 'batch-007-checkpoint.json', dict(
            status='ready_for_review' if through==114 else 'draft',
            completed_pages=list(range(95,through+1)), reviewed_pages=list(range(95,through+1)),
            context_pages_reviewed=sorted({p for w in t.words for p in w['pdf_pages'] if p>through}),
            words=len(t.words), last_word=t.words[-1]['spelling'], next_word=module.NEXT_WORD,
            next_pdf_page=module.NEXT_PAGE, next_id=f'w{1000+len(t.words):04}',
            continuations=[], merged_parts=merged.copy(),
            note='按主词起始页归属；只保存已完成段，不表示已经发布。第六批缺口独立保留。'))
        print(f'Saved through PDF{through}: {len(t.words)} words; next {module.NEXT_WORD}.', flush=True)
        if through < end:
            break
    guard_identities(identities(old), identities(result))
    print('Draft validated; all previously published batch-007 identities preserved.')
    return result

if __name__ == '__main__':
    merge()
