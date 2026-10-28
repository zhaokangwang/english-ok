"""PDF 86–89: manual visual transcription of the rendered source pages."""


def append(t, associated):
    group = '17 继承相关词汇'

    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(346 + len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)

    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))

    def include_page(page):
        w = t.words[-1]
        w['pdf_pages'] = sorted(set(w['pdf_pages'] + [page]))
        w['printed_pages'] = [f'{p-8:03}' for p in w['pdf_pages']]

    a('inherit', '/ɪnˈherɪt/', 'v. 继承，经遗传获得；接替；继任', 86,
      [('v.', '继承，经遗传获得'), ('v.', '接替；继任')],
      [(0, 'She inherited a fortune from her father.', '她从她父亲那里继承了一大笔财富。', 'inherited', '例', 86)],
      '他想让他儿子继承（inherit）他的遗产（heritage）。',
      [('inherent', 'adj. 内在的；固有的', 86)])
    material('inherent', 86, '例', english='Individuality is a valued and inherent part of the British character.', translation='个性是英国人重视并固有的特征。')

    group = '18 cat相关词汇'
    a('scatter', '/ˈskætə(r)/', 'v. 撒，撒播；散布；n. 散落', 86,
      [('v.', '撒，撒播；散布'), ('n.', '散落')],
      [(0, 'At the first gunshot, the crowd scattered.', '枪声一响，人群便逃散了。', 'scattered', '例', 86),
       (0, 'The goals of the prize-givers seem as scattered as the criticism.', '奖项提供者的目标似乎和（他们所受的）批评一样分散。', 'scattered', '真题', 86)])
    t.pending('scatter', 1, '真题中scattered为形容词用法，原书主词仅列动词和名词义；保留原文及原译，待词性义项核对，不用于练习。')
    a('catalogue', '/ˈkætəlɒɡ/', 'n. 目录；v. 将……编入目录', 86,
      [('n.', '目录'), ('v.', '将……编入目录')],
      [(0, 'An illustrated catalogue accompanies the exhibition.', '展览会有插图目录。', 'catalogue', '例', 86),
       (1, 'New books are catalogued on an electronic database.', '新书被编入电子数据库。', 'catalogued', '例', 86)],
      'cata（发音类似“开头”）+ logue（说话）→把作者说的话提取重点放在开头，可以形成“目录”。')
    material('catalog', 86, '美式拼写', main_word='catalogue')

    group = '19 appetite相关形近词'
    a('appetite', '/ˈæpɪtaɪt/', 'n. 胃口；强烈欲望', 86,
      [('n.', '胃口'), ('n.', '强烈欲望')],
      [(0, 'The walk gave me a good appetite.', '散步使我胃口大开。', 'appetite', '例', 86),
       (1, 'Technology has such an insatiable appetite for eating up human jobs.', '技术在吞噬人类工作方面非常“贪得无厌”。', 'appetite', '真题', 86)],
      'ap（一再）+ pet（寻找、追求）+ ite（名词后缀）→一再追求、寻求→强烈欲望。')
    a('petition', '/pəˈtɪʃn/', 'n. 请愿书；申诉书；v. 祈求；请求，请愿，申请', 86,
      [('n.', '请愿书；申诉书'), ('v.', '祈求；请求，请愿，申请')],
      [(0, 'Would you like to sign our petition against experiments on animals?', '您愿意在我们反对用动物做实验的请愿书上签名吗？', 'petition', '例', 86),
       (0, 'In response to another petition last year about banning fake lawns, which gathered 30,000 signatures, the government responded that it has “no plans to ban the use of artificial grass”.', '去年，另一份关于禁止人造草坪的请愿书收集了3万个签名，对这份请愿书，政府回应说，它“没有禁止使用人造草坪的计划”。', 'petition', '真题', 86)])
    a('impetus', '/ˈɪmpɪtəs/', 'n. 动力，推动，促进', 86,
      [('n.', '动力，推动，促进')],
      [(0, 'The debate seems to have lost much of its initial impetus.', '辩论会似乎没有开始时那么大的冲劲了。', 'impetus', '例', 87),
       (0, 'His articles provided the main impetus for change.', '他的那些文章是促进变革的主要推动力。', 'impetus', '例', 87)],
      'im（联想成in“里面”）+ pet（宠物）+ us（我们）→我们在家里养宠物，能够“促进”我们的孩子养成爱护动物的习惯。')
    a('impulse', '/ˈɪmpʌls/', 'n. 冲动；推动力；动力；刺激', 87,
      [('n.', '冲动'), ('n.', '推动力；动力；刺激')],
      [(0, 'I resisted the impulse to laugh.', '我强忍着没有笑出来。', 'impulse', '例', 87),
       (0, 'Some kids who are low in sympathy may make up for that shortfall by experiencing more guilt, which can rein in their nastier impulses.', '一些缺乏同情心的孩子可能会通过体验更多的内疚感来弥补这一不足，这可以遏制他们更恶劣的冲动。', 'impulses', '真题', 87)])

    group = '20 ally相关词汇'
    a('ally', '/ˈælaɪ/', 'n. 同盟国；盟友；v. 与……结盟', 87,
      [('n.', '同盟国；盟友'), ('v.', '与……结盟')],
      [(0, 'Portugal is a traditional ally of England.', '葡萄牙是英国的传统盟友。', 'ally', '例', 87)],
      'all（所有的）+ y（联想成yes“是”）→所有人都同意→结盟→盟友，同盟国。',
      [('alliance', 'n. 联盟，结盟团体', 87)])
    material('alliance', 87, '例', english='The Green Alliance was formed to campaign against environmental damage.', translation='绿色联盟的成立是为了开展反对破坏环境的运动。')
    a('rely', '/rɪˈlaɪ/', 'v. 依赖，依靠，信任', 87,
      [('v.', '依赖，依靠，信任')],
      [(0, 'They had to rely entirely on volunteer workers.', '他们不得不完全依靠志愿者。', 'rely', '例', 87),
       (0, 'It is preferable for journalists to rely on their own notions of significance and make their own judgments.', '记者最好还是依靠自己对事件重要性的认识，作出自己的判断。', 'rely', '真题', 87)],
      related=[('reliable', 'adj. 可靠的，可信赖的', 87)])
    a('reliance', '/rɪˈlaɪəns/', 'n. 依靠，依赖', 87,
      [('n.', '依靠，依赖')],
      [(0, 'There may be costs associated with our increased reliance on the Internet.', '我们越来越依赖互联网可能会带来一些成本。', 'reliance', '真题', 87)])
    a('liable', '/ˈlaɪəbl/', 'adj. （法律上）负有偿付责任；可能（做某事）；可能受……影响', 87,
      [('adj.', '（法律上）负有偿付责任'), ('adj.', '可能（做某事）；可能受……影响')],
      [(0, 'You will be liable for any damage caused.', '你必须对造成的任何损失负赔偿责任。', 'liable', '例', 87),
       (0, 'Juries began holding more companies liable for their customers’ misfortunes.', '陪审团开始要求更多公司对其客户的不幸负责。', 'liable', '真题', 87)],
      '我对给出可靠的（reliable）信息是有责任的（liable）。',
      [('liability', 'n. 责任，义务；惹麻烦的人（或事）；负债，债务', 87)])

    group = '21 荒谬相关词汇'
    a('absurd', '/əbˈsɜːd/', 'adj. 荒谬的，荒唐的，怪诞不经的', 87,
      [('adj.', '荒谬的，荒唐的，怪诞不经的')],
      [(0, 'That uniform makes the guards look absurd.', '警卫们穿着那种制服看起来怪模怪样的。', 'absurd', '例', 87),
       (0, 'It’s easy to dismiss as absurd the federal government’s ideas for plugging the chronic funding gap of our national parks.', '联邦政府填补国家公园长期资金缺口的想法很容易被认为是荒谬的。', 'absurd', '真题', 88)],
      'ab（一再地）+ surd（发音类似“笑”）→一再地笑→可笑的，荒谬的。')
    a('ridiculous', '/rɪˈdɪkjələs/', 'adj. 可笑的，荒谬的', 88,
      [('adj.', '可笑的，荒谬的')],
      [(0, 'I look ridiculous in this hat.', '我戴这顶帽子看上去很可笑。', 'ridiculous', '例', 88),
       (0, 'They ate and drank a ridiculous amount.', '他们胡吃海塞了很多东西。', 'ridiculous', '例', 88)])

    group = '22 适应相关词汇'
    a('accommodate', '/əˈkɒmədeɪt/', 'v. 为……提供住宿；容纳；适应', 88,
      [('v.', '为……提供住宿'), ('v.', '容纳'), ('v.', '适应')],
      [(0, 'The hotel can accommodate up to 500 guests.', '这家旅馆可供多达500位旅客住宿。', 'accommodate', '例', 88),
       (1, 'The garage can accommodate three cars.', '这个车库可以停放3辆小汽车。', 'accommodate', '例', 88)],
      '他千里迢迢来给你送货物（commodity），你总得给他提供住宿（accommodate）吧。',
      [('accommodation', 'n. 住处；膳宿；办公处；停留处', 88)])
    a('adopt', '/əˈdɒpt/', 'v. 收养；采纳，采用；采取', 88,
      [('v.', '采纳，采用；采取'), ('v.', '收养')],
      [(0, 'The council is expected to adopt the new policy at its next meeting.', '委员会有望在下次会议上正式通过这项新政策。', 'adopt', '例', 88),
       (1, 'Among the most popular: paternity and kinship testing, which adopted children can use to find their biological relatives.', '其中最受欢迎的是亲子关系和血缘关系鉴定，这种鉴定可以让被收养的孩子找到他们的生身父母。', 'adopted', '真题', 88)],
      'ad（一再地）+ opt（表示“选择”）→一再地给出多种选择，最后“采纳”。')
    a('adapt', '/əˈdæpt/', 'v. （使）适应；改编，改写', 88,
      [('v.', '改编，改写'), ('v.', '（使）适应')],
      [(0, 'Three of her novels have been adapted for television.', '她的长篇小说中有三部已改编成电视节目。', 'adapted', '例', 88),
       (1, 'You also quickly learn to adapt and come up with creative solutions to the problems the painting presents.', '你也能快速学会适应，并想出创造性的方法来解决绘画中出现的问题。', 'adapt', '真题', 88)],
      '虽然他刚刚被收养（adopt），但是他适应（adapt）新家庭的速度很快。')
    material('adapt to', 88, '拓展', definition='适应')

    group = '23 alarm相关词汇'
    a('alarm', '/əˈlɑːm/', 'n. 惊恐，惊慌；警报（器），闹钟；v. 使惊恐；使害怕', 88,
      [('n.', '警报（器），闹钟'), ('n.', '惊恐，惊慌'), ('v.', '使惊恐；使害怕')],
      [(0, 'By the time the alarm was raised the intruders had escaped.', '警报响起时，入侵者已经逃走了。', 'alarm', '例', 88),
       (2, 'Lansley has alarmed health campaigners.', '兰斯利已经对健康运动者发出信号。', 'alarmed', '真题', 88)],
      'a（一）+ l（联想成“拉”）+ arm（胳膊）→他用一只胳膊使劲拉警报器→警报（器）。',
      [('alarmist', 'adj. 危言耸听的，骇人的', 89)])
    include_page(89)
    t.pending('alarm', 1, '原书译文“对健康运动者发出信号”与alarmed（使惊恐）不符；保留原文，待核对，不用于练习。')
    material('alarmist', 89, '真题', english='This isn’t to be alarmist.', translation='这不是危言耸听。')
    a('panic', '/ˈpænɪk/', 'n. 惊慌，恐慌；人心惶惶的局面；惶恐不安；v. （使）恐慌', 89,
      [('v.', '（使）恐慌'), ('n.', '惊慌，恐慌；人心惶惶的局面；惶恐不安')],
      [(0, 'I panicked when I saw smoke coming out of the engine.', '我看见发动机冒烟时，吓得手足无措。', 'panicked', '例', 89),
       (1, 'There’s probably little reason to pay attention to our dreams at all unless they keep us from sleeping or we wake up in a panic.', '可能根本没有什么理由去关注我们的梦，除非它们让我们无法入睡，或者我们在恐慌中醒来。', 'panic', '真题', 89)],
      '几个小孩偷偷去山上野餐（picnic）了，他们的父母非常恐慌（panic）。')
    a('caution', '/ˈkɔːʃn/', 'n. 小心，谨慎；警告；v. 警告，劝……小心；提醒', 89,
      [('n.', '小心，谨慎'), ('n.', '警告'), ('v.', '警告，劝……小心；提醒')],
      [(0, 'Statistics should be treated with caution.', '对待统计数字要小心。', 'caution', '例', 89),
       (2, 'Sam cautioned him against making a hasty decision.', '萨姆告诫他不要草率作出决定。', 'cautioned', '例', 89)],
      '发音类似“靠身”→如果有人靠近你的身体，你要“谨慎”，处处“小心”一些！',
      [('cautious', 'adj. 谨慎的，小心的', 89)])
    material('cautious', 89, '真题', english='Employers are more cautious about hiring new staff.', translation='雇主对雇佣新员工更加谨慎。')
    a('precaution', '/prɪˈkɔːʃn/', 'n. 预防措施；防备', 89,
      [('n.', '预防措施；防备')],
      [(0, 'You must take all reasonable precautions to protect yourself and your family.', '你必须采取一切合理的预防措施，保护自己和家人。', 'precautions', '例', 89),
       (0, 'I’ll keep the letter as a precaution.', '我要保存这封信，以防万一。', 'precaution', '例', 89)],
      'pre（提前）+ caution（小心）→做事情前就小心→预防措施。')
    a('prudent', '/ˈpruːdnt/', 'adj. 谨慎的，慎重的；精明的', 89,
      [('adj.', '谨慎的，慎重的'), ('adj.', '精明的')],
      [(0, 'We thought it prudent to telephone first.', '为谨慎起见，我们认为应先打一个电话。', 'prudent', '例', 89),
       (0, 'A prudent people would take out an insurance policy now.', '一个谨慎的民族现在应该采取保护措施了。', 'prudent', '真题', 89)],
      '他既是一个骄傲的（proud）人，又是一个谨慎的（prudent）人。')
    a('alert', '/əˈlɜːt/', 'adj. 提防的，警惕的；v. 向……报警；n. 警报；警惕', 89,
      [('n.', '警报'), ('n.', '警惕'), ('adj.', '提防的，警惕的'), ('v.', '向……报警')],
      [(0, 'There is a bomb alert, not only on the rail link but also on the M1 motorway running parallel to it.', '不仅在铁路线上，而且在与之平行的M1高速公路上都有炸弹警报。', 'alert', '例', 89)],
      '发音类似“讹了他”→讹了他一次后，他就变得很警惕了→警惕的。')
