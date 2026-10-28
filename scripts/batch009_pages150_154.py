"""Visual transcription of fifth-unit headwords starting on PDF150–154."""
COMPLETE_THROUGH = 152
NEXT_WORD = 'compatible'
NEXT_PAGE = 153

def append(t, associated):
    group = '08 合格相关词汇'
    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(1216 + len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-005'
    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))
    def include_page(page):
        w=t.words[-1]
        w['pdf_pages']=sorted(set(w['pdf_pages']+[page]))
        w['printed_pages']=[f'{p-8:03}' for p in w['pdf_pages']]

    a('eligible', '/ˈelɪdʒəbl/', 'adj. 有资格的，合格的；具备条件的', 150,
      [('adj.', '有资格的，合格的；具备条件的')],
      [(0, 'Are you eligible for early retirement?', '你符合提前退休的条件吗？', 'eligible', '例', 150),
       (0, 'Passengers who pass a background check are eligible to use expedited screening lanes.', '通过背景审核的乘客有资格使用快速安检通道。', 'eligible', '真题', 150)],
      'eli（联想成“爱丽”）+ g + ible（形容词后缀，可以……的）→爱丽是可以的→合格的，具备条件的。')
    a('elevate', '/ˈelɪveɪt/', 'v. 举起，抬起；升高，使提高；晋升；使情绪高昂', 150,
      [('v.', '升高，使提高'), ('v.', '举起，抬起'), ('v.', '晋升'), ('v.', '使情绪高昂')],
      [(0, 'Smoking often elevates blood pressure.', '抽烟常常使血压升高。', 'elevates', '例', 150),
       (0, 'Even better would be to help elevate notions of beauty beyond the standards of a particular industry.', '甚至更好的情况是帮助人们提高对美的理解，以超越某个特定行业的标准。', 'elevate', '真题', 150)],
      'ele（联想成“爱丽”）+ v + ate（动词后缀）→爱丽为他“提升”自己→举起；提高。',
      [('elevator', 'n. 电梯', 150), ('elevation', 'n. 高地；海拔；提拔；晋级', 150)])
    material('elevation', 150, '例', english='The city is at an elevation of 2,000 metres.', translation='这座城市海拔2000米。')
    group = '09 中国是和谐社会'
    a('harmony', '/ˈhɑːməni/', 'n. 和谐，协调，和睦，融洽', 150,
      [('n.', '和谐，协调，和睦，融洽')],
      [(0, 'They lived together in perfect harmony.', '他们相处得十分和睦。', 'harmony', '例', 150),
       (0, 'Many laws and customs are about social harmony.', '许多法律和习俗都是关于社会和谐的。', 'harmony', '例', 150)],
      related=[('harmonious', 'adj. 和谐的，友好和睦的', 150)])
    group = '10 家装相关词汇'
    a('decorate', '/ˈdekəreɪt/', 'v. 装饰；粉刷', 150,
      [('v.', '装饰'), ('v.', '粉刷')],
      [(0, 'The cake was decorated to look like a car.', '这蛋糕装饰得像一辆汽车。', 'decorated', '例', 150),
       (0, 'Hilton is building its own hotel there, which you may be sure will be decorated with Hamlet Hamburger Bars.', '希尔顿正在那里修建自己的酒店，可以肯定，酒店会配有哈姆雷特汉堡酒吧。', 'decorated', '真题', 150)],
      'de（联想成“弟弟”）+ cor（联想成core“核心”）+ ate（动词后缀）→弟弟买了一套房子，现在他的主要想法是“装饰”这套房子→装饰。',
      [('decoration', 'n. 装饰，装潢', 150), ('decorative', 'adj. 装饰性的，作装饰用的', 150)])
    a('ornament', '/ˈɔːnəmənt/', 'n. 装饰，摆设，装饰品；首饰；v. 装饰，点缀；美化', 150,
      [('n.', '装饰，摆设，装饰品'), ('n.', '首饰'), ('v.', '装饰，点缀；美化')],
      [(0, 'The clock is simply for ornament; it doesn’t work any more.', '这架时钟纯属摆设，它再也不走了。', 'ornament', '例', 151),
       (2, 'She ornaments her dress with lace.', '她用蕾丝装饰她的裙子。', 'ornaments', '例', 151)],
      'orna（装饰；配备）+ ment（名词后缀）→装饰品。')
    a('furnish', '/ˈfɜːnɪʃ/', 'v. 在（房屋等）处布置家具；提供，供应', 151,
      [('v.', '在（房屋等）处布置家具'), ('v.', '提供，供应')],
      [(0, 'The room was furnished with antiques.', '房间里摆放了古董。', 'furnished', '例', 151),
       (1, 'Foreign investors furnished most of the capital for the project.', '外国投资者为该项目提供了大部分资金。', 'furnished', '例', 151)],
      '有些人喜欢用毛皮（fur）布置（furnish）房子。',
      [('furniture', 'n. 家具', 151)])
    group = '11 商业、产品相关词汇'
    a('commerce', '/ˈkɒmɜːs/', 'n. 商业，贸易', 151,
      [('n.', '商业，贸易')],
      [(0, 'She has little experience of the world of commerce.', '她没有什么商界经验。', 'commerce', '例', 151),
       (0, 'Another major shift in the model for Internet commerce concerns the technology available for marketing.', '互联网商务模式的另一个重大转变涉及可用于营销的技术。', 'commerce', '真题', 151)],
      related=[('commercial', 'n. （电台或电视播放的）广告；adj. 商业的，贸易的', 151)])
    material('commercial', 151, '例', english='He did a number of commercials for major brands.', translation='他为许多品牌做了许多广告。')
    a('commodity', '/kəˈmɒdəti/', 'n. 商品；有用的东西', 151,
      [('n.', '商品'), ('n.', '有用的东西')],
      [(0, 'Crude oil is the world’s most important commodity.', '原油是世界上最重要的商品。', 'commodity', '例', 151),
       (0, 'It was a year before she became head of a tiny Internet-based commodities exchange.', '一年后，她成了一家小型互联网商品交易所的负责人。', 'commodities', '真题', 151)])
    a('merchant', '/ˈmɜːtʃənt/', 'n. 商人；批发商，（尤指）进出口批发商', 151,
      [('n.', '商人；批发商，（尤指）进出口批发商')],
      [(0, 'Venice was once a city of rich merchants.', '威尼斯曾是富商云集的城市。', 'merchants', '例', 151)],
      '发音类似“摸钱他”→每天摸钱，和钱打交道→商人。')
    a('merchandise', '/ˈmɜːtʃəndaɪs/', 'n. 商品，货品；v. 推销', 151,
      [('n.', '商品，货品'), ('v.', '推销')],
      [(0, 'These tokens can be exchanged for merchandise in any of our stores.', '这些现金券可以兑换我们任何商店里的货品。', 'merchandise', '例', 151),
       (1, 'She works with companies that want to make or merchandise products.', '她与想制作或推销衍生产品的公司合作。', 'merchandise', '例', 151)])
    a('product', '/ˈprɒdʌkt/', 'n. 产品，制品；产物', 151,
      [('n.', '产品，制品'), ('n.', '产物')],
      [(0, 'He has eliminated dairy products from his diet.', '他已经把奶制品从饮食中剔除了。', 'products', '例', 151),
       (0, 'The company sells its products around the world.', '该公司在世界各地销售其产品。', 'products', '例', 151)],
      related=[('by-product', 'n. 副产品', 151)])
    a('productive', '/prəˈdʌktɪv/', 'adj. 生产的；（尤指）多产的；有效益的，富有成效的', 151,
      [('adj.', '生产的'), ('adj.', '（尤指）多产的'), ('adj.', '有效益的，富有成效的')],
      [(0, 'The aim was to maximize the machine’s productive capacity.', '目的是最大限度地提高机器的生产能力。', 'productive', '例', 152),
       (2, 'My time spent in the library was very productive.', '我花在图书馆的时间很有收获。', 'productive', '例', 152)])
    a('productivity', '/ˌprɒdʌkˈtɪvəti/', 'n. 生产率，生产效率', 152,
      [('n.', '生产率，生产效率')],
      [(0, 'Few employers measure employee productivity.', '很少有雇主衡量雇员的生产力。', 'productivity', '例', 152),
       (0, 'Productivity is growing at a very healthy rate.', '生产力正以一个非常健康的速度增长。', 'Productivity', '例', 152)])
    a('reproduce', '/ˌriːprəˈdjuːs/', 'v. 复制；繁殖；再生产', 152,
      [('v.', '复制'), ('v.', '繁殖'), ('v.', '再生产')],
      [(0, 'This material can be reproduced without payment.', '这种材料可以免费复制。', 'reproduced', '例', 152),
       (1, 'Most reptiles reproduce by laying eggs on land.', '大多数爬行动物通过在陆地产卵进行繁殖。', 'reproduce', '例', 152)])
    a('venture', '/ˈventʃə(r)/', 'n. （尤指有风险的）企业，商业；经营项目；v. 冒险，敢于去（危险或令人不快的地方）；小心地说，谨慎地做（尤指会使人烦恼或不快的事）', 152,
      [('n.', '（尤指有风险的）企业，商业；经营项目'), ('v.', '冒险，敢于去（危险或令人不快的地方）'), ('v.', '小心地说，谨慎地做（尤指会使人烦恼或不快的事）')],
      [(0, 'A disastrous business venture lost him thousands of dollars.', '一个彻底失败的经营项目使他损失数千美元。', 'venture', '例', 152),
       (0, 'The directors of the company refused to undertake such a risky venture.', '公司董事拒绝承担这样一个有风险的经营项目。', 'venture', '例', 152)],
      related=[('adventure', 'n. 冒险，冒险经历；奇遇', 152)])
    a('advent', '/ˈædvent/', 'n. （重要事件、人物、发明等的）出现，到来', 152,
      [('n.', '（重要事件、人物、发明等的）出现，到来')],
      [(0, 'The advent of the new government resulted in many changes.', '新政府的到来导致了许多变化。', 'advent', '例', 152)])
    group = '12 peer形近词及相关语境词汇'
    a('peer', '/pɪə(r)/', 'n. 同龄人，同辈；身份（或地位）相同的人；贵族；v. 仔细看，端详', 152,
      [('n.', '同龄人，同辈；身份（或地位）相同的人'), ('n.', '贵族'), ('v.', '仔细看，端详')],
      [(0, 'She enjoys the respect of her peers.', '她受到同侪的尊敬。', 'peers', '例', 152),
       (0, 'That whispered message, half invitation and half forcing, is what most of us think of when we hear the words peer pressure.', '那种半邀请半胁迫的耳语是我们大部分人听到“同辈压力”这个词时会想到的。', 'peer', '真题', 152)],
      'pe（联想成“拍”）+ er（名词后缀，表示“人”）→同龄人之间打招呼喜欢拍拍肩膀→同龄人。')
    a('pioneer', '/ˌpaɪəˈnɪə(r)/', 'n. 先锋，先驱；v. 当开拓者', 152,
      [('n.', '先锋，先驱'), ('v.', '当开拓者')],
      [(0, 'The school was an early pioneer of the technique.', '这所学校是这项技术的早期先驱。', 'pioneer', '例', 152),
       (0, 'Two anthropologist-linguists were pioneers in describing many native languages of North and South America during the first half of the twentieth century.', '这两位人类语言学家是20世纪上半叶描述北美和南美许多土著语言的先驱。', 'pioneers', '真题', 152)],
      'pi（披）+ one（一个人）+ er（名词后缀，表示“人”）→披荆斩棘的一个人→先锋，先驱。')
    include_page(153)
