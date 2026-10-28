"""Visual transcription of headwords beginning on PDF100–104; append-only part."""

COMPLETE_THROUGH = 104
NEXT_WORD = 'decay'
NEXT_PAGE = 105


def append(t, associated):
    group = '38 模糊相关词汇'

    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(1000 + len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-003'

    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))

    def include_page(page):
        w = t.words[-1]
        w['pdf_pages'] = sorted(set(w['pdf_pages'] + [page]))
        w['printed_pages'] = [f'{p-8:03}' for p in w['pdf_pages']]

    a('dim', '/dɪm/', 'adj. 暗淡的；昏暗的；看不清楚的，模糊的；不明朗的', 100,
      [('adj.', '暗淡的；昏暗的；看不清楚的，模糊的；不明朗的')],
      [(0, 'Her future career prospects look dim.', '她的职业前景看来很暗淡。', 'dim', '例', 100),
       (0, 'According to accounts of the experiments, their hourly output rose when lighting was increased, but also when it was dimmed.', '根据实验记录，他们每小时的产量在光线增强和变暗时都会增加。', 'dimmed', '真题', 100)],
      '灯光有点昏暗（dim），我看不清地上是不是有个一角硬币（dime）。')
    t.pending('dim', 1, '真题中的dimmed是动词被动用法；原书主词仅列形容词义，暂不作为形容词学习例句。')
    group = '39 dimension相关词汇'
    a('dilemma', '/dɪˈlemə/', 'n. （进退两难的）窘境，困境', 100,
      [('n.', '（进退两难的）窘境，困境')],
      [(0, 'They were caught in a real dilemma.', '他们陷入了进退两难的境地。', 'dilemma', '例', 100),
       (0, 'I could see no way of resolving this moral dilemma.', '我想不出解决这一道德困境的办法。', 'dilemma', '例', 100)],
      'di（弟）+ lemma（发音类似“来吗”）→弟弟不确定是否要来，陷入了进退两难的“困境”。')
    a('dimension', '/daɪˈmenʃn/', 'n. 尺寸；范围；规模；方面', 100,
      [('n.', '尺寸；范围；规模'), ('n.', '方面')],
      [(0, 'We measured the dimensions of the kitchen.', '我们测量了厨房的尺寸。', 'dimensions', '例', 100),
       (1, 'Her job added a new dimension to her life.', '她的工作为她的生活增添了新的内容。', 'dimension', '例', 100)],
      'di（分开）+ mens（测量）+ ion（名词后缀）→分开测量以计算它的“规模”。')
    a('cement', '/sɪˈment/', 'n. 水泥；胶合剂，胶接剂；v. 胶合；巩固，加强', 100,
      [('n.', '水泥；胶合剂，胶接剂'), ('v.', '胶合；巩固，加强')],
      [(0, 'Use a mixture of one part cement to four parts sand.', '使用一份水泥和四份沙子的混合物。', 'cement', '例', 100),
       (1, 'They could cement the status quo of peer-reviewed research.', '它们会使同行评审研究的现状停滞不前。', 'cement', '真题', 100)],
      '发音类似“塞门它”。我家的门已经破烂不堪了，都在晃动，门柱下塞些“水泥”，给它固定下。')
    group = '40 痛苦相关词汇'
    a('distress', '/dɪˈstres/', 'n. 忧虑；悲伤，痛苦；贫困；v. 使痛苦，使悲伤', 100,
      [('n.', '忧虑；悲伤，痛苦'), ('n.', '贫困'), ('v.', '使痛苦，使悲伤')],
      [(0, 'The newspaper article caused the actor considerable distress.', '报上的文章给这位演员带来极大的痛苦。', 'distress', '例', 100),
       (2, 'The child becomes increasingly distressed as she tries to capture her mother’s attention.', '孩子在试图吸引妈妈的注意力时，变得越来越痛苦。', 'distressed', '真题', 100)],
      'di（分开）+ stress（压力）→他们要忍受常年分开的压力，这让他们很痛苦→痛苦；使痛苦。',
      [('distressing', 'adj. 令人苦恼的，使人痛苦的', 100)])
    t.pending('distress', 1, 'distressed在becomes increasingly distressed中为形容词状态用法；原书主词未独立列形容词义，暂不配动词使痛苦义。')
    a('stress', '/stres/', 'n. （精神）压力；强调，重要性；重音；v. 着重，强调', 101,
      [('n.', '（精神）压力'), ('n.', '强调，重要性；重音'), ('v.', '着重，强调')],
      [(0, 'The incident has caused enormous stress and anxiety to my family.', '这件事给我的家人带来了巨大的压力和焦虑。', 'stress', '例', 101),
       (0, 'People are actually more stressed at home than at work.', '人们在家中实际上比在工作的压力更大。', 'stressed', '真题', 101)],
      related=[('stressful', 'adj. 压力大的；紧张的', 101)])
    t.pending('stress', 1, '原句stressed为形容词状态用法，主词仅列名词/动词；原译“比在工作的压力更大”语句也有疑点，按原文保留待复核。')
    a('misery', '/ˈmɪzəri/', 'n. 痛苦，悲惨；穷困；悲惨的生活', 101,
      [('n.', '痛苦，悲惨；悲惨的生活'), ('n.', '穷困')],
      [(0, 'Fame brought her nothing but misery.', '名声只给她带来了痛苦。', 'misery', '例', 101),
       (0, 'People in earlier eras were surrounded by reminders of misery.', '早期时代，苦难的提示信息总是围绕着人们。', 'misery', '真题', 101)],
      '发音类似“眯着睡”→只能眯着眼睛小睡，不能躺在床上睡，是件非常痛苦和悲惨的事→痛苦，悲惨。',
      [('miserable', 'adj. 痛苦的，可怜的；令人不快的', 101)])
    a('painful', '/ˈpeɪnfl/', 'adj. 疼痛的；困难的；艰难的；令人痛苦的', 101,
      [('adj.', '疼痛的'), ('adj.', '困难的；艰难的'), ('adj.', '令人痛苦的')],
      [(0, 'My ankle is still too painful to walk on.', '我的脚腕还是疼得不能走路。', 'painful', '例', 101),
       (2, 'Why do people read negative Internet comments and do other things that will obviously be painful?', '为什么人们会阅读网络上的负面评论，并做其他明显会让人痛苦的事情？', 'painful', '真题', 101)],
      'pain（伤痛，疼痛）+ ful（形容词后缀，充满……的）→充满伤痛的→痛苦的。')
    a('torture', '/ˈtɔːtʃə(r)/', 'n. 拷打，拷问，酷刑；v. 拷打，拷问，严刑逼供；使痛苦', 101,
      [('n.', '拷打，拷问，酷刑'), ('v.', '拷打，拷问，严刑逼供'), ('v.', '使痛苦')],
      [(1, 'Many of the rebels were captured and tortured by secret police.', '反叛者中许多人被捕并遭受到秘密警察的酷刑。', 'tortured', '例', 101),
       (2, 'He spent his life tortured by the memories of his childhood.', '童年的记忆使他痛苦了一辈子。', 'tortured', '例', 101)])
    a('torment', '/ˈtɔːment/', 'n. （尤指精神上的）折磨，痛苦；苦难之源；v. 使备受折磨；使痛苦；烦扰', 101,
      [('n.', '（尤指精神上的）折磨，痛苦'), ('n.', '苦难之源'), ('v.', '使备受折磨；使痛苦；烦扰')],
      [(0, 'She suffered years of mental torment after her son’s death.', '儿子去世后，她多年悲痛欲绝。', 'torment', '例', 101),
       (2, 'He was tormented by feelings of insecurity.', '他苦于没有安全感。', 'tormented', '例', 101)],
      'tor（= tort“扭曲”）+ ment（名词后缀）→扭曲的状态→折磨，痛苦。')
    a('retort', '/rɪˈtɔːt/', 'n. 回应；反驳；v. 反驳，回嘴', 101,
      [('n.', '回应；反驳'), ('v.', '反驳，回嘴')],
      [(1, 'Sam retorted that it was my fault as much as his.', '萨姆反驳说我和他同样有错。', 'retorted', '例', 101),
       (0, 'He was stung into an angry retort.', '他被惹得愤怒反击。', 'retort', '例', 101)],
      're（回）+ tort（扭）→往回扭→反驳。')
    a('distort', '/dɪˈstɔːt/', 'v. （使）变形，扭曲；歪曲', 101,
      [('v.', '（使）变形，扭曲；歪曲')],
      [(0, 'The loudspeaker seemed to distort his voice.', '他的声音从喇叭里传出来好像失真了。', 'distort', '例', 102)],
      'dis（表示“加强”）+ tort（扭曲）→一直扭曲→扭曲，使变形。')
    group = '41 -rive相关词汇'
    a('derive', '/dɪˈraɪv/', 'v. （~from）追溯……的起源，源于；得到，获得', 102,
      [('v.', '得到，获得'), ('v.', '（~from）追溯……的起源，源于')],
      [(0, 'He derived great pleasure from painting.', '他从绘画中得到极大的乐趣。', 'derived', '例', 102),
       (1, 'This income was derived directly from his writing.', '这笔收入直接来源于他的写作。', 'derived', '例', 102)],
      '弟弟（de）沿着河（rive联想成river）走，在寻找河的源头→追溯……的起源，源于。')
    a('deprive', '/dɪˈpraɪv/', 'v. （~of）剥夺，使丧失', 102,
      [('v.', '（~of）剥夺，使丧失')],
      [(0, 'They were imprisoned and deprived of their basic rights.', '他们遭到监禁并被剥夺了基本权利。', 'deprived', '例', 102),
       (0, 'The commission ignores that for several decades America’s colleges and universities have produced graduates who don’t know the content and character of liberal education and are thus deprived of its benefits.', '委员会忽视了几十年来美国大学和学院培养的毕业生不了解人文教育的内容和特质，因此他们也无法从中受益。', 'deprived', '真题', 102)])
    a('thrive', '/θraɪv/', 'v. 兴旺，繁荣；茁壮成长', 102,
      [('v.', '兴旺，繁荣；茁壮成长')],
      [(0, 'New businesses thrive in this area.', '新企业在这一地区蓬勃兴起。', 'thrive', '例', 102),
       (0, 'Future governments need to do more to provide the conditions for sport to thrive.', '未来的政府需要做更多工作，为体育的繁荣提供条件。', 'thrive', '例', 102)],
      'thr（联想成three“三”）+ rive（联想成river“河”）→三河交汇处→三河交汇的地方是不是经济发展比较好？→繁荣，兴旺。')
    a('strive', '/straɪv/', 'v. 努力，奋斗；力争', 102,
      [('v.', '努力，奋斗；力争')],
      [(0, 'We encourage all members to strive for the highest standards.', '我们鼓励所有成员为达到最高标准而努力。', 'strive', '例', 102),
       (0, 'The most successful monarchies strive to abandon or hide their old aristocratic ways.', '最成功的君主政体都在努力摆脱或隐藏旧有的贵族习气。', 'strive', '真题', 102)],
      '发音类似“死拽我”→生活死拽着我，我只能努力奋斗→努力，奋斗。')
    a('contrive', '/kənˈtraɪv/', 'v. 设法做到，促成某事；策划', 102,
      [('v.', '设法做到，促成某事'), ('v.', '策划')],
      [(0, 'She contrived to spend a couple of hours with him every Sunday evening.', '每周星期日晚上她都设法与他待上几个小时。', 'contrived', '例', 102),
       (1, 'Evidence either way is weak, relying on contrived laboratory tests or sometimes unreliable self-reports.', '无论如何，证据都很薄弱，它们依赖于人为的实验室测试，有时（甚至）是不可靠的自陈报告。', 'contrived', '真题', 102)],
      'con（共同，一起）+ tri（三）+ ve（发音类似“我”）→我们三个人一起“努力策划”，这件事儿才可能成功。')
    t.pending('contrive', 1, 'contrived laboratory tests为形容词/分词定语“人为的”；原书主词仅列动词义，暂不作为策划动词学习例句。')
    group = '42 document相关词汇'
    a('document', '/ˈdɒkjumənt/', 'n. 公文，文件；文献；v. 记载，记录', 103,
      [('n.', '公文，文件；文献'), ('v.', '记载，记录')],
      [(1, 'Urban life in the nineteenth century is well documented.', '十九世纪的城市生活是有据可查的。', 'documented', '例', 103),
       (0, 'Planning documents pledged that the great legacy of the Games would be to lever a nation of sport lovers away from their couches.', '规划文件承诺，奥运会的伟大遗产将会让一个国家的体育爱好者离开他们的沙发。', 'documents', '真题', 103)],
      'do（发音类似“多”）+ cu（发音类似“苦”）+ ment（发音类似“闷的”）→“文件”太多了，处理它们真苦闷啊！')
    a('documentary', '/ˌdɒkjuˈmentri/', 'n. 纪录片，纪实节目；adj. 文献的，书面的；记录的；纪实的', 103,
      [('n.', '纪录片，纪实节目'), ('adj.', '文献的，书面的；记录的；纪实的')],
      [(0, 'There were some interesting interviews in the documentary.', '在纪录片中有一些有意思的访谈。', 'documentary', '例', 103),
       (1, 'Perhaps most importantly, the images provided documentary evidence.', '也许最重要的是，这些图像提供了实证。', 'documentary', '真题', 103)])
    group = '43 state形近词'
    a('statement', '/ˈsteɪtmənt/', 'n. 声明，陈述；说法；结算单；报表', 103,
      [('n.', '声明，陈述；说法'), ('n.', '结算单'), ('n.', '报表')],
      [(1, 'My bank sends me monthly statements.', '银行按月给我寄来结算单。', 'statements', '例', 103),
       (0, 'Such statements appease parents and friends.', '这样的表述可以安抚父母和朋友。', 'statements', '真题', 103)])
    a('status', '/ˈsteɪtəs/', 'n. 地位，身份；职位；状况', 103,
      [('n.', '地位，身份；职位'), ('n.', '状况')],
      [(0, 'They were granted refugee status.', '他们获得了难民身份。', 'status', '例', 103),
       (0, 'They had pushed the agency to designate the bird as “endangered”, a status that gives federal officials greater regulatory power to crack down on threats.', '他们曾敦促该机构将这种鸟列为“濒危”物种，这一地位赋予联邦官员更大的监管权力来打击威胁。', 'status', '真题', 103)])
    a('statue', '/ˈstætʃuː/', 'n. 雕像，雕塑', 103,
      [('n.', '雕像，雕塑')],
      [(0, 'The statue stands in one of the main squares.', '雕像矗立在一处主广场上。', 'statue', '例', 103),
       (0, 'The protesters toppled a statue of King George III.', '抗议者推倒了国王乔治三世的雕像。', 'statue', '例', 103)])
    material('a statue of Apollo', 103, '拓展', definition='阿波罗的雕像')
    group = '44 liberate形近词'
    a('liberate', '/ˈlɪbəreɪt/', 'v. 解放，使自由；使摆脱约束（或限制）', 103,
      [('v.', '解放，使自由'), ('v.', '使摆脱约束（或限制）')],
      [(0, 'The city was liberated by the advancing army.', '军队向前挺进，解放了那座城市。', 'liberated', '例', 103),
       (1, 'Writing poetry liberated her from the routine of everyday life.', '写诗使她从日常生活的例行公事中解脱出来。', 'liberated', '例', 103)],
      '发音类似“隶搏”→奴隶努力拼搏为自由啊→使自由，解放。',
      [('liberal', 'adj. 开明的；自由的；开放的', 103), ('liberalism', 'n. 自由主义', 104)])
    include_page(104)
    material('liberal', 104, '真题', english='At its best, the European project is remarkably liberal.', translation='在最好的情况下，欧洲项目是非常自由的。')
    a('deliberate', '/dɪˈlɪbərət/ adj.; /dɪˈlɪbəreɪt/ v.', 'adj. 故意的，蓄意的；小心翼翼的；v. 仔细考虑，深思熟虑', 104,
      [('adj.', '故意的，蓄意的'), ('adj.', '小心翼翼的'), ('v.', '仔细考虑，深思熟虑')],
      [(2, 'They deliberated on whether to continue with the talks.', '他们仔细考虑了是否继续谈判的问题。', 'deliberated', '例', 104),
       (0, 'And the best way to learn how to encode information meaningfully was a process known as deliberate practice.', '学习对信息进行有意义地编码的最佳方式是一种被称为刻意练习的过程。', 'deliberate', '真题', 104)],
      'de（离开）+ liberate（解放，使自由）→放弃自由，需要深思熟虑→仔细考虑。',
      [('deliberately', 'adv. 故意地；小心翼翼地', 104), ('deliberation', 'n. 从容；考虑', 104)])
    material('deliberately', 104, '真题', english='Deep breaths can help, as can speaking more slowly and deliberately.', translation='深呼吸会有所帮助，缓慢且更谨慎地讲话也会管用。')
    a('devote', '/dɪˈvəʊt/', 'v. （~to）投入；献身，奉献', 104,
      [('v.', '（~to）投入；献身，奉献')],
      [(0, 'I could only devote two hours a day to the work.', '我一天只能在这个工作上花两个小时。', 'devote', '例', 104),
       (0, 'But if your work is your passion, you’ll be more likely to devote yourself to it.', '但如果你的工作是你的激情所在，你就更有可能全身心地投入其中。', 'devote', '真题', 104)],
      'de（发音类似“弟”）+ vot（发誓）+ e→弟弟发誓要效忠祖国→奉献。',
      [('devoted', 'adj. 挚爱的；忠诚的；全心全意的', 104)])
    material('devoted', 104, '真题', english='Devoted concertgoers are missing the point.', translation='那些忠实的音乐会听众没有领会到问题的关键点。')
    a('dedicate', '/ˈdedɪkeɪt/', 'v. 把……奉献给；题献词；为（建筑物等）举行落成典礼', 104,
      [('v.', '把……奉献给'), ('v.', '题献词'), ('v.', '为（建筑物等）举行落成典礼')],
      [(0, 'He dedicated his life to helping the poor.', '他毕生致力于帮助穷人。', 'dedicated', '例', 104),
       (0, 'Job security or stability was the second most important career goal, followed by a sense of being dedicated to a cause or to feel good about serving the greater good.', '工作保障或稳定是第二重要的职业目标，随后是事业奉献感或服务于宏大崇高事业的满足感。', 'dedicated', '真题', 104)],
      'dedi（发音类似daddy“爸爸”）+ cat（猫咪）+ e→爸爸把自己的一生奉献给了救助流浪猫咪的事业→把……奉献给。',
      [('dedicated', 'adj. 专心致志的，献身的', 104)])
    t.pending('dedicate', 1, 'being dedicated to a cause呈状态形容词语义，原书另列dedicated派生形容词；英文并列or to feel结构也有疑点，保留原文及原译待复核。')
    a('delicate', '/ˈdelɪkət/', 'adj. 易碎的，脆弱的；微妙的；精巧的，精致的，精美的；熟练的', 104,
      [('adj.', '易碎的，脆弱的'), ('adj.', '微妙的'), ('adj.', '精巧的，精致的，精美的'), ('adj.', '熟练的')],
      [(0, 'Babies have very delicate skin.', '婴儿的皮肤非常娇嫩。', 'delicate', '例', 105),
       (1, 'Parents still have a major role to play, but now it is more delicate.', '父母仍然扮演着重要的角色，但现在这个角色更加微妙了。', 'delicate', '真题', 105)],
      '发音类似“得离开他”→他这人太脆弱了，他妈妈决定离开他一段时间，让他自己锻炼一下→脆弱的。')
