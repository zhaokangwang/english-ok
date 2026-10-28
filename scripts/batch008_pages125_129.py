"""Visual transcription of headwords starting on PDF125–129."""
COMPLETE_THROUGH = 129
NEXT_WORD = 'responsible'
NEXT_PAGE = 130

def append(t, associated):
    group = '20 活力相关词汇'
    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(1105 + len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-004'
    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))
    def include_page(page):
        w=t.words[-1]
        w['pdf_pages']=sorted(set(w['pdf_pages']+[page]))
        w['printed_pages']=[f'{p-8:03}' for p in w['pdf_pages']]

    a('energetic', '/ˌenəˈdʒetɪk/', 'adj. 精力充沛的，充满活力的，积极的', 125,
      [('adj.', '精力充沛的，充满活力的，积极的')],
      [(0, 'She seems remarkably energetic for a woman of her age.', '对她那个年龄的女性来说，她显得活力十足。', 'energetic', '例', 125),
       (0, 'They are energetic participants in a global economy driven by the flow of work, money, and ideas.', '受工作、资金和观念潮流的驱使，他们成为全球经济的积极参与者。', 'energetic', '真题', 125)],
      'energ（联想成energy“能量，活力”）+ et + ic（形容词后缀）→精力充沛的，积极的。')
    a('vigorous', '/ˈvɪɡərəs/', 'adj. 精力充沛的；强壮的', 125,
      [('adj.', '精力充沛的；强壮的')],
      [(0, 'Take vigorous exercise for several hours a week.', '每周做几个小时剧烈运动。', 'vigorous', '例', 125),
       (0, 'This plant is a vigorous grower.', '这种植物生长旺盛。', 'vigorous', '例', 125)],
      '发音类似“喂个肉”→妈妈给他喂肉吃，所以他的身体还算比较强壮→强壮的。')
    t.pending('vigorous', 0, '本句vigorous修饰exercise，原译为“剧烈”，原书主释义只列精力充沛、强壮；不强行挂入，待补义核对。')
    t.pending('vigorous', 1, '本句vigorous指植物生长旺盛，原书主释义只列精力充沛、强壮；不强行挂入，待补义核对。')
    material('vigour',125,'拓展',definition='（美vigor）n. 精力，活力')
    material('vigour',125,'例',english='She was a wonderful, bubbly girl, full of vigour.',translation='她是个了不起的女孩，乐天活泼，活力四射。')
    a('dynamic', '/daɪˈnæmɪk/', 'adj. 动态的；发展变化的；充满活力的；精力充沛的，动力的；n. 动力；力学', 125,
      [('adj.', '充满活力的；精力充沛的'), ('adj.', '动态的；发展变化的'), ('adj.', '动力的'), ('n.', '动力；力学')],
      [(0, 'He was a dynamic young advertising executive.', '他年轻、精力充沛，是广告公司的管理人员。', 'dynamic', '例', 125),
       (0, 'The business has managed to change and remain dynamic.', '该企业设法做到了既发展变化又活力依旧。', 'dynamic', '例', 125)],
      'dy（大雁，汉语拼音缩写）+ na（拿）+ mic（麦克风）→大雁拿着麦克风→大雁是个非常内向的人，但是只要拿着麦克风，站在讲台上，她就像换了个人一样→精力充沛的，充满活力的。')
    group = '21 -titude相关词汇'
    a('altitude', '/ˈæltɪtjuːd/', 'n. 海拔，海拔高度；高处；高地', 125,
      [('n.', '海拔，海拔高度；高处；高地')],
      [(0, 'We are flying at an altitude of 6,000 metres.', '我们的飞行高度是6000米。', 'altitude', '例', 125),
       (0, 'Snow leopards live at high altitudes.', '雪豹生活在海拔高的地区。', 'altitudes', '例', 125)],
      '有的人说态度（attitude）决定了你的高度（altitude）。')
    a('latitude', '/ˈlætɪtjuːd/', 'n. 纬度（地区）；选择的自由', 125,
      [('n.', '纬度（地区）'), ('n.', '选择的自由')],
      [(0, 'These birds only survive in temperate latitudes.', '这些鸟只在温带才能存活。', 'latitudes', '例', 125),
       (1, 'Their managers enjoy wide latitude to make hiring decisions.', '他们的经理在用人方面享有广泛的自主权。', 'latitude', '例', 125)],
      '这个地方纬度（latitude）高，海拔（altitude）也高。')
    group = '22 标本相关词汇'
    a('sample', '/ˈsɑːmpl/', 'n. （抽查的）样本，样品；v. 体验，尝试；抽样检验', 126,
      [('n.', '（抽查的）样本，样品'), ('v.', '体验，尝试'), ('v.', '抽样检验')],
      [(0, 'The interviews were given to a random sample of students.', '随机抽选出部分学生进行了采访。', 'sample', '例', 126),
       (2, 'Typically, they survey and sample large areas of terrain.', '通常，他们会对大面积区域进行勘测和抽样检验（试验挖掘）。', 'sample', '真题', 126)],
      '我们需要抽查一下这批苹果（apple）的样品（sample）。')
    a('specimen', '/ˈspesɪmən/', 'n. 样品，标本，样本', 126,
      [('n.', '样品，标本，样本')],
      [(0, 'It is displaying more fossil specimens.', '它展示了更多的化石标本。', 'specimens', '例', 126)])
    group = '23 病相关语境词汇'
    a('virus', '/ˈvaɪrəs/', 'n. 病毒；病毒性疾病', 126,
      [('n.', '病毒'), ('n.', '病毒性疾病')],
      [(1, 'There’s a virus going around the office.', '办公室里流行着一种病毒性疾病。', 'virus', '例', 126),
       (0, 'In fact, a virus emerged in the 1970s that could have been just that fatal.', '事实上，20世纪70年代出现了一种病毒，这种病毒可能非常致命。', 'virus', '真题', 126)],
      'vi（围）+ r（热）+ us（我们）→围热我们→病毒围绕在我们周围使我们发热→病毒。')
    a('bacteria', '/bækˈtɪəriə/', 'n. 细菌', 126,
      [('n.', '细菌')],
      [(0, 'Neither chilling nor freezing kills all bacteria.', '冷藏和冷冻都不能杀死所有的细菌。', 'bacteria', '例', 126),
       (0, 'Raw meat and poultry may contain harmful bacteria.', '生肉和禽肉可能含有有害细菌。', 'bacteria', '例', 126)])
    a('germ', '/dʒɜːm/', 'n. 病菌，细菌，微生物', 126,
      [('n.', '病菌，细菌，微生物')],
      [(0, 'Dirty hands can be a breeding ground for germs.', '脏手可能滋生病菌。', 'germs', '例', 126),
       (0, 'Cracks and scratches in work surfaces can harbour germs.', '操作台的裂缝和划痕都会藏着细菌。', 'germs', '例', 126)],
      '发音类似“这么（多啊）”→原来我的手上有这么多“细菌”啊！→细菌，微生物。')
    a('alcohol', '/ˈælkəhɒl/', 'n. 酒；酒精，乙醇', 126,
      [('n.', '酒'), ('n.', '酒精，乙醇')],
      [(0, 'Alcohol should only be consumed in moderation.', '酒只能适量饮用。', 'Alcohol', '例', 126),
       (0, 'To help prevent headaches, drink plenty of water, and avoid alcohol and coffee.', '为了预防头疼，要多喝水，避免饮酒和喝咖啡。', 'alcohol', '例', 126)],
      '发音类似“一口喝”→一口喝什么？酒啊。酒桌上有一句话：感情深，一口闷→酒。')
    a('physical', '/ˈfɪzɪkl/', 'adj. 物质的；物理学的；身体的，肉体的，躯体的；有形的', 126,
      [('adj.', '身体的，肉体的，躯体的'), ('adj.', '物质的；有形的'), ('adj.', '物理学的')],
      [(0, 'All subjects undergo a physical examination.', '所有受试者都要接受体检。', 'physical', '例', 126),
       (1, 'Rather than portraying landscape, land artists used the physical substance of the land itself as their medium.', '地景艺术家使用土地本身的物质作为媒介，而不是描绘风光。', 'physical', '真题', 126)])
    include_page(127)
    a('physician', '/fɪˈzɪʃn/', 'n. 医生，内科医生', 127,
      [('n.', '医生，内科医生')],
      [(0, 'He became the President’s personal physician.', '他成了总统的私人医生。', 'physician', '例', 127),
       (0, 'My father is busy because he is a physician.', '我父亲很忙，因为他是一名医生。', 'physician', '例', 127)],
      'physic（身体）+ ian（表示“人”的后缀）→和你身体打交道的人→医生。')
    a('mental', '/ˈmentl/', 'adj. 思想的，精神的；思考的；智力的', 127,
      [('adj.', '思想的，精神的'), ('adj.', '思考的；智力的')],
      [(0, 'The experience caused her huge amounts of mental suffering.', '那次经历给她带来了巨大的精神痛苦。', 'mental', '例', 127),
       (0, 'Our mental health doesn’t really go anywhere.', '我们的心理健康并没有真的离开。', 'mental', '真题', 127)],
      'ment（与思想有关的）+ al（形容词后缀）→思想的。')
    t.pending('mental', 1, '原书将doesn’t really go anywhere直译为“并没有真的离开”，缺上下文且可能误译，保留原文原译待核对。')
    group = '24 -tal相关词汇'
    a('fundamental', '/ˌfʌndəˈmentl/', 'n. 基本原则；基本原理；adj. 基础的，根本的', 127,
      [('adj.', '基础的，根本的'), ('n.', '基本原则；基本原理')],
      [(0, 'Hard work is fundamental to success.', '勤奋工作是成功的基础。', 'fundamental', '例', 127),
       (0, 'Today the rapid growth of artificial intelligence (AI) raises fundamental questions.', '如今，人工智能（AI）的快速发展引发了一些根本性的问题。', 'fundamental', '真题', 127)],
      '资金（fund）对很多公司来说是最基本的（fundamental）东西。')
    a('refund', '/ˈriːfʌnd/ n.; /rɪˈfʌnd/ v.', 'n. 退款；v. 退还，退（款）', 127,
      [('v.', '退还，退（款）'), ('n.', '退款')],
      [(0, 'Your money will be refunded in full.', '您会得到全额退款。', 'refunded', '例', 127),
       (0, 'If you are not satisfied with the goods, the price will be refunded to you.', '如果对商品不满意，我们会给您退款。', 'refunded', '例', 127)],
      're（回来）+ fund（金钱）→把钱退回去→退款。')
    a('fatal', '/ˈfeɪtl/', 'adj. 致命的，灾难性的', 127,
      [('adj.', '致命的'), ('adj.', '灾难性的')],
      [(0, 'The disease is potentially fatal.', '这种疾病可能会致命。', 'fatal', '例', 127),
       (0, 'Since the beginning, this price tag has been PreCheck’s fatal flaw.', '从一开始，这个价格标签就是预检的致命缺陷。', 'fatal', '真题', 127)],
      '发音类似“肥头”→婴儿得了肥头（大头病）是很“致命的”→致命的。')
    a('total', '/ˈtəʊtl/', 'adj. 总的，总计的，全部的；完全的；彻底的；n. 总数，总计；v. 共计', 127,
      [('adj.', '完全的；彻底的'), ('n.', '总数，总计'), ('adj.', '总的，总计的，全部的'), ('v.', '共计')],
      [(0, 'All the people we interviewed expressed almost total satisfaction with it.', '我们采访的所有人对此都表示几乎完全满意。', 'total', '例', 127),
       (1, 'His businesses are worth a combined total of $3 billion.', '他的企业加在一起总值30亿美元。', 'total', '例', 127)],
      '发音类似“通通”→通通都是，全部都是→全部的，完全的。')
    a('digital', '/ˈdɪdʒɪtl/', 'adj. 数字的，数码的', 128,
      [('adj.', '数字的，数码的')],
      [(0, 'We are moving our CCTV to a fully digital network.', '我们正在把闭路电视转移到一个完全数字化的网络。', 'digital', '例', 128),
       (0, 'Digital products are there to promote maximal engagement.', '数字产品就是要最大程度地提高（你的）参与度。', 'Digital', '真题', 128)],
      '发音类似“低着头”→人家听课都抬着头，你却低着头，干什么呢？看数码产品→数字的，数码的。')
    a('talent', '/ˈtælənt/', 'n. 天资，天赋，天才', 128,
      [('n.', '天资，天赋，天才')],
      [(0, 'She displayed her talent for comedy at the event.', '她在活动中展示了自己的喜剧天赋。', 'talent', '例', 128)],
      'tal（联想成tall“高”）+ ent（表“人”）→高人就是在某方面有天赋、有才能的人→天赋，天才。')
    group = '25 “重要的”相关词汇'
    a('vital', '/ˈvaɪtl/', 'adj. 必不可少的，对……极重要的；生气勃勃的', 128,
      [('adj.', '必不可少的，对……极重要的'), ('adj.', '生气勃勃的')],
      [(0, 'Reading is of vital importance in language learning.', '阅读在语言学习中至关重要。', 'vital', '例', 128),
       (0, 'So it will be vital to prioritize areas at greatest risk of fire or drought.', '因此优先处理火灾或干旱风险最大的区域是至关重要的。', 'vital', '真题', 128)],
      'vit（生命）+ al（形容词后缀）→有生命的→生气勃勃的。',
      related=[('vitality', 'n. 活力，生命力', 128)])
    material('vitality',128,'例',english='The music has a wonderful freshness and vitality.',translation='这首乐曲给人以绝妙的新鲜感和活力。')
    a('essential', '/ɪˈsenʃl/', 'n. 必需品；要素，要点；adj. 必不可少的；极其重要的；本质的；基本的', 128,
      [('adj.', '必不可少的；极其重要的'), ('adj.', '本质的；基本的'), ('n.', '必需品'), ('n.', '要素，要点')],
      [(0, 'Vitamins play an essential role in many body processes.', '维生素在身体的许多过程中起着重要作用。', 'essential', '例', 128),
       (0, 'It is essential to keep the two groups separate.', '将这两组分开是完全必要的。', 'essential', '例', 128)],
      '很多人在女生的护肤品里会见到这个单词的名词essence（精华）→精华对于女生来说是“必不可少的”东西→必不可少的。')
    a('crucial', '/ˈkruːʃl/', 'adj. 至关重要的；关键性的', 128,
      [('adj.', '至关重要的；关键性的')],
      [(0, 'Parents play a crucial role in preparing their child for school.', '父母对孩子做好上学的准备起着至关重要的作用。', 'crucial', '例', 128),
       (0, 'Many Americans regard the jury system as a concrete expression of crucial democratic values.', '许多美国人认为陪审团制度是关键民主价值观的具体体现。', 'crucial', '真题', 128)])
    a('indispensable', '/ˌɪndɪˈspensəbl/', 'adj. 不可或缺的，必不可少的', 128,
      [('adj.', '不可或缺的，必不可少的')],
      [(0, 'Cars have become an indispensable part of our lives.', '汽车已成了我们生活中必不可少的一部分。', 'indispensable', '例', 128),
       (0, 'A good dictionary is indispensable for learning a foreign language.', '一本好词典是学习外语必备的。', 'indispensable', '例', 129)],
      'in（表示否定）+ dis（表示否定）+ pens（支付）+ able（形容词后缀）→不能不支付的，也就是必须花钱去购买的→不可或缺的，必不可少的。')
    a('inevitable', '/ɪnˈevɪtəbl/', 'adj. 不可避免的，必然发生的', 129,
      [('adj.', '不可避免的，必然发生的')],
      [(0, 'They came to see defeat as inevitable.', '他们逐渐认识到失败是不可避免的。', 'inevitable', '例', 129),
       (0, 'It is inevitable that the attention is focused elsewhere.', '人们将注意力集中在其他行业，这是不可避免的。', 'inevitable', '真题', 129)],
      'in（表示否定）+ evit（避免）+ able（形容词后缀）→不能避免的→必然发生的。',
      related=[('inevitably', 'adv. 不可避免地', 129)])
    material('inevitably',129,'例',english='Inevitably, the press exaggerated the story.',translation='新闻界照例又夸大了这件事。')
    a('imperative', '/ɪmˈperətɪv/', 'adj. 重要紧急的，迫切的，急需处理的；n. 必要的事', 129,
      [('adj.', '重要紧急的，迫切的，急需处理的'), ('n.', '必要的事')],
      [(0, 'We consider it absolutely imperative to start work immediately.', '我们认为必须立即开始工作，刻不容缓。', 'imperative', '例', 129)],
      'im（联想成“我妹”）+ per（每一天）+ ative（联想成active“积极的”）→我妹妹每天都很积极地处理这个事情，为什么？因为这个事情很“紧急”啊→重要紧急的。')
    group = '26 “pond-”相关词汇'
    a('ponder', '/ˈpɒndə(r)/', 'v. 沉思，考虑', 129,
      [('v.', '沉思，考虑')],
      [(0, 'She pondered for a moment before replying.', '她回答前考虑了一会儿。', 'pondered', '例', 129),
       (0, 'Intelligence seeks to grasp, manipulate, reorder, and adjust, while intellect examines, ponders, wonders, theorizes, criticizes, and imagines.', '智力寻求的是理解、运用、整合和调节，而才智是审视、思考、琢磨、形成理论、批判和想象。', 'ponders', '真题', 129)],
      '发音类似“胖的”→胖的人是不是要经常“考虑”该怎么减肥？→考虑。')
    a('ponderous', '/ˈpɒndərəs/', 'adj. 慢条斯理的；沉闷乏味的；缓慢的；笨拙的', 129,
      [('adj.', '缓慢的'), ('adj.', '慢条斯理的'), ('adj.', '沉闷乏味的'), ('adj.', '笨拙的')],
      [(0, 'She watched the ponderous progress of her old father.', '她看着老父亲缓慢地往前走着。', 'ponderous', '例', 129),
       (1, 'He spoke in a slow ponderous voice.', '他慢条斯理地开口说话。', 'ponderous', '例', 129)])
    a('clumsy', '/ˈklʌmzi/', 'adj. 笨拙的，不灵巧的；难处理的；复杂难懂的；使用不便的', 129,
      [('adj.', '复杂难懂的；使用不便的'), ('adj.', '笨拙的，不灵巧的'), ('adj.', '难处理的')],
      [(0, 'The complaints procedure is clumsy and time-consuming.', '申诉程序复杂耗时。', 'clumsy', '例', 129),
       (1, 'Competition law appears to be the only way to address these imbalances of power. But it is clumsy.', '竞争法似乎是解决这些权力失衡问题的唯一方法。但这种方法笨拙不堪。', 'clumsy', '真题', 129)],
      '他参加学校社团（club）经常出糗，显得很笨拙（clumsy）。')
    a('respond', '/rɪˈspɒnd/', 'v. （口头或书面）回答，回应；作出反应；反应灵敏', 129,
      [('v.', '（口头或书面）回答，回应'), ('v.', '作出反应；反应灵敏')],
      [(0, 'More than fifty people responded to the advertisement.', '五十多人对这个广告作出了回应。', 'responded', '例', 130)],
      're（字母发音联想成“阿姨”）+ spond（联想成“是棒的”）→这个阿姨“回应”很快，是不是很棒？→回应。',
      related=[('response', 'n. 回答，答复；反应', 130)])
    material('response',130,'例',english='I received an immediate response to my request.',translation='我的请求立即得到了答复。')
    material('response',130,'例',english='I am writing in response to your enquiry.',translation='我写信是为了答复你的询问。')
