"""Visual transcription of ninth-batch headwords beginning on PDF135–139."""
COMPLETE_THROUGH = 139
NEXT_WORD = 'swear'
NEXT_PAGE = 140

def append(t, associated):
    group = '32 性格相关词汇'
    def a(spelling, ipa, definition, page, senses, examples, mnemonic='', related=()):
        t.add(1216+len(t.words), spelling, ipa, definition, page, group, senses, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-004'
    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))
    def include(page):
        w = t.words[-1]
        w['pdf_pages'] = sorted(set(w['pdf_pages']+[page]))
        w['printed_pages'] = [f'{p-8:03}' for p in w['pdf_pages']]

    a('personality', '/ˌpɜːsəˈnæləti/', 'n. 性格，个性，人格；气质；名人', 135,
      [('n.', '性格，个性，人格'), ('n.', '气质'), ('n.', '名人')],
      [(0, 'My outgoing personality has definitely helped me succeed.', '我外向的性格绝对帮助我取得了成功。', 'personality', '例', 135),
       (0, 'It takes a while to judge complex aspects of personality.', '要判断性格的复杂方面，需要一段时间。', 'personality', '真题', 135)])
    group = '33 circumstance形近词'
    a('circumstance', '/ˈsɜːkəmstəns/', 'n. 条件，情况；环境；境况', 135,
      [('n.', '条件，情况'), ('n.', '环境；境况')],
      [(0, 'Under normal circumstances, your white blood cells are able to fight infections.', '在正常情况下，你的白细胞能够抵抗感染。', 'circumstances', '例', 135),
       (1, 'You may feel guilt over your past, but you are poisoning the present with the things and circumstances you cannot change.', '你可能会对自己的过去感到内疚，但是你正在用你无法改变的事情和境况来荼毒你的现在。', 'circumstances', '真题', 135)],
      'circum（联想成circle“环绕”）+ stan（站）+ ce→环绕着你的东西不就是你生存的“环境”吗？→环境。')
    a('circulate', '/ˈsɜːkjəleɪt/', 'v. （液体或气体）环流，循环；传播，流传；传送', 135,
      [('v.', '（液体或气体）环流，循环'), ('v.', '传播，流传'), ('v.', '传送')],
      [(0, 'The condition prevents the blood from circulating freely.', '这种病阻碍了血液的循环畅通。', 'circulating', '例', 135),
       (1, 'Rumours began to circulate about his financial problems.', '有关他财务问题的谣言开始流传开来。', 'circulate', '例', 135)],
      'circul（环绕）+ ate（动词后缀）→不断地环绕→循环，环流。',
      [('circulation', 'n. 循环；传递；流传；流通', 135)])
    a('ventilate', '/ˈventɪleɪt/', 'v. 使（房间、建筑物等）通风；使通气；公开发表', 135,
      [('v.', '使（房间、建筑物等）通风；使通气'), ('v.', '公开发表')],
      [(0, 'The bathroom is ventilated by means of an extractor fan.', '这个浴室使用抽风扇通风。', 'ventilated', '例', 135),
       (0, 'The building is naturally ventilated.', '这栋楼依靠自然通风。', 'ventilated', '例', 135)],
      'vent（风）+ il + ate（动词后缀）→使通风。',
      [('ventilation', 'n. 通风；通风系统', 135)])
    a('accumulate', '/əˈkjuːmjəleɪt/', 'v. 积累，积聚；逐渐增加', 135,
      [('v.', '积累，积聚'), ('v.', '逐渐增加')],
      [(0, 'I seem to have accumulated a lot of books.', '我好像已经收集了很多书。', 'accumulated', '例', 135),
       (1, 'Debts began to accumulate.', '债务开始增加。', 'accumulate', '例', 135)],
      'ac（表示加强）+ cumul（积累）+ ate（动词后缀）→一直积累→积聚。')
    a('calculate', '/ˈkælkjuleɪt/', 'v. 计算，核算；预测，推测', 135,
      [('v.', '计算，核算'), ('v.', '预测，推测')],
      [(0, 'Use the formula to calculate the volume of the container.', '用公式计算容器的容积。', 'calculate', '例', 135),
       (1, 'Conservationists calculate that hundreds of species could be lost in this area.', '自然资源保护主义者预测，数以百计的物种可能会从这个地区消失。', 'calculate', '例', 136)],
      'cal（发音类似“开”）+ cu（联想到“聊天工具QQ”）+ late（晚的）→你准备今天晚上与在国外的朋友用QQ聊天，但是你算错了时差，没有聊成→计算。',
      [('calculator', 'n. 计算机，计算器', 136), ('calculation', 'n. 计算', 136)])
    material('calculation', 136, '例', english='Cathy did a rough calculation.', translation='凯茜做了一个粗略的计算。')
    a('calendar', '/ˈkælɪndə(r)/', 'n. 日历；历书；历法；日程表；重大事件', 136,
      [('n.', '日程表'), ('n.', '日历；历书；历法'), ('n.', '重大事件')],
      [(0, 'This is one of the biggest weeks in the racing calendar.', '这是全年赛马日程表中最重要的几个星期之一。', 'calendar', '例', 136),
       (1, 'In the last calendar year the company had a turnover of $426 million.', '在上一个日历年度里，该公司的营业额为4.26亿美元。', 'calendar', '例', 136)],
      '上班族每天拿着日历（calendar）数日子，算算（calculate）什么时候过年。')
    group = '34 农活、产量相关词汇'
    a('sow', '/səʊ/', 'v. 播（种）；散布', 136,
      [('v.', '播（种）'), ('v.', '散布')],
      [(0, 'Water well after sowing.', '播种后要浇足水。', 'sowing', '例', 136),
       (0, 'You reap what you sow.', '种瓜得瓜，种豆得豆。', 'sow', '例', 136)])
    a('reap', '/riːp/', 'v. 取得（成果）；收获', 136,
      [('v.', '取得（成果）；收获')],
      [(0, 'They are now reaping the rewards of all their hard work.', '现在，他们的全部辛劳都得到了回报。', 'reaping', '例', 136)],
      '麦子成熟（ripe）了之后才能收割（reap）。')
    material('reap a / the harvest', 136, '拓展', definition='享受成果')
    a('irrigate', '/ˈɪrɪɡeɪt/', 'v. 灌溉', 136,
      [('v.', '灌溉')],
      [(0, 'The waters in these three rivers irrigate the plains of Punjab.', '这三条河流的水灌溉着旁遮普的平原。', 'irrigate', '例', 136),
       (0, 'He wants to use the water to irrigate barren desert land.', '他想用这淡水来灌溉贫瘠的沙漠土地。', 'irrigate', '例', 136)],
      '他反复灌溉（irrigate）已经湿润的土地，这让大家很生气（irritate）。')
    a('irritable', '/ˈɪrɪtəbl/', 'adj. 暴躁的，易怒的', 136,
      [('adj.', '暴躁的，易怒的')],
      [(0, 'She waved him away with an irritable gesture.', '她气恼地挥手赶走了他。', 'irritable', '例', 136)],
      'i（我）+ rri（阿姨，谐音）+ table（桌子）→我阿姨一生气就掀桌子，她的脾气是“暴躁的”→暴躁的。')
    a('yield', '/jiːld/', 'n. 产量，产出；利润；v. 出产；产生；屈服', 136,
      [('n.', '利润'), ('v.', '出产；产生'), ('n.', '产量，产出'), ('v.', '屈服')],
      [(0, 'This will give a yield of 10% on your investment.', '这会给你的投资带来10%的利润。', 'yield', '例', 136),
       (1, 'Google farms us for the data that our digital lives yield.', '谷歌“养殖”我们是为了获取我们数字生活中产生的数据。', 'yield', '真题', 136)],
      '他的土地（field）产量（yield）不错。')
    include(137)
    a('output', '/ˈaʊtpʊt/', 'n. （人、机器、机构的）产量，输出量；v. 输出', 137,
      [('n.', '（人、机器、机构的）产量，输出量'), ('v.', '输出')],
      [(0, 'It certainly does not improve the gross national product or output per worker.', '它当然不能提高国民生产总值或工人的人均产出。', 'output', '例', 137),
       (0, 'Boiling down an individual’s output to simple metrics entails considerable savings in time, energy and ambiguity.', '将个人的产出归结为简单的度量指标，可以节省大量的时间、精力并避免诸多分歧。', 'output', '真题', 137)],
      'out（往外）+ put（放）→往外放的东西→产量，输出量。')
    group = '35 观点相关词汇'
    a('outlook', '/ˈaʊtlʊk/', 'n. 景色，风光；前景；观点；世界观，人生观', 137,
      [('n.', '观点；世界观，人生观'), ('n.', '景色，风光'), ('n.', '前景')],
      [(0, 'Losing his job changed his whole outlook on life.', '失业改变了他的整个人生观。', 'outlook', '例', 137),
       (0, 'Computer-education advocates forsake this optimistic notion for a pessimism that betrays their otherwise cheery outlook.', '计算机教育的倡导者放弃了这种乐观的观念，取而代之的是一种与他们的快乐人生观背道而驰的悲观主义。', 'outlook', '真题', 137)],
      'out（往外）+ look（看）→往外看到的→景色，风景。')
    a('insight', '/ˈɪnsaɪt/', 'n. 洞察力，理解力；洞悉，了解', 137,
      [('n.', '洞察力，理解力'), ('n.', '洞悉，了解')],
      [(1, 'His work offers several useful insights.', '他的工作提供了一些有用的见解。', 'insights', '例', 137),
       (0, 'Many first-generation students lack insight about why they are struggling and do not understand how students “like them” can improve.', '许多第一代大学生看不透为什么他们在苦苦挣扎，也不明白“像他们”这样的学生如何才能提升。', 'insight', '真题', 137)],
      'in（往里）+ sight（看）→往里看→洞悉，了解。',
      [('insightful', 'adj. 有深刻了解的；富有洞察力的', 137)])
    t.pending('insight', 0, '本句复数insights为见解，原书主释义未明确列此可数用法；暂不直接挂到洞悉、了解。')
    group = '36 over-相关词汇'
    a('overlook', '/ˌəʊvəˈlʊk/', 'v. 俯瞰，俯视；忽略，忽视', 137,
      [('v.', '俯瞰，俯视'), ('v.', '忽略，忽视')],
      [(0, 'Our back yard is overlooked by several houses.', '从好几栋房子上都能俯瞰到我家后院。', 'overlooked', '例', 137),
       (1, 'Today, widespread social pressure to immediately go to college in conjunction with increasingly high expectations in a fast-moving world often causes students to completely overlook the possibility of taking a gap year.', '如今，（高中毕业后）立刻进入大学这一普遍的社会压力以及快速发展的社会（对人们）越来越高的期待，经常会导致学生完全忽略选择间隔年的可能性。', 'overlook', '真题', 137)],
      'over（上面）+ look（看）→从上边往下看→俯视，俯瞰。')
    a('overwhelm', '/ˌəʊvəˈwelm/', 'v. 淹没；压倒，压垮；难以承受', 137,
      [('v.', '淹没'), ('v.', '压倒，压垮'), ('v.', '难以承受')],
      [(2, 'She was overwhelmed by feelings of guilt.', '她感到愧疚难当。', 'overwhelmed', '例', 138),
       (1, 'The army was overwhelmed by the rebels.', '军队被叛乱者完全击败了。', 'overwhelmed', '例', 138)],
      'over（上面）+ whelm（联想成wheel“轮子”）→想象有一个大轮子压在人身上，不把人“压倒”才怪呢！→压倒。',
      [('overwhelming', 'adj. 压倒性的，势不可挡的；巨大的', 138)])
    material('overwhelming', 138, '真题', english='Overwhelming majorities of both groups said they believe it is harder for young people today to get started in life than it was for earlier generations.', translation='这两个人群体中的绝大多数人认为，今天的年轻人比前几代人更难开始新的生活。')
    a('overtime', '/ˈəʊvətaɪm/', 'n. 加班；加班费；（体育比赛等的）加时', 138,
      [('n.', '加班费'), ('n.', '加班'), ('n.', '（体育比赛等的）加时')],
      [(0, 'They pay $150 a day plus overtime.', '他们支付每天150美元的报酬，外加加班费。', 'overtime', '例', 138),
       (1, 'Overtime is not attractive to this generation.', '加班对这一代人没有吸引力。', 'Overtime', '真题', 138)])
    a('overcome', '/ˌəʊvəˈkʌm/', 'v. 克服，解决；战胜', 138,
      [('v.', '克服，解决'), ('v.', '战胜')],
      [(0, 'He finally managed to overcome his fear of flying.', '他终于克服了对飞行的恐惧。', 'overcome', '例', 138),
       (1, 'In the final game Sweden easily overcame France.', '在决赛中，瑞典队轻松战胜了法国队。', 'overcame', '例', 138)],
      'over（上面）+ come（来）→你从困难的上边飞过来了，也就是“克服”了困难→克服。')
    a('overflow', 'v. /ˌəʊvəˈfləʊ/; n. /ˈəʊvəfləʊ/', 'v. 漫出，溢出；挤满；装满；n. 容纳不下的人或物', 138,
      [('v.', '挤满；装满'), ('v.', '漫出，溢出'), ('n.', '容纳不下的人或物')],
      [(0, 'His bag was overflowing with clothes.', '他的包里塞满了衣服。', 'overflowing', '例', 138),
       (0, 'The streets were overflowing with the crowds.', '街上到处挤满了人。', 'overflowing', '例', 138)],
      'over（上面）+ flow（流）→杯子里的水从上面流出来了→溢出。')
    a('overthrow', 'v. /ˌəʊvəˈθrəʊ/; n. /ˈəʊvəθrəʊ/', 'v. 打倒；推翻；n. 推翻；打倒', 138,
      [('v.', '打倒；推翻'), ('n.', '推翻；打倒')],
      [(0, 'They succeeded in overthrowing the fascist dictatorship.', '他们成功推翻了法西斯专政。', 'overthrowing', '例', 138),
       (1, 'Six men were questioned on suspicion of plotting the overthrow of the government.', '六名男子因涉嫌策划推翻政府而受到审问。', 'overthrow', '例', 138)],
      'over（上面）+ throw（扔）→把一个人从上面扔过去→打倒，推翻。')
    a('overall', '/ˌəʊvərˈɔːl/', 'adj. 综合的，总体的，全面的；adv. 总体上，大致上', 138,
      [('adj.', '综合的，总体的，全面的'), ('adv.', '总体上，大致上')],
      [(0, 'The overall quality of the articles is good.', '文章整体质量不错。', 'overall', '例', 138),
       (1, 'Overall, the idea is to let “states remain in the driver’s seat for managing the species”, Ashe said.', '总的来说，这一想法是让“各州在管理该物种方面仍保持主导地位”，阿什说。', 'Overall', '真题', 138)])
    a('overnight', 'adv. /ˌəʊvəˈnaɪt/; adj. /ˈəʊvənaɪt/', 'adv. 一夜之间；突然；在夜间，在晚上；adj. 夜间的，晚上的', 138,
      [('adv.', '在夜间，在晚上'), ('adv.', '一夜之间；突然'), ('adj.', '夜间的，晚上的')],
      [(0, 'We stayed overnight in London after the theatre.', '我们看完戏后在伦敦住了一晚。', 'overnight', '例', 138),
       (1, 'This isn’t something you can do overnight.', '这不是你一夜之间就能做到的。', 'overnight', '真题', 139)])
    group = '37 sw-相关词汇'
    a('swing', '/swɪŋ/', 'v. 摇摆，摆动；转动；n. 秋千；摆动', 139,
      [('v.', '摇摆，摆动'), ('v.', '转动'), ('n.', '秋千'), ('n.', '摆动')],
      [(0, 'We swing on the swings together.', '我们一起荡秋千。', 'swing', '例', 139),
       (0, 'His arms swung as he walked.', '他边走边摆着双臂。', 'swung', '例', 139)],
      '我们坐在秋千（swing）上摇摆（swing），就像长了翅膀（wing）一样。')
    a('sway', '/sweɪ/', 'v. 摇摆，摇动；说服，使动摇', 139,
      [('v.', '摇摆，摇动'), ('v.', '说服，使动摇')],
      [(0, 'The branches were swaying in the wind.', '树枝在风中摇曳。', 'swaying', '例', 139),
       (1, 'Don’t allow yourself to be swayed by emotion.', '别让自己为感情所左右。', 'swayed', '例', 139)],
      's（蛇）+ way（路）→蛇在路上爬行的时候，不就是左右“摇摆”吗？→摇摆。')
    a('spread', '/spred/', 'v. 展开，打开；散布，传播；n. 传播，散布；广泛；活动范围', 139,
      [('v.', '展开，打开'), ('v.', '散布，传播'), ('n.', '传播，散布'), ('n.', '广泛'), ('n.', '活动范围')],
      [(0, 'The bird spread its wings.', '鸟展开翅膀。', 'spread', '例', 139),
       (1, 'The idea is intuitively compelling, but it doesn’t explain how ideas actually spread.', '从直觉上讲，这种观点令人信服，但它并没有解释观念实际上是如何传播的。', 'spread', '真题', 139)],
      '他把从书上读（read）到的知识传播（spread）给了山区的学生。')
    a('widespread', '/ˈwaɪdspred/', 'adj. 广泛的，分布广的，普遍的', 139,
      [('adj.', '广泛的，分布广的，普遍的')],
      [(0, 'There is widespread concern that new houses will be built on protected land.', '人们普遍对在保护区修建新的房屋感到忧虑。', 'widespread', '例', 139),
       (0, 'It’s just that individual actions are too slow, she says, for that to be the only, or even primary, approach to changing widespread behavior.', '她说，只是个人行动太慢，不足以成为改变普遍行为的唯一的乃至主要的途径。', 'widespread', '真题', 139)])
    a('swell', '/swel/', 'n. 海浪的涌动；隆起处；增加；v. 肿胀，隆起；增加；使凸出，鼓出', 139,
      [('v.', '增加'), ('n.', '海浪的涌动'), ('n.', '隆起处'), ('n.', '增加'), ('v.', '肿胀，隆起'), ('v.', '使凸出，鼓出')],
      [(0, 'The river was swollen with melted snow.', '积雪融化，河水上涨。', 'swollen', '例', 139),
       (1, 'The boat was caught in a heavy swell.', '船遇上了大涌浪。', 'swell', '例', 139)],
      '他掉到井（well）里了，很久没有人救他，腿在水里都泡肿（swell）了。')
    a('sweep', '/swiːp/', 'v. 打扫，清扫；掠过；席卷，迅速传播；n. 扫，打扫，清扫', 139,
      [('v.', '打扫，清扫'), ('v.', '席卷，迅速传播'), ('v.', '掠过'), ('n.', '扫，打扫，清扫')],
      [(0, 'The classroom was swept clean and I felt exhausted.', '教室打扫干净了，我也累坏了。', 'swept', '例', 139),
       (1, 'Rumours of his resignation swept through the company.', '他辞职的传言在全公司传播开了。', 'swept', '例', 139)],
      '她不想打扫（sweep）卫生，坐在角落里哭（weep）了。')
    include(140)
    material('windswept', 139, '拓展', definition='adj. 受大风吹的；当风的')
    material('windswept', 139, '真题', pdf_pages=[139,140],
      english='On a recent sunny day, 13,000 chickens roam over Larry Brown’s 40 windswept acres in Shiner, Texas.',
      translation='不久前的一天，艳阳高照，13000只鸡在拉里·布朗位于得克萨斯州希纳市的40英亩向风的露天农场里自由活动着。')
