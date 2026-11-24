from ap_wl.model import Doc

STEM = "06-global-contexts"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 6: Global Contexts", r"Unit 6 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 6 asks how global issues affect families and communities, and how people and governments respond. Its recommended contexts are global communication, the natural world, history, policy and planning, and transportation. This guide gives the vocabulary of disasters and preparedness, the environment (sorting garbage, mottainai, the plastic-bag charge), history and peace (the Meiji Restoration, Hiroshima, the paper cranes), global connections (exchange programs, tourism, migration) and the language for proposing solutions, and ends with a Project Q\&A kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Q\&A openings I can use: \blank[10em]",
        short="Unit 6", sub="Global Contexts")

G.sec("Disasters and preparedness")
G.tex(r"""
\begin{vocab}
地震（じしん） / 津波（つなみ） / 台風（たいふう） & earthquake / tsunami / typhoon & \\
防災（ぼうさい） & disaster prevention and preparedness & \\
避難訓練（ひなんくんれん） & evacuation drill & held several times a year at schools \\
防災の日 & Disaster Prevention Day, September 1 & remembering the 1923 Great Kantō Earthquake \\
非常持ち出し袋 & emergency go-bag & water, food, flashlight, radio \\
ハザードマップ & hazard map & shows flood and tsunami risk areas \\
東日本大震災 & Great East Japan Earthquake & March 11, 2011 \\
\end{vocab}

\textbf{Practices and perspectives.} Schools hold evacuation drills several times a year; many families keep a go-bag by the door, and towns publish hazard maps. The perspective: disasters cannot be prevented, but careful preparation in ordinary times (日ごろの備え) saves lives.
""")
G.q("1 Disasters", r"Why is September 1 Japan's Disaster Prevention Day?",
    "It marks the Great Kantō Earthquake of 1923.", [("It marks the 2011 earthquake.", "That was March 11."),
                                                     ("It is the start of typhoon season.", "Not the reason for the date."),
                                                     ("It is the first day of the school year.", "The school year starts in April.")],
    "9/1 → 1923 関東大震災.", "Disaster Prevention Day was established in 1960 on the anniversary of the 1923 earthquake.",
    ["防災の日 → 1923."])
G.q("1 Disasters", r"Japanese schools hold evacuation drills several times a year, even in years without a disaster. Which perspective does this practice reflect?",
    "Preparing in ordinary times saves lives when disaster comes.", [("Disasters can be completely prevented.", "Preparation reduces harm; it cannot prevent quakes."),
                                                                     ("Drills are mainly a way to miss class.", "No."),
                                                                     ("Only adults need to know what to do.", "Children practice too.")],
    "避難訓練 ↔ 日ごろの備え.", "A practice (regular drills) linked to a perspective (preparedness).",
    ["drills every year → be ready."])

G.sec("The environment")
G.tex(r"""
\begin{vocab}
ごみの分別（ぶんべつ） & sorting garbage & rules and collection days differ by city \\
燃えるごみ / 燃えないごみ / 資源ごみ & burnable / non-burnable / recyclable garbage & \\
3R（リデュース・リユース・リサイクル） & reduce, reuse, recycle & \\
もったいない & what a waste & a word taken up worldwide in 2005 by Wangari Maathai \\
レジ袋有料化 & charging for plastic shopping bags & nationwide since July 2020 \\
マイバッグ & reusable shopping bag & \\
\end{vocab}

\textbf{もったいない} expresses regret when something still useful is wasted: leftover food, a working machine thrown away, time used carelessly. Kenyan environmentalist Wangari Maathai, a Nobel Peace Prize winner, promoted the word internationally as a summary of the 3Rs plus respect for resources.
""")
G.q("2 Environment", r"Since when have shops across Japan charged for plastic shopping bags?",
    "July 2020", [("1964", "That is the first Tokyo Olympics."),
                  ("2011", "That is the Great East Japan Earthquake."),
                  ("2005", "That is when Wangari Maathai promoted もったいない.")],
    "レジ袋有料化 → 2020.", "The nationwide charge began in July 2020.",
    ["レジ袋 → 2020年7月."])
G.q("2 Environment", r"A grandmother says もったいない when her grandson throws away half a bowl of rice. What does she express?",
    "regret that something still useful is being wasted", [("joy at a good meal", "No."),
                                                         ("anger at the cook", "Not the meaning."),
                                                         ("a request for more rice", "No.")],
    "もったいない = what a waste.", "The word expresses respect for resources and regret at waste.",
    ["half a bowl thrown away → もったいない."])

G.sec("History and peace")
G.tex(r"""
\begin{compare}{Event or place}{When}{Why it matters}
明治維新 & 1868 & Japan modernizes rapidly and opens to the world \\
広島・長崎への原爆投下 & August 6 and 9, 1945 & cities destroyed; survivors (被爆者) became voices for peace \\
原爆ドーム & World Heritage since 1996 & left in ruins as a reminder \\
東京オリンピック & 1964 and 2021 & 1964 showed postwar recovery; the shinkansen opened just before \\
\end{compare}

\textbf{千羽鶴 (a thousand paper cranes).} Sadako Sasaki, who was exposed to radiation in Hiroshima at the age of two, folded paper cranes in the hospital hoping to recover. Today children from around the world send strings of cranes to the Children's Peace Monument in Hiroshima. The perspective: hope and the wish for peace, passed on through a small handmade object.
""")
G.q("3 History", r"What do strings of paper cranes sent to Hiroshima's Children's Peace Monument express?",
    "the wish for peace", [("congratulations on a wedding", "Cranes can mean long life, but here they mean peace."),
                           ("an apology for being late", "No."),
                           ("support for a sports team", "No.")],
    "千羽鶴 → peace.", "Inspired by Sadako Sasaki's story, the cranes have become a worldwide symbol of peace.",
    ["Sadako → cranes → peace."])
G.q("3 History", r"Which event in 1868 began Japan's rapid modernization?",
    "the Meiji Restoration", [("the first Tokyo Olympics", "1964."),
                              ("the opening of the shinkansen", "1964."),
                              ("the end of the Second World War", "1945.")],
    "1868 → 明治維新.", "The Meiji Restoration restored imperial rule and launched rapid modernization.",
    ["明治 → 1868."])

G.sec("Global connections and proposing solutions")
G.tex(r"""
\begin{vocab}
国際交流（こくさいこうりゅう） & international exchange & \\
JETプログラム & program bringing young foreigners to teach and work in Japan & since 1987 \\
訪日外国人 / インバウンド & foreign visitors to Japan & \\
観光公害 / オーバーツーリズム & overtourism & crowded buses and streets in popular cities \\
外国人住民 & foreign residents & \\
多文化共生（たぶんかきょうせい） & multicultural coexistence & \\
\end{vocab}

\begin{compare}{Purpose}{Structure}{Example}
Necessity & ～必要がある / ～なければならない & ルールを多言語で伝える必要があります。 \\
Recommendation & ～べきだ / ～たほうがいい & 観光客は地元のマナーを守るべきです。 \\
Purpose & ～ように / ～ために & 住民がバスに乗れるように、観光客用のバスを増やしました。 \\
Condition & ～ば / ～なら & 時間をずらせば、混雑は減ります。 \\
Proportion & ～ば～ほど & 観光客が増えれば増えるほど、ルールが大切になります。 \\
\end{compare}
""")
G.q("4 Global", r"What does 多文化共生 mean?",
    "people of different cultures living together in one community", [("traveling to many countries", "No."),
                                                                      ("learning many languages at school", "No."),
                                                                      ("exporting culture abroad", "No.")],
    "多文化 (many cultures) + 共生 (living together).", "The term describes policies that help foreign residents and Japanese neighbors live together.",
    ["共生 → coexistence."])
G.q("4 Solutions", r"Choose the form that fits: 住民がバスに乗れる\blank、観光客用のバスを増やしました。",
    "ように", [("ために", "ために of purpose needs a volitional verb; 乗れる is potential, so ように is used."),
               ("のに", "のに expresses contrast or regret."),
               ("ながら", "ながら means “while.”")],
    "Potential verb + ように = so that.", "With potential or non-volitional verbs, purpose is expressed with ように.",
    ["乗れる (can ride) + ように."])

G.sec("Task kit: the Project Q\\&A")
G.tex(r"""
The four recorded questions follow your presentation. You hear each twice and have 40 seconds to answer, about 150--200 characters at a natural pace. Questions usually ask which factor matters most, how the topic compares with your own community, what surprised you, and what may change in the future.

\begin{compare}{Question type}{Opening}{Then}
Most important & 一番大切だと思うのは～です。 & なぜなら～からです。 + one example \\
Compare & 私の町では～。日本と比べると～ & one similarity or difference, then why \\
Surprise & 一番意外だったのは、～ことです。 & what it taught you about the culture \\
Future & 十年後には、～と思います。 & a reason from your research \\
\end{compare}

\begin{keyidea}[The culture row in 40 seconds]
You need one answer with a cultural comparison \emph{or} a link between a perspective and a product or practice. Plan it before the exam: 太鼓のグループでは礼を大切にします。これは先生や道具を尊敬する考え方の表れです。私のバンドでは\ldots
\end{keyidea}
""")
G.q("5 Q&A", r"Which frame is best for a ``what surprised you'' question?",
    "一番意外だったのは、～ことです。", [("一番大切だと思うのは～です。", "That answers a “most important” question."),
                                       ("十年後には～と思います。", "That answers a question about the future."),
                                       ("私の町では～。", "That opens a comparison.")],
    "意外 = unexpected.", "Answer the question asked in the first sentence, then support it.",
    ["surprised → 意外だったのは."])
G.q("5 Q&A", r"A Q\&A prompt asks how taiko compares with music in your community. What does a strong answer need?",
    "a specific similarity or difference and what it shows about each culture", [("a summary of the whole presentation", "Repeating the presentation does not answer the question."),
                                                                                 ("a list of facts about taiko only", "The question asks for a comparison."),
                                                                                 ("a description of how you did the research", "The research process is not the topic.")],
    "Compare + explain.", "A cultural comparison that explains what each practice reflects can earn the top culture score.",
    ["Similarity/difference → why → perspective."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 6: Global Contexts: Question Set", r"Unit 6 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (a Presentation and an Audio and Chart for listening, an Article and a Literary Text for reading) on a school evacuation drill, reusable shopping bags, overtourism and a family that came to Japan from Brazil, followed by a practice Project Q\&A (9 points) with model answers. The Q\&A follows the practice presentation in the Unit 3 question set. Questions are in English, as on the exam; listening sources and Q\&A prompts are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 5 minutes for the Q\&A.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Q\&A: \blank\ / 9 \qquad Target: 15+ MCQ and 6+ Q\&A",
        short="Unit 6", sub="Global Contexts")

Q.sec("Listening: Presentation")
Q.src(r"Listening 1 \textperiodcentered\ Presentation (transcript) \textperiodcentered\ 先生の話「避難訓練の前に」", [
    r"（先生）明日は避難訓練です。地震が起きたという設定で、全校で校庭に避難します。",
    r"（先生）まず、揺れている間は、机の下に入って、机の脚をしっかり持ってください。揺れが止まったら、先生の指示を聞いて、ハンカチで口を押さえながら外に出ます。",
    r"（先生）避難するときの約束は「お・か・し・も」です。押さない、駆けない、しゃべらない、戻らない。忘れ物をしても、絶対に教室に戻ってはいけません。",
    r"（先生）訓練だからといって、ふざけないでください。本当の地震のときに体が自然に動くように、毎回真剣に練習することが大切なんです。",
], 5)
Q.q("1.A.1 Detail", "What should students do while the ground is shaking?",
    "get under their desks and hold the desk legs", [("run outside immediately", "They go out after the shaking stops."),
                                                     ("go back to get their bags", "Never go back."),
                                                     ("open the windows", "Not mentioned.")],
    "揺れている間は、机の下.", "Detail (1.A.1).",
    ["揺れている間は、机の下に入って、机の脚をしっかり持って."])
Q.q("1.B.5 Word meaning", r"What does the か in お・か・し・も stand for?",
    "don't run", [("don't push", "That is お (押さない)."),
                  ("don't talk", "That is し (しゃべらない)."),
                  ("don't go back", "That is も (戻らない).")],
    "か = 駆けない.", "Word meaning (1.B.5): each syllable starts one rule.",
    ["押さない・駆けない・しゃべらない・戻らない."])
Q.q("1.A.1 Detail", "What should students do if they forget something in the classroom?",
    "leave it and never return to the classroom", [("go back quickly", "絶対に…戻ってはいけません."),
                                                   ("ask a friend to get it", "Not stated."),
                                                   ("tell the teacher after lunch", "Not stated.")],
    "戻らない.", "Detail (1.A.1).",
    ["忘れ物をしても、絶対に教室に戻ってはいけません."])
Q.q("1.B.4 Organization", "How is the teacher's talk organized?",
    "an announcement, steps during the drill, a rule, then why the drill matters", [("a story about a past earthquake", "No narrative."),
                                                                                  ("a comparison of two schools", "No."),
                                                                                  ("a list of emergency foods", "No.")],
    "明日は… → まず… → 約束 → 大切なんです.", "Organization (1.B.4).",
    ["announcement → steps → rule → reason."])
Q.q("1.C.3 Inference", "Why does the teacher insist that students take the drill seriously?",
    "so they will act automatically in a real earthquake", [("because the principal will grade them", "Not stated."),
                                                            ("because the drill is dangerous", "Not the reason given."),
                                                            ("because visitors will watch", "Not stated.")],
    "体が自然に動くように.", "Inference (1.C.3): the purpose clause.",
    ["本当の地震のときに体が自然に動くように."])

Q.sec("Listening: Audio and Chart")
Q.src(r"Listening 2 \textperiodcentered\ Audio and Chart (transcript) \textperiodcentered\ ニュース「マイバッグは定着した？」", [
    r"（記者）二〇二〇年七月にレジ袋が有料になってから、マイバッグを持って買い物をする人が増えました。あるスーパーの調査では、レジ袋を断る人の割合は、有料化の前の年の三割から、一年後には七割を超えました。",
    r"（記者）その後も割合は少しずつ上がっていますが、コンビニでは、まだ袋を買う人が多いそうです。「急に買い物をするときは、バッグを持っていないことが多い」という声もあります。",
    r"（店長）数円でも、払うとなると考えますよね。小さなきっかけで、人の習慣は変わるんだと思います。",
], 5, table=(["年", "スーパー", "コンビニ"], [["2019年", "30\\%", "18\\%"], ["2021年", "74\\%", "45\\%"], ["2024年", "81\\%", "52\\%"]]),
      note="レジ袋を断った人の割合（架空のデータ）")
Q.q("1.A.2 Data", "According to the chart, what share of supermarket shoppers refused a plastic bag in 2021?",
    "74%", [("30%", "2019."),
            ("45%", "Convenience stores in 2021."),
            ("81%", "2024.")],
    "スーパー 2021 = 74%.", "Data (1.A.2).",
    ["スーパー × 2021年 = 74%."])
Q.q("1.C.1 Connect", "Which figure matches the report's statement that the share rose to more than 70% a year after the charge?",
    "74% at supermarkets in 2021", [("45% at convenience stores in 2021", "Below 70%."),
                                    ("81% at supermarkets in 2024", "Four years later, not one."),
                                    ("52% at convenience stores in 2024", "Below 70%.")],
    "一年後には七割を超えました ↔ 74%.", "Connect (1.C.1).",
    ["2020 charge → 2021: 74%."])
Q.q("1.C.3 Inference", "Why do more people still buy bags at convenience stores?",
    "They often shop there on impulse, without a bag.", [("Convenience-store bags are free.", "Not stated."),
                                                         ("Convenience stores sell only large items.", "No."),
                                                         ("The law does not apply to them.", "Not stated.")],
    "急に買い物をする.", "Inference (1.C.3).",
    ["急に買い物をするときは、バッグを持っていないことが多い."])
Q.q("1.B.3 Point of view", "What is the store manager's view?",
    "A small incentive can change people's habits.", [("The charge was too small to matter.", "He says even a few yen makes people think."),
                                                      ("Shoppers dislike reusable bags.", "No."),
                                                      ("Plastic bags should be free again.", "No.")],
    "小さなきっかけ.", "Point of view (1.B.3).",
    ["小さなきっかけで、人の習慣は変わる."])
Q.q("1.C.2 Conclusion", "Which conclusion do the report and chart together support?",
    "The charge changed habits, more at supermarkets than at convenience stores.", [("The charge had no effect.", "Shares rose sharply."),
                                                                                    ("Convenience-store shoppers refuse bags more often.", "The opposite."),
                                                                                    ("The share fell after 2021.", "It kept rising.")],
    "Supermarkets 81% vs. convenience stores 52%.", "Conclusions (1.C.2).",
    ["both rose; supermarkets higher."])

Q.sec("Reading: Article")
Q.src(r"Reading 1 \textperiodcentered\ Article \textperiodcentered\ 「観光客と住民の町」", [
    r"古い寺や町並みで有名なある町では、外国人観光客が増えて、町の経済は元気になった。しかし、住民の生活には困ったことも起きている。",
    r"一番の問題はバスだ。観光地へ行くバスが大きなスーツケースを持った観光客でいっぱいになり、病院や買い物に行くお年寄りが乗れないことがある。また、写真を撮るために私道に入る人もいる。",
    r"そこで町は、観光地へ行く人のための特別なバスを走らせ、住民が普通のバスに乗れるようにした。人気の場所には、多言語でマナーを説明する看板も立てた。",
    r"町の観光課の担当者は、「観光客を減らしたいわけではありません。住民も観光客も気持ちよく過ごせる町にしたいんです」と話している。",
], 5)
Q.q("1.B.1 Main idea", "What is the article mainly about?",
    "how a town is trying to balance tourism with residents' daily lives", [("how to plan a trip to an old temple", "No."),
                                                                           ("why tourists dislike buses", "No."),
                                                                           ("a town that has banned tourists", "The official says they do not want fewer tourists.")],
    "Balance tourism and residents.", "Main idea (1.B.1).",
    ["元気 vs. 困ったこと → measures → 両方."])
Q.q("1.A.1 Detail", "What is the biggest problem for residents?",
    "Buses are so full of tourists that older residents sometimes cannot board.", [("Tourists spend too little money.", "The economy improved."),
                                                                                  ("Temples are closing.", "No."),
                                                                                  ("There are no signs in Japanese.", "No.")],
    "一番の問題はバス.", "Detail (1.A.1).",
    ["お年寄りが乗れないことがある."])
Q.q("1.C.1 Connect", "How does the special bus address the problem described in the second paragraph?",
    "It separates tourists going to sights so residents can use regular buses.", [("It is free for tourists.", "Not stated."),
                                                                                  ("It runs only at night.", "Not stated."),
                                                                                  ("It replaces all regular buses.", "Regular buses remain.")],
    "住民が普通のバスに乗れるように.", "Connect (1.C.1): problem ↔ solution.",
    ["特別なバス → 住民が普通のバスに乗れる."])
Q.q("1.B.5 Word meaning", r"In the article, 私道 most likely means",
    "a private road", [("a famous temple", "No."),
                       ("a bus stop", "No."),
                       ("a souvenir shop", "No.")],
    "私 (private) + 道 (road).", "Word meaning (1.B.5): people enter it to take photos, causing problems.",
    ["写真を撮るために私道に入る → private road."])
Q.q("1.B.3 Point of view", "What does the tourism official want?",
    "a town where both residents and tourists can feel comfortable", [("fewer tourists", "She says that is not the goal."),
                                                                      ("more buses for tourists only", "Not her main point."),
                                                                      ("higher prices for residents", "No.")],
    "住民も観光客も.", "Point of view (1.B.3): わけではありません denies one goal; the next sentence gives the real one.",
    ["減らしたいわけではありません … 気持ちよく過ごせる町."])

Q.sec("Reading: Literary Text")
Q.src(r"Reading 2 \textperiodcentered\ Literary Text \textperiodcentered\ 「二つのことば」（エッセイ）", [
    r"私の祖母は、ブラジルで生まれた日系二世だ。曾祖父母は昔、日本から船でブラジルに渡った。祖母は一九九〇年代に、仕事を探して家族と日本に来た。",
    r"祖母の日本語は、少し古い。「ハイカラ」とか「ご無沙汰」とか、私の友だちが使わない言葉をよく使う。そして、怒るときと歌うときは、なぜかポルトガル語になる。",
    r"子どものころ、私は友だちの前で祖母がポルトガル語を話すのが恥ずかしかった。でも、去年ブラジルの親戚を訪ねたとき、私は自分のポルトガル語がほとんど通じないことに気がついた。祖母がどれだけ二つのことばの間で生きてきたのか、初めてわかった気がした。",
    r"今、私は祖母にポルトガル語を習っている。祖母は「遅いよ」と笑いながら、昔の歌を教えてくれる。",
], 5)
Q.q("1.A.1 Detail", "Why did the grandmother come to Japan?",
    "to find work, with her family, in the 1990s", [("to study at a university", "Not stated."),
                                                    ("to visit relatives for a summer", "She settled in Japan."),
                                                    ("because she was born in Japan", "She was born in Brazil.")],
    "仕事を探して.", "Detail (1.A.1).",
    ["一九九〇年代に、仕事を探して家族と日本に来た."])
Q.q("1.C.3 Inference", "Why does the grandmother's Japanese sound old-fashioned?",
    "She learned it from her parents' generation, who left Japan long ago.", [("She learned it from old movies only.", "Not stated."),
                                                                             ("She refuses to learn new words.", "Not stated."),
                                                                             ("She is joking with her friends.", "No.")],
    "日系二世 → parents' Japanese.", "Inference (1.C.3): the immigrants' Japanese kept older words.",
    ["曾祖父母は昔 … ブラジルに渡った → older Japanese."])
Q.q("1.B.3 Tone", "How did the narrator feel about her grandmother's Portuguese as a child?",
    "embarrassed", [("proud", "That came later."),
                    ("bored", "Not stated."),
                    ("afraid", "Not stated.")],
    "恥ずかしかった.", "Tone (1.B.3).",
    ["友だちの前で…恥ずかしかった."])
Q.q("1.C.2 Conclusion", "What changed the narrator's view?",
    "Visiting relatives in Brazil and finding she could hardly communicate in Portuguese.", [("Her friends started learning Portuguese.", "Not stated."),
                                                                                             ("Her grandmother moved back to Brazil.", "No."),
                                                                                             ("A teacher told her to study.", "No.")],
    "ブラジルの親戚を訪ねたとき.", "Conclusions (1.C.2): the turning point.",
    ["自分のポルトガル語がほとんど通じない → understood her grandmother."])
Q.q("1.B.1 Main idea", "What is the main idea of the essay?",
    "The narrator comes to value her grandmother's life between two languages and cultures.", [("Portuguese is easier than Japanese.", "Not the point."),
                                                                                               ("Immigrants should speak only Japanese.", "The opposite."),
                                                                                               ("Old words should be avoided.", "No.")],
    "二つのことばの間で生きてきた.", "Main idea (1.B.1).",
    ["恥ずかしかった → わかった → 習っている."])

Q.frq(kind="Project Q&A", head=r"Question 2 \textperiodcentered\ Project Q\&A (practice) \textperiodcentered\ 9 points \textperiodcentered\ 4 questions, 40 seconds each",
      mins=5,
      directions=[r"\textbf{Directions.} You will answer four questions about the practice presentation in the Unit 3 question set (和太鼓とグループの考え方). On the exam each question is heard twice and you have 40 seconds to respond. Respond as fully and appropriately as possible, and include at least one cultural comparison or one link between a perspective and a product or practice.",
                  "質問一：発表で説明した三つの点の中で、どれが一番大切だと思いますか。どうしてですか。",
                  "質問二：あなたの町では、みんなで一緒に演奏する音楽がありますか。和太鼓と比べてください。",
                  "質問三：研究の中で、一番意外だったことは何ですか。",
                  "質問四：十年後、和太鼓はどうなっていると思いますか。"],
      ask="Answer each question aloud in 40 seconds (time yourself), then jot down the key words you used for each.",
      lines=6,
      model=[r"\textbf{一：}一番大切だと思うのは、太鼓グループの習慣です。なぜなら、練習の前と後に礼をすることや、掛け声で応援することが、グループの和を大切にする考え方をよく表しているからです。インタビューしたメンバーも「音がそろわなければ意味がない」と言っていました。",
             r"\textbf{二：}私の町では、高校のマーチングバンドが一緒に演奏します。和太鼓と同じように、全員の音や動きをそろえることが大切です。でも、マーチングバンドは大会で勝つことが目標になりやすいのに対して、和太鼓のグループは、お祭りで地域の人と一緒に楽しむことを大切にしていると思います。",
             r"\textbf{三：}一番意外だったのは、今のような組太鼓のスタイルが、一九五〇年代に生まれた新しいものだということです。和太鼓はずっと昔から同じだと思っていましたが、伝統も新しく作られていくものなのだとわかりました。",
             r"\textbf{四：}十年後には、和太鼓はもっと世界中に広がっていると思います。アメリカの日系人のグループのように、日本人以外のメンバーも増えて、それぞれの国の音楽と合わせた新しい演奏も生まれるのではないでしょうか。"],
      rows=[("Task execution", 2, "All four questions answered directly, each with a reason or example (the interview quotation, a marching band, the 1950s, Japanese American groups).", "Answers that drift back to the presentation or stop after one sentence."),
            ("Cultural understanding", 2, "Answer 1 links practices (bowing, shouting encouragement) to a perspective (group harmony); answer 2 compares taiko with a marching band and explains the difference.", "Only describing taiko (1 point)."),
            ("Language control", 3, "Varied structures (～なければ, ～のに対して, ～ものなのだ, ～のではないでしょうか, noun modification) in consistent です・ます style.", "Short, repetitive sentences; mixed styles."),
            ("Fluency", 2, "Natural pace and intonation, clear pronunciation, few pauses.", "Long silences, many restarts.")],
      tips=[r"Each answer opens by answering the question in one sentence (一番大切だと思うのは / 私の町では / 一番意外だったのは / 十年後には), then supports it. Answer 2 is a full comparison: similarity, difference, and what each shows. About 150–200 characters fits 40 seconds."])

GUIDE, QSET = G, Q
