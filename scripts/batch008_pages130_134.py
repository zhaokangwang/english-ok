"""Visually reviewed fourth-unit headwords beginning on PDF130–134."""
COMPLETE_THROUGH = 134
NEXT_WORD = 'personality'
NEXT_PAGE = 135

def append(t, associated):
    group = '26 respond相关词汇'

    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(1105 + len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-004'

    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))

    def include_page(page):
        w = t.words[-1]
        w['pdf_pages'] = sorted(set(w['pdf_pages'] + [page]))
        w['printed_pages'] = [f'{p-8:03}' for p in w['pdf_pages']]

    a('responsible', '/rɪˈspɒnsəbl/', 'adj. 需要负责任的，应负责任的', 130,
      [('adj.', '需要负责任的，应负责任的')],
      [(0, 'Mike is responsible for designing the entire project.', '迈克负责设计全部工程。', 'responsible', '例', 130),
       (0, 'To serve as responsible stewards of the planet, we must press forward on deeper atmospheric and oceanic research.', '作为地球的负责任的管理者，我们必须推进对大气和海洋的更深层次的研究。', 'responsible', '真题', 130)],
      'respons（回答，回应）+ ible（能……的）→能够给出回答、回应的人是有责任心的，是可靠的→有责任的，可靠的。',
      [('responsibility', 'n. 责任，负责', 130)])
    material('responsibility', 130, '例', english='It’s time for someone to take responsibility and get the job done.', translation='是时候有人承担责任，完成工作了。')
    a('correspond', '/ˌkɒrəˈspɒnd/', 'v. 相一致，相符合；类似于，相当于；通信', 130,
      [('v.', '相一致，相符合'), ('v.', '类似于，相当于'), ('v.', '通信')],
      [(0, 'Your account of events does not correspond with hers.', '你对事情的陈述与她说的不相符。', 'correspond', '例', 130),
       (1, 'The word corresponds roughly in meaning to our “homesickness”.', '这个词的意思大致相当于我们的“思乡”一词。', 'corresponds', '例', 130)],
      'cor（一起）+ respond（回应，反应）→大家一起回应，异口同声→相符合，相一致。',
      [('correspondence', 'n. 信件（=letters）；相似；通信', 130), ('corresponding', 'adj. 相应的，一致的', 130)])
    material('correspondence', 130, '真题', english='comprehensive records of recent correspondence', translation='近期通信往来的详尽记录', status='quarantined', reason='原书为短语残片，非完整例句，保留关联资料不进入学习队列。')
    material('corresponding', 130, '真题', english='Such a view would require a corresponding shift in the way US society views fire, researchers say.', translation='研究者说，这样的观念需要当今美国社会相应地转变对火灾的看法。')
    group = '27 phase形近词及相关近义词'
    a('phase', '/feɪz/', 'n. 阶段，时期；v. 分阶段进行；逐步做', 130,
      [('n.', '阶段，时期'), ('v.', '分阶段进行；逐步做')],
      [(0, 'This technology is still in an early phase of development.', '这项技术仍处于早期开发阶段。', 'phase', '例', 130),
       (0, 'It is not easy to talk about the role of the mass media in this overwhelmingly significant phase in European history.', '要谈论大众媒体在欧洲历史上这个极其重要的阶段所扮演的角色并不容易。', 'phase', '真题', 130)],
      '发音类似“肥死”→我太胖（肥）了，需要减肥，但减肥不能太快，需要分“阶段”进行→阶段。')
    include_page(131)
    a('phrase', '/freɪz/', 'n. 短语，词组，惯用语；成语；v. 表达，措辞', 131,
      [('n.', '短语，词组，惯用语；成语'), ('v.', '表达，措辞')],
      [(0, 'He just comes out with the same old stock phrases.', '他总说那些同样的陈词滥调。', 'phrases', '例', 131),
       (0, 'There are colourful words and phrases in English.', '英语里有丰富多彩的单词和短语。', 'phrases', '例', 131)],
      '学习短语（phrase）要分阶段（phase）进行。')
    a('feasible', '/ˈfiːzəbl/', 'adj. 可行的，行得通的', 131,
      [('adj.', '可行的，行得通的')],
      [(0, 'At first this did not seem like a feasible suggestion.', '起初，这似乎不是一个可行的建议。', 'feasible', '例', 131),
       (0, 'Sounds great but how feasible is this vision?', '听起来很棒，但这一愿景的可行性如何？', 'feasible', '真题', 131)],
      'feas（做）+ ible（形容词后缀）→可以做的→可行的。')
    a('likely', '/ˈlaɪkli/', 'adj. 可能的；有希望的', 131,
      [('adj.', '可能的'), ('adj.', '有希望的')],
      [(0, 'Tickets are likely to be expensive.', '入场券可能很贵。', 'likely', '例', 131),
       (0, 'You’re more likely to be heard if you can connect your disagreement to a higher purpose.', '如果你能把你的不同意见与一个更高的目标结合起来，你的意见更有可能被倾听。', 'likely', '真题', 131)],
      related=[('likelihood', 'n. 可能，可能性', 131)])
    material('likelihood', 131, '例', english='There is very little likelihood of that happening.', translation='几乎没有发生那种事情的可能。')
    material('unlike', 131, '拓展', definition='adj. 不同的，不相似的；prep. 不像；与……不同')
    material('unlike', 131, '例', english='They are both teachers. Otherwise they are quite unlike.', translation='他们俩都是教师。除此之外他们迥然不同。')
    material('alike', 131, '拓展', definition='adj. 相像的，相似的；adv. 十分相像地')
    material('alike', 131, '例', english='They tried to treat all their children alike.', translation='他们尽量对他们的孩子一视同仁。')
    material('likewise', 131, '拓展', definition='adv. 同样地，也')
    material('likewise', 131, '例', english='He voted for the change and he expected his colleagues to do likewise.', translation='他投票赞成变革并期望他的同事投同样的票。')
    a('probable', '/ˈprɒbəbl/', 'adj. 可能的；n. 可能入选者', 131,
      [('adj.', '可能的'), ('n.', '可能入选者')],
      [(0, 'The two outcomes are equally probable.', '两种结果都同样有可能。', 'probable', '例', 131)],
      related=[('probability', 'n. 可能性；可能发生的事情', 131)])
    material('probability', 131, '例', english='A fall in interest rates is a strong probability in the present economic climate.', translation='在目前的经济形势下，降低利率大有可能。')
    group = '28 初始相关语境词汇'
    a('dawn', '/dɔːn/', 'n. 黎明；开端；v. 开始', 131,
      [('n.', '黎明'), ('n.', '开端'), ('v.', '开始')],
      [(0, 'I woke up just before dawn.', '我正好在拂晓前醒来。', 'dawn', '例', 131),
       (1, 'Peace marked a new dawn in the country’s history.', '和平使这个国家的历史翻开了新的一页。', 'dawn', '例', 132)],
      '黎明（dawn）的时候他们开始在山下（down）走了。')
    a('dusk', '/dʌsk/', 'n. 黄昏，傍晚', 132,
      [('n.', '黄昏，傍晚')],
      [(0, 'The street lights go on at dusk.', '街灯在黄昏时分亮起来。', 'dusk', '例', 132),
       (0, 'She arrived home as dusk was falling.', '黄昏降临时，她回到了家。', 'dusk', '例', 132)],
      '黄昏（dusk）时，他们把鸭子（duck）赶回了鸭舍。')
    a('launch', '/lɔːntʃ/', 'n. 发射；上市；发起；v. 发射；发动，发起；发行', 132,
      [('v.', '发动，发起'), ('v.', '发行'), ('v.', '发射'), ('n.', '发射'), ('n.', '上市'), ('n.', '发起')],
      [(0, 'Police have launched an investigation into the incident.', '警方已对该事件展开调查。', 'launched', '例', 132),
       (1, 'The updated website will be officially launched at the conference in April.', '更新后的网站将在4月份的会议上正式推出。', 'launched', '例', 132)],
      '科学家们吃完午饭（lunch）就准备进行火箭的发射（launch）啦。')
    a('initiate', '/ɪˈnɪʃieɪt/', 'v. 开始，发起，创始；使了解，传授', 132,
      [('v.', '开始，发起，创始'), ('v.', '使了解，传授')],
      [(0, 'He initiated a national debate on reform.', '他发起了一场关于改革的全国性讨论。', 'initiated', '例', 132),
       (0, 'The government has initiated a programme of economic reform.', '政府已开始实施经济改革方案。', 'initiated', '例', 132)],
      'in（进入）+ it（走）+ i + ate（动词后缀）→走进去→开始，发起。',
      [('initiative', 'n. 倡议；主动性，积极性；主动权', 132), ('initial', 'adj. 开始的，最初的；n. （姓名的）首字母', 132)])
    group = '29 陪伴相关词汇'
    a('companion', '/kəmˈpænjən/', 'n. 同伴，朋友；陪护', 132,
      [('n.', '同伴，朋友'), ('n.', '陪护')],
      [(0, 'He was a good friend, a dependable companion.', '他是个好朋友，一个可以信赖的同伴。', 'companion', '例', 132),
       (0, 'Would passengers feel comfortable traveling in companion?', '乘客在结伴飞行时会感到舒适吗？', 'companion', '真题', 132)])
    t.pending('companion', 1, '原书in companion搭配存疑，保留原文待核，不进入学习队列。')
    a('accompany', '/əˈkʌmpəni/', 'v. 陪伴；伴随；为……伴奏', 132,
      [('v.', '陪伴'), ('v.', '伴随'), ('v.', '为……伴奏')],
      [(0, 'His wife accompanied him on the trip.', '那次旅行他由妻子陪同。', 'accompanied', '例', 132),
       (1, 'The text is accompanied by a series of stunning photographs.', '正文附有一系列令人惊叹的照片。', 'accompanied', '例', 132)],
      '他陪伴（accompany）公司（company）的领导出席这次宴会。',
      [('accompanying', 'adj. 陪伴的；附随的', 132)])
    group = '30 估计相关词汇'
    a('reckon', '/ˈrekən/', 'v. 估算；计算；认为', 132,
      [('v.', '认为'), ('v.', '估算'), ('v.', '计算')],
      [(0, 'I reckon (that) I’m going to get that job.', '我认为我会得到那份工作。', 'reckon', '例', 132),
       (1, 'This time experts reckon that prices are about 40% down on their peak on average.', '这一次，专家估计，价格平均比峰值下降了40%左右。', 'reckon', '真题', 132)])
    a('reckless', '/ˈrekləs/', 'adj. 鲁莽的，不顾后果的', 133,
      [('adj.', '鲁莽的，不顾后果的')],
      [(0, 'He had always been reckless with money.', '他花钱总是大手大脚。', 'reckless', '例', 133),
       (0, 'She was a good rider, but reckless.', '她是个好骑手，但太鲁莽。', 'reckless', '例', 133)],
      'reck（计算）+ less（否定后缀）→不计后果的→鲁莽的。',
      [('recklessly', 'adv. 鲁莽地；不顾后果地', 133)])
    a('estimate', 'v. /ˈestɪmeɪt/; n. /ˈestɪmət/', 'v. 估计；估价；估算；n. 估计；估价', 133,
      [('v.', '估计；估价；估算'), ('n.', '估计；估价')],
      [(0, 'Police estimate the crowd at 30,000.', '警方估计聚集的人有3万。', 'estimate', '例', 133),
       (0, 'It is estimated (that) the project will last four years.', '据估计，这项工程将用时四年。', 'estimated', '例', 133)],
      'est（最高级）+ i（我）+ m + ate（动词后缀）→我干什么能赚到最多钱，我得“估算”一下→估算；估计。',
      [('overestimate', 'v. 高估', 133), ('underestimate', 'v. 低估', 133)])
    material('underestimate', 133, '真题', english='It is easy to underestimate English writer James Herriot.', translation='人们很容易低估英国作家詹姆斯·赫里奥特。')
    group = '31 -mate相关词汇'
    a('intimate', '/ˈɪntɪmət/', 'adj. 亲密的，亲近的；私人的', 133,
      [('adj.', '亲密的，亲近的'), ('adj.', '私人的')],
      [(0, 'We’re not on intimate terms with our neighbours.', '我们和邻居来往不多。', 'intimate', '例', 133)],
      'inti（在心里面）+ mate（人）→能放在心里的人，一般是很“亲密的”→亲密的。',
      [('intimately', 'adv. 密切地', 133)])
    material('intimate friends', 133, '拓展', definition='密友')
    a('ultimate', '/ˈʌltɪmət/', 'adj. 最后的，最终的；根本的；n. 极品；精华', 133,
      [('adj.', '最后的，最终的'), ('adj.', '根本的'), ('n.', '极品；精华')],
      [(0, 'The ultimate decision lies with the parents.', '最后的决定权握在父母手中。', 'ultimate', '例', 133),
       (0, 'War is the ultimate failure of public communication.', '战争是政治沟通最终失败的结果。', 'ultimate', '例', 133)],
      '发音类似“奥特曼的”→不到最后时刻，奥特曼不会出来→最终的，最后的。',
      [('ultimately', 'adv. 最终，最后，终归', 133)])
    material('ultimately', 133, '真题', english='The most challenging moments in life are getting married, starting a family and ultimately retiring.', translation='生活中最具挑战性的时刻是结婚、成家和最终退休。')
    a('approximate', '/əˈprɒksɪmət/', 'adj. 近似的，大约的；v. 近似，接近', 133,
      [('adj.', '近似的，大约的'), ('v.', '近似，接近')],
      [(0, 'The cost given is only approximate.', '所列成本仅是约计。', 'approximate', '例', 133)],
      '结婚前，他不断地接近（approximate）他的女朋友（mate），最后两个人才开始交往，直到结婚。',
      [('approximately', 'adv. 大约，近似', 133)])
    material('approximately', 134, '真题', english='Still, Jefferson freed Hemings’s children—though not Hemings herself or his approximately 150 other slaves.', translation='尽管如此，杰斐逊还是释放了海明斯的孩子们，虽然没有释放海明斯本人和其他大约150名奴隶。')
    include_page(134)
    a('climate', '/ˈklaɪmət/', 'n. 气候（区）；环境气氛', 134,
      [('n.', '气候（区）'), ('n.', '环境气氛')],
      [(0, 'We need to adjust to this changing climate.', '我们需要适应这种不断变化的气候。', 'climate', '例', 134),
       (1, 'They hope this will provide the right climate for social change.', '他们希望这将为社会变革提供合适的环境。', 'climate', '例', 134)],
      '我估计（estimate）明天的天气（climate）应该不错。')
    group = '32 周围、氛围、情绪相关词汇'
    a('surround', '/səˈraʊnd/', 'v. 包围，环绕；n. （物品的）框，饰边；周围', 134,
      [('v.', '包围，环绕'), ('n.', '（物品的）框，饰边'), ('n.', '周围')],
      [(0, 'The garden is surrounded by a wall.', '花园被一堵墙包围着。', 'surrounded', '例', 134),
       (0, 'If you are surrounded by problems and cannot stop thinking about the past, try to focus on the present moment.', '如果你被问题包围且无法停止回想过去，那就努力专注于当下吧。', 'surrounded', '真题', 134)],
      'sur（在……下面）+ round（圆圈）→在下面围一圈→包围，环绕。',
      [('surroundings', 'n. 环境', 134)])
    material('surroundings', 134, '例', english='His paintings try to capture the beauty of the surroundings.', translation='他的画试图捕捉周围环境的美。')
    a('atmosphere', '/ˈætməsfɪə(r)/', 'n. 大气，大气层；气氛，氛围', 134,
      [('n.', '气氛，氛围'), ('n.', '大气，大气层')],
      [(0, 'This type of lighting creates a relaxing atmosphere.', '这种类型的照明创造了一种放松的氛围。', 'atmosphere', '例', 134),
       (1, 'The Earth’s atmosphere is definitely warming.', '毫无疑问，地球气候正在变暖。', 'atmosphere', '真题', 134)])
    t.pending('atmosphere', 1, '原书把atmosphere译作气候，与所列大气义不一致，保留原文待核。')
    a('mood', '/muːd/', 'n. 情绪；气氛，氛围', 134,
      [('n.', '气氛，氛围'), ('n.', '情绪')],
      [(0, 'He threw in some jokes to lighten the mood.', '他讲了一些笑话来缓和气氛。', 'mood', '例', 134),
       (1, 'For instance, one of the apps the students are developing suggests movies based on your mood.', '例如，学生们正在开发的一个应用程序会根据你的心情推荐电影。', 'mood', '真题', 134)],
      '我心情（mood）不好的时候就喜欢晚上静静地看月亮（moon）。')
    a('temper', '/ˈtempə(r)/', 'n. 脾气，性情；怒气；v. 使缓和', 134,
      [('n.', '脾气，性情'), ('n.', '怒气'), ('v.', '使缓和')],
      [(0, 'He must learn to control his temper.', '他必须学会控制自己的脾气。', 'temper', '例', 134),
       (2, 'Sales have been lagging for months as shoppers temper their spending.', '随着购物者削减开支，销售额几个月来一直在下滑。', 'temper', '真题', 134)],
      '有时候温度（temperature）一高，人的脾气（temper）也会随之变得暴躁。',
      [('bad-tempered', 'adj. 易怒的，爱发脾气的', 134)])
    material('lose / keep one’s temper', 134, '拓展', definition='发脾气／忍住怒火')
