"""Visual transcription of sixth-unit headwords starting on PDF185–189."""
COMPLETE_THROUGH = 189
NEXT_WORD = 'sparkle'
NEXT_PAGE = 190

def append(t, associated):
    group = '19 培养、养育相关词汇'
    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(2104+len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-006'
    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))
    def include_page(page):
        w=t.words[-1]
        w['pdf_pages']=sorted(set(w['pdf_pages']+[page]))
        w['printed_pages']=[f'{p-8:03}' for p in w['pdf_pages']]

    a('flourish', '/ˈflʌrɪʃ/', 'v. 繁荣，昌盛，兴旺；茁壮成长', 185,
      [('v.', '繁荣，昌盛，兴旺'), ('v.', '茁壮成长')],
      [(0, 'The arts began to flourish at that time.', '艺术是从那时开始繁荣的。', 'flourish', '例', 185),
       (1, 'Helping forests flourish as valuable “carbon sinks” long into the future may require reducing their capacity to absorb carbon now.', '帮助森林发展成为宝贵的“碳汇”并一直持续下去，可能需要降低它们现有的碳吸收能力。', 'flourish', '真题', 185)],
      'flour（联想成flower“花”）+ ish（使）→使花茂盛生长→茁壮成长；繁荣。')
    a('flour', '/ˈflaʊə(r)/', 'n. 面粉，粉；v. 向……上撒面粉', 185,
      [('n.', '面粉，粉'), ('v.', '向……上撒面粉')],
      [(0, 'Flour is sold by the kilogram.', '面粉按千克出售。', 'Flour', '例', 185),
       (0, 'He added some flour to thicken the soup.', '他加了一些面粉使汤浓些。', 'flour', '例', 185)])
    a('feedback', '/ˈfiːdbæk/', 'n. 反馈的意见（或信息）', 185,
      [('n.', '反馈的意见（或信息）')],
      [(0, 'The teacher will give you feedback on the test.', '老师会对你的测验提供反馈信息。', 'feedback', '例', 185),
       (0, 'If you’re not sure, ask for honest feedback from trusted friends, colleagues and professionals.', '如果你不确定，向你信任的朋友、同事和专业人士寻求诚实的反馈。', 'feedback', '真题', 185)],
      'feed（提供）+ back（回来）→提供给你的信息，你需要看后返回来→反馈。')
    group = '20 幻想、想象相关词汇'
    a('fantasy', '/ˈfæntəsi/', 'n. 幻想，想象', 185,
      [('n.', '幻想，想象')],
      [(0, 'She dismissed the idea as a wild fantasy.', '她觉得那个想法太过不切实际而不予考虑。', 'fantasy', '例', 185),
       (0, 'On display here are various fantasy elements whose reference, at some basic level, seems to be the natural world.', '此处展示的是各种幻想元素，在某些基本层面上，这些元素的参照物就是自然世界。', 'fantasy', '真题', 185)],
      '发音类似“范特思”→范特思是一个爱做“白日梦”的人→幻想，想象。',
      [('fantastic', 'adj. 怪诞的；极好的；不切实际的', 185)])
    material('fantastic', 185, '例', english='This was a fantastic opportunity for students.', translation='这对学生来说是一个极好的机会。')
    a('illusion', '/ɪˈluːʒn/', 'n. 幻想的事物；错觉；错误的观念；幻想', 185,
      [('n.', '幻想的事物；幻想'), ('n.', '错觉'), ('n.', '错误的观念')],
      [(0, 'I don’t want to have my illusions shattered!', '我不想让我的幻想破灭！', 'illusions', '例', 185),
       (1, 'Mirrors in a room often give an illusion of space.', '房间里的镜子常给人一种空间增大的错觉。', 'illusion', '例', 185)],
      '发音类似“一路人”→你以为你俩是一路人，但有时候只是你的“错觉”→错觉。',
      [('illusory', 'adj. 虚假的；幻觉的；迷惑人的', 185)])
    a('illuminate', '/ɪˈluːmɪneɪt/', 'v. 照明，照射，照亮；阐明，解释', 185,
      [('v.', '照明，照射，照亮'), ('v.', '阐明，解释')],
      [(0, 'The earth is illuminated by the sun.', '太阳照亮地球。', 'illuminated', '例', 186),
       (1, 'The study of language can help to illuminate how the human mind works.', '对语言的研究有助于阐明人类思维是如何运作的。', 'illuminate', '例', 186)],
      '发音类似“一路明”→如果有人给你“照明，照亮”你的人生之路，那你的人生路有可能是一路光明的→照明，照亮。')
    a('fancy', '/ˈfænsi/', 'v. 认为，想象；想要，想做；自负；n. 想象（力）；想要；adj. 异常复杂的；精致的；奢华的', 186,
      [('v.', '想要，想做'), ('v.', '认为，想象'), ('v.', '自负'), ('n.', '想象（力）'), ('n.', '想要'), ('adj.', '异常复杂的'), ('adj.', '精致的；奢华的')],
      [(0, 'I fancied a change of scene.', '我倒希望换换环境。', 'fancied', '例', 186),
       (1, 'She fancied (that) she could hear footsteps.', '她觉得好像听到了脚步声。', 'fancied', '例', 186)],
      '发音类似“烦死”→备考特别烦的时候，不如坐那儿“想象”一下自己考上以后的美好时光，这样你瞬间就有了斗志→想象。')
    group = '21 风格、种类相关词汇'
    a('fashion', '/ˈfæʃn/', 'n. 时兴式样；流行款式；时尚；时装业；v. 制作；塑造', 186,
      [('v.', '制作；塑造'), ('n.', '时兴式样；流行款式'), ('n.', '时尚；时装业')],
      [(0, 'She fashioned a pot from the clay.', '她用黏土制成一个小罐。', 'fashioned', '例', 186),
       (2, 'The fashion industry knows it has an inherent problem in focusing on material adornment and idealized body types.', '时尚界清楚，它在注重物质装饰和理想化身材方面存在固有问题。', 'fashion', '真题', 186)],
      related=[('fashionable', 'adj. 流行的，时髦的', 186), ('unfashionable', 'adj. 不流行的；过时的', 186), ('old-fashioned', 'adj. 过时的，陈旧的', 186)])
    material('fashionable', 186, '例', english='It’s becoming fashionable to have long hair again.', translation='现在又开始流行留长发了。')
    a('style', '/staɪl/', 'n. 风格；款式，样式；时新，时髦；方式，作风；v. 设计', 186,
      [('n.', '方式，作风'), ('n.', '款式，样式'), ('n.', '风格'), ('n.', '时新，时髦'), ('v.', '设计')],
      [(0, 'I like your style.', '我喜欢你做事的方式。', 'style', '例', 186),
       (1, 'We stock a wide variety of styles and sizes.', '我们有各种款式各种尺码的货品。', 'styles', '例', 186)])
    a('genre', '/ˈʒɒnrə/', 'n. 体裁，类型', 186,
      [('n.', '体裁，类型')],
      [(0, 'His films cover a wide range of subjects and genres.', '他的电影涵盖了广泛的主题和流派。', 'genres', '例', 186),
       (0, 'Equally, in poetry, the highly personal, performative genre is the only form that could claim real liveliness.', '同样，在诗歌领域中，高度个性化和富有表现力的创作流派成为能够表达真实生动的唯一形式。', 'genre', '真题', 186)],
      '基因（gene）的类型（genre）很多。')
    group = '22 indignant相关词汇'
    a('dignity', '/ˈdɪɡnəti/', 'n. 庄重，庄严；尊严；高贵；高尚', 186,
      [('n.', '庄重，庄严'), ('n.', '尊严'), ('n.', '高贵；高尚')],
      [(0, 'She accepted the criticism with quiet dignity.', '她大度地接受了批评。', 'dignity', '例', 187),
       (1, 'One explanation might be the loss of dignity displayed through a cheesy grin.', '一种解释可能是做作地露齿笑显得有失尊严。', 'dignity', '真题', 187)],
      'dign（有价值的，高贵的）+ ity（具备某种性质）→高贵，高尚。')
    a('indignant', '/ɪnˈdɪɡnənt/', 'adj. 愤怒的，愤慨的，愤愤不平的', 187,
      [('adj.', '愤怒的，愤慨的，愤愤不平的')],
      [(0, 'They were quite indignant at his remarks.', '他们对他的言论十分恼火。', 'indignant', '例', 187),
       (0, 'They were indignant that they hadn’t been invited.', '他们因没有受到邀请而愤愤不平。', 'indignant', '例', 187)],
      'in（里面）+ dig（挖）+ nant（想成nation“国家”）→在别的国家里挖宝贝，别的国家肯定是“愤怒的”→愤怒的。',
      [('indignation', 'n. 愤慨，义愤', 187)])
    material('indignation', 187, '例', english='The rise in train fares has aroused public indignation.', translation='火车票提价激起了公愤。')
    a('rage', '/reɪdʒ/', 'n. 狂怒；愤怒的行为；v. 发怒，怒斥；迅速蔓延；猛烈地继续', 187,
      [('v.', '发怒，怒斥'), ('v.', '猛烈地继续'), ('v.', '迅速蔓延'), ('n.', '狂怒；愤怒的行为')],
      [(0, 'He raged against the injustice of it all.', '这一切不公正使他大发怒火。', 'raged', '例', 187),
       (1, 'The blizzard was still raging outside.', '外面暴风雪仍在肆虐。', 'raging', '例', 187)],
      '老是在一个女人面前故意提年龄（age），她有可能会发怒（rage）。',
      [('outrage', 'n. 暴行；愤怒；v. 激怒，使震怒', 187)])
    material('outrage', 187, '真题',
      english='Everybody loves a fat pay rise. Yet pleasure at your own can vanish if you learn that a colleague has been given a bigger one. Indeed, if he has a reputation for slacking, you might even be outraged.',
      translation='人人都喜欢大幅度加薪。然而，如果你得知某位同事得到了更大的加薪，自己的快乐就会消失。事实上，如果他有懒散的名声，你甚至可能会愤怒。')
    a('hospitable', '/hɒˈspɪtəbl/', 'adj. 好客的，热情友好的', 187,
      [('adj.', '好客的，热情友好的')],
      [(0, 'The local people are very hospitable to strangers.', '当地人对外来客人十分友好热情。', 'hospitable', '例', 187)],
      '医院（hospital）里的医生对待病人是很友好的（hospitable）。',
      [('hospitality', 'n. 好客；殷勤；服务；款待', 187)])
    material('hospitality', 187, '例', english='The natives are noted for their hospitality.', translation='当地人以好客而闻名。')
    group = '23 brutal相关形近词'
    a('brutal', '/ˈbruːtl/', 'adj. 残暴的；兽性的；冷酷的', 187,
      [('adj.', '残暴的'), ('adj.', '冷酷的'), ('adj.', '兽性的')],
      [(0, 'He is a brutal man.', '他是个残暴的人。', 'brutal', '例', 187),
       (1, 'With brutal honesty she told him she did not love him.', '她冷酷地直接告诉他，她不爱他。', 'brutal', '例', 187)],
      '发音类似“布鲁特”→布鲁特是个“残暴的”人→残暴的。')
    a('bruise', '/bruːz/', 'n. 碰伤；青肿；v. 打击，挫伤，擦伤', 187,
      [('n.', '碰伤；青肿'), ('v.', '打击，挫伤，擦伤')],
      [(0, 'He wore a hat to cover the bruises on his head.', '他戴着一顶帽子，遮住了他头上的淤青。', 'bruises', '例', 188),
       (0, 'She suffered only minor cuts and bruises.', '她只是受了点儿轻微的割伤和挫伤。', 'bruises', '例', 188)],
      '发音类似“不如死”→她很在意自己的外表，哪怕脸上受了“擦伤”，她都会夸张地说，自己不如死了算了→擦伤。')
    group = '24 谐音记忆更牢固哟'
    a('shrewd', '/ʃruːd/', 'adj. 精明的；敏锐的；有眼光的；判断得准的', 188,
      [('adj.', '有眼光的；判断得准的'), ('adj.', '精明的；敏锐的')],
      [(0, 'She is a shrewd judge of character.', '她看人看得很准。', 'shrewd', '例', 188),
       (1, 'Paul was too shrewd to be taken in by this argument.', '保罗太精明了，不会被这场争论所欺骗。', 'shrewd', '例', 188)],
      '发音类似“熟的”→熟悉这个事物的人，看待它一般比较“敏锐”→敏锐的。')
    a('stern', '/stɜːn/', 'adj. 严厉的，苛刻的；严峻的', 188,
      [('adj.', '严厉的，苛刻的'), ('adj.', '严峻的')],
      [(0, 'Her mother appeared, looking very stern.', '她母亲露面了，看上去非常严厉。', 'stern', '例', 188),
       (0, 'His voice was suddenly stern.', '他的声音突然严厉起来。', 'stern', '例', 188)],
      '发音类似“死瞪”→有些严厉的老师可能会在课上死死地瞪着你，观察你的表现→严厉的。')
    a('diligent', '/ˈdɪlɪdʒənt/', 'adj. 孜孜不倦的，勤奋的，勤勉的，刻苦的', 188,
      [('adj.', '孜孜不倦的，勤奋的，勤勉的，刻苦的')],
      [(0, 'He is a diligent student.', '他是个勤奋的学生。', 'diligent', '例', 188),
       (0, 'Meyers is a diligent and prolific worker.', '迈耶斯是个勤奋而且出活多的工人。', 'diligent', '例', 188)],
      'di（联想成“弟弟”）+ lig（发音类似“历经”）+ ent（联想成“enter”进入）→弟弟历经坎坷，勤奋努力，进入幸福生活→勤奋的。',
      [('diligence', 'n. 勤奋；勤勉', 188)])
    group = '25 东方、地平线相关词汇'
    a('orient', '/ˈɔːrient/', 'n. 东方；v. 确定方向；使朝向', 188,
      [('v.', '确定方向；使朝向'), ('n.', '东方')],
      [(0, 'We run a commercially oriented operation.', '我们经营一个商业性的企业。', 'oriented', '例', 188),
       (0, 'Our students are oriented towards science subjects.', '我们教授的学生都是理科方向的。', 'oriented', '例', 188)],
      related=[('oriental', 'adj. 东方的，东方人的', 188), ('orientation', 'n. 方向；定向；目标', 188)])
    t.pending('orient', 0, 'commercially oriented为定语导向用法，与原书动词确定方向、使朝向的映射待核。')
    t.pending('orient', 1, 'oriented towards science subjects为学科倾向或方向状态，暂不直接训练原书确定方向、使朝向义。')
    material('orientation', 188, '例', english='The course is essentially theoretical in orientation.', translation='该课程的定位是以理论为主。')
    a('horizon', '/həˈraɪzn/', 'n. 地平线；海平线；眼界，范围', 188,
      [('n.', '地平线；海平线'), ('n.', '眼界，范围')],
      [(0, 'The sun sank below the horizon.', '太阳落到了地平线下。', 'horizon', '例', 188),
       (1, 'She wanted to travel to broaden her horizons.', '她想旅行，以开阔眼界。', 'horizons', '例', 188)])
    group = '26 ready的副词哦'
    a('readily', '/ˈredɪli/', 'adv. 乐意地；轻易地；迅速地；便利地', 189,
      [('adv.', '便利地'), ('adv.', '轻易地'), ('adv.', '乐意地'), ('adv.', '迅速地')],
      [(0, 'All ingredients are readily available from your local store.', '所有的原料都可以方便地从你当地的商店买到。', 'readily', '例', 189),
       (1, 'While it probably wasn’t apparent at the time, much of this work is permeated by a spirit of romantic escapism that the likes of Wordsworth would have readily understood.', '虽然这在当时可能并不明显，但大部分这些作品都渗透着一种浪漫主义的避世精神，华兹华斯之类的人很容易理解这种精神。', 'readily', '真题', 189)],
      '只有准备好了的（ready），才可能轻易地（readily）获得成功。')
    group = '27 frame相关形近词'
    a('frame', '/freɪm/', 'n. 框架；构架；体形，身材', 189,
      [('n.', '框架；构架'), ('n.', '体形，身材')],
      [(0, 'She leaned against the frame of the door.', '她靠在门框上。', 'frame', '例', 189),
       (1, 'She has quite a small frame.', '她身材很瘦小。', 'frame', '例', 189)])
    a('flame', '/fleɪm/', 'n. 火焰；强烈的情感，激情', 189,
      [('n.', '火焰'), ('n.', '强烈的情感，激情')],
      [(0, 'The room was filled with smoke and flames.', '房间里充满了烟雾和火焰。', 'flames', '例', 189),
       (1, 'His childhood interest in the game had ignited a flame of passion for football.', '他童年时对足球的兴趣点燃了他对这项运动的激情。', 'flame', '例', 189)],
      '火烈鸟（flamingo）身上的颜色跟火焰（flame）的颜色相似。')
    include_page(190)
    group = '28 flare相关形近词'
    a('flare', '/fleə(r)/', 'v. 闪耀；燃烧；突发；加剧', 189,
      [('v.', '闪耀'), ('v.', '燃烧'), ('v.', '突发；加剧')],
      [(0, 'The match flared and went out.', '火柴闪亮了一下就熄灭了。', 'flared', '例', 189),
       (0, 'Colour flared in her cheeks.', '她两颊泛起了红晕。', 'flared', '例', 189)],
      '火焰（flame）在燃烧（flare）。')
    t.pending('flare', 1, '本句为脸颊泛红的比喻用法，原书闪耀、燃烧等释义未明确列出此义，暂待核对映射。')
    a('flee', '/fliː/', 'v. 逃避；逃跑；迅速离开', 189,
      [('v.', '逃避；逃跑；迅速离开')],
      [(0, 'He fled to London after an argument with his family.', '他与家人争吵以后离家去了伦敦。', 'fled', '例', 189),
       (0, 'The recession threatened to remove the advertising and readers that had not already fled to the internet.', '经济衰退差点将仅存的还未转至互联网的广告和读者统统清除。', 'fled', '真题', 189)],
      '发音类似“飞离”→飞着就离开了，跑得好快啊→逃跑。')
    a('flatter', '/ˈflætə(r)/', 'v. 奉承，讨好，向……谄媚；使显得更漂亮', 189,
      [('v.', '奉承，讨好，向……谄媚'), ('v.', '使显得更漂亮')],
      [(0, 'Are you trying to flatter me?', '你是想讨好我？', 'flatter', '例', 189),
       (0, 'I am flattered by his attention.', '他的关注使我感到格外高兴。', 'flattered', '例', 189)],
      '你最近买了10套房子（flat），有些人听说了后，纷纷来讨好（flatter）你。',
      [('flattering', 'adj. 奉承的，阿谀的，讨好的，使人显得更漂亮的', 190)])
    t.pending('flatter', 1, 'be flattered在本句为感到荣幸或高兴的状态义，原书奉承讨好义未明确列此语义，保留待核。')
    include_page(190)
    material('flattering', 190, '真题',
      english='If the subjects quickly chose a falsely flattering image—which most did—they genuinely believed it was really how they looked.',
      translation='如果受试者很快选择了一张比本人好看的虚假照片——大多数人都这么选了——那他们打心底相信这张照片就是他们真实的样子。')
