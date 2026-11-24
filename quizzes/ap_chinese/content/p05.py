from model import Doc

STEM = "05-contemporary-life"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 5: Contemporary Life", r"Unit 5 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 5 asks how daily life has changed in the last twenty years, how values and traditions shape it, and what shapes people's sense of what matters. Its recommended contexts are education and career, entertainment and media, food and health, pop culture, sports and leisure, and travel and tourism. This guide covers the vocabulary of school and work, food and health, and leisure and travel; the condition and purpose patterns these topics run on; the perspectives behind them (education as family investment, food as social life, balance and health); and a kit for the promotional and correspondence reading tasks, where dates, prices and conditions are tested. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 11+ \qquad Patterns I mix up: \blank[10em]",
        short="Unit 5", sub="Contemporary Life")

G.sec("Education and career")
G.tex(r"""
\begin{vocab}
高考 & gāokǎo & the national college entrance exam \\
中考 & zhōngkǎo & the senior-high entrance exam \\
补习班 / 课外班 & bǔxíbān / kèwàibān & cram school / after-school class \\
重点学校 & zhòngdiǎn xuéxiào & key (selective) school \\
专业 / 选专业 & zhuānyè & college major / to choose a major \\
留学 / 出国留学 & liúxué & to study abroad \\
毕业 / 找工作 / 求职 & bìyè / zhǎo gōngzuò / qiúzhí & to graduate / to look for work / to job-hunt \\
实习 / 面试 / 简历 & shíxí / miànshì / jiǎnlì & internship / interview / résumé \\
压力 / 竞争 & yālì / jìngzhēng & pressure / competition \\
内卷 & nèijuǎn & ``involution'': exhausting competition with little real gain (media term) \\
减负 & jiǎnfù & reducing students' workload \\
兴趣 / 特长 & xìngqù / tècháng & interest / special skill \\
理想 / 梦想 & lǐxiǎng / mèngxiǎng & ideal, aspiration / dream \\
\end{vocab}

\textbf{The exam and the family.} The 高考 shapes years of schooling, and families invest time and money in it (望子成龙, 望女成凤: hoping one's son becomes a dragon, one's daughter a phoenix). Recent readings often present the other side too: policies to reduce homework and after-school tutoring (减负, the 2021 ``double reduction'' policy, 双减), students who choose majors by interest, and the debate over 内卷.
""")
G.q("1 Education", r"望女成凤 describes",
    "parents' high hopes for their daughter's success", [("a daughter who wants to become a dancer", "凤 (phoenix) is a symbol of excellence, not a profession."),
                                                       ("a family that keeps birds", "The phoenix is figurative."),
                                                       ("parents who let their daughter choose freely", "The idiom stresses parents' expectations.")],
    "望 (hope) + 女 (daughter) + 成凤 (become a phoenix).", "It parallels 望子成龙: parents' hope that their child will excel.",
    ["Dragon and phoenix = excellence."])
G.q("1 Education", r"A reading says many students feel 内卷. They feel",
    "stuck in intense competition that leaves everyone exhausted for little gain", [("excited to compete in sports", "内卷 is negative and is not about sports."),
                                                                                   ("bored because school is too easy", "The term describes too much pressure, not too little."),
                                                                                   ("happy with their grades", "The term is a complaint.")],
    "内卷 = draining over-competition.", "内卷 is a media term for competition that intensifies without making anyone better off.",
    ["Negative media term → pressure, exhaustion."])
G.q("1 Education", r"减负 refers to",
    "reducing students' workload", [("reducing school fees", "Fees are 学费."),
                                     ("reducing the number of teachers", "Not about staffing."),
                                     ("reducing students' weight", "负 is burden, not body weight.")],
    "减 (reduce) + 负 (burden).", "减负 policies aim to lighten homework and tutoring.",
    ["负 = 负担, burden."])

G.sec("Food, health and leisure")
G.tex(r"""
\begin{vocab}
八大菜系 & bā dà càixì & the eight great regional cuisines (川, 鲁, 粤, 苏, 浙, 闽, 湘, 徽) \\
川菜 / 粤菜 & chuāncài / yuècài & Sichuan cuisine (spicy, numbing) / Cantonese cuisine (fresh, light) \\
早茶 & zǎochá & Cantonese morning tea with dim sum \\
口味 / 清淡 / 油腻 & kǒuwèi / qīngdàn / yóunì & taste / light / greasy \\
健康 / 营养 / 均衡 & jiànkāng / yíngyǎng / jūnhéng & healthy / nutrition / balanced \\
锻炼 / 健身 / 跑步 & duànliàn / jiànshēn / pǎobù & to exercise / to work out / to run \\
太极拳 / 广场舞 & tàijíquán / guǎngchǎngwǔ & tai chi / square dancing \\
熬夜 & áoyè & to stay up late \\
旅游 / 旅行 / 自由行 & lǚyóu / lǚxíng / zìyóuxíng & tourism / travel / independent travel \\
黄金周 & huángjīnzhōu & ``golden week'' (the long National Day holiday) \\
景点 / 门票 / 预订 & jǐngdiǎn / ménpiào / yùdìng & sight / admission ticket / to book \\
综艺节目 / 电视剧 / 网红 & zōngyì jiémù / diànshìjù / wǎnghóng & variety show / TV series / internet celebrity \\
\end{vocab}

\textbf{Food as social life.} 民以食为天 (for the people, food is heaven) is often quoted; meals mark celebrations, business, friendship and family. Paying for the group (请客) and ordering dishes to share are common practices. \textbf{Health} is often framed as balance (平衡): diet, rest, exercise, and the old idea of 养生 (nurturing life).
""")
G.q("2 Food", r"民以食为天 expresses the idea that",
    "food is central to people's lives", [("people should eat less", "The saying elevates food; it does not limit it."),
                                         ("heaven decides what people eat", "天 here means what matters most."),
                                         ("farmers are more important than emperors", "The saying is about food, not ranking people.")],
    "以 A 为 B = treat A as B: food is heaven.", "The saying says food is what people care about most.",
    ["以……为…… = regard … as …."])
G.q("2 Leisure", r"A traveler wants to avoid crowds. Which period should she avoid?",
    "黄金周", [("工作日", "Weekdays are usually less crowded."),
               ("淡季", "淡季 is the off-season, the quietest time."),
               ("周三上午", "A weekday morning is a quiet time.")],
    "黄金周 = peak holiday travel week.", "The National Day golden week is one of the busiest travel periods of the year.",
    ["Golden week → crowds."])
G.q("2 Health", r"他最近常常熬夜，所以白天没精神。 What is his problem?",
    "He stays up late and is tired during the day.", [("He eats too much at night.", "熬夜 is staying up late, not eating."),
                                                     ("He exercises too hard.", "No exercise is mentioned."),
                                                     ("He cannot find work.", "Not about work.")],
    "熬夜 = stay up late; 没精神 = tired, low energy.", "The cause (熬夜) and effect (没精神) are joined by 所以.",
    ["Cause → effect."])

G.sec("Patterns for conditions, purposes and choices")
G.tex(r"""
\begin{compare}{Pattern}{Meaning}{Example}
只要……就…… & as long as (sufficient) & 只要每天练习，就会进步。 \\
只有……才…… & only if (necessary) & 只有考上大学，才能当医生。 \\
无论/不管……都…… & no matter & 不管多忙，他都会运动半小时。 \\
为了…… & in order to & 为了减压，她开始学画画。 \\
宁可……也不…… & would rather \ldots\ than & 他宁可走路，也不坐拥挤的地铁。 \\
不得不 / 只好 & have to / have no choice but to & 下雨了，我们只好改天去。 \\
难怪…… & no wonder & 他天天熬夜，难怪成绩下降了。 \\
要不是……就…… & if it weren't for \ldots & 要不是你提醒我，我就忘了。 \\
\end{compare}

\begin{trap}
只要 names a condition that is \emph{enough}; 只有 names the \emph{only} condition. ``只有报名的人才能参加'' means people who did not register cannot attend, a meaning that 只要 would not carry. Promotional texts use 只有 for restrictions and 只要 for easy offers (只要扫码，就能打折).
\end{trap}
""")
G.q("3 Conditions", r"只有提前预订的客人，才能参加今晚的活动。 What does this mean?",
    "Guests who did not book in advance cannot attend.", [("Anyone can attend tonight.", "只有……才 restricts attendance."),
                                                           ("Booking is recommended but not necessary.", "只有 makes it necessary."),
                                                           ("Guests can book at the door tonight.", "提前 means in advance.")],
    "只有 = the only way.", "只有……才 sets a necessary condition.",
    ["Necessary condition → others excluded."])
G.q("3 Choices", r"他宁可走路，也不坐拥挤的地铁。 What does he prefer?",
    "walking rather than taking the crowded subway", [("taking the subway rather than walking", "Reversed: 宁可 marks the preferred option."),
                                                      ("taking a taxi", "No taxi is mentioned."),
                                                      ("staying at home", "He still goes, on foot.")],
    "宁可 A，也不 B = would rather A than B.", "宁可 introduces the choice he accepts despite its cost.",
    ["宁可 → preferred option."])
G.q("3 Inference", r"他每天都打三个小时游戏，难怪眼睛不舒服。 难怪 shows that the speaker",
    "finds the result unsurprising given the cause", [("is surprised by the result", "难怪 means “no wonder”: the opposite of surprise."),
                                                      ("disagrees with the cause", "难怪 explains; it does not argue."),
                                                      ("is asking a question", "It is a statement.")],
    "难怪 = no wonder.", "难怪 links a known cause to an effect that now makes sense.",
    ["Cause (3 hours of games) → unsurprising effect."])

G.sec("Perspectives in contemporary life")
G.tex(r"""
\begin{compare}{Perspective}{Practices and products}{Ways to discuss it}
Education as a family investment & Tutoring, school-district housing (学区房), grandparents' help & 望子成龙；但也有人认为快乐和健康更重要 \\
Hard work and endurance (吃苦) & Long study hours; ``吃得苦中苦，方为人上人'' & 吃苦耐劳 vs.\ 劳逸结合（balancing work and rest） \\
Face and social harmony (面子, 和) & Hosting guests generously; indirect refusals & 给面子, 委婉 (tactful) \\
Health as balance (养生) & Warm water, tai chi, seasonal foods & 平衡, 劳逸结合 \\
Change and choice & Gap years, 斜杠青年 (people with several careers), 自由行 & 越来越多的年轻人选择…… \\
\end{compare}

When writing about these topics, present a perspective and its counterpart: \emph{一方面，很多家长认为……；另一方面，越来越多的年轻人觉得……。} That balance is what Unit 5 readings model, and it reads as nuance in the Q\&A.
""")
G.q("4 Perspectives", r"劳逸结合 expresses the value of",
    "balancing work and rest", [("working without rest", "逸 is leisure; the phrase combines work and rest."),
                                ("retiring early", "Not about retirement."),
                                ("studying only what you enjoy", "Not about choice of subject.")],
    "劳 (work) + 逸 (rest) + 结合 (combine).", "The phrase is used to argue against nonstop study or work.",
    ["Break down the four characters."])
G.q("4 Perspectives", r"A host insists on paying for everyone's dinner and orders far more dishes than the group can eat. Which perspective best explains this practice?",
    "generosity to guests shows respect and maintains face", [("the host dislikes leftovers", "Ordering extra makes leftovers likely."),
                                                           ("the guests are expected to pay later", "The host insists on paying."),
                                                           ("food is cheaper in large amounts", "Cost saving is not the motive.")],
    "请客 + abundance ↔ 面子 and hospitality.", "Generous hosting honors the guests and shows the host's sincerity: face and hospitality.",
    ["Practice: paying and ordering plenty → perspective: respect, face."])

G.sec("Task kit: promotional texts and correspondence")
G.tex(r"""
\begin{vocab}
优惠 / 打折 / 打八折 & yōuhuì / dǎzhé / dǎ bā zhé & discount / to discount / 20\% off (pay 80\%) \\
免费 / 买一送一 & miǎnfèi / mǎi yī sòng yī & free / buy one, get one free \\
报名 / 截止日期 & bàomíng / jiézhǐ rìqī & to sign up / deadline \\
名额有限 / 先到先得 & míng'é yǒuxiàn / xiān dào xiān dé & limited places / first come, first served \\
凭……入场 & píng \ldots\ rùchǎng & admission with (a ticket, ID) \\
含 / 不含 & hán / bù hán & including / not including \\
详情 / 咨询 & xiángqíng / zīxún & details / to inquire \\
\end{vocab}

\begin{trap}
打八折 means you pay 80\% (20\% off), not 80\% off. 打五折 is half price. Price questions also hide conditions: 学生凭学生证 (students with ID), 满100减20 (spend 100, get 20 off), 不含午餐 (lunch not included).
\end{trap}
""")
G.q("5 Promotions", r"A jacket costs 500 yuan. The store says 全场打八折. What do you pay?",
    "400 yuan", [("100 yuan", "That would be 80% off; 打八折 means you pay 80%."),
                 ("420 yuan", "Subtract 20% of 500 (100), not 80."),
                 ("480 yuan", "That is a 20-yuan discount, not 20%.")],
    "打八折 = pay 80%: 500 × 0.8 = 400.", "Chinese discounts name the share you pay, in tenths.",
    ["八折 = 0.8 × price."])
G.q("5 Promotions", r"名额有限，先到先得 tells readers to",
    "act quickly because places are limited", [("pay a deposit", "No deposit is mentioned."),
                                              ("bring a friend", "Not mentioned."),
                                              ("wait for a second announcement", "The phrase urges acting now.")],
    "先到先得 = first come, first served.", "Limited places plus first-come-first-served signals urgency.",
    ["Two phrases, one message: hurry."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 5: Contemporary Life: Question Set", r"Unit 5 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (a Conversation and a Presentation for listening, Promotional Material and Correspondence for reading) on choosing a major, a city half-marathon, food and family, and a gap year, followed by a Story Narration task with a scoring guide and a model story. Listening sources are printed as transcripts. All sources are original and written for practice. Allow about 25 minutes for the multiple choice and 15 minutes for the story.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Story: \blank\ / 8 \qquad Target: 16+ MCQ and 6+ story \qquad Pace: 75 s per item",
        short="Unit 5", sub="Contemporary Life")

Q.sec("Listening: Conversation")
Q.src(r"Listening 1 \textperiodcentered\ Conversation (transcript) \textperiodcentered\ A student and her father talk about college majors", [
    "女：爸，我想跟您商量一件事。大学的专业，我不想选金融了，我想学设计。",
    "男：设计？你数学那么好，学金融以后工作好找，收入也高。设计以后能做什么呢？",
    "女：设计的工作其实很多，比如产品设计、用户界面设计。现在很多科技公司都需要。而且，我每次画画都觉得时间过得特别快，学金融的时候就没有这种感觉。",
    "男：喜欢是一回事，能不能找到工作是另一回事。",
    "女：我知道。所以我打算这个暑假先去王阿姨的设计公司实习两个月，看看自己到底适不适合。如果不适合，我再考虑金融。",
    "男：嗯……这个办法倒是不错。那好吧，实习完了我们再好好谈谈。",
], 5)
Q.q("1.A.1 Detail", "What does the daughter want to study?",
    "design", [("finance", "She no longer wants finance (不想选金融了)."),
               ("mathematics", "Her math is good, but she does not want to major in it."),
               ("computer science", "Tech companies are mentioned as employers, not as her major.")],
    "我想学设计.", "She states her new choice directly.",
    ["我不想……，我想…… → the new choice."])
Q.q("1.B.3 Point of view", "What is the father's main concern at first?",
    "whether a design degree leads to good jobs", [("whether design is too difficult", "He worries about jobs and income, not difficulty."),
                                                   ("the cost of art supplies", "Costs are not mentioned."),
                                                   ("that she is bad at math", "He says her math is good.")],
    "设计以后能做什么呢？ / 能不能找到工作是另一回事.", "Both of his lines focus on employment and income.",
    ["Read both of the father's objections."])
Q.q("1.B.5 Word meaning", r"喜欢是一回事，能不能找到工作是另一回事 means",
    "liking something and finding work in it are separate questions", [("liking something is the same as finding work", "一回事……另一回事 separates the two."),
                                                                      ("she will find work because she likes it", "He doubts that link."),
                                                                      ("she should stop liking design", "He separates the questions; he does not forbid the interest.")],
    "A 是一回事，B 是另一回事 = A and B are different matters.", "The pattern stresses that one thing does not guarantee the other.",
    ["一回事 vs. 另一回事."])
Q.q("1.A.1 Detail", "What does the daughter plan to do this summer?",
    "intern at a design company for two months", [("take a finance course", "She will consider finance only if design does not suit her."),
                                                  ("travel with her father", "No travel is mentioned."),
                                                  ("work at a tech company", "The internship is at 王阿姨's design company.")],
    "先去王阿姨的设计公司实习两个月.", "先 + plan: an internship to test her fit.",
    ["打算 → plan."])
Q.q("1.C.2 Conclusion", "How does the conversation end?",
    "The father accepts her plan and agrees to talk again after the internship.", [("The father refuses to let her study design.", "He calls the plan 不错 and agrees."),
                                                                                 ("The daughter decides to study finance.", "She will test design first."),
                                                                                 ("They decide to ask 王阿姨 to choose.", "王阿姨 only offers the internship.")],
    "这个办法倒是不错。那好吧……再好好谈谈.", "倒是 marks a concession: the father did not expect to like the plan, but does.",
    ["Final line → outcome."])

Q.sec("Reading: Promotional Material")
Q.src(r"Reading 1 \textperiodcentered\ Promotional Material \textperiodcentered\ An event poster", [
    "\\textbf{2027 春江城市半程马拉松 —— 跑过春江，跑出健康！}",
    "比赛日期：2027年3月28日（星期日）早上7:30起跑",
    "项目：半程马拉松（21.0975公里）；健康跑（5公里，适合家庭和初学者）",
    "报名费：半程马拉松 120元；健康跑 50元（12岁以下儿童免费，须由家长陪同）",
    "报名时间：1月10日至2月10日，名额有限，报满为止。半程马拉松选手须年满18岁，并提交近半年内的体检证明。",
    "所有完成比赛的选手都能得到纪念奖牌。比赛当天，沿途设有十个饮水站和三个医疗站。",
    "比赛当天，地铁2号线将提前一小时开始运营。",
], 5)
Q.q("1.B.1 Purpose", "What is the poster's main purpose?",
    "to attract runners to sign up for a city race", [("to announce a new subway line", "The subway line already exists; it opens early that day."),
                                                      ("to recruit medical volunteers", "Medical stations exist; no recruiting."),
                                                      ("to sell running shoes", "Nothing is sold.")],
    "Title + 报名 details.", "The poster gives dates, events, fees and sign-up rules: an invitation to register.",
    ["What action does it want? 报名."])
Q.q("1.A.1 Price", "A father registers for the health run with his 10-year-old daughter. How much do they pay in total?",
    "50 yuan", [("100 yuan", "The child under 12 runs free."),
                ("120 yuan", "120 is the half-marathon fee."),
                ("170 yuan", "That mixes the two events' fees.")],
    "健康跑 50 + child under 12 free = 50.", "Only the father pays; children under twelve run free with a parent.",
    ["Adult 50 + child 0."])
Q.q("1.A.1 Detail", "What must half-marathon runners submit?",
    "a recent health-check certificate", [("a letter from their school", "Not required."),
                                         ("a photo of previous races", "Not required."),
                                         ("proof that they live in the city", "Not required.")],
    "提交近半年内的体检证明.", "体检证明 = health-check certificate, dated within six months.",
    ["须 → requirement."])
Q.q("1.C.3 Inference", r"What does 报满为止 suggest?",
    "Registration may close before February 10 if all places fill.", [("Registration never closes.", "为止 marks an end point."),
                                                                     ("Runners must finish by noon.", "Not about finishing times."),
                                                                     ("Every applicant will get a place.", "名额有限 says otherwise.")],
    "报满为止 = until full.", "Registration ends when the places are filled, which may be before the stated end date.",
    ["为止 = until."])
Q.q("1.C.1 Connect", "Why will Subway Line 2 start running an hour early on race day?",
    "so runners can reach the 7:30 start", [("because the race uses the subway tunnels", "The race is through the city, not the tunnels."),
                                            ("to carry injured runners", "Medical stations handle injuries."),
                                            ("because the race is at night", "The start is 7:30 in the morning.")],
    "早上7:30起跑 + 提前一小时.", "Connecting the early start time with the early subway explains the change.",
    ["Connect two details."])

Q.sec("Reading: Correspondence")
Q.src(r"Reading 2 \textperiodcentered\ Correspondence \textperiodcentered\ A letter", [
    "亲爱的小文：",
    "你好！收到你的信，知道你在美国一切都好，我和你爷爷都很放心。",
    "你在信里说，最想念的是奶奶做的红烧肉，还说你在学校的中国超市买了材料，自己做了一次，可是味道“怎么都不对”。哈哈，奶奶告诉你一个秘密吧：红烧肉最重要的不是放什么，而是火候。要用小火慢慢地炖，最少一个小时，着急是做不好的。",
    "我把做法写在了下面，你再试试。做好了，请你的室友们一起吃。一个人吃饭，再好吃的菜也不香；大家一起吃，才有家的味道。",
    "天冷了，记得多穿衣服，别总喝冰水。",
    "奶奶",
    "（附：红烧肉做法）",
], 5)
Q.q("1.A.1 Detail", "What problem did Xiaowen describe in her letter?",
    "Her braised pork did not taste right.", [("She could not find a Chinese supermarket.", "She bought ingredients at one."),
                                             ("Her roommates did not like Chinese food.", "Roommates are only mentioned in Grandma's advice."),
                                             ("She forgot Grandma's birthday.", "Not mentioned.")],
    "味道“怎么都不对”.", "Xiaowen made the dish herself, but it never tasted right.",
    ["你在信里说 → Xiaowen's problem."])
Q.q("1.A.1 Detail", "According to Grandma, what is the secret of the dish?",
    "slow cooking over low heat", [("a special sauce", "She says it is not about what you put in."),
                                   ("expensive pork", "Ingredients are not the point."),
                                   ("cooking it quickly over high heat", "The opposite: 小火慢慢地炖.")],
    "最重要的不是放什么，而是火候.", "火候 is control of heat and time; she specifies low heat for at least an hour.",
    ["不是……而是…… → the real point."])
Q.q("1.B.3 Perspective", "Which perspective does Grandma express about food?",
    "Food is best when shared with others.", [("Expensive food is the most delicious.", "Price is never mentioned."),
                                             ("Eating alone is more relaxing.", "She says food alone is not tasty."),
                                             ("Cooking is women's work.", "Not suggested.")],
    "大家一起吃，才有家的味道.", "只有/才 logic: only shared meals taste like home.",
    ["一个人…… vs. 大家一起…… → value of sharing."])
Q.q("1.B.5 Word meaning", r"In the letter, 家的味道 most nearly means",
    "the feeling of home", [("the smell of the house", "Literal; here it is figurative."),
                            ("a family recipe book", "Not an object."),
                            ("the taste of salt", "Not literal flavor.")],
    "味道 used figuratively.", "家的味道 = the warmth and feeling of home, created by eating together.",
    ["Literal → figurative."])
Q.q("1.B.2 Relationship", "What is the relationship between the writer and the reader?",
    "grandmother and granddaughter", [("teacher and student", "She signs as 奶奶."),
                                      ("mother and daughter", "She mentions 你爷爷: Xiaowen's grandfather."),
                                      ("two classmates", "The tone and signature show an elder.")],
    "Signature 奶奶 + 你爷爷.", "The signature and references identify a grandmother writing to her granddaughter.",
    ["Look at the signature."])

Q.sec("Listening: Presentation")
Q.src(r"Listening 2 \textperiodcentered\ Presentation (transcript) \textperiodcentered\ A college student's talk", [
    "大家好！今天我想跟大家分享我的“间隔年”。",
    "高中毕业以后，我没有马上上大学，而是用了一年时间做三件事。第一，我在云南的一所小学当了半年志愿者老师，教孩子们英语和画画。第二，我在一家咖啡店打工，存了钱。第三，我用存下的钱一个人去了西藏和新疆旅行。",
    "很多人问我：“浪费一年，值得吗？”我的回答是：值得。当志愿者让我知道，自己其实很喜欢教书；打工让我明白，钱是怎么一分一分挣来的；而一个人旅行，让我学会了自己做决定。",
    "当然，间隔年不适合每个人。我的父母一开始非常反对，他们担心我会“玩野了”，不想再读书。我花了很长时间跟他们解释我的计划，最后他们才同意。",
    "现在，我在大学学教育，每天都很清楚自己为什么学习。谢谢大家！",
], 5)
Q.q("1.B.4 Organization", "How does the speaker organize the middle of the talk?",
    "by listing three activities and then what each taught her", [("by comparing two countries", "No country comparison is made."),
                                                                 ("by telling events in reverse order", "The order is chronological."),
                                                                 ("by answering questions from the audience", "She answers one common question she gets.")],
    "第一/第二/第三 + 让我…….", "She lists three activities, then pairs each with a lesson.",
    ["Look for 第一, 第二, 第三 and the 让我 sentences."])
Q.q("1.A.1 Detail", "What did volunteering teach the speaker?",
    "that she enjoys teaching", [("how hard it is to earn money", "That lesson came from her café job."),
                                 ("how to make decisions on her own", "That came from traveling alone."),
                                 ("how to speak Tibetan", "Not mentioned.")],
    "当志愿者让我知道，自己其实很喜欢教书.", "Each activity is paired with a lesson; volunteering → enjoying teaching.",
    ["Match activity to lesson."])
Q.q("1.B.3 Attitude", "How did her parents first react to the gap-year plan?",
    "They strongly opposed it.", [("They paid for the whole year.", "She saved her own money."),
                                  ("They were indifferent.", "非常反对 shows strong feeling."),
                                  ("They suggested it themselves.", "She had to persuade them.")],
    "我的父母一开始非常反对.", "一开始 marks the first reaction; they agreed only later (最后才同意).",
    ["一开始 vs. 最后."])
Q.q("1.B.5 Word meaning", r"The parents worried she would 玩野了. This means they feared she would",
    "get so used to freedom that she would not want to return to study", [("get lost in the wilderness", "野 is figurative here."),
                                                                         ("become a professional athlete", "Not related."),
                                                                         ("make wild friends online", "Not related.")],
    "玩野了 = grow too used to play; 不想再读书 explains it.", "The phrase is explained right after: 不想再读书.",
    ["The clause after the term defines it."])
Q.q("1.C.2 Conclusion", "What is the speaker's overall conclusion?",
    "The gap year was worthwhile because it gave her clear direction, though it is not for everyone.",
    [("Everyone should take a gap year.", "She says 间隔年不适合每个人."),
     ("A gap year is a waste of time.", "She answers 值得."),
     ("Students should work instead of going to college.", "She is now in college studying education.")],
    "值得 + 不适合每个人 + 很清楚自己为什么学习.", "A balanced conclusion: worthwhile for her, with a caveat.",
    ["Combine her answer, the caveat and the ending."])

Q.frq(kind="Story Narration", head=r"Question 3 \textperiodcentered\ Story Narration \textperiodcentered\ 8 points \textperiodcentered\ about 15 minutes",
      mins=15,
      directions=[r"\textbf{Directions.} The four pictures present a story. Imagine you are writing the story for a student magazine. Narrate a complete story as suggested by the pictures, in their order, with logical organization and relevant details."],
      panels=["一个男孩坐在书桌前，桌上堆满了课本和练习册，墙上的钟显示晚上十二点。他打着哈欠。",
              "第二天在跑道上，男孩跑步时脸色很差，停下来扶着膝盖喘气。教练在旁边看着他，有点担心。",
              "男孩和教练坐在跑道边的椅子上。教练拿着一张写着“作息时间表”的纸，在给他解释。",
              "几个星期以后，男孩在比赛中冲过终点线，脸上带着笑容。看台上，他的父母在为他鼓掌。"],
      model=["期末考试快到了，大明每天晚上都学习到半夜。这天晚上，钟已经指向十二点了，他还在做练习题，书桌上堆满了课本。他一边打哈欠，一边想：再做一页就睡。",
             "第二天下午是田径队的训练。平时跑得最快的大明，今天才跑了两圈就跑不动了。他停下来，扶着膝盖大口大口地喘气，脸色白得吓人。教练看见了，赶紧走过来问他怎么了。",
             "知道大明每天只睡五个小时以后，教练没有批评他，而是拉着他坐下来，拿出一张纸，帮他做了一个作息时间表：晚上十点半以前必须睡觉，每天的复习时间分成几段，中间休息十分钟。教练说：“学习和跑步一样，不能只靠拼命，要劳逸结合。”",
             "大明按照时间表坚持了几个星期。没想到，他不但考试成绩没有下降，跑步也越来越快了。在学校运动会的决赛中，他第一个冲过了终点。看台上，爸爸妈妈为他用力地鼓掌。大明终于明白了：休息不是浪费时间，而是为了走得更远。"],
      rows=[("Narrative development", 3, "All four pictures in order with details (the clock, the exhaustion, the schedule, the race) and the coach's line of dialogue.", "Skipping the schedule in picture 3 or not explaining why he improved."),
            ("Organization", 2, "Clear cause-and-effect chain; links: 这天晚上，第二天下午，知道……以后，没想到，终于.", "Four separate picture descriptions with no links."),
            ("Language control", 3, "Varied structures (一边……一边, 才……就, 不是……而是, 不但……而且, 越来越, 按照) and a culturally relevant expression (劳逸结合) used in dialogue.", "Overuse of 然后; 了 errors.")],
      tips=[r"The story turns on a perspective from this unit (劳逸结合), placed in the coach's mouth rather than stated by the narrator. The final sentence uses 不是……而是 to give a clear lesson, which completes the beginning-middle-end shape."])

GUIDE, QSET = G, Q
