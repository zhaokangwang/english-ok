"""PDF 90–94 starting headwords, manually checked against page images.

Senator continues onto PDF 95; that page's new headwords belong to the next batch.
"""


def append(t, associated):
    group = '23 alarm相关词汇'

    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(346 + len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)

    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))

    def include_page(page):
        w = t.words[-1]
        w['pdf_pages'] = sorted(set(w['pdf_pages'] + [page]))
        w['printed_pages'] = [f'{p-8:03}' for p in w['pdf_pages']]

    a('slip', '/slɪp/', 'v. 滑（倒）；溜走；下降；偷偷放', 90,
      [('v.', '滑（倒）'), ('v.', '下降'), ('v.', '溜走'), ('v.', '偷偷放')],
      [(0, 'As I ran up the stairs, my foot slipped and I fell.', '我跑上楼梯时，失脚摔倒了。', 'slipped', '例', 90),
       (1, 'Standards have slipped in the last few years.', '在过去的几年里，标准下降了。', 'slipped', '例', 90)],
      '在国外的一些公共场所，我们可能会看到下面的图片（内容：小心地面湿滑！）→滑（倒）。',
      [('slippery', 'adj. 滑的，光滑的；油滑的', 90)])
    material('slippery', 90, '例', english='The road is slippery after a heavy storm.', translation='大雨后路很滑。')
    material('slipper', 90, '拓展', phonetic='/ˈslɪpə(r)/', definition='n. 拖鞋')
    material('pink slip', 90, '拓展', definition='解聘书')

    group = '24 租房相关词汇'
    a('lease', '/liːs/', 'n. 租约，租契；v. 出租，租用', 90,
      [('v.', '出租，租用'), ('n.', '租约，租契')],
      [(0, 'We lease all our computer equipment.', '我们所有的计算机设备都是租来的。', 'lease', '例', 90)],
      '租约（lease）里要求这个场地的租赁年限最少（least）是一年。')
    a('tenant', '/ˈtenənt/', 'n. 房客；租户；佃户', 90,
      [('n.', '房客；租户；佃户')],
      [(0, 'They had evicted their tenants for non-payment of rent.', '他们赶走了未交房租的房客。', 'tenants', '例', 90),
       (0, 'The decorating was done by a previous tenant.', '装修是一位前房客搞的。', 'tenant', '例', 90)])
    a('rent', '/rent/', 'n. 租金；房租；v. 租借，出租，出借', 90,
      [('n.', '租金；房租'), ('v.', '租借，出租，出借')],
      [(0, 'I earn just about enough to pay the rent.', '我挣的钱刚好够付房租。', 'rent', '例', 90),
       (1, 'I can’t afford to pay my monthly mortgage payments on my own, so I have to rent rooms out to people to make that happen.', '凭我一己之力无法负担月供，因此我不得不把房间出租给别人以负担月供。', 'rent', '真题', 90)],
      related=[('rental', 'n. 租金；出租', 90)])
    material('rental environment', 90, '拓展', definition='租赁环境')

    group = '25 cur相关词汇'
    a('current', '/ˈkʌrənt/', 'n. 潮流；电流，水流，气流；趋势；adj. 当前的，现在的；通用的；流通的', 90,
      [('n.', '潮流；电流，水流，气流'), ('adj.', '当前的，现在的'), ('adj.', '通用的；流通的'), ('n.', '趋势')],
      [(0, 'It’s easier to go with the current.', '顺流而下比较容易。', 'current', '例', 90),
       (1, '“Children may face serious difficulties in coping with significant moves, especially if it removes them from their current school or support system,” he said.', '他说：“孩子们在应对重大变动时可能会面临严重的困难，特别是如果这一变动会使他们离开现在的学校或支持体系时更是如此。”', 'current', '真题', 90)],
      '货币（currency）是商品“流通的”（current）媒介。',
      [('currently', 'adv. 现在，当前', 90)])
    material('current news', 90, '拓展', definition='时事')
    a('accurate', '/ˈækjərət/', 'adj. 正确无误的，精确的，准确的', 90,
      [('adj.', '正确无误的，精确的，准确的')],
      [(0, 'I’m not convinced the reports are accurate.', '我不相信这些报道是准确的。', 'accurate', '例', 91),
       (0, 'Scientists have found a more accurate way of dating cave paintings.', '科学家发现了一种更准确的洞穴绘画年代测定方法。', 'accurate', '例', 91)],
      'ac（表示“加强”）+ cur（发音类似care“关心”）+ ate（形容词后缀）→一再地关注这件事，就会把事情做得越来越精确→精确的。',
      [('accuracy', 'n. 精确性，精确度', 91), ('inaccurate', 'adj. 不精确的；不准确的；有错误的', 91)])
    a('secure', '/sɪˈkjʊə(r)/', 'adj. 安全的；可靠的，稳固的；v. 保护，使安全；（尤指经过努力）获得，取得，实现', 91,
      [('adj.', '安全的；可靠的，稳固的'), ('v.', '保护，使安全'), ('v.', '（尤指经过努力）获得，取得，实现')],
      [(0, 'It’s not a very secure way to make a living.', '以此谋生终非长久之计。', 'secure', '例', 91),
       (0, 'During the past generation, the American middle-class family that once could count on hard work and fair play to keep itself financially secure has been transformed by economic risk and new realities.', '在上一代人中，美国中产阶级家庭曾依靠努力工作和公平竞争来保持自己的经济安全，但现在却被经济危机和新的现实所改变。', 'secure', '真题', 91)],
      related=[('security', 'n. 安全；保护措施；安全工作；机场安检区；抵押品', 91)])

    group = '26 好、大相关词汇'
    a('brilliant', '/ˈbrɪliənt/', 'adj. 巧妙的；使人印象深的；很好的，杰出的；明亮的，鲜艳的；聪颖的；技艺高的', 91,
      [('adj.', '明亮的，鲜艳的'), ('adj.', '聪颖的；很好的，杰出的；技艺高的'), ('adj.', '巧妙的；使人印象深的')],
      [(0, 'The sky was a brilliant blue.', '天空一片蔚蓝。', 'brilliant', '例', 91),
       (1, 'He is a brilliant young man.', '他是个才华横溢的年轻人。', 'brilliant', '例', 91)],
      'brilli（发光）+ ant（形容词后缀，“……的”）→发光的→明亮的，灿烂的；杰出的。',
      [('brilliance', 'n. 才华；光辉', 91)])
    a('terrific', '/təˈrɪfɪk/', 'adj. 极好的，绝妙的，了不起的；很大的，巨大的；异乎寻常的', 91,
      [('adj.', '极好的，绝妙的，了不起的'), ('adj.', '很大的，巨大的；异乎寻常的')],
      [(0, 'I feel absolutely terrific today!', '我今天的感觉真是好极了！', 'terrific', '例', 91),
       (1, 'I’ve got a terrific amount of work to do.', '我有大量的工作要做。', 'terrific', '例', 91)],
      '他觉得这个想法是极好的（terrific），但我觉得这个想法很可怕（terrible）。')
    a('magnificent', '/mæɡˈnɪfɪsnt/', 'adj. 宏伟的，壮丽的；值得赞扬的', 91,
      [('adj.', '值得赞扬的'), ('adj.', '宏伟的，壮丽的')],
      [(0, 'You’ve all done a magnificent job.', '你们都干得很出色。', 'magnificent', '例', 91),
       (1, 'Does that mean the writing is on the wall for all European royals, with their magnificent uniforms and majestic lifestyles?', '那是否意味着所有衣着华丽、生活高贵的欧洲皇室成员将大难临头了？', 'magnificent', '真题', 91)],
      'magni（表示“大”）+ fic（=fact，做）+ ent（形容词后缀）→做得够大→壮丽的，宏伟的。')
    a('magnify', '/ˈmæɡnɪfaɪ/', 'v. 放大，夸张；扩大，增强', 92,
      [('v.', '放大，夸张；扩大，增强')],
      [(0, 'The picture shows the insect’s head magnified ten times.', '这张图片上显示的是放大了10倍的这种昆虫的头部。', 'magnified', '例', 92)],
      'magni（表示“大”）+ fy（使……）→使变大→放大；扩大。')
    material('magnifying glass', 92, '真题', english='You really need a magnifying glass to appreciate all the fine detail.', translation='你需要放大镜才能欣赏到一切细微之处。', reason='原句使用名词短语magnifying glass（放大镜），另存关联材料。')
    a('fabulous', '/ˈfæbjələs/', 'adj. 绝妙的，极好的；很大的，巨大的', 92,
      [('adj.', '绝妙的，极好的'), ('adj.', '很大的，巨大的')],
      [(0, 'They put on a fabulous performance.', '他们上演了一场精彩的表演。', 'fabulous', '例', 92),
       (0, 'I want an outfit that’ll make me look fabulous.', '我想要一套让我看起来很棒的服装。', 'fabulous', '例', 92)],
      'fabu（发布）+ l（了）+ ous（形容词后缀）→我的书终于正式发布了，这对我来说是“极好的”。')
    a('fabricate', '/ˈfæbrɪkeɪt/', 'v. 编造，捏造；制造', 92,
      [('v.', '编造，捏造'), ('v.', '制造')],
      [(0, 'The evidence was totally fabricated.', '这个证据纯属伪造。', 'fabricated', '例', 92),
       (1, 'These specialized chips will be fabricated by Microsoft.', '这些专用芯片将由微软公司制造。', 'fabricated', '例', 92)],
      '这个工厂（factory）不制造（fabricate）这种布料（fabric）的衣服。',
      [('fabrication', 'n. 虚构的信息，捏造的故事', 92)])
    material('fabrication', 92, '例', english='Her story was a complete fabrication from start to finish.', translation='她的叙述从头至尾都是编造出来的。')
    a('marvelous', '/ˈmɑːvələs/', 'adj. 极好的，非凡的', 92,
      [('adj.', '极好的，非凡的')],
      [(0, 'It’s marvellous what modern technology can do.', '现代技术所能做的真是太了不起了。', 'marvellous', '例', 92),
       (0, 'This will be a marvellous opportunity for her.', '这对她可是千载难逢的机会。', 'marvellous', '例', 92)])
    t.words[-1]['notes'].append('原书主词拼作marvelous，两个例句均拼作marvellous；保留两种拼写。')
    a('marvel', '/ˈmɑːvl/', 'n. 奇迹；v. 感到惊奇；大为赞叹', 92,
      [('n.', '奇迹'), ('v.', '感到惊奇；大为赞叹')],
      [(0, 'The building is an architectural marvel.', '这座建筑是建筑奇迹。', 'marvel', '例', 92),
       (1, 'To read such books today is to marvel at the fact that their learned contents were once deemed suitable for publication in general-circulation dailies.', '今天读到这样的书，你会惊讶于这样一个事实：书里的学术内容曾经被认为适合发表在面向普通读者发行的日报上。', 'marvel', '真题', 92)])

    group = '27 rigorous相关词汇'
    a('rigorous', '/ˈrɪɡərəs/', 'adj. 严格的，严厉的；谨慎的；细致的；彻底的', 92,
      [('adj.', '谨慎的；细致的；彻底的'), ('adj.', '严格的，严厉的')],
      [(0, 'Few people have gone into the topic in such rigorous detail.', '很少有人如此严谨地讨论这个题目。', 'rigorous', '例', 92),
       (1, 'Schooling and rigorous book learning put unnatural restraints on children.', '学校教育和严格的课本学习对孩子们施加了不自然的限制。', 'rigorous', '真题', 92)],
      '发音类似“若哥惹事”→若哥哥惹了事情，妈妈一定会严厉处罚他的→严厉的。')
    include_page(93)
    t.words[-1]['examples'][-1]['note'] += ' 英文与译文续至PDF93。'
    a('rigid', '/ˈrɪdʒɪd/', 'adj. 严格死板的，僵硬的；固执的；僵化的，一成不变的；坚硬的', 93,
      [('adj.', '僵硬的；坚硬的'), ('adj.', '严格死板的；固执的；僵化的，一成不变的')],
      [(0, 'She sat upright, her body rigid with fear.', '她直挺挺地坐着，吓得浑身发僵。', 'rigid', '例', 93),
       (1, 'Today, we are much more rigid about immigrants.', '今天，我们对移民的态度要严格得多。', 'rigid', '真题', 93)])

    group = '28 bold相关形近词'
    a('bold', '/bəʊld/', 'adj. 大胆自信的；敢于表白情感的；敢于冒险的；明显的；轮廓突出的', 93,
      [('adj.', '大胆自信的；敢于冒险的'), ('adj.', '敢于表白情感的'), ('adj.', '明显的；轮廓突出的')],
      [(0, 'It was a bold move on their part to open a business in France.', '在法国开业是他们的一个大胆举动。', 'bold', '例', 93),
       (0, 'If we were really bold, we might even begin to think of high-calorie fast food in the same way as cigarettes.', '如果我们真的大胆，我们甚至可以开始像对待烟草一样对待高热量快餐。', 'bold', '真题', 93)],
      '虽然他有点老了（old），但是他依然敢于冒险（bold）。',
      [('boldness', 'n. 勇敢；冒失', 93)])
    a('bald', '/bɔːld/', 'adj. 光秃的，秃顶的；不加赘述的；简单的', 93,
      [('adj.', '光秃的，秃顶的'), ('adj.', '不加赘述的；简单的')],
      [(0, 'He started going bald in his twenties.', '他二十几岁便开始谢顶。', 'bald', '例', 93),
       (1, 'The letter was a bald statement of our legal position.', '那封信直截了当地说出我们的法律立场。', 'bald', '例', 93)],
      'ba（联想成“爸爸”）+ ld（联想成old“老了”）→爸爸老了，会有些秃顶→秃顶的，光秃的。')
    a('bleak', '/bliːk/', 'adj. 不乐观的，无望的，暗淡的；无遮掩的；荒凉的；索然无味的；阴冷的', 93,
      [('adj.', '不乐观的，无望的，暗淡的'), ('adj.', '无遮掩的；荒凉的；索然无味的；阴冷的')],
      [(0, 'The future looks bleak for the fishing industry.', '渔业前景暗淡。', 'bleak', '例', 93),
       (0, 'David Graddol concludes that monoglot English graduates face a bleak economic future.', '戴维·葛拉多尔的结论是，只会一门语言的英国本科毕业生面临惨淡的经济前景。', 'bleak', '真题', 93)],
      '这个房子一直漏（leak）水，屋子里非常阴冷（bleak）。')

    group = '29 barren相关形近词'
    a('barren', '/ˈbærən/', 'adj. 贫瘠的，不毛的；不孕的', 93,
      [('adj.', '贫瘠的，不毛的'), ('adj.', '不孕的')],
      [(0, 'The land was barren and infertile.', '这片土地荒芜而贫瘠。', 'barren', '例', 93),
       (0, 'He wants to use the water to irrigate barren desert land.', '他想用水来灌溉贫瘠的沙漠土地。', 'barren', '例', 93)],
      'bar（酒吧）+ ren（发音类似“人”）→人如果天天去酒吧喝酒，可能会对怀孕有影响→不孕的。')
    a('bare', '/beə(r)/', 'adj. 裸体的，裸露的；光秃秃的；空的；v. 使赤裸；使露出', 93,
      [('adj.', '裸体的，裸露的；光秃秃的'), ('adj.', '空的'), ('v.', '使赤裸；使露出')],
      [(0, 'I got in the habit of going around with bare feet.', '我养成了赤脚走路的习惯。', 'bare', '例', 94),
       (1, 'The fridge was completely bare.', '电冰箱里什么也没有。', 'bare', '例', 94)],
      '他在酒吧（bar）喝多了，赤裸（bare）着脚回家了。',
      [('barely', 'adv. 仅仅；刚刚；勉强可能；几乎不，几乎没有', 94)])
    material('barely', 94, '真题', english='During their six- to twelve-week voyage, they survived on barely enough food allotted to them.', translation='在六到十二周的航行中，他们靠分配给他们的食物勉强维持生计。')
    a('bargain', '/ˈbɑːɡən/', 'n. 减价品，便宜货；协议；交易；v. （与某人就某事）讨价还价，商讨条件', 94,
      [('n.', '减价品，便宜货'), ('n.', '协议；交易'), ('v.', '（与某人就某事）讨价还价，商讨条件')],
      [(0, 'I picked up a few good bargains in the sale.', '我在减价期间买了几样挺不错的便宜货。', 'bargains', '例', 94),
       (1, 'The bargain is very pure.', '这种交易非常纯粹。', 'bargain', '真题', 94)],
      '发音类似“八根”→我们用八根木头达成了一笔商品“交易”。')
    a('barrier', '/ˈbæriə(r)/', 'n. 屏障；障碍物；阻力；关卡；分界线；隔阂', 94,
      [('n.', '屏障；障碍物；关卡；分界线'), ('n.', '阻力；隔阂')],
      [(0, 'Concrete barriers were erected around the site.', '工地周围竖起了混凝土屏障。', 'barriers', '例', 94),
       (1, 'Unfortunately, people create inner barriers with a help of exaggerating fears.', '不幸的是，人们通过夸大恐惧来制造内心的障碍。', 'barriers', '真题', 94)],
      'barr（障碍）+ ier（名词后缀）→障碍物。')
    t.pending('barrier', 1, '原书英文为with a help of exaggerating fears，搭配疑有误；按原文保留并隔离，待人工复核。')
    a('embarrass', '/ɪmˈbærəs/', 'v. 使窘迫，使尴尬；使困惑；使为难，使陷入困境', 94,
      [('v.', '使窘迫，使尴尬'), ('v.', '使困惑；使为难，使陷入困境')],
      [(0, 'Her questions about my private life embarrassed me.', '她询问我的私生活使我感到很尴尬。', 'embarrassed', '例', 94)],
      related=[('embarrassing', 'adj. 使人尴尬的', 94), ('embarrassment', 'n. 困窘，局促不安', 94)])
    material('embarrassing', 94, '真题', english='It is financially terrifying, psychologically embarrassing.', translation='从经济上来说是可怕的，从心理上说是尴尬的。')
    material('embarrassment', 94, '真题', english='With them, there’s not the same embarrassment as when buying one carrot in a little greengrocer.', translation='有了它们，就不会像在小蔬菜水果店买一根胡萝卜那样尴尬。')
    a('embassy', '/ˈembəsi/', 'n. 大使馆；（统称）使馆官员', 94,
      [('n.', '大使馆'), ('n.', '（统称）使馆官员')],
      [(0, 'She works at the Malaysian embassy in Buenos Aires.', '她在马来西亚驻布宜诺斯艾利斯的大使馆工作。', 'embassy', '例', 94),
       (0, 'They broke off diplomatic relations and closed the embassies in each other’s country.', '两国中断外交关系，并关闭了在对方国家的大使馆。', 'embassies', '例', 94)])
    a('senator', '/ˈsenətə(r)/', 'n. 参议员', 94,
      [('n.', '参议员')],
      [(0, 'The senator was invited but was unable to attend.', '参议员受到了邀请，但是未能出席。', 'senator', '例', 94),
       (0, 'He was elected senator for Pennsylvania in 2004.', '2004年他当选宾夕法尼亚州参议员。', 'senator', '例', 94)],
      related=[('senate', 'n. 参议院', 95)])
    include_page(95)
    t.words[-1]['examples'][-1]['note'] = '英文与译文续至PDF95。'
