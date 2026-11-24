from ap_wl.model import Doc

STEM = "04-science-technology"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 4: Science and Technology", r"Unit 4 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 4 asks how science and technology change daily life, communication and society, and who benefits. Its recommended contexts are innovations and emerging technologies, personal technology and communication, science in everyday life, and the societal impacts of science and technology. This guide gives Japanese innovations from the shinkansen to emoji and iPS cells, messaging culture (stickers and read receipts), cashless payment, technology for an aging society and for disasters, the structures for cause, ability and the passive with によって, and an Email Response kit for writing politely to a community member. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Keigo I can use: \blank[10em]",
        short="Unit 4", sub="Science and Technology")

G.sec("Innovations from Japan")
G.tex(r"""
\begin{vocab}
発明（はつめい） / 発見（はっけん） & invention / discovery & \\
技術（ぎじゅつ） & technology, technique & \\
新幹線（しんかんせん） & bullet train & Tokyo--Osaka, 1964 \\
インスタントラーメン & instant noodles & Momofuku Andō, 1958 \\
絵文字（えもじ） & emoji & 176 designs for mobile phones, 1999 \\
QRコード & QR code & developed for car-parts factories, 1994 \\
iPS細胞（さいぼう） & induced pluripotent stem cells & Shinya Yamanaka, Nobel Prize 2012 \\
青色LED & blue LED & Nobel Prize in Physics 2014 \\
\end{vocab}

\textbf{Perspective often cited.} Many Japanese innovations grew out of everyday needs: instant noodles to feed people quickly after the war, QR codes to track parts in factories, emoji to say more in a short message. The perspective: careful improvement of ordinary things (改善) can change the world.
""")
G.q("1 Innovations", r"Which innovation began service between Tokyo and Osaka in 1964?",
    "新幹線", [("QRコード", "QR codes date from 1994."),
              ("絵文字", "Emoji date from 1999."),
              ("インスタントラーメン", "Instant noodles date from 1958.")],
    "1964 → 新幹線.", "The Tōkaidō Shinkansen opened just before the 1964 Tokyo Olympics.",
    ["新幹線 → 1964."])
G.q("1 Innovations", r"What was the QR code first developed for?",
    "tracking car parts in factories", [("paying in shops", "Payment came much later."),
                                        ("sending emoji", "No."),
                                        ("train tickets", "Not originally.")],
    "Factory logistics, 1994.", "A Japanese auto-parts company developed it to read part information quickly.",
    ["QR = quick response → factories."])

G.sec("Personal technology and communication")
G.tex(r"""
\begin{vocab}
スマホ & smartphone & \\
メッセージアプリ & messaging app & \\
スタンプ & stickers sent in chats & \\
既読（きどく） & ``read'' receipt & \\
既読スルー & leaving a message on read & often seen as rude \\
キャッシュレス決済（けっさい） & cashless payment & cards, QR codes, IC cards \\
交通系ICカード & transit IC card & tap to ride, also used in shops \\
マイナンバーカード & national ID number card & \\
\end{vocab}

\textbf{Messaging culture.} Stickers let people soften a message, thank someone or apologize without long sentences. Because chats show when a message has been read, many people feel they should reply quickly: leaving a message on read (既読スルー) can seem cold. The perspective: consideration for the other person's feelings shapes even short digital exchanges.
""")
G.q("2 Communication", r"What does 既読スルー mean?",
    "reading a message without replying", [("sending a sticker instead of text", "That is just sending a スタンプ."),
                                           ("deleting a message before reading it", "No."),
                                           ("replying very quickly", "The opposite.")],
    "既読 (read) + スルー (pass through).", "The sender can see the message was read, but no reply comes.",
    ["既読 → read; スルー → ignore."])
G.q("2 Communication", r"Many Japanese users send a sticker such as a bowing character to thank or apologize. Which perspective does this reflect?",
    "Softening messages and showing consideration for the other person's feelings.", [("Words are never important.", "Too extreme."),
                                                                                       ("Messages should be as blunt as possible.", "The opposite."),
                                                                                       ("Only young people should use phones.", "No.")],
    "Stickers ↔ consideration.", "A practice (sending a bowing sticker) linked to a perspective (care for relationships).",
    ["bowing sticker → politeness, warmth."])

G.sec("Science in everyday life and society")
G.tex(r"""
\begin{vocab}
少子高齢化（しょうしこうれいか） & fewer children, more older people & \\
介護（かいご）ロボット & care robot & lifting, conversation, monitoring \\
人手不足（ひとでぶそく） & labor shortage & \\
自動運転（じどううんてん） & self-driving & tested for rural buses \\
緊急地震速報（きんきゅうじしんそくほう） & earthquake early warning & alerts on phones and TV since 2007 \\
災害用伝言ダイヤル171 & disaster message dial & record a message for family \\
\end{vocab}

\textbf{Impact questions.} Technology in Japan is often discussed as an answer to social problems: robots and sensors to help care workers as the population ages, self-driving buses for towns that have lost their drivers, and warning systems that give people a few seconds to take cover before strong shaking. Good answers weigh benefits and limits: ロボットは便利ですが、人と人とのふれあいの代わりにはなりません。
""")
G.q("3 Society", r"Why is Japan developing care robots, according to the guide?",
    "The population is aging and there are not enough care workers.", [("Robots are cheaper than all human workers.", "Not the reason given."),
                                                                       ("Older people prefer robots to family.", "Not stated."),
                                                                       ("Hospitals are closing.", "Not stated.")],
    "少子高齢化 + 人手不足.", "Care robots respond to an aging population and a labor shortage.",
    ["高齢化 → more care needed; 人手不足 → fewer workers."])
G.q("3 Society", r"What does 緊急地震速報 do?",
    "It warns people seconds before strong shaking arrives.", [("It predicts earthquakes days in advance.", "No system can do that; it detects quakes that have started."),
                                                               ("It records messages for family members.", "That is the 171 dial."),
                                                               ("It measures air pollution.", "No.")],
    "Early warning after a quake starts.", "Sensors detect the first waves and send alerts before the strongest shaking reaches other areas.",
    ["緊急 (urgent) 地震 (earthquake) 速報 (quick report)."])

G.sec("Structures: ability, effort, cause, the passive with によって")
G.tex(r"""
\begin{compare}{Structure}{Use}{Example}
Potential form / ～ことができる & can & スマホで電車の切符が買えます。 \\
～ようにする & make an effort to & 寝る前はスマホを見ないようにしています。 \\
～ば～ほど & the more\ldots the more & 使えば使うほど、便利さがわかります。 \\
～によって（passive） & by (creator or inventor) & 絵文字は日本の会社員によって作られました。 \\
～おかげで / ～せいで & thanks to (good result) / because of (bad result) & アプリのおかげで道に迷わなかった。スマホのせいで寝不足だ。 \\
～ため（に） & because of (formal) & 地震のため、電車が止まっています。 \\
\end{compare}

\begin{trap}
おかげで introduces a cause of a good result and せいで a cause of a bad one: スマホのおかげで寝不足だ sounds sarcastic.
\end{trap}
""")
G.q("4 Structures", r"Choose the correct sentence: ``Emoji were created by a Japanese company employee.''",
    "絵文字は日本の会社員によって作られました。", [("絵文字は日本の会社員を作られました。", "The agent of a passive is marked with によって (or に), not を."),
                                                ("絵文字は日本の会社員によって作りました。", "The verb must be passive: 作られました."),
                                                ("日本の会社員は絵文字によって作られました。", "This reverses the meaning.")],
    "Creator + によって + passive.", "For things created, discovered or invented, the agent of the passive is marked with によって.",
    ["絵文字は (topic) … によって (by) … 作られました (were made)."])
G.q("4 Structures", r"Choose the ending that fits: 新しいアプリの\blank、道に迷わずに美術館に着きました。",
    "おかげで", [("せいで", "せいで is for a bad result; arriving without getting lost is good."),
                 ("ために", "ために would sound like purpose here."),
                 ("ばかりで", "ばかりで does not express cause this way.")],
    "Good result → おかげで.", "おかげで credits a cause for a good outcome.",
    ["arrived without getting lost → good → おかげで."])
G.q("4 Structures", r"Choose the form that means ``I try not to look at my phone before bed.'' 寝る前はスマホを見ない\blank。",
    "ようにしています", [("ことができます", "This would mean “I can not look.”"),
                         ("ようになりました", "This means it has become my habit, not an effort I make."),
                         ("せいです", "This means “it is because of.”")],
    "Effort → ～ようにする.", "～ようにしている expresses a habit the speaker makes an effort to keep.",
    ["見ないようにしています → I make a point of not looking."])

G.sec("Task kit: the Email Response to a community member")
G.tex(r"""
Unit 4 emails often come from a librarian, a teacher or a neighborhood organizer asking for help with technology. Use です・ます style throughout and humble forms for your own actions.

\begin{compare}{Move}{Phrases}{}
Open & ご連絡ありがとうございます。○○です。 & \\
Accept or decline politely & ぜひお手伝いさせていただきたいです。/ 申し訳ありませんが、その日は～ & \\
Restate request 1 & ～の件ですが、 & \\
Suggest & ～はいかがでしょうか。 / ～たらいいと思います。 & \\
Move to request 2 & また、～についてですが、 & \\
Close & 何かございましたら、ご連絡ください。どうぞよろしくお願いいたします。 & \\
\end{compare}

\begin{trap}
させていただく is humble: use it for your own action (お手伝いさせていただきます), never for the reader's. Keep every sentence in です・ます; a single plain ending (～と思う) breaks the register.
\end{trap}
""")
G.q("5 Email", r"Which sentence politely offers your own help to a librarian?",
    "ぜひお手伝いさせていただきたいです。", [("手伝ってあげるよ。", "Casual, and てあげる can sound condescending toward a superior."),
                                           ("お手伝いしてください。", "This asks the librarian to help."),
                                           ("手伝わせてやる。", "Rude.")],
    "Humble offer → させていただく.", "～させていただきたいです politely asks permission to do something for the other person.",
    ["お手伝い + させていただきたい → humble offer."])
G.q("5 Email", r"Which phrase best introduces a suggestion in a polite email?",
    "～はいかがでしょうか。", [("～しろ。", "A command."),
                             ("～しなよ。", "Casual advice to a friend."),
                             ("～するべきだ。", "Blunt and in plain style.")],
    "いかがでしょうか = how about.", "Polite suggestions to someone older or outside your group use ～はいかがでしょうか.",
    ["いかが (polite どう) + でしょうか."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 4: Science and Technology: Question Set", r"Unit 4 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Instructional Guidance and an Audio Report for listening, an Article and a Literary Text for reading) on the disaster message dial, the first emoji, a grandmother learning to chat on her phone and a robot in a care home, followed by an Email Response (8 points) with a scoring guide and a model reply. Questions are in English, as on the exam; listening sources are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 15 minutes for the email.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Email: \blank\ / 8 \qquad Target: 15+ MCQ and 6+ email",
        short="Unit 4", sub="Science and Technology")

Q.sec("Listening: Instructional Guidance")
Q.src(r"Listening 1 \textperiodcentered\ Instructional Guidance (transcript) \textperiodcentered\ 防災の授業「災害用伝言ダイヤルの使い方」", [
    r"（先生）大きな地震のあとは、電話がつながりにくくなります。そんなときに使えるのが「災害用伝言ダイヤル」です。番号は一七一。覚えやすいですね。",
    r"（先生）伝言を録音するときは、まず一七一に電話して、一を押します。それから、自分の家の電話番号を市外局番から入れてください。最後に、三十秒以内で伝言を話します。「ゆいです。学校にいます。けがはありません」のように、短く話しましょう。",
    r"（先生）家族の伝言を聞くときは、一七一のあとで二を押して、同じ電話番号を入れます。",
    r"（先生）いざというときにあわてないように、家族でどの番号を使うか決めておいてください。毎月一日には練習で使うこともできますよ。",
], 5)
Q.q("1.A.1 Detail", "Why is the disaster message dial useful after a big earthquake?",
    "Phone calls become hard to connect.", [("Cell phones stop working forever.", "Too strong; calls are just hard to connect."),
                                            ("It sends money to family members.", "No."),
                                            ("It predicts aftershocks.", "No.")],
    "電話がつながりにくくなります.", "Detail (1.A.1).",
    ["大きな地震のあとは、電話がつながりにくくなります."])
Q.q("1.B.4 Organization", "What is the correct order for recording a message?",
    "dial 171, press 1, enter the home phone number, then speak", [("dial 171, press 2, speak, then enter the number", "2 is for listening."),
                                                                  ("enter the number, dial 171, then press 1", "171 comes first."),
                                                                  ("press 1, speak, dial 171, then enter the number", "171 comes first.")],
    "まず … それから … 最後に.", "Instructional Guidance: follow the sequence markers.",
    ["まず一七一 … 一を押します。それから … 電話番号 … 最後に … 伝言."])
Q.q("1.A.1 Detail", "How long can a message be?",
    "up to 30 seconds", [("up to 3 minutes", "No."),
                         ("up to 10 seconds", "No."),
                         ("as long as needed", "No.")],
    "三十秒以内.", "Detail (1.A.1).",
    ["三十秒以内で伝言を話します."])
Q.q("1.B.5 Word meaning", r"In the lesson, いざというとき most likely means",
    "in an actual emergency", [("on your birthday", "No."),
                               ("every morning", "No."),
                               ("when you are bored", "No.")],
    "いざというとき = when it really counts.", "Word meaning (1.B.5): context of disasters.",
    ["あわてないように … 決めておいて → emergency."])
Q.q("1.C.3 Inference", "Why does the teacher mention the first day of each month?",
    "so families can practice using the service before a real disaster", [("because earthquakes happen on the first", "No."),
                                                                          ("because the service is free only then", "Not stated."),
                                                                          ("because school is closed then", "No.")],
    "練習で使える.", "Inference (1.C.3): preparation in advance.",
    ["毎月一日には練習で使うこともできます."])

Q.sec("Reading: Article")
Q.src(r"Reading 1 \textperiodcentered\ Article \textperiodcentered\ 「絵文字が生まれた日」", [
    r"今では世界中の人が使っている絵文字。最初の絵文字は、一九九九年に日本の携帯電話のために作られた。デザインしたのは、当時携帯電話の会社で働いていた若い社員だった。",
    r"当時の携帯電話の画面はとても小さく、メールに書ける文字の数も少なかった。「短い文だと、怒っているように見えることがある。気持ちを伝えるには、絵があったほうがいい」と考えたそうだ。",
    r"彼は、天気のマーク、ハート、顔など百七十六個の絵文字を、たった十二かける十二の小さな点で作った。二〇一六年には、この最初の絵文字がニューヨークの近代美術館に収蔵された。",
    r"小さな画面から生まれたアイデアが、今では言葉の違う人どうしの気持ちもつないでいる。",
], 5)
Q.q("1.A.1 Detail", "When and for what were the first emoji made?",
    "in 1999, for Japanese mobile phones", [("in 2016, for a museum", "2016 is when they entered a museum collection."),
                                            ("in 1964, for the shinkansen", "No."),
                                            ("in 1999, for computers", "They were made for mobile phones.")],
    "1999 + 携帯電話.", "Detail (1.A.1).",
    ["一九九九年に日本の携帯電話のために作られた."])
Q.q("1.B.1 Purpose", "Why did the designer think pictures were needed?",
    "Short text messages could seem angry, so pictures would help convey feelings.", [("Japanese has too few words.", "No."),
                                                                                      ("Pictures used less battery.", "Not stated."),
                                                                                      ("His boss asked for advertisements.", "Not stated.")],
    "気持ちを伝えるには.", "Purpose (1.B.1): the problem he wanted to solve.",
    ["短い文だと、怒っているように見えることがある."])
Q.q("1.A.1 Detail", "How many emoji were in the first set?",
    "176", [("12", "12 × 12 is the size in dots."),
            ("144", "That is 12 × 12, the size of each emoji."),
            ("2016", "That is a year.")],
    "百七十六個.", "Detail (1.A.1).",
    ["百七十六個の絵文字."])
Q.q("1.C.3 Inference", "What does the museum's decision in 2016 suggest?",
    "The first emoji came to be seen as important design.", [("Emoji are no longer used.", "Everyone uses them."),
                                                             ("The designer became a painter.", "Not stated."),
                                                             ("The museum sells mobile phones.", "No.")],
    "収蔵 = added to the collection.", "Inference (1.C.3): a museum of modern art recognized their design value.",
    ["近代美術館に収蔵された → recognized as design."])
Q.q("1.B.1 Main idea", "What is the main idea of the last paragraph?",
    "An idea born from a small screen now connects people across languages.", [("Emoji will replace all languages.", "Too strong."),
                                                                                ("Screens are still too small.", "No."),
                                                                                ("Emoji cause misunderstandings.", "The opposite.")],
    "言葉の違う人どうしの気持ちもつないでいる.", "Main idea (1.B.1).",
    ["小さな画面 → 世界中の人をつなぐ."])

Q.sec("Reading: Literary Text")
Q.src(r"Reading 2 \textperiodcentered\ Literary Text \textperiodcentered\ 「祖母のスタンプ」（エッセイ）", [
    r"八十歳の祖母がスマホを買った。最初の一週間、祖母から来るメッセージは、ほとんど「。」だけだった。どうやら、送るつもりはなかったらしい。",
    r"週末、私は祖母の家に行って、メッセージの送り方を教えた。祖母は老眼鏡をかけて、一本の指でゆっくり画面を押した。「若い人は、どうしてこんなに速く打てるのかねえ。」",
    r"一か月後、祖母から初めてスタンプが届いた。ぺこりとおじぎをするネコのスタンプだった。そのあとに、「いつもありがとう」と短いメッセージが続いていた。",
    r"字は小さいし、返事は遅い。でも、祖母のメッセージを読むたびに、私は昔もらった手紙のような温かさを感じる。",
], 5)
Q.q("1.C.3 Inference", r"Why were most of the grandmother's first messages just 「。」?",
    "She was sending them by accident.", [("She was angry with the writer.", "Not implied."),
                                          ("She preferred short messages.", "She did not mean to send them."),
                                          ("Her phone was broken.", "Not stated.")],
    "送るつもりはなかったらしい.", "Inference (1.C.3): らしい marks the writer's guess.",
    ["どうやら、送るつもりはなかったらしい."])
Q.q("1.A.1 Detail", "How did the grandmother type at first?",
    "slowly, with one finger, wearing reading glasses", [("quickly, with both thumbs", "That is how young people type."),
                                                        ("by voice only", "Not mentioned."),
                                                        ("with a pen", "Not mentioned.")],
    "一本の指でゆっくり.", "Detail (1.A.1).",
    ["老眼鏡をかけて、一本の指でゆっくり画面を押した."])
Q.q("1.B.5 Word meaning", r"In the essay, ぺこりとおじぎをする describes",
    "a quick, polite bow", [("a deep sleep", "No."),
                            ("a loud laugh", "No."),
                            ("a long wave", "No.")],
    "ぺこり = a quick bow.", "Word meaning (1.B.5): onomatopoeia for bowing.",
    ["ぺこりとおじぎ → quick bow."])
Q.q("1.B.3 Tone", "What tone does the last paragraph have?",
    "warm and affectionate", [("impatient and annoyed", "けど/でも turns the complaints into affection."),
                              ("sad and hopeless", "No."),
                              ("formal and distant", "No.")],
    "でも… 温かさ.", "Tone (1.B.3): small flaws, then warmth.",
    ["字は小さいし、返事は遅い。でも … 温かさを感じる."])
Q.q("1.C.2 Conclusion", "What does the essay suggest about technology and family?",
    "New tools can carry the same warmth as older ways of communicating.", [("Older people cannot learn new technology.", "The grandmother learned."),
                                                                            ("Letters are better than messages.", "The writer compares them positively."),
                                                                            ("Stickers are only for young people.", "The grandmother uses them.")],
    "手紙のような温かさ.", "Conclusions (1.C.2).",
    ["スタンプ + メッセージ → 手紙のような温かさ."])

Q.sec("Listening: Audio Report")
Q.src(r"Listening 2 \textperiodcentered\ Audio Report (transcript) \textperiodcentered\ ニュース「介護施設にロボット」", [
    r"（記者）ここは、さくら市の介護施設です。去年から、アザラシの形をした小さなロボットが使われています。なでると目を開けたり、鳴いたりします。",
    r"（記者）施設長によると、ロボットと遊ぶようになってから、あまり話さなかったお年寄りが笑うことが多くなったそうです。また、夜にベッドから起き上がるとセンサーが知らせてくれるので、職員の負担も少し軽くなりました。",
    r"（施設長）人手不足は深刻です。ロボットは助けになります。でも、ロボットが人の代わりになるわけではありません。手を握って話を聞くのは、やはり人の仕事です。",
], 5)
Q.q("1.A.1 Detail", "What does the robot in the care home look like?",
    "a small seal", [("a small dog", "No."),
                     ("a human nurse", "No."),
                     ("a cat", "No.")],
    "アザラシ = seal.", "Detail (1.A.1).",
    ["アザラシの形をした小さなロボット."])
Q.q("1.A.1 Detail", "What change has the director noticed in some residents?",
    "Residents who rarely talked now laugh more often.", [("Residents sleep all day.", "No."),
                                                          ("Residents no longer need staff.", "No."),
                                                          ("Residents want to go home.", "Not mentioned.")],
    "笑うことが多くなった.", "Detail (1.A.1).",
    ["あまり話さなかったお年寄りが笑うことが多くなった."])
Q.q("1.B.1 Purpose", "How do the sensors help the staff?",
    "They alert staff when a resident gets out of bed at night.", [("They cook meals.", "No."),
                                                                   ("They clean rooms.", "No."),
                                                                   ("They give medicine.", "No.")],
    "センサーが知らせてくれる.", "Detail/purpose.",
    ["夜にベッドから起き上がるとセンサーが知らせてくれる."])
Q.q("1.B.3 Point of view", "What is the director's view of robots?",
    "They help, but they cannot replace people.", [("They will soon replace all care workers.", "She says the opposite."),
                                                   ("They are useless.", "She says they help."),
                                                   ("They should be used only at night.", "Not stated.")],
    "助けになります。でも、…代わりになるわけではありません.", "Point of view (1.B.3): わけではない denies a conclusion.",
    ["ロボットが人の代わりになるわけではありません."])
Q.q("1.C.3 Inference", r"What does 手を握って話を聞くのは、やはり人の仕事です suggest?",
    "Human warmth and attention remain essential in care.", [("Robots cannot hold objects.", "Literal misreading."),
                                                             ("Staff should talk less.", "No."),
                                                             ("Residents prefer robots.", "No.")],
    "Human touch.", "Inference (1.C.3).",
    ["手を握って話を聞く → human warmth."])

Q.frq(kind="Email Response", head=r"Question 4 \textperiodcentered\ Email Response \textperiodcentered\ 8 points \textperiodcentered\ about 15 minutes",
      mins=15,
      directions=[r"\textbf{Directions.} Read the email from a member of your community. Write a reply in Japanese that responds to all the questions and requests in the email, in a culturally appropriate way."],
      prompt=[r"\textbf{差出人：}市立図書館　山田 \quad \textbf{件名：}「スマホ教室」のお手伝いのお願い",
              "こんにちは。市立図書館の山田です。来月の土曜日に、お年寄りのための「スマホ教室」を開くことになりました。そこで、高校生のボランティアを探しています。まず、手伝っていただける場合、お年寄りに最初に何を教えたらいいと思いますか。また、若い人がお年寄りに教えるとき、どんなことに気をつけたらいいでしょうか。お返事をお待ちしております。",
              "市立図書館　山田"],
      ask="Write your reply to 山田さん in Japanese.",
      model=["山田様",
             "ご連絡ありがとうございます。○○高校二年のエミリーです。「スマホ教室」のボランティア、ぜひお手伝いさせていただきたいです。",
             "まず、最初に教えることについてですが、家族とのビデオ通話の使い方がいいと思います。なぜなら、遠くに住んでいる孫の顔を見ながら話せたら、お年寄りもスマホを使いたいという気持ちになると思うからです。それに、私の祖母も、ビデオ通話を覚えてから、ほかの機能にも興味を持つようになりました。",
             "また、教えるときに気をつけることですが、ゆっくり、わかりやすい言葉で説明することが大切だと思います。たとえば、「タップ」や「アプリ」のようなカタカナの言葉は、使う前に意味を説明したほうがいいです。そして、私たちが代わりに操作するのではなく、お年寄りが自分の指で押せるように、横で待つようにしたいと思います。",
             "当日、何か準備するものがございましたら、ご連絡ください。どうぞよろしくお願いいたします。",
             "エミリー・ジョンソン"],
      rows=[("Message development", 3, "Answers both questions directly (what to teach first: video calls, with a reason and a personal example; what to be careful about: slow, clear explanations, explaining katakana words, letting them press the screen themselves) with details.", "Answering only one question; ideas with no reason or example."),
            ("Organization", 2, "Opening (thanks, self-introduction, acceptance) and closing; one paragraph per question; cohesive devices (まず～についてですが / なぜなら / それに / また / たとえば / そして).", "No opening or closing; both answers mixed together."),
            ("Language control", 3, "Consistent です・ます style with humble forms for one's own actions (させていただきたい, ございましたら, お願いいたします) and varied grammar (～たら, ～ようになる, ～ように, ～のではなく, ～ほうがいい).", "Plain endings mixed in; casual expressions to an adult outside one's group; frequent errors.")],
      tips=[r"The reply accepts the request before answering, then restates each question (～についてですが / ～ことですが). Humble forms (させていただきたい, ございましたら, いたします) fit a librarian the writer does not know well, and the style never slips into plain endings."])

GUIDE, QSET = G, Q
