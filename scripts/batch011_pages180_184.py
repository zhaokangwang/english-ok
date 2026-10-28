"""Visual transcription of sixth-unit headwords beginning on PDF180–184."""
COMPLETE_THROUGH = 184
NEXT_WORD = 'flourish'
NEXT_PAGE = 185

def append(t, associated):
    group = '12 大、宽、高相关词汇'
    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(2104+len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-006'
    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))
    def include_page(page):
        w = t.words[-1]
        w['pdf_pages'] = sorted(set(w['pdf_pages']+[page]))
        w['printed_pages'] = [f'{p-8:03}' for p in w['pdf_pages']]

    a('width', '/wɪdθ/', 'n. 宽度，广度', 180,
      [('n.', '宽度，广度')],
      [(0, 'It’s about ten metres in width.', '它大约有10米宽。', 'width', '例', 180),
       (0, 'The snow had narrowed the width of the road to a single track.', '大雪使路面变窄，成了单行道。', 'width', '例', 180)])
    group = '13 宽恕、同情相关词汇'
    a('mercy', '/ˈmɜːsi/', 'n. 仁慈，宽恕；幸运；恩惠', 180,
      [('n.', '仁慈，宽恕'), ('n.', '幸运'), ('n.', '恩惠')],
      [(0, 'In The Prince, he championed cunning, ruthlessness, and boldness, rather than virtue, mercy and justice, as the skills of successful leaders.', '在《君主论》中，他将狡诈、无情和勇敢作为成功领导人的技能，而非美德、仁慈和公正。', 'mercy', '真题', 180)],
      '发音类似“没事”→孩子打碎了花瓶，妈妈却说：“没事。”→妈妈对孩子很“仁慈”→仁慈。')
    a('sympathy', '/ˈsɪmpəθi/', 'n. 同情；赞同，支持；意气相投；志同道合', 180,
      [('n.', '赞同，支持'), ('n.', '同情'), ('n.', '意气相投；志同道合')],
      [(0, 'The seamen went on strike in sympathy with the dockers.', '海员举行罢工，以表示对码头工人的支持。', 'sympathy', '例', 180),
       (1, 'Mental health allows us to view others with sympathy if they are having troubles, with kindness if they are in pain.', '心理健康使我们在他人遇到麻烦时心怀同情，在他人遭遇痛苦时善意相待。', 'sympathy', '真题', 180)],
      'sym（同样的）+ pathy（感觉）→跟对方有同样的感觉，感同身受→同情。',
      [('sympathise', '（美sympathize）v. 同情；赞同', 180)])
    material('sympathise', 180, '例', english='Don’t always rely on others to understand and sympathise.', translation='不要老是指望别人的理解和同情。')
    a('sympathetic', '/ˌsɪmpəˈθetɪk/', 'adj. 同情的，有同情心的；赞同的；支持的；让人喜欢的', 180,
      [('adj.', '同情的，有同情心的'), ('adj.', '赞同的；支持的'), ('adj.', '让人喜欢的')],
      [(0, 'She was very sympathetic when I was sick.', '我生病时，她非常同情我。', 'sympathetic', '例', 180),
       (0, 'The guilt-prone ones share more, even though they hadn’t magically become more sympathetic to the other child’s deprivation.', '容易感到内疚的孩子会分享更多，虽然他们并没有魔法般地变得更加同情对方的贫穷。', 'sympathetic', '真题', 180)])
    a('pathetic', '/pəˈθetɪk/', 'adj. 可怜的，可悲的，令人怜惜的；无力的', 180,
      [('adj.', '可怜的，可悲的，令人怜惜的'), ('adj.', '无力的')],
      [(0, 'She thought he looked a pathetic figure of a man.', '她认为他看上去是个可悲的男人。', 'pathetic', '例', 180),
       (1, 'She made a pathetic attempt to smile.', '她勉强地微微一笑。', 'pathetic', '例', 180)])
    group = '14 sym-、-sem-相关词汇'
    a('symbol', '/ˈsɪmbl/', 'n. 符号，代号，记号；象征', 181,
      [('n.', '象征'), ('n.', '符号，代号，记号')],
      [(0, 'The new school stands as a symbol of hope for a better future.', '这所新学校象征着对美好未来的希望。', 'symbol', '例', 181),
       (1, 'A list of symbols used on the map is given in the index.', '这份地图所使用的符号全部列在索引中。', 'symbols', '例', 181)],
      'sym（同样的）+ bol（发音类似ball“球”）→你可以在相同的球上做一样的“符号”，这样便于你找到它们→符号。',
      [('symbolic', 'adj. 象征性的；作为象征的', 181), ('symbolise', '（美symbolize）v. 象征，代表', 181)])
    a('resemble', '/rɪˈzembl/', 'v. 看起来像；显得像；像', 181,
      [('v.', '看起来像；显得像；像')],
      [(0, 'So many hotels resemble each other.', '许多酒店看上去都差不多。', 'resemble', '例', 181),
       (0, 'The robot was the same size as a regular rat but resembled a simple plastic box.', '该机器鼠的大小与普通老鼠一样，但（外形）却像一个简单的塑料盒。', 'resembled', '真题', 181)],
      're（一再）+ sem（联想成same“一样的”）+ ble→一再地使他们变成一样→与……相似→像。')
    a('assemble', '/əˈsembl/', 'v. 集合，聚集；组装，装配', 181,
      [('v.', '集合，聚集'), ('v.', '组装，装配')],
      [(0, 'We had assembled for the first rehearsal.', '我们集合起来进行第一次排练。', 'assembled', '例', 181),
       (1, 'The shelves are easy to assemble.', '这些架子容易装配。', 'assemble', '例', 181)],
      'as（表示“加强”）+ sem（联想成same“一样的”）+ ble→把一样的人都“聚集”到一起→聚集。')
    a('symptom', '/ˈsɪmptəm/', 'n. 征候；征兆；症状', 181,
      [('n.', '症状'), ('n.', '征候；征兆')],
      [(0, 'Symptoms include a headache and sore throat.', '症状包括头痛和咽喉疼痛。', 'Symptoms', '例', 181),
       (0, 'And stay alert to serious symptoms, such as chest pain or pressure, severe shortness of breath or dizziness, or faintness, and seek medical attention immediately.', '要对胸痛、胸闷、严重呼吸急促、头晕、昏厥等严重的症状保持警惕，并立即就医。', 'symptoms', '真题', 181)])
    group = '15 原子、电子相关词汇'
    a('atom', '/ˈætəm/', 'n. 原子', 181,
      [('n.', '原子')],
      [(0, 'Two atoms of hydrogen combine with one atom of oxygen to form a molecule of water.', '两个氢原子和一个氧原子结合组成一个水分子。', 'atoms', '例', 181)],
      '发音类似“阿童木”→阿童木别名“原子”小金刚→原子。')
    material('the splitting of the atom', 181, '拓展', definition='原子的分裂')
    a('electron', '/ɪˈlektrɒn/', 'n. 电子', 181,
      [('n.', '电子')],
      [(0, 'The electron microscope uses a beam of electrons to produce images at high magnifications.', '电子显微镜利用一束电子产生高倍放大的影像。', 'electrons', '例', 182)],
      '发音类似“一来可愁”→当什么来临的时候，父母会发愁呢？电子化的时代。很多孩子容易沉迷玩游戏→电子。',
      [('electronic', 'adj. 电子的；电子设备的', 182)])
    material('electronic', 182, '例', english='Airline passengers no longer have to turn off all electronic devices while on the plane.', translation='飞机上的乘客不再需要关闭所有的电子设备。')
    material('electronic money', 182, '拓展', definition='电子货币')
    a('nuclear', '/ˈnjuːkliə(r)/', 'adj. 原子能的，核能的；核武器的', 182,
      [('adj.', '原子能的，核能的'), ('adj.', '核武器的')],
      [(0, 'It will produce electricity more cheaply than a nuclear plant.', '它的发电成本要比核电站低。', 'nuclear', '例', 182),
       (0, 'Nuclear power is cleaner than coal.', '核能比煤更清洁。', 'Nuclear', '例', 182)])
    material('a nuclear reactor', 182, '拓展', definition='核反应堆')
    group = '16 analyse相关形近词汇'
    a('analyse', '/ˈænəlaɪz/', 'v. 分析；对……进行精神分析', 182,
      [('v.', '分析'), ('v.', '对……进行精神分析')],
      [(0, 'The job involves collecting and analysing data.', '这项工作包括收集和分析数据。', 'analysing', '例', 182),
       (0, 'He analyses the weak lecture, learning lessons for the future about what works and what doesn’t.', '他分析这次失败的演讲，为以后吸取教训，了解哪些可取，哪些不可取。', 'analyses', '真题', 182)],
      related=[('analysis', 'n. 分析；分析结果', 182)])
    t.words[-1]['notes'].append('原书并列美式拼写analyze；保留analyse为主词，不另建重复词条。')
    material('analysis', 182, '真题', english='The great question is who should benefit from the analysis of all the data that our lives now generate.', translation='重要的问题是，谁应该从我们现今生活中产生的所有数据的分析中受益。')
    a('emphasise', '/ˈemfəsaɪz/', 'v. 强调，重视，着重；使突出，使明显', 182,
      [('v.', '强调，重视，着重'), ('v.', '使突出，使明显')],
      [(0, 'She emphasised the point in an interview at the weekend.', '她在周末的一次采访中强调了这一点。', 'emphasised', '例', 182),
       (0, 'They emphasised parents’ legal responsibilities.', '他们强调了父母的法律责任。', 'emphasised', '例', 182)],
      'em（前缀，表示“使”）+ phas（词根，表示“显露”）+ ise（动词后缀）→使显露出来→强调，使突出。',
      [('emphasis', 'n. 强调，重视，重要性', 182)])
    t.words[-1]['notes'].append('原书并列美式拼写emphasize；保留emphasise为主词，不另建重复词条。')
    material('emphasis', 182, '例', english='Increased emphasis is now being placed on corporate image.', translation='现在越来越强调企业形象。')
    group = '17 忍受、遭受相关词汇'
    a('tolerate', '/ˈtɒləreɪt/', 'v. 允许，容许；忍受，容忍', 182,
      [('v.', '允许，容许'), ('v.', '忍受，容忍')],
      [(0, 'This sort of behaviour will not be tolerated.', '这种行为是不能容许的。', 'tolerated', '例', 183),
       (1, 'I don’t know how you tolerate that noise!', '我不知道你怎么能忍受那样的噪声！', 'tolerate', '例', 183)],
      'tole（发音类似“逃了”）+ rate（速度）→他以很快的速度逃跑了。为什么？他“忍受”到了极点，受不了了→忍受，容忍。',
      [('tolerant', 'adj. 容忍的，宽容的', 183), ('tolerance', 'n. 容忍；宽容', 183)])
    material('tolerance', 183, '例', english='She had no tolerance for jokes of any kind.', translation='她容不得开任何玩笑。')
    a('undergo', '/ˌʌndəˈɡəʊ/', 'v. 经历，遭受', 183,
      [('v.', '经历，遭受')],
      [(0, 'The drug is currently undergoing trials in America.', '这种药目前正在美国进行试验。', 'undergoing', '例', 183),
       (0, 'Consequently, our feelings, thoughts and emotions have undergone a corresponding change.', '因此，我们的感觉、思想和情绪也发生了相应的变化。', 'undergone', '真题', 183)])
    a('endure', '/ɪnˈdjʊə(r)/', 'v. 忍受，忍耐；持久，持续', 183,
      [('v.', '忍受，忍耐'), ('v.', '持久，持续')],
      [(0, 'The pain was almost too great to endure.', '痛苦几乎难以忍受。', 'endure', '例', 183),
       (0, 'Equally, there is a sense that the travails of commuters in the South East, many of whom will face among the biggest rises, have received too much attention compared to those who must endure the relatively poor infrastructure of the Midlands and the North.', '此外，与中部、北部地区不得不忍受相对落后的基础设施的通勤者相比，东南部地区通勤者的出行困境（其中许多人将面临最大的票价涨幅）受到了过多关注。', 'endure', '真题', 183)],
      'end（最后）+ ure→他一直坚持到最后→忍耐，忍受。')
    a('duration', '/djuˈreɪʃn/', 'n. 期间；持续时间', 183,
      [('n.', '期间；持续时间')],
      [(0, 'The next contract will be of shorter duration.', '下一个合同持续时间会短一些。', 'duration', '例', 183),
       (0, 'But among student subjects who discussed meat ethics, meal purchases containing meat decreased from 52 to 45 percent—and this effect held steady for the study’s duration of several weeks.', '但是，在参与探讨肉食伦理的学生受试人群中，肉餐购买比率从52%下降到45%——而且这一影响在研究持续的几周内一直保持平稳。', 'duration', '真题', 183)],
      related=[('durable', 'adj. 持久的，耐用的', 183)])
    material('non-durable', 183, '真题', status='quarantined',
      english='Mass-produced clothing, like fast food, fills a hunger and need, yet is non-durable and wasteful.',
      translation='批量生产的服装，就像快餐一样，满足了饥饿感和需求，但却不耐用且浪费。',
      reason='原书列在durable派生项下，实际目标non-durable含否定前缀；关联保存，不把不耐用反挂到耐用义。')
    group = '18 污染相关词汇'
    a('pollute', '/pəˈluːt/', 'v. 弄脏，污染', 183,
      [('v.', '弄脏，污染')],
      [(0, 'Chemical wasted pollute the rivers and streams.', '化学废物污染了河流和小溪。', 'pollute', '例', 183),
       (0, 'Madrid was hailed as a public health beacon last November when it rolled out ambitious restrictions on the most polluting cars.', '去年11月，马德里针对污染最严重的汽车推出了耗时巨大的管控措施，因此被誉为公共卫生健康的灯塔。', 'polluting', '真题', 183)],
      related=[('pollution', 'n. 污染；污染物', 183), ('pollutant', 'n. 污染物（质）', 183)])
    t.pending('pollute', 0, '原书Chemical wasted pollute中wasted词形和主谓搭配存疑，保留原文待核。')
    t.pending('pollute', 1, 'ambitious restrictions原译耗时巨大的管控措施，译义存在疑点，保留原文原译待核，不入队。')
    a('contaminate', '/kənˈtæmɪneɪt/', 'v. 污染，弄脏；毒害', 184,
      [('v.', '污染，弄脏'), ('v.', '毒害')],
      [(0, 'The drinking water has become contaminated with lead.', '饮用水被铅污染了。', 'contaminated', '例', 184),
       (1, 'They were accused of contaminating the minds of our young people.', '他们被指控毒害我们青少年的心灵。', 'contaminating', '例', 184)],
      related=[('contamination', 'n. 污染，弄脏；毒害', 184)])
    group = '19 培养、养育相关词汇'
    a('rear', '/rɪə(r)/', 'v. 抚养，养育，培养；饲养；adj. 后方的，后面的；n. 后面，后部', 184,
      [('v.', '抚养，养育，培养'), ('v.', '饲养'), ('adj.', '后方的，后面的'), ('n.', '后面，后部')],
      [(0, 'She reared a family of five on her own.', '她一个人养活五个孩子。', 'reared', '例', 184),
       (0, 'Nothing gets people talking like the suggestion that child rearing is anything less than a completely fulfilling, life-enriching experience.', '没有什么比“育儿绝非完全是成就自我、丰富生活的体验”这一提议更能引发人们的讨论了。', 'rearing', '真题', 184)],
      '多数父母希望可以把自己的孩子抚养（rear）成真正（really）有用的人。')
    t.pending('rear', 1, 'child rearing在本句为名词化的育儿用法，原书未列独立名词养育义，暂不直接挂到动词义。')
    a('cultivate', '/ˈkʌltɪveɪt/', 'v. 耕作，种植；栽培，培养；逐渐形成', 184,
      [('v.', '耕作，种植'), ('v.', '栽培，培养'), ('v.', '逐渐形成')],
      [(0, 'The land here has been intensively cultivated for generations.', '这片土地经过了几代人的精耕细作。', 'cultivated', '例', 184),
       (0, 'The people cultivate mainly rice and beans.', '这里的人们主要种植水稻和豆类。', 'cultivate', '例', 184)],
      '老师们希望把学生们培养（cultivate）成有文化的（cultural）人才。',
      [('cultivation', 'n. 耕作；培养', 184), ('cultivated', 'adj. 有教养的；有修养的', 184)])
    a('breed', '/briːd/', 'v. 交配繁殖；饲养，培育（动植物）；n. 品种；种类，（人的）类型', 184,
      [('n.', '种类，（人的）类型'), ('v.', '饲养，培育（动植物）'), ('v.', '交配繁殖'), ('n.', '品种')],
      [(0, 'He represents a new breed of politician.', '他代表着新一类的政治家。', 'breed', '例', 184),
       (1, 'The rabbits are bred for their long coats.', '饲养兔子是为了获取它们的长毛。', 'bred', '例', 184)],
      '发音类似“哺育的”→饲养，培育。')
    a('foster', '/ˈfɒstə(r)/', 'v. 促进；助长；培养；鼓励；代养；抚育', 184,
      [('v.', '促进；助长'), ('v.', '培养；鼓励'), ('v.', '代养；抚育')],
      [(0, 'Such organizations need to foster innovation.', '这些组织需要促进创新。', 'foster', '例', 184),
       (2, 'They have fostered over 60 children during the past ten years.', '在过去10年间，他们抚育了60多个儿童。', 'fostered', '例', 184)],
      'fo（发音类似four“四个”）+ ster（联想成sister“姐姐”）→我的四个姐姐都是妈妈“培养”的→培养。')
    a('nourish', '/ˈnʌrɪʃ/', 'v. 滋养，抚养；养育；培养；促进', 184,
      [('v.', '培养；促进'), ('v.', '滋养，抚养；养育')],
      [(0, 'By investing in education, we nourish the talents of our children.', '我们通过教育投资，培养孩子们的才能。', 'nourish', '例', 184),
       (1, 'All the children were well nourished and in good physical condition.', '所有这些孩子都营养良好，身体健康。', 'nourished', '例', 185)],
      'nouris（联想成nurse“培育”）+ h→抚养，培养。')
