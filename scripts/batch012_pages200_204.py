"""Visual transcription of headwords starting on PDF200–204."""
COMPLETE_THROUGH = 204
NEXT_WORD = 'perfect'
NEXT_PAGE = 205

def append(t, associated):
    unit = 'unit-006'
    group = '46 名声、威望相关词汇'
    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(2213+len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = unit
    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))
    def include_page(page):
        w = t.words[-1]
        w['pdf_pages'] = sorted(set(w['pdf_pages']+[page]))
        w['printed_pages'] = [f'{p-8:03}' for p in w['pdf_pages']]

    a('reputation', '/ˌrepjuˈteɪʃn/', 'n. 名声，名誉', 200,
      [('n.', '名声，名誉')],
      [(0, 'She has the reputation of being remarkably sensible and clever.', '她以非常明智和聪明而闻名。', 'reputation', '例', 200),
       (0, 'The company enjoys an international reputation for quality of design.', '该公司在设计质量方面享有国际声誉。', 'reputation', '例', 200)],
      're（重复，反复）+ put（放）+ ation（名词后缀）→他们重复地要求把你的名字放到前面，说明你的“名声”很大→名声。')
    a('prestige', '/preˈstiːʒ/', 'n. 声望，威信，威望', 200,
      [('n.', '声望，威信，威望')],
      [(0, 'The couple’s prestige was damaged by the allegations.', '这对夫妇的威信因这些指控而受损。', 'prestige', '例', 200),
       (0, 'You cannot buy class, as the old saying goes, and these upstart entrepreneurs cannot buy their prizes the prestige of the Nobels.', '正如那句老话所说，你买不到阶级，这些自命不凡的企业家也无法为他们的奖项买到诺贝尔奖那样的声望。', 'prestige', '真题', 200)],
      'pre（提前）+ stige（形似stage“舞台”）→提前上舞台的演员“威望”高→声望，威望。')
    a('esteem', '/ɪˈstiːm/', 'n. 尊重，敬重；好评；v. 尊重，敬重；把……看作；认为', 200,
      [('n.', '尊重，敬重；好评'), ('v.', '尊重，敬重'), ('v.', '把……看作；认为')],
      [(2, 'He was esteemed as a dedicated and imaginative scholar.', '他被认为是一位敬业且富有想象力的学者。', 'esteemed', '例', 200),
       (0, 'We become defensive when criticised, and apply negative stereotypes to others to boost our own esteem.', '当受到批评时，我们会变得防御，并将负面的刻板印象应用于他人以提高自己的自尊。', 'esteem', '真题', 200)],
      'est（最高级）+ ee（联想成“两只眼睛”）+ m→最大限度地睁大两只眼睛看，以表示“尊重”与“敬重”→尊重，敬重。')
    t.pending('esteem', 1, '原译自尊与原书名词尊重、敬重、好评的对应需复核，暂不直接训练尊重义。')
    a('notorious', '/nəʊˈtɔːriəs/', 'adj. 声名狼藉的，臭名昭著的', 200,
      [('adj.', '声名狼藉的，臭名昭著的')],
      [(0, 'The country is notorious for its appalling prison conditions.', '这个国家因监狱状况恶劣而臭名远扬。', 'notorious', '例', 200),
       (0, 'Today, two years after the death of the notorious dictator, the house, which he used as an office, is opening as a visitor attraction.', '如今，在这位臭名昭著的独裁者去世两年后，这座他曾用作办公室的房子开始作为游客景点开放。', 'notorious', '例', 200)],
      'no（没有）+ tori（联想成story“故事”）+ ous（形容词后缀）→身上没有什么好故事的→声名狼藉的，臭名昭著的。')
    group = '47 mono-相关词汇'
    a('monotonous', '/məˈnɒtənəs/', 'adj. 单调的，无变化的', 201,
      [('adj.', '单调的，无变化的')],
      [(0, 'She thought life in the this city was monotonous.', '她觉得这个城市的生活单调乏味。', 'monotonous', '例', 201),
       (0, 'The housewives were asked if they found housework monotonous.', '家庭主妇们被问及是否觉得家务单调。', 'monotonous', '例', 201)],
      'mono（单一的）+ ton（想成tone“音调”）+ ous（形容词后缀）→单一音调的→单调的。')
    t.pending('monotonous', 0, '原书in the this city重复限定词，按原文保留，暂待核对。')
    a('monopoly', '/məˈnɒpəli/', 'n. 垄断；被垄断的商品（或服务）；独占，专利', 201,
      [('n.', '垄断；独占'), ('n.', '被垄断的商品（或服务）'), ('n.', '专利')],
      [(0, 'One company holds a monopoly of the raw materials.', '一家公司垄断着原材料。', 'monopoly', '例', 201),
       (0, 'In recent years, railroads have been combining with each other, merging into supersystems, causing heightened concerns about monopoly.', '近年来，铁路系统一直在相互合并，形成超级系统，这加剧了人们对垄断的担忧。', 'monopoly', '真题', 201)],
      'mono（单一的）+ poly（卖）→只能从这个地方买到→垄断。',
      [('monopolise', '（美monopolize）v. 独占，垄断', 201)])
    a('policy', '/ˈpɒləsi/', 'n. 政策，方针；原则；保险单', 201,
      [('n.', '政策，方针'), ('n.', '原则'), ('n.', '保险单')],
      [(0, 'They believe that Europe needs a common foreign and security policy.', '他们认为欧洲需要采取共同的外交和安全政策。', 'policy', '例', 201),
       (0, 'For a long time, scientists and policy makers concentrated on the idea that teenagers were a problem needed to be solved.', '很长一段时间以来，科学家和政策制定者都认为青少年是一个需要解决的问题。', 'policy', '真题', 201)],
      '发音类似“魄力才”→制定大政“方针”是需要魄力的→方针。')
    t.pending('policy', 1, '原书a problem needed to be solved的句法衔接存疑，保留原句原译待核。')
    unit = 'unit-007'
    group = '01 设备、制造、手工相关词汇'
    a('facility', '/fəˈsɪləti/', 'n. 设备，设施；场所；天资', 203,
      [('n.', '设备，设施'), ('n.', '场所'), ('n.', '天资')],
      [(0, 'The hotel provides excellent facilities for children.', '这家旅馆的儿童设施十分完善。', 'facilities', '例', 203)],
      'fac（做）+ il（易于，善于）+ ity（名词后缀）→易于做事→带来便利之物→设备，设施。')
    material('local facilities', 203, '拓展', definition='当地的设施')
    a('manufacture', '/ˌmænjuˈfæktʃə(r)/', 'v. （用机器）大量生产，成批制造；捏造，编造；n. 大量制造；批量生产；工业品', 203,
      [('v.', '（用机器）大量生产，成批制造'), ('v.', '捏造，编造'), ('n.', '大量制造；批量生产'), ('n.', '工业品')],
      [(1, 'The evidence against him had been largely manufactured.', '对他不利的证据大部分是伪造的。', 'manufactured', '例', 203),
       (2, 'What is the date of manufacture?', '生产日期是哪天？', 'manufacture', '例', 203)],
      related=[('manufacturer', 'n. 生产商，制造商', 203)])
    material('manufacturer', 203, '真题', english='Either way, one benefit of a “national” organization would be to negotiate better prices, if possible, with drug manufacturers.', translation='无论哪种方式，一个全国性组织的好处是，如果有可能的话，与药品制造商谈判更优惠的价格。')
    a('manual', '/ˈmænjuəl/', 'n. 使用手册，指南；adj. 手动的；手工的；体力的', 203,
      [('n.', '使用手册，指南'), ('adj.', '手动的'), ('adj.', '手工的'), ('adj.', '体力的')],
      [(0, 'The computer comes with a 600-page instruction manual.', '电脑附有一本600页的使用指南。', 'manual', '例', 203),
       (3, 'They can avoid doing much of the manual labor.', '他们可以避免做很多体力劳动。', 'manual', '例', 203)],
      'manu（手）+ al（形容词后缀）→用手做的→手动的，手工的→手册，指南。')
    a('manipulate', '/məˈnɪpjuleɪt/', 'v. （暗中）控制，操纵，影响；操作，使用', 203,
      [('v.', '（暗中）控制，操纵，影响'), ('v.', '操作，使用')],
      [(0, 'As a politician, he knows how to manipulate public opinion.', '身为政客，他知道如何左右公众舆论。', 'manipulate', '例', 203),
       (1, 'Computers are very efficient at manipulating information.', '计算机在处理信息方面效率极高。', 'manipulating', '例', 203)],
      'man（人）+ i + pul（联想成pull“拉”）+ ate（动词后缀）→靠人拉→控制，操纵。')
    a('handy', '/ˈhændi/', 'adj. 手边的，就近的，方便的，便利的；容易做的；易使用的', 203,
      [('adj.', '手边的，就近的'), ('adj.', '方便的，便利的'), ('adj.', '容易做的'), ('adj.', '易使用的')],
      [(1, 'The arrangement was handy for both of us.', '这样安排对我们两人都很方便。', 'handy', '例', 203),
       (0, 'Always keep a first-aid kit handy.', '手边要常备急救箱。', 'handy', '例', 203)])
    a('artifact', '/ˈɑːtɪfækt/', 'n. 人工制品，手工艺品（尤指有历史或文化价值的）', 203,
      [('n.', '人工制品，手工艺品（尤指有历史或文化价值的）')],
      [(0, 'Theoretically, you may be correct in claiming that every artifact has potential scientific value.', '从理论上讲，您认为每件文物都具有潜在的科学价值可能是正确的。', 'artifact', '例', 203),
       (0, 'Certain artifacts are especially vulnerable because some pioneers in plastic art didn’t always know how to mix ingredients properly.', '因为一些塑料艺术的先驱者并不总是知道如何正确地调配各种成分，所以某些手工艺品特别脆弱。', 'artifacts', '真题', 204)],
      'art（艺术）+ i + fact（做）→做出来的艺术品→人工制品；手工艺品。')
    t.pending('artifact', 1, 'plastic art原译塑料艺术的含义需结合出处复核，保留原文原译待核。')
    group = '02 -fect-相关词汇'
    a('defect', 'n. /ˈdiːfekt/; v. /dɪˈfekt/', 'n. 缺点，缺陷；v. 背叛，叛变', 204,
      [('n.', '缺点，缺陷'), ('v.', '背叛，叛变')],
      [(0, 'The creative aspects of advertisement, for instance, often cover up the defects or problems in products.', '例如，广告的创意往往掩盖了产品的缺陷或问题。', 'defects', '例', 204),
       (0, 'Goods with slight defects are sold at half price.', '有轻微瑕疵的货品以半价出售。', 'defects', '例', 204)],
      'de（联想成“弟弟”）+ fect（做）→弟弟做事常常会有“缺陷”。',
      [('defective', 'adj. 有缺陷的；有缺点的', 204)])
    material('defective', 204, '例', english='Her hearing was found to be slightly defective.', translation='经检查，她的听力有点缺陷。')
    a('effect', '/ɪˈfekt/', 'n. 效应；影响；结果；v. 实现；引起；使发生', 204,
      [('n.', '效应'), ('n.', '影响'), ('n.', '结果'), ('v.', '实现；引起；使发生')],
      [(0, 'The results show a statistically significant effect.', '结果显示了统计上显著的效果。', 'effect', '例', 204),
       (1, 'All of which would, of course, have a positive effect on our happiness levels.', '当然，所有这些都会对我们的幸福水平产生积极的影响。', 'effect', '真题', 204)],
      'ef（加强）+ fect（做）→反复做→实现。',
      [('effective', 'adj. 有效的；产生预期效果的；实际的；生效的', 204)])
    material('effective', 204, '例', english='His hard work is effective.', translation='他的努力工作很有成效。')
    material('in effect', 204, '拓展', definition='事实上；实际上')
    material('take effect', 204, '拓展', definition='开始起作用；见效')
    a('affect', '/əˈfekt/', 'v. 影响；使感染', 204,
      [('v.', '影响'), ('v.', '使感染')],
      [(0, 'What David said has affected me a lot and I have decided to work hard.', '戴维的话对我影响很大，我已决定努力学习了。', 'affected', '例', 204),
       (0, 'More than seven million people have been affected by drought.', '七百多万人受到了干旱的影响。', 'affected', '例', 204)])
    a('affection', '/əˈfekʃn/', 'n. 喜爱，钟爱；爱情', 204,
      [('n.', '喜爱，钟爱'), ('n.', '爱情')],
      [(0, 'People of different ages and genders show affection in different ways.', '不同年龄和性别的人表达爱意的方式不同。', 'affection', '例', 204),
       (0, 'I have a great affection for Beijing.', '我很喜欢北京。', 'affection', '例', 204)])
    a('infect', '/ɪnˈfekt/', 'v. 传染，使感染；使携带病菌；使感染（某种感情、计算机病毒）', 204,
      [('v.', '传染，使感染；使携带病菌'), ('v.', '使感染（某种感情、计算机病毒）')],
      [(0, 'Two million bees were infected with the disease.', '200万只蜜蜂感染了这种疾病。', 'infected', '例', 204),
       (1, 'The whole room was soon infected by his laughter.', '整个房间很快被他的笑声感染了。', 'infected', '例', 205)],
      'in（进入）+ fect（做，制作）→病毒进入身体做事，搞事情→传染，使感染。',
      [('infection', 'n. 传染；传染病，感染', 205), ('infectious', 'adj. 传染性的，感染的', 205)])
