"""Visual transcription of seventh-unit headwords beginning on PDF210–214."""
COMPLETE_THROUGH = 214
NEXT_WORD = 'ease'
NEXT_PAGE = 215

def append(t,associated):
    group='09 数量相关词汇'
    def a(spelling,ipa,definition,page,meanings,examples,mnemonic='',related=()):
        t.add(2213+len(t.words),spelling,ipa,definition,page,group,meanings,examples,mnemonic,related)
        t.words[-1]['book_unit_id']='unit-007'
    def material(word,page,label,**kw):
        associated.append(dict(word=word,pdf_page=page,label=label,**kw))
    def include_page(page):
        w=t.words[-1]; w['pdf_pages']=sorted(set(w['pdf_pages']+[page]))
        w['printed_pages']=[f'{p-8:03}' for p in w['pdf_pages']]

    a('mostly','/ˈməʊstli/','adv. 主要地，大部分地；一般地，通常',210,
      [('adv.','一般地，通常'),('adv.','主要地，大部分地')],
      [(0,'We’re mostly out on Sundays.','我们星期天一般不在家。','mostly','例',210),
       (1,'In that decade, however, large numbers also migrated from California, mostly to other parts of the West.','然而，在那十年里，也有大量的人从加利福尼亚州迁出，大部分去了西部的其他地区。','mostly','真题',210)])
    group='10 缺口、空白相关词汇'
    a('gap','/ɡæp/','n. 缺口，裂口；分歧；隔阂；差距',210,
      [('n.','差距'),('n.','缺口，裂口'),('n.','分歧；隔阂')],
      [(0,'There’s an enormous gap between the rich and the poor in that country.','那个国家的贫富差距很大。','gap','例',210),
       (1,'There are huge gaps in their knowledge.','他们的知识差距很大。','gaps','例',210)])
    t.pending('gap',1,'knowledge gaps在此或指知识缺漏，原译知识差距很大与缺口义的对应待核，原文原译保留。')
    material('the gap between the Medieval and modern periods',210,'拓展',definition='中世纪和现代之间的鸿沟')
    a('blank','/blæŋk/','adj. 空白的；空着的；茫然的，没有表情的；n. 空白处、空格',210,
      [('adj.','空白的；空着的'),('adj.','茫然的，没有表情的'),('n.','空白处、空格')],
      [(0,'Sign your name in the blank space below.','在下面的空白处签上名字。','blank','例',210),
       (1,'She stared at me with a blank expression on her face.','她一脸木然地盯着我。','blank','例',210)],
      '发音类似“不来客”→我开了一家小面馆，从来没有来过客人，不来客人，我的小面馆就是“空着的”。')
    a('vacant','/ˈveɪkənt/','adj. 空缺的；空着的；未被占用的；茫然的',210,
      [('adj.','空着的；未被占用的'),('adj.','空缺的'),('adj.','茫然的')],
      [(0,'We stared at the vacant table for a minute or so.','我们盯着那张空桌子看了大约一分钟。','vacant','例',210),
       (0,'They always give the vacant seats to whoever comes first.','他们总是把空位给最先来的人。','vacant','例',210)],
      '发音类似“未（开）垦的”→一片未开垦的土地→空着的，未被占用的。')
    group='11 意愿相关词汇'
    a('reluctant','/rɪˈlʌktənt/','adj. 不情愿的，勉强的',210,
      [('adj.','不情愿的，勉强的')],
      [(0,'She was reluctant to admit she was wrong.','她不愿承认自己有错。','reluctant','例',210),
       (0,'So when one monkey was handed a grape in exchange for her token, the second was reluctant to hand hers over for a mere piece of cucumber.','因此，当一只猴子用一个代币换到一颗葡萄时，第二只猴子就不愿意用代币仅换一片黄瓜了。','reluctant','真题',210)],
      '发音类似“驴拉坦克”→驴怎么可能拉得动坦克呢？→勉强的。')
    a('volunteer','/ˌvɒlənˈtɪə(r)/','n. 志愿者，志愿兵；义务工作者；v. 自愿做；义务做；主动建议（或告诉）',210,
      [('n.','志愿者，志愿兵；义务工作者'),('v.','自愿做；义务做'),('v.','主动建议（或告诉）')],
      [(0,'She does volunteer work at an orphanage.','她在孤儿院做志愿者工作。','volunteer','例',211),
       (1,'He volunteered as a tutor of immigrant children.','他自愿做移民儿童的家庭教师。','volunteered','例',211)],
      related=[('voluntary','adj. 自愿的，自发的',211)])
    t.pending('volunteer',0,'volunteer作work的定语，原书未列形容词用法，暂不直接训练志愿者名词义。')
    group='12 low相关词汇'
    a('hollow','/ˈhɒləʊ/','n. 凹陷处；坑洼处；adj. 空心的，中空的；虚伪的',211,
      [('n.','凹陷处；坑洼处'),('adj.','空心的，中空的'),('adj.','虚伪的')],
      [(0,'The village lay secluded in a hollow of the hills.','村子坐落在一个幽静的小山谷中。','hollow','例',211),
       (1,'The tree trunk was hollow inside.','这树干里面是空的。','hollow','例',211)],
      '坑洼处（hollow）就像地上有个洞（hole）。')
    a('shallow','/ˈʃæləʊ/','adj. 浅的；浅薄的；肤浅的',211,
      [('adj.','浅的'),('adj.','浅薄的；肤浅的')],
      [(0,'These fish are found in shallow waters around the coast.','这些鱼生长在海边浅水水域。','shallow','例',211),
       (1,'This shows how shallow their commitment to the environment really is.','这表明他们对环境的承诺是多么肤浅。','shallow','例',211)],
      '浅滩（shallow）上可以挖到很多贝壳（shell）。')
    a('swallow','/ˈswɒləʊ/','n. 燕子；v. 吞下，咽下；吞没，淹没',211,
      [('v.','吞下，咽下'),('v.','吞没，淹没'),('n.','燕子')],
      [(0,'The pills should be swallowed whole.','这些药要吞服。','swallowed','例',211),
       (1,'I watched her walk down the road until she was swallowed by the darkness.','我看着她沿公路越走越远，直至消失在黑暗中。','swallowed','例',211)],
      's（联想成“蛇”）+ wal（联想成wall“墙”）+ low（低的）→在低矮的墙上有一条蛇，它想要“吞下”那些“燕子”。')
    group='13 -vive-相关词汇'
    a('vivid','/ˈvɪvɪd/','adj. 生动的，逼真的；鲜艳的；鲜明的',211,
      [('adj.','生动的，逼真的'),('adj.','鲜明的'),('adj.','鲜艳的')],
      [(0,'He gave a vivid account of his life as a fighter pilot.','他生动地描述了他作为战斗机飞行员的生活。','vivid','例',211),
       (1,'Powerful memory doesn’t make my emotions any more acute or vivid.','强大的记忆并不能让我的情感更为强烈或更为鲜明。','vivid','真题',211)],
      '发音类似“娓娓地”→娓娓地道来，很生动→生动的。')
    a('survive','/səˈvaɪv/','v. 幸免于，幸存，生还；生存；比……活的时间长',211,
      [('v.','幸免于，幸存，生还'),('v.','生存'),('v.','比……活的时间长')],
      [(0,'She survived through two world wars.','她经历了两次世界大战而幸存。','survived','例',211),
       (1,'Some strange customs have survived from earlier times.','有些奇怪的风俗是从早年留存下来的。','survived','例',211)],
      'sur（在……上）+ vive（活）→他在战场上活了下来→幸存。',
      [('survivor','n. 生还者，幸存者',211),('survival','n. 幸存，生存；残存物',212)])
    t.pending('survive',1,'本句风俗留存的引申义未明列在原书生存等释义中，原文原译保留待核。')
    include_page(212)
    material('survivor',211,'例',pdf_pages=[211,212],english='Many firms will die, but the survivors will emerge leaner and stronger than before.',translation='许多公司将倒闭，但幸存者将变得比以前更加精干和强大。')
    material('survival',212,'例',english='Everybody needs some sleep for survival.',translation='每个人都需要睡眠才能生存。')
    a('revive','/rɪˈvaɪv/','v. 复活，苏醒；重新使用',212,
      [('v.','复活，苏醒'),('v.','重新使用')],
      [(0,'But rainfall can revive them in a matter of hours.','但是降雨可以在几个小时内使它们复活。','revive','例',212),
       (0,'And, unless banks carry toxic assets at prices that attract buyers, reviving the banking system will be difficult.','而且，如果银行不能够以吸引买家的价格出售不良资产，银行系统的复苏将会非常困难。','reviving','真题',212)],
      're（再，又）+ vive（活）→又活一遍→复活，苏醒。')
    t.pending('revive',1,'reviving the banking system为经济系统复苏的引申用法，原书释义未明确列，保留原文原译待核。')
    group='14 居住、住所相关词汇'
    a('shelter','/ˈʃeltə(r)/','n. 居所；遮蔽；避难所；v. 掩蔽，庇护',212,
      [('n.','居所'),('n.','遮蔽；避难所'),('v.','掩蔽，庇护')],
      [(0,'They were anxious to find shelter for the night.','他们急于找个地方过夜。','shelter','例',212),
       (1,'People were desperately seeking shelter from the gunfire.','人们拼命地找地方躲避炮火。','shelter','例',212)],
      '发音类似“歇（休息）了他”→为了救助难民，他实在太累了，在“避难所”休息一下。')
    a('reside','/rɪˈzaɪd/','v. 居住在；定居于',212,
      [('v.','居住在；定居于')],
      [(0,'Their passports do not give them the right to reside in Britain.','他们的护照没有给予他们在英国居住的权利。','reside','例',212)],
      related=[('residence','n. 居住，住处',212)])
    material('residence',212,'例',english='They had entered the country and had applied for permanent residence.',translation='他们已经入境该国，并申请了永久居住权。')
    a('resident','/ˈrezɪdənt/','n. 居民，住户；adj. 居住的',212,
      [('n.','居民，住户'),('adj.','居住的')],
      [(0,'The proposals sparked concern among local residents.','这些提议引起了当地居民的担忧。','residents','例',212),
       (1,'She has been resident abroad for years.','她侨居国外多年。','resident','例',212)])
    a('preside','/prɪˈzaɪd/','v. 主持，担任会议主席',212,
      [('v.','主持，担任会议主席')],
      [(0,'The special workshop was presided over by a famous scientist.','那次专题研讨会是由一位著名的科学家主持的。','presided','例',212)],
      '总统（president）需要主持（preside）很多会议。',
      [('president','n. 会长；院长；总裁；总统',212)])
    a('inhabit','/ɪnˈhæbɪt/','v. 居住于，栖息于',212,
      [('v.','居住于，栖息于')],
      [(0,'Mammals, such as dolphins, whales, seals inhabit the sea.','像海豚、鲸、海豹之类的哺乳动物均栖息于大海之中。','inhabit','例',212),
       (0,'Some of the rare species that inhabit the area are under threat.','栖息在这个地区的一些珍稀物种正面临威胁。','inhabit','例',213)],
      'in（里面）+ habit（习惯）→人一般都习惯居住在家里面→居住于，栖息于。',
      [('inhabitant','n. 居民，居住者；栖息动物',213)])
    material('inhabitant',213,'例',english='We will try to give cheap electric energy and heat to every inhabitant of the world.',translation='我们努力向全世界每位居民提供廉价的电能和热能。')
    a('habitat','/ˈhæbɪtæt/','n. 栖息地；生活环境',213,
      [('n.','栖息地'),('n.','生活环境')],
      [(0,'The panda’s natural habitat is the bamboo forest.','大熊猫的天然栖息地是竹林。','habitat','例',213),
       (0,'The fund will also be used to compensate landowners who set aside habitat.','该基金还将用于补偿那些留出栖息地的土地所有者。','habitat','真题',213)])
    group='15 collapse近义及形近词'
    a('breakdown','/ˈbreɪkdaʊn/','n. 破裂，失败；损坏，故障',213,
      [('n.','损坏，故障'),('n.','破裂，失败')],
      [(0,'The national breakdown organizations are on hand to help motorists 24 hours a day.','全国维修故障机构全天24小时为驾车者服务。','breakdown','例',213),
       (1,'The breakdown of the negotiations was not unexpected.','谈判的失败是预料之中的事。','breakdown','例',213)])
    a('collapse','/kəˈlæps/','n. & v. 倒塌；崩溃；突然失败；突然降价',213,
      [('v.','倒塌；崩溃'),('v.','突然失败'),('v.','突然降价'),('n.','倒塌；崩溃'),('n.','突然失败'),('n.','突然降价')],
      [(0,'The roof collapsed under the weight of snow.','房顶在雪的重压下突然坍塌下来。','collapsed','例',213),
       (0,'Integrity had collapsed, she argued, because of a collective acceptance that the only “sorting mechanism” in society should be profit and the market.','她认为，正直已经崩溃，因为人们普遍认为，社会中唯一的“分类机制”应该是利润和市场。','collapsed','真题',213)],
      'col（共同）+ laps（滑，滑走）+ e→一起滑落→倒塌。')
    a('elapse','/ɪˈlæps/','v. （时间）消逝，流逝',213,
      [('v.','（时间）消逝，流逝')],
      [(0,'Many years had elapsed before they returned to their original urban areas.','许多年过去了，他们才回到原来的城市地区。','elapsed','例',213)],
      'e（出）+ laps（滑，滑走）+ e→滑出去了→消逝，流逝。')
    group='16 avenue相关形近词'
    a('avenue','/ˈævənjuː/','n. 大街；林荫大道；选择',213,
      [('n.','大街'),('n.','林荫大道'),('n.','选择')],
      [(0,'The avenues of the city were crowded with people.','城里大街上挤满了人。','avenues','例',213),
       (1,'A mile-long avenue of lime trees leads to the house.','一英里长的石灰树大道通向房子。','avenue','例',213)])
    t.pending('avenue',1,'原译石灰树疑为lime trees逐字误译，保留原文原译待核，不进入学习队列。')
    a('revenue','/ˈrevənjuː/','n. 税收，财政收入；收益',213,
      [('n.','收益'),('n.','税收，财政收入')],
      [(0,'The company’s annual revenues rose by 30%.','公司的年收入增加了30%。','revenues','例',213),
       (0,'Tourism is the island’s main source of revenue.','旅游业是该岛的主要收入来源。','revenue','例',213)],
      're（回）+ ven（来）+ ue→回来的东西→收入。')
    group='17 重、轻相关词汇'
    a('grave','/ɡreɪv/','n. 墓穴，坟墓；adj. 严重的；严肃的',214,
      [('n.','墓穴，坟墓'),('adj.','严重的'),('adj.','严肃的')],
      [(0,'He did die as a pauper and was buried in an unmarked grave.','他死的时候是个穷光蛋，葬在一处无名墓穴中。','grave','例',214),
       (1,'This heavy rain could have grave consequences.','这场大雨会造成严重后果。','grave','例',214)],
      related=[('gravity','n. 严重性；严肃；重力',214)])
    a('aggravate','/ˈæɡrəveɪt/','v. 加重，使恶化；激怒',214,
      [('v.','加重，使恶化'),('v.','激怒')],
      [(0,'Pollution can aggravate asthma.','污染会使哮喘加重。','aggravate','例',214),
       (0,'Their negative reactions have greatly aggravated the situation.','他们的消极反应使形势严重恶化。','aggravated','例',214)],
      'ag（表示“加强”）+ grav（=grave“重”）+ ate（动词后缀）→一再地变严重→使恶化，加重。')
    a('grind','/ɡraɪnd/','v. 磨；磨碎，碾碎；使锋利；磨光；n. 刺耳的摩擦声',214,
      [('v.','磨；磨碎，碾碎'),('v.','使锋利'),('v.','磨光'),('n.','刺耳的摩擦声')],
      [(0,'The flour is ground using traditional methods.','这面粉是用传统方法磨制而成。','ground','例',214),
       (0,'The animal has teeth that grind its food into a pulp.','这种动物有把食物磨成浆的牙齿。','grind','例',214)])
    a('grieve','/ɡriːv/','v. 悲伤，使伤心',214,
      [('v.','使伤心'),('v.','悲伤')],
      [(0,'Their lack of interest grieved her.','他们不感兴趣使她很痛心。','grieved','例',214),
       (1,'I didn’t have any time to grieve.','我没有时间去悲伤。','grieve','例',214)],
      '发音类似“贵啊”→这件衣服好贵啊，我花了好多钱，好伤心啊→使伤心。')
    a('relieve','/rɪˈliːv/','v. 减轻，缓和，缓解',214,
      [('v.','减轻，缓和，缓解')],
      [(0,'Unfortunately, there is little that can be done to relieve muscle soreness.','不幸的是，几乎没有什么可以减轻肌肉酸痛的方法。','relieve','例',214),
       (0,'On July 29th they were relieved, at least temporarily.','7月29日，他们松了一口气，至少是暂时的。','relieved','真题',214)],
      '发音类似“热离我”→发热远离我，就可以缓解我的症状→减轻，缓解。',
      [('relief','n. 轻松；（痛苦等的）减轻；救济',214)])
    t.pending('relieve',1,'relieved为松了一口气的状态用法，原书主释义未列使宽慰等义，原文原译保留待核。')
    material('relief',214,'例',english='After the exam, I felt an incredible sense of relief.',translation='考试过后，我感到无比轻松。')
    a('alleviate','/əˈliːvieɪt/','v. 减轻，缓和，缓解',214,
      [('v.','减轻，缓和，缓解')],
      [(0,'A number of measures were taken to alleviate the problem.','采取了一系列措施缓解这个问题。','alleviate','例',214),
       (0,'The company alleviated some of the damage from its recall crisis earlier this year with a relatively quick and well-orchestrated social-media response campaign.','该公司今年早些时候通过相对迅速和精心策划的社交媒体回应活动，减轻了召回危机造成的部分损失。','alleviated','真题',214)],
      'al（加强）+ levi（变轻）+ ate（动词后缀）→不断变轻→减轻。')
    include_page(215)
