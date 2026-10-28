"""Visual transcription of fifth-unit headwords beginning on PDF160–164."""
COMPLETE_THROUGH = 164
NEXT_WORD = 'poison'
NEXT_PAGE = 165

def append(t, associated):
    group = '23 strike相关词汇'
    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(2000+len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-005'
    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))
    def include_page(page):
        w = t.words[-1]
        w['pdf_pages'] = sorted(set(w['pdf_pages']+[page]))
        w['printed_pages'] = [f'{p-8:03}' for p in w['pdf_pages']]

    a('strike', '/straɪk/', 'v. 击，撞；罢工；突然想到；一下子想起；n. 罢工；袭击，打击', 160,
      [('v.', '击，撞'), ('v.', '罢工'), ('v.', '突然想到；一下子想起'), ('n.', '罢工'), ('n.', '袭击，打击')],
      [(0, 'The tree was struck by lightning.', '这棵树遭到了雷击。', 'struck', '例', 160)])
    material('strike', 160, '例', status='quarantined',
      english='Now utopia has grown unfashionable, as we have gained a deeper appreciation of the range of threats facing us.',
      translation='如今，随着我们对自身面临的一系列威胁有了更加深刻的认识，乌托邦逐渐变得不再流行了。',
      reason='原书列在strike下的第二例不含strike或其屈折词形，未强行映射到主词。')
    a('striking', '/ˈstraɪkɪŋ/', 'adj. 显著的，引人注目的', 160,
      [('adj.', '显著的，引人注目的')],
      [(0, 'The similarities between the two cases are striking.', '这两个案例之间的相似之处是惊人的。', 'striking', '例', 160)],
      'strik(e)（打，击）+ ing（形容词后缀）→锣鼓队敲敲打打的，是不是很“引人注目”？→引人注目的。',
      [('strikingly', 'adv. 显著地，引人注目地', 160)])
    material('strikingly', 160, '例', english='Her latest novel is strikingly different from her earlier work.', translation='她最新的小说与她早期的作品截然不同。')
    group = '24 证据相关词汇'
    a('evident', '/ˈevɪdənt/', 'adj. 清楚的，显然的', 160,
      [('adj.', '清楚的，显然的')],
      [(0, 'The orchestra played with evident enjoyment.', '管弦乐队演奏得兴致勃勃。', 'evident', '例', 160),
       (0, 'This tendency in the natural sciences has long been evident in the social sciences too.', '自然科学中的这种趋势在社会科学中也一直很明显。', 'evident', '真题', 160)],
      'e（=ex向外，在外）+ vid（看）+ ent（具有……性质的）→在外面就能看到的→明显的，清楚的。',
      [('evidently', 'adv. 明显地，显然地', 160), ('self-evident', 'adj. 明摆着的，不言而喻的', 160)])
    a('evidence', '/ˈevɪdəns/', 'n. 证据，证明；v. 证明，表明', 160,
      [('v.', '证明，表明'), ('n.', '证据，证明')],
      [(0, 'There is no doubt that gardens evidence an irrepressible urge to create, express, fashion, and beautify.', '毫无疑问，花园表明了一种人们抑制不住的，想要去创造、表达、塑造和美化的冲动。', 'evidence', '真题', 160)])
    a('proof', '/pruːf/', 'n. 证据；检验；证明', 160,
      [('n.', '证明'), ('n.', '证据'), ('n.', '检验')],
      [(0, 'These results are a further proof of his outstanding ability.', '这些成果进一步证明了他的杰出才干。', 'proof', '例', 160),
       (1, 'But under anti-bribery laws, proof must be made of concrete benefits.', '但根据反贿赂法，证据必须由具体的利益构成。', 'proof', '真题', 160)],
      '该词为prove“证明”的名词。')
    material('waterproof', 160, '拓展', definition='adj. 防水的')
    a('approve', '/əˈpruːv/', 'v. 批准；赞成，同意', 160,
      [('v.', '赞成，同意'), ('v.', '批准')],
      [(0, 'She doesn’t approve of me going abroad this year.', '她不同意我今年出国。', 'approve', '例', 161)],
      'ap（表示“加强”）+ prove（证明）→你一再地证明干这件事情是可行的，想要得到别人的“同意、赞成”→同意、赞成。',
      [('approval', 'n. 赞成；批准', 161)])
    material('disapprove', 161, '真题', status='quarantined',
      english='More than two-thirds of young Americans disapprove of President Trump’s use of Twitter.',
      translation='超过三分之二的美国年轻人不赞成特朗普总统使用推特。',
      reason='原书在approve下使用反义词disapprove，单独保留，不挂到approve训练例句。')
    material('approval', 161, '例', english='It is not easy to get the approval of authorities.', translation='得到官方的批准不容易。')
    group = '25 radical相关形近词'
    a('radical', '/ˈrædɪkl/', 'n. 激进分子；adj. 根本的，彻底的；激进的', 161,
      [('adj.', '根本的，彻底的'), ('adj.', '激进的'), ('n.', '激进分子')],
      [(0, 'We need radical changes in education.', '我们需要对教育进行彻底变革。', 'radical', '例', 161),
       (1, 'Such senior doctors back such radical moves.', '这些资深医生支持这些激进的举措。', 'radical', '真题', 161)],
      'ra（发音类似“让”）+ di（发音类似“弟”）+ cal（发音类似“扣”）→让弟扣（篮）→设想弟弟那么小，你就让他学扣篮，太“激进”了→激进的。',
      [('radicalism', 'n. 激进主义', 161)])
    a('racial', '/ˈreɪʃl/', 'adj. 人种的，种族的', 161,
      [('adj.', '人种的，种族的')],
      [(0, 'He struggled to overcome racial prejudice.', '他努力克服种族偏见。', 'racial', '例', 161),
       (0, 'The Supreme Court of the United States had prohibited intentional racial discrimination in jury selection as early as the 1880 case of Strauder v. West Virginia.', '美国最高法院早在1880年的斯特劳德诉西弗吉尼亚州案（Strauder v. West Virginia）中就已经禁止了陪审团遴选中的蓄意种族歧视。', 'racial', '真题', 161)],
      'rac（种族，人种）+ ial（形容词后缀）→人种的，种族的。',
      [('racism', 'n. 种族主义，种族歧视', 161), ('racist', 'n. 种族主义者；adj. 种族主义的', 161)])
    a('ethnic', '/ˈeθnɪk/', 'adj. 种族的，民族的；具有民族特色的；n. 少数民族的人', 161,
      [('adj.', '种族的，民族的'), ('adj.', '具有民族特色的'), ('n.', '少数民族的人')],
      [(0, 'There are continuing ethnic tensions in the region.', '该地区种族关系持续紧张。', 'ethnic', '例', 161),
       (0, 'The school has a lot of ethnic minority students.', '学校有许多少数民族学生。', 'ethnic', '例', 161)])
    a('reality', '/riˈæləti/', 'n. 现实，事实', 161,
      [('n.', '现实，事实')],
      [(0, 'She refuses to face reality.', '她不肯面对现实。', 'reality', '例', 161),
       (0, 'But the reality is these things have very little lasting impact on our happiness levels.', '但现实是这些东西对我们的幸福水平几乎没有持久的影响。', 'reality', '真题', 161)],
      'real（真的）+ ity（名词后缀）→现实。',
      [('realistic', 'adj. 现实的，实际的', 161), ('realist', 'n. 现实主义者', 161)])
    group = '26 pri-相关词汇'
    a('primary', '/ˈpraɪməri/', 'adj. 主要的；最初的；小学教育的', 162,
      [('adj.', '主要的'), ('adj.', '最初的'), ('adj.', '小学教育的')],
      [(0, 'The primary aim of this course is to improve your spoken English.', '这门课的主要目的是提高英语会话能力。', 'primary', '例', 162),
       (0, 'The quality of writing is of primary importance.', '写作的质量是最重要的。', 'primary', '例', 162)])
    material('primary school', 162, '拓展', definition='小学')
    a('primitive', '/ˈprɪmətɪv/', 'adj. 原始的，简陋的；n. 文艺复兴前的艺术家（或作品）', 162,
      [('adj.', '原始的'), ('adj.', '简陋的'), ('n.', '文艺复兴前的艺术家（或作品）')],
      [(0, 'In primitive times human beings did not travel for pleasure but to find a more favourable climate.', '在原始时代，人类旅行不是为了找乐趣，而是寻找更有利的气候。', 'primitive', '例', 162),
       (1, 'The facilities on the campsite were very primitive.', '营地的设施非常简陋。', 'primitive', '例', 162)])
    a('prime', '/praɪm/', 'n. 盛年；鼎盛时期；v. 使（某人）做好准备；adj. 主要的，首要的', 162,
      [('adj.', '主要的，首要的'), ('v.', '使（某人）做好准备'), ('n.', '盛年；鼎盛时期')],
      [(0, 'My prime concern is to protect my property.', '我最关心的是保护自己的财产。', 'prime', '例', 162),
       (1, 'The action will remind you of the joy the activity brought you and prime your muscles for when you can get out there again.', '这个动作会让你想起这项活动带给你的快乐，并让你的肌肉为恢复运动做好准备。', 'prime', '真题', 162)])
    group = '27 元素相关词汇'
    a('element', '/ˈelɪmənt/', 'n. 基本部分；元素；因素，要素；基本原理', 162,
      [('n.', '因素，要素'), ('n.', '基本部分'), ('n.', '元素'), ('n.', '基本原理')],
      [(0, 'There are three important elements to consider.', '有三个重要因素需要考虑。', 'elements', '例', 162),
       (0, 'While climate is a key element, it shouldn’t come at the expense of the rest of the equation.', '虽然气候是一个关键因素，但它不应该以牺牲其他因素为代价。', 'element', '真题', 162)],
      '发音类似“饿了么”→人们饿了要吃点东西，这是生活最基本的部分→基本部分。',
      [('elementary', 'adj. 基本的；基础的，初级的', 162)])
    material('elementary study of English', 162, '拓展', definition='英语的基础学习')
    a('ingredient', '/ɪnˈɡriːdiənt/', 'n. 成分，要素；因素；材料', 162,
      [('n.', '成分，要素'), ('n.', '因素'), ('n.', '材料')],
      [(0, 'Persistence is the ingredient of success.', '坚持是成功的要素。', 'ingredient', '例', 162),
       (1, 'Investors now view stock-market swings as a necessary ingredient to a sustained boom.', '投资者现在认为股市波动是持续繁荣的必要因素。', 'ingredient', '真题', 162)],
      'in（里面）+ gredi（联想成“搁点”）+ ent（联想成enter“进去”）→做饭时要往菜里面放点“材料”→材料。')
    group = '28 情绪相关词汇'
    a('passion', '/ˈpæʃn/', 'n. 激情，强烈情感', 162,
      [('n.', '激情，强烈情感')],
      [(0, 'But the market generates interest far beyond its size because it brings together great wealth, enormous egos, greed, passion and controversy.', '但这个市场产生的利益远超其本身的规模，因为它汇集了大量的财富、巨大的自我、贪婪、激情和争议。', 'passion', '真题', 162)],
      '发音类似“拍心（胸膛）”→设想一个人在说话的时候总是拍着胸脯，他多么有“激情”啊！→激情。',
      [('passionate', 'adj. 情意绵绵的；怒不可遏的；热诚的；狂热的', 163)])
    include_page(163)
    material('passionate', 163, '真题', english='If that happens, passionate consumers would try to persuade others to boycott products.', translation='如果那种事情发生，激动的消费者将会试图劝服其他人抵制产品。')
    a('compassion', '/kəmˈpæʃn/', 'n. 同情，怜悯', 163,
      [('n.', '同情，怜悯')],
      [(0, 'I felt no compassion towards her.', '我对她没有任何怜悯。', 'compassion', '例', 163),
       (0, 'The old people are treated with great compassion.', '老人们得到了深切的同情。', 'compassion', '例', 163)],
      'com（所有人）+ passion（热情）→当发生灾难时，所有人都热情地帮助，就是对当事人充满了“同情”→同情。',
      [('compassionate', 'adj. 有同情心的，表示怜悯的', 163)])
    a('excitement', '/ɪkˈsaɪtmənt/', 'n. 刺激，兴奋，激动', 163,
      [('n.', '兴奋，激动'), ('n.', '刺激')],
      [(0, 'The dog leapt and wagged its tail in excitement.', '狗兴奋得摇着尾巴跳来跳去。', 'excitement', '例', 163),
       (0, 'Good TV shows cannot replace the excitement of a zoo visit as an intense, immersive and interactive experience.', '优秀的电视节目无法取代参观动物园带来的那种激动，那是一种强烈的、身临其境的、具有互动性的体验。', 'excitement', '真题', 163)],
      related=[('excited', 'adj. 激动的，兴奋的', 163), ('exciting', 'adj. 使人兴奋的，令人激动的', 163)])
    material('excited', 163, '例', english='Girls tend to get excited more easily than boys.', translation='女孩比男孩更容易激动。')
    a('enthusiastic', '/ɪnˌθjuːziˈæstɪk/', 'adj. 热心的，热情的', 163,
      [('adj.', '热心的，热情的')],
      [(0, 'You don’t sound very enthusiastic about the idea.', '你好像对这个想法不太感兴趣。', 'enthusiastic', '例', 163),
       (0, 'The failure was a big blow to him, but he wasn’t discouraged and soon got as enthusiastic as ever.', '这次失败对他来说是一个巨大的打击，但他并不气馁，很快就恢复了一如既往的热情。', 'enthusiastic', '例', 163)],
      related=[('enthusiast', 'n. 热心者，爱好者', 163), ('enthusiasm', 'n. 热情，热心；热衷的事物', 163)])
    material('enthusiasm', 163, '真题', english='No disciplines have seized on professionalism with as much enthusiasm as the humanities.', translation='没有哪个学科像人文学科那样热衷于专业化。')
    a('negative', '/ˈneɡətɪv/', 'adj. 消极的，负面的，否定的', 163,
      [('adj.', '消极的，负面的'), ('adj.', '否定的')],
      [(0, 'The whole experience was definitely more positive than negative.', '整个经历当然是利多于弊。', 'negative', '例', 163),
       (0, 'One study found that people responded best to comments that shifted from negative to positive.', '一项研究发现，人们对从消极转变为积极的评论反应最好。', 'negative', '真题', 163)],
      'neg（否认，拒绝）+ ative（有……倾向的）→否认的；否定的。')
    a('optimistic', '/ˌɒptɪˈmɪstɪk/', 'adj. 乐观的', 163,
      [('adj.', '乐观的')],
      [(0, 'The man is quite optimistic about human nature.', '这个人对人性相当乐观。', 'optimistic', '例', 164),
       (0, 'They nudge the self-image of the city into a bolder and more optimistic light.', '它们将这座城市的自我形象推向了更大胆、更乐观的方向。', 'optimistic', '真题', 164)],
      related=[('optimism', 'n. 乐观；乐观主义', 164)])
    material('optimism', 164, '例', english='There are very real grounds for optimism.', translation='的确有理由可以乐观。')
    a('pessimistic', '/ˌpesɪˈmɪstɪk/', 'adj. 悲观的', 164,
      [('adj.', '悲观的')],
      [(0, 'I think you’re being far too pessimistic.', '我觉得你过于悲观了。', 'pessimistic', '例', 164),
       (0, 'This long perspective makes the pessimistic view of our prospects seem more likely to be a passing fad.', '这种长远视角使对人类前景的悲观观点看起来更像一个短暂的风潮。', 'pessimistic', '真题', 164)],
      'pessi（联想成“怕是”）+ mistic（联想成mistake“错误”）→他总是害怕犯错误受批评，对待生活有点“悲观”→悲观的。',
      [('pessimism', 'n. 悲观，悲观主义', 164), ('pessimist', 'n. 悲观论者，悲观主义者', 164)])
    a('passive', '/ˈpæsɪv/', 'adj. 被动的，消极的', 164,
      [('adj.', '被动的'), ('adj.', '消极的')],
      [(0, 'We are passive recipients of information from the world around us.', '我们被动地接收周围世界的信息。', 'passive', '例', 164)],
      'pass（过）+ ive（形容词后缀）→他很难从过去走出来，非常“消极”→消极的。')
    group = '29 变坏相关词汇'
    a('spoil', '/spɔɪl/', 'v. 搞坏，破坏；宠坏，溺爱', 164,
      [('v.', '搞坏，破坏'), ('v.', '宠坏，溺爱')],
      [(0, 'Don’t let him spoil your evening.', '别让他弄得你一晚上不开心。', 'spoil', '例', 164),
       (1, 'Parents should not spoil their children.', '家长不应该溺爱孩子。', 'spoil', '例', 164)],
      'sp（some place某个地方）+ oil（油）→“在某个地方火上浇油”使更严重→破坏、损坏；溺爱。')
    a('destroy', '/dɪˈstrɔɪ/', 'v. 破坏，毁灭，摧毁', 164,
      [('v.', '破坏，毁灭，摧毁')],
      [(0, 'The earthquake destroyed countless homes.', '地震摧毁了无数的房屋。', 'destroyed', '例', 164),
       (0, 'Destroying the machines that are coming for our jobs would be nuts.', '摧毁即将取代我们工作的机器将是疯狂的。', 'Destroying', '真题', 164)],
      related=[('destruction', 'n. 破坏，毁灭', 164), ('destructive', 'adj. 破坏性的', 164)])
    material('destruction', 164, '例', english='The earthquake caused loss of life and property destruction.', translation='地震造成了生命和财产损失。')
    material('destructive', 164, '例', english='Too much happiness can be destructive.', translation='乐极生悲。')
    a('deteriorate', '/dɪˈtɪəriəreɪt/', 'v. 恶化，变坏', 164,
      [('v.', '恶化，变坏')],
      [(0, 'They had to cope with deteriorating weather conditions.', '他们不得不应对不断恶化的天气状况。', 'deteriorating', '例', 165),
       (0, 'Old objects continue to deteriorate.', '旧物件继续老化变质。', 'deteriorate', '真题', 165)],
      '事情的状况一直在恶化（deteriorate），我们必须想办法制止（deter）。')
