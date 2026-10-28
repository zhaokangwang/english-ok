"""Visual transcription of fifth-unit headwords starting on PDF165–169."""
COMPLETE_THROUGH = 169
NEXT_WORD = 'extinguish'
NEXT_PAGE = 171

def append(t, associated):
    group = '29 变坏相关词汇'
    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(2000+len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-005'
    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))
    def include_page(page):
        w=t.words[-1]
        w['pdf_pages']=sorted(set(w['pdf_pages']+[page]))
        w['printed_pages']=[f'{p-8:03}' for p in w['pdf_pages']]

    a('poison', '/ˈpɔɪzn/', 'n. 毒药，毒物；v. 毒害，下毒', 165,
      [('n.', '毒药，毒物'), ('v.', '毒害，下毒')],
      [(0, 'These mushrooms contain a deadly poison.', '这些蘑菇含有剧毒。', 'poison', '例', 165),
       (1, 'Large sections of the river have been poisoned by toxic waste from factories.', '工厂的有毒废弃物污染了大段的河流。', 'poisoned', '例', 165)],
      '因为给人下毒（poison），他被判入狱（prison）。',
      [('poisonous', 'adj. 有毒的', 165)])
    material('poisonous', 165, '例', english='This gas is highly poisonous.', translation='这种气体有剧毒。')
    group = '30 吸收相关词汇'
    a('absorb', '/əbˈzɔːb/', 'v. 使全神贯注；吸收；使并入', 165,
      [('v.', '使全神贯注'), ('v.', '吸收'), ('v.', '使并入')],
      [(0, 'He was totally absorbed in his work.', '他全神贯注于他的工作。', 'absorbed', '例', 165),
       (1, 'I never feel overwhelmed with the amount of information my brain absorbs.', '我从来不会因为大脑吸收的信息量庞大而感到难以承受。', 'absorbs', '真题', 165)])
    a('assimilate', '/əˈsɪməleɪt/', 'v. （使）同化；吸收', 165,
      [('v.', '（使）同化'), ('v.', '吸收')],
      [(1, 'Some people can only assimilate change gradually.', '有些人只能逐渐同化变化。', 'assimilate', '例', 165),
       (0, 'We are obliged to them because some of these languages have since vanished, as the peoples who spoke them died out or became assimilated and lost their native languages.', '我们得感激他们，因为从此以后这些语言中有一些语言消失了，这是由于讲这些语言的部族要么灭绝了，要么被同化而丧失了自己的本族语言。', 'assimilated', '真题', 165)],
      'as（表示“加强”）+ simil（相似）+ ate（动词后缀）→使相似→（使）同化。',
      [('assimilation', 'n. 吸收；同化现象', 165)])
    t.pending('assimilate', 0, '原译“同化变化”表意存疑，保留原句原译待核对，暂不作为吸收义学习例句。')
    group = '31 ab-表示否定相关词汇'
    a('abandon', '/əˈbændən/', 'v. 遗弃，抛弃；放弃', 165,
      [('v.', '遗弃，抛弃'), ('v.', '放弃')],
      [(0, 'The baby had been abandoned by its mother.', '这个婴儿被母亲遗弃了。', 'abandoned', '例', 165),
       (1, 'The extended family have been abandoned in favor of isolated, two generation households.', '大家庭已经被抛弃，取而代之的是单门独户的两代人家庭。', 'abandoned', '真题', 165)])
    material('abandon oneself to doing sth.',165,'拓展',definition='沉溺于做某事')
    material('abandon oneself to',165,'例',english='Please don’t abandon yourself to those games.',translation='请不要沉溺于那些游戏。')
    a('abolish', '/əˈbɒlɪʃ/', 'v. 废除，废止（法律、制度、习俗等）', 165,
      [('v.', '废除，废止（法律、制度、习俗等）')],
      [(0, 'This tax should be abolished.', '这种税应该取消。', 'abolished', '例', 166),
       (0, 'This law abolished special educational requirements for federal jurors and required them to be selected at random from a cross section of the entire community.', '该法案废除了对联邦陪审员的特殊教育要求，并要求联邦陪审员要在社会各阶层的民众中随机挑选。', 'abolished', '真题', 166)],
      'ab（表示“否定”）+ ol + ish（表示“使……”）→使这个东西不要了→废除。')
    a('abuse', 'n. /əˈbjuːs/; v. /əˈbjuːz/', 'n. 滥用；虐待；v. 滥用；虐待', 166,
      [('n.', '滥用'), ('n.', '虐待'), ('v.', '滥用'), ('v.', '虐待')],
      [(0, 'The legal system is open to abuse.', '这种法律制度容易被钻空子。', 'abuse', '例', 166),
       (0, 'He was arrested on charges of corruption and abuse of power.', '他因被控贪污腐化和滥用职权而遭逮捕。', 'abuse', '例', 166)],
      'ab（表示“否定”）+ use（使用）→不好好使用→滥用。')
    material('alcohol/drug abuse',166,'拓展',definition='酗酒／吸毒')
    material('child abuse',166,'拓展',definition='虐待儿童')
    group = '32 集中相关词汇'
    a('focus', '/ˈfəʊkəs/', 'n. 焦点，中心点，关注；v. 集中（注意力、精力等）', 166,
      [('v.', '集中（注意力、精力等）'), ('n.', '焦点，中心点，关注')],
      [(0, 'The discussion focused on three main issues.', '讨论集中在三个主要问题上。', 'focused', '例', 166),
       (1, 'When the government talks about infrastructure contributing to the economy, the focus is usually on roads, railways, broadband and energy.', '当政府谈论基础设施对经济的贡献时，重点通常是公路、铁路、宽带和能源。', 'focus', '真题', 166)])
    a('concentrate', '/ˈkɒnsntreɪt/', 'n. 浓缩物；v. 集中（注意力）；使……集中', 166,
      [('v.', '集中（注意力）；使……集中'), ('n.', '浓缩物')],
      [(0, 'She tried to concentrate on reading her book but couldn’t.', '她试图集中精力看书，但没能做到。', 'concentrate', '例', 166),
       (0, 'When we travel down a well-known route, because we don’t have to concentrate much, time seems to flow more quickly.', '当我们沿着熟悉的路线旅行时，因为我们不必太集中精力，时间似乎过得更快。', 'concentrate', '真题', 166)],
      'con（所有）+ centr（联想成centre“中心”）+ ate（动词后缀）→左右中心都放到一个地方→集中。')
    a('indulge', '/ɪnˈdʌldʒ/', 'v. 沉迷，沉溺（于）……；满足；放纵', 166,
      [('v.', '沉迷，沉溺（于）……'), ('v.', '满足；放纵')],
      [(0, 'They went into town to indulge in some serious shopping.', '他们进城去大肆购物。', 'indulge', '例', 166),
       (1, 'She did not believe in indulging the children with presents.', '她认为不能纵容孩子们要什么就给什么。', 'indulging', '例', 166)],
      'in（表示“加强”）+ dulge（联想成“妲己”）→纣王沉迷于妲己的美色→沉迷。')
    group = '33 -dict-相关词汇'
    a('addict', '/ˈædɪkt/', 'n. 吸毒成瘾的人，瘾君子', 166,
      [('n.', '吸毒成瘾的人，瘾君子')],
      [(0, 'Many young boys become computer addicts.', '许多男孩子小小年纪就迷上了电脑。', 'addicts', '例', 166)],
      'ad（表示“加强”）+ dict（说）→一再地说一个人、一件事，说明对他或它已经“入迷”了→瘾君子。',
      [('addicted', 'adj. 上瘾的；有瘾的', 167)])
    include_page(167)
    t.pending('addict', 0, 'computer addicts是对电脑上瘾的人，原书主释义仅明确吸毒成瘾者；保留原文原译，待补充匹配词义。')
    a('predict', '/prɪˈdɪkt/', 'v. 预言，预告', 167,
      [('v.', '预言，预告')],
      [(0, 'Nobody could predict the outcome.', '谁也无法预料结果。', 'predict', '例', 167),
       (0, 'Many people predicted that Mary would get married with a rich man.', '很多人预言玛丽会嫁给一个有钱人。', 'predicted', '例', 167)],
      'pre（预先）+ dict（说）→预先说→预言。',
      [('prediction', 'n. 预言，预告', 167)])
    t.pending('predict', 1, '原书get married with搭配疑点，保留原文原译，待核对后再用于学习。')
    a('abdicate', '/ˈæbdɪkeɪt/', 'v. 放弃职责；退位', 167,
      [('v.', '退位'), ('v.', '放弃职责')],
      [(0, 'She was forced to abdicate the throne of Spain.', '她被迫让出西班牙的王位。', 'abdicate', '例', 167)],
      'ab（表示“否定”）+ dic（说；命令）+ ate（动词后缀）→不再命令→退位。')
    a('dictate', 'v. /dɪkˈteɪt/; n. /ˈdɪkteɪt/', 'v. 口述；强行规定，指使；n. 命令；规定', 167,
      [('v.', '强行规定，指使'), ('v.', '口述'), ('n.', '命令；规定')],
      [(0, 'What right do they have to dictate how we live our lives?', '他们有什么权利强行规定我们怎样生活？', 'dictate', '例', 167),
       (0, 'Humans are born with an innate language-acquisition capacity that dictates a universal grammar.', '人类天生具有一种支配通用语法的先天性的语言习得能力。', 'dictates', '真题', 167)],
      'dict（说；命令）+ ate（动词后缀）→命令。',
      [('dictation', 'n. 口述，听写', 167), ('dictator', 'n. 发号施令者；独裁者', 167)])
    t.pending('dictate', 1, '本句dictates指先天能力支配、决定语法，源释义未明确列决定义，暂不直接训练强行规定义。')
    a('contradict', '/ˌkɒntrəˈdɪkt/', 'v. 反驳，驳斥；相矛盾，相抵触', 167,
      [('v.', '相矛盾，相抵触'), ('v.', '反驳，驳斥')],
      [(0, 'You’ve just contradicted yourself.', '你恰好与你刚才说的自相矛盾。', 'contradicted', '例', 167)],
      'contra（反对，相反）+ dict（说）→反着说→反驳。',
      [('contradiction', 'n. 矛盾；反驳；不一致', 167), ('contradictory', 'adj. 相互矛盾的，对立的', 167)])
    material('contradiction',167,'例',english='His public speeches are in direct contradiction to his personal lifestyle.',translation='他的公开言论与他本人的生活方式恰恰相反。')
    material('contradictory',167,'例',english='The argument is internally contradictory.',translation='论据本身自相矛盾。')
    group = '34 真假相关语境词汇'
    a('fake', '/feɪk/', 'n. 假货；赝品；adj. 假的；v. 伪造', 167,
      [('v.', '伪造'), ('adj.', '假的'), ('n.', '假货；赝品')],
      [(0, 'She faked her mother’s signature on the document.', '她伪造了母亲在文件上的签名。', 'faked', '例', 167),
       (1, 'Undercover investigators were able to sneak weapons—both fake and real—past airport security nearly every time they tried.', '卧底调查员能够偷偷携带武器（不管真假）成功通过机场安检，几乎屡试不爽。', 'fake', '真题', 167)])
    a('genuine', '/ˈdʒenjuɪn/', 'adj. 真的；真诚的', 167,
      [('adj.', '真的'), ('adj.', '真诚的')],
      [(0, 'Only genuine refugees will be granted asylum.', '只有真正的难民才会得到庇护。', 'genuine', '例', 168),
       (0, 'This suggests that the rats perceived the social robot as a genuine social being.', '这表明老鼠将社交机器鼠看作真正的社交生物。', 'genuine', '真题', 168)],
      '发音类似“姐牛”→姐姐很牛，这是“真的”→真的。')
    a('authentic', '/ɔːˈθentɪk/', 'adj. 真正的，真迹的，真实的', 168,
      [('adj.', '真正的，真迹的，真实的')],
      [(0, 'I don’t know if the painting is authentic.', '我不知道这幅画是不是真迹。', 'authentic', '例', 168),
       (0, 'The documents seem authentic enough.', '这些文件似乎足够可靠。', 'authentic', '例', 168)],
      'authen（联想成author“作者”）+ tic（联想成“挑出”）→我能挑出哪个是作者的“真迹”→真迹的。')
    a('authority', '/ɔːˈθɒrəti/', 'n. 权威，权力；官方，当局', 168,
      [('n.', '权力'), ('n.', '权威'), ('n.', '官方，当局')],
      [(0, 'The government has the authority to regulate the economy.', '政府有权调节经济。', 'authority', '例', 168),
       (1, 'And one leading authority says that these intensely powerful mental events can be not only harnessed but actually brought under conscious control.', '一位重要的权威人士说，这些异常重要的精神活动不仅可以被控制，而且在实际上可以被我们有意识地控制。', 'authority', '真题', 168)],
      related=[('authoritative', 'adj. 权威性的；命令式的；专断的', 168)])
    t.pending('authority', 1, '原译将intensely powerful处理为异常重要，语义存疑；原句原译保留待核，不进入学习。')
    material('authoritative',168,'例',english='She began to resent his authoritative manner.',translation='她开始讨厌他的权威态度。')
    group = '35 天才相关语境词汇'
    a('elite', '/eɪˈliːt/', 'n. 社会精英；上层集团；adj. 精英的，精锐的；出类拔萃的', 168,
      [('n.', '社会精英；上层集团'), ('adj.', '精英的，精锐的；出类拔萃的')],
      [(0, 'These people form an elite who have the power to make decisions.', '这些人构成了一个有决定权的精英集团。', 'elite', '例', 168)])
    a('genius', '/ˈdʒiːniəs/', 'n. 天才，天才人物；天赋', 168,
      [('n.', '天才，天才人物'), ('n.', '天赋')],
      [(0, 'He is a genius.', '他是个天才。', 'genius', '例', 168),
       (1, 'She was at the peak of her creative genius.', '她的创作力处于巅峰状态。', 'genius', '例', 168)],
      'ge（联想成“哥哥”）+ niu（牛）+ s→哥哥很牛，他在我们眼里就是个“天才”→天才。')
    a('ingenious', '/ɪnˈdʒiːniəs/', 'adj. 巧妙的；心灵手巧的；机敏的；善于创造发明的；精巧的', 168,
      [('adj.', '巧妙的；精巧的'), ('adj.', '心灵手巧的；机敏的；善于创造发明的')],
      [(1, 'She’s very ingenious when it comes to finding excuses.', '她很善于找借口。', 'ingenious', '例', 168),
       (0, 'His plots are always very ingenious.', '他的情节总是很巧妙。', 'ingenious', '例', 168)],
      '天才（genius）一般也是机灵的（ingenious）。')
    a('nuisance', '/ˈnjuːsns/', 'n. 讨厌的人（或东西）；麻烦事', 168,
      [('n.', '讨厌的人（或东西）'), ('n.', '麻烦事')],
      [(0, 'I don’t want to be a nuisance so tell me if you want to be alone.', '我不想讨人嫌，你要是想一个人待着就说一声。', 'nuisance', '例', 168),
       (0, 'I hope you’re not making a nuisance of yourself.', '我希望你没有讨人嫌。', 'nuisance', '例', 168)])
    group = '36 g哥哥相关语境词汇'
    a('forge', '/fɔːdʒ/', 'v. 伪造；锻造；艰苦干成；努力加强', 169,
      [('v.', '伪造'), ('v.', '努力加强'), ('v.', '锻造'), ('v.', '艰苦干成')],
      [(0, 'New digital techniques can spot paintings that have been forged.', '新的数字技术可以识别伪造的画作。', 'forged', '例', 169),
       (1, 'In particular, they called for forging closer collaborations with western state governments.', '特别是，他们呼吁与西部各州政府建立更密切的合作。', 'forging', '真题', 169)],
      'for（为了）+ ge（哥哥）→为了“锻造”一把好刀，哥哥必须“努力加强”自己的技艺。')
    t.words[-1]['notes'].append('第三释义首字扫描字形较模糊，暂按“艰苦干成”转录，该义无学习例句，待复核。')
    a('mortgage', '/ˈmɔːɡɪdʒ/', 'n. 按揭；按揭贷款；v. 抵押', 169,
      [('n.', '按揭；按揭贷款'), ('v.', '抵押')],
      [(0, 'He raised the money by taking out a second mortgage on his house.', '他通过对自己的房屋办理二次抵押筹集了这笔钱。', 'mortgage', '例', 169),
       (1, 'He had to mortgage his house to pay his legal costs.', '他不得不把房子抵押出去来付诉讼费。', 'mortgage', '例', 169)],
      '为了获得贷款，他把自己最爱的摩托车（motorbike）抵押（mortgage）给哥哥了。')
    a('vulgar', '/ˈvʌlɡə(r)/', 'adj. 粗俗的，庸俗的，不雅的', 169,
      [('adj.', '粗俗的，庸俗的，不雅的')],
      [(0, 'She gave a rather vulgar laugh.', '她发出一声相当粗俗的笑声。', 'vulgar', '例', 169),
       (0, 'What has happened is that people cannot confess fully to their dreams, lest they be thought pushing, acquisitive and vulgar.', '现在的情况是，人们不能完全承认自己的梦想，唯恐别人认为自己咄咄逼人、贪婪和庸俗。', 'vulgar', '真题', 169)],
      '这个乞丐（beggar）的行为有些粗俗（vulgar）。')
    a('gesture', '/ˈdʒestʃə(r)/', 'n. 姿势，手势；姿态，表示', 169,
      [('n.', '姿态，表示'), ('n.', '姿势，手势')],
      [(0, 'The president’s speech was seen as a conciliatory gesture towards former enemies.', '总统的讲话被看作是与昔日的敌人修好的表示。', 'gesture', '例', 169),
       (1, 'Ambady suspected that deliberation focused them on vivid misleading cues, such as certain gestures or utterances.', '安巴迪怀疑，深思使参与者将精力集中于那些生动但具有误导性的信号，比如特定的手势或说话方式。', 'gestures', '真题', 169)])
    a('cognitive', '/ˈkɒɡnətɪv/', 'adj. 认知的，感知的，认识的', 169,
      [('adj.', '认知的，感知的，认识的')],
      [(0, 'This is both a cognitive and an emotional process.', '这既是一个认知过程，也是一个情感过程。', 'cognitive', '例', 169),
       (0, 'To filter out what is unique from what is shared might enable us to understand how complex cultural behavior arose and what guides it in evolutionary or cognitive terms.', '从共有特征中滤出独有特征使我们得以理解复杂的文化行为是如何产生的，并从进化或认知角度理解什么引导了它的走向。', 'cognitive', '真题', 169)],
      'cogn（知道）+ it + ive（形容词后缀）→能够知道和认识的→认知的。',
      [('cognition', 'n. 认识；知识；感知', 169)])
