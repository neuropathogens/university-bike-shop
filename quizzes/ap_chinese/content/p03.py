from ap_chinese.model import Doc

STEM = "03-art-creativity"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 3: Art and Creativity", r"Unit 3 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 3 asks how art and creativity shape daily life, how art both reflects and challenges cultural perspectives, how communities value art, and how art records history. Its recommended contexts are architecture, artistic heritage, beauty and aesthetics, fashion and design, literature, and visual and performing arts. Unit 3 matters twice in 2026--27: the course project for the May 2027 exam uses music as its lens, so this guide gives music its own section and ends with a Project Presentation kit. It also covers the traditional arts and architecture, the language for describing and evaluating art, and the aesthetic ideas most often linked to Chinese art (留白, harmony, 知音). Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 11+ \qquad Project factors I could use: \blank[10em]",
        short="Unit 3", sub="Art and Creativity")

G.sec("Traditional arts and architecture")
G.tex(r"""
\begin{vocab}
书法 / 毛笔 / 墨 & shūfǎ / máobǐ / mò & calligraphy / writing brush / ink \\
国画 / 山水画 & guóhuà / shānshuǐhuà & Chinese painting / landscape painting \\
剪纸 & jiǎnzhǐ & paper-cutting \\
瓷器 / 青花瓷 & cíqì / qīnghuācí & porcelain / blue-and-white porcelain \\
刺绣 & cìxiù & embroidery \\
京剧 / 戏曲 / 脸谱 & jīngjù / xìqǔ / liǎnpǔ & Peking opera / traditional opera / painted opera faces \\
园林 & yuánlín & classical garden (e.g., the gardens of Suzhou) \\
四合院 & sìhéyuàn & courtyard house (Beijing) \\
故宫 / 长城 & Gùgōng / Chángchéng & the Palace Museum / the Great Wall \\
旗袍 / 汉服 & qípáo / hànfú & qipao / Han-style clothing (now revived as fashion) \\
文物 / 博物馆 / 展览 & wénwù / bówùguǎn / zhǎnlǎn & cultural relic / museum / exhibition \\
非物质文化遗产（非遗） & fēi wùzhì wénhuà yíchǎn & intangible cultural heritage \\
传承 & chuánchéng & to pass down (a tradition) \\
\end{vocab}

\textbf{Architecture records values.} A 四合院 faces inward around a courtyard, with the most important rooms on the north side for the eldest generation: the layout expresses family hierarchy and privacy. Classical gardens imitate mountains and water in a small space so that a walk becomes a sequence of ``borrowed'' views (借景).

\textbf{Opera faces.} In Peking opera, the colors of 脸谱 signal character: red for loyalty and courage, white for treachery, black for honesty and boldness. The four role types are 生 (male), 旦 (female), 净 (painted-face) and 丑 (clown).
""")
G.q("1 Arts", r"In Peking opera, a character with a red painted face is usually",
    "loyal and brave", [("treacherous", "Treachery is shown by white."),
                        ("a clown", "Clowns (丑) are marked by a white patch around the nose, not a red face."),
                        ("a young woman", "Female roles (旦) do not use the painted faces of 净 roles.")],
    "Red 脸谱 = loyalty and courage.",
    "Face colors are a visual code: red for loyalty and courage, white for treachery, black for honesty and boldness.",
    ["Recall the color code."])
G.q("1 Arts", r"How does the layout of a 四合院 reflect a cultural perspective?",
    "The best rooms go to the eldest generation, showing respect for family hierarchy.",
    [("Rooms face the street so the family can watch the neighbors.", "A 四合院 faces inward to its courtyard."),
     ("Every family member gets an identical room.", "Rooms are ranked, with the main north rooms for the elders."),
     ("It has no courtyard, to save space.", "The courtyard is its defining feature.")],
    "Layout (product) ↔ hierarchy and privacy (perspective).",
    "The inward-facing courtyard and the ranking of rooms express privacy and respect for elders.",
    ["Product: the house layout.", "Perspective: family hierarchy."])
G.q("1 Arts", r"传承 is closest in meaning to",
    "passing a tradition down to the next generation", [("selling cultural relics", "Selling is 卖; 传承 is about continuity."),
                                                        ("inventing a new art form", "Invention is 创造/创新."),
                                                        ("visiting a museum", "Visiting is 参观.")],
    "传 (pass on) + 承 (receive, carry on).",
    "传承 means to inherit and pass on, and is the key verb in texts about intangible cultural heritage.",
    ["Break the word into its two characters."])

G.sec("Music")
G.tex(r"""
\begin{vocab}
音乐 / 乐器 / 乐队 & yīnyuè / yuèqì / yuèduì & music / musical instrument / band \\
民乐 / 民族乐器 & mínyuè / mínzú yuèqì & traditional Chinese music / traditional instruments \\
古筝 & gǔzhēng & zither with movable bridges (21 strings on the modern instrument), plucked \\
古琴 & gǔqín & seven-string zither, the scholar's instrument \\
二胡 & èrhú & two-string bowed fiddle \\
琵琶 & pípa & four-string lute, plucked \\
笛子 & dízi & bamboo flute \\
扬琴 & yángqín & hammered dulcimer \\
民歌 / 流行歌曲 / 华语流行（C-pop） & míngē / liúxíng gēqǔ / huáyǔ liúxíng & folk song / pop song / Mandopop \\
中国风 & Zhōngguó fēng & ``Chinese style'' pop that blends traditional instruments, melodies or images with modern pop \\
演奏 / 弹 / 拉 / 吹 & yǎnzòu / tán / lā / chuī & to perform / to pluck (strings, keys) / to bow / to blow \\
旋律 / 节奏 / 歌词 & xuánlǜ / jiézòu / gēcí & melody / rhythm / lyrics \\
音乐会 / 演唱会 & yīnyuèhuì / yǎnchànghuì & concert (instrumental) / concert (singer) \\
KTV / 唱K & & karaoke / to sing karaoke, a common group social activity \\
广场舞音乐 & guǎngchǎngwǔ yīnyuè & music for square dancing \\
\end{vocab}

\textbf{Verbs follow how the instrument is played}: 弹古筝, 弹琵琶, 弹钢琴 (pluck or press); 拉二胡, 拉小提琴 (bow); 吹笛子 (blow); 敲 or 打 for percussion; 打扬琴 or 弹扬琴 for the struck dulcimer.

\textbf{Music as product, practice and perspective.} The \emph{product} is the instrument, the song, the recording or the app. The \emph{practice} is how and where people make and use music: a grandmother's square-dance group, friends at KTV, a school 民乐团, a wedding band, a song sung at a festival. The \emph{perspective} is the value behind it: harmony (和), friendship and understanding (知音), collective enjoyment, pride in heritage, or the wish to modernize tradition.

\begin{keyidea}[知音: the story behind the word]
The musician 伯牙 played the 琴 and only his friend 钟子期 could hear what the music meant: ``high mountains'' or ``flowing water'' (高山流水). When 钟子期 died, 伯牙 broke his instrument, because no one else could truly understand his music. A 知音 (one who knows the sound) is still the word for a friend who truly understands you, and 高山流水 is still used for deep friendship and for great music.
\end{keyidea}
""")
G.q("2 Music", r"Which verb goes with 二胡?",
    "拉", [("弹", "弹 is for plucked or keyboard instruments (古筝, 琵琶, 钢琴)."),
           ("吹", "吹 is for wind instruments (笛子)."),
           ("唱", "唱 is to sing.")],
    "Bowed → 拉.", "The erhu is bowed, so it takes 拉, like 拉小提琴.",
    ["How is it played? With a bow → 拉."])
G.q("2 Music", r"A friend who truly understands you is called a 知音. The word comes from a story about",
    "a musician whose friend understood what his music expressed", [("a singer who lost her voice", "The story is about 伯牙 and 钟子期, two men."),
                                                                    ("a teacher who invented musical notation", "No invention is involved."),
                                                                    ("an emperor who banned music", "No emperor appears in the story.")],
    "知音 = one who knows (知) the sound (音).", "伯牙's friend 钟子期 could hear “high mountains” or “flowing water” in his playing; after his friend's death, 伯牙 broke his instrument.",
    ["Break down the word: 知 + 音."])
G.q("2 Music", r"Songs that blend traditional instruments and images with modern pop are described as",
    "中国风", [("民歌", "民歌 are traditional folk songs, not a pop blend."),
               ("戏曲", "戏曲 is traditional opera."),
               ("广场舞", "广场舞 is the dance practice, not a song style.")],
    "中国风 = Chinese-style pop.", "中国风 pop uses traditional sounds, melodies or imagery inside modern pop production.",
    ["The key idea is blending: 中国 + 风 (style)."])

G.sec("Describing and evaluating art")
G.tex(r"""
\begin{compare}{Pattern}{Use}{Example}
给人……的感觉 & the impression art gives & 这首曲子给人一种很安静的感觉。 \\
既……又…… & two qualities at once & 这座建筑既有传统特色，又很现代。 \\
以……为主 / 以……为特色 & main feature & 苏州园林以小巧精致为特色。 \\
把……和……结合起来 & combining & 这首歌把琵琶和电子音乐结合了起来。 \\
无论……都…… & no matter & 无论老人还是年轻人，都喜欢这首民歌。 \\
与其说……不如说…… & it's less A than B & 与其说这是一首歌，不如说是一个故事。 \\
反映 / 表现 / 体现 & to reflect / express / embody & 这幅画体现了“天人合一”的思想。 \\
受……的影响 & influenced by & 他的音乐受到了民歌的影响。 \\
\end{compare}

\begin{vocab}
优美 / 动听 & yōuměi / dòngtīng & graceful, beautiful / pleasant to hear \\
独特 / 精致 & dútè / jīngzhì & unique / exquisite \\
创新 / 创作 & chuàngxīn / chuàngzuò & to innovate / to create (a work) \\
欣赏 & xīnshǎng & to appreciate (art) \\
灵感 & línggǎn & inspiration \\
\end{vocab}
""")
G.q("3 Patterns", r"Choose the sentence that says the song combines pipa with electronic music.",
    "这首歌把琵琶和电子音乐结合了起来。", [("这首歌被琵琶和电子音乐结合了。", "被 would make the song the receiver of the action of the pipa; the meaning is garbled."),
                                        ("这首歌琵琶和电子音乐给人结合。", "给人 is for impressions, not combining."),
                                        ("这首歌无论琵琶都电子音乐。", "无论……都 needs a full clause and means “no matter.”")],
    "把 A 和 B 结合起来.", "结合起来 with 把 moves both items into the combination.",
    ["把 + both items + 结合起来."])
G.q("3 Patterns", r"无论老人还是年轻人，都喜欢这首民歌。 This means",
    "both old and young people like this folk song", [("only young people like this folk song", "无论……都 includes both groups."),
                                                      ("old people like it more than young people", "No comparison is made."),
                                                      ("neither old nor young people like it", "都喜欢 is positive.")],
    "无论 A 还是 B，都 = regardless of A or B.", "无论……都 says the statement holds for every case listed.",
    ["都喜欢 applies to both groups."])

G.sec("Aesthetic perspectives")
G.tex(r"""
\begin{compare}{Idea}{What it means}{Where you see it}
留白 (leaving blank) & Empty space is part of the work; it invites the viewer to imagine. & Landscape painting; calligraphy layout; pauses in 古琴 music \\
天人合一 (harmony of heaven and humanity) & People belong within nature, not above it. & Gardens that imitate mountains and water; landscape painting \\
和 (harmony) & Balance and blending of different elements. & Ensemble 民乐; 和而不同 (harmony without sameness) \\
意境 (artistic mood) & A work should create a mood the viewer can enter, beyond its literal subject. & Poetry, painting, music titles like 高山流水 \\
传统与创新 & Keeping tradition alive by renewing it. & 中国风 pop; 汉服 fashion; museums' creative products \\
\end{compare}

\begin{trap}
In the presentation and Q\&A, \emph{naming} an idea such as 天人合一 earns little; the cultural understanding row rewards showing \emph{how} the perspective explains a specific product or practice: 苏州园林用假山和水池在小空间里表现自然，体现了天人合一的观念。
\end{trap}
""")
G.q("4 Perspectives", r"A landscape painting leaves most of the paper empty above the mountains. This reflects",
    "留白: empty space invites the viewer's imagination", [("a lack of time to finish the painting", "The blank space is deliberate."),
                                                          ("the painter's dislike of mountains", "The mountains are the subject."),
                                                          ("a rule that paintings must be cheap", "Cost is irrelevant.")],
    "留白 = meaningful empty space.", "In Chinese painting, empty space is deliberate: it can be read as mist, sky or water and invites imagination.",
    ["Deliberate blank → 留白."])
G.q("4 Perspectives", "Which sentence best links a product to the perspective behind it?",
    "苏州园林用假山和水池表现自然，体现了天人合一的观念。", [("苏州园林很漂亮。", "An opinion with no perspective."),
                                                           ("苏州园林有很多游客。", "A fact about tourism, not culture."),
                                                           ("我想去苏州园林。", "A personal wish.")],
    "Product (garden) + how + perspective (天人合一).", "The cultural understanding rows reward specific examples that show how a perspective relates to a product or practice.",
    ["Look for 体现了……的观念 attached to a specific feature."])

G.sec("Task kit: the Project Presentation")
G.tex(r"""
The Course Project Packet (January 2027) will give the cultural situation and sources. The kit below works for any music-centered prompt.

\subsection{Choosing three factors}
Pick factors you can support with a specific, researched example, and make at least one of them a cultural perspective:
\begin{enumerate}[leftmargin=2em]
\item a \textbf{product} (an instrument, a genre, a famous piece);
\item a \textbf{practice} (who makes or uses this music, where and when);
\item a \textbf{perspective} (the value that explains it).
\end{enumerate}
Example set for ``how a type of music reflects a community'': 广场舞音乐 (product: upbeat songs and portable speakers), how retirees dance together every evening (practice), and the value of collective activity and health in later life (perspective), with a comparison to how older people exercise in the U.S.

\subsection{A PPR in keywords}
\begin{compare}{Section}{Keywords (sample)}{What you say}
Opening & 广场舞 / 三方面 & topic and the three factors \\
Factor 1 & 音乐：节奏快 / 便携音箱 / 例：某城市调查 & product + one sourced fact \\
Factor 2 & 每天傍晚 / 退休老人 / 社区广场 & practice: who, when, where \\
Factor 3 & 集体 / 健康 / 交朋友 & perspective: why \\
Comparison & 美国：健身房、个人 & one comparison \\
Close & 总而言之 & what the factors show together \\
\end{compare}

\begin{keyidea}[Sentence frames for the presentation]
我的研究题目是…… \quad 我想从三个方面来介绍。 \quad 第一个方面是…… \quad 根据……的资料 / 据……统计 \quad 这说明…… \quad 这反映了……的观念 \quad 跟美国相比…… \quad 总而言之……
\end{keyidea}
""")
G.q("5 Presentation", "Which set of three factors best fits the presentation rubric?",
    "the instrument itself, how people use it today, and the value it expresses", [("three different instruments described one by one", "Three products with no practice or perspective; the rubric asks for at least one cultural perspective."),
                                                                                  ("my favorite song, my favorite singer, my favorite concert", "Personal preferences, not researched factors."),
                                                                                  ("the history of the piano, guitar and violin", "These are not tied to a Chinese-speaking community.")],
    "Product + practice + perspective.", "Task execution needs three factors explained with research; cultural understanding needs a perspective linked to a product or practice.",
    ["Check that one factor is a perspective."])
G.q("5 PPR", "Which entry is best suited to a PPR?",
    "广场舞 / 退休老人 / 每天傍晚 / 集体", [("A full paragraph of the script in sentences", "You may not read the PPR verbatim, and the word limit rules out full sentences."),
                                       ("A list of English translations of hard words", "Translations do not help you organize; keywords in Chinese do."),
                                       ("Nothing: the PPR is optional decoration", "The PPR is the outline you use on exam day; leaving it blank wastes it.")],
    "Keywords that cue each part of your talk.", "A PPR is a word-limited outline: brief keyword cues, written by you, that keep the 3-minute talk organized.",
    ["Keywords, not sentences."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 3: Art and Creativity: Question Set", r"Unit 3 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (Audio and Chart and a Conversation for listening, Article and Chart and Correspondence for reading) on music, traditional arts and their place in young people's lives, followed by a practice Project Presentation on music, the 2026--27 project lens, with the 11-point scoring guide and a model script. The presentation prompt is a practice prompt written for this set, not the official 2027 project prompt. Listening sources are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 15 minutes to prepare and deliver the presentation.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Presentation: \blank\ / 11 \qquad Target: 16+ MCQ and 8+ presentation",
        short="Unit 3", sub="Art and Creativity")

Q.sec("Listening: Audio and Chart")
Q.src(r"Listening 1 \textperiodcentered\ Audio and Chart (transcript) \textperiodcentered\ A campus radio report", [
    "这里是校园之声。上个月，学生会对全校八百名学生做了一个调查，问大家平时最常用什么方式听音乐。",
    "结果显示，用手机音乐软件听歌的同学最多，占百分之六十二。其次是看短视频的时候听音乐，占百分之二十一。去音乐会或者演唱会现场听的同学只占百分之五。",
    "有意思的是，虽然去现场的人很少，但是在回答“最难忘的音乐经历”这个问题时，超过一半的同学写的都是现场演出。一位高二的同学说：“在手机上听歌很方便，可是在现场跟几千个人一起唱，那种感觉是手机给不了的。”",
    "学生会表示，下学期打算每个月在学校礼堂办一场免费的学生音乐会，让更多同学有机会体验现场音乐。",
], 5, table=(["听音乐的方式", "百分比"], [["手机音乐软件", "62\\%"], ["短视频", "21\\%"], ["收音机或CD", "12\\%"], ["音乐会、演唱会现场", "5\\%"]]),
   note="Chart: How 800 students most often listen to music")
Q.q("1.A.2 Data", "According to the report and chart, which is the second most common way students listen to music?",
    "while watching short videos", [("music apps on their phones", "Apps are the most common (62%), not the second."),
                                   ("radio or CDs", "Radio and CDs are third (12%)."),
                                   ("live concerts", "Live concerts are last (5%).")],
    "其次是看短视频 (21%).", "其次 means “next, second.” The chart confirms: 62%, then 21%.",
    ["其次 → second place."])
Q.q("1.A.2 Data", "About how many of the 800 students listen mainly at live performances?",
    "40", [("5", "5 is the percentage, not the number of students."),
           ("400", "400 would be half the students."),
           ("168", "168 is 21% of 800, the short-video group.")],
    "5% of 800 = 40.", "Convert the percentage to a number: 800 × 0.05 = 40.",
    ["百分之五 × 800 = 40."])
Q.q("1.C.1 Connect", "What contrast does the report draw?",
    "Few students attend live music, but many find it the most memorable.", [("Students prefer radios to phones.", "Phones are far more popular than radios."),
                                                                            ("Students dislike short videos but use them often.", "No dislike is mentioned."),
                                                                            ("Live concerts are cheaper than apps.", "Cost is not compared.")],
    "虽然去现场的人很少，但是……超过一半……写的都是现场演出.", "虽然……但是 sets the low number (5%) against the high share of memorable experiences (over half).",
    ["Find 虽然……但是 and connect it to the chart."])
Q.q("1.B.5 Word meaning", r"When the student says 那种感觉是手机给不了的, she means",
    "a phone cannot give you that feeling", [("phones are not allowed at concerts", "Nothing about rules."),
                                            ("she lost her phone at a concert", "No phone was lost."),
                                            ("phones give a better feeling than concerts", "给不了 means cannot give: the opposite.")],
    "V + 不了 = cannot.", "给不了 is a potential complement: the phone is unable to give that feeling.",
    ["不了 after a verb = unable to."])
Q.q("1.C.2 Conclusion", "What does the student council plan to do, and why?",
    "hold free monthly concerts so more students can experience live music", [("ban phones in class to encourage concerts", "Nothing about banning phones."),
                                                                             ("sell concert tickets to raise money", "The concerts will be free."),
                                                                             ("make a music app for the school", "No app is planned.")],
    "每个月……办一场免费的学生音乐会，让更多同学有机会体验现场音乐.", "The plan responds to the survey: live music is memorable but rarely experienced.",
    ["学生会表示 introduces the plan; 让…… gives the purpose."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ From an arts magazine", [
    "\\textbf{年轻人回到了剧场}",
    "很长一段时间，人们都认为传统戏曲是“爷爷奶奶的艺术”。但是，最近几年，情况发生了变化。",
    "以某市大剧院为例，戏曲演出的观众中，三十岁以下的年轻人所占的比例从2019年的百分之十二上升到了2024年的百分之三十五。",
    "剧院经理认为，原因主要有两个。一是短视频平台上出现了很多戏曲演员，他们用年轻人喜欢的方式介绍戏曲，比如化妆过程、服装的故事。二是剧院推出了“新编戏”，把传统的唱腔和现代的灯光、舞台设计结合在一起，故事也更贴近现代生活。",
    "也有老观众担心，太多的改变会让戏曲失去原来的味道。对此，一位老演员说：“戏曲本来就是在变化中传下来的。只要唱腔的根还在，就不怕变。”",
], 5, table=(["年份", "2019", "2020", "2021", "2022", "2023", "2024"], [["30岁以下观众比例", "12\\%", "10\\%", "17\\%", "23\\%", "29\\%", "35\\%"]]),
   note="Chart: Share of opera audience members under 30 at a city theater (fictional data)")
Q.q("1.B.1 Main idea", "What is the main idea of the article?",
    "Traditional opera is attracting more young audience members.", [("Traditional opera is only for the elderly.", "The article says that view is changing."),
                                                                      ("Theaters should stop staging new works.", "The article reports on new works; it does not argue for stopping them."),
                                                                      ("Short videos are replacing live theater.", "Short videos bring young people to the theater.")],
    "Title + 情况发生了变化.", "The title and the data both point to young people returning to the theater.",
    ["Read the title and the sentence after 但是."])
Q.q("1.A.2 Trend", "What does the chart show?",
    "The share of young audience members dipped in 2020 and then rose every year.", [("The share rose steadily every year from 2019.", "2020 (10%) is lower than 2019 (12%)."),
                                                                                    ("The share fell from 35% to 12%.", "The direction is reversed: from 12% to 35%."),
                                                                                    ("The share stayed about the same.", "It nearly tripled.")],
    "12 → 10 → 17 → 23 → 29 → 35.", "Read every column: one dip in 2020, then a steady rise.",
    ["Check each year, not just the first and last."])
Q.q("1.A.1 Detail", "Which is one reason the manager gives?",
    "New productions combine traditional singing with modern stage design.", [("Tickets became free for students.", "Ticket prices are not mentioned."),
                                                                              ("Schools require students to attend.", "No requirement is mentioned."),
                                                                              ("Older audiences stopped coming.", "Older audiences are still there; some worry about changes.")],
    "二是……把传统的唱腔和现代的灯光、舞台设计结合在一起.", "The manager gives two reasons, marked 一是 and 二是.",
    ["一是…… 二是……"])
Q.q("1.B.3 Point of view", "What is the older performer's view of the changes?",
    "Change is acceptable as long as the core singing style remains.", [("All changes should be stopped.", "He says 不怕变: change is not to be feared."),
                                                                        ("Opera should copy pop music entirely.", "He insists the root of the singing style must remain."),
                                                                        ("Young people will never understand opera.", "He says nothing about young people's understanding.")],
    "只要唱腔的根还在，就不怕变.", "只要……就 sets a condition: if the root of the singing style remains, change is fine.",
    ["只要 (as long as) → the condition."])
Q.q("1.B.5 Word meaning", r"In this article, 根 most likely means",
    "the essential foundation", [("the root of a plant", "The literal meaning; here it is figurative."),
                                 ("the theater's building", "No building is meant."),
                                 ("a famous song", "根 is not a title.")],
    "唱腔的根 = the root (core) of the singing style.", "The performer uses 根 figuratively: what the art grows from and cannot lose.",
    ["Literal → figurative in context."])

Q.sec("Reading: Correspondence")
Q.src(r"Reading 2 \textperiodcentered\ Correspondence \textperiodcentered\ An email", [
    "主题：欢迎加入青少年民乐团！",
    "林同学：",
    "你好！谢谢你报名参加我们的青少年民乐团。看了你的报名表，我们知道你学过五年钢琴，但是没有学过民族乐器。别担心，乐团里很多团员也是从零开始的。",
    "根据你的情况，我们建议你先学扬琴。扬琴和钢琴一样，也是用两只手敲出声音，很多学过钢琴的人学得特别快。",
    "乐团每周六上午九点在文化中心排练。新团员需要先上四次基础课，然后才能参加正式排练。乐器可以向乐团借，但是要交两百元押金，还乐器的时候退还。",
    "今年十二月，乐团会在新年音乐会上演出《春节序曲》。如果你努力练习，说不定也能上台呢！",
    "如果有任何问题，欢迎回信。",
    "周老师",
], 5)
Q.q("1.B.1 Purpose", "What is the main purpose of the email?",
    "to welcome a new member and explain how to get started", [("to reject an application", "The subject line says 欢迎加入: welcome to join."),
                                                             ("to sell a yangqin", "Instruments can be borrowed; nothing is sold."),
                                                             ("to invite parents to a meeting", "No meeting is announced.")],
    "欢迎加入 + steps.", "The subject line and content welcome Lin and explain instrument choice, schedule and rules.",
    ["Subject line + structure."])
Q.q("1.C.3 Inference", "Why does the teacher recommend the yangqin?",
    "Its two-handed striking technique is similar to the piano.", [("It is the cheapest instrument to buy.", "Cost of buying is not discussed."),
                                                                   ("The orchestra needs no other instruments.", "Nothing says other instruments are not needed."),
                                                                   ("Lin has already played it for five years.", "Lin played piano, not yangqin.")],
    "扬琴和钢琴一样，也是用两只手敲出声音.", "The teacher links Lin's piano background to an instrument played in a similar way.",
    ["根据你的情况 → the reason follows."])
Q.q("1.A.1 Detail", "What must a new member do before joining regular rehearsals?",
    "take four basic lessons", [("pass a performance test", "No test is required."),
                                ("buy an instrument", "Instruments can be borrowed."),
                                ("perform at the New Year concert", "That comes later, if Lin practices hard.")],
    "先上四次基础课，然后才能参加正式排练.", "先……然后才 states the order: four basic lessons first.",
    ["先……然后才……"])
Q.q("1.A.1 Detail", "What does the email say about borrowing an instrument?",
    "A 200-yuan deposit is required and returned later.", [("Borrowing is free with no conditions.", "A deposit is required."),
                                                           ("Only experienced members may borrow.", "Any member may borrow."),
                                                           ("The deposit is not refunded.", "It is returned when the instrument is returned (退还).")],
    "要交两百元押金，还乐器的时候退还.", "押金 is a deposit; 退还 means it is given back.",
    ["押金 + 退还."])
Q.q("1.B.3 Tone", "What is the tone of the email?",
    "warm and encouraging", [("strict and discouraging", "别担心 and 说不定也能上台呢 are reassuring."),
                             ("formal and indifferent", "The writer engages with Lin's situation personally."),
                             ("apologetic", "There is nothing to apologize for.")],
    "别担心…… 说不定也能上台呢！", "Reassurance (别担心) and encouragement (说不定……呢) set a warm tone.",
    ["Look at 别担心 and the sentence ending 呢！"])

Q.sec("Listening: Conversation")
Q.src(r"Listening 2 \textperiodcentered\ Conversation (transcript) \textperiodcentered\ Two friends leave a museum", [
    "女：你觉得今天的展览怎么样？",
    "男：说实话，我本来以为就是一些旧瓷器，没想到这么有意思。特别是那个用手机扫一扫，瓷器上的画就会动起来的部分。",
    "女：是啊，我也最喜欢那个。不过我觉得最感人的是最后那个房间，展出的是一位老师傅修了四十年文物的工具。",
    "男：我没注意，我在那个房间里一直在看纪念品。你看，我买了一个青花瓷图案的手机壳。",
    "女：哈哈，你啊！其实那些工具旁边有一段话，说修文物最重要的不是技术，而是耐心。我觉得这句话对学什么都有用。",
    "男：嗯，有道理。下次你再来，叫上我，我好好看看那个房间。",
], 5)
Q.q("1.B.3 Attitude", "What was the man's attitude toward the exhibition before he saw it?",
    "He expected it to be dull.", [("He expected it to be exciting.", "以为就是一些旧瓷器 shows low expectations."),
                                   ("He had seen it many times before.", "本来以为 shows he had not seen it."),
                                   ("He did not want to buy anything.", "He bought a phone case.")],
    "本来以为……没想到…….", "本来以为 marks a mistaken earlier belief; 没想到 introduces the surprise.",
    ["本来以为 + 就是……: low expectations."])
Q.q("1.A.1 Detail", "What did both speakers like?",
    "the interactive section where porcelain pictures move on a phone", [("the gift shop", "Only the man spent time there."),
                                                                       ("the old craftsman's tools", "The woman found them moving; the man did not notice them."),
                                                                       ("a lecture by a curator", "No lecture is mentioned.")],
    "我也最喜欢那个.", "也 shows that the woman shares the man's favorite: the scan-and-animate porcelain.",
    ["也 = also → shared."])
Q.q("1.A.1 Detail", "What did the man do in the last room?",
    "He looked at souvenirs.", [("He studied the craftsman's tools.", "He says 我没注意: he did not notice them."),
                                ("He talked to the craftsman.", "The craftsman is not present."),
                                ("He took photos of the tools.", "No photos are mentioned.")],
    "我在那个房间里一直在看纪念品.", "一直在 shows he spent the whole time looking at souvenirs.",
    ["Listen to the man's reply to the last room."])
Q.q("1.C.2 Conclusion", "What lesson does the woman draw from the exhibition?",
    "Patience matters more than technique, in anything one learns.", [("Technology will replace craftsmen.", "She stresses a human quality, patience."),
                                                                      ("Souvenirs are a waste of money.", "She teases the man but draws no such lesson."),
                                                                      ("Old porcelain should be sold.", "Nothing about selling.")],
    "最重要的不是技术，而是耐心.", "不是……而是 states the lesson; she adds 对学什么都有用.",
    ["不是 A 而是 B → B is the point."])
Q.q("1.C.3 Inference", "What will the man probably do next time?",
    "go back with the woman to see the last room properly", [("skip the museum", "He asks her to take him next time."),
                                                            ("buy more phone cases", "He wants to see the room this time."),
                                                            ("visit a different museum alone", "He wants to go with her (叫上我).")],
    "下次你再来，叫上我，我好好看看那个房间.", "He asks to be included and plans to look carefully (好好看看).",
    ["Final line → next action."])

Q.frq(kind="Project Presentation", head=r"Question 1 \textperiodcentered\ Project Presentation (practice prompt) \textperiodcentered\ 11 points \textperiodcentered\ 3 minutes to prepare, 3 to present",
      mins=6,
      directions=[r"\textbf{Directions.} Deliver a 3-minute presentation in Chinese. Explain at least three factors, with relevant details and specific examples from research. Organize the presentation logically, use a variety of vocabulary and grammar and culturally relevant expressions, and speak clearly at an appropriate pace. You may use a keyword outline of no more than about 50 words, as practice for the PPR.",
                  r"\textbf{Practice prompt} (not the official 2027 prompt):以一种在华语社区里常见的音乐活动为例，说明音乐怎样反映这个社区的文化观念。"],
      ask="Say your presentation aloud (time it: 3 minutes), then write your keyword outline and the key sentences you used.",
      lines=8,
      model=["大家好！我的研究题目是“广场舞音乐和中国的社区生活”。我想从三个方面来介绍：音乐本身、跳舞的方式，以及它背后的文化观念。",
             "第一个方面是音乐。广场舞的音乐一般节奏比较快，很多是流行歌曲或者改编过的民歌，用一个小音箱就能放。根据我研究的资料，很多社区的舞队会一起选歌，有的舞队还会自己编舞。也就是说，音乐不只是背景，而是大家一起创造的东西。",
             "第二个方面是跳舞的方式，也就是一种社区习俗。在很多城市，每天傍晚，退休的阿姨、叔叔们会来到小区的广场，一跳就是一个小时。他们不需要报名，也不用花钱，谁来都欢迎。我采访过一位邻居奶奶，她说，自从退休以后，广场舞成了她每天最期待的事。",
             "第三个方面，也是最重要的，是文化观念。广场舞反映了重视集体、喜欢热闹的观念。在中国，很多老人觉得，跟大家一起活动比一个人在家更健康、更开心。这跟“远亲不如近邻”的想法也有关系：邻居们通过跳舞成了朋友，互相照顾。当然，也有人觉得广场舞的音乐太吵，所以现在很多社区规定了跳舞的时间和音量。",
             "跟美国相比，美国的老人更常去健身房或者自己散步，活动比较个人化。而广场舞把运动、音乐和社交结合了起来。",
             "总而言之，广场舞的音乐虽然简单，却体现了中国社区重视集体生活和邻里关系的文化。谢谢大家！"],
      rows=[("Task execution", 2, "Three factors (the music, the practice, the perspective), each explained with specific detail from research (shared song choice, daily evening practice, an interview).", "Naming three factors but explaining only one; relying only on general knowledge."),
            ("Cultural understanding", 2, "Shows how a perspective (valuing collective life and neighbors) explains the practice and the product, with a comparison.", "Describing square dancing without explaining why people do it."),
            ("Organization", 2, "Opening with a roadmap; 第一/第二/第三个方面; 也就是说, 当然, 跟……相比, 总而言之.", "No roadmap; ideas in random order."),
            ("Language control", 3, "Varied structures (不只是……而是, 自从……以后, 一……就, 虽然……却, 把……结合起来) and culturally relevant expressions (远亲不如近邻, 热闹, 邻里关系).", "Basic structures only; errors that block meaning."),
            ("Delivery", 2, "About 3 minutes at a natural pace, with clear tones and intonation that stresses the key words.", "Reading word for word; long pauses; rushing to fit.")],
      tips=[r"The script runs about three minutes at a relaxed pace. It acknowledges a counterpoint (noise rules) without losing its thread, which shows depth. On the exam, replace “根据我研究的资料” with your real sources from the project packet, named briefly."])

GUIDE, QSET = G, Q
