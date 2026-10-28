"""Visual transcription of headwords beginning on PDF120–124."""
COMPLETE_THROUGH = 124
NEXT_WORD = 'energetic'
NEXT_PAGE = 125


def append(t, associated):
    group = '14 particular相关词汇'

    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(1105 + len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-004'

    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))

    def include_page(page):
        w = t.words[-1]
        w['pdf_pages'] = sorted(set(w['pdf_pages'] + [page]))
        w['printed_pages'] = [f'{p-8:03}' for p in w['pdf_pages']]

    a('specialist', '/ˈspeʃəlɪst/', 'n. 专家；专科医生', 120,
      [('n.', '专家'), ('n.', '专科医生')],
      [(0, 'She is a specialist in children’s literature.', '她是儿童文学领域的专家。', 'specialist', '例', 120),
       (0, 'Yet his vast body of writings on music is unknown save to specialists.', '然而，他关于音乐的大量著作，除了专家之外，也鲜为人知。', 'specialists', '真题', 120)])
    a('speciality', '/ˌspeʃiˈæləti/', 'n. 特产；特色菜；专业，专长', 120,
      [('n.', '特产；特色菜'), ('n.', '专业，专长')],
      [(0, 'The drink is a house speciality prepared at the table.', '这是一种现调制的餐厅特色饮料。', 'speciality', '例', 120),
       (1, 'My speciality is international tax law.', '我的专业是国际税法。', 'speciality', '例', 120)])
    t.words[-1]['notes'].append('原书同时标美式specialty；使用speciality作为主词，不重复计数。')
    a('expert', '/ˈekspɜːt/', 'n. 专家，行家；adj. 老练的，内行的', 120,
      [('adj.', '老练的，内行的'), ('n.', '专家，行家')],
      [(0, 'His expert evidence played a key role in the trial.', '他的专家证据在审判中起了关键作用。', 'expert', '例', 120),
       (1, 'I don’t pretend to be an expert on the subject.', '我不想妄称自己是该学科的专家。', 'expert', '例', 120)],
      related=[('expertise', 'n. 专门知识，专长', 120)])
    material('expertise', 120, '例', english='We have the expertise to help you run your business.', translation='我们有帮助你经营自己企业的专门知识。')
    a('specific', '/spəˈsɪfɪk/', 'adj. 具体的，详细的；特定的', 120,
      [('adj.', '特定的'), ('adj.', '具体的，详细的')],
      [(0, 'The money was collected for a specific purpose.', '这笔钱是为一个特定用途而收的。', 'specific', '例', 120)],
      related=[('specify', 'v. 详细说明', 120), ('specification', 'n. 规格，规范；明细单；说明书', 120)])
    material('specify', 120, '真题', english='The justices had to specify novel rules for the new personal domain of the passenger car.', translation='那时法官们不得不为小轿车这一新兴私人领域明确新规则。')
    material('specification', 120, '例', english='The office was furnished to a high specification.', translation='办公室是按高规格装潢的。')
    a('peculiar', '/pɪˈkjuːliə(r)/', 'adj. 怪异的；特殊的；不舒服', 120,
      [('adj.', '怪异的'), ('adj.', '特殊的'), ('adj.', '不舒服')],
      [(0, 'There was something peculiar in the way he smiled.', '他笑起来有点怪。', 'peculiar', '例', 120),
       (1, 'But, the force of geographic conditions peculiar to America and the sheer difficulty of maintaining old-world ways in a raw, new continent caused significant changes.', '但是，美国特有的地理条件的作用以及在这个原始的新大陆上维持旧世界方式的巨大困难，引发了巨大的变化。', 'peculiar', '真题', 120)],
      'pecu（皮裤）+ li（里）+ ar（表示人的后缀）→他这个人运动裤里又穿了条皮裤，真的是“怪异”！→怪异的。',
      [('peculiarity', 'n. 特性；奇怪；怪癖', 121)])
    include_page(121)
    group = '15 优劣相关词汇'
    a('inferior', '/ɪnˈfɪəriə(r)/', 'adj. 较差的；次的；下级的；n. 级别（或地位）低的人', 121,
      [('adj.', '较差的；次的'), ('adj.', '下级的'), ('n.', '级别（或地位）低的人')],
      [(0, 'Modern music is often considered inferior to that of the past.', '现代音乐常被认为不如过去的。', 'inferior', '例', 121)],
      '里面（in）是废的（fer），一个人内在是废的，那就是“差的，劣等的”。',
      [('inferiority', 'n. 低等，劣等；劣势', 121)])
    material('inferiority', 121, '真题', english='Working with your hands is seen as almost a mark of inferiority.', translation='用双手工作几乎被看作是低下的表现。')
    a('superior', '/suːˈpɪəriə(r)/', 'n. 级别（或地位、职位）更高的人，上级，上司；adj. 更高级的', 121,
      [('adj.', '更高级的'), ('n.', '级别（或地位、职位）更高的人，上级，上司')],
      [(0, 'She felt socially superior to most of her neighbours.', '她觉得自己的社会地位比多数邻居高。', 'superior', '例', 121),
       (0, 'I’ll need to check with my superior officer.', '我需要和我的上级长官核实一下。', 'superior', '例', 121)],
      'super（超越，在……上面）+ i + or（表示人的后缀）→在你上面的那个人→上司，长辈。')
    a('superb', '/suːˈpɜːb/', 'adj. 极佳的，卓越的，质量极高的', 121,
      [('adj.', '极佳的，卓越的，质量极高的')],
      [(0, 'The car is in superb condition.', '这辆车车况极好。', 'superb', '例', 121),
       (0, 'He got a superb chance to show his talent.', '他得到了一个极好的机会来展示他的才能。', 'superb', '例', 121)],
      'super（超越）+ b（联想成“不”）→不能被超越的，无法被超越的→极好的，卓越的。')
    a('supreme', '/suːˈpriːm/', 'adj. 最高的，至高无上的；最大的', 121,
      [('adj.', '最高的，至高无上的'), ('adj.', '最大的')],
      [(0, 'It is an event in which she reigns supreme.', '这个比赛项目她所向无敌。', 'supreme', '例', 121)])
    material('the Supreme Court', 121, '拓展', definition='最高法院')
    material('the Supreme Court', 121, '例', english='The Supreme Court has delivered its opinion in a controversial case.', translation='最高法院对一个有争议的案件发表了意见。')
    a('superiority', '/suːˌpɪəriˈɒrəti/', 'n. 优势，优越性', 121,
      [('n.', '优势，优越性')],
      [(0, 'They tend to have a sense of superiority over their peers.', '他们往往比同龄人有优越感。', 'superiority', '例', 121)])
    group = '16 宗教相关语境词汇'
    a('superstition', '/ˌsuːpəˈstɪʃn/', 'n. 迷信', 121,
      [('n.', '迷信')],
      [(0, 'Most cultures have their superstitions.', '大多数文化都有自己的迷信。', 'superstitions', '例', 121),
       (0, 'Their thinking often had a traditional superstitions quality.', '他们的想法往往有一种传统的迷信特征。', 'superstitions', '真题', 121)],
      'super（在……上面）+ stit（联想成stand“站”）+ ion（名词后缀）→有些人觉得一些东西可以站在科学之上，我们认为这些人是有些“迷信”的→迷信。',
      [('superstitious', 'adj. 迷信的', 122)])
    t.pending('superstition', 1, '原书为superstitions quality，名词复数定语搭配可疑，按原文保存，待核对。')
    include_page(122)
    a('religion', '/rɪˈlɪdʒən/', 'n. 宗教，宗教信仰', 122,
      [('n.', '宗教，宗教信仰')],
      [(0, 'This kind of thinking is why so many people try to avoid arguments, especially about politics and religion.', '这种想法就是为什么这么多人试图避免争论，特别是关于政治和宗教的争论。', 'religion', '真题', 122)],
      related=[('religious', 'adj. 宗教的；虔诚的', 122)])
    material('religious', 122, '例', english='His wife is very religious.', translation='他的妻子非常虔诚。')
    a('regime', '/reɪˈʒiːm/', 'n. 政权，政体；社会制度；管理体制', 122,
      [('n.', '政权，政体'), ('n.', '社会制度；管理体制')],
      [(0, 'Crowds celebrated the downfall of the old regime.', '成群的人们欢庆旧政权的垮台。', 'regime', '例', 122),
       (0, 'The new regime was prepared to compromise on the oil dispute.', '新政权打算在石油争端上作出让步。', 'regime', '例', 122)])
    group = '17 关系相关词汇'
    a('relate', '/rɪˈleɪt/', 'v. （使）有联系；叙述', 122,
      [('v.', '（使）有联系'), ('v.', '叙述')],
      [(0, 'In the future, pay increases will be related to productivity.', '以后，工资的上涨将和业绩挂钩。', 'related', '例', 122),
       (0, 'Office speak can help you figure out how you relate to your work and how your work defines who you are.', '办公室语言可以帮助你弄清楚你和工作的关系，以及你的工作如何定义你是谁。', 'relate', '真题', 122)],
      're（重复）+ late（迟到）→你老是迟到，你得给我们讲述清楚你迟到的原因→讲述；叙述。',
      [('related', 'adj. 有关的，相关的', 122), ('unrelated', 'adj. 无关的', 122)])
    a('relation', '/rɪˈleɪʃn/', 'n. 关系，关联；亲属', 122,
      [('n.', '关系，关联'), ('n.', '亲属')],
      [(0, 'They attach too much importance to public relations.', '他们太重视公共关系了。', 'relations', '例', 122)],
      related=[('relative', 'n. 亲戚；adj. 相关的；相对的', 122)])
    material('relative', 122, '例', english='Mary is going to get a little dog from one of her relatives.', translation='玛丽打算从她的一个亲戚那里领养一只小狗。')
    a('relationship', '/rɪˈleɪʃnʃɪp/', 'n. 关系，联系', 122,
      [('n.', '关系，联系')],
      [(0, 'The relationship between the police and the local community has improved.', '警察和当地民众之间的关系已经得到改善。', 'relationship', '例', 122),
       (0, 'So they feel a responsibility to you to keep that relationship going.', '所以他们觉得对你有维持这一关系的责任。', 'relationship', '真题', 122)])
    a('correlate', '/ˈkɒrəleɪt/', 'v. 相关；关联', 122,
      [('v.', '相关；关联')],
      [(0, 'A high-fat diet correlates with a greater risk of heart disease.', '高脂肪饮食与增加心脏病发作的风险密切相关。', 'correlates', '例', 122),
       (0, 'That’s because economic growth can be correlated with environmental degradation, while protecting the environment is sometimes correlated with greater poverty.', '那是因为经济增长可能与环境退化有关，而保护环境有时与更重的贫困有关。', 'correlated', '真题', 122)])
    a('relevant', '/ˈreləvənt/', 'adj. 紧密相关的；切题的', 123,
      [('adj.', '紧密相关的'), ('adj.', '切题的')],
      [(0, 'The incident is still under investigation by the relevant authorities.', '该事件仍在接受有关当局的调查。', 'relevant', '例', 123),
       (0, 'Send me all the relevant information.', '把所有相关资料发给我。', 'relevant', '例', 123)],
      related=[('relevance', 'n. 相关性；实用性；意义', 123)])
    material('relevance', 123, '例', english='I don’t see the relevance of your question.', translation='我不懂你这个问题有什么意义。')
    group = '18 re相关词汇'
    a('regulate', '/ˈreɡjuleɪt/', 'v. 管理；调节；控制', 123,
      [('v.', '管理'), ('v.', '调节'), ('v.', '控制')],
      [(0, 'The department is responsible for regulating the insurance industry.', '该部门负责监管保险业。', 'regulating', '例', 123),
       (0, 'Communities throughout New England have been attempting to regulate short-term rentals.', '整个新英格兰地区的各个社区就一直在试图规范短期租赁。', 'regulate', '真题', 123)],
      're（发音类似“阿姨”）+ gu（联想成“规定”）+ late（迟到）→阿姨规定我们不要迟到，所以我们要提前调整好我们各自的生物钟→调节，调整。',
      [('regulation', 'n. 章程，规章制度，规则；法规；管理；控制', 123)])
    a('regular', '/ˈreɡjələ(r)/', 'adj. 规则的；定期的，有规律的；频繁的，经常的；标准尺寸的；中等大小的；普通的，平凡的；n. 常客，老主顾', 123,
      [('adj.', '定期的，有规律的'), ('adj.', '规则的'), ('adj.', '频繁的，经常的'), ('adj.', '标准尺寸的；中等大小的'), ('adj.', '普通的，平凡的'), ('n.', '常客，老主顾')],
      [(0, 'We also hold a regular monthly meeting.', '我们还每月定期举行会议。', 'regular', '例', 123)],
      related=[('regularly', 'adv. 有规律地；经常地', 123)])
    material('regularly', 123, '例', english='She regularly appears on TV.', translation='她经常在电视上露面。')
    a('resort', '/rɪˈzɔːt/', 'n. 求助；诉诸；采取；（度假）胜地；v. （～ to）求助于，诉诸', 123,
      [('v.', '（～ to）求助于，诉诸'), ('n.', '（度假）胜地'), ('n.', '求助；诉诸；采取')],
      [(0, 'We had to resort to another loan from the bank.', '我们不得不求助于银行的另一笔贷款。', 'resort', '例', 123),
       (1, 'They spent a month at a fashionable ski resort in Switzerland.', '他们在瑞士一个时尚的滑雪胜地待了一个月。', 'resort', '例', 123)],
      're（发音类似“阿姨”）+ sort（分类）→阿姨不懂垃圾分类，只能“求助”于我→求助。')
    a('release', '/rɪˈliːs/', 'v. 释放；放开；发表，发行；发泄；n. 释放；公开；发行；发布；排放；解脱', 123,
      [('v.', '释放；放开'), ('v.', '发表，发行'), ('v.', '发泄'), ('n.', '释放'), ('n.', '公开；发行；发布'), ('n.', '排放'), ('n.', '解脱')],
      [(0, 'He was released without charge after questioned by the police.', '他经警方讯问后被免于起诉并释放了。', 'released', '例', 123),
       (4, 'Therefore, unless customers are prepared to sign release agreements, the use of AI may become somewhat restricted in the future.', '因此，除非客户准备签署发布协议，否则未来人工智能的使用可能会受到一定程度的限制。', 'release', '真题', 123)],
      're（发音类似“阿姨”）+ lease（发音类似“立誓”）→阿姨立誓，说要减肥，不吃肉了，这个消息要“发布”给大家→发布。')
    t.pending('release', 0, '原书after questioned缺少being等成分，按原文保留，待核对语法。')
    t.pending('release', 1, 'release agreements的确切语境和词义待核对，暂不直接挂到原书发布义。')
    group = '19 公布相关语境词汇'
    a('publicity', '/pʌbˈlɪsəti/', 'n. （媒体的）关注，报道；宣传；传播工作', 124,
      [('n.', '（媒体的）关注，报道'), ('n.', '宣传；传播工作')],
      [(0, 'There has been a great deal of publicity surrounding his disappearance.', '他的失踪已被媒体广泛报道。', 'publicity', '例', 124),
       (1, 'Taking part in the event will be good publicity for our school.', '参与这项活动对我们学校将是很好的宣传。', 'publicity', '例', 124)],
      'public（公开的）+ ity（名词后缀）→媒体公开的东西→报道。')
    a('bulletin', '/ˈbʊlətɪn/', 'n. 公告，布告；新闻简报', 124,
      [('n.', '公告，布告'), ('n.', '新闻简报')],
      [(0, 'The government will issue an official bulletin later this week.', '本周晚些时候政府将发布一则官方公告。', 'bulletin', '例', 124),
       (0, 'We posted bulletins all day long.', '我们整天都在发布公告。', 'bulletins', '真题', 124)])
    a('publish', '/ˈpʌblɪʃ/', 'v. 出版，发行，发表；公开', 124,
      [('v.', '发表'), ('v.', '出版，发行'), ('v.', '公开')],
      [(0, 'Many plays were published anonymously.', '很多剧本都是匿名发表的。', 'published', '例', 124),
       (0, 'They publish more than 1.2 million articles each year in some 16,000 journals.', '他们每年在大约16000种期刊上发表120多万篇文章。', 'publish', '真题', 124)],
      related=[('publication', 'n. 出版，出版物', 124), ('publisher', 'n. 出版人（或机构），发行人（或机构）', 124)])
    a('punish', '/ˈpʌnɪʃ/', 'v. 处罚，惩罚；对……判罪；自责', 124,
      [('v.', '处罚，惩罚'), ('v.', '对……判罪'), ('v.', '自责')],
      [(0, 'My parents used to punish me by not letting me watch TV.', '过去我父母常以不让我看电视来惩罚我。', 'punish', '例', 124)],
      '发音类似“怕你失（迷失自己）”→妈妈怕你迷失自己，所以严格管教你，做错事会“惩罚”你→惩罚。',
      [('punishment', 'n. 惩罚；处罚；刑罚', 124)])
    a('issue', '/ˈɪʃuː/', 'n. 问题；议题；发行；期号；v. 宣布，公布；发出；出版，发行', 124,
      [('v.', '出版，发行'), ('n.', '问题；议题'), ('n.', '发行'), ('n.', '期号'), ('v.', '宣布，公布'), ('v.', '发出')],
      [(0, 'They issued a special set of stamps to mark the occasion.', '他们发行了一套特别的邮票来纪念这个场合。', 'issued', '例', 124),
       (1, 'Discussing the issue in private will make the powerful person feel less threatened.', '私下讨论这一问题会让这位权势人物觉得不那么受到威胁。', 'issue', '真题', 124)])
    a('tissue', '/ˈtɪʃuː/', 'n. 纸巾，手巾纸；组织', 124,
      [('n.', '组织'), ('n.', '纸巾，手巾纸')],
      [(0, 'Dyes were extracted by boiling the plant tissue.', '用煮的方法从植物组织中提取染料。', 'tissue', '例', 124),
       (1, 'She scrubbed at her face with a tissue.', '她用一张纸巾擦脸。', 'tissue', '例', 124)],
      '掏出口袋里的餐巾纸看一下，上面会有个英文单词tissue。')
    a('phenomenon', '/fəˈnɒmɪnən/', 'n. 现象；非凡的人（或事物）', 124,
      [('n.', '现象'), ('n.', '非凡的人（或事物）')],
      [(0, 'Globalization is a phenomenon of the 21st century.', '全球化是21世纪的现象。', 'phenomenon', '例', 124),
       (1, 'Harry Potter was the greatest book publishing phenomenon ever.', '《哈利·波特》是图书出版史上最了不起的成功典范。', 'phenomenon', '例', 125)])
