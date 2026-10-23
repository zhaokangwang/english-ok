"""One-time visual transcription of two PDF95 headwords, not the full batch."""
import json
from pathlib import Path
from transcription_helpers import Transcription

ROOT = Path(__file__).resolve().parents[1]
t = Transcription()
group = '30 ordinate相关词汇'
t.add(1000, 'coordinate', '/kəʊˈɔːdɪneɪt/', 'v. 使协调；使相配合；协调；搭配', 95, group,
      [('v.', '使协调；协调'), ('v.', '使相配合；搭配')],
      [(0, 'They appointed a new manager to coordinate the work of the team.',
        '为协调这个团队的工作，他们任用了一位新经理。', 'coordinate', '例', 95),
       (1, 'The bed linen coordinates with the bedroom curtains.',
        '床单和卧室的窗帘很相配。', 'coordinates', '例', 95)],
      'co（一起）+ ordinate（联想成ordinary“普通的，一般的”）→我们都是普通人，要一起配合才能把工作做好→协调；使相配合。',
      [('coordinator', 'n. 协调者', 95)])
t.add(1001, 'subordinate', '/səˈbɔːdɪnət/', 'n. 下级，部属；adj. 下级的，从属的；次要的；v. 使从属于', 95, group,
      [('n.', '下级，部属'), ('adj.', '下级的，从属的'), ('adj.', '次要的'), ('v.', '使从属于')],
      [(1, 'The individual’s needs are subordinate to those of the group.',
        '个人需求从属于集体需求。', 'subordinate', '例', 95),
       (0, 'You’re seen not as a disagreeable subordinate but as a colleague who’s trying to advance a common objective.',
        '你不会被看作是一个话不投机的下属，而是会被视为一个努力推进共同目标的同事。', 'subordinate', '真题', 95)],
      'sub（在下面）+ ordinate（联想成ordinary“普通的，一般的”）→在普通之下的→下级的→下级，部属。')
for word in t.words:
    word['notes'].append('第七批小样本：仅PDF95的coordinate和subordinate；本批及第三单元均未全部收录。音标未外部词典复核。')
result = dict(format_version=1, content_version='batch-007-sample-v1', source_id='src-0001',
              method='manual_visual_transcription', words=t.words,
              policy='PDF95两词人工视觉核对的小样本；第六批仍未导入。词义由编辑拆分；缺对应例句的词义不进入学习队列。')
draft = ROOT / 'content/drafts'
draft.mkdir(exist_ok=True)
for filename, data in [
    ('batch-007.json', result),
    ('batch-007-associated.json', dict(method='manual_visual_transcription', items=[])),
    ('batch-007-checkpoint.json', dict(status='sample_ready_for_review',
        completed_pages=[], reviewed_pages=[95],
        completed_words=['coordinate', 'subordinate'], words=2,
        last_word='subordinate', next_word='cancel', next_pdf_page=95,
        word_ids=['w1000', 'w1001'], next_id='w1002',
        continuations=[], note='只完成两个词；第95页仍有未处理主词，不标整页完成。第六批保留原检查点。'))]:
    destination = draft / filename
    if destination.exists():
        raise SystemExit(f'Refusing to overwrite an existing draft: {destination}')
    destination.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Saved batch-007 draft: 2 words, 6 senses, 4 examples; next cancel on PDF95.')
