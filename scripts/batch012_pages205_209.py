"""Visual transcription of seventh-unit headwords starting on PDF205–209."""
COMPLETE_THROUGH = 209
NEXT_WORD = 'mostly'
NEXT_PAGE = 210

def append(t, associated):
    group = '02 -fect-相关词汇'
    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(2213+len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-007'
    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))
    def include_page(page):
        w=t.words[-1]
        w['pdf_pages']=sorted(set(w['pdf_pages']+[page]))
        w['printed_pages']=[f'{p-8:03}' for p in w['pdf_pages']]

    a('perfect', 'adj. /ˈpɜːfɪkt/; v. /pəˈfekt/', 'adj. 完美的；准确的；极好的；完全的；v. 使完善，使完美，使完备', 205,
      [('adj.', '极好的'), ('adj.', '完美的'), ('adj.', '准确的'), ('adj.', '完全的'), ('v.', '使完善，使完美，使完备')],
      [(0, 'The new restaurant is a perfect place for dating.', '那家新餐馆是约会的绝佳场所。', 'perfect', '例', 205)],
      related=[('perfection', 'n. 完全，完美', 205), ('perfectly', 'adv. 完全地；非常，十分', 205)])
    material('perfectly', 205, '例', english='You know perfectly well what I mean.', translation='我的意思你是一清二楚的。')
    a('utilise', '/ˈjuːtəlaɪz/', 'v. 利用；使用；运用；应用', 205,
      [('v.', '利用；使用；运用；应用')],
      [(0, 'The company just released an updated version last week, and it’ll be utilised in over 50 undergraduate and graduate classrooms.', '该公司上周刚刚发布了一个更新版本，该版本将在50多个本科生和研究生课堂上使用。', 'utilised', '例', 205),
       (0, 'It also means that governments are increasingly compelled to interfere in these sectors in order to step up production and ensure that it is utilised to the best advantage.', '这也意味着政府越来越多地被迫干预这些部门，以加快生产并确保其得到最佳利用。', 'utilised', '真题', 205)],
      related=[('utility', 'n. 效用，实用；公用事业', 205)])
    t.words[-1]['notes'].append('原书并列美式拼写utilize，主词保留utilise，不另建重复词条。')
    material('utility', 205, '例', english='This information is of the highest utility to a historian.', translation='这条信息对历史学家来说是最有用的。')
    group = '03 优点、缺点相关词汇'
    a('advantage', '/ədˈvɑːntɪdʒ/', 'n. 优势；有利条件，有利因素；优点', 205,
      [('n.', '优点'), ('n.', '优势'), ('n.', '有利条件，有利因素')],
      [(0, 'Each of these systems has its advantages and disadvantages.', '这些系统各有其优缺点。', 'advantages', '例', 205)])
    material('disadvantage', 205, '拓展', definition='n. 缺点，劣势；不利因素')
    material('take advantage of', 205, '拓展', definition='利用')
    a('drawback', '/ˈdrɔːbæk/', 'n. 缺点，不利条件', 205,
      [('n.', '缺点，不利条件')],
      [(0, 'This is the one major drawback of the new system.', '这是新系统的一大弊端。', 'drawback', '例', 205),
       (0, 'Although a search agent worked for Redmon, career experts see drawbacks.', '尽管搜索引擎对雷德蒙有用，职业专家们还是看到了一些弊端。', 'drawbacks', '真题', 205)],
      '往后（back）拉（draw）→当你做事情时，拉你后腿的东西就是你的“缺点，不利条件”。')
    a('handicap', '/ˈhændɪkæp/', 'n. （身体或智力方面的）缺陷；不利条件；v. 妨碍，阻碍，使不利', 205,
      [('n.', '（身体或智力方面的）缺陷'), ('n.', '不利条件'), ('v.', '妨碍，阻碍，使不利')],
      [(0, 'She can’t drive because of her visual handicap.', '她因为视力缺陷不能开车。', 'handicap', '例', 205),
       (1, 'A history of long and effortless success can be a dreadful handicap.', '一段不费吹灰之力就可以获得持久成功的历史可能是一个可怕的障碍。', 'handicap', '真题', 206)],
      '他的手上（hand）总拿着一个帽子（cap），为了遮掩手上的“缺陷”（handicap）啊→缺陷。')
    a('flaw', '/flɔː/', 'n. 瑕疵；裂痕；缺点；弱点；错误', 206,
      [('n.', '瑕疵；缺点；弱点'), ('n.', '裂痕'), ('n.', '错误')],
      [(0, 'I am writing this letter to express my complaint against the flaws in your product.', '我写这封信是为了表达我对你们产品缺陷的不满。', 'flaws', '例', 206),
       (0, 'The most glaring flaw of the social cure as it’s presented here is that it doesn’t work very well for very long.', '正如这里所指出的，社会治疗最明显的缺陷是它不能长期有效。', 'flaw', '真题', 206)])
    a('shortcoming', '/ˈʃɔːtkʌmɪŋ/', 'n. 缺点，短处', 206,
      [('n.', '缺点，短处')],
      [(0, 'There were obvious shortcomings in the report.', '这个报告有明显纰漏。', 'shortcomings', '例', 206),
       (0, 'She made me aware of my own shortcomings.', '她让我意识到自己的缺点。', 'shortcomings', '例', 206)])
    group = '04 emerge相关形近词'
    a('surge', '/sɜːdʒ/', 'n. 激增，急剧上升；奔涌向前；v. 汹涌；激增', 206,
      [('n.', '激增，急剧上升'), ('v.', '激增'), ('n.', '奔涌向前'), ('v.', '汹涌')],
      [(0, 'We are having trouble keeping up with the recent surge in demand.', '对于近来出现的需求猛增，我们难以应对。', 'surge', '例', 206),
       (1, 'The railroad industry as a whole, despite its brightening fortunes, still does not earn enough to cover the cost of the capital it must invest to keep up with its surging traffic.', '就整个铁路行业来说，尽管前景大好，但它的收入目前依然不足以支付为满足激增的运输需要而投入的资金。', 'surging', '真题', 206)])
    t.pending('surge', 1, 'surging在本句作traffic的定语，派生形容词用法暂待复核，不直接训练原书动词激增义。')
    a('emerge', '/ɪˈmɜːdʒ/', 'v. 浮现；出现；兴起；暴露；显露', 206,
      [('v.', '浮现；出现'), ('v.', '兴起'), ('v.', '暴露；显露')],
      [(0, 'No new evidence emerged during the investigation.', '调查过程中未发现新证据。', 'emerged', '例', 206),
       (0, 'She finally emerged from her room at noon.', '中午，她终于从房间里出来了。', 'emerged', '例', 206)],
      'e（出）+ merg（沉，没）+ e→水落石出→浮现；出现。',
      [('emergence', 'n. 出现', 206)])
    a('merger', '/ˈmɜːdʒə(r)/', 'n. （组织、公司的）合并，归并', 206,
      [('n.', '（组织、公司的）合并，归并')],
      [(0, 'The merger is not necessarily a good thing.', '合并未必是件好事。', 'merger', '例', 206),
       (0, 'The world is going through the biggest wave of mergers and acquisitions ever witnessed.', '世界正在经历一场前所未有的巨大的并购浪潮。', 'mergers', '真题', 206)])
    a('submerge', '/səbˈmɜːdʒ/', 'v. 浸没，淹没；掩盖', 206,
      [('v.', '浸没，淹没'), ('v.', '掩盖')],
      [(0, 'The entire European coastline might be submerged.', '整个欧洲海岸线可能会被淹没。', 'submerged', '例', 206),
       (0, 'The fields had been submerged by floodwater.', '农田被洪水淹没了。', 'submerged', '例', 206)],
      'sub（下面）+ merg（沉没）+ e→沉没到下面去了→淹没。')
    group = '05 紧急、危机相关词汇'
    a('emergency', '/ɪˈmɜːdʒənsi/', 'n. 紧急情况；突发事件', 206,
      [('n.', '紧急情况；突发事件')],
      [(0, 'The government has declared a state of emergency following the earthquake.', '地震发生后政府已宣布进入紧急状态。', 'emergency', '例', 207),
       (0, 'In railway underground stations, people read notices and maps which told them where to go and what to do in the emergency.', '在铁路地下车站，人们阅读通知和地图，这些会告诉他们在紧急情况下去哪里和做什么。', 'emergency', '例', 207)],
      '医院里有急诊（emergency）室。')
    a('crisis', '/ˈkraɪsɪs/', 'n. 危机，危急关头；危难时刻；病危期', 207,
      [('n.', '危机，危急关头；危难时刻'), ('n.', '病危期')],
      [(0, 'The financial crisis has brought new factors into play.', '财政危机已引发了新的变数。', 'crisis', '例', 207),
       (0, 'In much of the world there is little sign of crisis.', '在世界大部分地区，几乎没有危机的迹象。', 'crisis', '真题', 207)],
      'cri（联想成cry“哭”）+ sis（名词后缀）→“危机”到了，很多人都会哭→危机。')
    group = '06 膨胀、扩大相关词汇'
    a('inflation', '/ɪnˈfleɪʃn/', 'n. 通货膨胀；膨胀；抬高；抬升', 207,
      [('n.', '通货膨胀'), ('n.', '膨胀'), ('n.', '抬高；抬升')],
      [(0, 'Their purchasing power has dropped markedly with inflation.', '随着通货膨胀，他们的购买力显著下降。', 'inflation', '例', 207)],
      'in（表示“否定”）+ falt（公寓）+ ion（名词后缀）→公寓都住不起了，因为“通货膨胀”了。')
    t.words[-1]['notes'].append('原书记忆辅助将公寓拼作falt，疑为flat；按扫描原样保留，不把助记拼写当作已核实知识。')
    material('cosmic inflation', 207, '拓展', definition='宇宙膨胀说')
    a('expand', '/ɪkˈspænd/', 'v. 扩大，扩展；增加，增强；详述', 207,
      [('v.', '增加，增强'), ('v.', '扩大，扩展'), ('v.', '详述')],
      [(0, 'Student numbers are expanding rapidly.', '学生人数在迅速增加。', 'expanding', '例', 207),
       (1, 'But in addition to those trusted coworkers, you should expand your horizons and find out about all the people around you.', '但除了那些信赖的同事，你还应拓宽范围，去了解你周围的每一个人。', 'expand', '真题', 207)],
      'ex（表示“往外”）+ pand（发音类似“胖的”）→往外变胖→往外扩张→扩大。',
      [('expansion', 'n. 扩张，扩大，膨胀', 207)])
    group = '07 财政相关词汇'
    a('finance', '/ˈfaɪnæns/', 'n. 财政；金融；资金；财务；v. 提供资金，负担经费', 207,
      [('n.', '金融'), ('n.', '财政'), ('n.', '资金'), ('n.', '财务'), ('v.', '提供资金，负担经费')],
      [(0, 'She developed a strong interest in finance.', '她对金融产生了浓厚的兴趣。', 'finance', '例', 207)],
      '发音类似“犯难死”→当西方发生“金融”危机时，很多人都会犯难！→金融，财政，资金。',
      [('financial', 'adj. 财政的，金融的', 207)])
    material('financial products', 207, '拓展', definition='金融产品')
    a('loan', '/ləʊn/', 'n. 贷款，借款；v. 借出；贷与', 207,
      [('n.', '贷款，借款'), ('v.', '借出；贷与')],
      [(0, 'We could apply for a loan to buy a car.', '我们可以申请贷款买一辆汽车。', 'loan', '例', 207),
       (0, 'She took out an $8,000 personal loan.', '她申请了8000美元的个人贷款。', 'loan', '例', 208)])
    a('deficit', '/ˈdefɪsɪt/', 'n. 赤字，亏损，逆差；缺少', 208,
      [('n.', '赤字，亏损，逆差'), ('n.', '缺少')],
      [(0, 'The money tourists spend helps decrease our chronic trade deficit.', '游客的消费有助于减少我们长期的贸易赤字。', 'deficit', '例', 208),
       (0, 'The trade balance has been in deficit for the past five years.', '过去五年来贸易状况一直是逆差。', 'deficit', '例', 208)],
      'de（表示“向下”）+ fic（做）+ it→经济往下做→经济走下坡路→亏损，赤字。')
    a('budget', '/ˈbʌdʒɪt/', 'n. 预算，政府的年度预算；v. 做预算，编入预算', 208,
      [('v.', '做预算，编入预算'), ('n.', '预算，政府的年度预算')],
      [(0, 'Sensible people budget their incomes.', '明智的人根据收入做预算。', 'budget', '例', 208),
       (1, 'He’s feeling positive, but he’ll carry on blogging—not about eating as cheaply as you can—but eating well on a budget.', '他现在心态很积极，但是他还是会继续更新博客——不是围绕尽可能吃得便宜——而是如何通过避免不必要的开支吃好。', 'budget', '真题', 208)],
      'bud（发音类似“爸爸”）+ get（得到）→爸爸得到了很多的“预算”。')
    a('target', '/ˈtɑːɡɪt/', 'n. 对象，目标；（射击的）靶子；v. 瞄准；把……作为攻击目标；面向', 208,
      [('n.', '对象，目标'), ('v.', '面向'), ('n.', '（射击的）靶子'), ('v.', '瞄准；把……作为攻击目标')],
      [(0, 'The target audience for the TV series is young people aged 13 to 18.', '这部电视剧的目标受众是13到18岁的年轻人。', 'target', '例', 208),
       (1, 'The products are targeted at young people.', '这些产品以年轻人为对象。', 'targeted', '例', 208)],
      'tar（发音类似“他”）+ get（获得）→他要获得胜利就得射中“靶子”→靶子；目标。')
    group = '08 平衡、平行para相关词汇'
    a('balance', '/ˈbæləns/', 'v. （使）平衡；相抵；n. 平衡；均衡；余额', 208,
      [('n.', '平衡；均衡'), ('v.', '（使）平衡'), ('v.', '相抵'), ('n.', '余额')],
      [(0, 'His wife’s death disturbed the balance of his mind.', '妻子的离世使他心神不宁。', 'balance', '例', 208),
       (1, 'Stop laughing: it’s not just cost effective but helps you balance your diet.', '别笑了，这不仅省钱，还能帮你平衡饮食。', 'balance', '真题', 208)],
      '发音类似“芭蕾思”→芭蕾舞者在跳舞时需要思考如何保持“平衡”。')
    a('parallel', '/ˈpærəlel/', 'n. 相似的人；相似特征；adj. 平行的；类似的；v. 与……相似；比得上', 208,
      [('v.', '与……相似'), ('adj.', '类似的'), ('n.', '相似的人；相似特征'), ('adj.', '平行的'), ('v.', '比得上')],
      [(0, 'Their legal system parallels our own.', '他们的法律制度与我们的相似。', 'parallels', '例', 208),
       (1, 'A parallel situation exists in respect of predatory mammals and fish-eating birds.', '食肉哺乳动物和食鱼鸟类也存在类似的情况。', 'parallel', '真题', 208)],
      'para（旁边）+ llel（联想成line“线”）→在旁边并排的线→平行的。')
    a('paralyse', '/ˈpærəlaɪz/', 'v. 使瘫痪；使不能正常工作；使麻痹', 208,
      [('v.', '使瘫痪'), ('v.', '使不能正常工作'), ('v.', '使麻痹')],
      [(0, 'He successfully fought a lawsuit involving a football player who was paralysed in a game.', '他成功地打了一场关于一名在比赛中瘫痪的足球运动员的官司。', 'paralysed', '例', 209),
       (2, 'She stood there, paralysed with fear.', '她站在那里，吓得呆若木鸡。', 'paralysed', '例', 209)],
      'para（旁边）+ ly（联想成“躺”）+ se（动词后缀）→这个人只能躺着→使瘫痪。')
    t.words[-1]['notes'].append('原书并列美式拼写paralyze，主词保留paralyse，不另建重复词条。')
    t.pending('paralyse', 1, 'paralysed with fear在本句描述僵住状态，与原译呆若木鸡及动词使麻痹义的直接映射需复核，暂待核。')
    a('parade', '/pəˈreɪd/', 'n. 游行；阅兵；炫耀；v. 游行，列队行进；炫耀', 209,
      [('n.', '游行'), ('v.', '炫耀'), ('n.', '阅兵'), ('n.', '炫耀'), ('v.', '游行，列队行进')],
      [(0, 'The parade is held every year.', '游行每年举办一次。', 'parade', '例', 209),
       (1, 'If people parade something, they show it in public so that it can be admired.', '如果人们炫耀某样东西，他们会在公共场合展示，以便被人赞赏。', 'parade', '例', 209)],
      '发音类似“颇累的”→“游行”是颇累的，“炫耀”也是颇累的→游行，炫耀。')
    a('paradox', '/ˈpærədɒks/', 'n. 悖论，似是而非的论点；矛盾的人或物', 209,
      [('n.', '悖论，似是而非的论点'), ('n.', '矛盾的人或物')],
      [(0, 'It is a curious paradox that we think of the physical sciences as “hard”, the social sciences as “soft”, and the biological sciences as somewhere in between.', '我们认为物理科学“硬”，社会科学“软”，生物科学介于两者之间，这是一个可怪的悖论。', 'paradox', '例', 209),
       (0, 'Two paradoxes exist throughout this credibility process.', '在整个获得可信度的过程中存在两个悖论。', 'paradoxes', '真题', 209)],
      'para（旁边）+ dox（观点）→观点旁边有观点→悖论；矛盾的人或物。',
      [('paradoxical', 'adj. 矛盾的', 209)])
    a('paramount', '/ˈpærəmaʊnt/', 'adj. 最重要的，首要的；至高无上的', 209,
      [('adj.', '最重要的，首要的'), ('adj.', '至高无上的')],
      [(0, 'This matter is of paramount importance.', '此事至关重要。', 'paramount', '例', 209),
       (0, 'The welfare of the child must always be the court’s paramount consideration.', '儿童的福利必须永远是法庭的首要考虑。', 'paramount', '例', 209)],
      'para（旁边）+ mount（山）→他总觉得旁边的那座山更高→最高；最重要的。')
    group = '09 数量相关词汇'
    a('amount', '/əˈmaʊnt/', 'n. 数量；金额；v. （～to）等于；总计，合计', 209,
      [('n.', '数量'), ('v.', '（～to）等于'), ('n.', '金额'), ('v.', '总计，合计')],
      [(0, 'During the course of trying various things, you will gain a large amount of social experience.', '在尝试各种事物的过程中，你会获得大量的社会经验。', 'amount', '例', 209),
       (1, 'Their actions amount to a breach of contract.', '他们的行为已属违反合同。', 'amount', '例', 209)],
      'a（一座）+ mount（山）→一座座山，到底有多少啊？→数量。')
    a('utmost', '/ˈʌtməʊst/', 'n. 极限，最大可能；最大量；adj. 极度的，最大的', 209,
      [('adj.', '极度的，最大的'), ('n.', '极限，最大可能；最大量')],
      [(0, 'You should study this document with the utmost care.', '你对这份文件的研究应该慎之又慎。', 'utmost', '例', 209),
       (1, 'The use of this little-known practice has accelerated in recent years, as colleges continue to do their utmost to keep students in school (and paying tuition) and improve their graduation rates.', '随着大学继续尽最大努力让学生留在学校（并支付学费），提高他们的毕业率，这一鲜为人知的做法近年来开始加快推行。', 'utmost', '真题', 209)])
    include_page(210)
    t.pending('utmost', 1, 'do their utmost为竭尽所能的固定用法，原译尽最大努力与原书名词极限、最大可能等释义的直接映射暂待复核。')
