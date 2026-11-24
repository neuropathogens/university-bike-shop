from model import Doc

STEM = "06-global-contexts"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 6: Global Contexts", r"Unit 6 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 6 asks how global phenomena affect Chinese-speaking communities, what role individuals play in responding to them, and how complex issues affect a society's culture. Its recommended contexts are global communication, the natural world, history, policy and planning, and transportation. This guide covers the vocabulary of the environment, history and transport; the formal written connectors that Unit 6 articles rely on; perspectives such as harmony with nature and the link between the individual and the community; and a Project Q\&A kit, since this is the unit where cultural comparison comes most naturally. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Formal connectors I don't use yet: \blank[10em]",
        short="Unit 6", sub="Global Contexts")

G.sec("Environment and the natural world")
G.tex(r"""
\begin{vocab}
环境保护（环保） & huánjìng bǎohù & environmental protection \\
污染 / 空气污染 / 塑料污染 & wūrǎn & pollution / air pollution / plastic pollution \\
垃圾分类 & lājī fēnlèi & sorting garbage \\
可回收物 / 厨余垃圾 / 有害垃圾 / 其他垃圾 & kě huíshōu wù / chúyú lājī / yǒuhài lājī / qítā lājī & recyclables / food waste / hazardous waste / residual waste \\
节约 / 浪费 & jiéyuē / làngfèi & to save, economize / to waste \\
低碳 / 节能 / 减排 & dītàn / jiénéng / jiǎnpái & low-carbon / energy-saving / emission reduction \\
气候变化 / 全球变暖 & qìhòu biànhuà / quánqiú biànnuǎn & climate change / global warming \\
可再生能源 / 太阳能 / 风能 & kě zàishēng néngyuán / tàiyángnéng / fēngnéng & renewable energy / solar / wind \\
植树 / 森林 / 沙漠 & zhíshù / sēnlín / shāmò & to plant trees / forest / desert \\
野生动物 / 大熊猫 / 保护区 & yěshēng dòngwù / dàxióngmāo / bǎohùqū & wildlife / giant panda / nature reserve \\
长江 / 黄河 & Cháng Jiāng / Huáng Hé & the Yangtze / the Yellow River \\
光盘行动 & guāngpán xíngdòng & ``clean plate campaign'' against food waste \\
\end{vocab}

\textbf{Practices.} Garbage sorting into four bins became mandatory in Shanghai in 2019 and has spread to other cities. The clean-plate campaign discourages ordering more than a table can eat, which pulls against the hospitality practice of ordering generously (Unit 5): a good example of a perspective changing. Tree-planting along deserts and the protection of pandas are common reading topics.

\textbf{Perspective.} 绿水青山就是金山银山 (clear waters and green mountains are as valuable as mountains of gold and silver) is a widely quoted slogan that frames environmental protection as a form of wealth. Older ideas such as 天人合一 (Unit 3) present people as part of nature.
""")
G.q("1 Environment", r"In which bin does a banana peel go?",
    "厨余垃圾", [("可回收物", "Recyclables are paper, plastic, glass and metal."),
                 ("有害垃圾", "Hazardous waste is batteries, medicine and paint."),
                 ("其他垃圾", "Residual waste is for what fits no other category; food scraps have their own bin.")],
    "Food scraps → 厨余垃圾.", "厨余 means kitchen leftovers: the food-waste bin.",
    ["厨 (kitchen) + 余 (leftover)."])
G.q("1 Environment", r"光盘行动 encourages people to",
    "finish their food and not over-order", [("recycle old CDs", "光盘 here means a clean (empty) plate, a pun on “disc.”"),
                                             ("turn off lights", "That would be about energy, not food."),
                                             ("buy fewer plates", "The campaign targets food waste.")],
    "光盘 = an empty plate.", "光 as “used up” + 盘 “plate”: eat everything you order.",
    ["光 = nothing left."])
G.q("1 Perspectives", r"绿水青山就是金山银山 presents environmental protection as",
    "a form of lasting wealth", [("a cost that slows the economy", "The slogan equates nature with wealth."),
                                 ("a hobby for tourists", "Not about tourism."),
                                 ("a reason to mine mountains", "It argues the opposite.")],
    "Nature = gold and silver.", "The slogan claims clean water and green mountains are themselves valuable.",
    ["就是 equates the two halves."])

G.sec("History, transportation and global communication")
G.tex(r"""
\begin{vocab}
历史 / 朝代 / 古代 / 现代 & lìshǐ / cháodài / gǔdài / xiàndài & history / dynasty / ancient / modern \\
丝绸之路 & Sīchóu zhī Lù & the Silk Road \\
郑和下西洋 & Zhèng Hé xià Xīyáng & Zheng He's voyages to the ``Western Seas'' (early 1400s) \\
长城 / 大运河 & Chángchéng / Dà Yùnhé & the Great Wall / the Grand Canal \\
交通 / 交通工具 & jiāotōng / jiāotōng gōngjù & transport / means of transport \\
高铁 / 地铁 / 航班 & gāotiě / dìtiě / hángbān & high-speed rail / subway / flight \\
堵车 / 高峰 / 春运 & dǔchē / gāofēng / chūnyùn & traffic jam / rush hour / Spring Festival travel season \\
国际 / 全球化 & guójì / quánqiúhuà & international / globalization \\
交流 / 合作 / 贸易 & jiāoliú / hézuò / màoyì & exchange / cooperation / trade \\
移民 / 华人社区 & yímín / huárén shèqū & immigration, immigrant / Chinese community \\
政策 / 规划 / 措施 & zhèngcè / guīhuà / cuòshī & policy / planning / measure \\
\end{vocab}

\textbf{The Silk Road as exchange.} Readings use the Silk Road to talk about exchange in both directions: silk, tea and porcelain traveling west; grapes, glassware, music and religions traveling east. \textbf{Transportation and society.} The Grand Canal once linked north and south; today high-speed rail and the Spring Festival travel rush show how transport shapes family life. \textbf{Chinese communities abroad.} Chinatowns, Lunar New Year parades and weekend Chinese schools are common topics in global communication.
""")
G.q("2 History", r"丝绸之路 is usually discussed in readings as an example of",
    "exchange of goods and ideas between East and West", [("a modern highway project", "It was an ancient network of trade routes."),
                                                          ("a wall built for defense", "That is the Great Wall."),
                                                          ("a canal linking north and south China", "That is the Grand Canal.")],
    "Silk Road = exchange in both directions.", "Silk and porcelain went west; grapes, glass and music came east.",
    ["Trade routes → exchange."])
G.q("2 Transport", r"上下班高峰的时候，地铁里人很多。 When are subways crowded?",
    "during rush hour", [("late at night", "高峰 is the peak period."),
                          ("on public holidays only", "上下班 refers to commuting days."),
                          ("during the Spring Festival only", "That is 春运.")],
    "上下班高峰 = commuting peak.", "高峰 (peak) + 上下班 (going to and from work).",
    ["高峰 = peak."])

G.sec("Formal connectors for articles and presentations")
G.tex(r"""
Unit 6 articles are the most formal on the exam. Recognizing these connectors is a reading skill; using a few of them is a language control skill.

\begin{compare}{Connector}{Meaning}{Example}
由于……，因此…… & because \ldots, therefore & 由于气候变暖，因此冰川在减少。 \\
然而 & however & 措施很多，然而效果并不明显。 \\
此外 / 另外 & in addition & 此外，政府还鼓励使用公共交通。 \\
尽管……，仍然…… & even though & 尽管困难很大，志愿者仍然坚持了十年。 \\
从而 & thereby & 植树可以防止沙漠扩大，从而保护农田。 \\
以便 & so that & 社区设立了回收站，以便居民分类。 \\
据报道 / 据统计 & according to reports / statistics & 据统计，去年游客增加了三成。 \\
由此可见 & it can thus be seen & 由此可见，个人的行动也很重要。 \\
与此同时 & at the same time & 与此同时，网购包装的垃圾也越来越多。 \\
\end{compare}

\begin{trap}
然而 and 而 can both mark contrast, but 而 also simply joins (而且 is ``moreover''; 而是 is ``but rather''). Read the whole sentence before deciding a 而 is a contrast. And 从而 introduces a \emph{result}, not a cause.
\end{trap}
""")
G.q("3 Connectors", r"植树可以防止沙漠扩大，从而保护农田。 What does 从而 introduce?",
    "the result of stopping the desert from spreading", [("the cause of desertification", "从而 introduces a result."),
                                                         ("a contrast", "Contrast would be 然而."),
                                                         ("an example", "Examples use 例如.")],
    "从而 = thereby.", "The chain: plant trees → stop the desert → (从而) protect farmland.",
    ["A → B，从而 C."])
G.q("3 Connectors", r"Fill the blank: 很多人知道垃圾分类的好处，\blank 真正做到的人并不多。",
    "然而", [("因此", "因此 gives a result; knowing the benefits does not cause few people to sort."),
             ("此外", "此外 adds a similar point; here the second clause contrasts."),
             ("以便", "以便 introduces a purpose.")],
    "Knowing vs. doing → contrast: 然而.", "然而 marks a contrast between what people know and what they do.",
    ["The clauses pull in opposite directions."])

G.sec("Perspectives on global issues")
G.tex(r"""
\begin{compare}{Perspective}{How it appears}{Language}
The individual and the community & Volunteers, neighborhood campaigns, ``从我做起'' (starting with myself) & 人人有责（everyone is responsible）, 从小事做起 \\
Long-term thinking & Planting trees for the next generation & 前人栽树，后人乘凉（earlier generations plant trees so later ones enjoy the shade） \\
Harmony with nature & Protected reserves, slogans on green development & 天人合一, 绿水青山 \\
Openness and exchange & Silk Road history, students abroad, Chinatowns & 交流, 互相学习, 和而不同 \\
\end{compare}

\begin{keyidea}[Comparing cultures without stereotypes]
The CED warns against generalizations and stereotypes. Compare \emph{specific practices} and qualify them: \emph{在上海，垃圾分类是法律规定的；在我住的城市，回收主要靠居民自愿。} Words like 有些, 不少, 在我住的地方 and 根据……的资料 keep a comparison accurate.
\end{keyidea}
""")
G.q("4 Perspectives", r"前人栽树，后人乘凉 expresses",
    "acting now for the benefit of future generations", [("planting trees only for shade", "The saying is figurative."),
                                                       ("young people should rest more", "Not about rest."),
                                                       ("the past was better than the present", "It looks forward.")],
    "Earlier people plant; later people enjoy the shade.", "The saying praises long-term effort whose benefits go to others later.",
    ["Who plants, who benefits?"])
G.q("4 Comparison", "Which comparison avoids a stereotype?",
    "在上海，垃圾分类是法律规定的；在我住的城市，回收主要靠居民自愿。",
    [("中国人都很注意环保，美国人都不注意。", "都 overgeneralizes about whole nations."),
     ("美国人只关心自己。", "A sweeping stereotype."),
     ("中国人都喜欢熊猫。", "An overgeneralization with no specific practice.")],
    "Specific places, specific practices.", "Naming a specific place and practice keeps a comparison accurate and earns cultural understanding.",
    ["Look for 都 + a nation: a red flag."])

G.sec("Task kit: the Project Q\\&A")
G.tex(r"""
Four recorded questions follow your presentation; each is heard twice and you have 40 seconds. Expect questions like these: \emph{Which factor do you think matters most, and why? How is this similar to or different from your community? What surprised you in your research? What might change in the future?}

\begin{compare}{Question type}{40-second shape}{Frames}
Most important factor & claim + reason + example & 我认为最重要的是……，因为……。比如…… \\
Comparison & their practice + yours + the perspective behind the difference & 跟……相比，……；这可能是因为…… \\
Surprise & what you expected + what you found & 我本来以为……，没想到…… \\
Future & prediction + reason & 我觉得将来……，因为随着…… \\
Opinion / advice & position + one reason + one condition & 我同意……，不过前提是…… \\
\end{compare}

\begin{keyidea}[Keep talking for 40 seconds]
Answer in the first sentence, give one reason, give one specific example, then add a comparison or a reflection. If a word is missing, paraphrase (就是那种……的). If the question is unclear the first time, it is played again: use the second hearing to plan.
\end{keyidea}
""")
G.q("5 Q&A", r"A Q\&A prompt asks which factor matters most. Which opening is best?",
    "我认为最重要的是第三个方面，因为它解释了人们为什么这样做。", [("这个问题很难。", "It delays the answer and wastes seconds."),
                                                             ("嗯……我不知道……", "Hesitation with no content lowers task execution and fluency."),
                                                             ("我的presentation有三个方面。", "Restates the presentation instead of choosing.")],
    "Answer first, then reason.", "Task execution rewards responses that address the prompt directly.",
    ["Claim in sentence one."])
G.q("5 Q&A", r"Which frame is best for a ``what surprised you'' question?",
    "我本来以为……，没想到……", [("首先……其次……最后……", "A listing frame, not a surprise frame."),
                                ("与其……不如……", "Recommends one option over another."),
                                ("只要……就……", "States a sufficient condition.")],
    "本来以为 + 没想到 = expectation vs. finding.", "This frame contrasts expectation with result, which is exactly what a surprise question asks.",
    ["Expectation → surprise."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 6: Global Contexts: Question Set", r"Unit 6 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (a Presentation and Audio and Chart for listening, an Article and a Literary Text for reading) on garbage sorting, desert tree-planting, a family that emigrated, and how students commute, followed by a practice Project Q\&A (9 points) with model answers. The Q\&A follows the practice presentation in the Unit 3 question set. Listening sources and Q\&A prompts are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 5 minutes for the Q\&A.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Q\&A: \blank\ / 9 \qquad Target: 16+ MCQ and 7+ Q\&A",
        short="Unit 6", sub="Global Contexts")

Q.sec("Listening: Presentation")
Q.src(r"Listening 1 \textperiodcentered\ Presentation (transcript) \textperiodcentered\ A student reports on a class project", [
    "大家好！我们小组研究的题目是：“垃圾分类，为什么这么难？”",
    "我们先在学校附近的三个小区观察了一个星期。我们发现，虽然每个小区都有四种颜色的垃圾桶，但是放错的垃圾很多，最常见的是把外卖盒直接扔进“可回收物”，可是盒子里还有剩饭。",
    "然后，我们采访了二十位居民。大部分人说，不是不想分，而是分不清。比如，用过的纸巾，很多人以为是可回收的，其实应该放进“其他垃圾”。还有人说，早上上班太急，没时间分。",
    "根据这些发现，我们做了两件事：第一，设计了一张图片很多、文字很少的分类提示卡，贴在每个垃圾桶上面；第二，跟居委会合作，每天早上七点到八点安排志愿者在垃圾桶旁边帮忙。",
    "一个月以后，我们再去观察，放错的情况减少了差不多一半。由此可见，只要方法对，每个人都能做到。谢谢！",
], 5)
Q.q("1.B.1 Main idea", "What is the presentation mainly about?",
    "why garbage sorting is difficult and how the group helped improve it", [("how recycling factories work", "No factory is discussed."),
                                                                           ("the history of garbage sorting laws", "No laws are discussed."),
                                                                           ("why residents refuse to sort garbage", "Residents say they want to but can't tell the categories apart.")],
    "题目 + 我们做了两件事 + results.", "The talk moves from the problem to causes to the group's solution and results.",
    ["Title + structure."])
Q.q("1.A.1 Detail", "What was the most common mistake the students observed?",
    "putting takeout boxes with leftover food into the recyclables bin", [("putting batteries in the food-waste bin", "Batteries are not mentioned."),
                                                                          ("leaving garbage outside the bins", "Not mentioned."),
                                                                          ("using only one bin for everything", "They used the bins, but wrongly.")],
    "最常见的是把外卖盒直接扔进“可回收物”.", "最常见的 points to the most frequent error.",
    ["最常见的 → answer."])
Q.q("1.A.1 Detail", "According to most residents interviewed, why don't they sort correctly?",
    "They cannot tell which category things belong to.", [("They think sorting is useless.", "They say it is not that they don't want to."),
                                                          ("The bins are too far away.", "Distance is not mentioned."),
                                                          ("They are fined too often.", "No fines are mentioned.")],
    "不是不想分，而是分不清.", "不是……而是 gives the real reason: 分不清 (can't tell apart).",
    ["不是 A 而是 B → B."])
Q.q("1.C.1 Connect", "How do the group's two actions respond to their findings?",
    "The cards address confusion; the morning volunteers address the rush before work.", [("Both actions punish residents who sort wrongly.", "Neither action punishes anyone."),
                                                                                       ("Both actions reduce the number of bins.", "The bins stay the same."),
                                                                                       ("The cards are for the volunteers, not residents.", "The cards are posted on the bins for residents.")],
    "分不清 → picture cards; 早上太急 → 7–8 a.m. volunteers.", "Each action matches one of the reasons residents gave.",
    ["Match each solution to a reason."])
Q.q("1.A.2 Data", "What happened after one month?",
    "Mistakes fell by about half.", [("Mistakes fell to zero.", "差不多一半 is about half."),
                                     ("Mistakes doubled.", "They decreased."),
                                     ("Nothing changed.", "The situation improved.")],
    "放错的情况减少了差不多一半.", "减少了 (decreased by) + 差不多一半 (about half).",
    ["减少了 + amount."])

Q.sec("Reading: Article")
Q.src(r"Reading 1 \textperiodcentered\ Article \textperiodcentered\ From a news magazine", [
    "\\textbf{沙漠边上的“绿色长城”}",
    "三十年前，老马所在的村子每年春天都会遇到沙尘暴。“风一来，天都是黄的，刚种下的庄稼一夜之间就被沙子埋了。”",
    "1995年，老马和村里的五户人家开始在村子北边种树。由于这里缺水，第一年种的树只活了不到三成。然而，他们没有放弃，而是一边向专家请教，一边试种耐旱的植物，比如沙柳和梭梭。",
    "如今，当年的五户人家变成了两百多户，他们种下的树林已经绵延了二十多公里，被当地人称为“绿色长城”。村子里的沙尘暴天数明显减少，一些年轻人也从城里回到了村子，在林子里养羊、种中药材。",
    "老马说：“我们这代人种树，是为了下一代能在这里好好生活。前人栽树，后人乘凉嘛。”",
], 5)
Q.q("1.A.1 Detail", "What problem did the village face thirty years ago?",
    "sandstorms that buried crops", [("floods from a nearby river", "The problem was sand, not water."),
                                     ("too many young people", "Young people later returned; before, the problem was sand."),
                                     ("a shortage of sheep", "Sheep are raised now, as a result of the forest.")],
    "沙尘暴 + 庄稼……被沙子埋了.", "The opening quote describes sandstorms that buried newly planted crops.",
    ["First paragraph → the problem."])
Q.q("1.A.2 Data", "What share of the trees planted in the first year survived?",
    "less than 30\\%", [("about 3\\%", "三成 is 30%, and 不到三成 is under that."),
                         ("about one third", "One third is 三分之一."),
                         ("more than 70\\%", "The first year went badly.")],
    "不到三成 = under 30%.", "成 is a tenth; 不到 means less than.",
    ["三成 = 30%."])
Q.q("1.B.4 Organization", "How is the article organized?",
    "problem, efforts and setbacks, results, then a personal reflection", [("a list of tree species with descriptions", "Species are mentioned only as examples."),
                                                                            ("an argument against planting trees", "The article supports the effort."),
                                                                            ("a comparison of two villages", "Only one village is described.")],
    "Then → effort → now → quote.", "The paragraphs move from 三十年前 to 1995 to 如今 and end with 老马's words.",
    ["Follow the time words."])
Q.q("1.C.2 Conclusion", "Which effect of the forest is mentioned?",
    "Some young people have returned to the village to work.", [("The village became a large city.", "No such change is described."),
                                                             ("Sandstorms stopped completely.", "They decreased (明显减少), not stopped."),
                                                             ("The government built a real wall.", "绿色长城 is a nickname.")],
    "一些年轻人也从城里回到了村子.", "The results paragraph lists fewer sandstorms and young people returning to raise sheep and herbs.",
    ["如今 → results."])
Q.q("1.B.3 Perspective", "Which perspective does 老马's quotation express?",
    "Today's effort is for the good of future generations.", [("Each generation should solve only its own problems.", "He works for the next generation."),
                                                              ("Trees are valuable mainly for their wood.", "Not about timber."),
                                                              ("Young people should stay in the cities.", "He welcomes their return.")],
    "为了下一代 + 前人栽树，后人乘凉.", "The saying and his explanation both point to long-term thinking.",
    ["The saying names the perspective."])

Q.sec("Reading: Literary Text")
Q.src(r"Reading 2 \textperiodcentered\ Literary Text \textperiodcentered\ From a personal essay", [
    "我的行李箱里，一直放着一包从老家带来的茶叶。",
    "十二岁那年，我们全家从福建搬到了温哥华。临走的时候，外公从柜子里拿出一包铁观音，塞进我的箱子：“想家的时候，泡一杯。”",
    "刚到加拿大的那一年，我很少打开它。我忙着学英语，忙着交新朋友，忙着变成一个“加拿大人”。有一次，同学来我家，闻到茶的味道，皱着眉头问：“这是什么奇怪的味道？”从那以后，我就把茶叶藏到了箱子最下面。",
    "直到上了大学，我在一门亚洲历史课上读到了茶叶怎样通过海上丝绸之路走向世界，读到了福建的茶农们几百年来怎样把一片叶子变成一种文化。那天晚上，我第一次自己泡了一杯铁观音。茶很苦，又很香，像外公的话。",
    "现在，我的同学们会来我的宿舍“喝茶聊天”。我教他们怎么闻香、怎么品茶。他们说，这是“Jenny的茶馆”。我想，外公要是知道，一定会笑的。",
], 5)
Q.q("1.A.1 Detail", "Why did the narrator hide the tea?",
    "A classmate reacted to its smell as strange.", [("Her parents told her not to drink tea.", "Not mentioned."),
                                                     ("The tea had gone bad.", "Nothing suggests that."),
                                                     ("She had forgotten about it.", "She hid it on purpose.")],
    "这是什么奇怪的味道？→ 从那以后……藏到了箱子最下面.", "从那以后 links the classmate's comment to the hiding.",
    ["从那以后 → consequence."])
Q.q("1.B.3 Feeling", "In her first year in Canada, the narrator mainly wanted to",
    "fit in as a Canadian", [("return to Fujian", "She was busy adapting, not planning to return."),
                             ("become a tea expert", "That comes much later."),
                             ("study Asian history", "That comes at university.")],
    "忙着变成一个“加拿大人”.", "The repeated 忙着 shows her effort to adapt and fit in.",
    ["忙着 ×3."])
Q.q("1.B.4 Turning point", "What changed the narrator's attitude toward the tea?",
    "learning in a university class how tea shaped history and culture", [("a visit from her grandfather", "Grandfather does not visit."),
                                                                          ("a classmate's praise", "The classmate's comment was negative."),
                                                                          ("a doctor's advice", "Not mentioned.")],
    "直到上了大学……那天晚上，我第一次自己泡了一杯.", "直到 marks the turning point; the history class leads her to brew the tea.",
    ["直到 → turning point."])
Q.q("1.B.5 Figurative meaning", r"茶很苦，又很香，像外公的话 suggests that her grandfather's words",
    "were bittersweet: about leaving home, yet full of love", [("tasted bad", "The comparison is figurative."),
                                                               ("were spoken in a loud voice", "Nothing about volume."),
                                                               ("were hard to understand", "She understood them.")],
    "苦 (bitter) + 香 (fragrant) = bittersweet.", "The words were about missing home (bitter) but were a gift of love (sweet, fragrant).",
    ["Simile: tea ↔ words."])
Q.q("1.C.3 Inference", "Why does the narrator think her grandfather would smile?",
    "Because the tea he gave her now connects her with friends and with her heritage.", [("Because she sold the tea for money.", "Nothing is sold."),
                                                                                        ("Because she moved back to Fujian.", "She is at university, apparently in Canada."),
                                                                                        ("Because she stopped drinking tea.", "She drinks and shares it.")],
    "Jenny的茶馆 + 外公……一定会笑.", "Sharing tea with friends fulfills the meaning of his gift.",
    ["Connect the gift at the start with the ending."])

Q.sec("Listening: Audio and Chart")
Q.src(r"Listening 2 \textperiodcentered\ Audio and Chart (transcript) \textperiodcentered\ A city radio report", [
    "下面是一条城市交通新闻。市交通局今天公布了中学生上学方式的调查结果。",
    "和五年前相比，坐地铁和公交车上学的学生从百分之四十增加到了百分之五十五，骑自行车的学生也从百分之八增加到了百分之十五。与此同时，坐家长的车上学的学生从百分之四十二下降到了百分之二十二。",
    "交通局认为，变化的主要原因是地铁新开了两条线，而且学校附近修了更安全的自行车道。",
    "不过，步行上学的比例一直变化不大。交通局表示，下一步将在学校附近设立“安全步行路线”，鼓励住得近的学生走路上学，这样既能锻炼身体，又能减少早上的堵车。",
], 5, table=(["上学方式", "五年前", "今年"], [["地铁、公交", "40\\%", "55\\%"], ["家长开车送", "42\\%", "22\\%"], ["自行车", "8\\%", "15\\%"], ["步行", "10\\%", "8\\%"]]),
   note="Chart: How middle school students get to school (fictional data)")
Q.q("1.A.2 Data", "Which way of getting to school decreased the most?",
    "being driven by parents", [("subway and bus", "Subway and bus increased (40% → 55%)."),
                                ("cycling", "Cycling increased (8% → 15%)."),
                                ("walking", "Walking fell only slightly (10% → 8%).")],
    "42% → 22%: down 20 points.", "Compare the change in each row; driving fell by 20 points.",
    ["Subtract each row."])
Q.q("1.A.2 Data", r"By how many percentage points did cycling increase?",
    "7", [("15", "15% is the new level."),
          ("8", "8% is the old level."),
          ("23", "23 is 8 + 15, not the change.")],
    "15 − 8 = 7.", "The increase is the difference between the two years.",
    ["从8%增加到15% → +7."])
Q.q("1.C.1 Connect", "What reasons does the transportation bureau give for the changes?",
    "two new subway lines and safer bike lanes near schools", [("higher gas prices", "Not mentioned."),
                                                              ("a ban on parents driving", "No ban is mentioned."),
                                                              ("free bus passes", "Not mentioned.")],
    "地铁新开了两条线，而且……更安全的自行车道.", "The two reasons match the two rising rows: transit and cycling.",
    ["原因是 → reasons."])
Q.q("1.C.3 Inference", "Why does the bureau plan ``safe walking routes''?",
    "Walking has not grown, and more walking would mean exercise and less traffic.", [("Walking has become dangerous because of bikes.", "No danger from bikes is mentioned."),
                                                                                    ("Too many students already walk.", "Walking is the smallest group and is not growing."),
                                                                                    ("Subway lines will close.", "Nothing suggests closures.")],
    "步行……变化不大 → 下一步……鼓励……走路.", "The plan targets the one mode that did not change, citing two benefits.",
    ["不过 → the remaining problem → the plan."])
Q.q("1.B.5 Word meaning", r"与此同时 in the report most nearly means",
    "at the same time", [("as a result", "That would be 因此 or 从而."),
                         ("for example", "That would be 比如."),
                         ("in contrast to the past", "与此同时 introduces a simultaneous change.")],
    "与此同时 = meanwhile.", "It presents the drop in car rides as happening alongside the rise in transit and cycling.",
    ["与 (with) + 此 (this) + 同时 (same time)."])

Q.frq(kind="Project Q&A", head=r"Question 2 \textperiodcentered\ Project Q\&A (practice) \textperiodcentered\ 9 points \textperiodcentered\ 4 questions, 40 seconds each",
      mins=5,
      directions=[r"\textbf{Directions.} You will answer four questions about the practice presentation in the Unit 3 question set (广场舞音乐和中国的社区生活). On the exam each question is heard twice and you have 40 seconds to respond. Respond as fully and appropriately as possible, and include at least one cultural comparison or a reflection on how a perspective relates to a product or practice.",
                  "问题一：在你介绍的三个方面中，你觉得哪一个最重要？为什么？",
                  "问题二：你住的地方，老人一般怎么锻炼身体？跟广场舞有什么不同？",
                  "问题三：在研究中，有没有什么让你觉得意外的发现？",
                  "问题四：你觉得十年以后，广场舞会有什么变化？"],
      ask="Answer each question aloud in 40 seconds (time yourself), then jot down the key words you used for each.",
      lines=6,
      model=[r"\textbf{一：}我觉得最重要的是文化观念这个方面，因为它解释了人们为什么愿意每天去跳舞。音乐和舞步可以换，但是喜欢热闹、重视邻里关系的想法不会变。比如，我采访的那位奶奶说，她去跳舞不只是为了锻炼，更是为了见朋友。",
             r"\textbf{二：}在我住的城市，老人一般去社区中心上健身课，或者自己在公园散步，很少在广场上一起跳舞。跟广场舞相比，这里的活动比较安静，也比较个人化。我觉得这可能是因为美国人更重视个人空间，而广场舞体现的是集体生活的观念。",
             r"\textbf{三：}我本来以为跳广场舞的都是老人，没想到现在也有很多年轻人参加，有的人还把跳舞的视频放到网上，成了网红。这让我觉得，传统的社区活动也能跟新的科技结合起来。",
             r"\textbf{四：}我觉得十年以后，广场舞会更安静，因为现在很多人用蓝牙耳机，大家听同一首歌，但是不会吵到邻居。另外，随着年轻人越来越多地参加，音乐的种类可能也会更多，比如加进中国风的流行歌曲。"],
      rows=[("Task execution", 2, "All four questions answered directly and appropriately, each with a reason or example.", "Answers that restate the question or stop after one sentence; fewer than three answered."),
            ("Cultural understanding", 2, "At least one comparison or reflection linking a perspective to a practice (answer 2: personal space vs. collective life).", "Describing practices with no explanation; stereotypes such as 中国人都……."),
            ("Language control", 3, "Varied structures (不只是……更是, 跟……相比, 本来以为……没想到, 随着) and paraphrase when needed.", "Vocabulary too limited to keep the answer going for 40 seconds."),
            ("Fluency", 2, "Fluid speech with natural pacing that fills the 40 seconds.", "Long pauses; restarting sentences.")],
      tips=[r"Each model answer puts the claim in its first sentence and then adds one reason and one example, which fills about 40 seconds. Answer 2 qualifies its comparison (在我住的城市, 一般, 可能) instead of generalizing about whole countries."])

GUIDE, QSET = G, Q
