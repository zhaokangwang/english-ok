"""Visual transcription of eighth-batch headwords beginning on PDF115–119."""
COMPLETE_THROUGH = 119
NEXT_WORD = 'specialist'
NEXT_PAGE = 120

def append(t, associated):
    group = '06 场地相关词汇'
    def a(spelling, ipa, definition, page, senses, examples, mnemonic='', related=()):
        t.add(1105+len(t.words), spelling, ipa, definition, page, group, senses, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-004'
    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))
    def include(page):
        w = t.words[-1]
        w['pdf_pages'] = sorted(set(w['pdf_pages']+[page]))
        w['printed_pages'] = [f'{p-8:03}' for p in w['pdf_pages']]

    a('spot', '/spɒt/', 'n. 地点，场所；污渍；v. 看见，看出', 115,
      [('n.', '地点，场所'), ('n.', '污渍'), ('v.', '看见，看出')],
      [(2, 'It took a practised eye to spot the difference.', '只有内行人才能看出其中的差异。', 'spot', '例', 115),
       (0, 'Scattered around the globe are more than 100 small regions of isolated volcanic activity known to geologists as hot spots.', '地球上散布着100多个孤立火山活动的小区域，地质学家称之为热点。', 'spots', '真题', 115)],
      '运动（sport）去掉r（人）就只剩运动的地点（spot）了。')
    a('potential', '/pəˈtenʃl/', 'n. 潜质，潜力；可能性，潜在性；adj. 潜在的，可能的', 115,
      [('n.', '潜质，潜力'), ('n.', '可能性，潜在性'), ('adj.', '潜在的，可能的')],
      [(0, 'The new business offers great potential for growth.', '新业务有巨大的增长潜力。', 'potential', '例', 115),
       (2, 'Asking them questions about what they like about the backyard of a potential home will make them feel like they’re being included in the decision-making process.', '向他们询问喜欢未来住宅后院的哪些方面，会让他们觉得自己也参与了决策过程。', 'potential', '真题', 115)])
    a('site', '/saɪt/', 'n. 地点，场所；网站', 115,
      [('n.', '地点，场所'), ('n.', '网站')],
      [(0, 'A site has been chosen for the new school.', '已为新学校选了校址。', 'site', '例', 115),
       (1, 'Until recently, Internet marketing activities have focused on strategies to “pull” customers into sites.', '就在不久前，互联网上的营销活动集中在如何将用户“拉进”网站的策略问题上。', 'sites', '真题', 115)])
    group = '07 引用相关词汇'
    a('cite', '/saɪt/', 'v. 引用，引证；列举', 115,
      [('v.', '引用，引证'), ('v.', '列举')],
      [(1, 'She cited examples of companies the city has helped relocate or expand.', '她列举了该市帮助搬迁或扩张的公司的例子。', 'cited', '例', 115),
       (0, 'She cited a passage from the President’s speech.', '她引用了总统的一段讲话。', 'cited', '例', 115)])
    a('quote', '/kwəʊt/', 'n. 引文；引语；v. 引用，举例说明', 115,
      [('v.', '引用，举例说明'), ('n.', '引文；引语')],
      [(0, 'He was widely quoted in the American media.', '他被美国媒体广泛引用。', 'quoted', '例', 115),
       (1, 'The essay was full of quotes.', '这篇文章满篇皆是引语。', 'quotes', '例', 115)],
      '发音类似“夸她”→想要夸她，可以“引用”一个词：倾国倾城→引用。')
    group = '08 tense相关词汇'
    a('tense', '/tens/', 'adj. 紧张的；n. 时态', 116,
      [('adj.', '紧张的'), ('n.', '时态')],
      [(0, 'The atmosphere in the meeting was getting more and more tense.', '会议的气氛越来越紧张。', 'tense', '例', 116),
       (1, 'Older generations often talk about their degree in the present and personal tense.', '老一辈人经常用现在时的和个人化的口吻谈论自己的学位。', 'tense', '真题', 116)],
      'ten（十）+ se（蛇）→放学的路上，突然跑出来十条蛇围着你，你是什么感觉？→紧张的。')
    t.pending('tense', 1, '本句personal tense为修辞表达，原译为口吻；与语法时态词义的直接对应需复核。')
    a('intensive', '/ɪnˈtensɪv/', 'adj. 密集的；彻底的；集约的', 116,
      [('adj.', '密集的；集约的'), ('adj.', '彻底的')],
      [(0, 'Ahead of us lay ten days of intensive training.', '我们还要进行十天的强化训练。', 'intensive', '例', 116),
       (0, 'Energy conservation, a shift to other fuels and a decline in the importance of heavy, energy-intensive industries have reduced oil consumption.', '能源节约、燃料替代以及能源密集型重工业的重要性逐渐降低，这些都减少了石油消耗。', 'intensive', '真题', 116)],
      related=[('intensively', 'adv. 集中地', 116)])
    a('intense', '/ɪnˈtens/', 'adj. 紧张的；强烈的；热切的；激烈的', 116,
      [('adj.', '强烈的；激烈的'), ('adj.', '紧张的'), ('adj.', '热切的')],
      [(0, 'We were all suffering in the intense heat.', '我们都在酷热下受折磨。', 'intense', '例', 116),
       (0, 'It is sure to spark intense opposition from the far larger number of motorists who will then be affected.', '这肯定会引发更多驾车者的强烈反对，届时他们会受到影响。', 'intense', '真题', 116)],
      related=[('intensity', 'n. 强度；强烈；紧张；剧烈', 116)])
    material('intensity', 116, '真题', english='Increase time, distance, and intensity gradually.', translation='逐渐增加时间、距离和强度。')
    group = '09 sense相关词汇'
    a('sense', '/sens/', 'n. 感觉；理解力；判断力；意义，含义；v. 感觉到，意识到', 116,
      [('n.', '意义，含义'), ('n.', '感觉；理解力；判断力'), ('v.', '感觉到，意识到')],
      [(0, 'Globalization in the broadest sense is nothing new.', '最广义的全球化并不是什么新鲜事。', 'sense', '例', 116)])
    material('common sense', 116, '真题', definition='常识',
      english='But when it came to their houses, it was a time of common sense and a belief that less could truly be more.',
      translation='但当涉及他们的房子时，这是一个“少即是多”成为常识和信念的时代。',
      reason='固定搭配common sense另存，未直接作为sense单列意义或感觉词义的例句。')
    a('sensitive', '/ˈsensətɪv/', 'adj. 敏感的；过敏的；体贴的；感觉敏锐的', 116,
      [('adj.', '敏感的'), ('adj.', '过敏的'), ('adj.', '体贴的'), ('adj.', '感觉敏锐的')],
      [(0, 'The elderly are more sensitive about their health.', '老年人对自己的健康更为敏感。', 'sensitive', '例', 116),
       (0, 'But keeping sensitive information on these devices is increasingly a requirement of normal life.', '而在这些设备上保存敏感信息越来越成为日常生活的一种需求。', 'sensitive', '真题', 116)],
      'sens（感，感觉）+ itive（形容词后缀）→敏感的。')
    a('senseless', '/ˈsensləs/', 'adj. 愚蠢的，无意义的；无知觉的', 116,
      [('adj.', '无意义的'), ('adj.', '愚蠢的'), ('adj.', '无知觉的')],
      [(0, 'His death was a senseless waste of life.', '他白浪费了性命，死得毫无意义。', 'senseless', '例', 116),
       (0, 'It’s senseless to continue any further.', '再继续下去毫无意义。', 'senseless', '例', 117)])
    a('sensible', '/ˈsensəbl/', 'adj. 明智的，合理的', 117,
      [('adj.', '明智的，合理的')],
      [(0, 'I think that’s a very sensible idea.', '我认为那是一个非常明智的想法。', 'sensible', '例', 117),
       (0, 'The sensible place to build new houses, factories and offices is where people are, in cities and towns where infrastructure is in place.', '建造新房子、工厂和办公室的明智地点是在人多的地方，在基础设施完备的城镇。', 'sensible', '真题', 117)])
    a('nonsense', '/ˈnɒnsns/', 'n. 谬论，胡扯，毫无意义的话', 117,
      [('n.', '谬论，胡扯，毫无意义的话')],
      [(0, 'Reports that he has resigned are nonsense.', '有关他已经辞职的报道是无稽之谈。', 'nonsense', '例', 117),
       (0, 'There is a great deal of this kind of nonsense in the medical journals.', '医学期刊中充斥着这类无稽之谈。', 'nonsense', '真题', 117)],
      'non（表示“否定”的前缀）+ sense（感觉，意识）→没有常识的→胡扯；谬论。')
    a('sensation', '/senˈseɪʃn/', 'n. 感觉（能力），知觉（能力）；轰动', 117,
      [('n.', '感觉（能力），知觉（能力）'), ('n.', '轰动')],
      [(0, 'I had a strange sensation in my leg.', '我的腿有些异样的感觉。', 'sensation', '例', 117),
       (1, 'News of his arrest caused a sensation.', '他被捕的消息引起了轰动。', 'sensation', '例', 117)],
      related=[('sensational', 'adj. 轰动的；耸人听闻的', 117)])
    material('sensational', 117, '真题',
      english='Their sometimes sensational findings were filled with warnings about the growing competition from overseas.',
      translation='有时他们那些耸人听闻的发现里充满了对海外竞争日益增长的警告之词。')
    group = '10 受伤相关词汇'
    a('harm', '/hɑːm/', 'n. & v. 伤害，损害', 117,
      [('n.', '伤害，损害'), ('v.', '伤害，损害')],
      [(0, 'The court case will do serious harm to my business.', '这起诉讼案件将严重损害我的生意。', 'harm', '例', 117),
       (1, 'The whirlwind that swept through newsrooms harmed everybody.', '席卷新闻编辑室的旋风伤害了所有人。', 'harmed', '真题', 117)],
      related=[('harmful', 'adj. 有害的，伤害的', 117), ('harmless', 'adj. 无害的', 117)])
    a('injure', '/ˈɪndʒə(r)/', 'v. （尤指在事故中）伤害，使受伤；损害，伤害（名誉、自尊等）', 117,
      [('v.', '（尤指在事故中）伤害，使受伤'), ('v.', '损害，伤害（名誉、自尊等）')],
      [(0, 'Several people were seriously injured.', '数人受重伤。', 'injured', '例', 117),
       (1, 'This could seriously injure the company’s reputation.', '这会严重损害公司的声誉。', 'injure', '例', 117)],
      related=[('injury', 'n. 伤害，损伤', 117)])
    material('injury', 117, '例', english='He was lucky to escape injury.', translation='他很幸运没有受伤。')
    a('injurious', '/ɪnˈdʒʊəriəs/', 'adj. 造成伤害的；有害的', 117,
      [('adj.', '造成伤害的；有害的')],
      [(0, 'They are injurious to women’s health.', '它们对妇女的健康有害。', 'injurious', '例', 117),
       (0, 'Darwin was convinced that the loss of these tastes was not only a loss of happiness, but might possibly be injurious to the intellect, and more probably to the moral character.', '达尔文认为，这些品味的缺失，不仅是一种快乐的丧失，还可能损伤智力，甚至更可能对道德品质有害。', 'injurious', '真题', 117)])
    include(118)
    a('rescue', '/ˈreskjuː/', 'n. & v. 营救，救援；抢救', 118,
      [('v.', '营救，救援；抢救'), ('n.', '营救，救援；抢救')],
      [(0, 'They were eventually rescued by helicopter.', '他们最后被直升机救走了。', 'rescued', '例', 118),
       (1, 'Scientists jumped to the rescue with some distinctly shaky evidence.', '科学家们立即伸出援手，提出了一些明显站不住脚的证据。', 'rescue', '真题', 118)],
      're（再次，往回）+ scue（发音类似secure，安全的）→再次回到安全状态→救援，营救。')
    group = '11 模糊相关词汇'
    a('obscure', '/əbˈskjʊə(r)/', 'adj. 无名的；鲜为人知的；费解的；难以理解的；v. 使模糊；使隐晦；使费解', 118,
      [('adj.', '费解的；难以理解的'), ('adj.', '无名的；鲜为人知的'), ('v.', '使模糊；使隐晦；使费解')],
      [(0, 'The origins of the tradition have become obscure.', '这个传统的起源已经变得模糊不清了。', 'obscure', '例', 118),
       (1, 'At the same time, Dickens submitted short sketches to obscure magazines.', '与此同时，狄更斯向一些不知名的杂志投递了一些短篇随笔。', 'obscure', '真题', 118)],
      'ob（表示“不”）+ scure（联想成sure“确切的”）→不确切的东西，会让人感到“难以理解”→费解的，难以理解的。')
    a('vague', '/veɪɡ/', 'adj. 模糊的，不清楚的，不明确的；不详细的；粗略的', 118,
      [('adj.', '模糊的，不清楚的，不明确的'), ('adj.', '不详细的；粗略的')],
      [(0, 'They had only a vague idea where the place was.', '他们只是大概知道那个地方的位置。', 'vague', '例', 118),
       (0, 'Rather than cloaking his exit in the usual vague excuses, he came right out and said he was leaving “to pursue my goal of running a company”.', '他没有用常见的一些含糊不清的借口掩盖自己的离职，而是公开声明，他离职是“为了追求我经营一家公司的目标”。', 'vague', '真题', 118)],
      '发音类似“喂哥”→你给你哥打电话时，一直喊：喂，哥！喂，哥！为什么？电话听不清楚啊→模糊的，不清楚的。')
    a('blur', '/blɜː(r)/', 'n. （移动的）模糊形状；模糊的记忆；v. （使）变模糊；（使）视线模糊', 118,
      [('v.', '（使）变模糊；（使）视线模糊'), ('n.', '（移动的）模糊形状；模糊的记忆')],
      [(0, 'The writing blurred and danced before his eyes.', '字迹变得一片模糊，在他眼前晃动。', 'blurred', '例', 118),
       (0, 'With the blurring of roles, it’s not surprising that women are more stressed at home.', '由于角色界限的模糊，女性在家中感到压力更大也就不足为奇了。', 'blurring', '真题', 118)],
      '发音类似“不乐”→这个老人不太快乐，因为他年龄大了看东西有点“模糊”→模糊。')
    t.pending('blur', 1, 'blurring在本句为名词化过程用法，暂不直接挂到动词或原书模糊形状名词义。')
    group = '12 变少相关词汇'
    a('shrink', '/ʃrɪŋk/', 'v. 缩小，减少；收缩；退缩，畏缩', 118,
      [('v.', '缩小，减少；收缩'), ('v.', '退缩，畏缩')],
      [(0, 'The market for their products is shrinking.', '市场对他们产品的需求在减少。', 'shrinking', '例', 119),
       (1, 'I shrank back into the shadows.', '我退回到了阴暗处。', 'shrank', '例', 119)],
      'shr（联想成share，分享）+ ink（墨水）→分享墨水给别人，自己的那份体积肯定就缩小了→缩小，减少。')
    a('fade', '/feɪd/', 'v. 褪色；逐渐消失；n. 淡出', 119,
      [('v.', '褪色'), ('v.', '逐渐消失'), ('n.', '淡出')],
      [(0, 'The sun had faded the curtains.', '太阳把窗帘晒褪了色。', 'faded', '例', 119),
       (1, 'Other studies have shown that rebellious behavior increases as you become a teenager and then fades away as you grow older.', '其他研究表明，叛逆行为随着你进入青少年时期而增加，然后随着年龄的增长而消失。', 'fades', '真题', 119)],
      '发音类似“废的”→买了一件羊毛衫，洗一次就废了，“褪色”了→褪色。')
    group = '13 天灾相关词汇'
    a('famine', '/ˈfæmɪn/', 'n. 饥荒', 119,
      [('n.', '饥荒')],
      [(0, 'Four million people are now facing famine.', '400万人正面临饥荒。', 'famine', '例', 119),
       (0, 'When famine strikes, it is often women and children who suffer the most.', '发生饥荒时，受害最深的往往是妇女和儿童。', 'famine', '例', 119)],
      '如果没有农民伯伯（farmer）的辛勤，很多人都会面临饥荒（famine）问题。')
    a('disaster', '/dɪˈzɑːstə(r)/', 'n. 灾难，灾祸，不幸', 119,
      [('n.', '灾难，灾祸，不幸')],
      [(0, 'Thousands died in the disaster.', '数千人在这场灾祸中丧生。', 'disaster', '例', 119),
       (0, 'Luckily, if the doormat or stove failed to warn of coming disaster, a successful lawsuit might compensate you for your troubles.', '幸运的是，如果门垫或炉子没有警告即将到来的灾难，一个成功的诉讼可能会补偿你所遭受的灾祸。', 'disaster', '真题', 119)],
      'dis（不）+ aster（星星）→星位不正，可能预示着有“灾难”→灾难。',
      related=[('disastrous', 'adj. 极糟糕的；灾难性的；完全失败的', 119)])
    a('deadly', '/ˈdedli/', 'adj. 致命的；极度的；枯燥的', 119,
      [('adj.', '致命的'), ('adj.', '极度的'), ('adj.', '枯燥的')],
      [(0, 'He has a deadly defect.', '他有一个致命的缺点。', 'deadly', '例', 119),
       (2, 'The lecture was absolutely deadly.', '这讲座简直无聊透了。', 'deadly', '例', 119)])
    group = '14 particular相关词汇'
    a('particular', '/pəˈtɪkjələ(r)/', 'adj. 专指的，特别的，独特的；n. 详情；详细资料', 119,
      [('adj.', '独特的'), ('adj.', '专指的，特别的'), ('n.', '详情；详细资料')],
      [(0, 'Each village has its own particular charm.', '每个村庄都有自己独特的魅力。', 'particular', '例', 119),
       (1, 'These documents are of particular interest.', '这些文件让人尤其感兴趣。', 'particular', '例', 119)],
      related=[('particularly', 'adv. 特别，尤其', 119)])
    material('particularly', 119, '例', english='The visitors were particularly impressed with the dessert.', translation='游客们对甜点印象特别深刻。')
    a('specialise', '/ˈspeʃəlaɪz/', 'v. 专攻，专门研究', 119,
      [('v.', '专攻，专门研究')],
      [(0, 'He specialised in criminal law.', '他专攻刑法。', 'specialised', '例', 120),
       (0, 'Under modern conditions, this requires varying measures of centralized control and hence the help of specialised scientists.', '在现代条件下，这需要不同程度的集中控制措施，因此需要专业科学家的帮助。', 'specialised', '真题', 120)],
      'special（特殊的；专门的）+ ize（动词后缀）→使专门化→专攻，专门研究。')
    t.words[-1]['notes'].append('原书并列美式拼写specialize，保留specialise为主词，不另建重复词条。')
    t.pending('specialise', 1, 'specialised在本句为定语形容词用法，不直接训练原书动词专攻义，暂待核实。')
