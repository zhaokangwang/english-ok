"""Visual transcription of twelfth-batch headwords beginning on PDF195–199."""
COMPLETE_THROUGH=199
NEXT_WORD='reputation'
NEXT_PAGE=200

def append(t,associated):
    group='37 fuse相关词汇'
    def a(spelling,ipa,definition,page,senses,examples,mnemonic='',related=()):
        t.add(2213+len(t.words),spelling,ipa,definition,page,group,senses,examples,mnemonic,related)
        t.words[-1]['book_unit_id']='unit-006'
    def material(word,page,label,**kw):
        associated.append(dict(word=word,pdf_page=page,label=label,**kw))
    def include(page):
        w=t.words[-1]; w['pdf_pages']=sorted(set(w['pdf_pages']+[page]))
        w['printed_pages']=[f'{p-8:03}' for p in w['pdf_pages']]

    a('refuse','/rɪˈfjuːz/','v. 拒绝；回绝；不准许',195,
      [('v.','拒绝；回绝'),('v.','不准许')],
      [(0,'He flatly refused to discuss the matter.','他断然拒绝商讨这件事。','refused','例',195),
       (0,'Readers are paying more for slimmer products. Some papers even had the nerve to refuse delivery to distant suburbs.','读者付费更多却获得缩水的内容。一些报社甚至敢拒绝向边远郊区递送报纸。','refuse','真题',195)],
      're（回去）+ fuse（流）→给我的东西，我再让它流回去就是“拒绝”→拒绝。',
      [('refusal','n. 拒绝，回绝',195)])
    a('diffuse','/dɪˈfjuːs/','v. 散布；传播，扩散；adj. 扩散的，弥漫的；漫射的',195,
      [('v.','散布；传播，扩散'),('adj.','扩散的，弥漫的'),('adj.','漫射的')],
      [(0,'Technologies diffuse rapidly.','技术普及非常快。','diffuse','例',195),
       (0,'Alvarez’s experience demonstrates the importance of finding ways to diffuse stress before it threatens your health and your ability to function.','阿尔瓦雷斯的经历表明，要在压力威胁到你的健康和正常生理机能之前找到方法疏导它，这一点很重要。','diffuse','真题',195)],
      'di（表示“往下，分开”）+ f + fuse（流）→往下分开流，不就是“散布”吗？→散布，传播。',
      [('diffusion','n. 传播，散布，扩散',195)])
    t.pending('diffuse',1,'原句diffuse stress译为疏导压力，与原书散布、传播、扩散释义的映射待核，原文原译保留。')
    group='38 fluent形近词'
    a('fluent','/ˈfluːənt/','adj. 流利的，流畅的',195,
      [('adj.','流利的，流畅的')],
      [(0,'She’s fluent in Polish.','她的波兰语很流利。','fluent','例',195),
       (0,'Conversely, some European firms have half or more of their employees fluent in a second language.','相反，一些欧洲公司有一半或一半以上的员工能流利地使用第二语言。','fluent','例',195)],
      'flu（流）+ ent（形容词后缀）→流利的。')
    a('affluent','/ˈæfluənt/','adj. 富裕的；富足的',195,
      [('adj.','富裕的；富足的')],
      [(0,'Sweden is one of affluent countries in the world.','瑞典是全球富国之一。','affluent','例',195),
       (0,'This is a very affluent neighbourhood.','这是一个富人区。','affluent','例',195)],
      'af（表示加强）+ flu（流）+ ent（形容词后缀）→钱多得向外流→富裕的。')
    t.pending('affluent',0,'原书one of affluent countries疑似缺少定冠词，保留原文原译，待核对语法。')
    group='39 temporary形近词'
    a('temporary','/ˈtemprəri/','adj. 暂时的，临时的；短暂的',195,
      [('adj.','暂时的，临时的'),('adj.','短暂的')],
      [(0,'The woman needs a temporary replacement for her assistant.','这名妇女需要一名临时替代者来接替她的助手。','temporary','例',195)],
      'tempor（表时间）+ ary（形容词后缀）→可持续的时间很短→暂时的，临时的。')
    material('temporary guest workers',195,'拓展',definition='临时外籍劳工')
    a('contemporary','/kənˈtemprəri/','adj. 现代的，当代的；同一时代的，同时期的；n. 同龄人；同辈人',195,
      [('adj.','现代的，当代的'),('adj.','同一时代的，同时期的'),('n.','同龄人；同辈人')],
      [(0,'In our contemporary society, games are popular among youngsters.','在我们当代社会中，游戏在年轻人中很盛行。','contemporary','例',196),
       (0,'Sales of contemporary art fell by two-thirds, and in the most overheated sector, they were down by nearly 90% in the year to November 2008.','截至2008年11月，当代艺术品的销售额下降了三分之二，在最热门的领域，销售额则下降了近90%。','contemporary','真题',196)],
      'con（共同）+ tempor（时间）+ ary（形容词后缀）→时间都一样，处在相同的时间→同时代的；同龄人。')
    group='40 好好背单词这是我们的treaty'
    a('treaty','/ˈtriːti/','n. （国家之间的）条约，协议',196,
      [('n.','（国家之间的）条约，协议')],
      [(0,'Negotiations on the treaty have lasted more than 700 days.','关于该条约的谈判已经持续了700多天。','treaty','例',196),
       (0,'All the members have voted to ratify the treaty.','所有成员都投赞成票通过了这一条约。','treaty','例',196)])
    group='41 -form-相关词汇'
    a('formal','/ˈfɔːml/','adj. 形式上的；正式的，正规的',196,
      [('adj.','正式的，正规的'),('adj.','形式上的')],
      [(0,'Young children are beginning their formal education as early as four years old.','幼儿从四岁开始接受正规教育。','formal','例',196),
       (0,'John McWhorter sees the triumph of 1960s counter-culture as responsible for the decline of formal English.','约翰·麦克沃特认为，20世纪60年代反主流文化的胜利是正式英语衰落的原因。','formal','真题',196)],
      'form（形式）+ al（形容词后缀）→形式上的→正式的。',
      [('formally','adv. 正式地，形式上',196),('informal','adj. 非正式的，不拘礼节的',196)])
    a('conform','/kənˈfɔːm/','v. 遵守，遵从；顺从，顺应；相一致，相符合',196,
      [('v.','相一致，相符合'),('v.','遵守，遵从；顺从，顺应')],
      [(0,'The building does not conform with safety regulations.','这座建筑物不符合安全条例。','conform','例',196),
       (1,'He refused to conform to the local customs.','他拒绝遵从当地的风俗习惯。','conform','例',196)],
      'con（共同）+ form（形式）→共同的形式→相一致。',
      [('conformity','n. （对社会规则的）遵从，遵守；（in ～ with/to）符合，一致',196)])
    material('conformity',196,'例',english='It was in conformity to the prevailing practice in the market.',translation='这符合市场的普通做法。')
    a('reform','/rɪˈfɔːm/','n. & v. 改革；改善；改良',196,
      [('n.','改革；改善；改良'),('v.','改革；改善；改良')],
      [(0,'Publishers continue to push for sweeping reforms.','出版商继续力求大刀阔斧的改革。','reforms','例',196),
       (1,'The key to reforming higher education is to alter the way in which the producers of knowledge are produced.','改革高等教育的关键在于改变培养知识分子的方式。','reforming','真题',197)],
      're（再）+ form（形式）→再换个形式→改革，改善。')
    a('uniform','/ˈjuːnɪfɔː(r)m/','n. 校服，制服；adj. 一致的；统一的',197,
      [('n.','校服，制服'),('adj.','一致的；统一的')],
      [(0,'The hat is part of the school uniform.','这帽子是校服的一部分。','uniform','例',197),
       (1,'Growth has not been uniform across the country.','全国各地的发展程度不一。','uniform','例',197)],
      'uni（统一的）+ form（形式）→统一形式的衣服→校服。')
    a('transform','/trænsˈfɔːm/','v. 使改变形态；使改观；改变',197,
      [('v.','使改变形态；使改观；改变')],
      [(0,'I am convinced that the electric power industry is transforming.','我确信电力工业正在发生变革。','transforming','例',197),
       (0,'But it takes collective scrutiny and acceptance to transform a discovery claim into a mature discovery.','但是将发现的声明变为一个成熟的发现是需要集体的审查和集体的接受。','transform','真题',197)],
      'trans（转变）+ form（形式）→转变形式→改变。',
      [('transformer','n. 变压器',197)])
    a('performance','/pəˈfɔːməns/','n. 表演，演出；表现；性能；业绩；执行；履行',197,
      [('n.','性能'),('n.','表现'),('n.','表演，演出'),('n.','业绩'),('n.','执行；履行')],
      [(0,'This machine delivers excellent performance at a very competitive price.','这台机器以极具竞争力的价格提供了出色的性能。','performance','例',197),
       (1,'Although a correlation between them leaving and subsequent bad performance at the firm is suggestive, it does not mean that such directors are always jumping off a sinking ship.','尽管外部董事离任与该公司随后的糟糕表现之间的关联暗示着这一点，但这并不意味着此类董事总是在跳离“沉船”。','performance','真题',197)])
    a('inform','/ɪnˈfɔːm/','v. 知会；通知；通告；了解；熟悉',197,
      [('v.','知会；通知；通告'),('v.','了解；熟悉')],
      [(0,'Please inform us of any changes of address.','地址若有变动请通知我们。','inform','例',197),
       (1,'We need time to inform ourselves thoroughly of the problem.','我们需要时间对这个问题有个透彻的了解。','inform','例',197)],
      '信息（information）是我们了解（inform）的东西。')
    material('well-informed',197,'拓展',definition='adj. 消息灵通的；见多识广的')
    material('ill-informed',197,'拓展',definition='adj. 消息不灵通的；了解不够的')
    a('formulate','/ˈfɔːmjuleɪt/','v. 确切表达，认真阐述；制定；规划；构想',197,
      [('v.','构想'),('v.','确切表达，认真阐述'),('v.','制定；规划')],
      [(0,'He struggled to formulate an answer.','他努力想出一个答案。','formulate','例',197),
       (1,'The role of natural selection in evolution was formulated only a little more than a hundred years ago.','自然选择在进化中的作用在一百多年前才被阐明。','formulated','真题',197)])
    material('formula',197,'拓展',definition='n. 公式；方案')
    group='42 -firm-相关词汇'
    a('confirm','/kənˈfɜːm/','v. 证实，证明；批准；确认；使确信',198,
      [('v.','证实，证明'),('v.','确认'),('v.','批准'),('v.','使确信')],
      [(0,'Rumours of job losses were later confirmed.','裁员的传言后来得到了证实。','confirmed','例',198),
       (1,'But today a man can boost his paternal (fatherly) wisdom—or at least confirm that he’s the kid’s dad.','但是如今男人可以提升自己作为父亲的智慧——至少可以确认自己是孩子的父亲。','confirm','真题',198)],
      'con（表示“加强”）+ firm（坚定的）→使坚定→证实。')
    a('affirm','/əˈfɜːm/','v. 确认，证实；断言……属实；申明；坚定（信念或观点）',198,
      [('v.','确认，证实'),('v.','断言……属实；申明'),('v.','坚定（信念或观点）')],
      [(1,'I can affirm that your dream will come true.','我肯定你的梦想会成真。','affirm','例',198),
       (0,'The decision was affirmed by the Court of Appeal.','上诉法院确认了这一决定。','affirmed','例',198)],
      'af（表示“加强”）+ firm（牢固的）→一再地使它牢固→肯定。')
    group='43 建筑、设施相关词汇'
    a('architecture','/ˈɑːkɪtektʃə(r)/','n. 建筑学；建筑设计或风格',198,
      [('n.','建筑设计或风格'),('n.','建筑学')],
      [(0,'There are examples of most styles of architecture in the town.','镇上有许多建筑风格的例子。','architecture','例',198),
       (1,'She’s a professor of architecture at the University of Oregon.','她是俄勒冈大学的建筑学教授。','architecture','例',198)],
      'ar（联想成art“艺术”）+ chi + tecture（联想成structure“结构”）→研究结构的艺术→建筑学。')
    a('architect','/ˈɑːkɪtekt/','n. 建筑师；设计师；缔造者，创造者',198,
      [('n.','建筑师；设计师'),('n.','缔造者，创造者')],
      [(0,'The house was designed by architect Louis Kahn.','这所房子是由建筑师路易斯·卡恩设计的。','architect','例',198),
       (0,'She’s a London-based architect and interior designer.','她是一位伦敦的建筑师和室内设计师。','architect','例',198)])
    a('infrastructure','/ˈɪnfrəstrʌktʃə(r)/','n. 基础设施，基础建设',198,
      [('n.','基础设施，基础建设')],
      [(0,'Roads, trails, restrooms, visitor centers and other infrastructure are crumbling.','道路、小径、厕所、游客中心和其他基础设施破损不堪。','infrastructure','真题',198),
       (0,'The infrastructure required to make a physical newspaper—printing presses, delivery trucks—isn’t just expensive; it’s excessive at a time when online-only competitors don’t have the same set of financial constraints.','制作一份实体报纸所需的基础设施——印刷机、送货卡车——不仅昂贵；而且贵得过分，当下只做网络报纸的竞争对手没有同样的财务限制。','infrastructure','真题',198)])
    group='44 争辩、争论相关词汇'
    a('argument','/ˈɑːɡjumənt/','n. 争论，争吵；辩论；论点；论据；理由',198,
      [('n.','争论，争吵；辩论'),('n.','论点；论据；理由')],
      [(0,'A decision was finally made after some heated argument.','经过一番激烈的争论，他们最后作出了决定。','argument','例',198),
       (1,'I don’t think that’s a very convincing argument.','我认为这个论点不太令人信服。','argument','例',199)])
    include(199)
    a('dispute','/dɪˈspjuːt/','n. 争论，辩论；争端；纠纷；v. 对……表示异议；就……发生争议；争论；辩论',199,
      [('n.','争论，辩论；争端；纠纷'),('v.','对……表示异议'),('v.','就……发生争议；争论；辩论')],
      [(0,'The matter was settled beyond dispute by the court judgment.','此问题已由法庭判决，不容争辩。','dispute','例',199),
       (1,'They never disputed our statements.','他们从未对我们的陈述提出异议。','disputed','例',199)],
      'dis（往下）+ put（放）+ e→你把我往下放，我把你往下放，是不是两个人在“辩论”或“争论”？→辩论，争论。')
    a('debate','/dɪˈbeɪt/','n. 争论，辩论，讨论；v. 辩论；讨论；思考',199,
      [('v.','辩论；讨论'),('n.','争论，辩论，讨论'),('v.','思考')],
      [(0,'It is time to debate the issue of school funding.','现在是讨论学校经费问题的时候了。','debate','例',199),
       (1,'But it can also be antagonistic, such as when a political candidate turns toward their competitor during a debate and makes eye contact that signals hostility.','但它也可能是在传达敌意，例如一位政治候选人在辩论中会转向对手，向其投去敌视的目光。','debate','真题',199)],
      'de（往下）+ bate（联想成beat“打”）→把对手往下打压→争论，辩论。')
    group='45 打斗、搏斗、打相关词汇'
    a('battle','/ˈbætl/','n. 战斗，战争，斗争；奋斗；v. 奋斗；搏斗；斗争',199,
      [('n.','斗争；奋斗'),('n.','战斗，战争'),('v.','奋斗；搏斗；斗争')],
      [(0,'They are engaged in a legal battle with their competitors.','他们正与竞争对手进行一场法律战。','battle','例',199),
       (0,'The Church’s long-standing dogma was losing the great battle for truth to rationalists and scientists.','在与理性主义者和科学家的“真理之战”中，教会长久以来坚持的教条输得一败涂地。','battle','真题',199)],
      'bat=beat（打），那battle就是“战斗，斗争”。')
    a('combat','/ˈkɒmbæt/','n. 战斗；搏斗；打仗；v. 与……搏斗；战斗；防止，减轻',199,
      [('v.','防止，减轻'),('v.','与……搏斗；战斗'),('n.','战斗；搏斗；打仗')],
      [(0,'What is Dr. Daffner’s advice for combating memory loss?','达夫纳医生对对抗失忆有什么建议？','combating','例',199),
       (1,'And that is very good news because the Internet may well be the most powerful tool for combating world poverty that we’ve ever had.','那是一个非常好的消息，因为互联网很可能是有史以来与世界贫困作斗争的最有力的工具。','combating','真题',199)],
      'com（都）+ bat（打）→大家一起打→战斗。')
    a('hammer','/ˈhæmə(r)/','n. 榔头；锤子；v. （用锤子）敲；锤打；轻易打败',199,
      [('v.','（用锤子）敲；锤打'),('n.','榔头；锤子'),('v.','轻易打败')],
      [(0,'We hammer metal with a hammer.','我们用铁锤锤打金属。','hammer','例',200),
       (0,'She hammered the nail into the wall.','她把钉子钉到墙上了。','hammered','例',200)])
