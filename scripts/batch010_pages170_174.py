"""Visually transcribed sixth-unit headwords beginning on PDF170–174."""
COMPLETE_THROUGH = 174
NEXT_WORD = 'opportunity'
NEXT_PAGE = 175

def append(t, associated):
    group = '01 extinguish相关形近词'
    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(2000+len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-006'
    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))
    def include_page(page):
        w=t.words[-1]
        w['pdf_pages']=sorted(set(w['pdf_pages']+[page]))
        w['printed_pages']=[f'{p-8:03}' for p in w['pdf_pages']]

    a('extinguish', '/ɪkˈstɪŋɡwɪʃ/', 'v. 熄灭；使破灭', 171,
      [('v.', '熄灭'), ('v.', '使破灭')],
      [(0, 'All lights had been extinguished.', '所有灯光都熄灭了。', 'extinguished', '例', 171),
       (1, 'News of the bombing extinguished all hope of peace.', '轰炸的消息使和平的希望全部破灭。', 'extinguished', '例', 171)],
      related=[('extinguisher', 'n. 灭火器', 171)])
    a('extinct', '/ɪkˈstɪŋkt/', 'adj. 灭绝的，绝种的；不再存在的', 171,
      [('adj.', '灭绝的，绝种的'), ('adj.', '不再存在的')],
      [(0, 'The numbers of these animals have been falling steadily and they are now almost extinct.', '这些动物数量持续下降，现在几近灭绝。', 'extinct', '例', 171),
       (0, 'When prehistoric man arrived in new parts of the world, something strange happened to the large animals: they suddenly became extinct.', '当史前人类到达世界的新区域时，某些奇怪的事情发生在大型动物身上：它们突然灭绝了。', 'extinct', '真题', 171)])
    a('distinguish', '/dɪˈstɪŋɡwɪʃ/', 'v. 区分，辨别；认出，听出', 171,
      [('v.', '区分，辨别'), ('v.', '认出，听出')],
      [(0, 'It was hard to distinguish one twin from the other.', '很难分辨出一对孪生儿谁是谁。', 'distinguish', '例', 171),
       (0, 'Quinn and her colleagues conducted a test to see if rats can distinguish a friendly rat from a hostile one.', '奎因和她的同事们进行了一项试验，观察老鼠是否能分辨一只老鼠是敌是友。', 'distinguish', '真题', 171)],
      '发音类似“弟似听故事”→弟弟似乎在努力地听老师讲故事，试图“辨别”出故事里谁好谁坏→辨别。',
      [('distinguished', 'adj. 杰出的，著名的', 171)])
    material('distinguished',171,'例',english='The college has a very distinguished academic record.',translation='这所学院有着非常出色的学术记录。')
    a('distinct', '/dɪˈstɪŋkt/', 'adj. 有区别的；明确的；清晰的；明显的', 171,
      [('adj.', '明显的'), ('adj.', '有区别的'), ('adj.', '明确的；清晰的')],
      [(0, 'There was a distinct smell of gas.', '有一股明显的煤气味。', 'distinct', '例', 171),
       (1, 'The results of the survey fell into two distinct groups.', '调查结果分为截然不同的两组。', 'distinct', '例', 171)],
      related=[('distinction', 'n. 差别，区别', 171), ('distinctly', 'adv. 明显地，清楚地', 171)])
    material('distinctly',171,'例',english='He could remember everything very distinctly.',translation='他什么事都能记得清清楚楚。')
    a('instinct', '/ˈɪnstɪŋkt/', 'n. 本能，直觉，天性', 171,
      [('n.', '本能；天性'), ('n.', '直觉')],
      [(0, 'Children do not know by instinct the difference between right and wrong.', '儿童并非生来就会分辨是非。', 'instinct', '例', 171),
       (1, 'It’s best to follow your first instincts in matters like this.', '在这种事情上，最好遵循你的第一直觉。', 'instincts', '例', 171)],
      '发音类似“鹰死盯他”→出于“本能”的警觉，鹰死死地盯着他→本能，直觉。')
    a('sting', '/stɪŋ/', 'v. 叮，蜇；刺伤；激怒，使不安', 171,
      [('v.', '叮，蜇；刺伤'), ('v.', '激怒，使不安')],
      [(0, 'I was stung on the arm by a wasp.', '我的胳膊被黄蜂蜇了一下。', 'stung', '例', 172),
       (1, 'He was stung by their criticism.', '他们的批评使他心烦意乱。', 'stung', '例', 172)],
      '发音类似“死盯”→蜜蜂死盯你，肯定就想“蜇”你→蜇。')
    a('string', '/strɪŋ/', 'n. 弦，线，细绳，带子；一串；一系列；v. 悬挂；系', 172,
      [('n.', '弦，线，细绳，带子'), ('n.', '一串；一系列'), ('v.', '悬挂；系')],
      [(0, 'The key is hanging on a string by the door.', '钥匙拴在门边的带子上。', 'string', '例', 172),
       (2, 'We strung paper lanterns up in the trees.', '我们把纸灯笼挂在树上。', 'strung', '例', 172)],
      '他用绳子（string）编了一个漂亮的戒指（ring）送给她。')
    material('a string of lucrative awards',172,'拓展',definition='一系列丰厚的奖项')
    group = '02 spontaneous相关形近词'
    a('spontaneous', '/spɒnˈteɪniəs/', 'adj. 自然的；自发的', 172,
      [('adj.', '自然的；自发的')],
      [(0, 'The audience burst into spontaneous applause.', '观众自发地鼓起掌来。', 'spontaneous', '例', 172),
       (0, 'Spontaneous smiles were relatively easy to capture by the 1890s, so we must look elsewhere for an explanation of why Victorians still hesitate to smile.', '19世纪90年代，自发的微笑相对容易捕捉，所以我们必须从别处寻找解释，为什么维多利亚时代的人仍然不愿微笑。', 'Spontaneous', '真题', 172)],
      '这次活动是主办方（sponsor）自发（spontaneous）组织的。')
    a('sponsor', '/ˈspɒnsə(r)/', 'n. 发起人，赞助者；资助者；v. 发起，主办；赞助；资助', 172,
      [('n.', '发起人，赞助者；资助者'), ('v.', '赞助；资助'), ('v.', '发起，主办')],
      [(0, 'The programme is funded by a number of corporate sponsors.', '该方案由许多公司赞助者资助。', 'sponsors', '例', 172),
       (1, 'It sponsors lots of symposiums and a credibility project.', '它赞助了很多研讨会，并且发起了一次可信度调查项目。', 'sponsors', '真题', 172)],
      'spons（允诺，约定）+ or（表“人”的名词后缀）→允许做某事的人→发起人。')
    group = '03 内、外相关词汇'
    a('intrinsic', '/ɪnˈtrɪnzɪk/', 'adj. 固有的，内在的，本身的', 172,
      [('adj.', '固有的，内在的，本身的')],
      [(0, 'The tasks were repetitive, lengthy and lacking any intrinsic interest.', '这些作业重复冗长，没什么意义。', 'intrinsic', '例', 172),
       (0, 'Birds should continue as a matter of intrinsic right, regardless of the presence or absence of economic advantage to us.', '无论鸟类能否给我们带来经济价值，它们自有生存下去的权利。', 'intrinsic', '真题', 172)],
      'in（里面）+ trins（发音类似“纯的”）+ ic→他的内心是非常纯洁的→内在的。')
    a('extrinsic', '/eksˈtrɪnzɪk/', 'adj. 外在的，外来的；非固有的；非本质的', 172,
      [('adj.', '外在的，外来的'), ('adj.', '非固有的；非本质的')],
      [(0, 'Nowadays there are fewer extrinsic pressures to get married.', '现在，结婚与否很少受到来自外部的压力。', 'extrinsic', '例', 172),
       (0, 'She was motivated by the idea of extrinsic rewards such as salary rather than intrinsic ones such as pride and self-respect.', '她受到外在奖励（如薪水）而不是内在奖励（如骄傲和自尊）的激励。', 'extrinsic', '例', 173)])
    a('internal', '/ɪnˈtɜːnl/', 'adj. 内心的；国内的，内政的；内部的；体内的', 173,
      [('adj.', '体内的'), ('adj.', '国内的，内政的'), ('adj.', '内部的'), ('adj.', '内心的')],
      [(0, 'The medicine is not for internal use.', '这种药不可内服。', 'internal', '例', 173),
       (1, 'He accused the US of trying to interfere in his country’s internal affairs.', '他指责美国试图干涉他的国家的内政。', 'internal', '例', 173)])
    a('external', '/ɪkˈstɜːnl/', 'adj. 外部的，外面的；外来的，外界的', 173,
      [('adj.', '外来的，外界的'), ('adj.', '外部的，外面的')],
      [(0, 'Many external influences can affect your state of mind.', '许多外在因素都可能影响人的心情。', 'external', '例', 173)])
    material('external challenge',173,'拓展',definition='外界的质疑')
    a('interior', '/ɪnˈtɪəriə(r)/', 'n. 内部；里面；内地；内陆；内政；adj. 内部的，里面的', 173,
      [('n.', '内部；里面'), ('n.', '内地；内陆'), ('n.', '内政'), ('adj.', '内部的，里面的')],
      [(0, 'The original interior of the hotel has been replaced.', '旅馆原来的内部装潢已经更换掉了。', 'interior', '例', 173)])
    material('the interior of a plate',173,'拓展',definition='一个板块的内部')
    a('exterior', '/ɪkˈstɪəriə(r)/', 'n. 外部，表面；外貌；adj. 外部的，外在的；表面的', 173,
      [('n.', '外部，表面'), ('adj.', '外部的，外在的；表面的'), ('n.', '外貌')],
      [(0, 'The exterior of the house needs painting.', '房子外部需要粉刷。', 'exterior', '例', 173),
       (1, 'The filming of the exterior scenes was done on the moors.', '外景是在沼泽地拍摄的。', 'exterior', '例', 173)])
    group = '04 -volv-相关词汇'
    a('evolve', '/ɪˈvɒlv/', 'v. 逐渐演变；逐步发展；进化；演化', 173,
      [('v.', '进化；演化'), ('v.', '逐渐演变；逐步发展')],
      [(0, 'The three species evolved from a single ancestor.', '这三种生物从同一祖先进化而来。', 'evolved', '例', 173),
       (1, 'The company has evolved into a major chemical manufacturer.', '这家公司已逐步发展成一家大型的化工厂。', 'evolved', '例', 173)],
      'e（向外）+ volv（旋转）+ e→向外不断地旋转，不断地“发展”→进化，逐步发展。',
      [('evolution', 'n. 进化；发展', 173)])
    a('revolve', '/rɪˈvɒlv/', 'v. 转动，旋转；环绕', 173,
      [('v.', '转动，旋转'), ('v.', '环绕')],
      [(0, 'The fan revolved slowly.', '电扇缓慢地转动着。', 'revolved', '例', 173),
       (1, 'In the first year or so of Web business, most of the action has revolved around efforts to tap the consumer market.', '在网络交易的第一年左右，大部分活动都是围绕着努力开发消费者市场而进行的。', 'revolved', '真题', 173)],
      're（表示“重复”）+ volv（旋转）+ e→重复地“旋转”→旋转；环绕。',
      [('revolution', 'n. 旋转；革命；变革', 173), ('revolutionary', 'adj. 革命性的；革命的', 173)])
    t.pending('revolve',1,'本句revolve around为以某事为中心的比喻搭配，原书只列环绕，暂待复核词义映射。')
    a('involve', '/ɪnˈvɒlv/', 'v. 牵涉；牵连；包含；需要；使参加', 173,
      [('v.', '使参加'), ('v.', '包含'), ('v.', '牵涉；牵连'), ('v.', '需要')],
      [(0, 'We want to involve as many people as possible in the celebrations.', '我们希望参加庆典的人越多越好。', 'involve', '例', 174),
       (1, 'Fantasies of great wealth often involve visions of fancy cars and extravagant homes.', '说起巨额财富，人们往往会想到名车（豪车）与豪宅。', 'involve', '真题', 174)],
      'in（进入）+ volv（卷，转）+ e→转进去→卷入→包含。')
    group = '05 假期相关词汇'
    a('hike', '/haɪk/', 'n. & v. 徒步旅行，远足', 174,
      [('n.', '徒步旅行，远足'), ('v.', '徒步旅行，远足')],
      [(0, 'They met on a hike.', '他们在一次远足中相遇。', 'hike', '例', 174),
       (1, 'If the weather’s fine, we’ll go hiking this weekend.', '如果天气好，我们这个周末就去远足。', 'hiking', '例', 174)],
      '我们不想骑自行车（bike）旅行，我们想徒步旅行（hike）。')
    a('vacation', '/veɪˈkeɪʃn/', 'n. 度假；假期；休庭期', 174,
      [('n.', '假期'), ('n.', '度假'), ('n.', '休庭期')],
      [(0, 'I got a full-time job during the vacation.', '假期里我找到了一份全职工作。', 'vacation', '例', 174),
       (1, 'If it’s their vacation home anyway, and it’s just empty, why can’t you make money off it?', '如果这是他们的度假屋，而且正好闲置，为什么不能靠它赚钱呢？', 'vacation', '真题', 174)],
      '发音类似“我开心”→我为什么开心？因为我有一个很长的“假期”→假期。')
    a('vocation', '/vəʊˈkeɪʃn/', 'n. 工作，职业；信心；使命感', 174,
      [('n.', '工作，职业'), ('n.', '信心'), ('n.', '使命感')],
      [(0, 'He is desperate to follow his vocation as an artist.', '他渴望从事艺术家的职业。', 'vocation', '例', 174),
       (2, 'He has a vocation for teaching.', '他是教书的材料。', 'vocation', '例', 174)],
      '很多人假期（vacation）的时候，会选择找一些兼职的工作（vocation）。',
      [('vocational', 'adj. 职业的', 174)])
    t.pending('vocation',1,'原译教书的材料指资质或天赋，原书主释义未明列此义，暂待复核词义映射。')
    a('excursion', '/ɪkˈskɜːʃn/', 'n. 远足，短途旅行', 174,
      [('n.', '远足，短途旅行')],
      [(0, 'They’ve gone on an excursion to York.', '他们到约克旅游去了。', 'excursion', '例', 174),
       (0, 'We decided to make an all-day excursion to the island.', '我们决定花一整天时间去那个岛上玩。', 'excursion', '例', 174)],
      'ex（出去）+ cursion（发音类似“开心”）→出去开心一下→远足，短途旅行。')
    group = '06 机会、时机相关词汇'
    a('occasion', '/əˈkeɪʒn/', 'n. 场合；合适的机会；某次；……的时候；理由', 174,
      [('n.', '合适的机会'), ('n.', '某次；……的时候'), ('n.', '场合'), ('n.', '理由')],
      [(0, 'I’ve had no occasion to visit him recently.', '我最近无缘去拜访他。', 'occasion', '例', 174),
       (1, 'Only on rare occasions do I go out socially.', '只有在极少数情况下，我才会出去社交。', 'occasions', '例', 174)],
      '发音类似“我开心”→我们不是每天都很开心或伤心的，基本上都是平静地度过每一天。所以开心是有“时候”的，分“场合”的→……的时候；场合。',
      [('occasional', 'adj. 偶然的，偶尔的；临时的', 175)])
    include_page(175)
    material('occasional',175,'例',english='He works for us on an occasional basis.',translation='他在我们这里做临时工。')
    material('on occasion(s)',175,'拓展',definition='偶尔，偶然，有时')
