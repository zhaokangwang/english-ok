"""Merge saved batch006 material, preserving the explicitly unfinished PDF82–85 gap."""
import importlib
import json
import os
from pathlib import Path
from build_data import validate
from transcription_helpers import Transcription

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / 'content/drafts'
BASE = ROOT / 'content/transcripts/batch-006-pages076-081.json'
BASE_ASSOCIATED = ROOT / 'content/transcripts/batch-006-pages076-081-associated.json'
MISSING = [('obstacle',81),('hamper',82),('display',82),('exhibit',82),('prohibit',82),
    ('forbid',82),('ban',83),('formidable',83),('awe',83),('plausible',83),('deploy',83),
    ('employment',84),('plot',84),('engage',84),('marital',84),('pregnant',84),('divorce',84),
    ('spouse',85),('household',85),('uphold',85),('hoist',85),('heir',85),('heritage',85)]

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def save(path, data):
    stage = path.with_suffix(path.suffix + '.staging')
    stage.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.replace(stage, path)

def merge():
    if not BASE.exists():
        current = read(DRAFT / 'batch-006.json')
        assert len(current['words']) == 34 and current['words'][-1]['spelling'] == 'hinder'
        save(BASE, current)
        save(BASE_ASSOCIATED, read(DRAFT / 'batch-006-associated.json'))
    result = read(BASE)
    t = Transcription()
    t.words = result['words']
    associated = read(BASE_ASSOCIATED)['items']
    for item in associated:
        if item.get('word') == 'nutritious' and item.get('translation') == '调整你的常饮食习惯，使之更富有营养。':
            item['translation'] = '调整你的日常饮食习惯，使之更富有营养。'
            item['note'] = '依据PDF77补回此前转录遗漏的“日”字。'
    for module in ('batch006_pages086_089', 'batch006_pages090_094'):
        importlib.import_module(module).append(t, associated)
    # The saved modules allocate relative IDs. Reserve the missing 23 source words
    # before these unpublished records, leaving the original 34 identities intact.
    for w in t.words[34:]:
        old = w['id'][1:]
        new = f'{int(old) + len(MISSING):04}'
        w['id'] = 'w' + new
        for s in w['senses']:
            s['id'] = s['id'].replace('s' + old + '-', 's' + new + '-', 1)
        for e in w['examples']:
            e['id'] = e['id'].replace('e' + old + '-', 'e' + new + '-', 1)
            e['sense_id'] = e['sense_id'].replace('s' + old + '-', 's' + new + '-', 1)
        for r in w['related']:
            r['id'] = r['id'].replace('r' + old + '-', 'r' + new + '-', 1)
    result['words'] = t.words
    result['policy'] = '第六批部分导入：仅已保存的76–81及86–94页起始83词；82–85页23词缺失（含81/86页衔接）。缺失内容不编补；senator续至95。人工视觉转录，音标未外部复核。'
    validate(result)
    expected = [f'w{i:04}' for i in list(range(346,380)) + list(range(403,452))]
    assert [w['id'] for w in t.words] == expected
    assert all(76 <= page <= 95 for w in t.words for page in w['pdf_pages'])
    assert all(76 <= item['pdf_page'] <= 95 for item in associated)
    missing = [dict(reserved_id=f'w{380+i:04}', spelling=word, starts_on_pdf_page=page,
        status='not_transcribed_not_imported') for i,(word,page) in enumerate(MISSING)]
    save(DRAFT / 'batch-006.json', result)
    save(DRAFT / 'batch-006-associated.json', dict(method='manual_visual_transcription', items=associated))
    save(DRAFT / 'batch-006-missing.json', dict(reason='输出流错误使82–85页转录未完成；本清单仅记录缺口，不是正式词条。', items=missing))
    save(DRAFT / 'batch-006-checkpoint.json', dict(status='ready_for_partial_import',
        completed_pages=list(range(76,81)) + list(range(87,95)),
        reviewed_pages=list(range(76,82)) + list(range(86,96)), pending_pages=list(range(81,87)),
        continuations=['obstacle自PDF81开始、heritage续至86；这23个主词均未转录或导入。'],
        words=len(t.words), last_word='senator', next_id='w0380', next_word='obstacle', next_pdf_page=81,
        completed_word_ids=expected, missing_word_ids=[item['reserved_id'] for item in missing],
        missing_file='content/drafts/batch-006-missing.json',
        note='部分数据可导入，不能标全批完成。coordinate/subordinate保留第七批w1000/w1001。'))
    print(f'Saved {len(t.words)} reviewed words; {len(missing)} words remain explicitly missing.')
    print('Senses:', sum(len(w['senses']) for w in t.words),
          'examples:', sum(len(w['examples']) for w in t.words),
          'ready:', sum(s['ready'] for w in t.words for s in w['senses']),
          'pending:', sum(e['review_status']=='pending' for w in t.words for e in w['examples']))
    return result

if __name__ == '__main__':
    merge()
