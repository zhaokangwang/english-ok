"""Visual transcription of fourth-unit headwords beginning on PDF140–144."""
COMPLETE_THROUGH = 144
NEXT_WORD = 'merit'
NEXT_PAGE = 146
CONTEXT_PAGES_REVIEWED = [145]

def append(t, associated):
    group = '37 sw-相关词汇'
    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(1216+len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-004'
    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))
    def include_page(page):
        w=t.words[-1]
        w['pdf_pages']=sorted(set(w['pdf_pages']+[page]))
        w['printed_pages']=[f'{p-8:03}' for p in w['pdf_pages']]

    a('swear', '/sweə(r)/', 'v. 宣誓，发誓；咒骂，诅咒；郑重承诺', 140,
      [('v.', '咒骂，诅咒'), ('v.', '宣誓，发誓；郑重承诺')],
      [(0, 'I don’t like to hear children swearing.', '我不喜欢听到孩子们骂人。', 'swearing', '例', 140),
       (1, 'She made him swear not to tell anyone.', '她要他发誓不告诉任何人。', 'swear', '例', 140)],
      '在法院上宣誓（swear）时，应该注意自己的穿着（wear）。')
    group = '38 sc-相关词汇'
    a('scream', '/skriːm/', 'v. 尖叫，高声喊，大声叫', 140,
      [('v.', '尖叫，高声喊，大声叫')],
      [(0, 'The kids were screaming with excitement.', '孩子们兴奋地喊叫着。', 'screaming', '例', 140),
       (0, 'The man screamed in agony and collapsed.', '那个人痛苦地尖叫着，倒下了。', 'screamed', '例', 140)],
      '她过生日时，同事们把奶油（cream）抹到她的脸上，她激动地尖叫（scream）起来。')
    a('scold', '/skəʊld/', 'v. 责骂，训斥', 140,
      [('v.', '责骂，训斥')],
      [(0, 'He scolded them for arriving late.', '他嫌他们迟到，训了他们一通。', 'scolded', '例', 140),
       (0, 'In the 2006 film version of The Devil Wears Prada, Miranda Priestly scolds her unattractive assistant for imagining that high fashion doesn’t affect her.', '在2006年电影版《穿普拉达的女王》中，米兰达·普利斯特利斥责自己毫不引人注目的助理，因为她认为高端时尚与自己无关。', 'scolds', '真题', 140)],
      '他们入住的酒店太冷（cold）了，他们忍不住跑到前台去训斥（scold）酒店经理。')
    a('scorn', '/skɔːn/', 'n. & v. 轻蔑，鄙视', 140,
      [('v.', '轻蔑，鄙视'), ('n.', '轻蔑，鄙视')],
      [(0, 'Such methods are scorned by reputable practitioners.', '这种方法受到声誉良好的从业者的蔑视。', 'scorned', '例', 140),
       (0, 'Homework has never been terribly popular with students and even many parents, but in recent years it has been particularly scorned.', '家庭作业从来就没有受到学生甚至是许多家长的特别欢迎，而近年来更是备受贬损。', 'scorned', '真题', 140)],
      '他们不应该鄙视（scorn）种玉米（corn）的农民。')
    a('scare', '/skeə(r)/', 'v. 吓唬；使惊恐，害怕；n. 恐慌，恐惧，惊恐', 140,
      [('v.', '吓唬；使惊恐，害怕'), ('n.', '恐慌，恐惧，惊恐')],
      [(0, 'It scared me to think I was alone in the building.', '想到楼里只有我一个人，怪害怕的。', 'scared', '例', 140),
       (1, 'Constant health scares just end up with no one listening.', '持续不断的健康恐吓最终只会无人听信。', 'scares', '真题', 140)],
      '你要好好照顾（care）你的弟弟，不要动不动吓唬（scare）他。',
      [('scary', 'adj. 恐怖的，吓人的', 140), ('scared', 'adj. 害怕的，恐慌的', 140)])
    t.pending('scare', 1, 'health scares原译“健康恐吓”语义存疑，保留原文原译，暂不进入学习队列。')
    group = '39 sp-相关词汇'
    a('sprout', '/spraʊt/', 'v. 发芽，长芽；出现；长出', 141,
      [('v.', '发芽，长芽'), ('v.', '出现；长出')],
      [(0, 'The seeds will sprout in a few days.', '这些种子几天后就会发芽。', 'sprout', '例', 141),
       (1, 'Hundreds of mushrooms had sprouted up overnight.', '一夜之间长出来好几百朵蘑菇。', 'sprouted', '例', 141)],
      'spr（联想成spring“春天”）+ out（出来）→春天来了，嫩芽就出来了→发芽。')
    a('spite', '/spaɪt/', 'n. 恶意，怨恨', 141,
      [('n.', '恶意，怨恨')],
      [(0, 'She was angry and full of spite.', '她怒气冲冲，满怀怨恨。', 'spite', '例', 141)],
      related=[('spiteful', 'adj. 恶意的', 141)])
    material('in spite of', 141, '拓展', definition='尽管，不管')
    material('in spite of', 141, '真题',
      english='In spite of “endless talk of difference”, American society is an amazing machine for homogenizing people.',
      translation='尽管人们“没完没了地谈论差异”，但美国社会是一台使人们同化的神奇机器。',
      reason='固定短语in spite of为尽管义，未挂到spite主词恶意或怨恨义。')
    a('spray', '/spreɪ/', 'n. 浪花，水花；喷雾，喷雾剂；v. 喷（洒），（使）溅散；扫射', 141,
      [('n.', '浪花，水花'), ('n.', '喷雾，喷雾剂'), ('v.', '喷（洒），（使）溅散'), ('v.', '扫射')],
      [(0, 'Spray flew up onto the rocks.', '水花飞溅到岩石上。', 'Spray', '例', 141),
       (2, 'In a Swiss study, researchers sprayed oxytocin into the noses of half the subjects.', '在瑞士的一项研究中，研究人员将催产素喷入一半受试者的鼻腔中。', 'sprayed', '真题', 141)],
      '家里的很多喷雾剂（spray）上都有这个词，在靠近喷嘴的地方。')
    a('pray', '/preɪ/', 'v. 祈祷；祷告；企盼', 141,
      [('v.', '祈祷；祷告'), ('v.', '企盼')],
      [(0, 'They knelt down and prayed.', '他们跪下来祷告。', 'prayed', '例', 141),
       (0, 'I’ll pray for you.', '我将为你祈祷。', 'pray', '例', 141)],
      '哪怕只有一线（ray）希望，他们也会祈祷（pray）。')
    a('prey', '/preɪ/', 'n. 猎物，受害者；v. （～on）捕食；欺凌，坑骗', 141,
      [('n.', '受害者'), ('n.', '猎物'), ('v.', '（～on）捕食'), ('v.', '欺凌，坑骗')],
      [(0, 'Elderly people are easy prey for dishonest salesmen.', '老年人容易上狡诈推销员的当。', 'prey', '例', 141),
       (1, 'The young deer are ideal prey for the leopard.', '小鹿是豹的理想猎物。', 'prey', '例', 141)],
      'p（联想成“扑”）+ rey（联想成“弱”）→弱小的动物很容易就被大型动物扑倒，成为“猎物”→猎物。')
    a('array', '/əˈreɪ/', 'n. 大群，大量；数组；阵列；v. 排列；布置', 141,
      [('n.', '大群，大量'), ('n.', '数组；阵列'), ('v.', '排列；布置')],
      [(0, 'Her writing covers a wide array of topics.', '她的作品涵盖的主题十分广泛。', 'array', '例', 141),
       (0, 'These two academics use an array of behavioral research to show that the most rewarding ways to spend money can be counterintuitive.', '这两位学者利用一系列的行为研究表明，最让人受益的消费方式可能是与直觉相反的。', 'array', '真题', 141)],
      '在光线（ray）下排列（array）好这些物品。')
    group = '40 fierce形近词'
    a('fierce', '/fɪəs/', 'adj. 凶猛的；强烈的，猛烈的；狂暴的；狂热的', 142,
      [('adj.', '凶猛的'), ('adj.', '强烈的，猛烈的'), ('adj.', '狂暴的'), ('adj.', '狂热的')],
      [(0, 'Two fierce eyes glared at them.', '一双凶狠的眼睛瞪着他们。', 'fierce', '例', 142),
       (1, 'Any threat of monopoly, they argue, is removed by fierce competition from trucks.', '他们认为，在公路运输的激烈竞争面前，垄断的威胁已经不复存在。', 'fierce', '真题', 142)],
      '发音类似“飞蛾死”→飞蛾扑火而死→扑火很激烈→狂热的；凶猛的。',
      [('fiercely', 'adv. 恶劣地；猛烈地', 142)])
    material('fiercely', 142, '例', english='The chimney was smoking fiercely.', translation='烟囱猛烈地冒着烟。')
    a('fearful', '/ˈfɪəfl/', 'adj. 担心的；可怕的', 142,
      [('adj.', '担心的'), ('adj.', '可怕的')],
      [(0, 'Parents are ever fearful for their children.', '父母总是为子女担忧。', 'fearful', '例', 142),
       (0, 'They were understandably fearful about the future.', '可以理解，他们对未来感到恐惧。', 'fearful', '例', 142)],
      '发音类似“飞蛾恐”→飞蛾忽然飞过来，吓了我一大跳→可怕的。')
    group = '41 胆小、威胁相关词汇'
    a('coward', '/ˈkaʊəd/', 'n. 懦夫，胆小鬼', 142,
      [('n.', '懦夫，胆小鬼')],
      [(0, 'I’m a real coward when it comes to going to the dentist.', '我一去看牙医就胆战心惊。', 'coward', '例', 142),
       (0, 'You coward! What are you afraid of?', '你这胆小鬼！你怕什么呢？', 'coward', '例', 142)])
    a('timid', '/ˈtɪmɪd/', 'adj. 胆小的；羞怯的', 142,
      [('adj.', '胆小的'), ('adj.', '羞怯的')],
      [(0, 'Deer are naturally timid creatures.', '鹿是天生胆小的动物。', 'timid', '例', 142),
       (0, 'Timid children need careful handling to build up their confidence.', '胆小的孩子需要小心的对待来建立他们的信心。', 'Timid', '例', 142)])
    a('intimidate', '/ɪnˈtɪmɪdeɪt/', 'v. 威胁，恐吓', 142,
      [('v.', '威胁，恐吓')],
      [(0, 'She refused to be intimidated by their threats.', '她没有被他们的威胁吓倒。', 'intimidated', '例', 142),
       (0, 'He was not a man to be easily intimidated.', '他不是一个能被轻易吓倒的人。', 'intimidated', '例', 142)],
      '他是个欺软怕硬的人，只会欺负和威胁（intimidate）胆小的（timid）人。',
      [('intimidation', 'n. 威胁，恐吓', 142)])
    material('intimidation', 142, '真题',
      english='It’s more likely to be associated with dominance or intimidation in adversarial situations.',
      translation='在敌对场合，它更可能与控制或恐吓有关。')
    a('threat', '/θret/', 'n. 恐吓，威胁；凶兆；构成威胁的人（或事物）', 142,
      [('n.', '恐吓，威胁'), ('n.', '凶兆'), ('n.', '构成威胁的人（或事物）')],
      [(0, 'Many wild plants are under threat of extinction.', '许多野生植物面临灭绝的危险。', 'threat', '例', 142),
       (0, 'Scientists in one wave after another try to awaken us to the growing threat of global warming.', '科学家们前赴后继地试图唤醒我们认识到全球变暖正在带来日益严重的威胁。', 'threat', '真题', 142)],
      related=[('threaten', 'v. 恐吓，威胁；预示凶兆，有……危险', 143)])
    include_page(143)
    material('threaten', 143, '真题',
      english='The crash was a major reason the U.S. Fish and Wildlife Service (USFWS) decided to formally list the bird as threatened.',
      translation='这种鸟的数量锐减是美国鱼类和野生动物管理局（USFWS）决定正式将其列为受威胁物种的主要原因。')
    a('frighten', '/ˈfraɪtn/', 'v. 使惊吓，使惊恐', 143,
      [('v.', '使惊吓，使惊恐')],
      [(0, 'Sorry, I didn’t mean to frighten you.', '对不起，我没有吓唬你的意思。', 'frighten', '例', 143),
       (0, 'It frightened him that she could see so easily into his private thoughts.', '她能如此轻易地看穿他的私人想法，这使他感到害怕。', 'frightened', '例', 143)],
      '他说他要跟你打架（fight），其实只是吓唬（frighten）你。',
      [('frightened', 'adj. 惊吓的，受惊的', 143)])
    material('frightened', 143, '例', english='What are you frightened of?', translation='你怕什么？')
    a('terror', '/ˈterə(r)/', 'n. 惊恐，恐惧；恐怖，恐怖行动', 143,
      [('n.', '惊恐，恐惧'), ('n.', '恐怖，恐怖行动')],
      [(0, 'Her eyes were wild with terror.', '她的眼睛里充满了恐惧。', 'terror', '例', 143),
       (1, 'These street gangs have become the terror of the neighbourhood.', '这些街头少年团伙使得周围邻里谈之色变。', 'terror', '例', 143)],
      '发音类似“太弱”→一个国家的政府太软弱，恐怖分子可能就很猖狂→恐怖行动，恐怖。',
      [('terrorist', 'n. 恐怖分子', 143)])
    t.pending('terror', 1, 'terror在本句指令人恐惧的人或事物，原书未明确列该名词义，暂不直接挂到恐怖行动义。')
    a('terrify', '/ˈterɪfaɪ/', 'v. 使恐惧，使十分害怕；使惊吓', 143,
      [('v.', '使恐惧，使十分害怕；使惊吓')],
      [(0, 'Flying terrifies her.', '她害怕坐飞机。', 'terrifies', '例', 143),
       (0, 'Stop it! You’re terrifying the children!', '住手！你吓着孩子们了！', 'terrifying', '例', 143)],
      'terri（想成terror“恐怖”）+ fy（动词后缀“使……”）→使……害怕→恐惧，威胁。')
    a('rebel', 'n. /ˈrebl/; v. /rɪˈbel/', 'n. 造反者，叛乱者；叛逆者；v. 造反，反抗', 143,
      [('n.', '造反者，叛乱者'), ('n.', '叛逆者'), ('v.', '造反，反抗')],
      [(2, 'Most teenagers find something to rebel against.', '大多数青少年都有反抗意识。', 'rebel', '例', 143),
       (2, 'The colonies rebelled and declared their independence.', '各殖民地起来反抗并宣布独立。', 'rebelled', '例', 143)],
      're（反复）+ bel（联想成bell“铃”）→政府反复地敲铃，提醒百姓们城里有“叛乱者”→叛乱者。',
      [('rebellious', 'adj. 造反的；叛逆的', 143), ('rebellion', 'n. 谋反，叛乱；叛逆', 143)])
    include_page(144)
    material('rebellious', 143, '真题',
      english='The participants filled out questionnaires about how often they did things that were altruistic and positive, like sacrificing their own interests to help a friend, or rebellious and negative, like getting drunk or staying out late.',
      translation='参与者填写了问卷，问卷内容是关于他们做利他的、积极的事情（例如牺牲自己的利益帮助朋友）的频率，以及做叛逆的、消极的事情（例如醉酒或晚归）的频率。')
    material('rebellion', 143, '例',
      english='At the start of the rebellion he pledged to kill his father’s enemies.',
      translation='叛乱开始时，他发誓要杀死他父亲的敌人。', continuation_pdf_pages=[144])
    group = '42 冒险相关词汇'
    a('hazard', '/ˈhæzəd/', 'n. 危险，危害；v. 冒……的风险', 144,
      [('n.', '危险，危害'), ('v.', '冒……的风险')],
      [(0, 'Growing levels of pollution represent a serious health hazard to the local population.', '日益严重的污染对当地人民的健康构成了重大威胁。', 'hazard', '例', 144),
       (0, 'Everybody is aware of the hazards of smoking.', '大家都明白吸烟的危害。', 'hazards', '例', 144)])
    a('stake', '/steɪk/', 'n. 桩；赌注；股份；重大利益关系；v. 以……打赌，拿……冒险', 144,
      [('n.', '桩'), ('n.', '赌注'), ('n.', '股份'), ('n.', '重大利益关系'), ('v.', '以……打赌'), ('v.', '拿……冒险')],
      [(2, 'She acquired a 4 per cent direct stake in the company.', '她获得了该公司4%的直接股份。', 'stake', '例', 144),
       (5, 'She staked her political career on tax reform, and lost.', '她把自己的政治前程押在税制改革上，结果赌输了。', 'staked', '例', 144)],
      's（蛇）+ take（拿）→拿蛇玩，是冒着很大危险的→拿……冒险。')
    material('at stake', 144, '拓展', definition='成败难料；得失都可能；有风险')
    a('trap', '/træp/', 'v. 使落入险境，使陷入困境；n. （捕捉动物的）陷阱；圈套；诡计；困境', 144,
      [('v.', '使落入险境，使陷入困境'), ('n.', '（捕捉动物的）陷阱'), ('n.', '圈套；诡计'), ('n.', '困境')],
      [(0, 'We became trapped by the rising floodwater.', '我们被上涨的洪水困住了。', 'trapped', '例', 144),
       (2, 'She had set a trap for him and he had walked straight into it.', '她给他设下圈套，他就径直钻了进去。', 'trap', '例', 144)],
      '他们去山区旅行（trip），结果被大雪困在（trap）了山里。')
    a('strap', '/stræp/', 'n. 带子；v. 用带子系好', 144,
      [('n.', '带子'), ('v.', '用带子系好')],
      [(0, 'The bag comes with detachable straps.', '这种包有可拆卸的带子。', 'straps', '例', 144),
       (1, 'Are you strapped in?', '您系好安全带了吗？', 'strapped', '例', 144)],
      '她用带子（strap）做了一个小陷阱（trap）。')
