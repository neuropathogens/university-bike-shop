from ap_wl.model import Doc

STEM = "03-art-creativity"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 3: Art and Creativity", r"Unit 3 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 3 asks how art and creativity shape daily life, how art reflects and challenges cultural perspectives, and how communities value and pass on their arts. Its recommended contexts are architecture, artistic heritage, beauty and aesthetics, fashion and design, literature, and the visual and performing arts. The course project for the May 2027 exam uses music as its lens, so this guide gives music its own section (Japanese instruments, folk songs and Bon dances, enka, J-pop and Vocaloid, school choirs and bands, taiko) and ends with a Project Presentation kit. It also covers architecture and gardens, kabuki, ukiyo-e and manga, the aesthetic ideas most often linked to Japanese art (wabi-sabi, ma, kintsugi), and the language for describing and evaluating art. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 11+ \qquad Three factors for my project: \blank[10em]",
        short="Unit 3", sub="Art and Creativity")

G.sec("Music in Japanese-speaking communities")
G.tex(r"""
\begin{vocab}
和楽器（わがっき） & traditional Japanese instruments & taught in middle-school music classes \\
三味線（しゃみせん） & three-stringed plucked lute & \\
尺八（しゃくはち） / 箏（こと） & bamboo flute / 13-string zither & \\
和太鼓（わだいこ） & Japanese drums & ensemble drumming (組太鼓) since the 1950s \\
民謡（みんよう） / 盆踊り & folk song / Bon dance & \\
演歌（えんか） & enka, sentimental ballads & \\
合唱コンクール & class choral contest & a school tradition \\
吹奏楽部（すいそうがくぶ） & school concert band club & \\
ボーカロイド（ボカロ） & singing voice synthesizer & Hatsune Miku, 2007 \\
\end{vocab}

\begin{compare}{Tradition}{Where and when}{What it often expresses}
民謡 and 盆踊り & summer festivals in every region & community, ancestors, local identity \\
演歌 & from the postwar era & nostalgia, endurance, longing for home \\
合唱コンクール & middle and high schools, every autumn & working together as a class; harmony \\
J-POP, anime songs, Vocaloid & from the 1990s; worldwide through the internet & creativity, fan participation \\
沖縄の三線とエイサー & Okinawa & a distinct Ryukyuan identity \\
\end{compare}

\begin{keyidea}[Products, practices, perspectives in music]
\textbf{Product}: a shamisen, an anime song, a Vocaloid track. \textbf{Practice}: dancing in a circle at a Bon festival; a class practicing every morning for the choral contest. \textbf{Perspective}: the value behind it (harmony in the group, welcoming ancestors, effort and perseverance). The presentation's culture row asks for the link: これは～という考え方の表れです.
\end{keyidea}
""")
G.q("1 Music", r"Which instrument is a three-stringed, plucked lute?",
    "三味線", [("尺八", "尺八 is a bamboo flute."),
              ("箏", "箏 is a 13-string zither played lying flat."),
              ("和太鼓", "和太鼓 are drums.")],
    "三 = three: 三味線.", "The shamisen has three strings and is played with a large plectrum (ばち).",
    ["三味線 → three strings."])
G.q("1 Music", r"Every autumn, each class in a Japanese middle school practices a song for weeks before the choral contest (合唱コンクール). Which perspective does this practice most directly reflect?",
    "Achieving harmony through the whole group's effort.", [("Only the best singers should perform.", "Every student in the class sings."),
                                                            ("Music is a private hobby.", "It is a group activity."),
                                                            ("Competition between individuals matters most.", "Classes compete as groups.")],
    "Choral contest ↔ group harmony and effort.", "A school practice linked to a perspective: the class succeeds together.",
    ["whole class + weeks of practice → harmony and effort."])
G.q("1 Music", r"What is 初音ミク (Hatsune Miku)?",
    "a character for a singing voice synthesizer, released in 2007", [("an enka singer from the 1960s", "No."),
                                                                      ("a traditional folk song", "No."),
                                                                      ("a type of drum", "No.")],
    "Vocaloid, 2007.", "Users compose songs that the software sings; fans worldwide share and remix them.",
    ["ボーカロイド → 初音ミク."])

G.sec("Architecture, gardens and heritage")
G.tex(r"""
\begin{vocab}
世界遺産（せかいいさん） & World Heritage & \\
寺（てら） / 神社（じんじゃ） & Buddhist temple / Shinto shrine & \\
城（しろ） & castle & \\
枯山水（かれさんすい） & dry landscape garden & stones and raked gravel, e.g., Ryōanji \\
式年遷宮（しきねんせんぐう） & periodic rebuilding of a shrine & Ise Jingū, every 20 years \\
\end{vocab}

\begin{compare}{Place}{What it is}{Why it matters}
法隆寺 & temple in Nara, founded in the early 600s & among the oldest wooden buildings in the world \\
姫路城 & 17th-century castle, the ``White Heron Castle'' & one of Japan's first World Heritage sites (1993) \\
伊勢神宮 & Shinto shrine rebuilt every 20 years & renewal; carpenters pass on their skills to the next generation \\
龍安寺の石庭 & a dry garden of fifteen stones & simplicity and contemplation \\
\end{compare}
""")
G.q("2 Heritage", r"Ise Jingū's main buildings are rebuilt in the same form every 20 years. Which perspective does this practice most directly reflect?",
    "Renewal keeps a tradition alive and passes skills on to the next generation.", [("Old buildings have no value.", "The form is carefully preserved."),
                                                                                    ("Shrines should become museums.", "No."),
                                                                                    ("Wood is a cheap material.", "Not the point.")],
    "Rebuilding ↔ continuity through renewal.", "Rebuilding (practice) means each generation of craftsmen learns the techniques (perspective: tradition lives through renewal).",
    ["式年遷宮 → 20 years → skills passed on."])
G.q("2 Heritage", r"What is a 枯山水 garden?",
    "a garden of stones and raked gravel with no water", [("a garden full of cherry trees", "No."),
                                                         ("a vegetable garden", "No."),
                                                         ("a garden with a large pond and fish", "枯 means dry: there is no water.")],
    "枯 (dry) + 山水 (landscape).", "Gravel stands for water; stones for islands or mountains.",
    ["枯山水 → dry landscape."])

G.sec("Traditional arts, pop culture and aesthetics")
G.tex(r"""
\begin{compare}{Art or idea}{What it is}{Perspective often cited}
歌舞伎 & stage drama with music, dance and elaborate makeup; UNESCO intangible heritage & passing on forms from master to student \\
浮世絵 & woodblock prints such as Hokusai's \emph{Great Wave} (around 1831) & influenced European painters (Japonisme) \\
茶道 & the way of tea & hospitality (おもてなし); 一期一会, every meeting happens only once \\
マンガ・アニメ & comics and animation, read and watched worldwide & creativity; stories for every age \\
わび・さび & beauty in simplicity, age and imperfection & \\
間（ま） & meaningful space or pause & in music, gardens, conversation \\
金継ぎ & repairing broken pottery with lacquer and gold & the history of an object is part of its beauty \\
\end{compare}
""")
G.q("3 Aesthetics", r"金継ぎ repairs a broken bowl with gold lacquer, making the cracks visible. Which perspective does it express?",
    "An object's history and imperfections can be part of its beauty.", [("Broken objects should be thrown away.", "The bowl is kept and repaired."),
                                                                         ("Only new objects are beautiful.", "The opposite."),
                                                                         ("Gold is more valuable than pottery.", "Not the point.")],
    "金継ぎ ↔ わび・さび.", "Instead of hiding damage, kintsugi highlights it as part of the object's story.",
    ["visible gold cracks → beauty in imperfection."])
G.q("3 Aesthetics", r"In the tea ceremony, 一期一会 means",
    "treasure each meeting, because it will never happen in the same way again", [("drink tea once a day", "No."),
                                                                                  ("meet the same people every week", "The opposite."),
                                                                                  ("one cup for each guest", "No.")],
    "一期 (one lifetime) 一会 (one meeting).", "The host prepares each gathering as a unique occasion.",
    ["一期一会 → once in a lifetime."])
G.q("3 Arts", r"Which art form influenced European painters such as Van Gogh in the 19th century?",
    "浮世絵", [("歌舞伎", "Kabuki is theater."),
              ("茶道", "The tea ceremony is not a visual art form that traveled this way."),
              ("ボーカロイド", "21st-century software.")],
    "Ukiyo-e → Japonisme.", "Japanese woodblock prints reached Europe in the 19th century and inspired Japonisme.",
    ["浮世絵 → Van Gogh."])

G.sec("Describing and evaluating art")
G.tex(r"""
\begin{compare}{Purpose}{Language}{Example}
Describe & ～が描かれている、～を表している & 大きな波と小さな富士山が描かれています。 \\
Interpret & ～を感じさせる、～を象徴している & 白い色は清らかさを象徴しています。 \\
Evaluate & ～が印象的だ、一番心を動かされたのは～ & 一番印象的だったのは、太鼓の音の迫力です。 \\
Influence & ～に影響を与えた / ～に影響を受けた & 浮世絵はヨーロッパの画家に影響を与えました。 \\
Report & ～と言われている & 法隆寺は世界最古の木造建築の一つと言われています。 \\
\end{compare}

\begin{trap}
The direction of influence depends on the verb: X が Y に影響を\textbf{与えた} (X influenced Y); X が Y に影響を\textbf{受けた} (X was influenced by Y).
\end{trap}
""")
G.q("4 Describing", r"Choose the sentence that means ``Van Gogh was influenced by ukiyo-e.''",
    "ゴッホは浮世絵に影響を受けました。", [("ゴッホは浮世絵に影響を与えました。", "This means Van Gogh influenced ukiyo-e."),
                                         ("浮世絵はゴッホに影響を受けました。", "This means ukiyo-e was influenced by Van Gogh."),
                                         ("ゴッホは浮世絵を影響しました。", "影響 needs を与える or を受ける, not a bare verb.")],
    "受けた = received the influence.", "X に影響を受ける: be influenced by X.",
    ["ゴッホ (receiver) + 浮世絵に (from) + 影響を受けました."])
G.q("4 Describing", r"Which sentence reports a widely held claim without stating it as your own fact?",
    "法隆寺は世界最古の木造建築の一つだと言われています。", [("法隆寺は世界最古の木造建築の一つです。", "States it as a fact on your own authority."),
                                                            ("法隆寺は世界最古の木造建築の一つかもしれない。", "Plain style and uncertain; not a report."),
                                                            ("法隆寺は世界最古の木造建築の一つでしょうか。", "A question.")],
    "～と言われている.", "～と言われています reports what is commonly said.",
    ["と言われています → it is said."])

G.sec("Task kit: the Project Presentation")
G.tex(r"""
You have 3 minutes to prepare (with your PPR) and 3 minutes to present: at a natural pace, about 900--1,000 characters. The rubric rewards \textbf{three or more factors, each explained with details from research}, and a cultural perspective linked to a product or practice.

\begin{compare}{Move}{Phrases}{}
Open & 私の研究テーマは「～」です。三つの点から説明します。 & \\
Move on & まず / 次に / 最後に & \\
Evidence & ～によると、～ / ～の資料では、～ / ～にインタビューしたところ、～ & \\
Perspective & これは～という考え方の表れだと思います。 / ～を大切にしていることがわかります。 & \\
Compare & アメリカと比べると、～ / 私の町でも～ & \\
Close & 以上のことから、～と言えます。これで発表を終わります。ありがとうございました。 & \\
\end{compare}

\begin{trap}
Use です・ます style throughout the presentation. Three factors named with no detail earn only 1 point for task; budget about 45 seconds for each factor so the third gets real detail.
\end{trap}
""")
G.q("5 Presentation", r"A presentation explains three factors, each with a specific example from research, but never links them to what people value. Which row is it most likely to lose points in?",
    "Cultural understanding", [("Task execution", "Three factors with relevant details earn full task credit."),
                               ("Delivery", "Delivery is about pronunciation and pace."),
                               ("Organization", "Nothing suggests poor organization.")],
    "No perspective link → culture row.", "Row B's top score needs a relationship between a perspective and a product or practice.",
    ["Factors and details → task OK.", "No perspective → culture 1 point."])
G.q("5 Presentation", r"Which sentence links a practice to a perspective?",
    "太鼓のグループでは、全員が先生や太鼓に礼をしてから練習を始めます。これは、道具や先生を大切にする考え方の表れだと思います。", [("太鼓はとても大きい楽器です。", "A product described with no perspective."),
                                                                                                                                  ("私は太鼓の音が好きです。", "A personal preference."),
                                                                                                                                  ("太鼓のグループはたくさんあります。", "A fact with no perspective.")],
    "Practice + これは～考え方の表れ.", "The practice (bowing before practice) is tied to the value behind it (respect for teachers and tools).",
    ["礼をしてから → 大切にする考え方."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 3: Art and Creativity: Question Set", r"Unit 3 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Audio and Chart and a Conversation for listening, an Article and Chart and a Correspondence for reading) on the music people listen to, a class choral contest, Japanese instruments in school and a taiko club's welcome email, followed by a practice Project Presentation on music, the 2026--27 project lens, with the 11-point scoring guide and a model script. The presentation prompt is a practice prompt written for this set, not the official 2027 project prompt. Questions are in English, as on the exam; listening sources are printed as transcripts. All sources and data are original and fictional. Allow about 25 minutes for the multiple choice and 6 minutes to prepare and deliver the presentation.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Presentation: \blank\ / 11 \qquad Target: 15+ MCQ and 8+ presentation",
        short="Unit 3", sub="Art and Creativity")

Q.sec("Listening: Audio and Chart")
Q.src(r"Listening 1 \textperiodcentered\ Audio and Chart (transcript) \textperiodcentered\ ラジオ「どんな音楽を聞いていますか」", [
    r"（アナウンサー）全国の千五百人に、一番よく聞く音楽のジャンルを聞きました。十代と二十代では、J-POPとアニメソングが人気です。特にアニメソングは、十代の三人に一人が「一番よく聞く」と答えました。",
    r"（アナウンサー）六十代以上では演歌が一番多くなっています。でも、おもしろいことに、演歌を聞く十代も少しずつ増えているそうです。動画サイトで、昔の歌手の映像を見る若者が多いからだと言われています。",
    r"（アナウンサー）音楽の聞き方は変わっても、いい歌は世代を超えて伝わっていくようです。",
], 5, table=(["ジャンル", "10--20代", "30--50代", "60代以上"], [["J-POP", "41\\%", "44\\%", "20\\%"], ["アニメソング", "33\\%", "12\\%", "3\\%"], ["演歌", "4\\%", "11\\%", "52\\%"], ["洋楽", "22\\%", "33\\%", "25\\%"]]),
      note="一番よく聞く音楽（架空のデータ）")
Q.q("1.A.2 Data", "According to the chart, which genre is most popular among people aged 60 and over?",
    "enka", [("J-pop", "20%."),
             ("Western music", "25%."),
             ("anime songs", "3%.")],
    "演歌 52%.", "Data (1.A.2): read the 60+ column.",
    ["60代以上: 52 > 25 > 20 > 3."])
Q.q("1.C.1 Connect", r"Which chart figure matches the announcer's statement that one in three teenagers listens most to anime songs?",
    "33% for anime songs among people in their teens and twenties", [("41% for J-pop among teens and twenties", "That is J-pop."),
                                                                     ("12% for anime songs among people aged 30 to 50", "Wrong age group."),
                                                                     ("33% for Western music among people aged 30 to 50", "Right number, wrong genre and age group.")],
    "三人に一人 ≈ 33%.", "Connect (1.C.1): match the description to the right row and column.",
    ["アニメソング × 10–20代 = 33%."])
Q.q("1.B.5 Word meaning", r"In the report, 世代を超えて most likely means",
    "across generations", [("faster than before", "No."),
                           ("in foreign countries", "No."),
                           ("only among young people", "The opposite.")],
    "超える = go beyond.", "Word meaning (1.B.5): 世代 (generation) + を超えて (beyond).",
    ["いい歌は世代を超えて伝わっていく."])
Q.q("1.C.3 Inference", "Why are more teenagers listening to enka, according to the report?",
    "They watch videos of older singers on video sites.", [("Schools require it.", "Not stated."),
                                                           ("Their grandparents force them.", "Not stated."),
                                                           ("Enka concerts are free.", "Not stated.")],
    "動画サイト.", "Detail/inference: the reason given with と言われています.",
    ["動画サイトで、昔の歌手の映像を見る若者が多い."])
Q.q("1.B.1 Main idea", "What is the main point of the announcer's conclusion?",
    "Good songs are passed on across generations even as listening habits change.", [("Young people no longer listen to music.", "No."),
                                                                                      ("Enka will soon disappear.", "The opposite trend is mentioned."),
                                                                                      ("Anime songs are the best genre.", "Not stated.")],
    "聞き方は変わっても… 伝わっていく.", "Main idea (1.B.1).",
    ["変わっても … 世代を超えて伝わっていく."])

Q.sec("Listening: Conversation")
Q.src(r"Listening 2 \textperiodcentered\ Conversation (transcript) \textperiodcentered\ 合唱コンクールの練習", [
    r"（女）ねえ、合唱コンクールまであと二週間だよ。今日も放課後、練習するよね？",
    r"（男）えー、今日はサッカー部の練習があるんだけど……。",
    r"（女）でも、男子の声がまだ小さいって、先生も言ってたよ。みんなでそろわないと、いい合唱にならないよ。",
    r"（男）わかってるよ。じゃあ、朝の練習を増やすのはどう？　部活の人も来られるし。",
    r"（女）いいね！　明日から、朝七時半に音楽室に集まろう。私がクラスのみんなに連絡するね。",
    r"（男）ありがとう。去年は三位だったから、今年は絶対優勝したいな。",
], 5)
Q.q("1.A.1 Detail", "How long is it until the choral contest?",
    "two weeks", [("two days", "No."),
                  ("one month", "No."),
                  ("one year", "Last year is mentioned only for the result.")],
    "あと二週間.", "Detail (1.A.1).",
    ["合唱コンクールまであと二週間だよ."])
Q.q("1.A.1 Detail", "Why can't the boy practice after school today?",
    "He has soccer club practice.", [("He has a part-time job.", "Not mentioned."),
                                     ("He is sick.", "Not mentioned."),
                                     ("The music room is closed.", "Not mentioned.")],
    "サッカー部の練習.", "Detail (1.A.1).",
    ["今日はサッカー部の練習があるんだけど."])
Q.q("1.B.3 Point of view", "What problem does the girl mention?",
    "The boys' voices are still too quiet.", [("The song is too difficult.", "Not mentioned."),
                                              ("The teacher is absent.", "No."),
                                              ("The class has no piano player.", "No.")],
    "男子の声がまだ小さい.", "Point of view (1.B.3): she cites the teacher's comment.",
    ["男子の声がまだ小さいって、先生も言ってた."])
Q.q("1.C.2 Conclusion", "What do they decide?",
    "to hold extra morning practices so club members can join", [("to cancel soccer practice", "No."),
                                                                 ("to practice only on weekends", "No."),
                                                                 ("to ask the teacher to change the song", "No.")],
    "朝の練習を増やす.", "Conclusions (1.C.2): his proposal and her agreement (いいね！).",
    ["朝の練習を増やすのはどう？ … 明日から、朝七時半に."])
Q.q("1.C.3 Inference", "What does the conversation suggest about the class?",
    "Students care about singing well together as a group.", [("Only a few students take the contest seriously.", "Both want to practice more."),
                                                              ("The class won first place last year.", "They were third."),
                                                              ("The contest is optional.", "Not implied.")],
    "みんなでそろわないと / 優勝したい.", "Inference (1.C.3): the group effort is the point.",
    ["みんなでそろわないと、いい合唱にならない."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ 「学校で和楽器を学ぶ」", [
    r"日本の中学校では、音楽の授業で和楽器を学ぶことになっている。しかし、楽器が高かったり、教えられる先生が少なかったりして、実際には箏や太鼓を一度も触ったことがない生徒も多い。",
    r"そこで、ある市では、地域の演奏家が学校に来て教える「和楽器出前授業」を始めた。生徒たちは、三味線のばちの持ち方や、太鼓の正しい立ち方を、プロから直接習うことができる。",
    r"参加した中学二年生は「和楽器は古くてつまらないと思っていたけど、太鼓を打ったら体中に音が響いて、すごくかっこよかった」と話している。",
], 5, table=(["楽器", "出前授業の前", "出前授業の後"], [["箏", "18\\%", "70\\%"], ["和太鼓", "35\\%", "81\\%"], ["三味線", "6\\%", "40\\%"], ["尺八", "3\\%", "12\\%"]]),
      note="その楽器を演奏したことがある生徒の割合（架空のデータ）")
Q.q("1.A.2 Data", "According to the chart, which instrument had the largest share of students who had played it after the program?",
    "Japanese drums", [("koto", "70%."),
                       ("shamisen", "40%."),
                       ("shakuhachi", "12%.")],
    "和太鼓 81%.", "Data (1.A.2): read the after column.",
    ["81 > 70 > 40 > 12."])
Q.q("1.A.2 Data", "For which instrument did the share of students who had played it rise the most?",
    "koto", [("Japanese drums", "35 → 81 is a rise of 46 points; koto rose 52 (18 → 70)."),
             ("shamisen", "6 → 40: a rise of 34 points."),
             ("shakuhachi", "3 → 12: a rise of 9 points.")],
    "Compare the differences.", "Data (1.A.2).",
    ["箏 +52, 和太鼓 +46, 三味線 +34, 尺八 +9."])
Q.q("1.B.1 Purpose", "Why did the city start the visiting-musician program?",
    "Many students had never touched a Japanese instrument because of cost and a lack of teachers.", [("Students asked for more pop music.", "No."),
                                                                                                     ("Professional musicians had no other work.", "No."),
                                                                                                     ("The national curriculum stopped including instruments.", "The curriculum requires them.")],
    "高い / 先生が少ない → 出前授業.", "Purpose (1.B.1): problem → solution.",
    ["楽器が高かったり、教えられる先生が少なかったりして…そこで…"])
Q.q("1.B.5 Word meaning", r"In the article, 出前授業 most likely means",
    "a lesson delivered at the school by visitors from outside", [("a cooking class", "出前 usually means food delivery; here it is used figuratively."),
                                                                 ("an online lesson", "The musicians come in person."),
                                                                 ("a lesson held at a concert hall", "They come to the school.")],
    "出前 = delivery.", "Word meaning (1.B.5): like food delivery, the lesson comes to the students.",
    ["地域の演奏家が学校に来て教える."])
Q.q("1.C.3 Inference", "What does the student's comment show?",
    "Hands-on experience changed his image of Japanese instruments.", [("He already loved traditional music.", "He thought it was old and boring."),
                                                                       ("He found the drums too loud.", "He found them cool."),
                                                                       ("He wants to quit music class.", "No.")],
    "つまらない → かっこよかった.", "Inference (1.C.3): the contrast marked by けど.",
    ["古くてつまらないと思っていたけど … かっこよかった."])

Q.sec("Reading: Correspondence")
Q.src(r"Reading 2 \textperiodcentered\ Correspondence \textperiodcentered\ 太鼓クラブからのメール", [
    r"リサさん、「みなと太鼓クラブ」への入会、ありがとうございます！　代表の木村です。",
    r"練習は毎週水曜日の夜七時から九時まで、市民センターの体育館で行います。動きやすい服と、タオル、飲み物を持ってきてください。ばちはクラブのものを貸しますので、買わなくても大丈夫です。",
    r"うちのクラブには、小学生から七十代まで、いろいろな人がいます。練習の前と後には、みんなで太鼓に礼をします。また、ほかの人が打っているときは、大きな声で掛け声をかけて応援します。最初は恥ずかしいかもしれませんが、すぐに慣れますよ。",
    r"十月の市民祭りでは、新しいメンバーも一曲いっしょに演奏する予定です。わからないことがあったら、いつでも聞いてください。　木村",
], 5)
Q.q("1.A.1 Detail", "What does Lisa NOT need to buy?",
    "drumsticks", [("comfortable clothes", "She should bring them."),
                   ("a towel", "She should bring one."),
                   ("a drink", "She should bring one.")],
    "ばちは貸します.", "Detail (1.A.1).",
    ["ばちはクラブのものを貸しますので、買わなくても大丈夫です."])
Q.q("1.B.2 Audience", "Who is the email written to?",
    "a new member of the taiko club", [("the club's teacher", "Kimura is the leader writing to Lisa."),
                                       ("a city official", "No."),
                                       ("a festival audience", "No.")],
    "入会、ありがとうございます.", "Audience (1.B.2).",
    ["リサさん、… 入会、ありがとうございます."])
Q.q("1.A.1 Detail", "What do members do before and after practice?",
    "They bow to the drums together.", [("They clean the gym floor.", "Not mentioned."),
                                        ("They sing a club song.", "Not mentioned."),
                                        ("They drink tea with the leader.", "Not mentioned.")],
    "太鼓に礼をします.", "Detail (1.A.1).",
    ["練習の前と後には、みんなで太鼓に礼をします."])
Q.q("1.C.3 Inference", r"What does the custom of shouting 掛け声 for other drummers suggest about the club?",
    "Members support one another as a group.", [("Members compete to be the loudest.", "The shouts are encouragement."),
                                                 ("The club practices in silence.", "The opposite."),
                                                 ("Only experienced members may shout.", "Not stated.")],
    "応援 = support.", "Inference (1.C.3).",
    ["大きな声で掛け声をかけて応援します."])
Q.q("1.C.2 Conclusion", "What can Lisa expect in October?",
    "She will perform one piece with the club at the city festival.", [("She will take a test to stay in the club.", "No."),
                                                                       ("She will teach elementary students.", "No."),
                                                                       ("She will buy her own drum.", "No.")],
    "市民祭りで一曲.", "Conclusions (1.C.2).",
    ["新しいメンバーも一曲いっしょに演奏する予定です."])

Q.frq(kind="Project Presentation", head=r"Question 1 \textperiodcentered\ Project Presentation (practice prompt) \textperiodcentered\ 11 points \textperiodcentered\ 3 minutes to prepare, 3 to present",
      mins=6,
      directions=[r"\textbf{Directions.} Deliver a 3-minute presentation in Japanese. Explain at least three factors, with relevant details and specific examples from research. Organize the presentation logically, use a variety of vocabulary and grammar and culturally relevant expressions, and speak clearly at an appropriate pace.",
                  r"\textbf{Practice prompt} (not the official 2027 prompt): 日本語を話すコミュニティでよく見られる音楽の活動を一つ例にして、その音楽がコミュニティのどんな考え方を表しているか説明してください。"],
      ask="Say your presentation aloud (time it: 3 minutes), then write your keyword outline and the key sentences you used.",
      lines=8,
      model=["みなさん、こんにちは。私の研究テーマは「和太鼓とグループの考え方」です。三つの点から説明します。楽器そのもの、太鼓グループの習慣、そしてアメリカの日系人と太鼓の関係です。",
             "まず、楽器です。和太鼓は、昔から村のお祭りや盆踊りで使われてきました。大きな太鼓は一本の木をくりぬいて作られ、皮は牛の皮です。資料によると、今のように何人もで一緒に打つ「組太鼓」のスタイルは、一九五〇年代に生まれたそうです。つまり、古い楽器を使った新しい音楽なのです。",
             "次に、太鼓グループの習慣です。私は地元の太鼓グループにインタビューしました。メンバーは練習の前と後に、先生と太鼓に礼をします。また、ほかの人が打っているときは、大きな声で掛け声をかけて応援します。メンバーの一人は「一人がうまくても、みんなの音がそろわなければ意味がない」と言っていました。これは、個人よりもグループの和を大切にする考え方の表れだと思います。",
             "最後に、アメリカの日系人と太鼓の関係です。一九六八年にサンフランシスコで太鼓の道場ができてから、アメリカ各地に太鼓グループが生まれました。日系人のお祭りでは、太鼓が日系人としてのアイデンティティを表すものになっています。日本と比べると、アメリカの太鼓グループには日系人以外のメンバーも多く、太鼓が文化をつなぐ役割を果たしていると言えます。",
             "以上のことから、和太鼓は、和を大切にする日本の考え方を表すと同時に、海を越えて新しいコミュニティを作ってきた音楽だと言えます。これで発表を終わります。ありがとうございました。"],
      rows=[("Task execution", 2, "Three factors (the instrument, the group's customs, taiko among Japanese Americans), each explained with specific detail from research (1950s ensemble style, an interview, the 1968 dojo).", "Naming three factors but explaining only one; relying only on general knowledge."),
            ("Cultural understanding", 2, "Shows how a perspective (valuing group harmony, identity) explains the practices (bowing, shouting encouragement, festival performance), with a comparison.", "Describing taiko without explaining why people practice it this way."),
            ("Organization", 2, "Opening with a roadmap; まず / 次に / 最後に; つまり, また, 以上のことから.", "No roadmap; ideas in random order."),
            ("Language control", 3, "Varied structures (passive 作られ / 使われてきました, hearsay ～そうです, ～なければ, ～と言えます, noun modification) in consistent です・ます style.", "Mixing plain and polite style; basic structures only."),
            ("Delivery", 2, "Clear pronunciation, natural pace and intonation, little hesitation.", "Hesitant, monotone or rushed speech.")],
      tips=[r"Each factor has a researched detail (the 1950s ensemble style, the interview quotation, the 1968 dojo) and a perspective (これは～の表れだと思います). The comparison with Japanese American groups doubles as cultural understanding and a strong third factor. About 950 characters: three minutes at a natural pace."])

GUIDE, QSET = G, Q
