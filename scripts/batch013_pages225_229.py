"""Visual transcription of seventh-unit headwords beginning on PDF225–229."""
COMPLETE_THROUGH = 229
NEXT_WORD = 'session'
NEXT_PAGE = 230

def append(t,associated):
    group='36 “contribute”近义词及形近词'
    def a(spelling,ipa,definition,page,meanings,examples,mnemonic='',related=()):
        t.add(2314+len(t.words),spelling,ipa,definition,page,group,meanings,examples,mnemonic,related)
        t.words[-1]['book_unit_id']='unit-007'
    def material(word,page,label,**kw):
        associated.append(dict(word=word,pdf_page=page,label=label,**kw))
    def include_page(page):
        w=t.words[-1];w['pdf_pages']=sorted(set(w['pdf_pages']+[page]))
        w['printed_pages']=[f'{p-8:03}' for p in w['pdf_pages']]

    a('attribute','/əˈtrɪbjuːt/ v.; /ˈætrɪbjuːt/ n.','v. 把……归因于；认为是……所为；n. 属性；性质；特征',225,
      [('n.','属性；性质；特征'),('v.','把……归因于；认为是……所为')],
      [(0,'They appeared to possess all the attributes of a ruling class.','他们似乎具有统治阶级的一切特征。','attributes','例',225),
       (1,'I attribute my success to this: I never gave or took an excuse.','我把我的成功归功于这一点：我从不找借口，也绝不接受借口。','attribute','例',225)],
      'at（表示“加强”）+ tribut（给）+ e→一直要求给原因→把……归因于。')
    a('distribute','/dɪˈstrɪbjuːt/','v. 分发；分配；分散',225,
      [('v.','分配'),('v.','分发'),('v.','分散')],
      [(0,'We need to find new ways to distribute food so no child goes to bed hungry.','我们需要找到新的方法来分配食物，让孩子们不会饿着肚子睡觉。','distribute','例',225),
       (1,'The newspaper is distributed free.','本报免费派发。','distributed','例',225)],
      'dis（= apart分开）+ tribut（给）+ e→分开给→分配。')
    a('retribution','/ˌretrɪˈbjuːʃn/','n. 惩罚，报应',225,
      [('n.','惩罚，报应')],
      [(0,'Evil actions will bring retribution.','恶行会有恶报。','retribution','例',225),
       (0,'People are seeking retribution for the latest terrorist outrages.','人们在设法对恐怖分子最近的暴行进行严惩。','retribution','例',225)],
      're（回来）+ tribut（给）+ ion（名词后缀）→给回来→惩罚，报应。')
    a('repay','/rɪˈpeɪ/','v. 偿还，归还；报答，回报',225,
      [('v.','偿还，归还'),('v.','报答，回报')],
      [(0,'Then, he can choose to turn to the bank for a loan to pay his way through university, which he can repay after graduation.','然后，他可以选择向银行贷款，以支付大学学费，并在毕业后偿还。','repay','例',225),
       (0,'I’ll repay the money I owe them next week.','我将在下个星期偿还欠他们的钱。','repay','例',225)],
      're（表示“回来”）+ pay（支付，付款）→归还；回报。')
    group='37 “accord”相关形近词'
    a('accord','/əˈkɔːd/','n. 协议；条约；v. （~to）相符合，相一致',225,
      [('n.','协议；条约'),('v.','（~to）相符合，相一致')],
      [(0,'The two sides signed a peace accord last July.','在刚过去的七月，双方签订了和平条约。','accord','例',225),
       (1,'His actions and his principles always accord well.','他的行为和他的原则总是很一致。','accord','例',225)],
      '发音类似“鹅烤得”→我们“一致”认为鹅烤得很好吃→相一致。')
    material('in accord with',225,'拓展',definition='与……一致（或相符合）')
    material('in accordance with',225,'拓展',definition='按照，依据',english='It is an obvious truism that people act in accordance with their motives.',translation='人人都按自己的动机行事是不言而喻的。')
    a('accordingly','/əˈkɔːdɪŋli/','adv. 相应地；因此，所以',225,
      [('adv.','相应地'),('adv.','因此，所以')],
      [(0,'As the economy develops, the living conditions of the people have been improved accordingly.','随着经济的发展，人民的生活水平也提高了。','accordingly','例',225),
       (0,'So, adapt your style accordingly to type.','因此，请根据类型调整你的方式。','accordingly','真题',226)])
    include_page(226)
    a('regard','/rɪˈɡɑːrd/','v. 把……看作是；注视，凝视；n. 注意；关心；尊重；问候，致意',226,
      [('v.','把……看作是'),('v.','注视，凝视'),('n.','注意；关心'),('n.','尊重'),('n.','问候，致意')],
      [(0,'I regard you as my best friend.','我把你看作是我最好的朋友。','regard','例',226),
       (0,'This is why researchers generally regard so-called moral guilt, in the right amount, to be a good thing.','这就是为什么研究人员普遍认为适量的所谓道德内疚是一件好事。','regard','真题',226)],
      related=[('regarding','prep. 关于，至于',226)])
    material('regardless of',226,'拓展',definition='不管；不顾',english='Regardless of his financial conditions, he buys anything he wants.',translation='他根本不顾及自己的经济状况，只要是他想买的他就会买。')
    material('regarding',226,'派生',phonetic='/rɪˈɡɑːdɪŋ/',definition='prep. 关于，至于')
    material('regarding',226,'真题',english='It may just encourage people to talk more honestly about their feelings regarding race issues.',translation='它可能只是鼓励人们更诚实地谈论他们对种族问题的感受。')
    group='38 “anticipate”相关形近词'
    a('antique','/ænˈtiːk/','adj. 古代的；古老的；n. 有价值的古物，古董',226,
      [('n.','有价值的古物，古董'),('adj.','古代的；古老的')],
      [(0,'They found the antiques there more valuable.','他们发现那里的古董更有价值。','antiques','例',226),
       (0,'Priceless antiques were destroyed in the fire.','价值连城的古董在大火中焚毁。','antiques','例',226)],
      '发音类似“俺提个”→俺提个“古董”，给老丈人送去啊，他就喜欢这种东西→古董。')
    a('anticipate','/ænˈtɪsɪpeɪt/','v. 预期，期望；预见',226,
      [('v.','预见'),('v.','预期，期望')],
      [(0,'He anticipated something unusual would happen.','他预感到不寻常的事将要发生。','anticipated','例',226),
       (0,'Do not try to anticipate your fate unless you spare no efforts to do it.','除非你全力以赴去做，否则不要试图去预测自己的命运。','anticipate','例',226)],
      related=[('anticipation','n. 预期，预料',226)])
    material('anticipation',226,'派生',phonetic='/ænˌtɪsɪˈpeɪʃn/',definition='n. 预期，预料')
    a('participate','/pɑːˈtɪsɪpeɪt/','v. 参与，参加',226,
      [('v.','参与，参加')],
      [(0,'Over half of the staff in the company participate in strike.','这个公司一半以上的人参加了罢工。','participate','例',226)],
      'parti（联想成party“聚会”）+ cip+ ate（动词后缀）→我们一起“参加”聚会→参与，参加。',
      [('participant','n. 参与者',226)])
    t.pending('participate',0,'原书participate in strike疑缺冠词，保留原文原译待核。')
    material('participant',226,'派生',phonetic='/pɑːˈtɪsɪpənt/',definition='n. 参与者')
    material('participant',226,'例',english='Companies are active participants in technical cooperation.',translation='各家公司积极参与技术合作。')
    group='39 “喜爱、崇拜”相关词汇'
    a('adore','/əˈdɔː(r)/','v. 崇拜，爱慕；喜爱，热爱',226,
      [('v.','喜爱，热爱'),('v.','崇拜，爱慕')],
      [(0,'She adores working with children.','她热爱参与儿童工作。','adores','例',227)],
      'ad（表示“加强”）+ ore（联想成core“核心”）→一般大家非常“崇拜”的人都是某个领域的核心人物→崇拜，爱慕。',
      [('adorable','adj. 可爱的；招人喜欢的',227)])
    material('adorable',227,'派生',phonetic='/əˈdɔːrəbl/',definition='adj. 可爱的；招人喜欢的')
    a('worship','/ˈwɜːʃɪp/','n. & v. 崇拜；热爱；爱慕',227,
      [('v.','热爱；爱慕'),('v.','崇拜'),('n.','崇拜；热爱；爱慕')],
      [(0,'She worships her children.','她极度疼爱自己的儿女。','worships','例',227),
       (1,'Blindly worshipping those physically attractive individuals exerts bad influence on the study of youngsters.','盲目崇拜那些颜值高的人给年轻人的学习带来了不好的影响。','worshipping','例',227)],
      '普通人看见军舰（warship），会张大嘴巴（嘴巴形似O），露出崇拜（worship）的眼神。')
    group='40 “-sert-”相关词汇'
    a('assert','/əˈsɜːt/','v. 断言，声称',227,
      [('v.','断言，声称')],
      [(0,'Her friends asserted that she was innocent.','她的朋友断言她是无罪的。','asserted','例',227),
       (0,'The Administration was in essence asserting that because it didn’t want to carry out Congress’s immigration wishes, no state should be allowed to do so either.','实际上，政府声称：因为它不想执行国会的移民意愿，所以其他州也不应被允许执行。','asserting','真题',227)],
      'as（表示加强）+ sert（加入，插入）→一再地插入观点→断言。',
      [('assertive','adj. 断言的；确定的',227)])
    material('assertive',227,'派生',phonetic='/əˈsɜːtɪv/',definition='adj. 断言的；确定的')
    a('desert','/dɪˈzɜːt/ v.; /ˈdezət/ n.','v. 离开；抛弃；放弃；n. 沙漠',227,
      [('v.','离开；抛弃；放弃'),('n.','沙漠')],
      [(0,'Pull down the deserted shopping mall.','拆除废弃的购物中心。','deserted','例',227),
       (1,'He drove off into the desert.','他驾车进入了沙漠。','desert','例',227)],
      'de（否定）+ sert（加入，插入）→不再加入→离开，抛弃。')
    a('dessert','/dɪˈzɜːt/','n. 餐后甜点，甜食',227,
      [('n.','餐后甜点，甜食')],
      [(0,'We finished off with a dessert of honey and nuts.','我们最后吃了蜂蜜果仁甜点。','dessert','例',227),
       (0,'Jack learned his trade from a famous dessert chef in Paris.','杰克是从巴黎一位著名的甜点师那里学会了他的手艺。','dessert','例',227)],
      '在沙漠（desert）里如果能吃到甜点（dessert），那该多好啊！')
    a('insert','/ɪnˈsɜːt/','v. 插入，嵌进；添加',227,
      [('v.','插入，嵌进'),('v.','添加')],
      [(0,'They inserted a tube in his mouth to help him breathe.','他们在他嘴里插了根导管帮助他呼吸。','inserted','例',227),
       (1,'The program will automatically insert the replacement text.','程序将自动插入替代文本。','insert','例',227)],
      'in（进入）+ sert（插入）→“插入”进来→插入，嵌进。',
      [('insertion','n. 插入',227)])
    material('insertion',227,'派生',phonetic='/ɪnˈsɜːʃn/',definition='n. 插入')
    group='41 “虫”相关词汇'
    a('insect','/ˈɪnsekt/','n. 昆虫',228,
      [('n.','昆虫')],
      [(0,'On the road there is little to protect them from mud, insects, and bird droppings.','在路上，几乎没有什么能保护它们免受泥土、昆虫和鸟粪的伤害。','insects','例',228),
       (0,'Most birds spend most of the day eating insects.','大多数鸟一天大部分时间都在吃昆虫。','insects','例',228)],
      'in（入，向内）+ sect（切割）→这只“昆虫”的纹理看上去是一段一段的，像被切割过一样→昆虫。')
    a('worm','/wɜːm/','n. 蠕虫；懦夫',228,
      [('n.','蠕虫'),('n.','懦夫')],
      [(0,'To wriggle is to wrest about like a worm.','蠕动就是像蠕虫一样扭来扭去。','worm','例',228),
       (0,'Worms burrow down into the soil.','蠕虫往土里钻。','Worms','例',228)],
      '发音类似“乌木”→乌木受潮了，里面长了很多虫子→蠕虫。')
    t.pending('worm',0,'原书wrest about用语疑误，保留原文原译待核。')
    group='42 “-tract-”相关词汇'
    a('abstract','/ˈæbstrækt/ n., adj.; /æbˈstrækt/ v.','n. 摘要，概要；adj. 抽象（派）的；v. 提炼，提取',228,
      [('n.','摘要，概要'),('adj.','抽象（派）的'),('v.','提炼，提取')],
      [(0,'He wrote an abstract of a long article.','他为一篇长文章写了摘要。','abstract','例',228),
       (1,'He is an abstract painter.','他是一个抽象派画家。','abstract','例',228),
       (2,'They can abstract precious medicines from ordinary substances.','他们能从普通物质中提取珍贵药物。','abstract','例',228)],
      'ab（表示“强调”）+ s + tract（拽，拉）→重复地拽、拉→提取，提炼。')
    a('tractor','/ˈtræktə(r)/','n. 拖拉机',228,
      [('n.','拖拉机')],
      [(0,'What’s needed to build a complex airliner or a tractor?','建造一架复杂的客机或拖拉机需要什么？','tractor','例',228)],
      'tract（拖，拉）+ or（名词词缀）→能拖拉东西的车→拖拉机。')
    a('subtract','/səbˈtrækt/','v. 减去，扣除',228,
      [('v.','减去，扣除')],
      [(0,'We have subtracted $25 per adult to arrive at a basic room rate.','我们已给每位成人房客减去了25美元，这就是基本的房费价格了。','subtracted','例',228)],
      'sub（表示“往下”）+ tract（拽，拉）→往下拽→减去，扣除。')
    a('extract','/ˈekstrækt/；/ɪkˈstækt/ v.; /ˈekstrækt/ n.','v. 抽出，拔出；提取；提炼；n. 提取物，摘录；选录',228,
      [('v.','提取；提炼'),('n.','摘录；选录'),('v.','抽出，拔出'),('n.','提取物')],
      [(0,'Corporate profits increasingly rely on extracting value from the public.','企业的利润越来越依赖于从公众那里获取价值。','extracting','例',228),
       (1,'The following extract is taken from her new novel.','下面一段摘自她的新小说。','extract','例',228)],
      'ex（表示“往外”）+ tract（拽，拉）→往外拽→抽出，拔出→提取，摘录。')
    t.words[-1]['notes'].append('原书extract动词音标印为/ɪkˈstækt/，疑漏r，按扫描页保留待音标复核。')
    a('contract','/ˈkɒntrækt/ n.; /kənˈtrækt/ v.','n. 合同，契约；v. 与……订立合同（或契约）；缩小',228,
      [('v.','与……订立合同（或契约）'),('n.','合同，契约'),('v.','缩小')],
      [(0,'Several computer engineers have been contracted to the finance department.','有几位计算机工程师与财务部门签订了合同。','contracted','例',229),
       (1,'I was on a three-year contract that expired last week.','我签订的三年期合同已于上周期满。','contract','例',229)],
      'con（所有的）+ tract（拽，拉）→一起拽，大家都往有利于自己利益的方向拽，需要一个“合同，契约”。',
      [('contractor','n. 承包人，承包商；承包公司',229)])
    material('contractor',229,'派生',phonetic='/kənˈtræktə(r)/',definition='n. 承包人，承包商；承包公司')
    a('attract','/əˈtrækt/','v. 吸引；引起；招引',229,
      [('v.','吸引；引起；招引')],
      [(0,'All the key words in the article are printed in bold type so as to attract readers’ attention.','文章中所有的关键词都是用粗体字体印刷的，以吸引读者的注意。','attract','例',229),
       (0,'What first attracted me to her was her sense of humour.','她首先吸引我的是她的幽默感。','attracted','例',229)],
      'at（表示“加强”）+ tract（拽，拉）→一再地拽→吸引。',
      [('attractive','adj. 有吸引力的',229)])
    material('attractive',229,'派生',phonetic='/əˈtræktɪv/',definition='adj. 有吸引力的')
    a('distract','/dɪˈstrækt/','v. 分散注意力；使分心',229,
      [('v.','分散注意力；使分心')],
      [(0,'You’re distracting me from my work.','你使我不能专心工作。','distracting','例',229),
       (0,'Engaging in leisure-time activities with others helps us to meet our social needs while at the same time distracting us from our worries and troubles.','与他人一起参加休闲活动有助于我们满足社交需求，同时分散我们的注意力和烦恼。','distracting','例',229)],
      'dis（表示“分开”）+ tract（拽，拉）→分开拉，注意力就分散了→分散注意力。',
      [('distracting','adj. 分散注意力的，分心的',229)])
    t.pending('distract',1,'原译分散我们的注意力和烦恼表述疑不准确，原文原译保留待核。')
    material('distracting',229,'派生',phonetic='/dɪˈstræktɪŋ/',definition='adj. 分散注意力的，分心的')
    group='43 “部门、会议”相关语境词汇'
    a('council','/ˈkaʊnsl/','n. 委员会；地方议会',229,
      [('n.','委员会；地方议会')],
      [(0,'He won a seat on the council.','他赢得了议会的一个席位。','council','例',229)])
    a('sector','/ˈsektə(r)/','n. （尤指一国经济的）部门，领域，行业',229,
      [('n.','（尤指一国经济的）部门，领域，行业')],
      [(0,'China is making efforts to expand such economic sectors as tourism and information technology.','中国正在努力发展旅游业和信息技术等经济部门。','sectors','例',229)],
      'sect（切，割）+ or（名词后缀）→切开，切割→分成部分→部门。')
    a('bureau','/ˈbjʊərəʊ/','n. 局，科，处；办事处',229,
      [('n.','局，科，处；办事处')],
      [(0,'The weather bureau makes daily reports on weather conditions.','气象局每天报告天气状况。','bureau','例',229)],
      '发音类似“不弱”→在科室和局里办事的人，一般还真不弱→局，科，处。',
      [('bureaucratic','adj. 官僚的；官僚主义的',229)])
    material('bureaucratic',229,'派生',phonetic='/ˌbjʊərəˈkrætɪk/',definition='adj. 官僚的；官僚主义的')
