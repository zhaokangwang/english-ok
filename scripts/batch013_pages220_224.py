"""Visual transcription of seventh-unit headwords beginning on PDF220–224."""
COMPLETE_THROUGH = 224
NEXT_WORD = 'attribute'
NEXT_PAGE = 225

def append(t,associated):
    group='28 “economy”相关词汇'
    def a(spelling,ipa,definition,page,meanings,examples,mnemonic='',related=()):
        t.add(2314+len(t.words),spelling,ipa,definition,page,group,meanings,examples,mnemonic,related)
        t.words[-1]['book_unit_id']='unit-007'
    def material(word,page,label,**kw):
        associated.append(dict(word=word,pdf_page=page,label=label,**kw))
    def include_page(page):
        w=t.words[-1]; w['pdf_pages']=sorted(set(w['pdf_pages']+[page]))
        w['printed_pages']=[f'{p-8:03}' for p in w['pdf_pages']]

    a('autonomy','/ɔːˈtɒnəmi/','n. 自治，自治权；自主，自主权',220,
      [('n.','自治，自治权'),('n.','自主，自主权')],
      [(0,'The Act granted limited autonomy to the republics.','该法案赋予各共和国的自治权是有限的。','autonomy','例',220),
       (1,'Schools have gained greater autonomy from government control.','学校受政府的管控少了，获得了更大的自主权。','autonomy','例',220)],
      'auto（自主的，自动的）+ nomy（形似economy）→经济上自主的→自治权，自治。',
      [('autonomous','adj. 自治的；自主的',220)])
    material('autonomous',220,'派生',phonetic='/ɔːˈtɒnəməs/',definition='adj. 自治的；自主的')
    group='29 “文明、城乡”相关词汇'
    a('civil','/ˈsɪvl/','adj. 国家的；公民的；民用的，民事的；有礼貌的',220,
      [('adj.','国家的'),('adj.','公民的'),('adj.','民用的，民事的'),('adj.','有礼貌的')],
      [(1,'We have been actively exercising our civil rights.','我们一直在积极行使自己的公民权利。','civil','例',220),
       (3,'The teachers were all perfectly civil to me.','老师们对我都很和蔼。','civil','例',220)])
    material('citizen',220,'拓展',phonetic='/ˈsɪtɪzn/',definition='n. 公民，市民')
    a('civilise','/ˈsɪvəlaɪz/','v. 开化，使文明；教化',220,
      [('v.','开化，使文明；教化')],
      [(0,'Its hero avoids being civilised—going to school and learning to read.','该书的主人公逃避被教化——上学识字。','civilised','例',220),
       (0,'Such behaviour is totally unacceptable in a civilised society.','这种行为在文明社会是完全不能被接受的。','civilised','例',220)],
      related=[('civilisation','n. 文明，文明社会',220)])
    t.pending('civilise',1,'civilised在此修饰society，属形容词文明的用法，原书主释义只列动词，原文原译保留待核。')
    material('civilize',220,'美式拼写',definition='civilise的美式拼写')
    material('civilisation',220,'例',phonetic='/ˌsɪvəlaɪˈzeɪʃn/',definition='n. 文明，文明社会',american_spelling='civilization',english='Yet science has a cultural history, too, with roots going back to the dawn of civilisation.',translation='然而，科学也有一段文化史，其根源可以追溯到文明的开端。')
    a('urban','/ˈɜːbən/','adj. 城市的；都市的；城镇的；城市音乐的',220,
      [('adj.','城市的；都市的；城镇的'),('adj.','城市音乐的')],
      [(0,'Today, as urban population explodes globally, cities become more crowded.','今天，随着全球城市人口激增，城市变得更加拥挤。','urban','例',220)],
      'ur（鹅）+ ban（禁止）→就是禁止养鹅，在哪儿禁止养鹅？一般在城市里是有限制或禁令的→城市的；都市的。')
    a('suburb','/ˈsʌbɜːb/','n. 市郊，郊区',220,
      [('n.','市郊，郊区')],
      [(0,'They live in the suburbs.','他们住在郊区。','suburbs','例',220),
       (0,'He was born in a suburb of Xian of Shaanxi province.','他出生于陕西省西安市的一个郊区。','suburb','例',220)],
      '在市区（urb联想成urban）的下面（sub），就是“郊区”。',
      [('suburban','adj. 郊区的；呆板的',220)])
    material('suburban',220,'派生',phonetic='/səˈbɜːbən/',definition='adj. 郊区的；呆板的')
    a('rural','/ˈrʊərəl/','adj. 乡下的，农村的',221,
      [('adj.','乡下的，农村的')],
      [(0,'There is no denying the limited land can no longer produce enough crops for an ever-increasing rural population.','不可否认，有限的土地不能再为不断增加的农村人口生产足够的粮食。','rural','例',221),
       (0,'He grew up in a predominantly rural area.','他在一个以农村为主的地区长大。','rural','例',221)],
      '发音类似“孺弱”→年轻力壮的都出去打工去了，农村只剩下了老弱妇孺→乡下的，农村的。')
    a('metropolis','/məˈtrɒpəlɪs/','n. 大都会，大城市',221,
      [('n.','大都会，大城市')],
      [(0,'He was dazzled by the high buildings of the metropolis.','大都市的高楼大厦使他眼花缭乱。','metropolis','例',221),
       (0,'New Orleans is the metropolis of the American South.','新奥尔良是美国南部的大都会。','metropolis','例',221)],
      related=[('metropolitan','adj. 大都市的；大都会的',221)])
    material('metropolitan',221,'派生',phonetic='/ˌmetrəˈpɒlɪtən/',definition='adj. 大都市的；大都会的')
    group='30 “scrutiny”相关形近词'
    a('scrutiny','/ˈskruːtəni/','n. 仔细检查，认真彻底的审查',221,
      [('n.','仔细检查，认真彻底的审查')],
      [(0,'Her argument doesn’t really stand up to scrutiny.','她的观点经不起认真推敲。','scrutiny','例',221),
       (0,'Manuscript will be flagged up for additional scrutiny by the journal’s internal editors, or by its existing Board of Reviewing Editors or by outside peer reviewers.','原稿将由该期刊的内部编辑、其现有评审编委会或外部同行评审者作出标记，以接受额外审查。','scrutiny','真题',221)],
      '多小的（tiny）错误我们都要仔细检查（scrutiny）。')
    a('screw','/skruː/','n. 螺丝（钉）；v. 用螺丝钉固定；拧紧',221,
      [('n.','螺丝（钉）'),('v.','用螺丝钉固定'),('v.','拧紧')],
      [(0,'A screw is stronger than a nail.','螺丝钉比普通钉子牢固。','screw','例',221),
       (1,'The table legs are screwed to the floor.','桌子腿用螺丝钉固定在地板上。','screwed','例',221)],
      '发音类似“四个儒”（生）→想象四个文弱的书生在那拧“螺丝钉”，累得满头大汗，也没有“固定”住→用螺丝钉固定。')
    group='31 “champion”相关形近词'
    a('champion','/ˈtʃæmpiən/','n. 冠军，第一名；优胜者',221,
      [('n.','冠军，第一名；优胜者')],
      [(0,'After three years, he became the champion!','三年后，他成了冠军。','champion','例',221),
       (0,'She is a former Olympic skating champion.','她是前奥运会滑冰冠军。','champion','例',221)])
    a('campaign','/kæmˈpeɪn/','n. 战役；运动；v. 参加运动',221,
      [('n.','战役'),('n.','运动'),('v.','参加运动')],
      [(1,'Local people started a petition and letter-writing campaign to keep the hospital open.','为让医院不关门，当地民众发起请愿和写联名信的活动。','campaign','例',221),
       (1,'Its Campaign to Protect Rural England struck terror into many local Conservative parties.','它保护英格兰农村的活动让许多地方保守党感到害怕。','Campaign','真题',221)],
      '发音类似“肯拼”→在这场“战役”中，每个战士都肯拼命守卫自己的国家和人民→战役。')
    t.pending('campaign',1,'Campaign to Protect Rural England在原句中大写，可能为组织专名；原译按活动处理，与运动义映射待核。')
    a('campus','/ˈkæmpəs/','n. 校园，校区',222,
      [('n.','校园，校区')],
      [(0,'The statue stands on the campus of Princeton University.','这座雕像矗立在普林斯顿大学的校园里。','campus','例',222),
       (0,'Otherwise outside directors will follow the example of Ms. Simmons, once again very popular on campus.','否则，外部董事将会效仿西蒙斯女士的做法，重返学校仍能大受欢迎。','campus','真题',222)])
    group='32 “特征”相关词汇'
    a('trait','/treɪt/','n. 特点，特性，特征',222,
      [('n.','特点，特性，特征')],
      [(0,'Awareness of class is a typically British trait.','阶层意识是英国人的典型特征。','trait','例',222)],
      '发音类似“踹他”→他的“特点”就是什么事情都想用暴力来解决，这是不对的→特点，特性。')
    material('traits of character',222,'拓展',definition='性格特征')
    a('character','/ˈkærəktə(r)/','n. 性格，特征；人物，角色',222,
      [('n.','人物，角色'),('n.','性格，特征')],
      [(0,'The minor characters in the novel provide a lot of the humour.','小说中的那些小角色制造了很多幽默。','characters','例',222),
       (1,'He reveals his true character to very few people.','他没有向什么人显露过他的真实性格。','character','例',222)],
      related=[('characteristic','adj. 特有的，独特的；n. 特点，特征',222)])
    material('characteristic',222,'派生',phonetic='/ˌkærəktəˈrɪstɪk/',definition='adj. 特有的，独特的；n. 特点，特征')
    a('characterise','/ˈkærəktəraɪz/','v. 是……的特征；描述，刻画',222,
      [('v.','是……的特征'),('v.','描述，刻画')],
      [(0,'The city is characterised by tall modern buildings in steel and glass.','这座城市的特点是钢铁和玻璃建造的现代化高楼大厦林立。','characterised','例',222),
       (0,'Since the days of Aristotle, a search for universal principles has characterised the scientific enterprise.','从亚里士多德时代起，对普遍通用原理的探索就成为科学事业的特征。','characterised','真题',222)])
    material('characterize',222,'美式拼写',definition='characterise的美式拼写')
    a('feature','/ˈfiːtʃə(r)/','n. 特点，特征，特色；v. 以……为特征',222,
      [('n.','特点，特征，特色'),('v.','以……为特征')],
      [(0,'Such features are easily written into the software.','这些特性很容易写入软件。','features','例',222),
       (0,'Teamwork is a key feature of the training programme.','团队合作是这项训练计划的重要特点。','feature','例',222)])
    group='33 “consicous”形近词及近义词'
    a('conscience','/ˈkɒnʃəns/','n. 良知，良心；愧疚',222,
      [('n.','良知，良心'),('n.','愧疚')],
      [(0,'He won’t let it trouble his conscience.','他不会让这件事搞得自己良心不安的。','conscience','例',222),
       (0,'This is an issue of equality, opportunity and national conscience.','这是一个关于平等、机会和国家良知的问题。','conscience','例',222)],
      '从事科学（science）事业的科学家们是很有良知（conscience）的。',
      [('conscientious','adj. 认真的',222)])
    material('conscientious',222,'派生',phonetic='/ˌkɑːnʃiˈenʃəs/',definition='adj. 认真的')
    a('conscious','/ˈkɒnʃəs/','adj. 注意到，意识到；有知觉的，有意识的',222,
      [('adj.','注意到，意识到'),('adj.','有知觉的，有意识的')],
      [(0,'He was conscious that he was talking too much with the stranger.','他意识到他和这个陌生人说得实在太多了。','conscious','例',222),
       (1,'It’s not explicitly conscious; it’s the idea that I’m a coach, and you’re my team, and we’re in this together.','它不是明明白白的有意行为；它是这样一种想法：我是教练，你们是我的队员，我们同舟共济。','conscious','真题',223)],
      related=[('consciousness','n. 意识，知觉',223),('unconscious','adj. 失去知觉的，无意识的',223)])
    include_page(223)
    material('consciousness',223,'派生',phonetic='/ˈkɒnʃəsnəs/',definition='n. 意识，知觉')
    material('unconscious',223,'派生',phonetic='/ʌnˈkɒnʃəs/',definition='adj. 失去知觉的，无意识的')
    a('aware','/əˈweə(r)/','adj. 知道，明白；意识到',223,
      [('adj.','知道，明白；意识到')],
      [(0,'They are less aware of the value of their money.','他们很少意识到他们的钱的价值。','aware','例',223),
       (0,'She slipped away without him being aware of it.','她悄悄离开，没有让他发觉。','aware','例',223)],
      'a（一个）+ war（战争）+ e→一个经历过战争的人“知道”和平的重要性→知道的，明白的。')
    group='34 “intact”相关形近词'
    a('contact','/ˈkɒntækt/','n. 联系，联络；接触；v. 联络；联系',223,
      [('n.','联系，联络'),('n.','接触'),('v.','联络；联系')],
      [(1,'Personality can affect how a person reacts to eye contact.','个性会影响一个人对目光接触的反应。','contact','例',223),
       (2,'This morning he had tried every possible way to contact her.','今天早晨，他想尽一切办法与她联系。','contact','例',223)],
      'con（都）+ tact（接触）→都“接触”→接触，联系。')
    a('intact','/ɪnˈtækt/','adj. 完整；完好无损',223,
      [('adj.','完整；完好无损')],
      [(0,'The bridge remains intact even after 30 years.','虽然过了30年，这座桥还保持完好。','intact','例',223),
       (0,'Most of the house remains intact even after two hundred years.','即使过了200年，这房子的大部分还保持完好。','intact','例',223)],
      'in（表示否定）+ tact（接触）→没有接触→我没碰你的东西，它还是“完好无损”的。')
    a('tangible','/ˈtændʒəbl/','adj. 有形的；实际的；真实的',223,
      [('adj.','有形的'),('adj.','实际的'),('adj.','真实的')],
      [(1,'The scheme must have tangible benefits for the unemployed.','这项计划必须对失业者有切实的好处。','tangible','例',223),
       (2,'The tension between them was almost tangible.','他们之间的紧张关系几乎让人都感觉得出来。','tangible','例',223)],
      'tang（触摸）+ ible（形容词后缀）→可以触摸到的→有形的。')
    group='35 “粘着、分离”相关词汇'
    a('attach','/əˈtætʃ/','v. 系；贴上；附上；重视；（使）与……有联系',223,
      [('v.','系；贴上；附上'),('v.','重视'),('v.','（使）与……有联系')],
      [(1,'We attach great importance to good design of buildings and neighbourhoods.','我们非常重视建筑和社区的良好设计。','attach','例',223),
       (0,'I attach a copy of my notes for your information.','我附上笔记一份供你参考。','attach','例',223)],
      'at（表示“加强”）+ tach（钉；钉子）→牢牢钉上→附上。',
      [('attachment','n. 附件，附属物',224)])
    include_page(224)
    material('attachment',224,'派生',phonetic='/əˈtætʃmənt/',definition='n. 附件，附属物')
    a('detach','/dɪˈtætʃ/','v. 分开，分离；分派，派遣',224,
      [('v.','分开，分离'),('v.','分派，派遣')],
      [(0,'One of the panels had become detached from the main structure.','一块镶板已从主体结构上脱落。','detached','例',224),
       (0,'Detach the coupon and return it as soon as possible.','将表格撕下后尽快寄回。','Detach','例',224)],
      'de（分开）+ tach（接触）→不接触了→分开，分离。')
    a('adhere','/ədˈhɪə(r)/','v. 附着；（~to）遵循；坚持',224,
      [('v.','附着'),('v.','（~to）遵循；坚持')],
      [(0,'There was oil adhering to the bird’s feathers.','鸟的羽毛上附着油。','adhering','例',224),
       (1,'The bank adheres to all rules regarding the opening and closing of accounts.','银行遵守所有关于开立和关闭账户的规定。','adheres','例',224)],
      'ad（表示“加强”）+ here（在这）→一直都在这儿→坚持。')
    a('cling','/klɪŋ/','v. 紧紧抓住；粘住；（~to）坚持',224,
      [('v.','紧紧抓住'),('v.','粘住'),('v.','（~to）坚持')],
      [(0,'I clung closely to my mother’s arm.','我紧紧抓着妈妈的胳膊。','clung','例',224),
       (1,'Her hair clung to her hot damp skin.','她的头发紧贴在湿热的皮肤上。','clung','例',224)],
      '发音类似“可怜”→那个可怜的孩子一直“紧紧抓住”母亲的衣角，一刻都不离开。')
    a('coherent','/kəʊˈhɪərənt/','adj. 合乎逻辑的；有条理的；清楚易懂的；有表达能力的；能表达清楚的',224,
      [('adj.','合乎逻辑的'),('adj.','有条理的'),('adj.','清楚易懂的'),('adj.','有表达能力的；能表达清楚的')],
      [(1,'You’re not being very coherent.','你的话前后不太一致。','coherent','例',224),
       (0,'The subjects of the curriculum form a coherent whole.','课程中的科目构成了一个连贯的整体。','coherent','例',224)],
      related=[('cohesive','adj. 使结合的；使凝结的；使内聚的',224)])
    material('cohesive',224,'派生',phonetic='/kəʊˈhiːsɪv/',definition='adj. 使结合的；使凝结的；使内聚的')
    group='36 “contribute”近义词及形近词'
    a('donate','/dəʊˈneɪt/','v. 捐赠，赠予；捐献',224,
      [('v.','捐赠，赠予；捐献')],
      [(0,'Customers may be willing to buy a company’s products as an indirect way to donate to the good causes it helps.','消费者可能愿意将购买企业的产品作为一种间接方式去资助该企业所帮助的慈善事业。','donate','真题',224)],
      related=[('donor','n. 捐赠者',224),('donation','n. 捐赠，捐款',224)])
    material('donor',224,'派生',phonetic='/ˈdəʊnə(r)/',definition='n. 捐赠者')
    material('donation',224,'例',phonetic='/dəʊˈneɪʃn/',definition='n. 捐赠，捐款',english='A local businessman offered a large donation for the school.',translation='当地一位商人捐了一大笔款给学校。')
    a('contribute','/kənˈtrɪbjuːt/','v. 是……的原因之一；促进，促成；捐助，捐献',224,
      [('v.','是……的原因之一；促进，促成'),('v.','捐助，捐献')],
      [(0,'Fresh air, enough exercise and nutritious food contribute to good health.','新鲜空气、足够的运动和营养的食物有助于身体健康。','contribute','例',224),
       (1,'The student volunteers contributed their own time to helping exchange students.','学生志愿者贡献自己的时间来帮助交换生。','contributed','例',224)],
      'con（共同）+ tribut（=give，表示“给予”）+ e→共同给出→捐献。')
    include_page(225)
