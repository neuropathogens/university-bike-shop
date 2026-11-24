from ap_chinese.model import Doc

STEM = "01-families-communities"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 1: Families and Communities", r"Unit 1 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 1 asks what makes a family, which family values shape daily life, and how families and communities experience a changing world. Its recommended contexts are family relationships, community activities, social interactions and relationships, and urban and rural communities. This guide gives the kinship and community vocabulary the exam assumes, the sentence patterns for describing relationships and routines, the cultural products, practices and perspectives most often tested (filial piety, reunion, respect for elders, neighborliness), and an Email Response kit, since emails from friends and community members are the unit's natural writing task. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 11+ \qquad Words I keep forgetting: \blank[10em]",
        short="Unit 1", sub="Families and Communities")

G.sec("Family and kinship terms")
G.tex(r"""
Chinese kinship terms say \emph{which side} of the family and \emph{older or younger}, which English leaves out. The exam uses them in correspondence and conversations; misreading 舅舅 as ``father's brother'' changes who is visiting.

\begin{vocab}
爷爷 / 奶奶 & yéye / nǎinai & father's father / father's mother \\
外公 / 外婆（姥爷 / 姥姥） & wàigōng / wàipó (lǎoye / lǎolao) & mother's father / mother's mother (姥 forms are northern) \\
伯伯 / 叔叔 & bóbo / shūshu & father's older / younger brother; 叔叔 is also any man of one's parents' age \\
姑姑 & gūgu & father's sister \\
舅舅 / 阿姨（姨妈） & jiùjiu / āyí (yímā) & mother's brother / mother's sister; 阿姨 is also any woman of one's parents' age \\
哥哥 / 姐姐 / 弟弟 / 妹妹 & gēge / jiějie / dìdi / mèimei & older brother / older sister / younger brother / younger sister \\
堂兄弟姐妹 & táng xiōngdì jiěmèi & cousins through one's father's brothers (same surname) \\
表兄弟姐妹 & biǎo xiōngdì jiěmèi & all other cousins \\
独生子女 & dúshēng zǐnǚ & only child \\
亲戚 & qīnqi & relatives \\
父母 / 长辈 / 晚辈 & fùmǔ / zhǎngbèi / wǎnbèi & parents / elders, senior generation / juniors \\
\end{vocab}

\begin{vocab}
三代同堂 / 四世同堂 & sān dài tóng táng / sì shì tóng táng & three / four generations under one roof \\
照顾 & zhàogù & to look after \\
陪 & péi & to keep someone company \\
孝顺 & xiàoshùn & filial, devoted to one's parents \\
团圆 & tuányuán & (family) reunion \\
家务 & jiāwù & housework \\
带孩子 & dài háizi & to look after (raise) children \\
\end{vocab}
""")
G.q("1 Kinship", r"Lili's mother's brother is visiting. Lili calls him",
    "舅舅", [("叔叔", "叔叔 is the father's younger brother (or a polite term for a man of one's parents' age)."),
             ("伯伯", "伯伯 is the father's older brother."),
             ("姑姑", "姑姑 is the father's sister, and a woman.")],
    "Mother's brother = 舅舅.",
    "Kinship terms mark the side of the family: 舅舅 is the mother's brother, while 伯伯 and 叔叔 are the father's brothers.",
    ["Mother's side, male, same generation as the mother → 舅舅."])
G.q("1 Kinship", r"Which sentence describes a family in which grandparents, parents and children live together?",
    "他们家三代同堂。", [("他们家是独生子女。", "独生子女 means an only child; it describes the number of children, not generations."),
                       ("他们家有很多亲戚。", "Having many relatives says nothing about living together."),
                       ("他们家很孝顺。", "孝顺 describes devotion to parents, not the household structure.")],
    "三代同堂 = three generations under one roof.",
    "三代同堂 (three generations) and 四世同堂 (four) describe extended families living in one household.",
    ["Grandparents + parents + children = three generations → 三代同堂."])
G.q("1 Kinship", r"In 我的表哥, 表 tells you the cousin is",
    "not the child of your father's brother", [("older than your father", "表哥 is an older male cousin, not someone older than your father."),
                                              ("a woman", "哥 marks an older male."),
                                              ("your father's brother's son", "A father's brother's son is a 堂哥 (same surname); 表 covers all other cousins.")],
    "堂 = father's brothers' children; 表 = all other cousins.",
    "Cousins through the father's brothers share the surname and are 堂; cousins through the father's sisters or anyone on the mother's side are 表.",
    ["表哥: older male cousin, not through the father's brothers."])

G.sec("Community and social life")
G.tex(r"""
\begin{vocab}
社区 / 小区 & shèqū / xiǎoqū & community / residential compound \\
邻居 & línjū & neighbor \\
志愿者 / 当志愿者 & zhìyuànzhě & volunteer / to volunteer \\
社区活动 & shèqū huódòng & community activity \\
居委会 & jūwěihuì & neighborhood (residents') committee \\
广场舞 & guǎngchǎngwǔ & square dancing (group dancing in public squares) \\
养老院 & yǎnglǎoyuàn & home for the elderly \\
互相帮助 & hùxiāng bāngzhù & to help each other \\
参加 / 举办 / 组织 & cānjiā / jǔbàn / zǔzhī & to take part in / to hold / to organize \\
城市 / 农村 / 乡下 & chéngshì / nóngcūn / xiāngxia & city / rural area / the countryside \\
搬家 / 搬到 & bānjiā / bān dào & to move house / to move to \\
外地 / 老家 & wàidì / lǎojiā & another part of the country / one's hometown \\
打工 & dǎgōng & to work (often a job away from home) \\
留学生 & liúxuéshēng & international student \\
\end{vocab}

\textbf{Urban and rural life.} Many people have moved from rural areas to cities for work, which shapes family life: grandparents often help raise grandchildren, and the Spring Festival trip home (春运) is the year's great reunion journey. Questions in this context ask about \emph{reasons} (为了找工作) and \emph{effects} (老人和孩子留在老家).

\textbf{Social interactions.} Politeness rules show up in correspondence and conversations: declining a first offer before accepting, 客气 (being polite, standing on ceremony), and the reply 哪里哪里 to a compliment.
""")
G.q("2 Community", r"A flyer says: 社区下个星期六举办敬老活动，欢迎志愿者报名。 Who is the flyer looking for?",
    "volunteers", [("elderly residents to sign up for classes", "The activity honors the elderly (敬老), but 欢迎志愿者报名 asks volunteers to sign up."),
                   ("neighbors to move out", "Nothing about moving; 搬家 does not appear."),
                   ("paid workers", "志愿者 are unpaid volunteers.")],
    "志愿者 = volunteer; 报名 = sign up.",
    "举办 means to hold an event; 欢迎……报名 invites a group to register.",
    ["欢迎志愿者报名: volunteers are welcome to sign up."])
G.q("2 Community", r"他为了找工作，从农村搬到了城市。 Why did he move?",
    "to find work", [("to look after his grandparents", "Nothing about grandparents; the purpose is given by 为了找工作."),
                     ("to go to school", "上学 does not appear; 找工作 is to look for a job."),
                     ("because the city is quieter", "No comparison is made, and cities are not described as quieter.")],
    "为了 + purpose.",
    "为了 introduces the purpose of an action: 为了找工作 = in order to find work.",
    ["为了找工作 → purpose: work."])
G.q("2 Social", r"Someone praises your Chinese, and you answer modestly. Which reply fits Chinese politeness norms?",
    "哪里哪里，还差得远呢。", [("对，我说得很好。", "Agreeing with praise can sound boastful; modest deflection is the expected reply."),
                             ("你说得不对。", "Bluntly contradicting the speaker is rude."),
                             ("不客气。", "不客气 answers thanks (you're welcome), not praise.")],
    "Deflect praise: 哪里哪里, 还差得远.",
    "Modesty is valued: the conventional answer to a compliment deflects it (哪里哪里, 过奖了, 还差得远呢).",
    ["Praise → modest deflection."])

G.sec("Patterns for describing people and routines")
G.tex(r"""
\begin{compare}{Pattern}{Use}{Example}
对……来说 & from someone's point of view & 对我奶奶来说，家人在一起最重要。 \\
跟……一起 / 陪……& with / keeping someone company & 周末我常常陪外婆去公园。 \\
一边……一边…… & two actions at once & 爸爸一边做饭，一边听新闻。 \\
除了……以外，还/都 & besides / except & 除了哥哥以外，全家都会说上海话。 \\
越来越 & increasingly & 年轻人越来越晚结婚。 \\
不是……而是…… & not A but B & 她搬家不是因为工作，而是为了照顾父母。 \\
既……又…… & both \ldots\ and \ldots & 我的邻居既热情又细心。 \\
一……就…… & as soon as & 我一回家就帮妈妈做家务。 \\
被……照顾 / 由……负责 & cared for by / be the responsibility of & 孩子平时由爷爷奶奶照顾。 \\
\end{compare}

\begin{trap}
除了……以外 has two meanings. With 还 or 也 it \emph{adds}: 除了中文以外，他还会法语 (besides Chinese, he also speaks French). With 都 it \emph{excludes}: 除了他以外，我们都去了 (everyone went except him). Reading questions test this directly.
\end{trap}
""")
G.q("3 除了", r"除了妹妹以外，我们全家都喜欢吃辣的。 Who does not like spicy food?",
    "the younger sister", [("everyone in the family", "都 says everyone else likes it; only the sister is excluded."),
                          ("the speaker", "The speaker is part of 我们全家, who like it."),
                          ("no one; the sister also likes it", "That reading needs 还/也; 除了……都 excludes.")],
    "除了 X 以外，都 = everyone except X.",
    "除了……以外 + 都 excludes X from the group; with 还/也 it would add X.",
    ["The main clause uses 都 → exclusion.", "Excluded: 妹妹."])
G.q("3 不是而是", r"她搬家不是因为工作，而是为了照顾父母。 Why did she move?",
    "to look after her parents", [("for her job", "不是因为工作 explicitly rules work out."),
                                 ("because her parents told her to", "No one tells her to; she moves in order to care for them."),
                                 ("because housing was cheaper", "Housing costs are not mentioned.")],
    "不是 A，而是 B: B is the true reason.",
    "不是……而是…… rejects the first option and asserts the second.",
    ["Rejected: work.", "Asserted: 为了照顾父母."])
G.q("3 由", r"Choose the best way to say: ``On weekdays the child is looked after by the grandparents.''",
    "孩子平时由爷爷奶奶照顾。", [("孩子平时照顾爷爷奶奶。", "This reverses the roles: the child looks after the grandparents."),
                               ("爷爷奶奶平时由孩子照顾。", "Again reversed: the grandparents are cared for by the child."),
                               ("孩子平时爷爷奶奶由照顾。", "由 must come before the agent: 由爷爷奶奶照顾.")],
    "由 + person + V: the person responsible.",
    "由 introduces who is responsible for an action: 由爷爷奶奶照顾.",
    ["Who cares? Grandparents → 由爷爷奶奶 + 照顾."])

G.sec("Culture: products, practices and perspectives")
G.tex(r"""
\begin{compare}{Perspective}{Practices and products that express it}{Language to use}
\textbf{Filial piety} (孝): children owe care and respect to parents. & Adult children support aging parents; grandparents live with the family; visiting on holidays (常回家看看). & 孝顺父母，养儿防老（raise children to be cared for in old age）, 百善孝为先（filial piety comes first among virtues） \\
\textbf{Reunion} (团圆): the family belongs together. & The New Year's Eve dinner (年夜饭/团圆饭); the Mid-Autumn round mooncake; the Spring Festival journey home (春运). & 团团圆圆, 每逢佳节倍思亲（one misses family most at festivals） \\
\textbf{Respect for elders} (尊老爱幼). & Serving elders first at meals; giving seats on the bus; the Double Ninth Festival (重阳节) for the elderly. & 尊老爱幼, 敬老 \\
\textbf{Neighborliness}. & Helping neighbors; community dance and exercise groups; residents' committees. & 远亲不如近邻（a near neighbor is better than a distant relative） \\
\textbf{Education as a family project}. & Grandparents helping with pick-up; family savings for school. & 望子成龙（hoping one's son becomes a dragon: high hopes for children） \\
\end{compare}

\begin{keyidea}[How to use these in writing]
Name the practice, then the perspective behind it, then a comparison: \emph{在中国，很多老人帮子女带孩子（practice），这反映了家庭成员互相照顾的观念（perspective）。在美国，祖父母一般不跟孙子孙女住在一起（comparison）。} This three-step move earns cultural understanding points in the presentation and Q\&A.
\end{keyidea}
""")
G.q("4 Perspectives", r"Grandparents in many Chinese families help raise their grandchildren. Which perspective does this practice most directly reflect?",
    "family members are expected to support one another across generations",
    [("children should become independent as early as possible", "This describes a value often associated with other cultures; the practice shows interdependence."),
     ("elders should not be involved in family decisions", "Grandparents raising children is deep involvement."),
     ("education matters less than work", "The practice is about care across generations, not ranking education and work.")],
    "Multi-generation care ↔ mutual family support.",
    "A perspective explains why a practice exists. Grandparents raising grandchildren reflects the value of interdependence across generations.",
    ["Practice: grandparents help raise children.", "Value behind it: families support each other across generations."])
G.q("4 Sayings", r"Which saying best fits a story about neighbors helping an old man whose children live far away?",
    "远亲不如近邻", [("望子成龙", "望子成龙 is about parents' high hopes for their children."),
                   ("一举两得", "一举两得 means killing two birds with one stone."),
                   ("入乡随俗", "入乡随俗 means when in Rome, do as the Romans do.")],
    "远亲不如近邻: a near neighbor beats a distant relative.",
    "The saying praises the help of nearby neighbors over relatives who live far away.",
    ["Distant children + helpful neighbors → 远亲不如近邻."])
G.q("4 Practices", r"The 春运 period is best described as",
    "the travel rush when people go home for the Spring Festival", [("a spring sports meeting at school", "运 here is from 运输 (transport), not 运动 (sports)."),
                                                                  ("the start of the school year", "The school year does not start at Spring Festival."),
                                                                  ("a farming season in the countryside", "春运 is about travel, not farming.")],
    "春运 = Spring Festival travel season.",
    "春运 is the period around the Spring Festival when hundreds of millions travel home for reunion, a practice that reflects the value of 团圆.",
    ["春 = Spring (Festival); 运 = transport → the holiday travel rush."])

G.sec("Task kit: the Email Response")
G.tex(r"""
Unit 1 emails come from a friend, a host family, a neighbor or a community organizer. They usually ask for \emph{advice} or \emph{a choice}, plus \emph{a reason}.

\begin{compare}{Move}{To a friend}{To an elder or organizer}
Open & 小美，你好！收到你的邮件我很高兴。 & 王阿姨，您好！谢谢您的来信。 \\
Request 1 & 关于你问的……，我觉得…… & 关于您问的……，我认为…… \\
Reasons & 首先……其次……另外…… & 首先……其次……此外…… \\
Request 2 & 至于……，我建议你…… & 至于……，我的建议是…… \\
Close & 有什么问题随时问我。祝你开心！ & 如果需要帮忙，请随时告诉我。祝您身体健康！ \\
\end{compare}

\textbf{Advice frames}: 我建议你…… / 你最好…… / 与其……不如……（rather than \ldots, better to \ldots） / 要是我是你，我会……
\textbf{Choice frames}: 我比较倾向于……，因为…… / 两个都不错，不过……
""")
G.q("5 Email", r"A host family member 张叔叔 asks whether you prefer to stay in the city or the countryside and why. Which first sentence best answers the first request directly?",
    "张叔叔，您好！关于您问的住城市还是乡下，我比较想住在乡下。",
    [("张叔叔，你好！最近怎么样？", "A greeting with small talk, but it never answers the question; and 你 is too casual for an older host."),
     ("我觉得城市和乡下都有很多人。", "This makes a statement about both places without stating a preference."),
     ("谢谢您的邮件，祝您身体健康！", "This is a closing, not an answer.")],
    "Answer the request directly, in the right register.",
    "Message development rewards clear, direct answers to each request; start by restating it (关于您问的……) and give your choice.",
    ["Greeting with 您 → restate the request → state your preference."])
G.q("5 Email", r"Which frame gives advice by recommending one option over another?",
    "与其在家玩手机，不如去社区当志愿者。", [("因为在家玩手机，所以去社区当志愿者。", "This makes playing on the phone the cause of volunteering; it is not advice."),
                                         ("一边在家玩手机，一边去社区当志愿者。", "一边……一边 means doing both at once, which is impossible here."),
                                         ("除了在家玩手机以外，都去社区当志愿者。", "除了……都 means everyone except; it does not compare options.")],
    "与其 A，不如 B = rather than A, better to B.",
    "与其……不如…… recommends B over A, a useful advanced advice structure.",
    ["Two options, B preferred → 与其……不如……"])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 1: Families and Communities: Question Set", r"Unit 1 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (a Conversation and an Audio Report for listening, a Correspondence and an Article for reading) on family relationships, community activities and urban and rural life, followed by an Email Response with a scoring guide and a model reply. Listening sources are printed as transcripts: read each once at normal speed, then answer without rereading. Questions and choices are in English, as on past AP Chinese exams. All sources are original and written for practice. Allow about 25 minutes for the multiple choice and 15 minutes for the email.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Email: \blank\ / 8 \qquad Target: 16+ MCQ and 6+ email \qquad Pace: 75 s per item",
        short="Unit 1", sub="Families and Communities")

Q.sec("Listening: Conversation")
Q.src(r"Listening 1 \textperiodcentered\ Conversation (transcript) \textperiodcentered\ Two classmates talk about a weekend plan", [
    "男：小林，这个周末你有空吗？我们几个同学打算去爬山。",
    "女：我也很想去，可是我外婆下个星期过生日，我妈让我周六跟她一起去外婆家帮忙准备。",
    "男：你外婆不是住在乡下吗？坐车要三个小时吧？",
    "女：对，所以我们周五晚上就得出发。外婆七十岁了，我舅舅、阿姨他们都会回去，大概有二十多个人呢。",
    "男：哇，这么热闹！那你们准备做什么？",
    "女：我妈负责做饭，我负责布置房间，还要给外婆做一个生日视频，把大家的祝福都录下来。",
    "男：这个主意真好！要不要我帮你剪视频？我剪视频挺快的。",
    "女：太好了！那你周四放学以后来我家吧，我把录好的视频给你。",
], 5)
Q.q("1.A.1 Detail", "Why can't the woman go hiking this weekend?",
    "She is helping prepare her grandmother's birthday celebration.",
    [("She has to study for a test.", "No test is mentioned; she is going to her grandmother's house."),
     ("Her mother is sick.", "Her mother is cooking for the party, not sick."),
     ("She does not like hiking.", "She says 我也很想去: she would like to go.")],
    "外婆过生日 → she helps prepare.", "The woman says she would like to go, but her grandmother's birthday preparations come first.",
    ["我也很想去，可是……: the reason follows 可是.", "我妈让我周六跟她一起去外婆家帮忙准备."])
Q.q("1.A.1 Detail", "Whose side of the family is the woman visiting?",
    "her mother's", [("her father's", "外婆 and 舅舅 are on the mother's side."),
                     ("her neighbor's", "The relatives are her own family, not neighbors."),
                     ("the man's", "The man is a classmate; the family is the woman's.")],
    "外婆, 舅舅, 阿姨 = mother's side.", "外婆 is the mother's mother, 舅舅 the mother's brother: the gathering is on the mother's side.",
    ["Kinship terms identify the side: 外 and 舅 are maternal."])
Q.q("1.A.1 Detail", "When will the woman and her mother leave?",
    "Friday evening", [("Saturday morning", "They must leave Friday night because the trip takes three hours: 周五晚上就得出发."),
                       ("Thursday after school", "Thursday after school is when the man will come to edit the video."),
                       ("next week", "The birthday is next week, but they leave this Friday to help prepare.")],
    "周五晚上就得出发.", "The 就 in 周五晚上就得出发 stresses that they must leave as early as Friday evening.",
    ["Listen for the departure time after 所以."])
Q.q("1.B.1 Main idea", "What is the woman's main task?",
    "decorating the room and making a video of everyone's wishes", [("cooking for the guests", "Her mother is in charge of cooking (我妈负责做饭)."),
                                                                  ("driving the relatives", "No one mentions driving."),
                                                                  ("buying the birthday cake", "A cake is never mentioned.")],
    "我负责布置房间，还要……做一个生日视频.", "负责 assigns responsibility: the mother cooks; the woman decorates and makes the video.",
    ["Match each 负责 with its person."])
Q.q("1.C.3 Inference", "What will probably happen on Thursday?",
    "The man will go to the woman's home to edit the video.", [("The woman will go hiking with the class.", "The hike is this weekend, and she is not going."),
                                                              ("The relatives will arrive at the grandmother's house.", "The relatives gather on the weekend, not Thursday."),
                                                              ("The man will record a birthday wish for the grandmother.", "He offers to edit (剪视频), not to record a message.")],
    "那你周四放学以后来我家吧.", "The woman accepts the man's offer and invites him over on Thursday to give him the footage.",
    ["要不要我帮你剪视频？→ 太好了 → 周四来我家."])

Q.sec("Reading: Correspondence")
Q.src(r"Reading 1 \textperiodcentered\ Correspondence \textperiodcentered\ An email", [
    "主题：周末的社区活动",
    "亲爱的各位邻居：",
    "大家好！为了让小区里的老人过一个热闹的重阳节，居委会决定在十月十一日（星期六）上午九点到十二点，在小区花园举办“敬老爱老”活动。",
    "活动内容包括：给八十岁以上的老人量血压、免费理发，还有孩子们表演的节目。中午我们会请大家一起吃饺子。",
    "我们现在需要十五位志愿者：五位帮忙包饺子，五位负责照顾老人，还有五位帮忙打扫。如果您愿意参加，请在十月八日以前给我回邮件，并写明您想做哪一项工作。高中生参加志愿活动，可以得到社区服务证明。",
    "谢谢大家的支持！",
    "居委会 陈红",
], 5)
Q.q("1.B.1 Purpose", "What is the main purpose of the email?",
    "to recruit volunteers for a community event for the elderly", [("to invite children to a birthday party", "The event is for the Double Ninth Festival and honors the elderly."),
                                                                  ("to announce a new garden in the neighborhood", "The garden is only the location."),
                                                                  ("to ask neighbors to pay for haircuts", "The haircuts are free (免费理发).")],
    "我们现在需要十五位志愿者.", "The email describes the event and then states its request: fifteen volunteers.",
    ["Find the request: 需要……志愿者 + 请……回邮件."])
Q.q("1.A.1 Detail", "Who will receive free haircuts?",
    "residents over eighty", [("all the volunteers", "The service is for the elderly, not volunteers."),
                              ("the children who perform", "The children perform; the services are for older residents."),
                              ("high school students", "Students can get a service certificate, not haircuts.")],
    "给八十岁以上的老人……免费理发.", "以上 means “and above”: residents eighty and older.",
    ["Find 理发 and read who it is for."])
Q.q("1.A.1 Detail", "What must volunteers include when they reply?",
    "which job they want to do", [("their age", "Age is not requested."),
                                  ("how many dumplings they can make", "Dumpling-making is one job, not a quantity to report."),
                                  ("their apartment number", "No address is requested.")],
    "写明您想做哪一项工作.", "写明 means to state clearly in writing: volunteers must name the job they want.",
    ["请……回邮件，并写明……"])
Q.q("1.B.2 Audience", "Who is the intended audience of the email?",
    "residents of the neighborhood", [("the writer's family", "亲爱的各位邻居 addresses neighbors."),
                                      ("a school principal", "No school is addressed."),
                                      ("only people over eighty", "The elderly are the guests; the email asks all neighbors to help.")],
    "亲爱的各位邻居 = dear neighbors.", "The salutation names the audience; the sender is the residents' committee.",
    ["Look at the salutation."])
Q.q("1.C.3 Inference", "Why does the writer mention high school students?",
    "to point out a benefit that may encourage them to volunteer", [("to say they cannot take part", "They can take part and get a certificate."),
                                                                   ("to ask them to perform", "The performers are children; students are mentioned as volunteers."),
                                                                   ("to say they must pay a fee", "No fee is mentioned.")],
    "可以得到社区服务证明 = a benefit.", "Mentioning the community-service certificate gives students a reason to sign up.",
    ["The sentence states what students gain → motivation."])

Q.sec("Reading: Article")
Q.src(r"Reading 2 \textperiodcentered\ Article \textperiodcentered\ From a city newspaper", [
    "“候鸟老人”：为孙辈奔波的一代",
    "每年九月，退休教师刘阿姨都会从东北的老家坐火车到深圳，帮女儿照顾两个外孙。像她这样为了帮子女带孩子而离开家乡、跟着子女在城市生活的老人，被人们叫做“候鸟老人”。",
    "据一项调查，在一些大城市，约有三分之一的学龄前儿童主要由祖父母照顾。很多年轻父母工作很忙，请保姆又太贵，所以父母的帮助就显得特别重要。",
    "不过，“候鸟”生活也有不容易的地方。刘阿姨说，在深圳她不认识什么人，听不太懂本地话，而且老伴还留在东北，两个人一年只能见几次面。“为了孩子，累一点没关系，就是有时候觉得孤单。”",
    "专家建议，社区可以多为这些老人组织活动，比如合唱团、太极班，让他们在新的城市也能交到朋友。",
], 5)
Q.q("1.B.5 Word meaning", "In the article, 候鸟老人 (literally ``migratory-bird elders'') refers to",
    "older people who move to their children's cities to help with grandchildren", [("retired teachers who study birds", "Liu is a retired teacher, but the term describes moving to help raise grandchildren."),
                                                                                   ("older people who travel south every winter for vacation", "They move to help with children, not for vacation."),
                                                                                   ("grandparents who stay in their hometown", "They leave their hometown (离开家乡).")],
    "为了帮子女带孩子而离开家乡……被人们叫做“候鸟老人”.", "The article defines the term in the sentence before it: elders who leave home to help raise grandchildren in the city.",
    ["被人们叫做 introduces the term; the definition comes just before."])
Q.q("1.A.2 Data", "According to the survey, about how many preschool children in some big cities are cared for mainly by grandparents?",
    "one third", [("one half", "三分之一 is one third, not half."),
                  ("two thirds", "三分之二 would be two thirds."),
                  ("almost all", "约有三分之一 is about one third.")],
    "三分之一 = one third.", "Chinese fractions put the denominator first: 三分之一 = 1/3.",
    ["分之: denominator before, numerator after."])
Q.q("1.A.1 Detail", "Which difficulty does Liu mention?",
    "She feels lonely in the new city.", [("Her daughter does not want her help.", "Nothing suggests the daughter refuses help."),
                                          ("The train ticket is too expensive.", "Cost of the trip is not mentioned; the expense mentioned is hiring a nanny."),
                                          ("Her grandchildren do not speak Mandarin.", "It is Liu who can't understand the local dialect.")],
    "有时候觉得孤单.", "Liu lists not knowing anyone, not understanding the local speech, and living apart from her husband; she sums it up as loneliness.",
    ["Find the 不容易的地方 paragraph."])
Q.q("1.B.3 Attitude", "What is Liu's attitude toward her life as a 候鸟老人?",
    "willing to sacrifice for her family, though sometimes lonely", [("angry and eager to go home", "She says 累一点没关系: she accepts the hardship."),
                                                                   ("completely carefree", "She admits she feels lonely."),
                                                                   ("regretful about having grandchildren", "Nothing suggests regret.")],
    "累一点没关系，就是有时候觉得孤单.", "The quotation shows both acceptance (没关系) and a reservation introduced by 就是 (it's just that …).",
    ["Read the quotation closely: 没关系 + 就是……"])
Q.q("1.C.2 Conclusion", "What solution do experts propose?",
    "community activities that help these elders make friends", [("paying grandparents a salary", "No payment is proposed."),
                                                               ("sending children back to the hometown", "The proposal keeps everyone in the city."),
                                                               ("hiring more nannies", "Nannies are described as too expensive.")],
    "社区可以多为这些老人组织活动.", "The final paragraph proposes choirs and tai chi classes so the elders can make friends.",
    ["专家建议 introduces the solution."])

Q.sec("Listening: Audio Report")
Q.src(r"Listening 2 \textperiodcentered\ Audio Report (transcript) \textperiodcentered\ A local radio report", [
    "各位听众，晚上好。今天我们关注的是一个新的城市现象：“共享厨房”。",
    "在城东的阳光小区，居委会把一楼的一间空房改成了公共厨房。小区居民只要提前在手机上预约，就可以免费使用。厨房里有大锅、烤箱，还有一张能坐十二个人的大桌子。",
    "很多住在小公寓的年轻人说，自己家里的厨房太小，朋友来了没办法一起做饭。现在，他们周末常常在这里聚会。一些老人也喜欢来这里，教年轻人包粽子、做家乡菜。",
    "居委会的王主任说，开厨房的目的不只是做饭，更重要的是让邻居们认识彼此。“以前大家住在同一栋楼里，见面都不打招呼。现在，厨房成了小区的客厅。”",
    "不过，也有居民担心卫生问题。居委会表示，以后每次使用完，使用者都要负责打扫，下周还会安装监控。",
], 5)
Q.q("1.A.1 Detail", "How do residents get to use the kitchen?",
    "They book it in advance on their phones.", [("They pay a monthly fee.", "Use is free (免费使用)."),
                                                 ("They ask the committee director in person.", "Booking is done on the phone."),
                                                 ("They must be over sixty.", "No age limit; young people and elders both use it.")],
    "只要提前在手机上预约，就可以免费使用.", "只要……就 states the one condition: book ahead on the phone.",
    ["Find 只要 → the condition."])
Q.q("1.A.1 Detail", "Why do young residents like the kitchen?",
    "Their own kitchens are too small for cooking with friends.", [("They can learn to cook from professional chefs.", "The teachers are older residents, not chefs."),
                                                                  ("The food there is free.", "The space is free; the food is not mentioned as free."),
                                                                  ("They do not have stoves at home.", "They have kitchens, just small ones.")],
    "自己家里的厨房太小.", "The young people say their kitchens are too small to cook with friends.",
    ["很多……年轻人说: their reason follows."])
Q.q("1.B.1 Main idea", "According to Director Wang, what is the main purpose of the kitchen?",
    "to help neighbors get to know each other", [("to save residents money on food", "Money is not the stated purpose."),
                                                 ("to teach traditional cooking", "Teaching happens, but Wang says the more important aim is neighbors meeting."),
                                                 ("to replace the residents' living rooms", "厨房成了小区的客厅 is a metaphor for a gathering place.")],
    "不只是做饭，更重要的是让邻居们认识彼此.", "不只是 A，更重要的是 B: B is the main purpose.",
    ["更重要的是 marks the main point."])
Q.q("1.B.5 Word meaning", r"What does Wang mean by 厨房成了小区的客厅?",
    "The kitchen has become a place where the community gathers.", [("The kitchen was turned into a living room.", "It is still a kitchen; 客厅 is used figuratively."),
                                                                   ("Residents now cook in their living rooms.", "Literal reading; the sentence is a metaphor."),
                                                                   ("The kitchen is too crowded to cook in.", "Nothing suggests overcrowding.")],
    "客厅 = where a family receives guests → a social gathering place.", "A living room is where people gather and receive guests; calling the kitchen the community's living room means it is now the community's shared social space.",
    ["Contrast with 以前……见面都不打招呼."])
Q.q("1.C.3 Inference", "What concern is addressed at the end of the report?",
    "keeping the kitchen clean", [("noise late at night", "Noise is not mentioned."),
                                  ("the cost of electricity", "Cost is not mentioned."),
                                  ("too few residents using it", "The report says many people use it.")],
    "担心卫生问题 → 打扫, 监控.", "卫生 means hygiene/cleanliness; the committee responds with cleaning rules and cameras.",
    ["不过 signals the concern; 卫生 is the key word."])

Q.frq(kind="Email Response", head=r"Question 4 \textperiodcentered\ Email Response \textperiodcentered\ 8 points \textperiodcentered\ about 15 minutes",
      mins=15,
      directions=[r"\textbf{Directions.} Read the email from a friend. Write a reply in Chinese that responds to all the questions and requests in the email, in a culturally appropriate way."],
      prompt=[r"\textbf{发件人：}王小雨 \quad \textbf{主题：}请你帮我出出主意",
              "你好！好久没联系了。我有一件事想听听你的意见。我爷爷奶奶住在乡下，他们年纪大了，我爸妈想让他们搬到城里跟我们一起住，可是爷爷奶奶说住不惯城市，不想搬。你觉得爷爷奶奶应该搬来城里吗？为什么？另外，这个暑假我想为爷爷奶奶做一件有意义的事，你有什么好建议？",
              "等你的回信！小雨"],
      ask="Write your reply to 小雨 in Chinese.",
      model=["小雨，你好！",
             "收到你的邮件很高兴。关于你问的爷爷奶奶要不要搬到城里，我觉得最好先尊重他们自己的想法。首先，老人在乡下住了一辈子，那里有老邻居、老朋友，正所谓“远亲不如近邻”，突然搬到城里，他们可能会觉得孤单。其次，城里的公寓又小又吵，生活习惯也不一样。当然，你爸妈担心他们的身体，也很有道理。所以，我建议你们可以找一个折中的办法：比如让爷爷奶奶冬天来城里住几个月，夏天回乡下，或者请村里的邻居常常去看看他们。",
             "至于暑假做什么有意义的事，我有两个建议。一是跟爷爷奶奶住一个月，陪他们聊天、做家务，顺便教他们用手机视频，这样以后你们就能常常“见面”了。二是把爷爷奶奶年轻时候的故事录下来，做成一本家庭相册。这不但能让他们开心，而且也能让我们这些晚辈更了解家里的历史。",
             "希望我的建议对你有帮助。如果还有什么问题，随时告诉我！祝你暑假愉快！",
             "你的朋友 明明"],
      rows=[("Message development", 3, "Answers both questions directly (should they move: respect their wishes, with a compromise; a meaningful summer project: two specific ideas) with reasons and examples.", "Answering only one question; giving an opinion with no reason; a list of ideas with no detail."),
            ("Organization", 2, "Greeting and closing; one paragraph per request; cohesive devices (关于……，首先……其次……，当然……所以……，至于……，一是……二是……).", "No greeting or closing; both answers mixed in one paragraph."),
            ("Language control", 3, "Varied structures (不但……而且, 让, 把, 又……又, 这样……就) and culturally relevant expressions (远亲不如近邻, 晚辈, 尊重) in a consistent friendly register.", "Shifting between 你 and 您; basic vocabulary only; frequent errors.")],
      tips=[r"The reply restates each question before answering it (关于你问的…… / 至于……), so a reader can see both requests are covered. The saying is tied to the argument rather than dropped in, and the compromise shows nuance without dodging the question."])

GUIDE, QSET = G, Q
