"""Visual transcription of seventh-unit headwords beginning on PDF215–219."""
COMPLETE_THROUGH = 219
NEXT_WORD = 'autonomy'
NEXT_PAGE = 220

def append(t,associated):
    group='17 重、轻相关词汇'
    def a(spelling,ipa,definition,page,meanings,examples,mnemonic='',related=()):
        t.add(2314+len(t.words),spelling,ipa,definition,page,group,meanings,examples,mnemonic,related)
        t.words[-1]['book_unit_id']='unit-007'
    def material(word,page,label,**kw):
        associated.append(dict(word=word,pdf_page=page,label=label,**kw))
    def include_page(page):
        w=t.words[-1]; w['pdf_pages']=sorted(set(w['pdf_pages']+[page]))
        w['printed_pages']=[f'{p-8:03}' for p in w['pdf_pages']]

    a('ease','/iːz/','n. 舒适，轻松；v. 减轻，缓和',215,
      [('n.','舒适，轻松'),('v.','减轻，缓和')],
      [(0,'He doesn’t feel at ease in the firm.','他在公司里感到不自在。','ease','例',215),
       (1,'Environmental problems must be solved to ease the current global food shortage.','必须通过解决环境问题来缓解当前的全球粮食短缺。','ease','例',215)],
      '发音类似“椅子”→他坐在椅子上，怡然自得，证明状态“舒适”→舒适，轻松。')
    material('uneasy',215,'拓展',phonetic='/ʌnˈiːzi/',definition='adj. 心神不安的，担心的')
    group='18 “gr”相关语境词汇'
    a('grateful','/ˈɡreɪtfl/','adj. 感激的，感谢的',215,
      [('adj.','感激的，感谢的')],
      [(0,'She said she was grateful for the support offered by the community.','她说她很感激社区给予的支持。','grateful','例',215),
       (0,'Instead, being grateful for small things every day is a much better way to improve wellbeing.','相反，对每天的小事心存感激是一个更好的提高幸福感的方法。','grateful','真题',215)],
      '如果你让一个人（gr联想成一个人）吃（ate）饱（ful联想成full）了，他就会“感谢”你→感激的，感谢的。',
      [('gratitude','n. 感激之情；感谢',215)])
    material('gratitude',215,'例',phonetic='/ˈɡrætɪtjuːd/',definition='n. 感激之情；感谢',english='Her eyes were immediately filled with gratitude.',translation='她的眼里立刻充满了感激之情。')
    material('thankful',215,'拓展',phonetic='/ˈθæŋkfl/',definition='adj. 感谢；欣慰')
    a('grant','/ɡrɑːnt/','n. 拨款；v. 同意，准予；承认',215,
      [('n.','拨款'),('v.','同意，准予'),('v.','承认')],
      [(0,'She won a grant to develop her own business.','她赢得了一笔拨款，用以发展自己的企业。','grant','例',215),
       (1,'International tax rules do not grant them that right.','国际税收规则没有赋予他们那种权利。','grant','真题',215)])
    material('take... for granted',215,'拓展',definition='认为……理所当然')
    material('take... for granted',215,'真题',english='Americans stopped taking prosperity for granted.',translation='美国人不再把繁荣视为理所当然。')
    a('analogy','/əˈnælədʒi/','n. 类比，比拟，类推',215,
      [('n.','类比，比拟，类推')],
      [(0,'The doctor drew an analogy between the human heart and a pump.','这位医生把心脏比作泵。','analogy','例',215),
       (0,'We can understand this theory by analogy with human beings.','我们用人来作类比就能理解这个理论了。','analogy','例',215)],
      'an（一个）+ a（一个）+ logy（发音类似“逻辑”）→从一个逻辑推理到另一个逻辑叫“类比”推理→类比，类推。',
      [('analogous','adj. 类似的，相似的',215)])
    material('analogous',215,'派生',phonetic='/əˈnæləɡəs/',definition='adj. 类似的，相似的')
    group='19 “bench”相关形近词'
    a('bench','/bentʃ/','n. 长凳，长椅；法官；法官席位',215,
      [('n.','长凳，长椅'),('n.','法官'),('n.','法官席位')],
      [(0,'We sat at either end of a long bench.','我们坐在一张长凳的两端。','bench','例',216),
       (1,'His lawyer turned to address the bench.','他的律师转身对法官讲话。','bench','例',216)],
      '他坐在沙滩（beach）上的长凳（bench）上。')
    a('bend','/bend/','v. 使弯曲，折弯；使倾斜；n. 弯道，拐弯',216,
      [('v.','使弯曲，折弯'),('v.','使倾斜'),('n.','弯道，拐弯')],
      [(0,'Bend your knees, keeping your back straight.','膝盖弯曲，保持背部挺直。','Bend','例',216),
       (2,'He lost control on a bend and crashed into a tree.','他在拐弯处失控，撞到了一棵树上。','bend','例',216)],
      'b这个字母最后（end）变成了d，不就是“弯曲”的结果吗？')
    group='20 “捆绑”相关词汇'
    a('bond','/bɑːnd/','n. 纽带；联系，关系；契合；债券，公债',216,
      [('n.','纽带；联系，关系'),('n.','契合'),('n.','债券，公债')],
      [(0,'It will help strengthen their emotional bonds.','这将有助于加强他们的情感纽带。','bonds','例',216)],
      '发音类似“绑的”→绑在一起的，就是有“联系”的→联系，关系。')
    a('bind','/baɪnd/','v. 捆绑，结合；约束',216,
      [('v.','捆绑，结合'),('v.','约束')],
      [(0,'She was bound to a chair.','她被捆在一把椅子上。','bound','例',216),
       (1,'Laws and regulations are used to bind citizens’ behaviors.','法律和规则是用来约束公民的行为。','bind','例',216)])
    group='21 “bound”形近词'
    a('bound','/baʊnd/','n. 跳跃；adj. 一定会，很可能会；有义务；受约束；v. 跳跃着跑',216,
      [('n.','跳跃'),('adj.','一定会，很可能会'),('adj.','有义务；受约束'),('v.','跳跃着跑')],
      [(2,'You are bound by the contract to pay before the end of the month.','按照合同规定，你必须在月底前付款。','bound','例',216),
       (1,'You are bound to lose all your friends if you continue cheating them.','如果你再继续欺骗朋友的话，你一定会失去你所有的朋友。','bound','例',216)],
      '发音类似“蹦跶”→小时候我妈妈常说：“你可以蹦跶，但是不能超越我容忍的限度。”言外之意是：你可以要自由，但是要在一定的范围内→跳跃；受约束。')
    a('abound','/əˈbaʊnd/','v. 有许多；大量存在',216,
      [('v.','有许多；大量存在')],
      [(0,'Stories about his travels abound.','有关他游历的故事多得很。','abound','例',216),
       (0,'As the economy picks up, opportunities will abound for aspiring leaders.','随着经济的复苏，有抱负的领导人将获得大量机会。','abound','真题',216)],
      '发音类似“啊棒的”→这里到处都是玩具，对于小朋友来说是很棒的→大量存在。')
    group='22 “auction”近义词及形近词'
    a('bid','/bɪd/','n. & v. 出价，投标；努力争取；叫牌',216,
      [('n.','出价，投标'),('n.','努力争取'),('n.','叫牌'),('v.','出价，投标'),('v.','努力争取'),('v.','叫牌')],
      [(0,'They have invited bids for the property.','他们为这块地产招标。','bids','例',217),
       (1,'Parents would be looking at their emails while the children would be making excited bids for their attention.','家长们会看他们的电子邮件，而孩子们会兴奋地努力争取他们的注意。','bids','真题',217)])
    a('auction','/ˈɔːkʃn/','n. & v. 拍卖',217,
      [('n.','拍卖'),('v.','拍卖')],
      [(1,'He auctioned all his collection of stamps.','他把他收集的所有邮票都拍卖掉了。','auctioned','例',217)])
    material('auction houses',217,'拓展',definition='拍卖行')
    a('sanction','/ˈsæŋkʃn/','n. 批准，同意；制裁；处罚；v. 批准，同意；惩罚',217,
      [('n.','批准，同意'),('n.','制裁'),('n.','处罚'),('v.','批准，同意'),('v.','惩罚')],
      [(1,'Trade sanctions were imposed against any country that refused to sign the agreement.','凡拒签该协议的国家均受到贸易制裁。','sanctions','例',217)])
    group='23 fasten跟fast没什么关系哦'
    a('fasten','/ˈfɑːsn/','v. 系牢，扎牢',217,
      [('v.','系牢，扎牢')],
      [(0,'Please fasten your seat belts.','请系好安全带。','fasten','例',217),
       (0,'The garment is fastened with a sash.','这件衣服是用腰带系住的。','fastened','例',217)])
    group='24 “squeeze”形近词'
    a('squeeze','/skwiːz/','n. & v. 挤压，捏',217,
      [('v.','挤压，捏'),('n.','挤压，捏')],
      [(0,'Cut the lemon in half and squeeze the juice into the bowl.','把柠檬一切为二，将汁挤到碗里。','squeeze','例',217),
       (1,'He gave my hand a little squeeze.','他轻轻捏了捏我的手。','squeeze','例',217)],
      '发音类似“死贵死”→想买件衣服，价格太贵，你就往下“压”价啊，能便宜些吗？→挤，压。')
    a('breeze','/briːz/','n. 微风，轻风；轻而易举的事',217,
      [('n.','微风，轻风'),('n.','轻而易举的事')],
      [(0,'The flowers were gently swaying in the breeze.','花儿在微风中轻轻舞动。','breeze','例',217),
       (1,'Going down the hill would be a breeze after the long climb up!','爬了很长一段路后，下山是轻而易举的事。','breeze','例',217)],
      '微风（breeze）吹拂，我感觉有点冷，打了个喷嚏（sneeze）。')
    a('freeze','/friːz/','v. 冻住，结冰；冰冻；惊呆',217,
      [('v.','冻住，结冰；冰冻'),('v.','惊呆')],
      [(0,'It’s so cold that even the river has frozen.','天气冷得河都封冻了。','frozen','例',217),
       (0,'The cold weather had frozen the ground.','寒冷的天气使地面都冻硬了。','frozen','例',217)],
      '和煦的微风（breeze）送走了寒冷的冰冻（freeze）。',
      [('freezing','adj. 极冷的，冰冻的；n. 冰点',217),('freezer','n. 冰箱，冷库',217)])
    material('freezing',217,'派生',phonetic='/ˈfriːzɪŋ/',definition='adj. 极冷的，冰冻的；n. 冰点')
    material('freezer',217,'派生',phonetic='/ˈfriːzər/',definition='n. 冰箱，冷库')
    group='25 “永久的”相关词汇'
    a('permanent','/ˈpɜːmənənt/','adj. 永久的，持久的；永恒的',217,
      [('adj.','永久的，持久的；永恒的')],
      [(0,'The accident has not done any permanent damage.','那场事故没有造成什么永久性损伤。','permanent','例',218),
       (0,'But the professional companies prospered in their permanent theaters, and university men with literary ambitions were quick to turn to these theaters as offering a means of livelihood.','但是专业公司在他们的固定剧院里蓬勃发展，而有文学抱负的大学生迅速投身这些剧院，并将其视为谋生的手段。','permanent','真题',218)],
      'per（每一）+ man（人）+ ent（联想为enter“进入”）→每一个人都希望进入永恒→永久的，持久的。')
    a('perpetual','/pəˈpetʃuəl/','adj. 永恒的，永久的；终身的；持续的',218,
      [('adj.','永恒的，永久的'),('adj.','终身的'),('adj.','持续的')],
      [(1,'She’s a perpetual student.','她是个终身学习者。','perpetual','例',218),
       (2,'Government and parliament are in a state of perpetual conflict.','政府和议会处于长期冲突状态。','perpetual','例',218)])
    a('eternal','/ɪˈtɜːnl/','adj. 永恒的，永远的',218,
      [('adj.','永恒的，永远的')],
      [(0,'A wedding ring is a symbol of eternal love.','结婚戒指是永恒爱情的象征。','eternal','例',218),
       (0,'The two heroes swore eternal friendship.','两位主人公发誓永远做朋友。','eternal','例',218)])
    group='26 “渗透、渗出”相关词汇'
    a('permeate','/ˈpɜːmieɪt/','v. 弥漫，渗透；扩散，传播',218,
      [('v.','弥漫，渗透'),('v.','扩散，传播')],
      [(0,'The smell of leather permeated the room.','屋子里弥漫着皮革的气味。','permeated','例',218),
       (0,'Eventually, the water will permeate through the surrounding concrete.','最终，水会渗透进周围的混凝土中。','permeate','例',218),
       (0,'Democratic values and gender-equality permeate the curriculum.','民主价值观和性别平等渗透在课程中。','permeate','例',218)],
      related=[('permeation','n. 渗透；弥漫',218)])
    material('permeation',218,'派生',phonetic='/ˌpɜːmiˈeɪʃn/',definition='n. 渗透；弥漫')
    a('penetrate','/ˈpenətreɪt/','v. 渗透，进入，穿过',218,
      [('v.','渗透，进入，穿过')],
      [(0,'The sun’s radiation penetrates the skin.','太阳的辐射能透进皮肤。','penetrates','例',218),
       (0,'Without those masses of cooling sea ice, warm air brought to the Arctic can penetrate further inland than it ever did before.','如果没有那些大量的海冰，进入北极的暖空气可以比以往更深入内陆。','penetrate','例',218)],
      'pe（发音类似“拍”）+ net（网络）+ rate（速度）→你的电脑死机了，你一直拍电脑，想“进入”网络。')
    a('sweat','/swet/','n. 汗水；艰苦的劳动；v. 出汗；艰苦努力',218,
      [('n.','汗水'),('n.','艰苦的劳动'),('v.','出汗'),('v.','艰苦努力')],
      [(0,'Their bodies were soaked in sweat.','他们的身体被汗水浸湿了。','sweat','例',218),
       (2,'The palms of his hands began to sweat.','他的手掌开始出汗。','sweat','例',218)],
      '以后的甜蜜（sweet）就是今天的汗水（sweat）换来的。')
    group='27 “陡峭、垂直”相关词汇'
    a('steep','/stiːp/','adj. 陡峭的，险峻的；急剧的；过高的',218,
      [('adj.','陡峭的，险峻的'),('adj.','急剧的'),('adj.','过高的')],
      [(0,'The path grew steeper as we climbed higher.','我们越往上爬路就越陡。','steeper','例',219),
       (1,'Part of the issue is that the government did not anticipate the steep increase in airline travele.','部分问题是政府没有预料到航空旅行的急剧增长。','steep','真题',219)],
      's + tee（发音类似“提”）+ p（发音类似“坡”）→提着心就是很小心，很小心地上坡，估计坡很陡峭吧→陡峭的。')
    t.pending('steep',1,'原书句末印为travele，疑为travel拼写错误，保留原文原译待核。')
    a('cliff','/klɪf/','n. 悬崖，峭壁',219,
      [('n.','悬崖，峭壁')],
      [(0,'The cliff is gradually crumbling away.','峭壁正在逐渐坍塌。','cliff','例',219),
       (0,'We set off along the cliff path.','我们沿着悬崖小路出发了。','cliff','例',219)],
      '发音类似“可立扶”→设想你站在“悬崖”边，快掉下去的时候，可以立刻扶住旁边的一棵树→悬崖，峭壁。')
    a('vertical','/ˈvɜːtɪkl/','adj. 垂直的，直立的，纵向的；n. 垂直线',219,
      [('adj.','垂直的，直立的，纵向的'),('n.','垂直线')],
      [(0,'The cliff was almost vertical.','那悬崖几乎是笔直的。','vertical','例',219),
       (0,'There was a vertical drop to the ocean.','至海洋有一段垂直落差。','vertical','例',219)],
      '发音类似“我体考”→我在体考中做“垂直”引体向上→垂直的。')
    group='28 “economy”相关词汇'
    a('economy','/ɪˈkɒnəmi/','n. 经济；节约；国家',219,
      [('n.','经济'),('n.','节约'),('n.','国家')],
      [(0,'Tourism clearly dominates the local economy.','旅游业明显主导着当地经济。','economy','例',219),
       (0,'Government measures to slow the economy failed to curb fuel demand growth.','政府控制经济增速的措施未能遏制燃油需求的增加。','economy','例',219)],
      related=[('economic','adj. 经济的，经济上的',219),('economist','n. 经济学家',219)])
    material('economic',219,'例',phonetic='/ˌiːkəˈnɒmɪk/',definition='adj. 经济的，经济上的',english='Political power depends upon economic strength.',translation='政治权力取决于经济实力。')
    material('economist',219,'派生',phonetic='/ɪˈkɒnəmɪst/',definition='n. 经济学家')
    a('economical','/ˌiːkəˈnɒmɪkl/','adj. 经济的，实惠的；节俭的；简洁的',219,
      [('adj.','经济的，实惠的'),('adj.','节俭的'),('adj.','简洁的')],
      [(0,'Solid fuel would be more economical.','固体燃料会更加经济。','economical','例',219),
       (0,'Fans of electric cars say they are clean, quiet, and economical.','电动车爱好者说电动车无污染，无噪声，而且经济。','economical','例',219)],
      related=[('economically','adv. 经济上；节约地',219)])
    material('economically',219,'例',phonetic='/ˌiːkəˈnɒmɪkli/',definition='adv. 经济上；节约地',english='Services could be operated more efficiently and economically.',translation='可以更有效、更经济地提供服务。')
    a('economics','/ˌiːkəˈnɒmɪks/','n. 经济学；经济情况',219,
      [('n.','经济学'),('n.','经济情况')],
      [(0,'He studied politics and economics at Yale.','他曾在耶鲁大学学习政治学和经济学。','economics','例',219),
       (0,'They may cooperate directly in the growing number of international projects related to science, economics and industry.','他们可能在日益增多的与科学、经济学和工业有关的跨国项目中直接合作。','economics','真题',219)])
    a('thrift','/θrɪft/','n. 节约，节俭',219,
      [('n.','节约，节俭')],
      [(0,'Thrift has become the prevailing practice.','节约成风。','Thrift','例',220),
       (0,'We should oppose extravagant eating and drinking and pay attention to thrift and economy.','我们应该反对大吃大喝并注意节俭。','thrift','例',220)])
