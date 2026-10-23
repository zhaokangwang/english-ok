"""Visually transcribed sample. IDs are assigned once, never derived from editable text."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows = []
def word(spelling, ipa, definition, page, group, meanings, examples, mnemonic='', related=(), notes=()):
    n = len(rows) + 1
    wid = f'w{n:04}'
    senses = [dict(id=f's{n:04}-{i+1:02}', pos=p, gloss=g, origin='editor_mapping', ready=False) for i,(p,g) in enumerate(meanings)]
    exs = []
    for j,(si,en,zh,target,label,ep) in enumerate(examples):
        start = en.index(target)
        exs.append(dict(id=f'e{n:04}-{j+1:02}', sense_id=senses[si]['id'], english=en, translation=zh, target=target, target_start=start, target_end=start+len(target), book_label=label, pdf_page=ep, printed_page=f'{ep-8:03}', review_status='visual_checked', note='真题标签仅据原书，年份题号未核实。' if label=='真题' else ''))
        senses[si]['ready'] = True
    rows.append(dict(id=wid, spelling=spelling, phonetic=ipa, source_definition=definition, mnemonic=mnemonic, group_name=group, pdf_pages=sorted(set([page]+[e['pdf_page'] for e in exs])), printed_pages=sorted(set([f'{page-8:03}']+[e['printed_page'] for e in exs])), review_status='visual_checked', senses=senses, examples=exs, related=[dict(id=f'r{n:04}-{i+1:02}',spelling=s,definition=d,relation='derived',pdf_page=p,note=note) for i,(s,d,p,note) in enumerate(related)], notes=list(notes)))

word('action','/ˈækʃn/','n. 行为，行动；功能，作用',10,'01 act相关词汇',[('n.','行为，行动'),('n.','功能，作用')],[(0,'Actions speak louder than words.','行胜于言。','Actions','例',10),(0,'Prior knowledge and interests influence the subsequent actions we take.','先前的知识和兴趣会影响我们接下来采取的行动。','actions','真题',10)],'act（发音类似“爱个他”）+ ion（名词后缀）→如果爱他就不要口头说，要勇敢去追，行动起来→行动。')
word('activate','/ˈæktɪveɪt/','v. 使活动；激活',10,'01 act相关词汇',[('v.','使活动；激活')],[(0,'The burglar alarm is activated by movement.','这防盗警报器一动就会响。','activated','例',10),(0,'Curiosity activates creative minds.','好奇心激发创造性思维。','activates','真题',10)])
word('active','/ˈæktɪv/','adj. 积极的，活跃的；起作用的',10,'01 act相关词汇',[('adj.','积极的，活跃的'),('adj.','起作用的')],[(0,'Playing with digital devices discourages kids from active discovery.','玩电子设备会阻碍孩子积极探索。','active','例',10),(0,'The brain is as active during REM (rapid eye movement) sleep as it is when fully awake.','大脑在快速眼动睡眠时与完全清醒时是一样活跃的。','active','真题',10)],related=[('activist','n. 积极分子',10,''),('actively','adv. 积极地；活跃地',10,'')])
word('react','/riˈækt/','v. 起化学反应；回应，作出反应',10,'01 act相关词汇',[('v.','回应，作出反应'),('v.','起化学反应')],[(0,'All students in our university react strongly to the resign of the president.','我们学校所有学生对校长辞职的反应很激烈。','react','例',10),(0,'The stock market reacts positively when companies tie CEO pay to stock prices.','当公司把股价和首席执行官的工资挂钩时，股市会作出积极反应。','reacts','真题',10)],'act（行动）+ re（回）→我们对这个地方采取行动，这个地方的人给我们作出相应的“回应”。',related=[('reaction','n. 反应；反作用力',10,''),('reactor','n. 核反应堆',10,'')],notes=['原书例句使用 the resign，疑有用词问题；保留原文，例句 e0004-01 暂不用于学习。'])
word('exact','/ɪɡˈzækt/','adj. 准确的，精确的，严谨的；v. 要求；强迫；强求',10,'01 act相关词汇',[('adj.','准确的，精确的'),('adj.','严谨的'),('v.','要求；强迫；强求')],[(0,'The colours were an almost exact match.','这些颜色几乎完全匹配。','exact','例',10),(0,'You should make shopping lists for your ingredients in their exact quantities.','你列购买原料的清单时，应当列出它们准确的数量。','exact','真题',10)],'ex（出去）+ act（行动）→警察集体外出行动时，必须有严谨的计划，精准的安排→严谨的。',related=[('exactly','adv. 精确地，准确地',10,'派生词例句未计入 exact 的掌握进度。')])
word('actual','/ˈæktʃuəl/','adj. 实际的；真正的；真实的',10,'01 act相关词汇',[('adj.','实际的；真正的；真实的')],[(0,'The actual cost was higher than we expected.','实际成本比我们预料的要高。','actual','例',11),(0,'Their methods do not attempt to estimate the actual biomass.','他们的方法不是尝试去估算实际的生物量。','actual','真题',11)],'我们要行动（act）起来，才能解决实际的（actual）问题。',related=[('actually','adv. 实际上；事实上',11,'派生词例句未计入 actual 的掌握进度。')])
word('interact','/ˌɪntərˈækt/','v. 交流，沟通；相互影响，相互作用',11,'01 act相关词汇',[('v.','交流，沟通'),('v.','相互影响，相互作用')],[(0,'He interacts very well with other children.','他和其他孩子交往得很好。','interacts','例',11)],'inter（中间，之间）+ act（行动）→两个事物之间不断地有行动→相互作用。',related=[('interaction','n. 互动，交流；相互作用',11,'原书真题使用 interactions，单独保留在转录文本中。')])
word('behave','/bɪˈheɪv/','v. 举止得体；表现',11,'02 行为相关词汇',[('v.','举止得体'),('v.','表现')],[(0,'She doesn’t know how to behave in public.','她在公共场合举止无措。','behave','例',11)],related=[('behaviour','n. 行为，举止；态度',11,'美式拼写 behavior；原书真题使用 behavior。')])
word('conduct',None,'/kənˈdʌkt/ v. 组织，安排；实施，执行；指挥；引导；传导；/ˈkɒndʌkt/ n. 行为；举止',11,'02 行为相关词汇',[('n.','行为；举止'),('v.','组织，安排'),('v.','实施，执行'),('v.','指挥；引导'),('v.','传导')],[(0,'The sport has a strict code of conduct.','这种体育运动有严格的行为规范。','conduct','例',11),(1,'The school board is responsible for conducting public hearings.','校董会负责组织公开的听证会。','conducting','真题',11)],'con（共同）+ duct（引导；带来）→引导大家共同做→指挥。',related=[('conductor','n. 指挥；售票员，检票员；导体',11,''),('semiconductor','n. 半导体',11,'派生词例句单独保存。')],notes=['按词性保留两组读音，暂放在原书释义字段，不合并为一个音标。'])
word('direct','/dəˈrekt/','v. 指导，指挥；adj. 直接的',11,'02 行为相关词汇',[('v.','指导，指挥'),('adj.','直接的')],[(0,'The project managers direct the day-to-day operations of the project.','项目经理指导项目的日常运作。','direct','例',11)],'发音类似“得绕开它”→前面有一个障碍物，不能“直接”通过，得绕开它→听着指挥走→指导，指挥。',related=[('directly','adv. 直接地',12,'派生内容跨页，例句单独保留。')])
word('ambition','/æmˈbɪʃn/','n. 野心，雄心，抱负',12,'03 action与ambition',[('n.','野心，雄心，抱负')],[(0,'His burning ambition was to study medicine.','他梦寐以求的是学医。','ambition','例',12),(0,'He left the bank in 2005 with ambitions to be a CEO.','他一心想当总裁，在2005年离开了银行。','ambitions','真题',12)],'发音类似“俺必胜”→我有必胜的决心→抱负，雄心。',related=[('ambitious','adj. 有抱负的；有雄心的',12,'')])
word('ancient','/ˈeɪnʃənt/','adj. 古代的；古老的',12,'04 旧、新相关词汇',[('adj.','古代的；古老的')],[(0,'The pyramids were built in ancient times.','金字塔建造于古代。','ancient','例',12),(0,'The town is notable for its ancient harbour.','这座小镇因其古老的港口而出名。','ancient','例',12)])
word('stale','/steɪl/','adj. 不新鲜的；（空气）污浊的；陈腐的；没有新意的；厌倦的',12,'04 旧、新相关词汇',[('adj.','不新鲜的'),('adj.','陈腐的；没有新意的'),('adj.','（空气）污浊的'),('adj.','厌倦的')],[(0,'They starved but only could eat a piece of stale bread every day.','他们饿了，但每天只能吃一块不新鲜的面包。','stale','例',12),(1,'You need to do some self-assessment to determine where you have become stale in your thinking.','你需要做一些自我评估，以确定你的思考模式中的哪些地方已经变得陈旧。','stale','例',12)],'s（蛇）+ tale（故事）→蛇的故事→关于蛇的故事太多了，如果我再讲，那就是“没有新意的”了。')
word('refresh','/rɪˈfreʃ/','v. （使）精神振作，（使）精力恢复',12,'04 旧、新相关词汇',[('v.','（使）精神振作，（使）精力恢复')],[(0,'The following morning she awoke refreshed.','第二天早上，她醒来时精神焕发。','refreshed','例',12)],'re（再）+ fresh（新鲜的）→再一次新鲜的→振作精神，恢复精力。',notes=['refreshed 是原书 refresh 词条下的分词用法；refreshing air 的句子保留为关联素材，未当成相同词义。'])
word('flesh','/fleʃ/','n. 肉；果肉；肉体；皮肤',12,'04 旧、新相关词汇',[('n.','果肉'),('n.','肉；肉体；皮肤')],[(0,'The flesh of the peach is sweet and juicy.','桃子的果肉甜而多汁。','flesh','例',12),(0,'The flesh of this apple is fresh.','这个苹果的果肉很新鲜。','flesh','例',12)],'这些果肉（flesh）看起来非常新鲜（fresh）。')
word('renew','/rɪˈnjuː/','v. 更新；重新开始',12,'04 旧、新相关词汇',[('v.','重新开始'),('v.','更新')],[(0,'We have to renew our efforts to attract young players.','我们只好重新开始努力吸引年轻队员。','renew','例',12),(1,'These labels encourage style-conscious consumers to see clothes as disposable and to renew their wardrobe every few weeks.','这些品牌鼓励那些有时尚意识的消费者把衣服看作一次性的消费品，并且鼓励他们每隔几周就更新他们的衣柜。','renew','真题',13)])
word('restore','/rɪˈstɔː(r)/','v. 恢复，修复；归还',13,'04 旧、新相关词汇',[('v.','恢复，修复'),('v.','归还')],[(0,'The operation restored his sight.','手术使他恢复了视力。','restored','例',13),(0,'Trust is easily destroyed and hugely expensive to restore.','信任很容易被摧毁，但是恢复需要花费巨大的代价。','restore','真题',13)],'病人休息（rest）得好，才能慢慢恢复（restore）身体。',related=[('restoration','n. 整修；恢复，归还',13,'派生词例句单独保留。')])
word('storage','/ˈstɔːrɪdʒ/','n. 贮藏（空间），贮存',13,'04 旧、新相关词汇',[('n.','贮藏（空间），贮存')],[(0,'There’s a lot of storage space in the loft.','阁楼上有很大的存储空间。','storage','例',13),(0,'But a boost in the storage capacity of batteries is making their ability to keep power flowing around the clock more likely.','但是，电池存储容量的提升正使其更有可能能够昼夜不停地持续供电。','storage','真题',13)],related=[('store','n. 商店；仓库；v. 贮藏，贮存',13,'原书标记为“拓展”，不是派生。')])
word('renovate','/ˈrenəveɪt/','v. 修复，翻新；重新粉刷',13,'04 旧、新相关词汇',[('v.','修复，翻新'),('v.','重新粉刷')],[(0,'They spent the summer renovating the farmhouse.','他们花了一个夏天翻新农舍。','renovating','例',13)],'re（再）+ nov（=new“新的”）+ ate（动词后缀）→再次使它变成“新的”→翻新。',related=[('renovation','n. 整修，翻新',13,'')])
word('innovate','/ˈɪnəveɪt/','v. 创新；革新',13,'04 旧、新相关词汇',[('v.','创新；革新')],[(0,'The company can once again innovate its way out of tough economic times.','该公司可以再次创新，走出经济困难时期。','innovate','例',13)],'in（表加强）+ nov（=new“新的”）+ ate（动词后缀）→使它变得新一些→创新；革新。',related=[('innovation','n. 创造；创新；改革',13,'原书真题的目标是 innovation，不直接作为 innovate 的学习例句。')])

# Hold suspicious original wording for review without silently correcting the book.
rows[3]['examples'][0]['review_status'] = 'pending'
rows[3]['examples'][0]['note'] = '原书 the resign 用法待核实；不进入学习队列。'
rows[17]['related'][0]['relation'] = 'extension'
data = dict(format_version=1, content_version='sample-0.1.0', source_id='src-0001', method='manual_visual_transcription', words=rows,
    policy='释义原文保留在 source_definition；senses 为编辑按语境拆分，非原书逐项分类。音标为视觉转录并统一重音符号，未作外部词典复核。无音频。')
dest=ROOT/'content'/'sample.json'
dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Wrote {len(rows)} main words to {dest}')
