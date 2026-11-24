from model import Doc

STEM = "02-language-culture"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 2: Language and Culture", r"Unit 2 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 2 asks how language and culture shape each other, how both change over time, and how technology changes them. Its recommended contexts are customs and celebrations, linguistics, and Chinese in the world. This guide covers the vocabulary of the language itself (characters, tones, dialects, idioms), the major festivals and their customs, the homophone culture behind many traditions, the cause-and-concession patterns the unit's readings lean on, and a Story Narration kit, since the CED places the story task in this unit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 11+ \qquad Festivals I mix up: \blank[10em]",
        short="Unit 2", sub="Language and Culture")

G.sec("Talking about the language")
G.tex(r"""
\begin{vocab}
汉字 / 简体字 / 繁体字 & hànzì / jiǎntǐzì / fántǐzì & Chinese characters / simplified / traditional characters \\
拼音 / 声调 & pīnyīn / shēngdiào & pinyin romanization / tone \\
普通话 / 国语 / 华语 & pǔtōnghuà / guóyǔ / huáyǔ & Mandarin (mainland / Taiwan / Singapore and Malaysia usage) \\
方言 / 粤语 / 上海话 & fāngyán / yuèyǔ / Shànghǎihuà & dialect / Cantonese / Shanghainese \\
成语 / 俗语 / 歇后语 & chéngyǔ / súyǔ / xiēhòuyǔ & four-character idiom / common saying / two-part allegorical saying \\
谐音 & xiéyīn & homophone; a pun based on similar sound \\
偏旁 / 部首 / 笔画 & piānpáng / bùshǒu / bǐhuà & character component / radical / stroke \\
书法 & shūfǎ & calligraphy \\
网络用语 & wǎngluò yòngyǔ & internet slang \\
外来词 & wàiláicí & loanword (咖啡, 沙发, 巧克力) \\
华人 / 华侨 / 华裔 & huárén / huáqiáo / huáyì & ethnic Chinese / overseas Chinese citizens / people of Chinese descent \\
唐人街 / 中文学校 & tángrénjiē / Zhōngwén xuéxiào & Chinatown / weekend Chinese school \\
\end{vocab}

\textbf{Language and identity.} Mandarin is the common language, but many families also speak a regional language such as Cantonese, Hokkien or Shanghainese at home. Overseas, weekend Chinese schools and Chinatowns keep the language alive across generations. \textbf{Technology and language}: pinyin input on phones means many people type far more characters than they write by hand, which has produced the worry about 提笔忘字 (picking up a pen and forgetting how to write a character).
""")
G.q("1 Language", r"提笔忘字 describes",
    "forgetting how to write characters by hand because one mostly types", [("forgetting to bring a pen to class", "提笔 is “to pick up the pen”; the phrase is about forgetting characters."),
                                                                           ("writing characters with the wrong tones", "Tones are spoken; the phrase is about handwriting."),
                                                                           ("refusing to learn traditional characters", "Nothing about traditional characters.")],
    "提笔 (pick up a pen) + 忘字 (forget the character).",
    "The phrase names a modern worry: typing in pinyin lets people recognize characters but forget how to write them.",
    ["Read the idiom literally, then apply it to technology."])
G.q("1 Language", r"咖啡, 沙发 and 巧克力 are all examples of",
    "loanwords", [("four-character idioms", "成语 have four characters and a fixed meaning; these are sound-borrowed foreign words."),
                  ("dialect words", "They are standard Mandarin."),
                  ("radicals", "Radicals are parts of characters, not whole words.")],
    "Sound-borrowed foreign words = 外来词.",
    "咖啡 (coffee), 沙发 (sofa) and 巧克力 (chocolate) imitate the sound of the foreign word: loanwords.",
    ["Say them aloud: kāfēi, shāfā, qiǎokèlì."])
G.q("1 Language", r"A Singaporean speaker calls Mandarin",
    "华语", [("国语", "国语 is the usual name in Taiwan."),
             ("粤语", "粤语 is Cantonese, a different language."),
             ("方言", "方言 means dialect or regional language.")],
    "华语 = Mandarin in Singapore and Malaysia.",
    "The same language has different names in different communities: 普通话 (mainland), 国语 (Taiwan), 华语 (Singapore, Malaysia).",
    ["Match each name to its community."])

G.sec("Festivals and customs")
G.tex(r"""
\begin{compare}{Festival (date)}{Practices and products}{Perspective}
春节 (1st of the 1st lunar month) & 年夜饭, 饺子 (north), 年糕, 红包, 贴春联, 放鞭炮, 拜年 & Reunion; a fresh start; good fortune for the year \\
元宵节 (15th of the 1st month) & 汤圆/元宵, 猜灯谜 (lantern riddles), 看花灯 & The first full moon: family togetherness \\
清明节 (around April 5) & 扫墓 (sweeping ancestors' graves), 踏青 (spring outing) & Respect and remembrance for ancestors \\
端午节 (5th of the 5th month) & 粽子, 赛龙舟 (dragon boat races); remembering 屈原 & Loyalty; warding off illness in summer \\
中秋节 (15th of the 8th month) & 月饼, 赏月 (admiring the moon); the legend of 嫦娥 & Reunion: the full, round moon (月圆人团圆) \\
重阳节 (9th of the 9th month) & 登高 (climbing heights), 敬老 & Respect for the elderly; long life \\
\end{compare}

\begin{vocab}
农历 / 阳历 & nónglì / yánglì & lunar calendar / solar calendar \\
生肖 & shēngxiào & Chinese zodiac animal \\
压岁钱 & yāsuìqián & New Year money given to children (in 红包) \\
拜年 & bàinián & to pay a New Year call, offer New Year wishes \\
春联 / 福字 & chūnlián / fúzì & New Year couplets / the character 福 posted on doors \\
风俗 / 习俗 / 传统 & fēngsú / xísú / chuántǒng & custom / custom / tradition \\
庆祝 / 过节 & qìngzhù / guòjié & to celebrate / to celebrate a festival \\
\end{vocab}
""")
G.q("2 Festivals", r"Which festival is associated with racing dragon boats and eating 粽子?",
    "端午节", [("中秋节", "中秋节 is for mooncakes and admiring the full moon."),
               ("元宵节", "元宵节 is for 汤圆, lanterns and lantern riddles."),
               ("清明节", "清明节 is for sweeping ancestors' graves.")],
    "端午节: 粽子 + 赛龙舟 (Qu Yuan).",
    "The Dragon Boat Festival on the 5th day of the 5th lunar month remembers the poet Qu Yuan with zongzi and boat races.",
    ["粽子 and 龙舟 → 端午."])
G.q("2 Festivals", r"Why is the Mid-Autumn Festival linked to family reunion?",
    "The full, round moon symbolizes completeness and togetherness.", [("It is the only day families have off work.", "The link is symbolic, not about holidays from work."),
                                                                     ("Families must sweep ancestors' graves together.", "Grave sweeping is the Qingming Festival."),
                                                                     ("Children receive red envelopes.", "红包 belong to the Spring Festival.")],
    "月圆人团圆: round moon ↔ reunited family.",
    "Roundness (圆) suggests completeness; the full moon and round mooncakes stand for a family that is together (团圆).",
    ["The product (round mooncake, full moon) expresses the perspective (reunion)."])
G.q("2 Festivals", r"扫墓 is a practice of which festival?",
    "清明节", [("春节", "春节 practices include 拜年 and 年夜饭."),
               ("重阳节", "重阳节 practices are 登高 and honoring the elderly."),
               ("元宵节", "元宵节 practices are lanterns and 汤圆.")],
    "清明 = 扫墓.",
    "Qingming, around April 5, is when families clean their ancestors' graves and remember them.",
    ["扫 (sweep) + 墓 (grave) → Qingming."])

G.sec("Homophones and taboos")
G.tex(r"""
Many customs rest on 谐音, words that sound like other words. Reading questions ask why a custom exists; the answer is often a pun.

\begin{compare}{Custom}{Sounds like}{So}
吃鱼 at New Year, leaving some & 鱼 yú $\approx$ 余 yú (surplus) & 年年有余: abundance every year \\
福 posted upside down & 倒 dào (upside down) $\approx$ 到 dào (arrive) & 福到了: good fortune has arrived \\
年糕 & 糕 gāo $\approx$ 高 gāo (high) & 年年高: rising every year \\
Avoiding the number 四 & 四 sì $\approx$ 死 sǐ (death) & Buildings may skip floor 4 \\
Liking 八 & 八 bā $\approx$ 发 fā (prosper) & 888 in phone numbers and prices \\
Not giving a clock & 送钟 sòng zhōng $\approx$ 送终 sòngzhōng (attend a deathbed) & A clock is an unlucky gift \\
Not splitting a pear & 分梨 fēn lí $\approx$ 分离 fēnlí (separate) & Friends and couples don't share a pear \\
\end{compare}
""")
G.q("3 Homophones", r"A family leaves some fish uneaten at the New Year's Eve dinner. Why?",
    "鱼 sounds like 余, so leftover fish wishes for surplus every year", [("Fish is unlucky to finish because it is a symbol of death", "Fish is lucky, not a death symbol; 四 is the number avoided for that reason."),
                                                                        ("The fish is saved for the Lantern Festival", "There is no such custom; the point is the pun."),
                                                                        ("Eating fish at night is considered unhealthy", "Health is not the reason; the reason is 年年有余.")],
    "鱼 yú ≈ 余 yú → 年年有余.",
    "Many New Year foods are chosen for their sound. Leaving fish means there is “fish left over,” which sounds like “surplus left over.”",
    ["Say 有鱼 and 有余 aloud: identical."])
G.q("3 Homophones", r"Why would a clock be considered an inappropriate gift?",
    "送钟 sounds like 送终, which is associated with death", [("Clocks are too expensive", "Price is not the reason; the problem is the phrase “give a clock.”"),
                                                            ("Clocks remind people they are late", "This is a joke, not the cultural reason."),
                                                            ("The number on a clock includes 四", "The taboo is about the phrase 送钟.")],
    "送钟 ≈ 送终.", "To 送终 is to attend a parent at their death; saying 送钟 (give a clock) evokes it.",
    ["Identify the homophone and its meaning."])

G.sec("Patterns for causes, contrasts and examples")
G.tex(r"""
Readings in this unit explain why customs exist and how they are changing. They lean on these connectors.

\begin{compare}{Pattern}{Function}{Example}
之所以……是因为…… & result, then the reason & 人们之所以贴倒福，是因为“倒”和“到”同音。 \\
由于……因此…… & formal cause and result & 由于手机普及，因此手写的机会越来越少。 \\
随着…… & as (something changes) & 随着时代的发展，过年的方式也变了。 \\
虽然……但是/却…… & concession & 虽然发电子红包很方便，但是有人觉得少了年味。 \\
不但……而且…… & addition & 汉字不但是文字，而且是一种艺术。 \\
以……为例 & taking X as an example & 以春节为例，很多年轻人现在“旅游过年”。 \\
被称为 / 叫做 & is called & 中秋节也被称为“团圆节”。 \\
据说 & it is said & 据说，月饼的历史有一千多年了。 \\
\end{compare}

\begin{trap}
却 is an adverb, so it goes after the subject: 他虽然是美国人，\textbf{却}会说流利的粤语 — not 却他会说. 但是 goes before the subject.
\end{trap}
""")
G.q("4 Patterns", r"人们之所以贴倒福，是因为“倒”和“到”同音。 Which part gives the reason?",
    "“倒”和“到”同音", [("人们贴倒福", "This is the result being explained."),
                    ("之所以", "之所以 marks the result clause, not the reason."),
                    ("同音 only", "同音 alone is a fragment; the whole clause after 是因为 is the reason.")],
    "之所以 [result]，是因为 [reason].", "之所以……是因为 states the result first and the reason after 是因为.",
    ["Reason follows 是因为."])
G.q("4 Patterns", r"Choose the correct sentence.",
    "他虽然在美国长大，却会说流利的中文。", [("他虽然在美国长大，却他会说流利的中文。", "却 is an adverb; it must follow the subject: 他却会."),
                                           ("虽然他在美国长大，所以会说流利的中文。", "虽然 pairs with 但是/却, not 所以."),
                                           ("他在美国长大虽然，却会说流利的中文。", "虽然 comes at the start of the clause or right after the subject, never at the end.")],
    "却 after the subject (or no subject repeated).", "虽然……却: 却 goes in the adverb position, after any subject.",
    ["Check where 却 sits."])
G.q("4 Patterns", r"随着科技的发展，越来越多的人用手机发红包。 What does 随着 express?",
    "a change that happens along with another change", [("a contrast between two facts", "Contrast would use 但是/却/然而."),
                                                       ("a condition that must be met", "Conditions use 只要/只有/如果."),
                                                       ("an example", "Examples use 比如/例如/以……为例.")],
    "随着 X = as X changes.", "随着 introduces a development that brings another one with it.",
    ["随着科技的发展 → 越来越多的人……"])

G.sec("Task kit: Story Narration")
G.tex(r"""
\begin{compare}{Purpose}{Words}{Example}
Setting the scene & 有一天，那天，上个周末，春节前 & 春节前一天，小华和爸爸一起去买年货。 \\
Something happening & 正在……的时候，突然，忽然，一不小心 & 正在贴春联的时候，突然刮起了大风。 \\
Reaction & 于是，只好，赶紧，马上 & 小华赶紧跑过去追。 \\
Surprise & 没想到，原来，居然 & 没想到，春联被邻居家的小狗叼走了。 \\
Outcome & 结果，最后，终于 & 最后，大家一起笑着把春联贴好了。 \\
Ending & 从那以后，这件事让他明白了…… & 这件事让他明白了“福到了”的意思。 \\
\end{compare}

\begin{keyidea}[Add culture to a story without forcing it]
If a picture shows a festival or a family meal, name the custom and give its meaning in one clause: 他们把“福”字倒着贴，意思是“福到了”。 One natural cultural detail supports the language control row (culturally relevant expressions) and makes the story concrete.
\end{keyidea}
""")
G.q("5 Story", r"A picture shows a boy chasing a couplet blown off a door by the wind. Which sentence best links it to the previous picture of him putting the couplet up?",
    "正在他贴春联的时候，突然刮起了一阵大风。", [("然后他贴春联。然后刮风。", "Repeated 然后 with two flat sentences: weak cohesion."),
                                              ("因为他贴春联，所以刮风。", "The wind is not caused by putting up the couplet."),
                                              ("他贴春联，和刮大风。", "和 cannot join clauses.")],
    "正在……的时候，突然…… links an ongoing action to an interruption.",
    "This frame shows a logical, time-based link between pictures, which the organization row rewards.",
    ["Action in progress + sudden event."])
G.q("5 Story", r"Which ending gives the story a clear resolution?",
    "最后，大家一起把春联重新贴好，小华也明白了“福到了”的意思。", [("然后他们吃了饭。", "A bare event with no link to the problem in the story."),
                                                              ("这个故事很有意思。", "Comments on the story instead of ending it."),
                                                              ("突然又刮起了大风。", "Introduces a new problem instead of resolving the old one.")],
    "最后 + resolution + what was learned.", "A resolution closes the problem and can add a lesson or feeling, completing beginning, middle and end.",
    ["Does the sentence solve the story's problem? Only the first does."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 2: Language and Culture: Question Set", r"Unit 2 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (a Presentation and Instructional Guidance for listening, a Literary Text and Promotional Material for reading) on Chinese characters and dialects, festivals, and language online, followed by a Story Narration task with a scoring guide and a model story. Listening sources are printed as transcripts: read each once at normal speed, then answer without rereading. Questions and choices are in English, as on past AP Chinese exams. All sources are original and written for practice. Allow about 25 minutes for the multiple choice and 15 minutes for the story.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Story: \blank\ / 8 \qquad Target: 16+ MCQ and 6+ story \qquad Pace: 75 s per item",
        short="Unit 2", sub="Language and Culture")

Q.sec("Listening: Presentation")
Q.src(r"Listening 1 \textperiodcentered\ Presentation (transcript) \textperiodcentered\ A student's talk in a culture class", [
    "大家好！今天我想跟大家谈谈汉字里的“家”字。",
    "大家看，“家”字上面是一个“宀”，表示房子；下面是“豕”，也就是猪。为什么家里会有一头猪呢？有一种说法是，在古代，养猪的人家生活比较稳定，有房子、有猪，才算是一个家。",
    "从这个字我们可以看出，在古人的观念里，家首先是一个能让人吃饱、住好的地方。",
    "不过，随着时代的变化，“家”的意思也越来越丰富。比如“国家”这个词，就是把国和家放在一起，说明在中国文化里，人们常常把国家看成一个大家庭。还有“大家”，意思是所有的人，好像每个人都是一家人。",
    "最后，我想说，学汉字不只是记笔画，每个汉字背后都有一个故事。了解了这些故事，汉字就不再难记了。谢谢大家！",
], 5)
Q.q("1.B.1 Main idea", "What is the presentation mainly about?",
    "what the character 家 shows about Chinese ideas of home", [("how to raise pigs in ancient China", "The pig explains the character; farming is not the topic."),
                                                           ("why simplified characters were created", "Simplification is not mentioned."),
                                                           ("how to write characters in the right stroke order", "The speaker says learning characters is more than strokes.")],
    "今天我想跟大家谈谈汉字里的“家”字.", "The opening sentence names the topic, and every later part interprets 家.",
    ["Main idea: the topic sentence plus the conclusion."])
Q.q("1.A.1 Detail", "According to the speaker, what does the top part of 家 represent?",
    "a roof or house", [("a pig", "The pig is the bottom part (豕)."),
                        ("a person", "No person component is described."),
                        ("a field", "No field is mentioned.")],
    "上面是一个“宀”，表示房子.", "宀 is the “roof” radical, found in 家, 室, 安.",
    ["上面 = top part → 宀 → house."])
Q.q("1.C.2 Conclusion", "Why, according to one explanation, does 家 contain a pig?",
    "Keeping pigs meant a household had a stable living.", [("Pigs were sacred animals.", "Nothing is said about sacred animals."),
                                                           ("The character was drawn by a farmer.", "No author is mentioned."),
                                                           ("Pigs and people lived in separate buildings.", "The speaker says house and pig together made a home.")],
    "养猪的人家生活比较稳定.", "The speaker gives one explanation (有一种说法): a house plus a pig meant a secure household.",
    ["有一种说法 introduces the explanation."])
Q.q("1.B.4 Organization", "How does the speaker support the point that the meaning of 家 has broadened?",
    "by giving the words 国家 and 大家 as examples", [("by quoting an ancient poem", "No poem is quoted."),
                                                  ("by comparing 家 with an English word", "No English comparison is made."),
                                                  ("by citing survey numbers", "No statistics are given.")],
    "比如“国家”……还有“大家”.", "比如 introduces examples that support the claim made just before.",
    ["Claim: meaning became richer. Support: two compound words."])
Q.q("1.B.3 Point of view", "What is the speaker's view on learning characters?",
    "Knowing the stories behind them makes them easier to remember.", [("Memorizing strokes is the only effective method.", "The speaker says learning is not only memorizing strokes."),
                                                                      ("Characters are too hard for most students.", "The speaker says they become easier."),
                                                                      ("Students should learn pinyin instead.", "Pinyin is not mentioned.")],
    "了解了这些故事，汉字就不再难记了.", "The closing gives the speaker's view: understanding the story behind a character makes it easier to remember.",
    ["最后，我想说 introduces the opinion."])

Q.sec("Reading: Literary Text")
Q.src(r"Reading 1 \textperiodcentered\ Literary Text \textperiodcentered\ From a short story", [
    "奶奶的电话总是在星期天晚上八点准时打来。她只会说广东话，而我的广东话，只够说“食咗饭未呀”（吃饭了没有）。",
    "小时候，我觉得这个电话很麻烦。奶奶在电话那头说得又快又多，我只能“嗯、嗯”地答着，然后把电话交给爸爸，自己跑去看电视。",
    "上了高中，我选了中文课。老师说，语言是一座桥。我不太明白，直到去年夏天，我跟爸爸回香港看奶奶。",
    "奶奶已经住进了医院。她拉着我的手，慢慢地说了一句话。我用尽了自己所有的中文，终于听懂了：“你长大了，奶奶好开心。”",
    "那一刻，我突然明白了老师的话。从那以后，我每个星期都跟爸爸学一点广东话。现在，星期天晚上八点的电话，我总是第一个跑去接。",
], 5)
Q.q("1.A.1 Detail", "Why did the narrator find the phone calls troublesome as a child?",
    "The narrator could barely understand Grandmother's Cantonese.", [("Grandmother always called during dinner.", "The call came at 8 p.m., and nothing says it interrupted dinner."),
                                                                     ("The narrator's father did not allow TV.", "The narrator ran off to watch TV."),
                                                                     ("The calls were too short.", "Grandmother spoke 又快又多: fast and a lot.")],
    "我的广东话只够说…… / 说得又快又多.", "The narrator's Cantonese was limited to one phrase, and Grandmother spoke fast and long.",
    ["小时候，我觉得这个电话很麻烦 + the following sentence."])
Q.q("1.B.5 Word meaning", r"The teacher says 语言是一座桥. In the story, this means that language",
    "connects people, such as the narrator and Grandmother", [("is hard to cross, like a long bridge", "The image is about connection, not difficulty."),
                                                           ("is learned best while traveling", "Travel is the setting, not the point of the metaphor."),
                                                           ("should be studied in Hong Kong", "No place is recommended.")],
    "A bridge connects two sides.", "The story shows language connecting the narrator with Grandmother, which is when the narrator understands the metaphor.",
    ["The narrator understands the saying at the moment of connection with Grandmother."])
Q.q("1.B.4 Turning point", "What is the turning point in the story?",
    "understanding Grandmother's words at the hospital", [("choosing a Chinese class in high school", "This leads up to the change but the narrator still did not understand."),
                                                         ("running away to watch TV", "This shows the narrator before the change."),
                                                         ("Grandmother learning English", "Grandmother only speaks Cantonese.")],
    "那一刻，我突然明白了.", "那一刻 (at that moment) marks the turning point, followed by 从那以后 (from then on).",
    ["Look for 那一刻 and 从那以后."])
Q.q("1.B.3 Feeling", "How does the narrator feel about the Sunday calls now?",
    "eager", [("bored", "The narrator is always the first to answer."),
              ("nervous", "Nothing suggests nervousness."),
              ("annoyed", "That was the narrator's childhood feeling, not the present one.")],
    "总是第一个跑去接 = eager.", "Running to be the first to answer shows eagerness, the reverse of the childhood reaction.",
    ["Compare 小时候 with 现在."])
Q.q("1.C.1 Connect", "Which detail at the end connects most directly to the story's beginning?",
    "the Sunday 8 p.m. phone call", [("the hospital visit", "The hospital is in the middle of the story."),
                                     ("the Chinese class", "The class is introduced in the middle."),
                                     ("the trip with the father", "The trip is in the middle.")],
    "Same call, opposite reaction.", "The story opens and closes with the Sunday call, showing how the narrator has changed.",
    ["Frame structure: first and last paragraphs."])

Q.sec("Reading: Promotional Material")
Q.src(r"Reading 2 \textperiodcentered\ Promotional Material \textperiodcentered\ A flyer", [
    "\\textbf{“汉字之美”寒假书法班}",
    "想写一手漂亮的毛笔字吗？想了解每个汉字背后的故事吗？欢迎参加华光中文学校寒假书法班！",
    "上课时间：一月六日至一月二十四日，每周一、三、五下午两点到四点",
    "地点：华光中文学校三楼",
    "对象：十至十八岁学生，零基础也可以",
    "费用：每人三百元（含笔、墨、纸）；两人一起报名，每人二百五十元",
    "课程最后一天，学生将用自己写的春联布置学校大厅，家长也可以来参观。",
    "名额有限，只收二十人。报名请在一月三日以前打电话：(408) 555-0123，或者扫描下面的二维码。",
], 5)
Q.q("1.B.2 Audience", "Who is the class for?",
    "students aged 10 to 18, including beginners", [("only students who already know calligraphy", "零基础也可以: beginners are welcome."),
                                                    ("parents of young children", "Parents may visit at the end, but the class is for students."),
                                                    ("adults over eighteen", "对象 is ten to eighteen.")],
    "对象：十至十八岁学生，零基础也可以.", "对象 names the target group; 零基础 means no prior experience.",
    ["Find 对象."])
Q.q("1.A.1 Detail", "How often does the class meet?",
    "three afternoons a week", [("every day for three weeks", "It meets Monday, Wednesday and Friday only."),
                                 ("once a week on weekends", "The days given are weekdays."),
                                 ("every morning", "Classes are 下午两点到四点.")],
    "每周一、三、五下午.", "每周一、三、五 = every Monday, Wednesday and Friday.",
    ["Read 上课时间."])
Q.q("1.A.2 Price", "Two friends sign up together. How much do they pay in total?",
    "500 yuan", [("600 yuan", "600 would be two people at the regular price; the pair price is 250 each."),
                 ("250 yuan", "250 is the price per person, not the total."),
                 ("300 yuan", "300 is the regular price for one person.")],
    "两人一起报名，每人二百五十元 → 2 × 250 = 500.", "The discount is per person: two people at 250 each.",
    ["每人 = per person.", "2 × 250 = 500."])
Q.q("1.A.1 Detail", "What will happen on the last day of the class?",
    "Students will decorate the school hall with couplets they wrote.", [("Students will take a written test.", "No test is mentioned."),
                                                                       ("Parents will teach calligraphy.", "Parents only come to look (参观)."),
                                                                       ("The school will sell the students' work.", "Nothing is sold.")],
    "用自己写的春联布置学校大厅.", "布置 means to decorate; the couplets are the students' own work.",
    ["课程最后一天 → the event."])
Q.q("1.C.3 Inference", "What can be inferred about signing up?",
    "Students should register early because places are limited.", [("Registration is open until the class begins.", "The deadline is January 3, before the class starts on January 6."),
                                                                  ("Students must register in person at the school.", "Registration is by phone or QR code."),
                                                                  ("Only pairs may register.", "Pairs get a discount, but individuals may register.")],
    "名额有限，只收二十人 + a deadline.", "名额有限 (limited places) with a cap of twenty implies signing up early.",
    ["名额有限 is the clue."])

Q.sec("Listening: Instructional Guidance")
Q.src(r"Listening 2 \textperiodcentered\ Instructional Guidance (transcript) \textperiodcentered\ A teacher explains a project", [
    "同学们，下个月我们要做一个“我家的过年故事”的小项目。我先把要求说清楚。",
    "第一，每个人要采访一位家里的长辈，比如爷爷奶奶或者外公外婆，问问他们小时候怎么过年。采访最少十五分钟，记得先问长辈可不可以录音。",
    "第二，根据采访的内容，写一篇三百到五百字的短文。短文里要比较一下以前和现在过年有什么不同。",
    "第三，带一样跟过年有关的东西来学校，可以是一张老照片、一个红包，或者一件传统的小东西，然后跟同学们介绍它的意思。",
    "短文下个月十五号交，介绍放在十六号和十七号两天的课上。如果你家里没有长辈可以采访，可以来找我，我帮你联系学校附近养老院的老人。",
], 5)
Q.q("1.B.1 Purpose", "What is the purpose of the teacher's talk?",
    "to explain the requirements of a project", [("to describe how the teacher's family celebrates New Year", "The teacher does not tell a personal story."),
                                                 ("to announce a New Year party", "No party is announced."),
                                                 ("to invite students to a nursing home", "The nursing home is only a backup for some students.")],
    "我先把要求说清楚.", "The teacher states the purpose (making the requirements clear) and then lists them.",
    ["Instructional guidance → steps and requirements."])
Q.q("1.A.1 Detail", "What must students do before recording the interview?",
    "ask the elder's permission", [("write the essay", "The essay is written after the interview."),
                                   ("email the teacher", "No email is required."),
                                   ("buy a red envelope", "A red envelope is one possible object, not a requirement before recording.")],
    "记得先问长辈可不可以录音.", "先 marks what comes first: asking permission to record.",
    ["Find 先 in the first requirement."])
Q.q("1.A.1 Detail", "What must the essay include?",
    "a comparison of past and present New Year celebrations", [("a recipe for a festival dish", "No recipe is required."),
                                                              ("the elder's full life story", "The focus is on how they celebrated New Year."),
                                                              ("at least 1,000 characters", "The length is 300 to 500 characters.")],
    "要比较一下以前和现在过年有什么不同.", "The second requirement says the essay must compare then and now.",
    ["第二 → 短文里要……"])
Q.q("1.A.1 Sequence", "In what order are the tasks due?",
    "the essay on the 15th, then the presentations on the 16th and 17th", [("the presentations first, then the essay", "The essay is due first (15th)."),
                                                                       ("everything on the 15th", "Presentations are on the 16th and 17th."),
                                                                       ("the interview recording on the 15th", "The recording is not something students hand in.")],
    "短文……十五号交，介绍……十六号和十七号.", "Two dates: essay due on the 15th, introductions on the 16th and 17th.",
    ["Listen for each 号."])
Q.q("1.C.3 Inference", "What can be inferred about a student whose grandparents live overseas and are hard to reach?",
    "The teacher will help arrange an interview with an elder from a nursing home.", [("The student can skip the interview.", "The teacher offers an alternative, not an exemption."),
                                                                                    ("The student must fly overseas.", "Nothing so extreme is suggested."),
                                                                                    ("The student will interview the teacher.", "The teacher offers to contact nursing-home residents.")],
    "没有长辈可以采访 → 来找我 → 养老院的老人.", "The teacher's offer covers students without an elder available to interview.",
    ["如果……可以来找我 → the alternative."])

Q.frq(kind="Story Narration", head=r"Question 3 \textperiodcentered\ Story Narration \textperiodcentered\ 8 points \textperiodcentered\ about 15 minutes",
      mins=15,
      directions=[r"\textbf{Directions.} The four pictures present a story. Imagine you are writing the story for a student magazine. Narrate a complete story as suggested by the pictures, in their order, with logical organization and relevant details."],
      panels=["春节前，一个女孩和爸爸站在门口，女孩手里拿着一张“福”字，正要把它贴在门上。",
              "女孩把“福”字倒着贴好了，很高兴。爸爸看了，皱着眉头，好像想说什么。",
              "爷爷从屋里走出来，笑着指着倒贴的“福”字，跟女孩和爸爸说话。",
              "晚上，一家人围着桌子吃年夜饭，桌上有鱼和饺子，门上的“福”字还是倒着的。"],
      model=["春节前一天，小丽和爸爸在家门口贴春联。小丽手里拿着一张红红的“福”字，开心地说：“这张让我来贴！”",
             "可是她一不小心，把“福”字贴倒了。小丽看了看，还觉得挺好看的。爸爸却皱起了眉头，正想让她撕下来重新贴。",
             "就在这时，爷爷从屋里走了出来。他看了一眼，哈哈大笑：“贴得好！‘福’倒了，就是‘福到了’啊！”原来，“倒”和“到”同音，很多人家都故意把“福”字倒着贴，希望新的一年福气到家。爸爸听了，也笑着点了点头。",
             "晚上，全家人围坐在一起吃年夜饭。桌子上有饺子，还有一条大鱼，奶奶说这叫“年年有余”。小丽看着门上那个倒着的“福”字，心里想：原来一个小小的字，也藏着这么多的祝福。"],
      rows=[("Narrative development", 3, "All four pictures in order, with details (the mistake, the father's frown, the grandfather's explanation, the dinner) and dialogue.", "Describing each picture without explaining why the 福 is upside down; skipping the dinner."),
            ("Organization", 2, "Beginning, middle, end; links such as 可是，一不小心，正想……，就在这时，原来，晚上.", "Four disconnected descriptions."),
            ("Language control", 3, "Varied grammar (把, 让, 得, 正想, 原来) and culturally relevant expressions (福到了, 年年有余, 年夜饭) used naturally; consistent narrative tense marking with 了.", "Errors with 把 and 了; basic vocabulary.")],
      tips=[r"The story's twist depends on the homophone 倒/到, and the model explains it in one clause through the grandfather instead of lecturing. 就在这时 and 原来 make the turn of picture 3 clear, and the ending ties the custom back to the girl's feelings."])

GUIDE, QSET = G, Q
