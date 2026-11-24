from model import Doc

STEM = "04-science-technology"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 4: Science and Technology", r"Unit 4 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 4 asks what drives innovation, how technology changes communication, and what the social effects of scientific and technological change are. Its recommended contexts are innovations and emerging technologies, personal technology and communication, science in everyday life, and the societal impacts of science and technology. This guide covers the vocabulary of everyday digital life in Chinese-speaking communities (mobile payment, delivery, high-speed rail, AI), historic inventions, the language of change and comparison, the trade-offs that readings in this unit like to weigh, and a kit for the chart-based tasks (Audio and Chart, Article and Chart), where numbers and trends are tested. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 11+ \qquad Data words I mix up: \blank[10em]",
        short="Unit 4", sub="Science and Technology")

G.sec("Everyday technology")
G.tex(r"""
\begin{vocab}
智能手机 / 应用（App） & zhìnéng shǒujī / yìngyòng & smartphone / app \\
手机支付 / 扫码 / 二维码 & shǒujī zhīfù / sǎo mǎ / èrwéimǎ & mobile payment / to scan a code / QR code \\
网购 / 快递 / 外卖 & wǎnggòu / kuàidì / wàimài & online shopping / parcel delivery / food delivery \\
共享单车 & gòngxiǎng dānchē & shared bicycles \\
高铁 & gāotiě & high-speed rail \\
电动车 / 新能源汽车 & diàndòngchē / xīn néngyuán qìchē & e-bike or electric car / new-energy vehicle \\
人工智能（AI） & réngōng zhìnéng & artificial intelligence \\
机器人 & jīqìrén & robot \\
网上 / 线上 / 线下 & wǎngshàng / xiànshàng / xiànxià & online / online / offline, in person \\
视频通话 / 直播 & shìpín tōnghuà / zhíbō & video call / livestream \\
社交媒体 / 朋友圈 & shèjiāo méitǐ / péngyouquān & social media / WeChat ``Moments'' feed \\
下载 / 上传 / 更新 & xiàzài / shàngchuán / gēngxīn & download / upload / update \\
个人信息 / 隐私 & gèrén xìnxī / yǐnsī & personal information / privacy \\
\end{vocab}

\textbf{The cashless city.} In many Chinese cities people pay almost everything by scanning a QR code, from street food to utility bills, and red envelopes are sent by phone at New Year. \textbf{The delivery economy.} Food and parcels arrive within hours, carried by delivery riders (外卖小哥). \textbf{High-speed rail} has made trips of several hundred kilometers a matter of hours, which changes where people live and work and how they travel home at festivals.
""")
G.q("1 Vocabulary", r"扫码付款 means",
    "to pay by scanning a code", [("to scan a document for a teacher", "付款 is to pay; the phrase is about payment."),
                                 ("to order food delivery", "Ordering food is 点外卖."),
                                 ("to download an app", "Downloading is 下载.")],
    "扫码 (scan a code) + 付款 (pay).", "扫码付款 is the everyday QR-code payment.",
    ["Split the compound: 扫码 + 付款."])
G.q("1 Vocabulary", r"线下活动 is",
    "an in-person event", [("an online event", "Online is 线上."),
                           ("a canceled event", "Canceled is 取消."),
                           ("a livestream", "A livestream is 直播, which is online.")],
    "线上 = online; 线下 = offline, in person.", "线下 means off the line (the internet): face to face.",
    ["线上 vs. 线下."])
G.q("1 Vocabulary", r"A text says 高铁让“周末回老家”成为可能. What has high-speed rail made possible?",
    "going back to one's hometown for a weekend", [("moving permanently to the countryside", "The text is about a weekend trip."),
                                                  ("working from home on weekends", "Nothing about working from home."),
                                                  ("visiting relatives abroad", "高铁 is domestic rail; 老家 is one's hometown.")],
    "让……成为可能 = makes … possible.", "Faster trains make a short trip home realistic.",
    ["老家 = hometown; 周末 = weekend."])

G.sec("Inventions and scientific heritage")
G.tex(r"""
\begin{vocab}
四大发明 & sì dà fāmíng & the Four Great Inventions \\
造纸术 / 印刷术 / 指南针 / 火药 & zàozhǐshù / yìnshuāshù / zhǐnánzhēn / huǒyào & papermaking / printing / the compass / gunpowder \\
发明 / 发现 / 研究 & fāmíng / fāxiàn / yánjiū & to invent / to discover / to research \\
科学家 / 工程师 & kēxuéjiā / gōngchéngshī & scientist / engineer \\
中医 / 针灸 / 中药 & zhōngyī / zhēnjiǔ / zhōngyào & traditional Chinese medicine / acupuncture / herbal medicine \\
太空 / 宇航员 / 空间站 & tàikōng / yǔhángyuán / kōngjiānzhàn & space / astronaut / space station \\
实验 / 数据 / 结果 & shíyàn / shùjù / jiéguǒ & experiment / data / result \\
\end{vocab}

\textbf{Innovation from need.} Texts in this unit often explain an invention by the problem it solved: the compass for navigation, paper for cheaper recording, the abacus (算盘) for calculation. Use 为了解决……的问题 (in order to solve the problem of \ldots) to explain it.

\textbf{Tradition and science together.} Traditional medicine and modern medicine often coexist: many hospitals have both departments, and families may combine them. Readings present this as a matter of choice and balance, not as one replacing the other.
""")
G.q("2 Inventions", r"Which is NOT one of the 四大发明?",
    "算盘", [("指南针", "The compass is one of the four."),
             ("印刷术", "Printing is one of the four."),
             ("造纸术", "Papermaking is one of the four.")],
    "Four: paper, printing, compass, gunpowder.", "The abacus is an important Chinese invention, but it is not one of the traditional Four Great Inventions.",
    ["List the four; the abacus is not among them."])
G.q("2 Inventions", r"为了解决航海时迷路的问题，人们开始用指南针。 Why did people start using the compass?",
    "to avoid getting lost at sea", [("to measure the time", "That would be a clock."),
                                     ("to find gold", "No treasure is mentioned."),
                                     ("to print maps", "Printing is another invention.")],
    "为了解决……的问题 = to solve the problem of ….", "航海 (sailing) + 迷路 (getting lost): the problem the compass solved.",
    ["Read the problem inside 为了解决……的问题."])

G.sec("Language of change, comparison and data")
G.tex(r"""
\begin{compare}{Meaning}{Words and patterns}{Example}
Increase & 增加, 增长, 上升, 提高 & 用户增加了百分之二十。 \\
Decrease & 减少, 下降, 降低 & 现金使用率下降到了百分之十。 \\
Change \emph{by} vs.\ \emph{to} & 增加了 (by) vs.\ 增加到 (to) & 从100增加到150 = 增加了50 \\
Multiples & 倍：是……的两倍; 增加了一倍 (doubled) & 今年的销量是去年的三倍。 \\
Share & 占（百分之……） & 年轻人占用户的一半以上。 \\
Fractions & 三分之一, 四分之三 & 三分之二的人用手机支付。 \\
Approximation & 大约, 左右, 将近, 超过, 不到 & 将近一半；不到三成 \\
Tenths (成) & 一成 = 10\%, 七成 = 70\% & 七成的学生有自己的电脑。 \\
Trend & 越来越……, 随着……, 从……到…… & 随着网速提高，视频通话越来越普及。 \\
\end{compare}

\begin{trap}
增加了一倍 means \emph{doubled} (increased by 100\%), not ``increased by one.'' And 成 counts tenths: 三成 is 30\%, not 3\%. These two are the most common chart-question traps.
\end{trap}
""")
G.q("3 Data", r"去年有200名学生参加，今年增加了一倍。 How many students joined this year?",
    "400", [("201", "增加了一倍 does not mean “increased by one.”"),
            ("300", "That would be an increase of half (增加了一半)."),
            ("200", "200 is last year's number.")],
    "增加了一倍 = doubled.", "倍 means a multiple; increasing by one 倍 adds 100% of the original.",
    ["200 + 200 = 400."])
G.q("3 Data", r"三成的家长担心孩子用手机的时间太长。 What share of parents is worried?",
    "30\\%", [("3\\%", "成 means tenths: 三成 = 3/10 = 30%."),
              ("one third", "One third is 三分之一."),
              ("three quarters", "Three quarters is 四分之三.")],
    "成 = tenth.", "One 成 is 10%, so 三成 is 30%.",
    ["3 × 10% = 30%."])
G.q("3 Data", r"现金支付的比例从百分之六十下降到了百分之十五。 By how many percentage points did it fall?",
    "45", [("15", "15% is the new level (下降到 = fell to)."),
           ("60", "60% is the starting level."),
           ("75", "75 is 60 + 15; the size of a drop is the difference, 60 − 15.")],
    "下降到 = fell to; drop = 60 − 15.", "到 marks the end point, so subtract: 60 − 15 = 45 points.",
    ["从 60 … 到 15 → difference 45."])

G.sec("Trade-offs and perspectives")
G.tex(r"""
Unit 4 readings rarely praise or condemn technology outright; they weigh it. Learn the vocabulary of both sides and the frames that balance them.

\begin{compare}{Topic}{Benefits (好处 / 优点)}{Concerns (坏处 / 缺点 / 问题)}
Mobile payment & 方便、快, no cash to carry & 老年人不会用 (the digital gap), 隐私, 花钱太容易 \\
Social media & 跟远方的家人保持联系 & 低头族 (people glued to their phones), 网瘾, 假消息 \\
AI & 提高效率, new medical tools & 工作被取代, 抄袭 (copying), 依赖 \\
Delivery and e-commerce & 省时间, more choice & 包装垃圾, riders' working conditions \\
\end{compare}

\begin{compare}{Frame}{Use}{Example}
一方面……另一方面…… & two sides & 一方面手机让沟通更方便，另一方面也让面对面交流变少了。 \\
有利也有弊 / 是一把双刃剑 & it cuts both ways & 人工智能是一把双刃剑。 \\
关键在于…… & the key lies in \ldots & 关键在于怎么使用。 \\
对……有好处 / 有影响 & good for / affects & 长时间看屏幕对眼睛有影响。 \\
\end{compare}

\textbf{Perspectives behind the practices.} Families teaching grandparents to use phones reflects intergenerational care; community ``smart-phone classes'' for elders reflect the value of including everyone (不让一个老人掉队: not letting a single elder fall behind).
""")
G.q("4 Trade-offs", r"人工智能是一把双刃剑 means AI",
    "has both benefits and dangers", [("is a dangerous weapon", "The sword image is a metaphor for two edges, two sides."),
                                     ("will replace all teachers", "No such claim is made."),
                                     ("is only useful in the military", "Nothing about the military.")],
    "双刃剑 = double-edged sword.", "Like a blade with two edges, it can help and harm.",
    ["Metaphor → both sides."])
G.q("4 Perspectives", r"A community runs free classes teaching elders to pay by phone and make video calls. Which perspective does this most directly reflect?",
    "No one should be left behind by technological change.", [("Elders should stop using cash immediately.", "The class helps elders; it does not ban cash."),
                                                            ("Technology is only for the young.", "The class exists because the community believes otherwise."),
                                                            ("Video calls should replace family visits.", "The aim is inclusion, not replacing visits.")],
    "Inclusion: 不让一个老人掉队.", "Teaching elders closes the digital gap; the value behind the practice is inclusion and care across generations.",
    ["Practice: classes for elders → perspective: inclusion."])

G.sec("Task kit: charts and the Email Response")
G.tex(r"""
\subsection{Reading a chart in five seconds}
\begin{enumerate}[leftmargin=2em]
\item Title: what is measured (使用率, 人数, 时间)?
\item Units: percent (\%), people (人), hours (小时), yuan (元)?
\item Axis or columns: which years, which groups?
\item The shape: rising, falling, a peak, a dip?
\item Then read the question, and check the text for the \emph{reason} behind the shape.
\end{enumerate}

\subsection{Technology emails}
Unit 4 emails often ask for a recommendation (which device, which app, whether to try online classes) and how to handle a problem (too much screen time, a grandparent who can't use a phone). Answer with a recommendation plus reasons, then concrete steps:

\begin{keyidea}[Steps and advice]
你可以先……，然后……，最后…… \quad 我的经验是…… \quad 最好别…… \quad 如果……的话，可以试试…… \quad 关键在于……
\end{keyidea}
""")
G.q("5 Charts", "Before answering a chart question, which should you check first?",
    "what is measured and in what units", [("which choice is longest", "Choice length tells you nothing."),
                                          ("the last number only", "The trend needs every point."),
                                          ("whether you agree with the article", "Your opinion is not tested.")],
    "Title and units first.", "Most chart errors come from misreading what is measured (percent vs. people) or the units.",
    ["Title → units → categories → shape."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 4: Science and Technology: Question Set", r"Unit 4 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Audio Report and Instructional Guidance for listening, Article and Chart and Promotional Material for reading) on mobile payment, AI at school, robots and the digital gap, followed by an Email Response with a scoring guide and a model reply. Listening sources are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 15 minutes for the email.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Email: \blank\ / 8 \qquad Target: 16+ MCQ and 6+ email \qquad Pace: 75 s per item",
        short="Unit 4", sub="Science and Technology")

Q.sec("Listening: Audio Report")
Q.src(r"Listening 1 \textperiodcentered\ Audio Report (transcript) \textperiodcentered\ A news report", [
    "各位听众，下面是一条科技新闻。",
    "从下个月一号开始，本市的三十家社区医院将试用一种新的“AI导诊机器人”。病人到医院以后，可以先跟机器人说说自己哪里不舒服，机器人会告诉病人应该去哪个科室，还能帮忙挂号。",
    "医院的李院长说，过去病人常常不知道该看哪个科，排错了队，浪费很多时间。试用机器人以后，估计每位病人平均可以节省二十分钟。",
    "不过，李院长也强调，机器人只能“指路”，不能代替医生看病。考虑到很多老年人不习惯跟机器说话，每台机器人旁边都会安排一名志愿者帮忙。",
    "如果试用效果好，明年全市所有的社区医院都会使用这种机器人。",
], 5)
Q.q("1.B.1 Main idea", "What is the report mainly about?",
    "community hospitals trying out AI robots that direct patients", [("robots replacing doctors in hospitals", "The director stresses robots cannot replace doctors."),
                                                                     ("a shortage of volunteers at hospitals", "Volunteers are assigned; no shortage is reported."),
                                                                     ("a new hospital being built", "Existing hospitals are trying a new tool.")],
    "试用一种新的“AI导诊机器人”.", "The second paragraph names the main news: a trial of AI guide robots.",
    ["The main news usually follows the introduction."])
Q.q("1.A.1 Detail", "What can the robot do for patients?",
    "tell them which department to go to and help them register", [("diagnose their illness", "It only “points the way”; it does not diagnose."),
                                                                 ("give them medicine", "No medicine is mentioned."),
                                                                 ("drive them home", "Nothing about transport.")],
    "告诉病人应该去哪个科室，还能帮忙挂号.", "科室 is a hospital department; 挂号 is registering for an appointment.",
    ["Listen for what the robot 会 and 能 do."])
Q.q("1.A.2 Data", "How much time is each patient expected to save, on average?",
    "about twenty minutes", [("about two hours", "The figure is 二十分钟."),
                             ("about two minutes", "二十 is twenty."),
                             ("a full day", "Nothing so large is claimed.")],
    "平均可以节省二十分钟.", "估计 (estimated) and 平均 (on average) frame the figure: twenty minutes.",
    ["节省 + number."])
Q.q("1.C.3 Inference", "Why will volunteers stand next to each robot?",
    "Many older patients are not used to talking to machines.", [("The robots often break down.", "Breakdowns are not mentioned."),
                                                                ("Volunteers will replace the robots next year.", "If the trial works, more robots will be used."),
                                                                ("Doctors are too busy to explain the robots.", "Doctors are not mentioned in that sentence.")],
    "考虑到很多老年人不习惯跟机器说话.", "考虑到 (taking into account) gives the reason for the volunteers.",
    ["考虑到 → reason."])
Q.q("1.A.1 Detail", "What will happen if the trial goes well?",
    "All community hospitals in the city will use the robots next year.", [("The robots will start treating patients.", "Their role stays guidance."),
                                                                          ("The trial will be stopped.", "Stopping would follow a poor trial."),
                                                                          ("The hospitals will hire fewer doctors.", "Nothing about staffing.")],
    "如果试用效果好，明年全市所有的社区医院都会使用.", "The final sentence states the condition and the result.",
    ["如果……都会……"])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ From a school newspaper", [
    "\\textbf{AI 来到了我们的作业里}",
    "上学期，学校开始允许学生在写作文以前用AI工具找资料、列提纲，但是规定作文本身必须自己写。这学期，学校报社对四百名高中生做了一个调查。",
    "调查发现，用AI“查资料”的学生最多，“改语法”的其次，而承认用AI“直接写作文”的学生不到一成。",
    "语文老师王老师说，AI让学生找资料快多了，这是好事。但是她也发现，一些学生的作文“越来越像”，用的例子差不多，句子也很相似。“工具本身没有好坏，关键在于怎么用。如果连自己的想法都交给机器，那写作就没有意义了。”",
    "学校决定，从下个月开始，每篇作文都要附一张“写作过程表”，写清楚哪些部分用了AI、怎么用的。",
], 5, table=(["用AI做什么（可多选）", "学生比例"], [["查资料", "71\\%"], ["改语法", "48\\%"], ["列提纲", "35\\%"], ["直接写作文", "8\\%"]]),
   note="Chart: What 400 high school students use AI for (more than one answer allowed; fictional data)")
Q.q("1.A.2 Data", "According to the chart, what share of students use AI to fix grammar?",
    "48\\%", [("71\\%", "71% is for finding information."),
              ("35\\%", "35% is for outlines."),
              ("8\\%", "8% is for writing whole essays.")],
    "改语法 → 48%.", "Match the row label to its number.",
    ["Find 改语法 in the chart."])
Q.q("1.C.1 Connect", r"How does the chart support the article's statement 直接写作文的学生不到一成?",
    "8\\% is less than one tenth.", [("71\\% is more than half.", "This is about finding information, not writing essays."),
                                     ("The percentages add up to more than 100\\%.", "True (multiple answers allowed), but irrelevant to 不到一成."),
                                     ("35\\% is about one third.", "This concerns outlines.")],
    "不到一成 = under 10%; chart: 8%.", "一成 is one tenth (10%), and 8% is below it.",
    ["成 = tenth."])
Q.q("1.A.1 Detail", "What were students allowed to do with AI last semester?",
    "find information and make outlines before writing", [("write the essay itself", "The rule says the essay must be the student's own writing."),
                                                          ("take tests", "Tests are not mentioned."),
                                                          ("grade other students' essays", "Not mentioned.")],
    "用AI工具找资料、列提纲，但是规定作文本身必须自己写.", "The permitted uses come before 但是; the restriction after it.",
    ["允许 → permitted; 但是规定 → restriction."])
Q.q("1.B.3 Point of view", "What is Teacher Wang's view of AI?",
    "It is a neutral tool; what matters is how students use it.", [("It should be banned at school.", "She calls faster research a good thing."),
                                                                 ("It makes every essay better.", "She notices essays becoming too similar."),
                                                                 ("It is more creative than students.", "She worries about students handing over their own ideas.")],
    "工具本身没有好坏，关键在于怎么用.", "She sees a benefit and a risk, and puts the responsibility on how it is used.",
    ["关键在于 → her main point."])
Q.q("1.C.2 Conclusion", "What is the purpose of the new 写作过程表?",
    "to make students state clearly how they used AI", [("to ban AI completely", "It records AI use rather than banning it."),
                                                       ("to grade grammar", "It is about the process, not grammar."),
                                                       ("to replace the essay", "It is attached to each essay (附).")],
    "写清楚哪些部分用了AI、怎么用的.", "The form makes AI use transparent.",
    ["学校决定 → the new rule and its content."])

Q.sec("Reading: Promotional Material")
Q.src(r"Reading 2 \textperiodcentered\ Promotional Material \textperiodcentered\ A community notice", [
    "\\textbf{“银发上网”智能手机课堂 —— 让爷爷奶奶跟上时代！}",
    "您会用手机扫码买菜吗？会跟远方的孙子孙女视频聊天吗？会在网上挂号吗？",
    "明光社区和明光中学的学生志愿者一起，为六十岁以上的居民开设免费的智能手机课。",
    "课程内容：第一课 视频通话；第二课 扫码支付；第三课 网上挂号；第四课 识别网络诈骗",
    "时间：每周二、周四上午十点（每课一小时）　地点：社区活动中心二楼",
    "一对一教学，请带上自己的手机。家人可以陪同。",
    "报名：社区服务台，或请家人在“明光社区”小程序上报名。",
], 5)
Q.q("1.B.2 Audience", "Who is the class for?",
    "residents aged sixty and above", [("high school students", "The students are the teachers (志愿者)."),
                                      ("people who want to buy phones", "Participants bring their own phones."),
                                      ("children of the residents", "Family may accompany, but the class is for elders.")],
    "为六十岁以上的居民开设.", "以上 = and above; the title's 银发 (silver hair) also signals older people.",
    ["Find 为……开设."])
Q.q("1.A.1 Detail", "What will be taught in the fourth lesson?",
    "how to recognize online scams", [("how to make video calls", "That is lesson 1."),
                                     ("how to pay by scanning", "That is lesson 2."),
                                     ("how to book a doctor online", "That is lesson 3.")],
    "第四课 识别网络诈骗.", "识别 is to identify; 诈骗 is fraud or a scam.",
    ["第四课 → its content."])
Q.q("1.A.1 Detail", "What should participants bring?",
    "their own phones", [("a family member", "Family may come (可以陪同) but are not required."),
                         ("a fee", "The class is free."),
                         ("a laptop", "The class is about smartphones.")],
    "请带上自己的手机.", "The notice asks participants to bring their own phones for one-on-one teaching.",
    ["请带上 → what to bring."])
Q.q("1.B.5 Word meaning", r"In the title, 跟上时代 most nearly means",
    "keep up with the times", [("go back to the past", "跟上 is to keep pace with, not to go back."),
                               ("follow a famous person", "时代 is an era, not a person."),
                               ("become younger", "The goal is keeping up, not age.")],
    "跟上 (keep pace with) + 时代 (the era).", "The title invites elders to keep pace with modern technology.",
    ["跟上 = keep up with."])
Q.q("1.C.3 Inference", "Why does the notice suggest asking family members to register on the mini-program?",
    "Some elders may not yet be able to register online themselves.", [("The service desk is closed.", "The service desk is offered as an option."),
                                                                    ("Only family members may attend.", "The class is for the elders."),
                                                                    ("Registration costs money online.", "The class is free.")],
    "请家人在……小程序上报名.", "The audience is still learning to use phones, so the notice offers family help with online sign-up.",
    ["Connect the audience (elders learning phones) with the request."])

Q.sec("Listening: Instructional Guidance")
Q.src(r"Listening 2 \textperiodcentered\ Instructional Guidance (transcript) \textperiodcentered\ A science teacher before an experiment", [
    "同学们，今天我们来做“自制净水器”的实验。请先听我说完，再动手。",
    "第一步，把塑料瓶的底部剪掉，然后把瓶子倒过来，瓶口朝下。第二步，按顺序放进材料：最下面放棉花，再放活性炭，然后是细沙，最上面放小石子。注意顺序不能错，不然水会流得太快，过滤不干净。",
    "第三步，慢慢地把脏水倒进去，用杯子接住流出来的水，观察颜色有什么变化。",
    "请大家记住：过滤以后的水看起来干净了，但是里面可能还有细菌，所以绝对不能喝。",
    "做完以后，每组用手机拍一张前后对比的照片，上传到班级网站，并写三句话说明你们的发现。好，现在开始吧。",
], 5)
Q.q("1.A.1 Sequence", "What goes at the very bottom of the bottle (near the opening)?",
    "cotton", [("small stones", "Stones go on top."),
               ("fine sand", "Sand is third from the bottom."),
               ("activated charcoal", "Charcoal goes just above the cotton.")],
    "最下面放棉花.", "The order from bottom to top: cotton, charcoal, fine sand, small stones.",
    ["最下面 = the very bottom."])
Q.q("1.A.1 Detail", "What happens if the materials are in the wrong order?",
    "The water flows too fast and is not filtered well.", [("The bottle will break.", "Not mentioned."),
                                                          ("The water will turn black.", "Color change is observed, but not given as the result of a wrong order."),
                                                          ("The experiment will take too long.", "The problem is speed in the other direction: too fast.")],
    "不然水会流得太快，过滤不干净.", "不然 (otherwise) introduces the consequence.",
    ["不然 → consequence."])
Q.q("1.B.3 Emphasis", "Which warning does the teacher stress most strongly?",
    "Do not drink the filtered water.", [("Do not cut the bottle.", "Cutting the bottle is step one."),
                                         ("Do not use your phones.", "Phones are used to take photos."),
                                         ("Do not pour water too slowly.", "The teacher says to pour slowly.")],
    "绝对不能喝.", "绝对不能 (absolutely must not) is the strongest prohibition in the instructions.",
    ["请大家记住 + 绝对不能."])
Q.q("1.C.3 Inference", "Why can't the water be drunk even if it looks clean?",
    "It may still contain bacteria.", [("It still contains sand.", "The reason given is bacteria."),
                                       ("It is too cold.", "Temperature is not mentioned."),
                                       ("It has charcoal in it.", "The reason given is bacteria.")],
    "里面可能还有细菌.", "但是 introduces the hidden risk: bacteria the filter cannot remove.",
    ["看起来干净了，但是…… → the reason."])
Q.q("1.A.1 Detail", "What must each group do after the experiment?",
    "post a before-and-after photo with a three-sentence explanation", [("write a five-page report", "Only three sentences are required."),
                                                                         ("drink a cup of the filtered water", "Drinking is forbidden."),
                                                                         ("present the filter to the principal", "No principal is mentioned.")],
    "拍一张前后对比的照片，上传……并写三句话.", "The final instruction lists the photo, the upload and three sentences.",
    ["做完以后 → the final task."])

Q.frq(kind="Email Response", head=r"Question 4 \textperiodcentered\ Email Response \textperiodcentered\ 8 points \textperiodcentered\ about 15 minutes",
      mins=15,
      directions=[r"\textbf{Directions.} Read the email from a member of your community. Write a reply in Chinese that responds to all the questions and requests in the email, in a culturally appropriate way."],
      prompt=[r"\textbf{发件人：}社区中心 赵阿姨 \quad \textbf{主题：}请你提提建议",
              "同学你好！我是社区中心的赵阿姨。听说你很会用电脑和手机。下个月我们想给社区里的老人开一个智能手机课，但是不知道应该先教什么。你觉得老人最需要学的是哪些功能？为什么？另外，有的老人担心学不会，不敢报名，你觉得我们应该怎么鼓励他们？",
              "谢谢你！赵阿姨"],
      ask="Write your reply to 赵阿姨 in Chinese.",
      model=["赵阿姨，您好！",
             "谢谢您的来信，能为社区的老人帮忙，我很高兴。关于您问的应该先教什么，我认为最需要的是两个功能。首先是视频通话。很多老人的子女在外地工作，如果会视频，他们就可以常常“见到”孙子孙女，不会那么孤单。其次是识别网络诈骗。现在骗子越来越多，专门骗老年人，所以教他们怎么保护个人信息，比学扫码付款还重要。",
             "至于怎么鼓励担心学不会的老人，我有几个建议。第一，可以请学生志愿者一对一地教，进度慢一点，一个功能多练几次。第二，请已经学会的老人来分享经验，大家听到同龄人也能学会，就不会那么紧张了。第三，可以让家人陪着来，这样老人更放心。俗话说“活到老，学到老”，只要有耐心，谁都能学会。",
             "如果需要志愿者，我和我的同学都很愿意参加。祝您工作顺利，身体健康！",
             "社区的学生 李安"],
      rows=[("Message development", 3, "Answers both questions: which functions and why (video calls for family ties; fraud awareness for safety), and how to encourage hesitant elders (three specific ideas).", "Listing functions with no reasons; ignoring the encouragement question."),
            ("Organization", 2, "Greeting and closing; 关于……，首先……其次……，至于……，第一……第二……第三.", "Run-on list; no closing."),
            ("Language control", 3, "Respectful register throughout (您); varied structures (如果……就, 比……还, 只要……就, 让); culturally relevant expression (活到老，学到老).", "Switching to 你; basic vocabulary; errors with 的/得/地.")],
      tips=[r"The reply ranks fraud awareness above payment and says why, which is the kind of detail that separates a 3 from a 2 in message development. The offer to volunteer is a natural, culturally appropriate close for a community email."])

GUIDE, QSET = G, Q
