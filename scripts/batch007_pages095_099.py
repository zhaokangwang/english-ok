"""Continuation from PDF95 cancel; append only visually reviewed records."""
COMPLETE_THROUGH = 99
NEXT_WORD = 'dim'
NEXT_PAGE = 100

def append(t, associated):
    group = '31 消除相关词汇'
    def a(spelling, ipa, definition, page, senses, examples, mnemonic='', related=()):
        t.add(1000 + len(t.words), spelling, ipa, definition, page, group,
              senses, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-003'
    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))
    def include(page):
        w = t.words[-1]
        w['pdf_pages'] = sorted(set(w['pdf_pages'] + [page]))
        w['printed_pages'] = [f'{p-8:03}' for p in w['pdf_pages']]

    a('cancel', '/ˈkænsl/', 'v. 取消；撤销；终止', 95,
      [('v.', '取消；撤销；终止')],
      [(0, 'All flights have been cancelled because of bad weather.', '因天气恶劣，所有航班均已取消。', 'cancelled', '例', 95),
       (0, 'No charge will be made if you cancel within 10 days.', '如果你在10天以内取消，不收取费用。', 'cancel', '例', 95)],
      '发音类似“看馊了”→馊了就赶紧退了，取消交易吧！→取消。')
    a('delete', '/dɪˈliːt/', 'v. 删除，删去', 95,
      [('v.', '删除，删去')],
      [(0, 'Your name has been deleted from the list.', '你的名字已从名单上删除。', 'deleted', '例', 95),
       (0, 'Once you have a first draft on paper, you can delete material that is unrelated to your thesis.', '一旦你在纸上有了初稿，你就可以删除与你的论文无关的材料。', 'delete', '真题', 95)])
    a('erase', '/ɪˈreɪz/', 'v. 清除，消除；消灭；擦掉，抹掉（笔迹等）', 95,
      [('v.', '清除，消除'), ('v.', '消灭'), ('v.', '擦掉，抹掉（笔迹等）')],
      [(0, 'She tried to erase the memory of that evening.', '她试图消除那天晚上的记忆。', 'erase', '例', 95),
       (0, 'Half of the participants were told the information would be erased.', '一半的参与者被告知信息将被删除。', 'erased', '真题', 95)])
    group = '32 console相关形近词'
    a('console', '/kənˈsəʊl/', 'v. 安慰；抚慰，慰藉', 95,
      [('v.', '安慰；抚慰，慰藉')],
      [(0, 'Nothing could console him when his wife died.', '他妻子去世后，什么事情也不能使他感到宽慰。', 'console', '例', 96),
       (0, 'Console yourself with the thought that you did your best.', '你可以安慰自己的是你已经尽了最大的努力。', 'Console', '例', 96)],
      '发音类似“可瘦了”→说我可瘦了，我知道你只是在“安慰”我。')
    a('counsel', '/ˈkaʊnsl/', 'n. 律师；法律顾问；忠告，劝告；v. 建议；劝告；提供专业咨询', 96,
      [('n.', '忠告，劝告'), ('v.', '建议；劝告'), ('n.', '律师；法律顾问'), ('v.', '提供专业咨询')],
      [(0, 'Listen to the counsel of your elders.', '要听从长辈的忠告。', 'counsel', '例', 96),
       (1, 'Most experts counsel caution in such cases.', '大多数专家建议在这样的情况下要谨慎从事。', 'counsel', '例', 96)],
      'coun（联想成can“能”）+ sel（联想成sell）→这些物品能不能卖，我得问问专业的“法律顾问”。')
    a('consult', '/kənˈsʌlt/', 'v. 咨询，请教；查阅；商议，商量', 96,
      [('v.', '咨询，请教'), ('v.', '查阅'), ('v.', '商议，商量')],
      [(0, 'If the pain continues, consult your doctor.', '如果疼痛持续不消退，要请医生诊治。', 'consult', '例', 96),
       (2, 'I need to consult with my colleagues on the proposals.', '我需要和我的同事商讨这些建议。', 'consult', '例', 96)],
      '他查阅（consult）了各种资料，但依然没有结果（result）。',
      [('consultant', 'n. 顾问', 96), ('consultancy', 'n. 咨询公司；专家咨询', 96)])
    a('insult', '/ɪnˈsʌlt/', 'n. 辱骂；侮辱；冒犯；v. 辱骂；冒犯', 96,
      [('n.', '辱骂；侮辱；冒犯'), ('v.', '辱骂；冒犯')],
      [(0, 'His comments were seen as an insult to her.', '他的评论被看成是对她的冒犯。', 'insult', '例', 96),
       (0, 'Emma Marris’ article is an insult and a disservice to the thousands of passionate people.', '艾玛·马里斯的文章是对成千上万热情人士的侮辱和伤害。', 'insult', '真题', 96)],
      '你可千万别冒犯（insult）他，不然没有什么好结果（result）的。')
    group = '33 pro-相关词汇'
    a('prompt', '/prɒmpt/', 'adj. 立即的，迅速的；及时的；v. 促使，导致，激起；鼓励；提示，提醒（某人说话）', 96,
      [('v.', '促使，导致，激起；鼓励'), ('adj.', '立即的，迅速的；及时的'), ('v.', '提示，提醒（某人说话）')],
      [(0, 'His speech prompted an angry outburst from a man in the crowd.', '他的讲话激起了人群中一男子的愤怒。', 'prompted', '例', 96),
       (0, 'And guilt, by prompting us to think more deeply about our goodness, can encourage humans to make up for errors and fix relationships.', '通过促使我们更深入地思考我们的善良，内疚感会鼓励人们去弥补错误、修复关系。', 'prompting', '真题', 96)],
      'pro（往前）+ m + pt（扑他）→立刻往前扑向他→立即的，迅速的。')
    a('promote', '/prəˈməʊt/', 'v. 促进，推动；提升；促销', 96,
      [('v.', '促销'), ('v.', '促进，推动'), ('v.', '提升')],
      [(0, 'The band has gone on tour to promote their new album.', '这个乐队已开始巡回宣传他们的新唱片。', 'promote', '例', 96),
       (1, 'The purpose of editing the News of the World was not to promote reader understanding.', '编辑《世界新闻报》的目的不是为了提升读者的认知。', 'promote', '真题', 96)],
      'pro（往前）+ mot（=move，移动）+ e→使你往前移动→促进，提升。')
    include(97)
    a('promotion', '/prəˈməʊʃn/', 'n. 提升，提拔，晋升；促销活动；广告宣传', 97,
      [('n.', '提升，提拔，晋升'), ('n.', '促销活动；广告宣传')],
      [(0, 'The company encourages internal promotion.', '公司鼓励内部晋升。', 'promotion', '例', 97),
       (1, 'Her job is mainly concerned with sales and promotion.', '她的工作主要是销售和广告宣传方面的。', 'promotion', '例', 97)])
    group = '34 -mot-/-mov-相关词汇'
    a('motion', '/ˈməʊʃn/', 'n. 运动；移动；动作；动议，提议；v. 做动作，示意', 97,
      [('n.', '运动；移动；动作'), ('n.', '动议，提议'), ('v.', '做动作，示意')],
      [(0, 'The swaying motion of the ship was making me feel seasick.', '船身摇摆不定，让我觉得恶心。', 'motion', '例', 97),
       (0, 'Do not open the door when the train is in motion.', '列车行驶时不要打开车门！', 'motion', '例', 97)],
      'mot（=move，移动）+ ion（名词后缀）→移动。', [('motionless', 'adj. 一动不动的，静止的', 97)])
    a('remote', '/rɪˈməʊt/', 'adj. 偏远的，偏僻的；遥远的，久远的；相差很大的；极不相同的', 97,
      [('adj.', '偏远的，偏僻的'), ('adj.', '相差很大的；极不相同的'), ('adj.', '遥远的，久远的')],
      [(0, 'The area is remote, mountainous, and roadless.', '这个地区偏远、多山、没有道路。', 'remote', '例', 97),
       (1, 'His theories are somewhat remote from reality.', '他的理论有点儿脱离现实。', 'remote', '例', 97)],
      're（向后，重复）+ mot（=move，移动）+ e→往后移动，那就越来越远了→遥远的。')
    a('motive', '/ˈməʊtɪv/', 'n. 动机，原因；目的', 97,
      [('n.', '动机，原因；目的')],
      [(0, 'She should examine her motives for marrying him.', '她应该认真考虑自己为什么要嫁给他。', 'motives', '例', 97),
       (0, 'But this effect is not a part of its original motive.', '但是这种影响并不是它最初动机的一部分。', 'motive', '真题', 97)],
      'mot（=move，移动）+ ive（名词后缀）→使你动起来的东西是什么？→动机。')
    a('motivate', '/ˈməʊtɪveɪt/', 'v. 激励，激发；成为……的动机，是……的原因', 97,
      [('v.', '激励，激发'), ('v.', '成为……的动机，是……的原因')],
      [(0, 'She’s very good at motivating her students.', '她非常擅长激励她的学生。', 'motivating', '例', 97)],
      'motiv（motive动机）+ ate（动词后缀）→使你有动机→刺激，激发。')
    material('motivate', 97, '真题',
      english='Not only are the tasks apparently infinite, the co-workers are much harder to motive.',
      translation='不仅任务无穷无尽，同事们也很难被激励起来。', status='quarantined',
      reason='原书此处拼作motive，不是motivate的词形；保留原文，待核对，不进入学习队列。')
    a('remove', '/rɪˈmuːv/', 'v. 移开，拿开；去掉；从……机构开除；脱去（衣服等）；摘下；去除，排除（污渍、不愉快的事物等）；使消失；免除，解除（职务等）', 97,
      [('v.', '移开，拿开；去掉'), ('v.', '从……机构开除；免除，解除（职务等）'),
       ('v.', '脱去（衣服等）；摘下'), ('v.', '去除，排除（污渍、不愉快的事物等）；使消失')],
      [(0, 'He removed his hand from her shoulder.', '他将手从她的肩膀上拿开。', 'removed', '例', 98),
       (0, 'The shortage is compounded by federal immigration raids, which remove some workers and drive others underground.', '联邦政府对移民的突击检查加剧了劳动力短缺，因为这些突击检查赶走了一些工人，另一些人则被迫转入地下工作。', 'remove', '真题', 98)],
      're（反复，再一次）+ move（移动）→再次移动，移走→移开。',
      [('removal', 'n. 移动；调动；消除；免职；搬迁', 98)])
    a('emotion', '/ɪˈməʊʃn/', 'n. 强烈的感情；激情；情感，情绪', 98,
      [('n.', '强烈的感情；激情；情感，情绪')],
      [(0, 'Fear is a normal human emotion.', '恐惧是正常的人类情感。', 'emotion', '例', 98),
       (0, 'Consequently, our feelings, thoughts and emotions have undergone a corresponding change.', '因此，我们的感觉、思想和情绪也发生了相应的变化。', 'emotions', '真题', 98)],
      'e（表示“出去”）+ mot（=move，移动；动）+ ion（名词后缀）→把你内心的运动表示出来，通过什么表示出来？→情感，情绪。',
      [('emotional', 'adj. 感情的，情感的，情绪的', 98)])
    material('emotional problems / stress', 98, '拓展', definition='情感问题／压力')
    group = '35 合理相关词汇'
    a('rational', '/ˈræʃənl/', 'adj. 合理的；理性的；明智的；理智的；清醒的', 98,
      [('adj.', '合理的'), ('adj.', '理性的；明智的；理智的；清醒的')],
      [(0, 'There is no rational explanation for his actions.', '对他的所作所为无法作出合理的解释。', 'rational', '例', 98)],
      'ratio（比率）+ n + al（形容词后缀）→一个人总是用比率和数字说话，他是不是很“理性的”？',
      [('rationally', 'adv. 合理地；理性地', 98), ('rationalization', 'n. 合理化', 98)])
    material('rationalization', 98, '真题',
      english='This seems a justification for neglect of those in need, and a rationalization of exploitation.',
      translation='这种说法似乎为忽视需要帮助的人找到了借口，使剥削合理化。')
    material('rationale', 98, '拓展', definition='n. 基本原理；根本原因')
    a('irrational', '/ɪˈræʃənl/', 'adj. 不合理的，失去理性的', 98,
      [('adj.', '不合理的，失去理性的')],
      [(0, 'Consumers are sometimes irrational.', '消费者有时是不理性的。', 'irrational', '例', 98)])
    a('reasonable', '/ˈriːznəbl/', 'adj. 合乎情理的，合理的；不错的', 98,
      [('adj.', '合乎情理的，合理的'), ('adj.', '不错的')],
      [(0, 'We have reasonable grounds for believing that you are responsible.', '我们有合理的理由相信你有责任。', 'reasonable', '例', 98),
       (0, 'They could take reasonable measures to ensure that phone data are not erased or altered while waiting for a warrant.', '在等待搜查令期间，他们可以采取合理措施，来确保手机中的数据不会被删除或修改。', 'reasonable', '真题', 98)],
      related=[('reasonably', 'adv. 合情合理地；明智地；通情达理地；尚可', 98)])
    a('advisable', '/ədˈvaɪzəbl/', 'adj. 可取的，明智的', 99,
      [('adj.', '可取的，明智的')],
      [(0, 'Early booking is advisable.', '提早预订是明智的。', 'advisable', '例', 99),
       (0, 'It is advisable to save money for your children.', '为你的孩子省点钱是很明智的。', 'advisable', '例', 99)])
    group = '36 显著的相关词汇'
    a('noticeable', '/ˈnəʊtɪsəbl/', 'adj. 显而易见的，显著的', 99,
      [('adj.', '显而易见的，显著的')],
      [(0, 'There is a noticeable difference between the two brands.', '这两个品牌有明显的区别。', 'noticeable', '例', 99),
       (0, 'Her scars are hardly noticeable now.', '她的伤疤现在几乎看不出来了。', 'noticeable', '例', 99)])
    material('notify', 99, '拓展', definition='v. 通报，通知')
    material('notify', 99, '例', english='Competition winners will be notified by post.', translation='将发信通知竞赛的优胜者。')
    a('noteworthy', '/ˈnəʊtwɜːði/', 'adj. 值得注意的，显著的；重要的', 99,
      [('adj.', '值得注意的，显著的'), ('adj.', '重要的')],
      [(0, 'It is noteworthy that only 15% of senior managers are women.', '值得注意的是，只有15%的高级管理人员是女性。', 'noteworthy', '例', 99),
       (0, 'The bridge is noteworthy for its sheer size.', '这座桥以宏伟闻名。', 'noteworthy', '例', 99)])
    t.pending('noteworthy', 1, '原译将noteworthy for意译为“以……闻名”，需复核与值得注意的词义对应；保留原文与原译。')
    group = '37 怀疑相关词汇'
    a('skeptical', '/ˈskeptɪkl/', 'adj. 怀疑的，持怀疑态度的', 99,
      [('adj.', '怀疑的，持怀疑态度的')],
      [(0, 'I am skeptical about his chances of winning.', '我怀疑他取胜的可能性。', 'skeptical', '例', 99),
       (0, 'Art became more skeptical of happiness.', '艺术对快乐愈发怀疑。', 'skeptical', '真题', 99)],
      'skep（察看）+ ti（联想成it“它”）+ c + al（形容词后缀）→察看它，为什么要察看呢？肯定是不放心，持怀疑态度→怀疑的。')
    a('dubious', '/ˈdjuːbiəs/', 'adj. 可疑的；不可靠的；不确定的；无把握的', 99,
      [('adj.', '可疑的；不可靠的'), ('adj.', '不确定的；无把握的')],
      [(0, 'The man who sold it to him was known to be of dubious character.', '那个卖东西给他的男人是出了名的不可靠。', 'dubious', '例', 99),
       (1, 'They consider the plan to be of dubious benefit to most families.', '他们认为这项计划对大多数家庭不一定有好处。', 'dubious', '例', 99)])
    a('doubtful', '/ˈdaʊtfl/', 'adj. 怀疑的；不大可能的', 99,
      [('adj.', '怀疑的；不大可能的')],
      [(0, 'It’s doubtful if this painting is a Picasso.', '这未必就是毕加索的画。', 'doubtful', '例', 99),
       (0, 'And whether the community’s work contributes much to an overall accumulation of knowledge is doubtful.', '而且社科界的工作是否对知识的整体积累作出了很大贡献，是令人怀疑的。', 'doubtful', '真题', 99)])
    group = '38 模糊相关词汇'
    a('ambiguous', '/æmˈbɪɡjuəs/', 'adj. 模棱两可的，含混不清的；多义的', 99,
      [('adj.', '模棱两可的，含混不清的'), ('adj.', '多义的')],
      [(0, 'Her account was deliberately ambiguous.', '她的陈述故意含混不清。', 'ambiguous', '例', 99),
       (0, 'But discovery frequently follows an ambiguous and complicated route.', '然而，发现通常遵循一条模糊而复杂的路径。', 'ambiguous', '真题', 100)],
      'amb（两）+ ig（驱使，做）+ uous（形容词后缀，……的）→两边都驱使做，都不知道做哪个好→模棱两可的，含混不清的。')
