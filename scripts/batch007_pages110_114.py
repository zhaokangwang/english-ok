"""PDF110 unit divider and PDF111 onward: visually checked fourth-unit material."""

COMPLETE_THROUGH = 114
NEXT_WORD = 'spot'
NEXT_PAGE = 115


def append(t, associated):
    group = '01 -cline相关词汇'

    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(1000 + len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-004'

    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))

    def include_page(page):
        word = t.words[-1]
        word['pdf_pages'] = sorted(set(word['pdf_pages'] + [page]))
        word['printed_pages'] = [f'{p-8:03}' for p in word['pdf_pages']]

    a('incline', '/ˈɪnklaɪn/ n.; /ɪnˈklaɪn/ v.', 'n. 斜坡，斜面；v. （使）倾斜，（使）倾向于', 111,
      [('v.', '（使）倾斜'), ('v.', '（使）倾向于'), ('n.', '斜坡，斜面')],
      [(0, 'The land inclined gently towards the shore.', '地面缓缓向海岸倾斜。', 'inclined', '例', 111),
       (1, 'It is that one is actually inclined to interruption.', '实际上，一个人也真的愿意被打断。', 'inclined', '真题', 111)],
      'in（使，加以）+ clin（倾斜）+ e →（使）倾斜，（使）倾向于。')
    t.pending('incline', 1, '原书句子It is that one is actually inclined to interruption.缺少前文；inclined为状态用法，暂不直接映射动词倾向于义。保留原句原译。')
    a('decline', '/dɪˈklaɪn/', 'n. 下降；衰落，衰退；v. 谢绝；下降，衰退', 111,
      [('v.', '下降，衰退'), ('v.', '谢绝'), ('n.', '下降；衰落，衰退')],
      [(0, 'Jobs in manufacturing have steadily declined.', '制造业的就业岗位稳步下降。', 'declined', '例', 111),
       (1, 'Microsoft declined to comment.', '微软拒绝作出评论。', 'declined', '真题', 111)],
      'de（向下）+ clin（倾斜）+ e →向下倾斜，就是“下降”→下降。')

    group = '02 抢夺相关词汇'
    a('snatch', '/snætʃ/', 'v. 抢走，夺去；抓紧时间做；一下夺过', 111,
      [('v.', '抢走，夺去；一下夺过'), ('v.', '抓紧时间做')],
      [(0, 'Someone tried to snatch her purse.', '有人要抢她的钱包。', 'snatch', '例', 111),
       (1, 'I managed to snatch an hour’s sleep.', '我偷空儿睡了一小时的觉。', 'snatch', '例', 111)])
    a('grab', '/ɡræb/', 'n. 猛然的抓取；突然的抢夺；v. 抓住；攫取', 111,
      [('v.', '抓住；攫取'), ('n.', '猛然的抓取；突然的抢夺')],
      [(0, 'She grabbed the chance of a job interview.', '她抓住了一次求职面试的机会。', 'grabbed', '例', 111),
       (1, 'The thief made a grab at my bag but I pushed him away.', '这个贼想抢我的手提包，但被我推开了。', 'grab', '例', 111)])

    group = '03 延伸相关词汇'
    a('stretch', '/stretʃ/', 'v. 伸展，舒展；拉紧；伸长；延续；n. 一片；连续的一段时间；伸展', 111,
      [('v.', '伸展，舒展'), ('v.', '拉紧；伸长'), ('v.', '延续'), ('n.', '一片'), ('n.', '连续的一段时间'), ('n.', '伸展')],
      [(0, 'The exercises are designed to stretch and tone your leg muscles.', '这些活动目的在于伸展和增强你的腿部肌肉。', 'stretch', '例', 111),
       (1, 'Stop stretching your sleeves like that!', '别一个劲地抻袖子了！', 'stretching', '例', 111)],
      '发音类似“死拽扯”→他“伸出”手臂拼命地拽我扯我→伸展；拉长。')
    a('extend', '/ɪkˈstend/', 'v. 延长；使伸长；扩大，扩展', 111,
      [('v.', '延长；使伸长'), ('v.', '扩大，扩展')],
      [(1, 'There are plans to extend the children’s play area.', '有扩大儿童游戏区的计划。', 'extend', '例', 111),
       (1, 'To find out if this extends to non-living beings, Laleh Quinn tested whether rats can detect social signals from robotic rats.', '为了弄清楚这是否也适用于非生物，拉蕾·奎因测试了老鼠是否能感知到机器老鼠发出的社交信号。', 'extends', '真题', 111)],
      'ex（出，外）+ tend（伸展）→向外伸展→延长，使伸展。',
      [('extensive', 'adj. 广阔的，广泛的；大量的', 111), ('extension', 'n. 伸展，延伸；扩建部分', 111)])
    t.pending('extend', 1, 'extends to在本句为适用于的语义；原书主词仅列延长、扩大等义，暂待独立词义映射，保留原句原译。')
    material('extensive', 111, '例', english='The house has extensive grounds.', translation='这栋房子有宽敞的庭院。')
    material('extension', 112, '例', english='My home life was becoming no more than an extension of my job.', translation='我的家庭生活只不过是我工作的延伸。')
    include_page(112)
    a('tend', '/tend/', 'v. 往往会，常常就；趋向，走向，倾向，趋于；照料；护理', 112,
      [('v.', '往往会，常常就'), ('v.', '趋向，走向，倾向，趋于'), ('v.', '照料；护理')],
      [(0, 'People tend to be happier if they are in a long-term relationship.', '如果处于长期关系中，人们往往会更快乐。', 'tend', '例', 112),
       (0, 'Although American men tend to talk more than women in public situations, they often talk less at home.', '尽管在公众场合美国男性通常比女性健谈，但在家他们一般话比较少。', 'tend', '真题', 112)])
    a('tendency', '/ˈtendənsi/', 'n. 倾向，偏好；趋势', 112,
      [('n.', '倾向，偏好'), ('n.', '趋势')],
      [(0, 'There’s a growing tendency for women to marry later.', '女性越来越倾向于晚婚。', 'tendency', '例', 112),
       (1, 'Attempts have been made to curb this tendency.', '为了遏制这种趋势，已经进行了一些尝试。', 'tendency', '真题', 112)],
      'tend（趋向）+ ency（状态，行为）→趋向，趋势。')
    a('trend', '/trend/', 'n. 趋势，趋向，倾向；动态，动向；v. 朝着大方向变化或发展', 112,
      [('n.', '趋势，趋向，倾向；动态，动向'), ('v.', '朝着大方向变化或发展')],
      [(0, 'There is a growing trend towards later retirement.', '以后的退休有越来越晚的趋向。', 'trend', '例', 112),
       (0, 'The functioning of the market is based on flexible trends dominated by potential buyers.', '市场的运转基于潜在买者所支配的灵活趋势。', 'trends', '真题', 112)])
    t.pending('trend', 1, '原书flexible trends与市场运转语境搭配可疑；保留原句和原译待复核，不自动改词。')
    a('attend', '/əˈtend/', 'v. 出席，参加；注意，专心；经常去，定期去（某处）', 112,
      [('v.', '出席，参加'), ('v.', '注意，专心'), ('v.', '经常去，定期去（某处）')],
      [(0, 'We’d like as many people as possible to attend.', '我们希望出席的人越多越好。', 'attend', '例', 112),
       (0, 'Students are expected to attend class regularly.', '学生应该定期上课。', 'attend', '例', 112)],
      'at（一再地）+ tend（延伸）→想象你在课堂上一再地延伸你的手臂，就是举手，你在干什么？在积极“参加”啊→参加。',
      [('attendance', 'n. 出席，参加', 112)])
    material('attendance', 112, '真题', english='The theatre has broken attendance records for three years in a row.', translation='这家剧院已连续三年打破了上座率的纪录。')
    a('contend', '/kənˈtend/', 'v. 主张，认为；竞争', 112,
      [('v.', '主张，认为'), ('v.', '竞争')],
      [(0, 'He contends that the Supreme Court’s ruling could have “profound effects” on other biotech industries.', '他认为，最高法院的裁决可能对其他生物技术行业产生“深远影响”。', 'contends', '例', 112),
       (0, 'It is the playgoers, the RSC contends, who bring in much of the town’s revenue.', '皇家莎士比亚剧团认为，是看戏的人给小镇带来了大部分的收入。', 'contends', '真题', 112)])
    a('intend', '/ɪnˈtend/', 'v. 打算，计划，想要；意指', 112,
      [('v.', '打算，计划，想要'), ('v.', '意指')],
      [(0, 'I never intended to hurt you.', '我从来都没想伤害你。', 'intended', '例', 112),
       (0, 'We accumulate the 50 percent of stuff in our cart that we never intended buying.', '我们把本来根本没打算买的那一半东西推进了购物车。', 'intended', '真题', 113)],
      '发音类似“因疼得”→我因为肚子疼得受不了，“打算”去医院检查一下→打算。')
    a('intention', '/ɪnˈtenʃn/', 'n. 打算，计划；意图，目的', 113,
      [('n.', '打算，计划'), ('n.', '意图，目的')],
      [(0, 'He left England with the intention of travelling in Africa.', '他离开英格兰，打算去非洲旅行。', 'intention', '例', 113),
       (1, 'But the intention is not to neglect social science; rather, the complete opposite.', '但其目的并不是要忽视社会科学；而是完全相反。', 'intention', '真题', 113)],
      related=[('intentional', 'adj. 有意的，故意的，存心的', 113)])
    material('intentional', 113, '例', english='It is difficult to prove whether their actions were negligent or intentional.', translation='很难证明他们的行为是疏忽还是故意的。')

    group = '04 假装、掩盖相关词汇'
    a('pretend', '/prɪˈtend/', 'v. 假装，佯装；模拟；自认为', 113,
      [('v.', '假装，佯装'), ('v.', '模拟'), ('v.', '自认为')],
      [(0, 'I pretended to be asleep.', '我假装睡着了。', 'pretended', '例', 113),
       (0, 'I’m tired of having to pretend all the time.', '我讨厌一直得假装。', 'pretend', '例', 113)],
      'pre（提前）+ tend（谐音“疼的”）→提前喊疼，这一定是“假装”→假装。')
    a('disguise', '/dɪsˈɡaɪz/', 'v. 假装，伪装；掩蔽，掩饰', 113,
      [('v.', '假装，伪装'), ('v.', '掩蔽，掩饰')],
      [(1, 'She made no attempt to disguise her surprise.', '她根本不曾试图掩饰自己的惊奇。', 'disguise', '例', 113),
       (0, 'Dreams were the disguised shadows of our unconscious desires and fears.', '梦是人们无意识的欲望和恐惧伪装的影子。', 'disguised', '真题', 113)])
    t.pending('disguise', 1, 'disguised在本句中修饰shadows，为分词定语；原书仅列动词义，暂不作为动词学习卡。保留原句原译。')
    a('mask', '/mɑːsk/', 'n. 面具，假面具；伪装；v. 掩饰', 113,
      [('n.', '面具，假面具'), ('n.', '伪装'), ('v.', '掩饰')],
      [(0, 'The kids were all wearing animal masks.', '孩子们都戴着动物面具。', 'masks', '例', 113),
       (2, 'Mies’s sophisticated presentation masked the fact that the spaces he designed were small and efficient, rather than big and often empty.', '密斯复杂的展示方式掩盖了这样一个事实：他设计的空间是小而高效的，而不是大而空旷的。', 'masked', '真题', 113)])
    a('screen', '/skriːn/', 'n. 屏幕，荧光屏；屏风；画面；纱窗；v. 放映；检查，审查', 113,
      [('n.', '屏幕，荧光屏'), ('n.', '屏风'), ('n.', '画面'), ('n.', '纱窗'), ('v.', '放映'), ('v.', '检查，审查')],
      [(5, 'Government employees may be screened by the security services.', '政府雇员可能要接受安全部门的审查。', 'screened', '例', 113),
       (0, 'With so much focus on children’s use of screens, it’s easy for parents to forget about their own screen use.', '随着儿童对屏幕（数字产品）的使用备受关注，父母很容易忽视他们自己对屏幕（数字产品）的使用。', 'screens', '真题', 113)])
    a('veil', '/veɪl/', 'n. 面纱，面罩；v. 遮掩，掩饰', 113,
      [('n.', '面纱，面罩'), ('v.', '遮掩，掩饰')],
      [(0, 'The bridal veil was fringed with lace.', '新娘戴的面纱上镶着花边。', 'veil', '例', 113),
       (1, 'A fine drizzle began to veil the hills.', '蒙蒙的细雨渐渐笼罩了群山。', 'veil', '例', 113)],
      related=[('unveil', 'v. 揭开，展示', 113)])
    material('unveil', 114, '例', english='They will be unveiling their new models at the Motor Show.', translation='他们将在汽车展上首次推出自己的新型汽车。')
    include_page(114)
    a('conceal', '/kənˈsiːl/', 'v. 隐藏，隐瞒；掩盖', 114,
      [('v.', '隐藏，隐瞒'), ('v.', '掩盖')],
      [(0, 'She sat down to conceal the fact that she was trembling.', '她坐下来以隐瞒她在发抖的事实。', 'conceal', '例', 114),
       (1, 'Nature gave us lips to conceal our teeth.', '大自然给了我们嘴唇来掩盖我们的牙齿。', 'conceal', '真题', 114)])

    group = '05 揭示、察觉相关词汇'
    a('reveal', '/rɪˈviːl/', 'v. 揭示；显示；透露', 114,
      [('v.', '揭示；显示；透露')],
      [(0, 'Her expression revealed nothing.', '从她的表情什么也看不出来。', 'revealed', '例', 114),
       (0, 'Even without knowing what was in the messages, the knowledge of who sent them and to whom was enormously revealing and still could be.', '即使不知道信息中的具体内容，但其发送者以及接收者的信息在极大程度上也会透露内情，且这种情况仍会继续。', 'revealing', '真题', 114)],
      related=[('revelation', 'n. 被暴露的真相；被曝光的秘闻；披露，揭露', 114)])
    t.pending('reveal', 1, 'revealing在原句中作表语，为提供信息的形容词用法；原书仅列reveal动词，暂不直接计入动词学习进度。保留原文原译。')
    a('uncover', '/ʌnˈkʌvə(r)/', 'v. 揭开盖子；揭露，发现', 114,
      [('v.', '揭开盖子'), ('v.', '揭露，发现')],
      [(0, 'Uncover the pan and let the soup simmer.', '揭开锅盖，让汤再慢慢熬一下。', 'Uncover', '例', 114),
       (1, 'It will be difficult to uncover the truth.', '揭开真相会很困难。', 'uncover', '例', 114)],
      'cover“覆盖”，uncover是其反义词（un表示“否定”），就是“揭开，揭露”。')
    a('disclose', '/dɪsˈkləʊz/', 'v. 透露；泄露；揭露', 114,
      [('v.', '透露；泄露；揭露')],
      [(0, 'The spokesman refused to disclose details of the takeover to the press.', '发言人拒绝向新闻界透露公司收购的详细情况。', 'disclose', '例', 114),
       (0, 'I cannot disclose what we discussed.', '我不能泄露我们讨论的内容。', 'disclose', '例', 114)],
      'dis（不）+ close（关）→不关了，就是敞开了→透露；泄露。')
    a('enclose', '/ɪnˈkləʊz/', 'v. 把……围起来；围住；附入；随函（或包裹等）附上', 114,
      [('v.', '把……围起来；围住'), ('v.', '附入；随函（或包裹等）附上')],
      [(0, 'The yard had been enclosed with iron railings.', '院子用铁栅栏围了起来。', 'enclosed', '例', 114),
       (0, 'The garden was enclosed by a tall, black wooden fence.', '花园被一堵高高的黑色木栅栏围了起来。', 'enclosed', '例', 114)],
      related=[('enclosure', 'n. 围场；圈占地；附件', 114)])
    material('enclosure', 114, '真题', english='No matter how you enhance enclosures, they do not allow for freedom, a natural diet or adequate exercise.', translation='无论你如何改善圈养环境，都不能给它们自由的空间、自然的饮食或充分的运动。')
    a('detect', '/dɪˈtekt/', 'v. 发现，查明；察觉；侦察出', 114,
      [('v.', '发现，查明；察觉；侦察出')],
      [(0, 'The sensor detects changes of light level and temperature.', '传感器检测光线水平和温度的变化。', 'detects', '例', 115),
       (0, 'People have failed to detect the massive changes which have happened in the ocean.', '人们未能察觉到海洋中发生的巨大变化。', 'detect', '真题', 115)],
      'de（往下）+ tect（联想成“探”）→这群钻探工人向下钻孔，取出岩心等样品是为了探测地层构造→查明，发现。',
      [('detector', 'n. 检测器，探测器', 115), ('detective', 'n. 侦探；警探；私人侦探', 115)])
    material('detective', 115, '例', english='A team of around 30 detectives and uniformed officers have been working on the case.', translation='一个由大约30名侦探和穿制服的警察组成的小组一直在调查此案。')
