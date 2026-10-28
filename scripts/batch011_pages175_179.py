"""Visual transcription of eleventh-batch headwords beginning on PDF175–179."""
COMPLETE_THROUGH = 179
NEXT_WORD = 'width'
NEXT_PAGE = 180

def append(t,associated):
    group='06 机会、时机相关词汇'
    def a(spelling,ipa,definition,page,senses,examples,mnemonic='',related=()):
        t.add(2104+len(t.words),spelling,ipa,definition,page,group,senses,examples,mnemonic,related)
        t.words[-1]['book_unit_id']='unit-006'
    def material(word,page,label,**kw):
        associated.append(dict(word=word,pdf_page=page,label=label,**kw))
    def include(page):
        w=t.words[-1]; w['pdf_pages']=sorted(set(w['pdf_pages']+[page]))
        w['printed_pages']=[f'{p-8:03}' for p in w['pdf_pages']]

    a('opportunity','/ˌɒpəˈtjuːnəti/','n. 机会，时机',175,
      [('n.','机会，时机')],
      [(0,'You’ll have the opportunity to ask any questions at the end.','你们最后将有机会提问任何问题。','opportunity','例',175),
       (0,'There was no opportunity for further discussion.','没有机会进行深入讨论了。','opportunity','例',175)])
    a('frequent','/ˈfriːkwənt/','adj. 频繁的，经常发生的',175,
      [('adj.','频繁的，经常发生的')],
      [(0,'There is a frequent bus service into the centre of town.','公共汽车有很多班次开往市中心。','frequent','例',175),
       (0,'The new job involved frequent absences from home.','新工作需要经常离家。','frequent','例',175)],
      related=[('frequency','n. 频率；频繁；发生率',175),('frequently','adv. 频繁地；经常',175)])
    material('frequency',175,'真题',english='Though often viewed as a problem for western states, the growing frequency of wildfires is a national concern because of its impact on federal tax dollars.',translation='虽然野火的频繁发生经常被视为西部各州的一个问题，但由于它对联邦税收的影响，它已经成为全国关注的问题。')
    material('frequently',175,'真题',english='Throughout the evening, one man had been particularly talkative, frequently offering ideas and anecdotes, while his wife sat silently beside him on the couch.',translation='整个晚上，一位男士显得特别健谈，频繁表达自己的观点，讲述一些逸闻趣事，而他妻子则安静地坐在他旁边的沙发上。')
    group='07 诊断、疾病、治疗相关词汇'
    a('diagnose','/ˈdaɪəɡnəʊz/','v. 诊断，判断',175,
      [('v.','诊断'),('v.','判断')],
      [(0,'The illness was diagnosed as cancer.','此病被诊断为癌症。','diagnosed','例',175),
       (1,'I quickly diagnosed the problem as a faulty battery.','我很快诊断出问题是电池故障。','diagnosed','例',175)],
      'di（穿过）+ a + gnos（知道）+ e→需要X光穿过之后，检查一下才能知道是什么疾病→诊断，判断。',
      [('diagnosis','n. 诊断；判断',175),('diagnostic','adj. 诊断的；判断的',175)])
    a('clinic','/ˈklɪnɪk/','n. 门诊部，诊所；门诊时间；私人诊所',175,
      [('n.','门诊部，诊所；私人诊所'),('n.','门诊时间')],
      [(0,'He failed to keep his appointment at the clinic.','他未能按预约的时间去诊所。','clinic','例',175),
       (0,'He is being treated at an expensive clinic.','他正在一家收费昂贵的诊所接受治疗。','clinic','例',175)],
      '野餐（picnic）时我吃坏了肚子，要去诊所（clinic）看一下。')
    a('severe','/sɪˈvɪə(r)/','adj. 十分严重的，极为恶劣的，严厉的；重的',175,
      [('adj.','十分严重的，极为恶劣的；重的'),('adj.','严厉的')],
      [(0,'The fire has caused severe damage to the building.','这场火灾给大楼造成了严重的损坏。','severe','例',176),
       (1,'Her parents were never so severe with her older brother.','她的父母对她哥哥从来没有这么严厉过。','severe','例',176)])
    a('acute','/əˈkjuːt/','adj. 严重的，敏锐的，灵敏的；急性的',176,
      [('adj.','敏锐的，灵敏的'),('adj.','严重的'),('adj.','急性的')],
      [(0,'Her judgement is acute.','她的判断敏锐。','acute','例',176),
       (1,'As well as those chronic problems, the EU faces an acute crisis in its economic core, the 16 countries that use the single currency.','除了这些长期的问题之外，欧盟的经济核心也面临着严重的危机：16个国家使用单一货币。','acute','真题',176)],
      '一个（a）可爱的（cute）孩子，得了“急性的”疾病。')
    a('terminal','/ˈtɜːmɪnl/','n. 航站楼；航空终点站；（火车、公共汽车或船的）终点站；终端；adj. 晚期的',176,
      [('n.','航站楼；航空终点站'),('adj.','晚期的'),('n.','（火车、公共汽车或船的）终点站'),('n.','终端')],
      [(0,'Flights for Rome depart from Terminal 3.','飞往罗马的班机从3号航站楼出发。','Terminal','例',176),
       (1,'He is in the terminal stage of cancer.','他正处于癌症晚期。','terminal','例',176)],
      '在机场外，大家细心观察一下，很容易看到这个词。',
      [('terminate','v. （使）终止',176)])
    material('terminate',176,'例',english='You have no right to terminate the contract.',translation='你无权终止合同。')
    a('chronic','/ˈkrɒnɪk/','adj. 长期的；慢性的；难以治愈（或根除）的',176,
      [('adj.','慢性的'),('adj.','长期的'),('adj.','难以治愈（或根除）的')],
      [(0,'He was suffering from chronic bronchitis.','他患有慢性支气管炎。','chronic','例',176),
       (1,'It’s easy to dismiss as absurd the federal government’s ideas for plugging the chronic funding gap of our national parks.','联邦政府填补国家公园长期资金缺口的想法很容易被认为是荒谬的。','chronic','真题',176)],
      'chron（时间）+ ic→长期的；慢性的。')
    a('surgery','/ˈsɜːdʒəri/','n. 外科学；外科手术；诊室',176,
      [('n.','外科手术'),('n.','外科学'),('n.','诊室')],
      [(0,'He will require surgery on his left knee.','他的左膝需要做手术。','surgery','例',176),
       (0,'She’s had laser surgery on her eye.','她做了眼部激光手术。','surgery','例',176)],
      related=[('surgical','adj. 外科的；外科手术的',176),('surgeon','n. 外科医生',176)])
    material('surgeon',176,'例',english='I knew that I owed the surgeon my life.',translation='我明白外科医生救了我的命。')
    a('therapy','/ˈθerəpi/','n. 治疗，疗法，疗效',176,
      [('n.','治疗，疗法'),('n.','疗效')],
      [(0,'He is receiving therapy for cancer.','他正在接受癌症治疗。','therapy','例',176),
       (0,'They recommend exercise therapy for patients with chronic back pain.','他们建议对慢性背痛患者进行运动疗法。','therapy','例',176)])
    a('remedy','/ˈremədi/','n. 处理方法；改进措施；补偿；治疗；v. 改正，纠正，补救；改进',176,
      [('v.','改正，纠正，补救；改进'),('n.','处理方法；改进措施'),('n.','补偿'),('n.','治疗')],
      [(0,'This situation is easily remedied.','这种情形易于补救。','remedied','例',176),
       (0,'By the time a problem has been addressed and remedied it may have vanished in the marketplace.','某个问题待其得到解决和补救时，它可能已经在市场上消失了。','remedied','真题',177)])
    a('heal','/hiːl/','v. （使）康复，复原；治疗；（使）结束',177,
      [('v.','（使）康复，复原'),('v.','治疗'),('v.','（使）结束')],
      [(0,'It took a long time for the wounds to heal.','伤口过了很长时间才愈合。','heal','例',177),
       (1,'This will help to heal your cuts and scratches.','这个会有助于治好割伤和擦伤。','heal','例',177)],
      '她需要接受脚部的治疗（heal），所以治疗期间不能穿高跟鞋（heels）。')
    a('recovery','/rɪˈkʌvəri/','n. 恢复；痊愈；改善；回升；复苏',177,
      [('n.','恢复；痊愈'),('n.','改善'),('n.','回升；复苏')],
      [(0,'My father has made a full recovery from the operation.','我父亲手术后完全康复了。','recovery','例',177),
       (2,'There has been a budding economic recovery since the 2008 global crash.','自2008年全球危机以来，经济出现了复苏的苗头。','recovery','真题',177)],
      '小时候发烧的时候，妈妈就给我盖很多被子，她说多盖（cover）被子，捂捂汗就康复（recovery）了。')
    group='08 了解、发现、理解相关词汇'
    a('discover','/dɪˈskʌvə(r)/','v. 发现，找到；了解到，认识到',177,
      [('v.','发现，找到'),('v.','了解到，认识到')],
      [(0,'They first discovered this protein about five years ago.','大约五年前，他们首次发现了这种蛋白质。','discovered','例',177),
       (1,'For instance, failure can help you discover how strong a person you are.','例如，失败可以帮助你发现你是多么强大。','discover','真题',177)],
      'dis（表示“否定”）+ cover（表示“覆盖”）→不盖了，这件事被“发现”了→发现。')
    a('understanding','/ˌʌndəˈstændɪŋ/','n. 了解，理解（力）；谅解；协议；adj. 善解人意的；富有同情心的，体谅人的',177,
      [('n.','了解，理解（力）'),('n.','谅解'),('n.','协议'),('adj.','善解人意的；富有同情心的，体谅人的')],
      [(0,'The committee has no understanding of the problem.','委员会对这个问题根本不了解。','understanding','例',177),
       (0,'Such an approach to education does not expand children’s knowledge and understanding of the world.','这样的教育方式并没有扩大孩子们对世界的认识和理解。','understanding','例',177)])
    a('grasp','/ɡrɑːsp/','v. 抓住，抓紧；理解，领会；n. 紧抓；理解（力）；领会',177,
      [('v.','抓住，抓紧'),('v.','理解，领会'),('n.','紧抓'),('n.','理解（力）；领会')],
      [(0,'Kay grasped him by the wrist.','凯紧紧抓住他的手腕。','grasped','例',177),
       (1,'They failed to grasp the importance of his words.','他们没有理解他的话的重要性。','grasp','例',177)],
      '他紧紧地抓住（grasp）这个草（grass），往外拔。')
    a('grip','/ɡrɪp/','n. 紧握，紧抓；（对……的）控制，影响力；理解；了解；v. 紧握；紧抓；抓牢；使感兴趣；使激动；吸引住（某人）的注意',177,
      [('n.','理解；了解'),('v.','紧握；紧抓；抓牢'),('n.','紧握，紧抓'),('n.','（对……的）控制，影响力'),('v.','使感兴趣；使激动；吸引住（某人）的注意')],
      [(0,'You need to keep a good grip on reality in this job.','做这个工作你需要充分了解实际情况。','grip','例',177),
       (1,'Strengthening economic growth, at the same time as winter grips the northern hemisphere, could push the oil price higher still in the short term.','强劲的经济增长势头，以及北半球冬季的到来，仍有可能在短期内使石油价格涨得更高。','grips','真题',177)])
    include(178)
    t.pending('grip',1,'winter grips为比喻笼罩、控制，原译为冬季到来；原书动词释义未明确列此用法，保留待核，不直接训练紧握义。')
    group='09 strip相关形近词'
    a('strip','/strɪp/','v. 除去，剥去；剥夺；拿走；n. 条，带；狭长地带',178,
      [('n.','条，带'),('v.','剥夺'),('v.','除去，剥去；拿走'),('n.','狭长地带')],
      [(0,'Cut the meat into strips.','把肉切成条。','strips','例',178),
       (1,'Downloading and consuming culture requires great skills, but failing to move beyond downloading is to strip oneself of a defining constituent of humanity.','下载（模式）和消费的文化需要高超的技能，但是如果仅限于下载（模式），则无异于剥夺了人之所以为人的定义性要素。','strip','真题',178)])
    a('stripe','/straɪp/','n. 条纹，线条；种类，类型',178,
      [('n.','条纹，线条'),('n.','种类，类型')],
      [(0,'He was wearing a grey shirt with white stripes.','他穿着一件灰底白条的衬衫。','stripes','例',178),
       (1,'Scholars, policymakers, and critics of all stripes have debated the social implications of these changes.','学者、政策制定者以及各界评论人士就这些变化的社会影响展开了讨论。','stripes','真题',178)])
    group='10 strain相关形近词'
    a('stain','/steɪn/','n. 污点，污渍；v. 玷污；留下污渍；败坏（名声）',178,
      [('v.','败坏（名声）'),('n.','污点，污渍'),('v.','玷污；留下污渍')],
      [(0,'The events had stained the city’s reputation unfairly.','这些事件使该市背上了不应有的恶名。','stained','例',178),
       (0,'His affair with a slave stained his prestige.','他与一个女奴的风流韵事玷污了他的威望。','stained','真题',178)],
      '这个污点（stain）洗不掉，只能一直留在（stay）衣服上了。')
    a('strain','/streɪn/','n. 张力；紧张；压力；拉伤；v. 损伤；拉伤；尽力；竭力；过度使用；使不堪承受',178,
      [('n.','紧张'),('n.','压力'),('n.','张力'),('n.','拉伤'),('v.','损伤；拉伤'),('v.','尽力；竭力'),('v.','过度使用；使不堪承受')],
      [(0,'Their marriage is under great strain at the moment.','眼下他们的婚姻关系非常紧张。','strain','例',178),
       (1,'I found it a strain having to concentrate for so long.','我觉得这么长时间全神贯注挺累的。','strain','例',178)])
    a('restrain','/rɪˈstreɪn/','v. 阻止；制止；约束，控制；抑制',178,
      [('v.','阻止；制止；约束，控制'),('v.','抑制')],
      [(0,'He placed a restraining hand on her arm.','他拉住她的胳膊制止她。','restraining','例',178),
       (1,'John managed to restrain his anger.','约翰努力压制住自己的怒气。','restrain','例',178)],
      're（反复）+ strain（拉紧）→反复拉紧→阻止，制止。',
      [('restrained','adj. 克制的；有节制的',178),('restraint','n. 抑制，限制；约束力',178)])
    t.pending('restrain',0,'restraining在本句作hand的定语，原译改述制止动作；暂待复核，不直接训练动词阻止义。')
    a('constrain','/kənˈstreɪn/','v. 限制，约束；强迫，迫使',178,
      [('v.','强迫，迫使'),('v.','限制，约束')],
      [(0,'The company said that it was constrained to raise prices.','该公司说它被迫提高价格。','constrained','例',178),
       (1,'Men and women are becoming less constrained by stereotyped roles.','男性和女性越来越不受陈规定型角色的束缚。','constrained','例',179)],
      'con（表示“加强”）+ strain（拉紧）→使劲拉紧→强迫，迫使。')
    a('refrain','/rɪˈfreɪn/','v. 克制，节制；避免',179,
      [('v.','避免'),('v.','克制，节制')],
      [(0,'Both sides should refrain from actions that would make the situation worse.','双方都应避免采取会使局势恶化的行动。','refrain','例',179),
       (0,'California has asked the justices to refrain from a sweeping ruling.','加利福尼亚州呼吁法官不要作出太笼统的裁定。','refrain','真题',179)],
      're（热）+ f（伏）+ rain（雨）→三伏天很热，终于下雨了，我无法“克制”内心的喜悦→克制。')
    group='11 force相关词汇'
    a('enforce','/ɪnˈfɔːs/','v. 强制执行；强行实施；强迫，迫使',179,
      [('v.','强制执行；强行实施'),('v.','强迫，迫使')],
      [(0,'It’s the job of the police to enforce the law.','警察的工作就是执法。','enforce','例',179),
       (0,'In Arizona v. United States, the majority overturned three of the four contested provisions of Arizona’s controversial plan to have state and local police enforce federal immigration law.','在亚利桑那州与联邦政府一案中，多数法官推翻了颇具争议的亚利桑那州移民方案（让州和地方警察执行联邦移民法）中四项受质疑条款里的三项。','enforce','真题',179)],
      'en（使）+ force（力量）→用力量使你去做→强迫。')
    a('reinforce','/ˌriːɪnˈfɔːs/','v. 加强；充实；使更强烈；加固；给……加强力量',179,
      [('v.','加强；使更强烈；给……加强力量'),('v.','加固'),('v.','充实')],
      [(0,'This report strongly reinforces the view that the system must be changed.','这份报告强有力地证实了必须进行制度改革的观点。','reinforces','例',179),
       (1,'All buildings are now reinforced to withstand earthquakes.','所有建筑现都已加固，以抗地震。','reinforced','例',179)],
      're（再）+ in（往里）+ force（力量）→再往里增加力量→加强；加固。')
    t.pending('reinforce',0,'原译证实与原书加强等释义的对应需复核，保留原文原译，暂不直接训练加强义。')
    group='12 大、宽、高相关词汇'
    a('enlarge','/ɪnˈlɑːdʒ/','v. 扩大；扩充；扩展，增大；放大',179,
      [('v.','扩大；扩充；扩展，增大'),('v.','放大')],
      [(0,'Reading will enlarge your vocabulary.','阅读能扩大词汇量。','enlarge','例',179),
       (1,'We’re going to have this picture enlarged.','我们准备将这张照片放大。','enlarged','例',179)])
    a('largely','/ˈlɑːdʒli/','adv. 在很大程度上；多半；主要地',179,
      [('adv.','主要地；多半'),('adv.','在很大程度上')],
      [(0,'The decision was based largely on consumer feedback.','这个决定主要是基于消费者的反馈。','largely','例',179),
       (1,'However, there is another important part of the jobs picture that was largely overlooked.','然而，就业形势中的另一个重要部分很大程度上被忽视了。','largely','真题',179)])
    a('heighten','/ˈhaɪtn/','v. 提高，（使）加强，增加',179,
      [('v.','提高，（使）加强，增加')],
      [(0,'The campaign is intended to heighten public awareness of the disease.','这场运动的目的是使公众更加了解这种疾病。','heighten','例',179),
       (0,'The drug is said to give users a heightened sense of well-being.','据说这种药物能给使用者带来更高的幸福感。','heightened','例',180)],
      'height（高度）+ en（使）→使……高→提高，（使）加强。')
    include(180)
    t.pending('heighten',1,'heightened在本句为sense的定语，派生形容词用法暂待复核，不直接训练原书动词提高义。')
