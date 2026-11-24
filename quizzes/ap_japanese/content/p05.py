from ap_wl.model import Doc

STEM = "05-contemporary-life"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 5: Contemporary Life", r"Unit 5 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 5 asks how traditions shape daily life today: school and work, food and health, leisure and pop culture. Its recommended contexts are education and career, entertainment and media, food and health, pop culture, sports and leisure, and travel and tourism. This guide gives the vocabulary of daily life and the practices most often tested (the April school year, club activities, students cleaning their classrooms, school lunch, entrance exams and cram school, job hunting, washoku and itadakimasu, hot-spring manners, Kōshien and karaoke), the structures for narrating events in time, and a second Story Narration kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Practices I can link to a perspective: \blank[8em]",
        short="Unit 5", sub="Contemporary Life")

G.sec("School life")
G.tex(r"""
\begin{vocab}
入学式（にゅうがくしき） & entrance ceremony & the school year starts in April \\
部活（ぶかつ） & school club activities & sports, music, art; often daily \\
掃除の時間 & cleaning time & students clean their own classrooms \\
給食（きゅうしょく） & school lunch & served by students, eaten in the classroom \\
受験（じゅけん） / 塾（じゅく） & entrance exams / cram school & \\
修学旅行（しゅうがくりょこう） & school trip & often to Kyoto, Nara or Hiroshima \\
文化祭 / 体育祭 & culture festival / sports day & \\
先輩（せんぱい） / 後輩（こうはい） & senior / junior student & \\
\end{vocab}

\textbf{Practices and perspectives.} In most Japanese schools there are no janitors for the classrooms: after lunch, students sweep, wipe and tidy their own rooms. At lunch, students in white coats serve their classmates. These practices reflect a perspective that school teaches responsibility for shared spaces and for each other, not only academic subjects.
""")
G.q("1 School", r"When does the Japanese school year begin?",
    "in April", [("in September", "That is common in the U.S. and Europe."),
                 ("in January", "No."),
                 ("in June", "No.")],
    "April: 入学式 under the cherry blossoms.", "The school and fiscal year in Japan begins in April.",
    ["入学式 → April."])
G.q("1 School", r"Japanese students clean their own classrooms every day. Which perspective does this practice most directly reflect?",
    "Everyone shares responsibility for the spaces they use.", [("Schools cannot afford janitors.", "Cost is not the perspective the practice is linked to."),
                                                               ("Cleaning is a punishment.", "It is a daily routine for all."),
                                                               ("Only teachers should be responsible for school.", "The opposite.")],
    "掃除の時間 ↔ shared responsibility.", "Practice (students cleaning) linked to a perspective (responsibility, respect for shared spaces).",
    ["掃除 → 自分たちで使う場所は自分たちできれいに."])
G.q("1 School", r"What is a 先輩?",
    "a student in a higher grade, or a more senior colleague", [("a younger student", "That is 後輩."),
                                                               ("a teacher", "Teachers are 先生."),
                                                               ("a classmate of the same age", "That is 同級生.")],
    "先 (ahead) + 輩 (fellow).", "Seniority shapes language: juniors often use polite forms to their 先輩.",
    ["先輩 ↔ 後輩."])

G.sec("Work and career")
G.tex(r"""
\begin{vocab}
就職活動（就活） & job hunting & students in dark ``recruit suits'' \\
新卒一括採用 & hiring new graduates all at once & most start work on April 1 \\
終身雇用（しゅうしんこよう） & lifetime employment & less common than before \\
転職（てんしょく） & changing jobs & increasingly common \\
働き方改革 & work-style reform & limits on overtime since 2019 \\
アルバイト（バイト） & part-time job & \\
\end{vocab}

\textbf{Change.} For decades many Japanese joined one company after graduation and stayed until retirement. Today more people change jobs, work remotely or start companies, and the law limits overtime. Questions about work often ask how these changes affect family time and well-being.
""")
G.q("2 Work", r"What does 就活 refer to?",
    "university students' job hunting", [("a part-time job", "That is バイト."),
                                         ("changing jobs mid-career", "That is 転職."),
                                         ("retirement", "No.")],
    "就職活動 → 就活.", "Final-year students apply, attend information sessions and interviews.",
    ["就職 (getting a job) + 活動 (activity)."])
G.q("2 Work", r"Many companies hire new graduates all at once to start work on April 1 (新卒一括採用). What does this practice suggest?",
    "Companies traditionally train employees themselves after hiring them young.", [("Graduates must already be experts.", "The system assumes training on the job."),
                                                                                    ("Hiring happens randomly all year.", "It is concentrated in one season."),
                                                                                    ("Companies prefer older workers.", "The opposite.")],
    "Hire young, train inside.", "Bulk hiring of graduates fits a perspective that the company shapes its own employees.",
    ["一括 (all at once) + 新卒 (new graduates)."])

G.sec("Food and health")
G.tex(r"""
\begin{vocab}
和食（わしょく） & traditional Japanese food culture & UNESCO intangible heritage, 2013 \\
一汁三菜（いちじゅうさんさい） & one soup, three side dishes & the classic balanced meal \\
いただきます / ごちそうさま & said before / after eating & \\
弁当（べんとう） / キャラ弁 & boxed lunch / lunch decorated as characters & \\
長寿（ちょうじゅ） & long life & life expectancy among the world's highest \\
ラジオ体操 & radio calisthenics & broadcast since 1928 \\
温泉（おんせん） & hot spring & wash before entering; no swimsuits \\
\end{vocab}

\textbf{Words at the table.} いただきます literally means ``I humbly receive.'' Many people explain it as thanks to everyone who produced and prepared the food, and to the plants and animals themselves. The perspective: gratitude and not wasting food (もったいない).
""")
G.q("3 Food", r"Which perspective is most often given for saying いただきます before a meal?",
    "Gratitude to the people and living things that provided the food.", [("A request for second helpings.", "No."),
                                                                          ("A way to call the waiter.", "No."),
                                                                          ("A wish for good weather.", "No.")],
    "いただく = humbly receive.", "The phrase expresses thanks for the food and those who made it possible.",
    ["いただきます → thanks."])
G.q("3 Food", r"Which is the correct manner at an 温泉?",
    "Wash your body before getting into the bath.", [("Wear a swimsuit in the bath.", "Swimsuits are not worn in traditional hot springs."),
                                                     ("Put your towel in the water.", "Towels stay out of the water."),
                                                     ("Swim laps.", "No.")],
    "Wash first; towel out of the water.", "Hot-spring manners keep the shared bath clean for everyone.",
    ["かけ湯・体を洗う → then enter."])

G.sec("Leisure, sports and pop culture")
G.tex(r"""
\begin{vocab}
甲子園（こうしえん） & national high-school baseball tournament & since 1915; watched by the whole country \\
カラオケ & karaoke & from Japan, 1970s \\
ゴールデンウィーク & Golden Week & a cluster of holidays in late April and early May \\
推し（おし） / 推し活 & one's favorite (idol, character) / supporting them & \\
コスプレ & costume play & \\
\end{vocab}

\textbf{Kōshien.} Every summer, high-school teams from every prefecture play at Kōshien Stadium. Players who lose often scoop up a little of the stadium's dirt to take home. The practice reflects a perspective that effort and team spirit matter as much as winning.
""")
G.q("4 Leisure", r"What is 甲子園 best known for?",
    "the national high-school baseball tournament", [("a professional soccer league", "No."),
                                                    ("a karaoke contest", "No."),
                                                    ("a sumo tournament", "No.")],
    "甲子園 → high-school baseball.", "The summer tournament at Kōshien Stadium dates from 1915 and is a national event.",
    ["甲子園 → 高校野球."])
G.q("4 Leisure", r"A fan says 私の推しは、このアニメのキャラクターです。What does 推し mean here?",
    "her favorite, the one she supports", [("her enemy", "No."),
                                           ("her teacher", "No."),
                                           ("her younger sister", "No.")],
    "推す = to push, recommend.", "推し is the person or character one supports most; 推し活 is the activity of supporting them.",
    ["推し → favorite."])

G.sec("Task kit: narrating events in time")
G.tex(r"""
\begin{compare}{Structure}{Use}{Example}
V-ようとしたら & just as I tried to & 家を出ようとしたら、雨が降ってきました。 \\
V-るところ / V-たところ & about to / just did & 今、出かけるところです。ちょうど着いたところです。 \\
V-ている間に & while & 私が準備している間に、友だちが手伝ってくれました。 \\
V-てしまう & ended up, unfortunately & ケーキが全部売り切れてしまいました。 \\
～ことにする & decide & みんなで写真を撮ることにしました。 \\
\end{compare}

\begin{trap}
In a Story Narration, keep the main narration in the past (～ました or ～た). Use the present only inside dialogue or for something still true now.
\end{trap}
""")
G.q("5 Story", r"Choose the form that means ``I have just arrived at the station.'' 今、ちょうど駅に着いた\blank です。",
    "ところ", [("ように", "ように means “so that” or “like.”"),
               ("ために", "ために means “in order to” or “because of.”"),
               ("ながら", "ながら means “while doing” and cannot end the sentence this way.")],
    "V-たところ = have just done.", "V-たところだ marks the moment right after an action; V-るところだ, the moment just before.",
    ["着いたところです → I've just arrived."])
G.q("5 Story", r"Which sentence keeps the narration in a consistent style?",
    "ケーキがなくなってしまいました。みんなは困りました。", [("ケーキがなくなってしまいました。みんなは困る。", "The second sentence switches to plain present."),
                                                          ("ケーキがなくなっちゃった。みんなは困りました。", "The first sentence is casual, the second polite."),
                                                          ("ケーキがなくなります。みんなは困った。", "Tense and style both change.")],
    "One tense, one style.", "Consistent past-tense です・ます narration avoids language control penalties.",
    ["しまいました … 困りました → consistent."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 5: Contemporary Life: Question Set", r"Unit 5 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (a Conversation and a Presentation for listening, an Article and Chart and a Promotional Material for reading) on choosing between a club and cram school, how high-school students spend their afternoons, a hot-spring inn and the history of school lunch, followed by a Story Narration (8 points) with a scoring guide and a model story. Questions are in English, as on the exam; listening sources are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 15 minutes for the story.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Story: \blank\ / 8 \qquad Target: 15+ MCQ and 6+ story",
        short="Unit 5", sub="Contemporary Life")

Q.sec("Listening: Conversation")
Q.src(r"Listening 1 \textperiodcentered\ Conversation (transcript) \textperiodcentered\ 部活か、塾か", [
    r"（男）先輩、相談があるんですけど……。来年受験なので、母に「バスケ部をやめて、塾に行きなさい」って言われたんです。",
    r"（女）そっか。でも、たくみ君はバスケが好きでしょう？",
    r"（男）はい。チームのみんなと練習するのが一番楽しいんです。でも、成績が下がってきたのも本当で……。",
    r"（女）私も去年、同じことで悩んだよ。結局、部活は夏の大会まで続けて、そのあと塾に通ったの。部活で体力がついたから、受験勉強もがんばれたと思う。",
    r"（男）なるほど。じゃあ、母にもそう話してみます。夏までは部活を続けて、毎日一時間は家で勉強するって約束します。",
], 5)
Q.q("1.A.1 Detail", "What did the boy's mother tell him to do?",
    "quit the basketball club and go to cram school", [("practice basketball more", "No."),
                                                     ("get a part-time job", "No."),
                                                     ("change schools", "No.")],
    "バスケ部をやめて、塾に行きなさい.", "Detail (1.A.1): the passive 言われた reports what his mother said.",
    ["母に…って言われたんです."])
Q.q("1.B.3 Point of view", "What is the boy's attitude toward the basketball club?",
    "He enjoys practicing with the team most of all.", [("He wants to quit because it is boring.", "No."),
                                                        ("He thinks the team is too weak.", "Not stated."),
                                                        ("He only plays for his mother.", "No.")],
    "一番楽しい.", "Point of view (1.B.3).",
    ["チームのみんなと練習するのが一番楽しいんです."])
Q.q("1.A.1 Detail", "What did the senior student do last year?",
    "She stayed in her club until the summer tournament, then went to cram school.", [("She quit her club immediately.", "No."),
                                                                                      ("She never went to cram school.", "She did, after summer."),
                                                                                      ("She changed clubs.", "No.")],
    "夏の大会まで続けて、そのあと塾.", "Detail (1.A.1).",
    ["部活は夏の大会まで続けて、そのあと塾に通った."])
Q.q("1.C.3 Inference", "Why does the senior think the club helped her studying?",
    "The club built her stamina, which helped her keep up exam study.", [("Club members taught her math.", "Not stated."),
                                                                         ("The club gave her free time.", "No."),
                                                                         ("Her coach wrote her a recommendation.", "Not stated.")],
    "体力がついた.", "Inference (1.C.3).",
    ["部活で体力がついたから、受験勉強もがんばれた."])
Q.q("1.C.2 Conclusion", "What will the boy probably do next?",
    "propose to his mother that he continue the club until summer and study at home every day", [("quit the club tomorrow", "No."),
                                                                                                ("ask the senior to talk to his mother", "He will talk himself."),
                                                                                                ("skip the summer tournament", "No.")],
    "母にもそう話してみます.", "Conclusions (1.C.2): his plan at the end.",
    ["夏までは部活を続けて、毎日一時間は家で勉強するって約束します."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ 「高校生の放課後」", [
    r"放課後、高校生はどのように過ごしているのだろうか。ある調査によると、一年生では部活に一番多くの時間を使っているが、三年生になると塾や家での勉強の時間が大きく増える。",
    r"一方で、アルバイトをする高校生もいる。「自分で働いたお金で、好きなバンドのコンサートに行きたい」と話す二年生もいた。",
    r"教育の専門家は、「どの過ごし方にも意味があります。大切なのは、自分で選んで、時間をうまく使うことです」と話している。",
], 5, table=(["過ごし方", "1年生", "3年生"], [["部活", "1日 2.1時間", "1日 0.6時間"], ["塾", "1日 0.4時間", "1日 1.5時間"], ["家での勉強", "1日 0.8時間", "1日 2.0時間"], ["アルバイト", "1日 0.3時間", "1日 0.2時間"]]),
      note="平日の平均（架空のデータ）")
Q.q("1.A.2 Data", "According to the chart, how much time do first-year students spend on club activities per weekday?",
    "2.1 hours", [("0.6 hours", "That is third-year students."),
                  ("0.8 hours", "That is home study for first-years."),
                  ("1.5 hours", "That is cram school for third-years.")],
    "1年生 部活 2.1.", "Data (1.A.2).",
    ["部活 × 1年生 = 2.1時間."])
Q.q("1.C.1 Connect", "Which data support the article's statement that third-year students study much more?",
    "Cram school rises from 0.4 to 1.5 hours and home study from 0.8 to 2.0 hours.", [("Club activities fall from 2.1 to 0.6 hours.", "True, but that is about clubs, not study."),
                                                                                      ("Part-time work falls from 0.3 to 0.2 hours.", "Not about study."),
                                                                                      ("Home study stays at 0.8 hours.", "It rises to 2.0.")],
    "塾 + 家での勉強 both rise.", "Connect (1.C.1).",
    ["塾 0.4 → 1.5; 家 0.8 → 2.0."])
Q.q("1.C.3 Inference", "Why does the second-year student work part time?",
    "to pay for concerts of a band she likes with her own money", [("to support her family", "Not stated."),
                                                                  ("to pay cram-school fees", "Not stated."),
                                                                  ("because her school requires it", "No.")],
    "自分で働いたお金で.", "Detail/inference.",
    ["自分で働いたお金で、好きなバンドのコンサートに行きたい."])
Q.q("1.B.3 Point of view", "What is the education expert's view?",
    "Each way of spending time has value if students choose for themselves and use time well.", [("Students should quit clubs in third year.", "Not stated."),
                                                                                                  ("Part-time jobs are harmful.", "No."),
                                                                                                  ("Cram school is the only useful choice.", "No.")],
    "自分で選んで、時間をうまく使う.", "Point of view (1.B.3).",
    ["どの過ごし方にも意味があります."])
Q.q("1.B.4 Organization", r"What is the function of 一方で in the second paragraph?",
    "It introduces another group of students who spend time differently.", [("It summarizes the article.", "No."),
                                                                            ("It gives an example of cram school.", "No."),
                                                                            ("It disagrees with the survey.", "No.")],
    "一方で = meanwhile, on the other hand.", "Organization (1.B.4).",
    ["clubs and study → 一方で → part-time work."])

Q.sec("Reading: Promotional Material")
Q.src(r"Reading 2 \textperiodcentered\ Promotional Material \textperiodcentered\ 温泉旅館のチラシ", [
    r"\textbf{山の湯旅館　〜森の中の小さな温泉〜}",
    r"駅から送迎バスで二十分。四季の山を見ながら、露天風呂でゆっくりお過ごしください。",
    r"\textbf{料金：}一泊二食付き　大人一人一万八千円、小学生一万円、未就学児無料。",
    r"\textbf{チェックイン：}午後三時から　\textbf{夕食：}午後六時または七時半（予約時にお選びください）。",
    r"\textbf{お願い：}お風呂に入る前に、体を洗ってからお入りください。タオルはお湯に入れないでください。",
    r"平日に三泊以上ご予約のお客様には、地元の野菜をプレゼントいたします。",
], 5)
Q.q("1.A.1 Detail", "How do guests get from the station to the inn?",
    "by the inn's shuttle bus", [("by taxi only", "Not mentioned."),
                                 ("on foot", "No."),
                                 ("by train", "No.")],
    "送迎バス.", "Detail (1.A.1).",
    ["駅から送迎バスで二十分."])
Q.q("1.C.2 Conclusion", "Two adults and one elementary-school child stay one night. How much do they pay in total?",
    "46,000 yen", [("36,000 yen", "That would be two adults only."),
                   ("54,000 yen", "That would be three adults."),
                   ("28,000 yen", "That would be one adult and one child.")],
    "18,000 × 2 + 10,000.", "Apply the details: adults 18,000 each, elementary students 10,000.",
    ["一万八千円 × 2 + 一万円 = 四万六千円."])
Q.q("1.A.1 Detail", "What must guests decide when they make a reservation?",
    "the time of dinner", [("the time of breakfast", "Not mentioned."),
                           ("the room number", "Not mentioned."),
                           ("the check-out time", "Not mentioned.")],
    "予約時にお選びください.", "Detail (1.A.1).",
    ["夕食：午後六時または七時半（予約時にお選びください）."])
Q.q("1.B.2 Audience", "Who receives local vegetables as a gift?",
    "guests who book three or more nights on weekdays", [("all guests", "Only some."),
                                                         ("children under six", "They stay free."),
                                                         ("guests who arrive by car", "No.")],
    "平日に三泊以上.", "Detail (1.A.1).",
    ["平日に三泊以上ご予約のお客様には…"])
Q.q("1.C.3 Inference", "What does the request about towels show?",
    "Guests are expected to keep the shared bath water clean.", [("Towels are very expensive.", "Not the reason."),
                                                                 ("The inn has no towels.", "No."),
                                                                 ("Guests must bring their own water.", "No.")],
    "Shared bath → keep clean.", "Inference (1.C.3).",
    ["タオルはお湯に入れないでください → clean shared water."])

Q.sec("Listening: Presentation")
Q.src(r"Listening 2 \textperiodcentered\ Presentation (transcript) \textperiodcentered\ 「給食の歴史」", [
    r"（先生）日本の給食は、一八八九年、山形県の小学校で始まったと言われています。家が貧しくて弁当を持ってこられない子どものために、おにぎりや焼き魚、漬物が出されたそうです。",
    r"（先生）戦争のあと、食べ物が足りなかった時代に、給食は全国に広がりました。多くの子どもにとって、給食は一日で一番大切な食事でした。",
    r"（先生）今の給食は、栄養のバランスを考えて作られています。地元でとれた野菜や魚を使う学校も多く、食べ物や地域について学ぶ「食育」の時間にもなっています。",
    r"（先生）給食の当番が配って、みんなで「いただきます」を言ってから食べる。この習慣も、給食が教えてくれる大切なことの一つです。",
], 5)
Q.q("1.A.1 Detail", "Why was school lunch first served in 1889?",
    "for children whose families were too poor to give them a lunch", [("to celebrate a festival", "No."),
                                                                     ("to teach cooking", "No."),
                                                                     ("because teachers had no time to eat", "No.")],
    "貧しくて弁当を持ってこられない.", "Detail (1.A.1).",
    ["家が貧しくて弁当を持ってこられない子どものために."])
Q.q("1.B.4 Organization", "How is the presentation organized?",
    "chronologically, from the first school lunch to today's practices", [("as a comparison of Japan and the U.S.", "No."),
                                                                         ("as a list of recipes", "No."),
                                                                         ("as an argument against school lunch", "No.")],
    "1889 → 戦争のあと → 今.", "Organization (1.B.4).",
    ["一八八九年 … 戦争のあと … 今の給食."])
Q.q("1.C.3 Inference", "Why was school lunch so important after the war?",
    "Food was scarce, so it was often children's most important meal.", [("Schools were closed.", "No."),
                                                                        ("Children did not like home cooking.", "No."),
                                                                        ("It was a new law for festivals.", "No.")],
    "食べ物が足りなかった.", "Inference (1.C.3).",
    ["給食は一日で一番大切な食事でした."])
Q.q("1.B.5 Word meaning", r"In the presentation, 食育 most likely means",
    "education about food, nutrition and where food comes from", [("a type of rice", "No."),
                                                                  ("a cooking contest", "No."),
                                                                  ("a school cafeteria building", "No.")],
    "食 (food) + 育 (raise, educate).", "Word meaning (1.B.5): explained in the same sentence.",
    ["食べ物や地域について学ぶ「食育」."])
Q.q("1.B.1 Main idea", "What point does the teacher make in the last paragraph?",
    "School lunch also teaches habits such as serving others and expressing thanks.", [("School lunch should be eaten quickly.", "No."),
                                                                                       ("Students should bring their own lunches.", "No."),
                                                                                       ("いただきます is no longer said.", "The opposite.")],
    "大切なことの一つ.", "Main idea (1.B.1).",
    ["当番が配って … いただきます → 習慣."])

Q.frq(kind="Story Narration", head=r"Question 3 \textperiodcentered\ Story Narration \textperiodcentered\ 8 points \textperiodcentered\ about 15 minutes",
      mins=15,
      directions=[r"\textbf{Directions.} The four pictures present a story. Imagine you are writing the story for a student magazine. Narrate a complete story as suggested by the pictures, in their order, with logical organization and relevant details."],
      panels=["文化祭の前の日、リナのクラスは教室でカフェの準備をしている。リナは看板の絵を描いている。",
              "文化祭の日、カフェにはお客さんがたくさん来て、教室の外まで長い列ができている。",
              "お昼ごろ、ケーキがなくなってしまい、リナとクラスメートが困った顔をしている。",
              "料理部の友だちがケーキを持ってきてくれる。最後に、クラス全員で記念写真を撮っている。"],
      model=[r"文化祭の前の日、リナさんのクラスは、教室をカフェにするために夜遅くまで準備をしました。絵が得意なリナさんは、入り口に飾る大きな看板を描くことになりました。「たくさんお客さんが来てくれるといいな」とリナさんは思いました。",
             r"文化祭の日、カフェはオープンしたとたん、お客さんでいっぱいになりました。教室の外の廊下まで長い列ができて、クラスのみんなは休む時間もないほど忙しかったです。",
             r"ところが、お昼ごろ、用意していたケーキが全部なくなってしまいました。まだ列に並んでいるお客さんがいるのに、出すものがありません。リナさんたちは、どうしたらいいかわからなくて、困ってしまいました。",
             r"そのとき、料理部のさきさんが「うちの部で作ったケーキ、よかったら使って！」と言って、ケーキを持ってきてくれました。おかげで、カフェは最後まで開けることができました。文化祭が終わったあと、さきさんも一緒に、クラス全員で記念写真を撮りました。リナさんは、みんなで力を合わせることの大切さを感じました。"],
      rows=[("Narrative development", 3, "All four pictures, in order, with details (the sign, the long line, the cakes running out, the cooking club's help, the photo) and dialogue.", "Leaving out the cooking club's help or the photo; describing pictures with no connection."),
            ("Organization", 2, "A clear beginning (preparation), middle (success, then the problem) and end (help and the photo); varied links: ～ために, ～たとたん, ところが, ～のに, そのとき, おかげで, ～たあと.", "Only そして; no ending."),
            ("Language control", 3, "Varied grammar (～ことになる, ～たとたん, ～ほど, ～てしまう, ～のに, ～てくれる, ～ことができる) and culturally relevant words (文化祭, 看板, 料理部, 記念写真, 力を合わせる) in consistent です・ます narration.", "Switching tense or style; basic vocabulary only.")],
      tips=[r"ところが and ～のに make picture 3 a real problem; ～てくれました and おかげで show the help and its result; 力を合わせる (work together) gives the story a culturally relevant lesson about the class as a team."])

GUIDE, QSET = G, Q
