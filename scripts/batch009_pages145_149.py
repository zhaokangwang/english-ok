"""Visual transcription of fifth-unit words starting on PDF146–149; PDF145 is its cover."""
COMPLETE_THROUGH = 149
NEXT_WORD = 'eligible'
NEXT_PAGE = 150

def append(t, associated):
    group = '01 做好事相关词汇'
    def a(spelling, ipa, definition, page, meanings, examples, mnemonic='', related=()):
        t.add(1216 + len(t.words), spelling, ipa, definition, page, group, meanings, examples, mnemonic, related)
        t.words[-1]['book_unit_id'] = 'unit-005'
    def material(word, page, label, **kw):
        associated.append(dict(word=word, pdf_page=page, label=label, **kw))
    def include_page(page):
        w=t.words[-1]
        w['pdf_pages']=sorted(set(w['pdf_pages']+[page]))
        w['printed_pages']=[f'{p-8:03}' for p in w['pdf_pages']]

    a('merit', '/ˈmerɪt/', 'n. 优点；美德；价值；功绩', 146,
      [('n.', '价值'), ('n.', '优点'), ('n.', '美德'), ('n.', '功绩')],
      [(0, 'The plan is entirely without merit.', '这个计划毫无价值。', 'merit', '例', 146),
       (3, 'Reform has been vigorously opposed, perhaps most egregiously in education, where charter schools, academies and merit pay all faced drawn-out battles.', '改革一直遭到强烈反对，也许在教育业尤为激烈，其中特许学校、专科学院和绩效工资都面临着持久的斗争。', 'merit', '真题', 146)],
      '他身上有很多优点（merit），所以很多女生想要嫁（marry）给他。')
    t.pending('merit', 1, 'merit pay为绩效工资固定搭配，merit作名词定语；与原书功绩义的直接对应待核对，暂不训练。')
    a('virtue', '/ˈvɜːtʃuː/', 'n. 美德，优点', 146,
      [('n.', '美德'), ('n.', '优点')],
      [(0, 'He understands the traditional virtue of hard work.', '他懂得勤劳这一传统美德。', 'virtue', '例', 146),
       (1, 'The plan has the virtue of simplicity.', '这项计划的优点是简单。', 'virtue', '例', 146)],
      'vi（像罗马数字Ⅵ）+ r（联想成“花”）+ tue→六朵花→小时候我们得到的小红花越多，说明我们的“优点”和“美德”越多→优点，美德。')
    a('charity', '/ˈtʃærəti/', 'n. 慈善；慈善机构（组织）；仁爱', 146,
      [('n.', '慈善机构（组织）'), ('n.', '慈善'), ('n.', '仁爱')],
      [(0, 'Many charities sent money to help the victims of the famine.', '许多慈善机构捐款赈济饥民。', 'charities', '例', 146),
       (1, 'She does a lot of charity work.', '她做了很多慈善工作。', 'charity', '例', 146)],
      'cha（插）+ r（联想成“花”）+ ity（名词后缀）→她把平时插花挣的钱都做了“慈善”→慈善。',
      related=[('charitable', 'adj. 慈善的；宽容的', 146)])
    material('charitable',146,'真题',english='Should they become charitable corporations?',translation='它们应该成为慈善公司吗？')
    group = '02 vibrate形近词'
    a('vibrate', '/vaɪˈbreɪt/', 'v. （使）振动，颤动', 146,
      [('v.', '（使）振动，颤动')],
      [(0, 'The atmosphere seemed to vibrate with tension.', '气氛似乎紧张得发颤。', 'vibrate', '例', 146),
       (0, 'The sound of the gong was still vibrating in the air.', '锣声仍在空气中振动。', 'vibrating', '例', 146)],
      related=[('vibration', 'n. 震动，颤动；抖动；（感情的）共鸣', 146)])
    a('violent', '/ˈvaɪələnt/', 'adj. 暴力的；猛烈的', 146,
      [('adj.', '暴力的'), ('adj.', '猛烈的')],
      [(0, 'Children should not be allowed to watch violent movies.', '不应允许儿童看暴力电影。', 'violent', '例', 146),
       (0, 'The crowd suddenly turned violent.', '人群中突然有人开始大打出手。', 'violent', '例', 146)],
      related=[('violence', 'n. 暴力', 146)])
    material('violence',146,'例',english='Our organization works with victims of violence.',translation='我们的组织与暴力受害者合作。')
    material('domestic violence',146,'拓展',definition='家庭暴力')
    a('violate', '/ˈvaɪəleɪt/', 'v. 违反，违背；侵犯；亵渎', 146,
      [('v.', '违反，违背'), ('v.', '侵犯'), ('v.', '亵渎')],
      [(0, 'They were charged with violating federal law.', '他们被指控违反了联邦法律。', 'violating', '例', 146),
       (1, 'For example, it is unclear whether the sequencing of a whole genome violates the patents of individual genes within it.', '比如说，整个基因组序列是否违背了其中单个基因的专利仍无定论。', 'violates', '真题', 147)],
      '他们对无辜贫民使用暴力（violence），违反（violate）了法律的规定。')
    include_page(147)
    a('navigate', '/ˈnævɪɡeɪt/', 'v. 航行，航海；导航；正确处理，有效应对', 147,
      [('v.', '导航'), ('v.', '正确处理，有效应对'), ('v.', '航行，航海')],
      [(0, 'I’ll drive, and you can navigate.', '我开车，你引路。', 'navigate', '例', 147),
       (1, 'Many first-generation students struggle to navigate the middle-class culture of higher education.', '许多第一代大学生挣扎于应付高等教育中的中产阶级文化。', 'navigate', '真题', 147)],
      '海军（navy）乘船出门（gate）航行（navigate）。')
    group = '03 研究生的录取通知书正在summon我们哟'
    a('summon', '/ˈsʌmən/', 'v. 召唤，召集；鼓起；振作；传唤，传讯（出庭）', 147,
      [('v.', '召唤，召集'), ('v.', '传唤，传讯（出庭）'), ('v.', '鼓起；振作')],
      [(0, 'They summoned men to defend their country.', '他们召集男人来保卫国家。', 'summoned', '例', 147),
       (1, 'He was summoned to appear before the magistrates.', '他被传唤在地方法院出庭。', 'summoned', '例', 147)],
      '他们决定在夏天（summer）召集（summon）会议。')
    group = '04 挫败相关词汇'
    a('setback', '/ˈsetbæk/', 'n. 挫折，阻碍', 147,
      [('n.', '挫折，阻碍')],
      [(0, 'Don’t be put off by any early setbacks.', '不要被任何早期的挫折所拖累。', 'setbacks', '例', 147),
       (0, 'The transition from school to work can be less of a setback if the start-up adult is ready for the move.', '如果这个准成年人做好了从学校向职场过渡的准备，那么在这一转变过程中就不会那么受挫了。', 'setback', '真题', 147)])
    a('frustrate', '/frʌˈstreɪt/', 'v. 使沮丧；挫败；阻止；防止', 147,
      [('v.', '使沮丧'), ('v.', '挫败；阻止；防止')],
      [(0, 'This exam should be easy enough so as not to frustrate students.', '这次的考试应该足够容易，以免让学生感到沮丧。', 'frustrate', '例', 147),
       (1, 'The rescue attempt was frustrated by bad weather.', '营救行动因天气恶劣受阻。', 'frustrated', '例', 147)],
      'fru（联想成“妇孺”）+ st（联想成street“街道”）+ rat（老鼠）+ e→一群妇孺在街上追老鼠，能追上吗？街上人和车那么多，他们追不上→挫败。',
      related=[('frustration', 'n. 挫败，受挫', 147)])
    a('discourage', '/dɪsˈkʌrɪdʒ/', 'v. 使灰心，使泄气；阻拦，阻止', 147,
      [('v.', '阻拦，阻止'), ('v.', '使灰心，使泄气')],
      [(0, 'His parents tried to discourage him from being an actor.', '他的父母试图阻止他去当演员。', 'discourage', '例', 147),
       (0, 'A heavy rain discouraged us from moving on.', '一场大雨阻止了我们继续前进。', 'discouraged', '例', 147)],
      related=[('discouraging', 'adj. 令人沮丧的', 147), ('discouraged', 'adj. 气馁的，灰心的', 147)])
    a('encourage', '/ɪnˈkʌrɪdʒ/', 'v. 支持，鼓励，激励；刺激，鼓动', 147,
      [('v.', '支持，鼓励，激励'), ('v.', '刺激，鼓动')],
      [(0, 'She encouraged many young writers and artists.', '她鼓励了许多年轻的作家和艺术家。', 'encouraged', '例', 148),
       (1, 'Music and lighting are used to encourage shoppers to buy more.', '用音乐和灯光刺激购物者买更多的东西。', 'encourage', '例', 148)],
      'en（使）+ courage（勇气）→使你有勇气→激励，鼓励。',
      related=[('encouragement', 'n. 鼓励，鼓舞；起激励作用的事物', 148)])
    material('encouragement',148,'真题',english='If you have no friends or relatives, try to participate in several online communities, full of people who are always willing to share advice and encouragement.',translation='如果你没有朋友或亲戚，试着参加几个在线社区，那里到处都是愿意分享建议和提供鼓励的人。')
    group = '05 撤退相关词汇'
    a('retreat', '/rɪˈtriːt/', 'n. 退却，撤退；僻静处，隐居处；v. 撤退，后退', 148,
      [('v.', '撤退，后退'), ('n.', '退却，撤退'), ('n.', '僻静处，隐居处')],
      [(0, 'We retreated back down the mountain.', '我们从山上撤了下来。', 'retreated', '例', 148),
       (1, 'The retreat from predominance proved painful.', '从优势地位退出被证明是痛苦的。', 'retreat', '真题', 148)],
      're（往回，向后）+ treat（=tract，回拉）→往回拉，向后拉→撤退，后退。')
    a('withdraw', '/wɪðˈdrɔː/', 'v. 提，取（账户存款）；（使）撤回，撤离；收回', 148,
      [('v.', '提，取（账户存款）'), ('v.', '（使）撤回，撤离'), ('v.', '收回')],
      [(0, 'He has withdrawn all the money from their joint account.', '他已经从他们的联名账户中取出了所有的钱。', 'withdrawn', '例', 148),
       (1, 'The government has agreed to withdraw its troops.', '政府已经同意撤军。', 'withdraw', '例', 148)],
      'with（有）+ draw（拉）→我有钱存在银行，我想把它“提取”出来→提，取。',
      related=[('withdrawal', 'n. 提款，取款；撤走；收回', 148)])
    group = '06 代替相关词汇'
    a('replace', '/rɪˈpleɪs/', 'v. 取代，代替；替换；更换，更新', 148,
      [('v.', '取代，代替'), ('v.', '替换；更换，更新')],
      [(0, 'Teachers will never be replaced by computers in the classroom.', '在教室里，电脑永远不会取代老师。', 'replaced', '例', 148),
       (1, 'American manufacturing still needs to replace tens of thousands of retiring boomers every year.', '美国制造业每年仍需要替换数以万计的即将退休的婴儿潮一代人。', 'replace', '真题', 148)],
      related=[('replacement', 'n. 更换，替换；替代的人或物', 148)])
    a('displace', '/dɪsˈpleɪs/', 'v. 取代，替代', 148,
      [('v.', '取代，替代')],
      [(0, 'Gradually factory workers have been displaced by machines.', '工厂的工人已逐渐被机器取代。', 'displaced', '例', 148),
       (0, 'The Industrial Revolution didn’t go so well for Luddites whose jobs were displaced by mechanized looms.', '工业革命对那些工作被机械织布机取代的卢德派来说不太友好。', 'displaced', '真题', 148)],
      related=[('displacement', 'n. 取代，替代；移位；免职', 148)])
    a('pierce', '/pɪəs/', 'v. 穿透，刺破，扎', 149,
      [('v.', '穿透，刺破，扎')],
      [(0, 'The arrow pierced his shoulder.', '箭射入他的肩膀。', 'pierced', '例', 149),
       (0, 'She was pierced to the heart with guilt.', '她万般愧疚，心如刀割。', 'pierced', '例', 149)],
      '一块玻璃碎片（piece）刺破（pierce）了他的手掌。')
    t.pending('pierce', 1, '本句为使内心痛苦的比喻用法，原书只列穿透、刺破、扎；不直接训练字面义，待补义核对。')
    group = '07 完成相关词汇'
    a('accomplish', '/əˈkʌmplɪʃ/', 'v. 完成', 149,
      [('v.', '完成')],
      [(0, 'The first part of the plan has been accomplished.', '计划的第一部分已完成。', 'accomplished', '例', 149),
       (0, 'Universal history, the history of what man has accomplished in this world, is at bottom the History of the Great Men who have worked here.', '世界历史就是人类在这个世界上取得的成就的历史，实质上也就是在世界上活动的伟人的历史。', 'accomplished', '真题', 149)],
      related=[('accomplished', 'adj. 熟练的，技艺高超的', 149), ('accomplishment', 'n. 成就；完成', 149)])
    material('accomplished',149,'例',english='Sarah had become accomplished at running the house.',translation='萨拉已能老练地操持家务了。')
    a('achieve', '/əˈtʃiːv/', 'v. （凭长期努力）达到（某目标、地位、标准）', 149,
      [('v.', '（凭长期努力）达到（某目标、地位、标准）')],
      [(0, 'She has worked hard to achieve her goal.', '她努力工作来实现她的目标。', 'achieve', '例', 149),
       (0, 'Sooner or later our shared efforts will achieve results.', '我们的共同努力迟早会取得成果。', 'achieve', '例', 149)],
      related=[('achievement', 'n. 成就；完成；成绩', 149)])
    material('achievement',149,'真题',english='This is the gap that must be narrowed to close the achievement gap.',translation='这正是弥合成就差距所必须缩小的缺口。')
    a('fulfil', '/fʊlˈfɪl/', 'v. 实现；符合；履行，执行', 149,
      [('v.', '符合'), ('v.', '实现'), ('v.', '履行，执行')],
      [(0, 'No candidate fulfils all the criteria for this position.', '没有一个候选人完全符合这个职位要求。', 'fulfils', '例', 149),
       (1, 'Traditionally, this role was fulfilled by data banks, libraries, and other humans.', '传统上，这个角色是由数据库、图书馆和其他人来实现的。', 'fulfilled', '真题', 149)],
      'ful（满）+ fil（满）→满上加满，这件事非常圆满→实现。')
    t.words[-1]['notes'].append('原书并列美式拼写fulfill，主词保留fulfil，不另建重复词。')
    group = '08 资格相关语境词汇'
    a('qualify', '/ˈkwɒlɪfaɪ/', 'v. 使具备资格；取得资格（或学历）；合格', 149,
      [('v.', '取得资格（或学历）'), ('v.', '使具备资格'), ('v.', '合格')],
      [(0, 'He qualified as a doctor last year.', '他去年获得了医生的资格。', 'qualified', '例', 149),
       (1, 'This training course will qualify you for a better job.', '本培训课程将使你能胜任更好的工作。', 'qualify', '例', 149)],
      'qualify字面意思就是“使……有质量”，使你有质量当老师，那就是“使你有资格”当老师→使具备资格。',
      related=[('qualified', 'adj. 具备……的学历（或资历）；具备……的知识（或技能）；符合资格', 149), ('qualification', 'n. 资格，学历', 150)])
    include_page(150)
    material('qualified',150,'例',english='She’s extremely well qualified for the job.',translation='她完全符合承担这项工作的条件。')
