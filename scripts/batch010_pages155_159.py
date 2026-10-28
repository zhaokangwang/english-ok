"""Visual transcription of tenth-batch headwords beginning on PDF155–159."""
COMPLETE_THROUGH = 159
NEXT_WORD = 'strike'
NEXT_PAGE = 160

def append(t, associated):
    group = '14 upset相关词汇'
    def a(spelling, ipa, definition, page, senses, examples, mnemonic='', related=()):
        t.add(2000+len(t.words), spelling, ipa, definition, page, group, senses, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-005'
    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))
    def include(page):
        w = t.words[-1]
        w['pdf_pages'] = sorted(set(w['pdf_pages']+[page]))
        w['printed_pages'] = [f'{p-8:03}' for p in w['pdf_pages']]

    a('upset', '/ˌʌpˈset/', 'adj. 难过；不高兴；失望；沮丧；v. 使心烦意乱，使生气', 155,
      [('adj.', '难过；不高兴'), ('adj.', '失望；沮丧'), ('v.', '使心烦意乱，使生气')],
      [(0, 'There’s no point getting upset about it.', '犯不着为此事难过。', 'upset', '例', 155),
       (2, 'If it is trying to upset Google, it has chosen an indirect method.', '如果它是在试图惹恼谷歌，那么它选择了一种间接的方法。', 'upset', '真题', 155)],
      '发音类似“俺不赛”→俺不想参加比赛了，因为俺很郁闷，“烦”死了→使心烦。')
    group = '15 住相关词汇'
    a('settle', '/ˈsetl/', 'v. 定居；解决', 155,
      [('v.', '解决'), ('v.', '定居')],
      [(0, 'It’s time you settled your differences with your father.', '是你该解决与你父亲之间的分歧的时候了。', 'settled', '例', 155),
       (1, 'She settled in Vienna after her father’s death.', '在她的父亲死后，她就在维也纳定居了。', 'settled', '例', 155)],
      'set（往下）+ tle→放下来，把自己放下来，不再漂泊，就是“定居”；把一个问题放下来了，那就是把这个问题“解决”了→定居；解决。',
      [('settlement', 'n. 解决；处理；协议', 155)])
    material('settlement', 155, '例', english='The management and unions have reached a settlement over new working conditions.', translation='资方和工会已就新的工作条件达成协议。')
    a('dwell', '/dwel/', 'v. 居住；栖身', 155,
      [('v.', '居住；栖身')],
      [(0, 'He dwelt in a ruined cottage on the hillside.', '他住在山坡上一座破败的农舍里。', 'dwelt', '例', 155),
       (0, 'For ten years she dwelled among the nomads of North America.', '她在北美游牧民中生活了十年。', 'dwelled', '例', 155)],
      '他想居住（dwell）在老家，好好地（well）度过晚年。',
      [('dweller', 'n. 居民，居住者', 155)])
    material('dweller', 155, '真题', english='It was specifically to provide city dwellers with spaces for leisure.', translation='它专门为城市居民提供了一些休闲之地。')
    a('dwelling', '/ˈdwelɪŋ/', 'n. 住宅，住所', 155,
      [('n.', '住宅，住所')],
      [(0, 'The development will consist of 66 dwellings and a number of offices.', '新建楼区将由66套住房和一些办公室组成。', 'dwellings', '例', 155),
       (0, 'In one case, many researchers have located hundreds of small rural villages and individual dwellings by using aerial photographs and by making surveys on foot.', '在一个案例中，许多研究人员通过使用航空照片和徒步考察，已经确定了数百个小村庄和个体住宅的位置。', 'dwellings', '真题', 155)])
    group = '16 处理相关词汇'
    a('handle', '/ˈhændl/', 'v. 处理，应付；n. 把手；拉手', 155,
      [('v.', '处理，应付'), ('n.', '把手；拉手')],
      [(0, 'A new man was appointed to handle the crisis.', '新指派了一个人来处理这场危机。', 'handle', '例', 156),
       (0, 'When the skills mismatch is in the broader economy, though, the focus usually turns to government to handle.', '不过，当技能不匹配问题出现在更宏观的经济领域时，重点通常转向政府来处理。', 'handle', '真题', 156)],
      '发音类似“憨豆”→是不是憨豆先生在“处理”问题时总会出现问题？→处理。')
    a('manage', '/ˈmænɪdʒ/', 'v. 管理，负责；完成（困难的事）；勉力完成', 156,
      [('v.', '管理，负责'), ('v.', '完成（困难的事）；勉力完成')],
      [(0, 'We need people who are good at managing.', '我们需要擅长管理的人。', 'managing', '例', 156),
       (1, 'They can manage to have a job in one place and a family in another.', '他们可以在一个地方谋职，在另一个地方安家。', 'manage', '真题', 156)],
      related=[('management', 'n. 经营，管理', 156), ('manager', 'n. 经营者，经理', 156), ('manageable', 'adj. 可操纵的；可处理的', 156)])
    a('tackle', '/ˈtækl/', 'v. 处理，应付；解决', 156,
      [('v.', '处理，应付；解决')],
      [(0, 'The problem is being tackled with a range of measures.', '这个问题正通过一系列措施予以处理。', 'tackled', '例', 156),
       (0, 'The government is determined to tackle inflation.', '政府决心解决通货膨胀问题。', 'tackle', '例', 156)],
      '发音类似“太抠”→对于销售而言，“应付”太抠的人是很困难的→应付。')
    a('cope', '/kəʊp/', 'v. 对付，处理', 156,
      [('v.', '对付，处理')],
      [(0, 'They are able to cope with the global climate change.', '他们能够应对全球气候变化。', 'cope', '例', 156),
       (0, 'She is unable to cope with her increasing workload.', '她无法应付日益加重的工作负担。', 'cope', '例', 156)],
      '谐音“靠谱”→你处理这些事情很靠谱→处理。')
    a('solve', '/sɒlv/', 'v. 解决；解答', 156,
      [('v.', '解决；解答')],
      [(0, 'Attempts are being made to solve the problem of waste disposal.', '正在想办法解决废物处理的问题。', 'solve', '例', 156)],
      related=[('solution', 'n. 解答，解决办法', 156), ('unsolved', 'adj. 未破解的，未解决的', 156)])
    material('solution', 156, '例', english='There’s no simple solution to this problem.', translation='这个问题没有简单的解决办法。')
    a('resolve', '/rɪˈzɒlv/', 'v. 解决；决定；决心', 156,
      [('v.', '解决'), ('v.', '决定；决心')],
      [(0, 'Attempts are being made to resolve the problem of security in schools.', '正在努力解决学校的安全问题。', 'resolve', '例', 156),
       (1, 'He resolved not to tell her the truth.', '他决定不告诉她真相。', 'resolved', '例', 156)],
      're（重复）+ solve（解决）→一件事情开始没有解决，后来“下决心”再次“解决”→解决；下决心。',
      [('resolved', 'adj. 下定决心', 156), ('resolution', 'n. 决心；解决', 156)])
    material('resolution', 156, '例', english='I made a New Year resolution to give up smoking.', translation='我决心在新的一年把烟戒掉。')
    a('dissolve', '/dɪˈzɒlv/', 'v. 溶解；解除；消除', 157,
      [('v.', '溶解'), ('v.', '解除'), ('v.', '消除')],
      [(0, 'Heat gently until the sugar dissolves.', '慢慢加热直到糖溶解为止。', 'dissolves', '例', 157),
       (1, 'Their marriage was dissolved in 1999.', '他们于1999年解除了婚姻关系。', 'dissolved', '例', 157)],
      'dis（不能）+ solve（解决）→他们遇到不能解决的矛盾时，有可能会选择“解除、解散”合作关系→解除。')
    group = '17 范围相关词汇'
    a('scope', '/skəʊp/', 'n. 范围；机会', 157,
      [('n.', '机会'), ('n.', '范围')],
      [(0, 'There’s still plenty of scope for improvement.', '还有很大的改进余地。', 'scope', '例', 157)],
      '很多时候我们只能解决（cope）我们能力范围（scope）内的问题。')
    a('realm', '/relm/', 'n. 领域；场所；王国', 157,
      [('n.', '王国'), ('n.', '领域'), ('n.', '场所')],
      [(0, 'They fought to defend the realm.', '他们为保卫王国而战。', 'realm', '例', 157),
       (1, 'But snap decisions in reaction to rapid stimuli aren’t exclusive to the interpersonal realm.', '但是，对快速刺激作出快速反应的决定并不是人际关系领域所独有的。', 'realm', '真题', 157)],
      'real（真的）+ m（联想成man“男人”）→有些人认为，真正的男人需要在某个“领域”作出成绩→领域。')
    a('span', '/spæn/', 'n. 跨度，范围；持续时间；宽度；v. 持续；贯穿', 157,
      [('v.', '持续；贯穿'), ('n.', '跨度，范围'), ('n.', '持续时间'), ('n.', '宽度')],
      [(0, 'His acting career spanned 55 years.', '他的演艺生涯长达55年。', 'spanned', '例', 157),
       (1, 'Managers have a wide span of control.', '经理的职权范围很大。', 'span', '例', 157)],
      '美女（s）盼（pan）望着在一段时间内自己的人生能有一个新的“跨度”→跨度。')
    group = '18 典型、等级相关词汇'
    a('typical', '/ˈtɪpɪkl/', 'adj. 典型的，有代表性的；一贯的，平常的', 157,
      [('adj.', '典型的，有代表性的'), ('adj.', '一贯的，平常的')],
      [(0, 'This meal is typical of local cookery.', '这是有当地风味的饭菜。', 'typical', '例', 157),
       (1, 'The weather at the moment is not typical for July.', '现在的天气并不是七月份常有的。', 'typical', '例', 157)])
    a('classic', '/ˈklæsɪk/', 'adj. 最优秀的；第一流的；有代表性的，典型的；n. 名著，经典作品', 157,
      [('adj.', '最优秀的；第一流的'), ('adj.', '有代表性的，典型的'), ('n.', '名著，经典作品')],
      [(0, 'I grew up listening to classic rock.', '我是听着古典摇滚长大的。', 'classic', '例', 157),
       (1, 'This was a classic case of what not to do.', '这是一个不该做什么的典型例子。', 'classic', '例', 157)],
      related=[('classical', 'adj. 古典的，经典的', 157)])
    t.pending('classic', 0, 'classic rock原译古典摇滚与原书最优秀、第一流等释义对应存疑，保留原文原译，暂待复核。')
    material('classical', 157, '例', english='They gained some knowledge of classical art and architecture.', translation='他们获得了一些古典艺术和建筑方面的知识。')
    a('upgrade', 'v. /ˌʌpˈɡreɪd/; n. /ˈʌpɡreɪd/', 'v. 使升级；提高；n. 升级', 157,
      [('v.', '使升级；提高'), ('n.', '升级')],
      [(0, 'We are constantly upgrading our software to meet customers’ needs.', '我们不断升级软件，以满足用户的需要。', 'upgrading', '例', 158),
       (1, 'As an executive coach, I’ve seen image upgrades be particularly helpful during transitions.', '作为一名管理人员培训师，我发现在过渡时期提升形象特别有帮助。', 'upgrades', '真题', 158)],
      'up（往上）+ grade（等级；年级）→使你的等级往上升→升级。')
    group = '19 m妈妈词汇'
    a('image', '/ˈɪmɪdʒ/', 'n. 图像，影像；形象，印象；声音', 158,
      [('n.', '图像，影像'), ('n.', '形象，印象'), ('n.', '声音')],
      [(0, 'The visual image is steadily replacing the written word.', '视觉图像正在逐渐取代文字。', 'image', '例', 158),
       (1, 'That’s a far different image from the cherry-tree-chopping George most people remember from their history books.', '那与大多数人从历史书上看到的砍樱桃树的乔治的形象截然不同。', 'image', '真题', 158)],
      'i（我）+ m（妈妈）+ age（年纪）→我妈妈上了年纪，仍然在灯光下缝补衣服，这种“形象”让人永远忘不了→形象。')
    material('imagine', 158, '拓展', definition='v. 想象，设想')
    a('calm', '/kɑːm/', 'adj. 镇静的，沉着的；风平浪静的；v. 使平静；使镇静', 158,
      [('adj.', '镇静的，沉着的'), ('adj.', '风平浪静的'), ('v.', '使平静；使镇静')],
      [(0, 'It is important to keep calm in an emergency.', '情况紧急的时候，保持镇静是重要的。', 'calm', '例', 158),
       (0, 'They were impressed by her calm demeanour.', '她平静的举止给他们留下了深刻印象。', 'calm', '例', 158)],
      '你难过的时候，给妈妈（m）打电话（call），妈妈安慰你，你心情好多了，就“平静”了。')
    group = '20 道德相关词汇'
    a('moral', '/ˈmɒrəl/', 'n. 道德；adj. 道德（上）的', 158,
      [('adj.', '道德（上）的'), ('n.', '道德')],
      [(0, 'In some states, for example, jury duty was limited to persons of supposedly superior intelligence, education, and moral character.', '例如，在有些州，陪审团职责仅限于由那些所谓的智商高、学历和道德品格高人一等的人来承担。', 'moral', '真题', 158)],
      'm（联想成“妈妈”）+ oral（口头的）→妈妈口头上教育我们要做“有道德的”人→道德（上）的。',
      [('morality', 'n. 道德；道德准则', 158)])
    a('mortal', '/ˈmɔːtl/', 'adj. 终将死亡的；致命的；n. 人；普通人', 158,
      [('adj.', '终将死亡的'), ('adj.', '致命的'), ('n.', '人；普通人')],
      [(0, 'We are all mortal.', '我们都总有一死。', 'mortal', '例', 158)],
      '即便是道德高尚（moral）的人，也终有一死（mortal）。',
      [('mortality', 'n. 死亡数量，死亡率', 158), ('immortal', 'adj. 长生的，不朽的', 158)])
    material('mortality', 158, '例', english='Mortality from lung cancer is still increasing.', translation='死于肺癌的人数仍在上升。')
    a('ethic', '/ˈeθɪk/', 'n. 伦理标准，道德准则', 158,
      [('n.', '伦理标准，道德准则')],
      [(0, 'He began to question the ethics of his position.', '他开始对他的立场是否符合道德准则提出疑问。', 'ethics', '例', 159)])
    group = '21 re-相关词汇'
    a('recommend', '/ˌrekəˈmend/', 'v. 推荐，介绍；建议', 159,
      [('v.', '推荐，介绍'), ('v.', '建议')],
      [(0, 'Can you recommend a good hotel?', '你能推荐一家好的旅馆吗？', 'recommend', '例', 159),
       (0, 'All the experts we spoke with highly recommend walking.', '我们采访过的所有专家都强烈推荐步行。', 'recommend', '真题', 159)],
      '发音类似“来叩门的”→这个时候来叩门的人可能是来提“建议”的→建议。')
    a('receipt', '/rɪˈsiːt/', 'n. 收据；收入', 159,
      [('n.', '收据'), ('n.', '收入')],
      [(0, 'We will email the receipt to you.', '我们会把收据用电子邮件发给你。', 'receipt', '例', 159),
       (0, 'The machine issues a paper receipt on request.', '如果需要，该机器可提供收据小票。', 'receipt', '例', 159)],
      'receive意为“接收”，人们买完东西后接收到的票据为“收据”。')
    a('recipe', '/ˈresəpi/', 'n. 烹饪法，食谱；秘诀', 159,
      [('n.', '烹饪法，食谱'), ('n.', '秘诀')],
      [(0, 'You need to follow the recipe carefully.', '你需要仔细遵循食谱。', 'recipe', '例', 159),
       (0, 'Each month we feature easy low-fat recipes.', '我们每个月都会推出一些特色的简易低脂食谱。', 'recipes', '例', 159)],
      're（表示“重复”）+ cipe（联想成“食谱”）→他一再地提到“食谱”→食谱。')
    a('reciprocal', '/rɪˈsɪprəkl/', 'adj. 互惠的，相应的', 159,
      [('adj.', '互惠的'), ('adj.', '相应的')],
      [(0, 'The two colleges have a reciprocal arrangement whereby students from one college can attend classes at the other.', '这两所学院有一项互惠协定，允许学生跨院选课。', 'reciprocal', '例', 159),
       (0, 'Rats have been shown to engage in multiple forms of reciprocal help and cooperation.', '已有研究表明，老鼠会进行多种形式的互助及合作。', 'reciprocal', '真题', 159)])
    group = '22 credible相关词汇'
    a('credible', '/ˈkredəbl/', 'adj. 可信的；可接受的', 159,
      [('adj.', '可信的'), ('adj.', '可接受的')],
      [(0, 'It seemed to be a credible account of events.', '这似乎是对事件的可信描述。', 'credible', '例', 159),
       (0, 'He turned up credible evidence that music has positive effects on intelligence.', '他发现了音乐对智力有积极影响的可信的证据。', 'credible', '例', 159)],
      'credit card是信用卡，credit是“信用，相信”的意思，credible就是“可信的”。')
    a('incredible', '/ɪnˈkredəbl/', 'adj. 极好的，难以置信的', 159,
      [('adj.', '极好的'), ('adj.', '难以置信的')],
      [(1, 'It seemed incredible that she had been there a week already.', '真让人难以置信，她已经在那里待了一个星期。', 'incredible', '例', 159),
       (0, 'Or, we can look at failure as an incredible learning experience.', '或者，我们可以把失败看作一次不可思议的学习经历。', 'incredible', '真题', 159)],
      related=[('incredibly', 'adv. 极其，极端地；令人难以置信', 159)])
    t.pending('incredible', 1, '本句incredible learning experience的褒义极好与原译不可思议的对应需上下文确认，暂不直接训练极好义。')
    include(160)
    material('incredibly', 160, '真题', english='In fact, creative problem-solving skills are incredibly useful in daily life.', translation='事实上，创造性解决问题的能力在日常生活中非常有用。')
