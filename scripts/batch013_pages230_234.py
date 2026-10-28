"""Visual transcription of seventh-unit headwords beginning on PDF230–234."""
COMPLETE_THROUGH = 234
NEXT_WORD = 'basis'
NEXT_PAGE = 235
# PDF234 is the eighth-unit title page; seventh-unit entries end with instrument on PDF233.

def append(t,associated):
    group='43 “部门、会议”相关语境词汇'
    def a(spelling,ipa,definition,page,meanings,examples,mnemonic='',related=()):
        t.add(2314+len(t.words),spelling,ipa,definition,page,group,meanings,examples,mnemonic,related)
        t.words[-1]['book_unit_id']='unit-007'
    def material(word,page,label,**kw):
        associated.append(dict(word=word,pdf_page=page,label=label,**kw))
    def include_page(page):
        w=t.words[-1];w['pdf_pages']=sorted(set(w['pdf_pages']+[page]))
        w['printed_pages']=[f'{p-8:03}' for p in w['pdf_pages']]

    a('session','/ˈseʃn/','n. 一场，一节；会议；（法庭的）开庭；（议会等的）会议',230,
      [('n.','一场，一节'),('n.','（法庭的）开庭'),('n.','会议；（议会等的）会议')],
      [(0,'We have both elementary and advanced training sessions.','我们有初级和高级培训课程。','sessions','例',230),
       (1,'The court is now in session.','法庭现在正在开庭。','session','例',230)],
      '发音类似“塞心”→一想到这周要开这么多的“会议”，我就感觉心塞→会议。')
    a('minister','/ˈmɪnɪstə(r)/','n. 部长，大臣；牧师',230,
      [('n.','部长，大臣'),('n.','牧师')],
      [(0,'The minister advised him to leave as soon as possible.','部长建议他尽快离开。','minister','例',230),
       (0,'He has been successfully elected Prime Minister.','他已成功当选首相。','Minister','例',230)],
      'mini（小的）+ ster（表示“人”）→古代的一些“大臣”称自己为小人→大臣。')
    t.pending('minister',1,'本例Prime Minister整体意为首相，原书未单列该短语义，保留原文原译待核。')
    a('administer','/ədˈmɪnɪstə(r)/','v. 管理；执行；给予；提供',230,
      [('v.','管理'),('v.','执行'),('v.','给予；提供')],
      [(0,'The company’s finances have been admirably administered.','该公司的财务管理得很好。','administered','例',230)],
      'ad（去，往）+ minister（部长）→去当部长，“管理”部门，“执行”任务→管理，执行。',
      [('administration','n. 管理；执行；行政部门；（尤指美国）政府',230),('administrator','n. 管理人员，行政人员',230)])
    material('administration',230,'派生',phonetic='/ədˌmɪnɪˈstreɪʃn/',definition='n. 管理；执行；行政部门；（尤指美国）政府')
    material('administrator',230,'派生',phonetic='/ədˈmɪnɪstreɪtə(r)/',definition='n. 管理人员，行政人员')
    a('delegate','/ˈdelɪɡət/','n. 代表，参会人员；v. 授（权）',230,
      [('n.','代表，参会人员'),('v.','授（权）')],
      [(0,'Many a delegate was in favor of his proposal.','许多代表赞成他的建议。','delegate','例',230),
       (1,'Some managers find it difficult to delegate.','有些经理认为难以做到下放权力。','delegate','例',230)],
      related=[('delegation','n. 代表团；委托',230)])
    material('delegation',230,'派生',phonetic='/ˌdelɪˈɡeɪʃn/',definition='n. 代表团；委托')
    a('tutor','/ˈtjuːtə(r)/','n. 导师，指导教师；v. 指导，辅导',230,
      [('n.','导师，指导教师'),('v.','指导，辅导')],
      [(0,'He can serve as the woman’s tutor.','他可以担任该女士的指导教师。','tutor','例',230)],
      'tut（保护；指导，教育）+ or（表示“人”的名词后缀）→指导的人，教育的人→导师，指导教师。')
    a('tuition','/tjuˈɪʃn/','n. 学费；讲授，教学',230,
      [('n.','学费'),('n.','讲授，教学')],
      [(0,'Few can afford the tuition of $10,000 a term.','很少有人能够付得起一学期1万美元的学费。','tuition','例',230),
       (1,'She received private tuition in French.','她由私人教授法语。','tuition','例',230)],
      '发音类似“推身”→假设你想参加一个特长班，但是又不好意思问负责人“学费”多少，就往前推着你朋友的身体，让他帮你问→学费。')
    group='44 “概念”相关词汇'
    a('notion','/ˈnəʊʃn/','n. 信念，观念，想法；理解',230,
      [('n.','信念，观念，想法'),('n.','理解')],
      [(0,'Online culture thinks highly of the notion that the information flowing onto the screen comes there by specific request.','网上文化推崇这样一种理念，即在你提出具体的要求之后，信息才会出现在屏幕上。','notion','例',231),
       (1,'He has no notion of the difficulty of the problem.','他不知道这个问题有多难。','notion','例',231)],
      '发音类似“闹心”→我女儿最近有个“想法”，就是长大后要去离家特别远的地方工作，这个“想法”让我很闹心。')
    a('concept','/ˈkɒnsept/','n. 观念，概念',231,
      [('n.','观念，概念')],
      [(0,'They radically changed people’s concept of beauty.','他们从根本上改变了人们对美的观念。','concept','例',231)],
      'New Concept English《新概念英语》我们很熟悉，那concept就是“概念”。')
    group='45 “学校”相关语境词汇'
    a('academic','/ˌækəˈdemɪk/','n. 大学教师，学者；adj. 学业的，学术的',231,
      [('adj.','学业的，学术的'),('n.','大学教师，学者')],
      [(0,'Maintaining high academic standards should be the priority of a responsible university.','维持高水平的学术标准才是一个负责任的大学应当首先考虑的事情。','academic','例',231)],
      'aca（发音类似“挨个”）+ dem（发音类似“点名”）+ ic→这位“大学老师”一上课就开始挨个点名。')
    a('academy','/əˈkædəmi/','n. 专科院校；研究院',231,
      [('n.','专科院校'),('n.','研究院')],
      [(0,'She trained at the Royal Academy of Music.','她在皇家音乐学院培训过。','Academy','例',231)])
    material('Chinese Academy of Sciences',231,'拓展',definition='中国科学院')
    a('punctual','/ˈpʌŋktʃuəl/','adj. 按时的，准时的',231,
      [('adj.','按时的，准时的')],
      [(0,'He is always punctual for his class.','他上课总是很准时。','punctual','例',231)],
      'punct（点；变尖）+ ual（有……性质的）→卡在点上的→准时的。')
    a('epidemic','/ˌepɪˈdemɪk/','n. 流行病；泛滥；adj. 流行性的，极为盛行的',231,
      [('n.','流行病'),('n.','泛滥'),('adj.','流行性的，极为盛行的')],
      [(0,'Over fifty people died during the flu epidemic last winter.','在去年冬天的一场流感中有50多人丧生。','epidemic','例',231)],
      'epi（发音类似“爱扑”）+ demic（联想成academic“学术上”）→爱扑在学术研究上，现在在大学里面是很“流行的”。')
    a('scholar','/ˈskɒlə(r)/','n. 学者；奖学金获得者',231,
      [('n.','学者'),('n.','奖学金获得者')],
      [(0,'The prize attracts thousands of scholars and researchers.','这个奖项吸引了成千上万的学者和研究人员。','scholars','例',231)],
      'schol（联想成school“学校”）+ ar（表示“人”的名词后缀）→学校的人→学习的人，钻研学术的人→学者。',
      [('scholarship','n. 奖学金；学术研究',231)])
    include_page(232)
    material('scholarship',231,'派生',phonetic='/ˈskɒləʃɪp/',definition='n. 奖学金；学术研究')
    material('scholarship',231,'例',pdf_pages=[231,232],english='She won a scholarship to study at Stanford.',translation='她获得了奖学金，得以在斯坦福大学求学。')
    a('forum','/ˈfɔːrəm/','n. 论坛，讨论会',232,
      [('n.','论坛，讨论会')],
      [(0,'We will be hosting a two-day forum on childcare.','我们将主办为期两天的儿童保育讨论会。','forum','例',232)],
      'for（为了）+ um（字母谐音，联想成“有名”）→为了变得有名，我经常在“论坛”或“讨论会”上进行辩论→论坛，讨论会。')
    group='46 “board”近义词及形近词'
    a('panel','/ˈpænl/','n. 控制板，仪表盘；专家咨询组；（广播、电视上的）讨论小组',232,
      [('n.','控制板，仪表盘'),('n.','专家咨询组'),('n.','（广播、电视上的）讨论小组')],
      [(0,'A red light flashed on the control panel.','控制面板上的一只红灯在闪。','panel','例',232),
       (1,'The panel then informally accepted several general conclusions, although some details have not been settled.','该小组非正式地接受了几项一般性的结论，尽管有些细节还有待解决。','panel','真题',232)])
    a('board','/bɔːd/','n. 板，木板；董事会，委员会；伙食；v. 上船（或火车、飞机等）；付费（在某人家里）膳宿',232,
      [('n.','董事会，委员会'),('n.','伙食'),('n.','板，木板'),('v.','上船（或火车、飞机等）'),('v.','付费（在某人家里）膳宿')],
      [(0,'He’s on the board of directors.','他是董事会成员。','board','例',232),
       (1,'She pays $100 a week board and lodging.','她每周支付100美元的食宿费。','board','例',232)],
      '这个单词可以结合我们熟悉的blackboard（黑板）来记忆，black是“黑”，board就是“板”了。')
    t.pending('board',1,'原书pays $100 a week board and lodging疑漏介词for，保留原文原译待核。')
    a('aboard','/əˈbɔːd/','adv. & prep. 登机；上船',232,
      [('adv.','登机；上船'),('prep.','登机；上船')],
      [(0,'Welcome aboard!','欢迎登机！','aboard','例',232)],
      'a（一个）+ board（板子）→你登船的时候，需要通过一个板子→上船。')
    group='47 “课程”相关语境词汇'
    a('seminar','/ˈsemɪnɑː(r)/','n. 研讨课，研讨会，培训会',232,
      [('n.','研讨课，研讨会，培训会')],
      [(0,'Teaching is by lectures and seminars.','教学形式为讲座和研讨课。','seminars','例',232),
       (0,'Professor Mackay will give a seminar on Pound’s poetry.','麦凯教授将开设一个关于庞德诗歌的研讨课。','seminar','例',232)])
    a('curriculum','/kəˈrɪkjələm/','n. 课程',232,
      [('n.','课程')],
      [(0,'The school curriculum should be as broad as possible.','学校的课程应当尽可能广泛。','curriculum','例',232),
       (0,'All children should have access to the mainstream curriculum.','所有的孩子都应该有机会接触主流课程。','curriculum','例',232)])
    a('semester','/sɪˈmestə(r)/','n. 学期',232,
      [('n.','学期')],
      [(0,'I was finishing my last semester in college and trying to look for a job.','我当时即将结束最后一个学期的大学生活，正想找份工作。','semester','例',232),
       (0,'I spent a semester at the University of Madrid.','我在马德里大学待了一个学期。','semester','例',233)])
    group='48 “app-”相关词汇'
    a('apply','/əˈplaɪ/','v. 申请，请求；使用，应用',233,
      [('v.','使用，应用'),('v.','申请，请求')],
      [(0,'The new technology was applied to farming.','这项新技术已应用于农业。','applied','例',233),
       (1,'I have decided to apply for this new job.','我已经决定申请这份新工作。','apply','例',233)],
      related=[('application','n. 申请（书）',233)])
    material('application',233,'派生',phonetic='/ˌæplɪˈkeɪʃn/',definition='n. 申请（书）')
    a('applicant','/ˈæplɪkənt/','n. 申请人',233,
      [('n.','申请人')],
      [(0,'Employers require applicants to submit very personal information on background checks.','雇主要求求职者在背景调查中提交非常私人的信息。','applicants','例',233)])
    a('appliance','/əˈplaɪəns/','n. （家用）电器，器具',233,
      [('n.','（家用）电器，器具')],
      [(0,'Caution! Don’t turn on any electric appliance without permission.','注意！未经许可不得擅自开启任何电器设备。','appliance','例',233)])
    material('appliance',233,'例',status='quarantined',reason='原书本条第二例无appliance及其词形，隔离保存原文原译。',english='The information on the website should be treated with some caution.',translation='网站上的信息应该谨慎对待。')
    group='49 “器具、仪器”相关词汇'
    a('apparatus','/ˌæpəˈreɪtəs/','n. 器械，仪器；装置',233,
      [('n.','器械，仪器；装置')],
      [(0,'Firefighters needed breathing apparatus to enter the burning house.','消防队员需要呼吸器以便进入燃烧的大楼。','apparatus','例',233),
       (0,'Science departments say they are lacking basic apparatus.','理科系说他们缺少最基本的仪器。','apparatus','例',233)],
      'appar（联想成appear“出现”）+ a（一个）+ tus（吐丝）→以后不用春蚕吐丝了，出现了一个“仪器”来完成吐丝的工作→仪器。')
    a('device','/dɪˈvaɪs/','n. 装置，设备；手段',233,
      [('n.','装置，设备'),('n.','手段')],
      [(0,'The device has no new function.','这个设备没有新的功能。','device','例',233),
       (0,'Playing with digital device discourages kids from active discovery.','玩数字设备会阻碍孩子积极探索。','device','例',233)])
    t.pending('device',1,'原书digital device为无冠词的单数可数名词，疑有语法问题，原文原译保留待核。')
    a('equip','/ɪˈkwɪp/','v. 装备，配备；使有能力',233,
      [('v.','装备，配备'),('v.','使有能力')],
      [(0,'All riders are equipped with reflective vests and safety lights.','所有骑手都配有反光背心和安全灯。','equipped','例',233)],
      related=[('equipment','n. 装备，设备，器材',233)])
    material('equipment',233,'派生',phonetic='/ɪˈkwɪpmənt/',definition='n. 装备，设备，器材')
    material('equipment',233,'例',english='First, he bought new equipment for one of the departments.',translation='首先，他为其中一个部门购买了新设备。')
    a('instrument','/ˈɪnstrəmənt/','n. 工具，器具，仪器',233,
      [('n.','工具，器具，仪器')],
      [(0,'With creativity, even old-fashioned instruments may produce spectacular sound effects.','有了创造力，即使是老式乐器也能产生令人惊叹的音效。','instruments','例',233)])
    t.pending('instrument',0,'本例instruments指乐器，原书主释义未列乐器义，保留原文原译待核。')
