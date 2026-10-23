"""One-time visual transcription of batch006. No OCR or prior batch rewrites.
Default saves a resumable unpublished draft; --publish requires completed coverage.
"""
import json
import sys
from pathlib import Path
from transcription_helpers import Transcription
ROOT=Path(__file__).resolve().parents[1]
t=Transcription(); associated=[]; group='01 起源相关词汇'
def a(spelling,ipa,definition,page,meanings,examples,mnemonic='',related=()):
    t.add(346+len(t.words),spelling,ipa,definition,page,group,meanings,examples,mnemonic,related)
def material(word,page,label,**kw):associated.append(dict(word=word,pdf_page=page,label=label,**kw))
a('origin','/ˈɒrɪdʒɪn/','n. 起源，源头；起因；出身',76,[('n.','起源，源头；起因'),('n.','出身')],[(0,'The origin of the word remains obscure.','该词的来源尚不清楚。','origin','例',76)],'这种文化的起源（origin）是在东方（orient）。',[('original','adj. 最初的，原先的',76),('originally','adv. 原来，起初',76)])
material('originally',76,'真题',english='Members of social networks are learning that they can hijack media to apply pressure on the businesses that originally created them.',translation='社交网络用户正领悟到，他们可以通过劫持媒体来对最初创建该媒体的企业施加压力。')
a('originate','/əˈrɪdʒɪneɪt/','v. 起源，发源，发端于',76,[('v.','起源，发源，发端于')],[(0,'The disease is thought to have originated in the tropics.','这种疾病据说起源于热带地区。','originated','例',76),(0,'The universe originated in an explosion from a single mass of energy.','宇宙起源于一团能量的爆炸。','originated','真题',76)])
a('region','/ˈriːdʒən/','n. 地方，区域；领域',76,[('n.','地方，区域'),('n.','领域')],[(0,'This is one of the most densely populated regions of North America.','这是北美洲人口最稠密的地方之一。','regions','例',76),(0,'Home prices are holding steady in most regions.','在大多数地区房屋价格保持稳定。','regions','真题',76)],'发音类似“瑞金”（江西省的一个地方）→地方，区域。',[('zone','n. 地区，区域，地带',76)])
a('stem','/stem/','n. 茎，干；v. 阻止',76,[('n.','茎，干'),('v.','阻止')],[(0,'There are several leaves on each stem.','每根茎上都有几片叶子。','stem','例',76)])
material('stem from',76,'拓展',definition='起源于')
material('stem from',76,'真题',english='Some growth stems from a commitment by governments and farsighted businesses to fund cleaner energy sources.',translation='一些增长源于各国政府和有远见的企业为更清洁的能源提供资金的一个承诺。',reason='固定搭配起源于，不等于主词所列阻止；另存关联资料。')
a('cradle','/ˈkreɪdl/','n. 摇篮，发源地；v. 轻轻抱着',76,[('n.','摇篮'),('v.','轻轻抱着'),('n.','发源地')],[(0,'The baby is crying in the cradle.','宝宝在摇篮里啼哭。','cradle','例',76),(1,'She sat with the child cradled against her.','她怀抱孩子坐着。','cradled','例',76)])
a('source','/sɔːs/','n. 源头，发源地；根源，原因；来源，出处',76,[('n.','来源，出处'),('n.','源头，发源地；根源，原因')],[(0,'Tourism is a major source of revenue for the area.','旅游业是该地区的主要收入来源。','source','例',76),(0,'In many parts of the world renewable energy is already a principal energy source.','在世界许多地方，再生能源已经成为主要的能源来源。','source','真题',76)])
a('resource','/rɪˈsɔːs/','n. 资源；财力；资料；v. 向……提供资金',76,[('n.','资源；资料'),('n.','财力'),('v.','向……提供资金')],[(0,'The website is an invaluable educational resource.','该网站是一个宝贵的教育资源。','resource','例',77),(0,'A government with finite resources should simply stop paying for medical care that sustains life beyond a certain age—say 83 or so.','对于超过一定年龄（比如83岁左右）的人，一个资源有限的政府应当停止支付维持其生命的医疗费用。','resources','真题',77)],'想要重复的（re表示重复）找到金矿的源头（source），是需要很多资源、财力的→资源；财力。')
group='02 未加工的相关词汇'
a('raw','/rɔː/','adj. 未经加工的；生的，未熟制的，未煮的；天然状态的，原始的；不熟练的，没有经验的',77,[('adj.','生的，未熟制的，未煮的'),('adj.','未经加工的；天然状态的，原始的'),('adj.','不熟练的，没有经验的')],[(0,'The tigers were fed raw chicken bones.','老虎被喂了生鸡骨头。','raw','例',77)],'发音类似“肉”→肉最开始一般是“生的，未加工的”。')
a('crude','/kruːd/','adj. 天然的，未加工的；粗俗的，粗鲁的',77,[('adj.','天然的，未加工的'),('adj.','粗俗的，粗鲁的')],[(0,'In most countries the cost of crude oil now accounts for a smaller share of the price of petrol than it did in the 1970s.','与20世纪70年代相比，现在大多数国家的原油成本在汽油价格中所占的比例要小很多。','crude','真题',77)],'有些人是粗鲁的（crude），也是残忍的（cruel）。')
group='03 营养相关词汇'
a('nutrition','/njuˈtrɪʃn/','n. 营养，滋养；营养的补给',77,[('n.','营养，滋养；营养的补给')],[(0,'Nutrition information is now provided on the back of most food products.','现在大多数食品的背面都有营养信息。','Nutrition','例',77),(0,'It is like the immune system of the body, which under stress or through lack of nutrition or exercise can be weakened.','它就像身体的免疫系统，在压力之下，或缺乏营养和锻炼之时，会被削弱。','nutrition','真题',77)],'nut（坚果）+ ri（日）+ tion（名词后缀）→每日吃点坚果可以补充一定的“营养”。',[('nutritious','adj. 有营养的',77)])
material('nutritious',77,'例',english='Adapt your usual eating regime to make it more nutritious.',translation='调整你的常饮食习惯，使之更富有营养。')
a('nutrient','/ˈnjuːtriənt/','n. 营养素，营养物',77,[('n.','营养素，营养物')],[(0,'Plants draw minerals and other nutrients from the soil.','植物从土壤中吸取矿物质和其他养分。','nutrients','例',77),(0,'Growth demands calories and nutrients—notably, protein—to feed expanding tissues.','长高需要卡路里和营养——特别是蛋白质——以满足身体组织生长的需求。','nutrients','真题',77)],related=[('nurture','v. 培养，促进；养育；帮助；培植；n. 养育；培养',77)])
group='04 常规、规划相关词汇'
a('routine','/ruːˈtiːn/','n. 常规，例行程序；adj. 常规的；日常的；例行公事的',77,[('n.','常规，例行程序'),('adj.','常规的；日常的；例行公事的')],[(0,'Make exercise a part of your daily routine.','让锻炼成为你日常生活的一部分。','routine','例',78),(1,'Cargo aircraft, in contrast, might be easier to reschedule, as might routine military flights.','相比之下，货运飞机可能更容易重新安排航程，例行军事飞行也可能如此。','routine','真题',78)],'发音类似“路听”→很多老板行程比较满，通常会在路上听秘书汇报日常工作→例行程序；日程的。')
a('agenda','/əˈdʒendə/','n. 议程表，议事日程；计划，方案；意图，目的',78,[('n.','议程表，议事日程；计划，方案'),('n.','意图，目的')],[(0,'We have a very full agenda of issues to discuss.','我们的议程安排很满，有很多议题要讨论。','agenda','例',78),(1,'And since these messages have an agenda—to lure us to open our wallets—they make the very idea of happiness seem unreliable.','由于这些信息有一个目的——引诱我们打开钱包——它们使幸福这个概念看起来并不可靠。','agenda','真题',78)],'age（年龄）+ n + da（大）→年纪大了，记性不好，所以要写好议事日程提醒自己→议程表，议事日程。')
a('schedule','/ˈʃedjuːl/','n. 工作计划；日程安排；v. 安排；为……安排时间；预定',78,[('n.','工作计划；日程安排'),('v.','安排；为……安排时间；预定')],[(0,'They have a very flexible work schedule.','他们的工作日程非常灵活。','schedule','例',78),(1,'It is important that we schedule in time to enjoy the things we love.','重要的是，我们要及时安排享受我们喜欢的东西。','schedule','真题',78)],'是（s）车（che）堵（du）了（le）堵车了，耽误了我们的“日程安排”。')
a('scheme','/skiːm/','n. 计划，方案；体系，体制；阴谋；v. 计划；认为；图谋',78,[('n.','计划，方案；体系，体制'),('n.','阴谋'),('v.','计划；认为；图谋')],[(0,'In the grand scheme of life, one lecture really doesn’t matter.','在宏大的人生长卷里，一堂课真的不算什么。','scheme','真题',78)],'s（联想成曲线美女）+ che（车）+ me（我）→我爱上了一个美女，我“计划”送她一辆车。')
group='05 苦与乐相关词汇'
a('triumph','/ˈtraɪʌmf/','n. 巨大成功，重大成就，伟大胜利；（巨大成功或胜利的）心满意足，喜悦，狂喜；v. 打败，战胜；成功',78,[('v.','打败，战胜；成功'),('n.','巨大成功，重大成就，伟大胜利'),('n.','（巨大成功或胜利的）心满意足，喜悦，狂喜')],[(0,'In both oral and written English, talking is triumphing over speaking, spontaneity over craft.','在口语和书面英语中，（随意的）谈话胜于（正式的）发言，即兴发挥也胜过了精雕细琢。','triumphing','例',78)],'他们吹响了喇叭（trumpet）来庆祝取得的伟大胜利（triumph）。')
a('delight','/dɪˈlaɪt/','n. 高兴；v. （使）高兴',78,[('n.','高兴'),('v.','（使）高兴')],[(0,'He looked up at his father, his features overflowing with energy and delight.','他抬头看着父亲，脸上洋溢着活力和喜悦。','delight','例',78)],'de（表加强）+ light（使明亮）→使心情明亮→高兴。')
a('plight','/plaɪt/','n. 苦难，困境，苦境',78,[('n.','苦难，困境，苦境')],[(0,'The African elephant is in a desperate plight.','非洲象正处于一种绝境之中。','plight','例',79),(0,'A neighbour heard of her plight and offered to help.','一位邻居听说她的苦境，主动提出帮忙。','plight','例',79)],'人处于困境（plight）的时候，只要看到光（light）就有希望。')
a('blight','/blaɪt/','n. 有害的事物，不利因素；v. 损害，妨害',79,[('v.','损害，妨害'),('n.','有害的事物，不利因素')],[(0,'His career has been blighted by injuries.','他的事业不断受到伤病的困扰。','blighted','例',79),(1,'Her divorce was a great blight in her life.','她的离婚是她生活中的一大败笔。','blight','例',79)],'b（发音类似“不”，即“没有”）+ light（光）→没有光，很多生物的生长就会受到“损害”。')
group='06 光相关词汇'
a('alight','/əˈlaɪt/','adj. 燃烧的；v. 降落；从（公共汽车、火车等）下来',79,[('adj.','燃烧的'),('v.','降落；从（公共汽车、火车等）下来')],[(0,'A cigarette set the dry grass alight.','一支香烟把干草点燃了。','alight','例',79),(0,'Her dress caught alight in the fire.','她的衣服让火烧着了。','alight','例',79)],'a（表示状态）+ light（光）→表示光的一种状态→燃烧的。')
a('slight','/slaɪt/','adj. 轻微的，略微的；细小的',79,[('adj.','轻微的，略微的；细小的')],[(0,'This gives rats the ability to detect slight smells.','这使老鼠能够察觉轻微的气味。','slight','例',79),(0,'It won’t make the slightest bit of difference.','这不会有丝毫的区别。','slightest','例',79)],'s（发音类似“丝”）+ light（轻的）→像蚕丝一样又轻又细→轻微的，细小的。',[('slightly','adv. 略微，稍微',79)])
material('slightly',79,'真题',english='The use of privacy law to curb the tech giants in this instance feels slightly maladapted.',translation='本案中用隐私法限制科技巨头似乎稍显牵强。')
a('ignite','/ɪɡˈnaɪt/','v. （使）燃烧，着火；点燃',79,[('v.','（使）燃烧，着火；点燃')],[(0,'They ignited a candle to give the baby a surprise.','他们点燃蜡烛给宝宝一个惊喜。','ignited','例',79),(0,'His words ignited their anger.','他的话点燃了他们的怒火。','ignited','例',79)],'ig（发音类似“一个”）+ nite（发音类似night“夜晚”）→一个晚上都没电，我们“点燃”一根蜡烛吧。')
a('highlight','/ˈhaɪlaɪt/','n. 最好（或最精彩、最激动人心）的部分；v. 突出，强调',79,[('v.','突出，强调'),('n.','最好（或最精彩、最激动人心）的部分')],[(0,'The report highlighted the importance of exercise to maintain a healthy body.','报告强调了锻炼对保持健康身体的重要性。','highlighted','例',79),(0,'The current emphasis on standardized testing highlights analysis and procedure.','目前对标准化测试的重视就是强调分析和程序。','highlights','真题',79)],'high（高）+ light（光）→高光→女生在脸上打高光（一种化妆用品）是为了“突出”脸部某个位置。')
group='07 patience相关词汇'
a('patience','/ˈpeɪʃns/','n. 忍耐，耐心；毅力',79,[('n.','忍耐，耐心'),('n.','毅力')],[(0,'I have run out of patience with her.','我对她已失去耐心了。','patience','例',80),(0,'It gives us patience for ourselves and toward others.','它让我们对自己和他人更有耐心。','patience','真题',80)],'陪伴病人（patient）需要很大的耐心（patience）。',[('patient','n. 病人；adj. 忍耐的，耐心的',80)])
material('patient',80,'真题',english='Children of every age benefit from patient parenting.',translation='每个年龄的孩子都受益于耐心的养育。')
a('pace','/peɪs/','n. 步伐；速度；节奏；v. 来回踱步，走来走去；确定速度；调整节奏',80,[('n.','速度；节奏'),('n.','步伐'),('v.','来回踱步，走来走去'),('v.','确定速度；调整节奏')],[(0,'It is difficult to keep up with the rapid pace of change.','跟上快速的变化是很困难的。','pace','例',80),(0,'The pace of change in energy sources appears to be speeding up.','能源资源方面的转变速度似乎在加快。','pace','真题',80)])
material('keep pace with',80,'拓展',definition='（与……）并驾齐驱；（与……）步调一致')
a('patent','/ˈpeɪtnt/','n. 专利；专利证书；v. 获得专利；adj. 专利生产的；专利经销的',80,[('n.','专利；专利证书'),('v.','获得专利'),('adj.','专利生产的；专利经销的')],[(0,'The device was protected by patent.','这一装置受专利保护。','patent','例',80),(0,'The Federal Circuit’s action comes in the wake of a series of recent decisions by the Supreme Court that has narrowed the scope of protections for patent holders.','在最高法院最近作出一系列限制对专利持有人的保护范围的决定之后，联邦巡回法院采取了行动。','patent','真题',80)],'pa（发音类似pay“付款”）+ tent（帐篷）→需要付款才能拥有这款有“专利”的帐篷。')
group='08 me相关词汇'
a('melt','/melt/','v. 融化，（使）熔化',80,[('v.','融化，（使）熔化')],[(0,'The snow showed no sign of melting.','雪没有一点融化的迹象。','melting','例',80),(0,'They melt into sludge.','它们会融化成污泥。','melt','真题',80)],'me（我）+ l（了）+ t（他）→我“融化”了他的内心。')
a('tame','/teɪm/','adj. （动物）驯服的，温顺的；v. 驯服；使易于控制',80,[('v.','驯服；使易于控制'),('adj.','（动物）驯服的，温顺的')],[(0,'Lions can never be completely tamed.','狮子永远不能被完全驯化。','tamed','例',80),(1,'The bird became so tame that it was impossible to release it back into the wild.','这只鸟变得如此温顺，以至于不可能把它放回野外。','tame','例',80)],'ta（她）+ me（我）→她和我都是“温顺的”人。')
a('lame','/leɪm/','adj. 跛的；没有说服力的',80,[('adj.','没有说服力的'),('adj.','跛的')],[(0,'Stephen made some lame excuse.','斯蒂芬找了些站不住脚的借口。','lame','例',80),(0,'They should start by discarding California’s lame argument.','他们应该从抛弃加州的蹩脚的论点开始。','lame','真题',81)],'la（拉）+ me（我）→你需要拉我一下，因为我有点跛足，走不快。→跛的。',[('lameness','n. 残缺，不完全（备）；跛脚',81)])
a('blame','/bleɪm/','v. 责备，责怪，指责；n. 责备；责任；指责',81,[('v.','责备，责怪，指责'),('n.','责备；责任；指责')],[(0,'A dropped cigarette is being blamed for the fire.','一根乱扔的烟被认为是这场火灾的肇因。','blamed','例',81),(1,'To some extent the housing sector must shoulder the blame.','在某种程度上，住房部门必须承担责任。','blame','真题',81)],'b（发音类似“不”）+ la（拉）+ me（我）→我腿脚不灵活，跑步时他还不拉我一把，我就“责备，责怪”他。')
group='09 吵、骂相关词汇'
a('quarrel','/ˈkwɒrəl/','n. 争论，争辩，口角；争论的原因；v. 争吵，争辩',81,[('n.','争论，争辩，口角'),('n.','争论的原因'),('v.','争吵，争辩')],[(0,'He got involved in a quarrel with his neighbour.','他和邻居吵了一架。','quarrel','例',81)],'发音类似“口哦”→需要用口说出来哦→争辩，争论。')
a('curse','/kɜːs/','n. 咒骂，咒语；v. 诅咒，咒骂',81,[('v.','诅咒，咒骂'),('n.','咒骂，咒语')],[(0,'He cursed himself for his stupidity.','他咒骂自己愚蠢。','cursed','例',81)],'发音类似“渴死”→在大家都很渴的时候，就会不自觉地抱怨，咒骂→咒骂。')
a('accuse','/əˈkjuːz/','v. 谴责，指责；控告',81,[('v.','谴责，指责；控告')],[(0,'She accused him of lying.','她指责他说谎。','accused','例',81),(0,'Some scholars even accused Boas and Sapir of fabricating their data.','一些学者甚至谴责博厄斯和萨丕尔伪造数据。','accused','真题',81)],'ac（表示“加强”）+ cuse（发音类似curse“诅咒”）→一再地诅咒→谴责，指责。',[('accusation','n. 指责，谴责',81)])
group='10 阻碍相关词汇'
a('hinder','/ˈhɪndə(r)/','v. 妨碍，阻碍',81,[('v.','妨碍，阻碍')],[(0,'An injury was hindering him from playing his best.','受伤后他无法发挥出最高水平。','hindering','例',81),(0,'A gap year does not hinder the success of academic pursuits.','间隔年并不会阻碍学业上的成功。','hinder','真题',81)],'发音类似“恨得”→他总是做一些奇怪的事情“妨碍”大家，大家提起他就恨得咬牙切齿→妨碍。',[('hindrance','n. 障碍；妨碍的人或物',81)])
# NEXT_RECORDS
completed_pages=list(range(76,82))
continuations=['PDF81底部obstacle：待82页续文一起转录。']
publish=False
out=dict(format_version=1,content_version='batch-006-v1',source_id='src-0001',method='manual_visual_transcription',words=t.words,policy='第三单元；人工视觉转录，词义由编辑拆分，音标未外部词典复核。')
draft=ROOT/'content/drafts';draft.mkdir(exist_ok=True)
(draft/'batch-006.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(draft/'batch-006-associated.json').write_text(json.dumps(dict(method='manual_visual_transcription',items=associated),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(draft/'batch-006-checkpoint.json').write_text(json.dumps(dict(status='ready_for_review' if publish else 'draft',completed_pages=completed_pages,continuations=continuations,words=len(t.words),last_word=t.words[-1]['spelling'],next_id=f'w{346+len(t.words):04}'),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
if '--publish' in sys.argv:
    assert publish and not continuations, 'Incomplete batch must not be published'
    for name in ['batch-006.json','batch-006-associated.json']:(ROOT/'content/batches'/name).write_bytes((draft/name).read_bytes())
    snap=ROOT/'content/transcripts/batch-006-initial.json'
    if not snap.exists():snap.write_bytes((draft/'batch-006.json').read_bytes())
print('Saved',len(t.words),'words; pages',completed_pages,'publishable',publish)
