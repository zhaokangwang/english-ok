"""Visual transcription of sixth-unit headwords beginning on PDF190–194."""
COMPLETE_THROUGH = 194
NEXT_WORD = 'refuse'
NEXT_PAGE = 195

def append(t, associated):
    group = '29 闪耀、发光相关词汇'
    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(2104+len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-006'
    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))
    def include_page(page):
        w=t.words[-1]
        w['pdf_pages']=sorted(set(w['pdf_pages']+[page]))
        w['printed_pages']=[f'{p-8:03}' for p in w['pdf_pages']]

    a('sparkle', '/ˈspɑːkl/', 'n. 闪烁的光；亮点；v. 闪烁，闪耀；神采飞扬', 190,
      [('n.', '闪烁的光'), ('n.', '亮点'), ('v.', '闪烁，闪耀'), ('v.', '神采飞扬')],
      [(0, 'The sky went dark and the sea lost its sparkle.', '天空变暗了，大海失去了光彩。', 'sparkle', '例', 190),
       (2, 'Her jewellery sparkled in the light.', '灯光下，她的首饰光彩熠熠。', 'sparkled', '例', 190)],
      's（嘶嘶的响声）+ park（公园）+ le→节日里公园嘶嘶的声音就是有人在放烟火→闪烁，闪耀。')
    a('twinkle', '/ˈtwɪŋkl/', 'n. 闪烁；闪亮；欣喜的神情；v. 闪烁，闪耀', 190,
      [('v.', '闪烁，闪耀'), ('n.', '欣喜的神情'), ('n.', '闪烁；闪亮')],
      [(0, 'Stars twinkled in the sky.', '星星在天空中闪烁。', 'twinkled', '例', 190),
       (1, 'He looked at me with a twinkle in his eye.', '他目光熠熠地望着我。', 'twinkle', '例', 190)],
      '儿时的一首歌：twinkle twinkle little star→闪一闪亮晶晶→闪烁。')
    a('radiate', '/ˈreɪdieɪt/', 'v. 辐射，放射；显出，流露', 190,
      [('v.', '显出，流露'), ('v.', '辐射，放射')],
      [(0, 'He radiated self-confidence and optimism.', '他显得自信乐观。', 'radiated', '例', 190),
       (1, 'The hot stars radiate energy.', '灼热的恒星发射出能量。', 'radiate', '例', 190)],
      'radi（光线）+ ate（动词后缀）→发出光线→发射（光或热）。',
      [('radiation', 'n. 辐射；放射线', 190), ('radiant', 'adj. 灿烂的；辐射的，喜气洋洋的；容光焕发的，面色红润的', 190)])
    material('radiant', 190, '例', english='She was radiant with health.', translation='她身体健康，容光焕发。')
    a('flash', '/flæʃ/', 'n. 闪光，闪耀；闪光灯；快讯；v. 闪光，使闪耀；突然想到', 190,
      [('n.', '闪光，闪耀'), ('n.', '闪光灯'), ('n.', '快讯'), ('v.', '闪光，使闪耀'), ('v.', '突然想到')],
      [(0, 'Flashes of light were followed by an explosion.', '阵阵闪光后就是一声爆炸的巨响。', 'Flashes', '例', 190),
       (3, 'Start crossing when the green WALK sign starts to flash.', '当绿色步行标志开始闪烁时，开始通过。', 'flash', '例', 190)],
      '我们在夜间拍照时，可能会被问需不需要开闪光（flash）。',
      [('flasher', 'n. （车用）闪光灯，闪光装置', 190)])
    material('a flash of lightning', 190, '拓展', definition='一道闪电')
    group = '30 fiction相关词汇'
    a('fiction', '/ˈfɪkʃn/', 'n. 小说；虚构的故事', 190,
      [('n.', '小说；虚构的故事')],
      [(0, 'He is a fiction writer.', '他是位小说家。', 'fiction', '例', 191),
       (0, 'And so he reads everything from encyclopedias to science fiction novels.', '所以他什么都读，从百科全书到科幻小说。', 'fiction', '真题', 191)],
      '发音类似“飞可神”→想象一个画面，每个人都像神一样飞起来了，现实生活中不会发生吧，这应该是在“小说”中发生的事情→小说。')
    a('junction', '/ˈdʒʌŋkʃn/', 'n. 接合点；交叉路口；汇合处', 191,
      [('n.', '汇合处'), ('n.', '交叉路口'), ('n.', '接合点')],
      [(0, 'There’s a bridge at the junction of the two rivers.', '两河的汇合处有座桥。', 'junction', '例', 191),
       (1, 'It was near the junction of City Road and Old Street.', '那是在城市路与老街的交叉路口附近。', 'junction', '例', 191)],
      '在交叉路口（junction）不要上蹿下跳（jump），很危险。')
    a('novel', '/ˈnɒvl/', 'n. （长篇）小说；adj. 新颖的，珍奇的', 191,
      [('adj.', '新颖的，珍奇的'), ('n.', '（长篇）小说')],
      [(0, 'It tried to implement a novel financial aid program.', '它试图实施一项新的财政援助计划。', 'novel', '例', 191),
       (0, 'The plan sounded rather novel.', '这个计划听上去挺有新意。', 'novel', '例', 191)],
      'nov（=new“新的”）+ el→新的东西→新颖的。',
      [('novelty', 'n. 新奇；新奇的事物', 191)])
    material('novelty',191,'真题',english='Novelty itself frequently provokes disbelief.',translation='新奇的事物本身经常引起怀疑。')
    a('mystery', '/ˈmɪstri/', 'n. 神秘的人或物；奥秘', 191,
      [('n.', '神秘的人或物'), ('n.', '奥秘')],
      [(0, 'There was a mystery guest on the programme.', '节目中有位神秘嘉宾。', 'mystery', '例', 191),
       (1, 'It is one of the great unsolved mysteries of this century.', '这是本世纪尚未解开的大奥秘之一。', 'mysteries', '例', 191)],
      related=[('mysterious', 'adj. 神秘的；奇怪的', 191)])
    t.pending('mystery',0,'mystery guest中的定语修饰指身份未知，原书名词神秘的人或物的映射需复核，暂不训练。')
    material('mysterious',191,'例',english='The whole thing was very mysterious.',translation='整件事非常神秘。')
    group = '31 碎、小相关词汇'
    a('fragment', '/ˈfræɡmənt/', 'n. 碎片；片段；v. （使）破碎，分裂', 191,
      [('n.', '碎片；片段'), ('v.', '（使）破碎，分裂')],
      [(0, 'She could recall only fragments of his poetry.', '她只能回忆起他诗歌的片段。', 'fragments', '例', 191),
       (1, 'Frequent explosions caused the chalk to fragment.', '频繁的爆炸导致粉笔碎裂。', 'fragment', '例', 191)],
      '这个花瓶是易碎的（fragile），稍不留意可能就摔成碎片（fragment）了。')
    a('fragile', '/ˈfrædʒaɪl/', 'adj. 易碎的；易损的；脆弱的；虚弱的；精细的', 191,
      [('adj.', '易碎的；易损的'), ('adj.', '脆弱的；虚弱的'), ('adj.', '精细的')],
      [(0, 'Be careful not to drop it; it’s very fragile.', '小心别把它摔了，它很容易碎。', 'fragile', '例', 191),
       (1, 'The economy remains extremely fragile.', '经济仍然极其脆弱。', 'fragile', '例', 191)])
    a('fraction', '/ˈfrækʃn/', 'n. 小部分；少量；一点儿；分数', 191,
      [('n.', '小部分；少量；一点儿'), ('n.', '分数')],
      [(0, 'She hesitated for the merest fraction of a second.', '她略微犹豫了一下。', 'fraction', '例', 191),
       (0, 'An old saying has it that half of all advertising budgets are wasted—the trouble is, no one knows which half. In the internet age, at least in theory, this fraction can be much reduced.', '常言道，一半的广告预算都被浪费了——问题是，没人知道是哪一半。在互联网时代，至少在理论上，被浪费的这部分可以大大降低。', 'fraction', '真题', 191)],
      '小部分（fraction）的行动（action）也是有意义的。')
    include_page(192)
    group = '32 摩擦、冲突相关词汇'
    a('friction', '/ˈfrɪkʃn/', 'n. 摩擦（力）；不和；争执；分歧', 192,
      [('n.', '不和；争执；分歧'), ('n.', '摩擦（力）')],
      [(0, 'I’m exhausted from the constant friction between my boss and my colleagues.', '老板和同事之间不断的摩擦搞得我筋疲力尽。', 'friction', '例', 192),
       (1, 'Rubbing the stones together produces friction.', '石头相互摩擦会产生摩擦力。', 'friction', '例', 192)])
    a('conflict', 'v. /kənˈflɪkt/; n. /ˈkɒnflɪkt/', 'v. 冲突；抵触；n. 冲突；争执，争论；矛盾；战斗', 192,
      [('v.', '冲突；抵触'), ('n.', '冲突；争执，争论'), ('n.', '矛盾'), ('n.', '战斗')],
      [(0, 'The results of the new research would seem to conflict with existing theories.', '这项新研究的结果似乎与现有的理论相冲突。', 'conflict', '例', 192),
       (0, 'There are several major areas where their interests conflict.', '他们在几个主要领域存在利益冲突。', 'conflict', '例', 192)])
    group = '33 实践、理论相关词汇'
    a('practically', '/ˈpræktɪkli/', 'adv. 实际上；几乎；差不多', 192,
      [('adv.', '几乎；差不多'), ('adv.', '实际上')],
      [(0, 'My essay is practically finished now.', '我的论文现在差不多写完了。', 'practically', '例', 192),
       (0, 'Practically every week features at least one celebrity mom, or mom-to-be, smiling on the newsstands.', '几乎每周都至少有一位明星妈妈或准妈妈微笑着出现在报摊上。', 'Practically', '真题', 192)])
    a('virtual', '/ˈvɜːtʃuəl/', 'adj. 实质上的；虚拟的；模拟的', 192,
      [('adj.', '虚拟的；模拟的'), ('adj.', '实质上的')],
      [(0, 'You can also take a virtual tour of the museum.', '你也可以虚拟参观博物馆。', 'virtual', '例', 192),
       (0, 'The best uses of 3D printers and virtual reality haven’t been invented yet.', '3D打印机和虚拟现实的最佳用途还没有发明出来。', 'virtual', '真题', 192)],
      related=[('virtually', 'adv. 事实上；几乎；实质上', 192)])
    material('virtually',192,'真题',english='Unfortunately, these critics are virtually forgotten.',translation='不幸的是，这些评论家几乎被遗忘了。')
    a('theory', '/ˈθɪəri/', 'n. 理论，原理；学说', 192,
      [('n.', '理论，原理'), ('n.', '学说')],
      [(0, 'She has written a book explaining the theory behind her art.', '她写了一本书解释她艺术背后的理论。', 'theory', '例', 192),
       (0, 'This is your chance to put theory into practice.', '这是你将理论付诸实践的机会。', 'theory', '例', 192)])
    group = '34 查明、证书相关词汇'
    a('ascertain', '/ˌæsəˈteɪn/', 'v. 查明，弄清楚', 192,
      [('v.', '查明，弄清楚')],
      [(0, 'I ascertained that the driver was not badly hurt.', '我已查清，驾驶员伤势不重。', 'ascertained', '例', 193),
       (0, 'It can be difficult to ascertain the facts.', '可能难以查明事实真相。', 'ascertain', '例', 193)],
      'as（表示“加强”）+ certain（确信，必然的）→一再地确信→查明，弄清楚。')
    a('certify', '/ˈsɜːtɪfaɪ/', 'v. 证明，证实；颁发（或授予）专业资格证书', 193,
      [('v.', '证明，证实'), ('v.', '颁发（或授予）专业资格证书')],
      [(0, 'He handed her a piece of paper certifying (that) she was in good health.', '他递给她一份证明其健康状况良好的文件。', 'certifying', '例', 193),
       (0, 'The accounts were certified (as) correct by the finance department.', '账目经财务部门证实无误。', 'certified', '例', 193)],
      related=[('certification', 'n. 证明；鉴定', 193)])
    a('certificate', 'n. /səˈtɪfɪkət/; v. /səˈtɪfɪkeɪt/', 'n. 证明，证明书；文凭；结业证书；v. 发给结业证书；（尤指）发给职业培训证书', 193,
      [('n.', '证明，证明书'), ('n.', '文凭；结业证书'), ('v.', '发给结业证书；（尤指）发给职业培训证书')],
      [(0, 'She showed her certificate of insurance.', '她出示了她的保险证明。', 'certificate', '例', 193)])
    material('a birth/marriage/death certificate',193,'拓展',definition='出生/结婚/死亡证明')
    a('licence', '/ˈlaɪsns/', 'n. 执照，许可证；放肆，放纵', 193,
      [('n.', '执照，许可证'), ('n.', '放肆，放纵')],
      [(0, 'Her licence was revoked by the court.', '她的执照被法院吊销了。', 'licence', '例', 193),
       (0, 'Applicants must hold a valid driver’s licence.', '申请者必须持有有效的驾照。', 'licence', '例', 193)],
      '发音类似“来审视”→他去车管所审一下驾照→执照。')
    t.words[-1]['notes'].append('原书并列美式license，保留licence为主词，不重复建词条。')
    a('diploma', '/dɪˈpləʊmə/', 'n. 文凭课程，毕业文凭；毕业证', 193,
      [('n.', '文凭课程'), ('n.', '毕业文凭；毕业证')],
      [(0, 'My younger brother is taking a diploma in management studies.', '我弟弟在攻读管理学文凭课程。', 'diploma', '例', 193),
       (1, 'The university awards diplomas in higher education.', '大学颁发高等教育文凭。', 'diplomas', '例', 193)],
      '发音类似“弟扑了妈”→弟弟大学顺利毕业了，拿到了“毕业证”，于是他激动地扑向了妈妈→毕业证书。')
    a('diplomat', '/ˈdɪpləmæt/', 'n. 外交官；善于交际的人', 193,
      [('n.', '外交官'), ('n.', '善于交际的人')],
      [(0, 'They are two of the world’s most prominent diplomats.', '他们是世界上最杰出的外交官中的两位。', 'diplomats', '例', 193)],
      '他拿到大学毕业证（diploma）后，立志成为一名外交官（diplomat）。',
      [('diplomatic', 'adj. 外交的；有手腕的', 193)])
    material('diplomatic',193,'例',english='Attempts are being made to settle the dispute by diplomatic means.',translation='正在努力通过外交途径解决争端。')
    group = '35 复合、复杂相关词汇'
    a('compound', 'n. & adj. /ˈkɒmpaʊnd/; v. /kəmˈpaʊnd/', 'n. 复合物；混合物；复合词；adj. 复合的；v. 使加重；由……构成；混合', 193,
      [('adj.', '复合的'), ('n.', '复合物；混合物'), ('n.', '复合词'), ('v.', '使加重'), ('v.', '由……构成'), ('v.', '混合')],
      [(0, 'A compound sentence contains two or more clauses.', '复合句包含两个或多个从句。', 'compound', '例', 193),
       (1, 'The air smelled like a compound of diesel and petrol fumes.', '空气闻起来像是柴油和汽油混在一起发出的强烈气味。', 'compound', '例', 193)])
    include_page(194)
    a('complex', '/ˈkɒmpleks/', 'adj. 复杂的；难懂的；复合的', 194,
      [('adj.', '复杂的'), ('adj.', '难懂的'), ('adj.', '复合的')],
      [(0, 'We live in an increasingly complex world.', '我们生活在一个日益复杂的世界。', 'complex', '例', 194),
       (0, 'She managed to put over a fairly complex argument in a brilliantly simple way.', '她设法用极为简洁的方式将一个相当复杂的论证阐释清楚。', 'complex', '例', 194)])
    a('complicate', '/ˈkɒmplɪkeɪt/', 'v. 使复杂化；使恶化', 194,
      [('v.', '使复杂化'), ('v.', '使恶化')],
      [(0, 'I do not wish to complicate the task more than is necessary.', '我不想使这项任务不必要地复杂化。', 'complicate', '例', 194),
       (0, 'These events will greatly complicate the situation.', '这些事件将使局势变得极其复杂。', 'complicate', '例', 194)],
      'com（全部）+ pli（折叠）+ cate（表示形容词）→全部折叠的→使复杂化。',
      [('complicated', 'adj. 复杂的，难懂的', 194)])
    t.words[-1]['notes'].append('原书助记中cate被说明为表示形容词，与主释义v.不一致；原样留存助记，词性按主释义和例句录入动词。')
    group = '36 困惑相关词汇'
    a('perplex', '/pəˈpleks/', 'v. 使困惑；迷惑', 194,
      [('v.', '使困惑；迷惑')],
      [(0, 'They were perplexed by her response.', '她的答复令他们困惑不解。', 'perplexed', '例', 194),
       (0, 'The new tax laws perplex me.', '新的税收法律使我很困惑。', 'perplex', '例', 194)],
      'per（每一个）+ plex（联想成complex“复杂的”）→每一个都复杂→使困惑。',
      [('perplexed', 'adj. 困惑的；迷惑不解的', 194)])
    material('perplexed',194,'例',english='We are all perplexed as to how this happened.',translation='我们都对这事是如何发生的感到困惑不已。')
    a('puzzle', '/ˈpʌzl/', 'n. 迷，智力游戏；拼图；不解之谜；疑问；v. 迷惑，（使）困惑', 194,
      [('n.', '智力游戏'), ('v.', '迷惑，（使）困惑'), ('n.', '拼图'), ('n.', '不解之谜；疑问')],
      [(0, 'This is a book of puzzles for children.', '这是一本儿童谜语书。', 'puzzles', '例', 194),
       (1, 'This question has puzzled scientists for decades.', '这个问题已经困惑科学家数十载。', 'puzzled', '例', 194)],
      '发音类似“趴着”→这个孩子在地面上趴着玩“拼图”→拼图。',
      [('puzzling', 'adj. 令人迷惑的，令人费解的', 194)])
    t.words[-1]['notes'].append('原书首个名词释义作“迷”，疑为“谜”的字形或排印问题；源释义原样保留，编辑义项只采用明列的智力游戏等释义。')
    group = '37 fuse相关词汇'
    a('confuse', '/kənˈfjuːz/', 'v. 使糊涂；使困惑；（将……）混淆，混同', 194,
      [('v.', '使糊涂；使困惑'), ('v.', '（将……）混淆，混同')],
      [(0, 'These two sets of statistics are guaranteed to confuse the public.', '这两套统计数据肯定会把公众搞糊涂。', 'confuse', '例', 194),
       (1, 'Be careful not to confuse quantity with quality.', '注意不要把数量与质量混淆了。', 'confuse', '例', 194)],
      'con（共同）+ fus（流）+ e→流到一起→（将……）混淆。',
      [('confusion', 'n. 混乱局面；混淆；困惑', 194), ('confusing', 'adj. 令人困惑的，难以理解的', 194)])
