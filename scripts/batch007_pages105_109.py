"""Visual transcription of headwords beginning on PDF105–109."""

COMPLETE_THROUGH = 109
NEXT_WORD = 'incline'
NEXT_PAGE = 111


def append(t, associated):
    group = '45 腐烂相关词汇'

    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(1000 + len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-003'

    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))

    def include_page(page):
        w = t.words[-1]
        w['pdf_pages'] = sorted(set(w['pdf_pages'] + [page]))
        w['printed_pages'] = [f'{p-8:03}' for p in w['pdf_pages']]

    a('decay', '/dɪˈkeɪ/', 'n. & v. 衰退，衰减；腐烂，腐朽', 105,
      [('n.', '衰退，衰减'), ('n.', '腐烂，腐朽'), ('v.', '衰退，衰减'), ('v.', '腐烂，腐朽')],
      [(0, 'Radioactive decay happens at a constant rate regardless of exposure to air.', '无论是否暴露在空气中，放射性衰变都以恒定的速率发生。', 'decay', '例', 105),
       (2, 'In zones of increased turbulence, the planes’ wakes will decay more quickly and the effect will diminish.', '在湍流增强的区域，飞机的尾流会消失得更快，它的效果也会减弱。', 'decay', '真题', 105)],
      'de（向下）+ cay（落下）→向下掉落→衰退。')
    a('erode', '/ɪˈrəʊd/', 'v. 腐蚀；风化；逐渐毁坏；削弱', 105,
      [('v.', '腐蚀；风化；逐渐毁坏'), ('v.', '削弱')],
      [(0, 'The rocks have eroded away over time.', '这些石头随着时间的推移逐渐风化了。', 'eroded', '例', 105),
       (1, 'The experience had seriously eroded his confidence in himself.', '这次经历严重挫伤了他的自信心。', 'eroded', '例', 105)],
      'e（外面）+ rode（联想成rock“岩石”）→岩石的外面容易被侵蚀→侵蚀，腐蚀；削弱。')
    group = '46 拥护相关词汇'
    a('advocate', '/ˈædvəkət/ n.; /ˈædvəkeɪt/ v.', 'n. 提倡者，拥护者；v. 提倡，拥护；主张；支持', 105,
      [('n.', '提倡者，拥护者'), ('v.', '提倡，拥护；主张；支持')],
      [(0, 'She became a firm advocate of overseas ventures.', '她成为海外投资的坚定支持者。', 'advocate', '例', 105),
       (1, 'In Beethoven’s music, he advocated freedom of thought and of personal expression.', '贝多芬在他的音乐中倡导思想和个人表达的自由。', 'advocated', '真题', 105)],
      'ad（表加强）+ voc（声音，喊叫）+ ate（动词后缀）→大声喊叫→主张；提倡。',
      [('advocation', 'n. 拥护，支持', 105)])
    a('following', '/ˈfɒləʊɪŋ/', 'n. 拥护者，追随者；adj. 后面的，接着的；下列的', 105,
      [('adj.', '后面的，接着的'), ('adj.', '下列的'), ('n.', '拥护者，追随者')],
      [(0, 'They arrived on Monday evening and we got there the following day.', '他们是星期一晚上到的，我们次日也抵达那里。', 'following', '例', 105),
       (2, 'The band has a huge following in Italy.', '这个乐队在意大利有一大批热心的追随者。', 'following', '例', 105)])
    group = '47 引起相关词汇'
    a('provoke', '/prəˈvəʊk/', 'v. 激起，引起；刺激；激怒', 105,
      [('v.', '激起，引起'), ('v.', '刺激；激怒')],
      [(0, 'The article was intended to provoke discussion.', '这篇文章旨在引发讨论。', 'provoke', '例', 105),
       (0, 'Unhappy parents rarely are provoked to wonder if they shouldn’t have had kids.', '不幸福的父母很少会反思自己是否不该生孩子。', 'provoked', '真题', 106)],
      'pro（向前）+ vok（叫喊；声音）+ e→在别人前面叫喊，容易刺激到别人→激怒；刺激。')
    a('trigger', '/ˈtrɪɡə(r)/', 'v. 引发，引起，触发；n. 扳机', 106,
      [('v.', '引发，引起，触发'), ('n.', '扳机')],
      [(0, 'Nuts can trigger off a violent allergic reaction.', '坚果可以引起严重的过敏反应。', 'trigger', '例', 106),
       (0, 'Eye contact triggered more activity associated with avoidance.', '眼神接触会引发更多与回避相关的活动。', 'triggered', '真题', 106)],
      '你是害怕老虎（tiger）呢？还是更害怕扣着“扳机”（trigger）的坏人呢？')
    a('evoke', '/ɪˈvəʊk/', 'v. 唤起，引起；博得', 106,
      [('v.', '唤起，引起'), ('v.', '博得')],
      [(0, 'These images are likely to evoke a strong response in the viewers.', '这些图像很可能会在观众中产生强烈反响。', 'evoke', '例', 106),
       (0, 'The music evoked memories of her youth.', '这乐曲勾起了她对青年时代的回忆。', 'evoked', '例', 106)],
      'e（出去）+ vok（声音）+ e→向外发出声音→唤起，引起。')
    group = '48 stir相关语境词汇'
    a('stir', '/stɜː(r)/', 'v. 搅拌；激起，引起；n. 搅拌；激动，震动；愤怒', 106,
      [('v.', '搅拌'), ('v.', '激起，引起'), ('n.', '激动，震动'), ('n.', '搅拌；愤怒')],
      [(0, 'She stirred her tea.', '她搅了搅茶。', 'stirred', '例', 106),
       (2, 'Since I started posting them on Twitter they have been causing quite a stir.', '自从我把它们发布在Twitter上，它们就引起了不小的轰动。', 'stir', '真题', 106)])
    a('blend', '/blend/', 'v. 混合，融合；n. 混合物', 106,
      [('v.', '混合，融合'), ('n.', '混合物')],
      [(0, 'Blend the flour with the milk to make a smooth paste.', '把面粉和牛奶调成均匀的面糊。', 'Blend', '例', 106),
       (0, 'Their music blends traditional and modern styles.', '他们的音乐融合了传统和现代风格。', 'blends', '例', 106)],
      'b（发音类似“不”）+ lend（借）→不借他→别把你的书借给他，他会把你的书和别人的书混在一起，搞不清楚→混合。')
    a('turbulent', '/ˈtɜːbjələnt/', 'adj. 动荡的，混乱的；汹涌的；猛烈的', 106,
      [('adj.', '汹涌的；猛烈的'), ('adj.', '动荡的，混乱的')],
      [(0, 'The aircraft is designed to withstand turbulent conditions.', '这架飞机是为经受猛烈的气流而设计的。', 'turbulent', '例', 106),
       (1, 'But particularly when viewed against America’s turbulent past, today’s social indices hardly suggest a dark and deteriorating social environment.', '但尤其是与美国动荡不安的过去相比，如今的社会指数几乎不能说明美国的社会环境正变得黑暗，或是在恶化。', 'turbulent', '真题', 106)],
      related=[('turbulence', 'n. 骚乱，动荡，混乱', 106)])
    group = '49 protest相关形近词汇'
    a('protest', '/ˈprəʊtest/', 'n. & v. 抗议，反对', 106,
      [('v.', '抗议，反对'), ('n.', '抗议，反对')],
      [(0, 'They were taken away protesting loudly.', '他们大声抗议，被带走了。', 'protesting', '例', 107),
       (1, 'This has resulted in protests from social scientists.', '这引发了社会科学家的抗议。', 'protests', '真题', 107)],
      'pro（提前）+ test（考试）→考试突然提前了，大家都反对这件事→反对，抗议。')
    a('detest', '/dɪˈtest/', 'v. 厌恶，讨厌', 107,
      [('v.', '厌恶，讨厌')],
      [(0, 'I loathe and detest racism in any form.', '我厌恶和憎恶任何形式的种族主义。', 'detest', '例', 107)],
      '弟弟（de）对考试（test）是什么态度？当然是讨厌考试了→厌恶，讨厌。')
    a('contest', '/ˈkɒntest/ n.; /kənˈtest/ v.', 'n. 竞争，争夺；比赛，竞赛；v. 争辩，提出异议；争取赢得', 107,
      [('v.', '争辩，提出异议'), ('v.', '争取赢得'), ('n.', '竞争，争夺；比赛，竞赛')],
      [(0, 'The divorce was not contested.', '这桩离婚案没有人提出异议。', 'contested', '例', 107),
       (2, 'In 1995 the CIA held a contest to see who could compile the most data about Burundi.', '1995年，中央情报局举办了一场比赛，看谁能收集到关于布隆迪的最多数据。', 'contest', '真题', 107)],
      'con（一起；都）+ test（考试）→当我们都考试的时候，我们之间的关系就是“竞争”关系。',
      [('contestant', 'n. 竞争者，争论者', 107)])
    a('context', '/ˈkɒntekst/', 'n. 背景；环境；上下文；语境', 107,
      [('n.', '背景；环境'), ('n.', '上下文；语境')],
      [(0, 'Such databases are being used in a wide range of contexts.', '这类数据库广泛应用于各种场合。', 'contexts', '例', 107),
       (1, 'You begin to infer a context for the text, for instance, by making decisions about what kind of speech event is involved.', '例如，你可以通过判定文本涉及何种类型的语言情景，来推测文章的语境。', 'context', '真题', 107)],
      'con（所有的）+ text（文章）→所有的文章都有写作的“背景”→背景；语境，上下文。')
    group = '50 出现、消失相关词汇'
    a('appearance', '/əˈpɪərəns/', 'n. 露面；出现；外表，外观，外貌；出版；广播', 107,
      [('n.', '露面；出现'), ('n.', '外表，外观，外貌'), ('n.', '出版；广播')],
      [(1, 'We must avoid any appearance of impropriety.', '我们必须避免出现任何不当的行为。', 'appearance', '例', 107),
       (1, 'They should be quick to respond to letters to the editor, lest animal rights misinformation go unchallenged and acquire a deceptive appearance of truth.', '他们应该对报刊的读者来信及时做出反应，以防让动物权利的误导言论在毫无质疑的情况下横行，从而获得一副欺骗性的真理的面容。', 'appearance', '真题', 107)])
    t.pending('appearance', 0, '原译将appearance of impropriety译为实际不当行为，未体现给人以不当印象的表象含义；保留原文与原译待复核。')
    a('disappear', '/ˌdɪsəˈpɪə(r)/', 'v. 消失，不见；失踪；完全消失', 107,
      [('v.', '消失，不见；完全消失'), ('v.', '失踪')],
      [(0, 'The problem won’t just disappear.', '这个问题不会就这样不了了之的。', 'disappear', '例', 107),
       (0, 'Although many worker shortages had disappeared, not all had done so.', '尽管许多劳动力短缺问题已经消失，但并非所有问题都是如此。', 'disappeared', '真题', 107)],
      related=[('disappearance', 'n. 消失，不见', 108), ('reappear', 'v. 再次出现', 108)])
    include_page(108)
    a('evaporate', '/ɪˈvæpəreɪt/', 'v. （使）蒸发；消失，衰减', 108,
      [('v.', '（使）蒸发'), ('v.', '消失，衰减')],
      [(0, 'Heat until all the water has evaporated.', '加热直至水全部蒸发。', 'evaporated', '例', 108),
       (1, 'The job security that the US economy once offered to high school graduates has largely evaporated.', '美国经济曾经提供给高中毕业生的工作保障很大程度上已经消失了。', 'evaporated', '真题', 108)],
      'e（表示“出去”）+ vapor（发音类似“外婆”）+ ate（动词后缀）→他的外婆有老年痴呆，出去后走丢了，再也没回来→消失。')
    group = '51 当你了解更多，会有更多选择'
    a('acquaint', '/əˈkweɪnt/', 'v. 使熟悉，使了解', 108,
      [('v.', '使熟悉，使了解')],
      [(0, 'Let me acquaint you with the facts.', '让我把事实告诉你。', 'acquaint', '例', 108)],
      'ac（表示“加强”）+ quai（发音类似“怪”）+ nt→我们中国有句老话叫“见怪不怪”，意思是见得多了就不奇怪了，见得多了不就“熟悉”了吗？→使熟悉，使了解。',
      [('acquaintance', 'n. 熟人；（与某人）认识，略有交情；（对某事物的）了解', 108)])
    material('acquaintance', 108, '真题', english='It does not take a lifelong acquaintance to pick up various software programs.', translation='学会各种软件程序并不需要花半生的时间。', status='quarantined', reason='lifelong acquaintance与原译花半生的时间存在语义差异，保留原文与原译待复核；不是acquaint主词动词例句。', continuation_pdf_page=109)
    material('acquaintance', 109, '真题', english='For a social epidemic to occur, however, each person so affected must then influence his or her own acquaintances.', translation='然而，要使一种社会流行现象发生，每个受影响的人必须影响他或她自己的熟人。')
    include_page(109)
    group = '52 选择相关词汇'
    a('prone', '/prəʊn/', 'adj. 易于遭受；有做……倾向的', 108,
      [('adj.', '易于遭受'), ('adj.', '有做……倾向的')],
      [(0, 'Working without a break makes you more prone to error.', '连续工作不停歇使你更容易出错。', 'prone', '例', 108),
       (1, 'We are prone to snap overreactions.', '我们很容易作出瞬时的过度反应。', 'prone', '真题', 108)],
      'pro（向前）+ ne（呢）→想要向前走呢→有做……倾向的。')
    a('apt', '/æpt/', 'adj. 易于，有……倾向的；恰当的，适宜的', 108,
      [('adj.', '易于，有……倾向的'), ('adj.', '恰当的，适宜的')],
      [(1, 'The song would have been more apt for a bass voice.', '这首歌更适合男低音。', 'apt', '例', 108),
       (0, 'Babies are apt to put objects into their mouths.', '婴儿爱把东西往嘴里塞。', 'apt', '例', 108)],
      '这只猿猴（ape）有扑倒它的倾向（apt）。')
    a('opt', '/ɒpt/', 'v. 选择，挑选', 108,
      [('v.', '选择，挑选')],
      [(0, 'After graduating she opted for a career in music.', '毕业后她选择了从事音乐工作。', 'opted', '例', 108),
       (0, 'Many workers opted to leave their jobs rather than take a pay cut.', '许多工人宁愿离职也不接受减薪。', 'opted', '例', 108)],
      '发音类似“我扑他”→我扑向他，就是我选择他→选择，挑选。',
      [('option', 'n. 供选择的事物；选择（权）', 109)])
    include_page(109)
    material('option', 109, '例', english='There are various options open to you.', translation='你有多种选择。')
    a('optional', '/ˈɒpʃənl/', 'adj. 可选择的，选修的', 109,
      [('adj.', '可选择的，选修的')],
      [(0, 'Certain courses are compulsory; others are optional.', '有些课程是必修的，其他是选修的。', 'optional', '例', 109),
       (0, 'It is said that in England death is pressing, in Canada inevitable and in California optional.', '据说在英国死亡是紧迫的，在加拿大死亡是不可避免的，而在加利福尼亚死亡是可以选择的。', 'optional', '真题', 109)])
    a('compulsory', '/kəmˈpʌlsəri/', 'adj. （因法律或规则而）必须做的，强制的，强迫的', 109,
      [('adj.', '（因法律或规则而）必须做的，强制的，强迫的')],
      [(0, 'English is a compulsory subject at this level.', '英语在这一级别是必修科目。', 'compulsory', '例', 109),
       (0, 'It is compulsory for all motorcyclists to wear helmets.', '所有骑摩托车的人都必须戴头盔，这是强制性的。', 'compulsory', '例', 109)],
      'com（表示“加强”）+ puls（推动）+ ory（形容词后缀）→一直推动去做的→必须做的，强制的。')
    a('discipline', '/ˈdɪsəplɪn/', 'n. 训练；纪律；学科；知识领域', 109,
      [('n.', '训练'), ('n.', '纪律'), ('n.', '学科；知识领域')],
      [(1, 'She keeps good discipline in class.', '她严格执行课堂纪律。', 'discipline', '例', 109),
       (2, 'Scholars from various disciplines have been working on these problems.', '来自不同领域的学者一直致力于解决这些问题。', 'disciplines', '例', 109)],
      'dis（不）+ cip（抓住，拿）+ line（线）→不拿老百姓的一针一线，这是铁的“纪律”。')
    material('compulsory disciplines', 109, '拓展', definition='必修课')
    material('optional disciplines', 109, '拓展', definition='选修课')
    material('self-discipline', 109, '拓展', definition='自律')
    a('principal', '/ˈprɪnsəpl/', 'adj. 最重要的，主要的；n. 校长', 109,
      [('n.', '校长'), ('adj.', '最重要的，主要的')],
      [(0, 'The regulations have been opposed by local high school principals.', '这些规定受到地方高中校长们的反对。', 'principals', '例', 109),
       (1, 'The United States is the product of two principal forces.', '美国是两种主要力量的产物。', 'principal', '真题', 109)],
      'princi（联想成prince“王子”）+ pa（发音类似“怕”）→王子也有怕（pal）的人，是谁？→校长。')
    a('principle', '/ˈprɪnsəpl/', 'n. 法则；原理；（道德）原则', 109,
      [('n.', '法则'), ('n.', '原理'), ('n.', '（道德）原则')],
      [(0, 'There are three fundamental principles of teamwork.', '团队合作有三个基本原则。', 'principles', '例', 109),
       (1, 'When applied to aircraft, the principles are not substantially different.', '当这些原理应用于飞机时，它们并没有本质区别。', 'principles', '例', 109)],
      '即便是校长（principal）也要受到法则（principle）的约束。')
    material('in principle', 109, '拓展', definition='原则上；大体上')
