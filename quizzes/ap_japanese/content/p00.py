from ap_wl.model import Doc

STEM = "00-exam-playbook"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Part 0: The Revised Exam and the Task Playbook", r"Part 0 \textperiodcentered\ Study Guide",
        abstract=r"""This guide is written for the revised AP Japanese Language and Culture course (effective fall 2026) and its first exam, in May 2027, which runs entirely in Bluebook. It sets out what each of the four free-response tasks and ten multiple-choice task types asks you to do, how the free-response tasks are scored, and the language that moves a response up a scoring row. Read it before the unit guides: every unit guide ends with a task kit that assumes the rubrics here. Japanese is written with kanji and kana and no furigana, as on the exam; on exam day you type your writing with a Japanese input method. Sources: the College Board AP Japanese exam page and the Course and Exam Description (CED), effective fall 2026. Check AP Central for any later change.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 13+ \qquad Rubric rows I still mix up: \blank[10em]",
        short="Part 0", sub="The Revised Exam and the Task Playbook")

G.sec("The revised exam at a glance")
G.tex(r"""
The exam takes about 1 hour 50 minutes. The free-response section now comes \emph{first}. Two of its four tasks are speaking tasks built on a course project you prepare before exam day; the other two are writing tasks that are independent of the project.

\begin{compare}{Part}{What you do}{Count, time, weight}
I-A Speaking & Q1 \textbf{Project Presentation}: present your project research. & 3 min to prepare, 3 min to present; 20\% \\
 & Q2 \textbf{Project Q\&A}: answer four recorded questions about your presentation and research. & Each question heard twice; 40 s per answer; 15\% \\
I-B Writing & Q3 \textbf{Story Narration}: narrate a story from four pictures. & 30 min for Q3 and Q4 together; 7.5\% \\
 & Q4 \textbf{Email Response}: reply to an email from a friend or community member. & 7.5\% \\
II-A Listening & Five sets of five questions. & 25 questions, 25 min, 25\% \\
II-B Reading & Six sets. & 30 questions, 40 min, 25\% \\
\end{compare}

\subsection{The six units}
\begin{terms}
Unit 1 & Families and Communities: family relationships, community activities, social interactions, urban and rural life. \\
Unit 2 & Language and Culture: customs and celebrations, linguistics, Japanese in the world. \\
Unit 3 & Art and Creativity: architecture, artistic heritage, beauty and aesthetics, fashion and design, literature, visual and performing arts. \\
Unit 4 & Science and Technology: innovations, personal technology and communication, science in everyday life, societal impacts. \\
Unit 5 & Contemporary Life: education and career, entertainment and media, food and health, pop culture, sports and leisure, travel. \\
Unit 6 & Global Contexts: global communication, the natural world, history, policy and planning, transportation. \\
\end{terms}

\subsection{The three skill categories}
\textbf{1 Interpretive communication} (all of Section II): 1.A recognize explicit meaning (details, data points and trends); 1.B interpret meaning (main idea, audience, point of view and tone, organization, word meaning from context); 1.C synthesize and infer (connect sources, draw conclusions, infer what is implied).
\textbf{2 Interpersonal and presentational communication} (Section I): 2.A language for the purpose and context, including register (plain or polite style, honorifics); 2.B comprehensibility (circumlocution, self-correction, pronunciation, written conventions); 2.C sharing ideas, examples and sources; 2.D organization and cohesive devices.
\textbf{3 Cultural understanding}: 3.A describe, compare and reflect on cultural \emph{products}, \emph{practices} and \emph{perspectives}.

\begin{keyidea}[Products, practices, perspectives]
A \textbf{product} is a thing people make (a bento, a song, a temple, an app). A \textbf{practice} is what people do (how New Year is celebrated, how guests are welcomed, taking off shoes at the door). A \textbf{perspective} is the value or belief that explains the product or practice (respect for elders, harmony in the group, gratitude). Two rubric rows reward linking a product or practice to the perspective behind it.
\end{keyidea}
""")
G.q("1 Format", r"On the revised exam, which part of the score does the reading section carry?",
    r"25\%", [(r"50\%", "50% is the whole multiple-choice section (listening plus reading) or the whole free-response section."),
              (r"20\%", "20% is the Project Presentation alone."),
              (r"7.5\%", "7.5% is one writing task (Story Narration or Email Response).")],
    "Reading: 30 Q, 40 min, 25%.", "Section II is 50% of the score, split evenly: listening 25%, reading 25%.",
    ["Section II (multiple choice) = 50%.", "It has two equal parts: Part A listening and Part B reading, 25% each."])
G.q("1 Format", r"How long do you have to answer each Project Q\&A question?",
    "40 seconds", [("20 seconds", "20 seconds was the response time in the old Conversation task; the Q&A gives 40."),
                   ("3 minutes", "3 minutes is the preparation time, and the speaking time, of the Project Presentation."),
                   ("2 minutes", "2 minutes matches no task on the revised exam.")],
    "Q&A: four questions, each heard twice, 40 s each.",
    "The Project Q&A plays four recorded questions about your presentation and research. Each is heard twice, and you have 40 seconds to answer each.",
    ["Know the clock for each speaking task: 3 + 3 minutes for the presentation, 40 seconds per Q&A answer."])
G.q("1 Skills", r"Explaining that many families visit a shrine at New Year (初詣) \emph{because} starting the year with a wish for health and good fortune matters connects a practice to a",
    "perspective", [("product", "A product is a made thing, such as the shrine's amulets; the value behind the visit is not a thing."),
                    ("register", "Register is the level of formality of your language, not a cultural concept."),
                    ("cohesive device", "A cohesive device is a linking word such as それに or そのため.")],
    "The value behind a practice = a perspective.",
    "Perspectives are the values, beliefs and ideas that explain why people make certain products or follow certain practices.",
    ["Visiting a shrine at New Year is a practice.", "The wish to start the year well is the reason behind it: a perspective."])

G.sec("Multiple choice: the ten task types")
G.tex(r"""
Every set is built on one source. The listening sources are heard, the reading sources are read; you see the questions on screen, in English. Each listening set has five questions. Reading has six sets: Article (0--2 sets), Article and Chart (1--2), Correspondence (1--2), Literary Text (0--2) and Promotional Material (1--2).

\begin{compare}{Task type}{The source}{What the questions target}
\multicolumn{3}{@{}l}{\textsf{\textbf{Part A: Listening (one set of each)}}}\\
Audio and Chart & A short audio report with a chart or graph. & Data points, trends, and how the audio and chart fit together. \\
Audio Report & A news-style or radio report. & Main idea, details, the speaker's purpose. \\
Conversation & Two or more people talking. & Each speaker's view, what they decide, what will happen next. \\
Instructional Guidance & Instructions or an announcement (a teacher, a guide, a station). & Steps, sequence, conditions, who must do what. \\
Presentation & A talk, lecture or podcast segment. & Organization, examples, the speaker's conclusion. \\
\multicolumn{3}{@{}l}{\textsf{\textbf{Part B: Reading}}}\\
Article & A news or feature article. & Main idea, details, point of view. \\
Article and Chart & An article with a table, chart or graph. & Reading the data, connecting it to the text. \\
Correspondence & A letter, email or message. & Purpose, requests, relationship of writer and reader. \\
Literary Text & A story or essay excerpt. & Character, feeling, implied meaning, word meaning. \\
Promotional Material & An ad, flyer or notice. & Audience, offer, conditions, dates and prices. \\
\end{compare}

\subsection{Method}
\textbf{Read the questions first} when the screen allows; they tell you what to listen or read for. \textbf{Listen for structure words} (まず, 次に, しかし, つまり, 最後に) because they mark where answers sit. \textbf{Answer from the source}, not from what is generally true: a choice that is true about Japan but not stated or implied in the source is wrong. With charts, \textbf{read the title, units and years} before the numbers (\%, 人, 円, 時間).

\begin{trap}
In this series the listening sets are printed as transcripts, because a PDF cannot play audio. Read each transcript once at normal speed and do not reread before answering. On the exam you will hear each source; practice with real audio (AP Classroom, Japanese podcasts and news) as well.
\end{trap}
""")
G.q("2 Task types", "Which of these is a reading task type, not a listening one?",
    "Correspondence", [("Conversation", "Conversation is a listening set: two or more people talking."),
                       ("Audio and Chart", "Audio and Chart is a listening set: an audio report paired with a chart."),
                       ("Presentation", "Presentation is a listening set: a talk or lecture you hear.")],
    "Correspondence is one of the five reading types.",
    "Listening: Audio and Chart, Audio Report, Conversation, Instructional Guidance, Presentation. Reading: Article, Article and Chart, Correspondence, Literary Text, Promotional Material.",
    ["Sort the ten task types by section; only Correspondence is in reading."])
G.q("2 Method", "A reading choice says something true about Japanese culture that the passage never mentions. It is",
    "wrong, because answers must come from the source",
    [("right, because it is culturally accurate", "Accuracy in general does not make it the answer; the question asks about this source."),
     ("right if it uses a word from the passage", "Choices that reuse a word from the passage but say something the passage does not are a classic trap."),
     ("usually the main idea", "A main idea must summarize the passage itself, not outside knowledge.")],
    "Answer from the source, not from general knowledge.",
    "Multiple-choice questions test comprehension of the given source. A statement the source neither states nor implies cannot be the answer.",
    ["Find the line in the source that supports a choice before picking it."])

G.sec("Interpretive skills and question types")
G.tex(r"""
Most questions fall into one of three skill groups. Learning to spot the group from the stem tells you how to read.

\begin{compare}{Skill}{Typical stems}{How to answer}
1.A Explicit meaning & According to the email, when\ldots? What does the chart show about 2024? & Find the sentence or cell; match its meaning, not its words. \\
1.B Interpret & What is the main purpose? Who is the intended audience? What is the speaker's attitude? What does 「XX」 most likely mean? & Look at the opening and closing for purpose; at word choice for tone; at surrounding sentences for word meaning. \\
1.C Synthesize and infer & What can be inferred? How does the chart support the speaker's claim? What will the woman probably do next? & Combine two pieces of information; choose the conclusion that must be true, not the one that could be. \\
\end{compare}

\subsection{Words that signal the answer}
\begin{vocab}
実は & actually & what follows corrects or reveals something \\
しかし / でも / ところが & but, however & ところが signals something unexpected \\
つまり & in other words & a summary: main-idea answer \\
～らしい / ～そうだ & apparently / I hear & hearsay, not the speaker's own claim \\
～はずだ & should, is expected to & a confident inference \\
やっと & finally & relief after waiting \\
せっかく & with all the trouble taken & often regret that an effort was wasted \\
～てしまった & ended up, unfortunately & completion or regret \\
\end{vocab}

\begin{trap}
Tone questions turn on small words. まさか signals disbelief; さすが signals admiration (``as expected of''); ～のに after a fact signals disappointment or complaint (一時間も待ったのに). Particles carry tone too: も after a number stresses ``that many''.
\end{trap}
""")
G.q("3 1.B Tone", r"A speaker says: 一時間も待ったのに、彼は来なかった。 The speaker's attitude is best described as",
    "disappointed and annoyed", [("grateful", "Nothing in the sentence thanks anyone."),
                                 ("relieved", "やっと would signal relief after waiting; のに signals a complaint."),
                                 ("indifferent", "も after 一時間 stresses how long the wait was, so the speaker clearly cares.")],
    "～のに = complaint; 一時間も = that long.",
    "のに after a fact introduces an unwelcome result; も after a number stresses the amount.",
    ["一時間も待った: the speaker waited a full hour.", "のに、彼は来なかった: and still he didn't come → annoyance."])
G.q("3 1.C Inference", r"A message ends: 明日テストがあるなら、映画は週末にしようか。 What can be inferred?",
    "The movie is postponed because of the test", [("The writer is taking a test tomorrow", "The writer is reacting to the reader's test (テストがあるなら, if you have a test)."),
                                                   ("They will see the movie tonight", "週末にしよう moves the movie to the weekend."),
                                                   ("The writer does not like movies", "The writer proposes going on the weekend, so this is unsupported.")],
    "なら (given that) + 週末にしよう = postponing.",
    "なら takes up what the other person said as a premise; the main clause draws the conclusion.",
    ["明日テストがあるなら: since you have a test tomorrow.", "映画は週末にしようか: let's make the movie the weekend."])

G.sec("Story Narration")
G.tex(r"""
You see four pictures and write a complete story that follows them in order. Plan for about 15 of the 30 writing minutes. The CED sets no length; 300--400 characters gives room for detail and cohesion without careless errors.

\begin{compare}{Row (points)}{To earn the top score}{What drops you a point}
Narrative development (3) & A complete story consistent with all four pictures, with relevant details or dialogue. & Skipping or misreading a picture (2 if at least three are used; 1 if only one or two); no details. \\
Organization (2) & Clear beginning, middle and end; logical progression; effective cohesive devices. & Parts hard to follow; only そして as a link. \\
Language control (3) & Wide vocabulary including culturally relevant expressions; a variety of grammar; consistent style; no errors that impede comprehension. & Basic vocabulary and structures; mixing plain and polite style; wrong kanji conversions. \\
\end{compare}

\subsection{A five-step method}
\begin{enumerate}[leftmargin=2em]
\item \textbf{Choose one style and keep it}: です・ます (safe) or plain style (だ・である). Never mix them.
\item \textbf{Name the characters and the setting} in one line (ある日、ケンさんは友だちと公園へ行きました。).
\item \textbf{One to three sentences per picture}, in picture order. Say what happens \emph{and} why or how people feel.
\item \textbf{Link the pictures} with time and logic words: ある日, ～ていると, 急に, ～たら, そこで, ところが, すると, 結局, 最後に.
\item \textbf{Add one line of dialogue, one feeling, and an ending} (それ以来、ケンさんは毎朝天気予報を見るようになりました。). Leave two minutes to check particles and kanji conversion.
\end{enumerate}

\begin{keyidea}[Picture-to-sentence frames]
～ていると、急に…… \quad ～たら、…… \quad ところが…… \quad そこで…… \quad ～てくれました \quad ～てしまいました \quad 結局…… \quad それ以来……ようになりました
\end{keyidea}
""")
G.q("4 Rubric", "A story uses only three of the four pictures but is otherwise detailed and logical. What is the most it can earn for narrative development?",
    "2 of 3", [("3 of 3", "A 3 requires a complete story that integrates all four pictures."),
               ("1 of 3", "1 is for a story that uses only one or two pictures, with minimal detail."),
               ("0 of 3", "0 is for a response that is irrelevant, restates the prompt or is too brief.")],
    "Three pictures caps development at 2.",
    "The narrative development row scores 3 only for a complete story consistent with all four pictures; a story that includes at least three pictures with some details can earn 2.",
    ["Count pictures used: three.", "The descriptor for 2 says “includes at least three pictures.”"])
G.q("4 Cohesion", "Which sequence of links best shows the organization the story rubric rewards?",
    "ある日…… ～ていると、急に…… そこで…… 結局……",
    [("そして…… そして…… そして…… そして……", "Repeating そして links the events, but limited, repeated devices earn 1, not 2, for organization."),
     ("と…… と…… と…… と……", "と as \"and\" joins nouns, not sentences; it cannot link the events of a story."),
     ("から…… から…… から…… から……", "Every link gives a reason; there is no sense of time, surprise or result.")],
    "Varied time, surprise and result links = effective cohesive devices.",
    "Organization rewards a clear beginning, middle and end with a variety of cohesive devices.",
    ["ある日 sets the scene; ～ていると、急に introduces the problem; そこで gives the reaction; 結局 the outcome."])

G.sec("Email Response")
G.tex(r"""
You read an email from a friend or community member and reply in Japanese. The email always contains \textbf{two requests or questions}; the top score requires clear, direct answers to both, with details or examples. Plan for about 15 minutes.

\begin{compare}{Row (points)}{To earn the top score}{What drops you a point}
Message development (3) & Clearly and directly answers both requests, with relevant details or examples. & Answering only one request (2 at most); answering without giving the requested information (1). \\
Organization (2) & Logical flow; an opening and a closing; effective cohesive devices. & No opening or closing; ideas in a list. \\
Language control (3) & Wide vocabulary including culturally relevant expressions; variety of grammar; consistently appropriate register; no impeding errors. & Mixing plain and polite style; casual language to a teacher or elder; frequent errors. \\
\end{compare}

\subsection{Register}
To a friend: plain style is natural (ゆいさん、メールありがとう！ \ldots じゃあ、またね。), and です・ます is also fine if you keep it throughout. To a teacher, a host family, an elder or a community member: です・ます style with honorific and humble forms where they fit (いらっしゃる, おっしゃる, 伺う, いただく, 申します) and a formal closing (どうぞよろしくお願いいたします。). Whichever style you choose, keep it from the first line to the last.

\subsection{A four-part plan}
\begin{enumerate}[leftmargin=2em]
\item \textbf{Opening and thanks}: メールありがとうございました。/ お元気ですか。
\item \textbf{Request 1}: restate it in a few words (～についてですが、), answer it, give two reasons or details (まず……それに……).
\item \textbf{Request 2}: the same (それから、～のことですが、).
\item \textbf{Closing}: an offer or a wish (何かあったら、いつでも聞いてください。), then your name.
\end{enumerate}
""")
G.q("5 Rubric", "An email reply answers the first question with two good reasons but never addresses the second. Message development can earn at most",
    "2 of 3", [("3 of 3", "3 requires clear, direct answers to both requests."),
               ("1 of 3", "1 is for a response that does not provide the requested information at all; this one answers one request well."),
               ("0 of 3", "0 is for an irrelevant reply or one that only restates the prompt.")],
    "One of two requests answered = 2 at most.",
    "Message development: 3 answers both requests with details; 2 addresses at least one request.",
    ["One request is fully answered, one ignored: the 2 descriptor."])
G.q("5 Register", "Your neighbor 田中さん, an older woman, emails to ask whether you could help at the neighborhood festival. Which opening and closing fit the register?",
    "田中さん、こんにちは。……どうぞよろしくお願いいたします。", [("田中さん、やあ！……じゃあね！", "やあ and じゃあね are casual; to an older community member use polite style throughout."),
                                                          ("おはよう！……またね！", "This is what you would write to a friend your own age."),
                                                          ("田中さん、こんにちは。……じゃあ、またね！", "The opening is right, but the closing drops to casual style; shifting style is penalized.")],
    "Elder + community member → polite, formal closing, no shift.",
    "Language control rewards a consistently appropriate register. To an older neighbor, use です・ます style throughout and a formal closing.",
    ["Identify the reader: an older neighbor.", "Keep polite style from the greeting to the closing."])

G.sec("The course project: Presentation, Q\\&A and the PPR")
G.tex(r"""
The College Board releases the Course Project Packet in January of the exam year (January 2027). For 2026--27 the project looks at \textbf{music} as a lens on cultural products, practices and perspectives; you choose a topic within Japanese-speaking communities. Over about fifteen class periods you explore sources, choose \textbf{three factors to explain, at least one of them a cultural perspective}, research them, and practice.

\subsection{The Personalized Project Reference (PPR)}
The PPR is a word- or character-limited outline that you write yourself and submit in the AP Digital Portfolio by \textbf{April 30, 2027}. You get a printed copy on exam day to refer to. You may not read it aloud word for word, so write keywords, not sentences. Your teacher may advise on choosing keywords but may not write the wording or the examples. Check the project packet for the exact limit.

\subsection{Q1 Project Presentation (11 points)}
\begin{compare}{Row (points)}{To earn the top score}{What drops you a point}
Task execution (2) & At least three factors, each explained with detail and specific examples from your research. & Listing factors; explaining only one or two; relying on anecdotes or general knowledge. \\
Cultural understanding (2) & Specific examples that show how a perspective relates to a product or practice. & Examples with no link to the perspective behind them. \\
Organization (2) & Clear structure and logical progression; varied cohesive devices. & Ideas that jump; the same link word every time. \\
Language control (3) & Wide vocabulary with culturally relevant expressions; varied grammar; appropriate, consistent style; no impeding errors. & Basic structures; errors that block meaning. \\
Delivery (2) & Engaging rate and intonation; smooth, confident speech; clear pronunciation. & Hesitant, monotone or disconnected speech. \\
\end{compare}

\subsection{Q2 Project Q\&A (9 points)}
\begin{compare}{Row (points)}{To earn the top score}{What drops you a point}
Task execution (2) & At least three of the four prompts answered appropriately. & Incomplete or irrelevant answers. \\
Cultural understanding (2) & In at least one answer, a cultural comparison or a reflection on how a perspective relates to a product or practice. & Describing culture without explaining it. \\
Language control (3) & Wide, varied language; uses circumlocution and paraphrase to keep going. & Vocabulary too limited to keep the exchange going. \\
Fluency (2) & Fluid, automatic speech; effective rate and intonation. & Speech that stops and starts. \\
\end{compare}

\begin{keyidea}[A 3-minute shape]
Opening, 20 s: topic and the three factors (私の研究テーマは～です。三つの点から説明します。). Each factor, 45 s: claim, one researched example with its source (～によると), and the perspective behind it (これは～という考え方を表しています). Conclusion, 20 s: what the factors show together and one comparison (アメリカと比べると、～).
\end{keyidea}
""")
G.q("6 PPR", "Which use of the Personalized Project Reference is allowed on exam day?",
    "glancing at keywords to keep the presentation organized",
    [("reading the full script aloud", "Students may refer to the PPR but may not read from it verbatim."),
     ("asking the teacher to rewrite it on exam morning", "Teachers may advise on keywords but may not write its wording or examples, and it is submitted by April 30."),
     ("adding new pages of notes in the exam room", "You receive a printed copy of the PPR you submitted; you cannot add to it on exam day.")],
    "PPR = your own keyword outline; refer to it, don't read it.",
    "The PPR is a limited outline you submit by April 30 and receive in print on exam day. It supports a spoken presentation, so verbatim reading is not allowed.",
    ["Keywords, not sentences: that is what the limit forces anyway."])
G.q("6 Rubric", "A presentation names three factors but explains only one with researched detail. For task execution it earns",
    "1 of 2", [("2 of 2", "2 requires detailed explanation of at least three factors from research."),
               ("0 of 2", "It does address the prompt with factors and one detailed explanation, which is the 1 descriptor."),
               ("3 of 3", "Task execution is out of 2, not 3.")],
    "Listing factors but explaining only one or two = 1.",
    "Task execution: 2 = at least three factors explained with detail from research; 1 = factors listed with only one or two explained in detail, or reliance on anecdote.",
    ["Three named, one explained: the 1 descriptor."])
G.q("6 Rubric", r"Which Q\&A answer best earns the cultural understanding point?",
    "日本では友だちとカラオケで一緒に歌うことが多いです。これはグループで楽しむことを大切にする考え方を表していると思います。アメリカでは、パーティーで音楽を聞くことのほうが多いです。",
    [("私は日本の歌が好きです。きれいだからです。", "A personal preference with no cultural product, practice or perspective explained."),
     ("日本には歌手がたくさんいます。", "A bare fact with no comparison and no link to a perspective."),
     ("たくさん資料を読んで、時間がかかりました。", "Describes your process, not the culture.")],
    "Comparison + perspective linked to a practice = cultural understanding 2.",
    "The Q&A cultural understanding row rewards, in at least one answer, a comparison or a reflection on how a perspective relates to a product or practice.",
    ["The karaoke answer names a practice (singing together), a perspective (enjoying things as a group) and a comparison (the U.S.)."])

G.sec("Language control: structures that raise the score")
G.tex(r"""
Every free-response rubric has a language control row worth 3 points. The top descriptor asks for \emph{a variety of grammatical structures} and a consistent, appropriate style with no errors that impede comprehension. Each structure below should appear naturally at least once in your practice writing.

\begin{compare}{Structure}{Pattern}{Example}
て-form linking & V-て, V-て & 朝ご飯を食べて、学校へ行きました。 \\
Reason & ～から / ～ので & 雨が降っていたので、家にいました。 \\
Contrast with regret & ～のに & 練習したのに、負けてしまいました。 \\
Concession & ～ても & 雨が降っても、試合をします。 \\
Conditionals & と / ば / たら / なら & 春になると、桜が咲きます。京都に行くなら、秋がいいですよ。 \\
Giving and receiving & V-てあげる / てくれる / てもらう & 友だちが宿題を手伝ってくれました。 \\
Passive & V-(ら)れる & 電車の中で足を踏まれました。 \\
Causative & V-(さ)せる & 母は弟に部屋を掃除させました。 \\
Causative-passive & V-(さ)せられる & 子どものころ、ピアノを練習させられました。 \\
Noun modification & plain form + noun & 祖母が作った着物を着ました。 \\
Change and decision & ～ようになる / ～ことにする & 日本語が話せるようになりました。留学することにしました。 \\
Honorific and humble & いらっしゃる, おっしゃる / 伺う, 申す & 先生はいらっしゃいますか。明日伺います。 \\
\end{compare}

\begin{trap}
Inside a noun modifier, use the plain form: 祖母が作った着物, not 祖母が作りました着物. And keep one style: a reply that switches between です・ます and plain endings loses credit on language control even when every sentence is grammatical.
\end{trap}
""")
G.q("7 Giving", r"Choose the correct ending: 友だちが宿題を手伝って\blank。",
    "くれました", [("あげました", "あげる is used when the speaker (or the speaker's side) gives to someone else; here the friend helps the speaker."),
                   ("もらいました", "With もらう the receiver is the subject: 友だちに手伝ってもらいました."),
                   ("やりました", "やる is giving downward (to a younger person, an animal or a plant), not a friend helping you.")],
    "Someone does something for me → てくれる.",
    "When another person does a favor for the speaker, use V-てくれる with that person as the subject (marked by が).",
    ["友だちが (the friend is the subject) … 手伝って (helped) … for me → くれました."])
G.q("7 Modification", r"Choose the correct sentence: ``This is the kimono my grandmother made.''",
    "これは祖母が作った着物です。", [("これは祖母が作りました着物です。", "Polite forms are not used inside a noun modifier; use the plain form 作った."),
                                    ("これは祖母が作ったの着物です。", "Do not put の between a verb and the noun it modifies."),
                                    ("これは着物が祖母を作りました。", "This scrambles the meaning: “the kimono made grandmother.”")],
    "Plain form + noun.",
    "Japanese relative clauses come before the noun with no relative pronoun; the verb is in the plain form.",
    ["祖母が作った (that grandmother made) + 着物."])

G.sec("Cohesive devices and register")
G.tex(r"""
\begin{compare}{Function}{Informal (speech, email to a friend)}{Formal (presentation, email to an elder)}
First, next & まず、それから & 第一に、次に、最後に \\
Adding & それに、あと & さらに、また \\
Contrast & でも & しかし、一方 \\
Cause, result & だから & そのため、したがって \\
Example & たとえば & 例を挙げると \\
Concluding & とにかく & このように、以上のことから \\
Citing a source & ～って聞いた & ～によると / ～の調査では \\
\end{compare}

\subsection{Circumlocution}
When a word is missing, describe it instead of stopping: ～するときに使うもの (a thing you use when\ldots), ～みたいなもの (something like\ldots), つまり～ということです (in other words\ldots). The Q\&A language control row explicitly rewards circumlocution and paraphrase.
""")
G.q("8 Register", "In a formal project presentation, which phrase best introduces a statistic from your research?",
    "ある調査によると、……", [("なんか～らしいけど……", "Vague hearsay in casual style; the rubric rewards researched, specific information."),
                            ("友だちが言ってたんだけど……", "A friend's comment is an anecdote, not research, and the style is casual."),
                            ("とにかく……", "とにかく means “anyway”; it is informal and dismissive.")],
    "～によると = formal source citation.",
    "Presentation task execution rewards specific information from research; citing it with ～によると also shows appropriate formal register.",
    ["Choose the formal citing frame."])
G.q("8 Circumlocution", r"In the Q\&A you forget the word 楽器 (\emph{musical instrument}). The best move is to say",
    "音楽を演奏するときに使う道具です", [("（stay silent and wait for the next question）", "Silence loses task execution and fluency; keep the exchange going."),
                                       ("music thing", "Switching to English does not help comprehensibility in Japanese."),
                                       ("わかりません。次の質問をお願いします。", "Giving up leaves the prompt unanswered.")],
    "Describe it: circumlocution keeps the answer going.",
    "Language control in the Q&A rewards communication strategies such as circumlocution and paraphrasing.",
    ["～するときに使う道具 = “a tool you use when …”."])

G.sec("A study plan", "A study plan")
G.tex(r"""
\begin{compare}{When}{Do this}{Using}
Now -- January & One unit every two to three weeks: read the guide, take its checks, then its question set. Type one email or story a week and score it with the rubric. & Unit guides and question sets 1--6 \\
January -- April & Project: read the packet, pick three factors (one a perspective), research, draft the PPR keywords, time 3-minute run-throughs, rehearse Q\&A answers aloud for 40 seconds. & Part 0 \S6, Unit 3 (music) \\
April & Submit the PPR by April 30. Full timed listening and reading practice with real audio. & AP Classroom, this series \\
May & Two timed writing pairs (30 minutes each), typed with the input method; one recorded presentation a day in the last week. & Part 0 \S\S4--6 \\
\end{compare}
""")

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Part 0: Language Control Drill", r"Part 0 \textperiodcentered\ Question Set",
        abstract=r"""Every free-response task on the AP Japanese exam is scored partly on language control: a variety of grammar and a consistent, appropriate style with no errors that block meaning. The items drill the structures that most often decide that row (particles, giving and receiving, conditionals, the passive and causative, noun modification and the て-form, connectors) and the register choices that the email and presentation rubrics check. A Story Narration task with a scoring guide and a model response closes the set. All items are original.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Story: \blank\ / 8 \qquad Target: 18+ MCQ, 6+ story \qquad 40 s per item",
        short="Part 0", sub="Language Control Drill")

Q.sec("Particles")
Q.q("7 Particles", r"図書館\blank 勉強します。",
    "で", [("に", "に marks where something exists or where you go, not where an action takes place."),
           ("を", "図書館を勉強します would mean “I study the library.”"),
           ("へ", "へ marks direction of movement.")],
    "Place of an action → で.", "Use で for the place where an action happens; に for existence (図書館にいます) or destination.",
    ["勉強する is an action → 図書館で."])
Q.q("7 Particles", r"毎朝六時\blank 起きます。",
    "に", [("で", "で does not mark a point in time."),
           ("を", "を marks a direct object or a path."),
           ("が", "が marks a subject.")],
    "Specific clock time → に.", "Specific times and dates take に (六時に, 三月五日に); relative times like 毎朝 or 明日 do not.",
    ["六時 is a specific time → に."])
Q.q("7 Particles", r"どの季節\blank 一番好きですか。",
    "が", [("は", "A question word as the subject takes が, never は: だれが, どれが, どの季節が."),
           ("を", "好き describes the thing liked with が, not を, in standard Japanese."),
           ("に", "に does not mark the thing liked.")],
    "Question word subject → が.", "Question words cannot be the topic (は); as subject they take が. 好き also marks its object with が.",
    ["どの季節 is a question word phrase → が."])
Q.q("7 Particles", r"日本へ行ったこと\blank ありますか。",
    "が", [("を", "～たことがある uses が."),
           ("に", "に does not fit this pattern."),
           ("で", "で does not fit this pattern.")],
    "Experience: V-たことがある.", "Have you ever …? = V-たことがありますか.",
    ["行ったこと + が + あります."])

Q.sec("Giving and receiving")
Q.q("7 Giving", r"誕生日に、母が私にケーキを作って\blank。",
    "くれました", [("あげました", "あげる is used when the giver is the speaker or the speaker's side giving outward; here mother gives to me."),
                   ("もらいました", "With もらう the receiver is the subject: 私は母に作ってもらいました."),
                   ("さしあげました", "さしあげる is humble giving upward, from me to a superior.")],
    "Someone does something for me → てくれる.", "The giver is the subject with が; the favor comes toward the speaker.",
    ["母が … 私に … → くれました."])
Q.q("7 Giving", r"私は先生に推薦状を書いて\blank。",
    "いただきました", [("くださいました", "With くださる the giver (先生が) is the subject: 先生が書いてくださいました."),
                       ("あげました", "あげる would mean I did a favor for the teacher; and it is too plain toward a teacher."),
                       ("さしあげました", "This would mean I wrote the letter for the teacher.")],
    "I receive a favor from a superior → ていただく.", "いただく is the humble form of もらう: the speaker is the subject, the teacher is marked with に.",
    ["私は (receiver) 先生に (from the teacher) → いただきました."])

Q.sec("Conditionals")
Q.q("7 Conditionals", r"駅に着い\blank、電話してください。",
    "たら", [("と", "と cannot be followed by a request or command."),
             ("ても", "ても means “even if”; it does not fit a simple instruction."),
             ("のに", "のに expresses contrast or regret.")],
    "Once X happens, do Y → たら.", "たら marks a condition that, once it is realized, is followed by the main action; it allows requests.",
    ["着いたら (when you arrive) + 電話してください."])
Q.q("7 Conditionals", r"京都に行く\blank、秋がいいですよ。",
    "なら", [("と", "と expresses an automatic result and cannot introduce advice here."),
             ("たら", "行ったら would mean “after you have gone,” which makes no sense with advice about when to go."),
             ("ば", "行けば, 秋がいい does not give advice about the listener's plan.")],
    "Advice on the listener's topic → なら.", "なら takes up what the other person is planning and gives advice about it.",
    ["If you're going to Kyoto → autumn is good."])

Q.sec("Passive and causative")
Q.q("7 Passive", r"電車の中で、だれかに足を\blank。",
    "踏まれました", [("踏みました", "Active voice: I stepped on (someone's) foot."),
                     ("踏ませました", "Causative: I made someone step."),
                     ("踏まされました", "Causative-passive: I was made to step.")],
    "Suffering passive: V-(ら)れる.", "The passive expresses something done to the speaker, often unwelcome; the doer takes に.",
    ["だれかに (by someone) + 踏まれました (was stepped on)."])
Q.q("7 Passive", r"母は弟に部屋を掃除\blank。",
    "させました", [("されました", "Passive: the room was cleaned (by someone)."),
                   ("させられました", "Causative-passive: mother was made to clean."),
                   ("しました", "Mother cleaned it herself; 弟に would make no sense.")],
    "Make or let someone do → させる.", "Causative: the causer is the subject, the person made to act takes に.",
    ["母は (causer) 弟に (the one made to act) 掃除させました."])
Q.q("7 Passive", r"Choose the form that means ``As a child I was made to practice the piano every day.'' 子どものころ、毎日ピアノを練習\blank。",
    "させられました", [("させました", "This means I made someone practice."),
                       ("されました", "This passive would mean the piano was practiced."),
                       ("しました", "This loses the meaning “was made to.”")],
    "Was made to → causative-passive.", "V-(さ)せられる: the speaker is made to do something, often unwillingly.",
    ["練習する → させる → させられる."])

Q.sec("Noun modification and the て-form")
Q.q("7 Modification", r"Choose the form that means ``After eating breakfast, I go to school.'' 朝ご飯を食べ\blank、学校に行きます。",
    "てから", [("ながら", "ながら means “while”: eating and going at the same time."),
               ("ないで", "ないで means “without eating.”"),
               ("ても", "ても means “even if I eat.”")],
    "After → V-てから.", "V-てから stresses that one action is completed before the next.",
    ["食べてから (after eating) → 行きます."])
Q.q("7 Modification", r"窓が\blank います。（The window is open.）",
    "開いて", [("開けて", "開ける is transitive and takes を; 窓を開けています means someone is opening it."),
               ("開いた", "Before います you need the て-form."),
               ("開く", "Before います you need the て-form.")],
    "Intransitive + ている = a state.", "Intransitive verb (開く) + ている describes a resulting state: 窓が開いています.",
    ["が + intransitive 開く → 開いています."])
Q.q("7 Modification", r"これは、去年京都で\blank 写真です。",
    "撮った", [("撮りました", "Polite forms are not used inside a noun modifier."),
               ("撮ったの", "Do not put の between a verb and the noun it modifies."),
               ("撮って", "The て-form cannot modify a noun.")],
    "Plain form + noun.", "The modifying clause uses the plain form: 去年京都で撮った写真.",
    ["撮った + 写真."])

Q.sec("Connectors")
Q.q("8 Cohesion", r"一生懸命練習した\blank、試合に負けてしまった。",
    "のに", [("から", "から gives a reason; practicing hard is not a reason for losing."),
             ("ので", "ので gives a reason."),
             ("ために", "ために gives a purpose or a cause.")],
    "Despite + disappointment → のに.", "のに links an effort with an unwelcome result; てしまった adds regret.",
    ["practiced hard → lost anyway → のに."])
Q.q("8 Cohesion", r"昨日は大雨だった。\blank、試合は中止になった。",
    "そのため", [("でも", "でも introduces a contrast; the second sentence is a result."),
                 ("ところで", "ところで changes the subject (by the way)."),
                 ("それに", "それに adds another point; it does not mark a result.")],
    "Result → そのため / だから.", "そのため introduces a consequence in formal style.",
    ["heavy rain → game canceled → result."])
Q.q("8 Cohesion", "Which sentence uses a cohesive device beyond そして and でも, the kind the rubrics call effective?",
    "この活動は楽しいだけでなく、地域のお年寄りの役にも立ちます。",
    [("この活動は楽しいです。そして、役に立ちます。", "そして works, but it is the most basic link; the rubric rewards a variety of devices."),
     ("この活動は楽しいです。この活動は役に立ちます。", "Two separate sentences with no link at all."),
     ("この活動は楽しいから、役に立つから、いいです。", "Stacking から does not connect the ideas logically.")],
    "～だけでなく…も = not only … but also.", "～だけでなく…も adds a second, stronger point and shows varied cohesion.",
    ["楽しいだけでなく (not only fun) … 役にも立ちます (also useful)."])

Q.sec("Register")
Q.q("8 Register", r"In an email to a teacher: 先生、明日の発表会に\blank か。",
    "いらっしゃいます", [("来る", "The plain form is too casual and cannot end a polite question."),
                         ("参ります", "参る is humble: used for your own coming, not the teacher's."),
                         ("おります", "おる is humble: used for yourself.")],
    "Teacher's action → honorific いらっしゃる.", "Honorific forms raise the other person's action; humble forms lower your own.",
    ["先生 + come → いらっしゃいます."])
Q.q("8 Register", "Which closing suits an email to a teacher?",
    "お忙しいところすみませんが、どうぞよろしくお願いいたします。", [("じゃあね、またね！", "Casual closing for a friend."),
                                                              ("よろしく！", "Clipped and casual."),
                                                              ("バイバイ！", "Casual spoken farewell.")],
    "Teacher → polite, formal closing.", "A formal closing thanks the reader for their time and keeps the polite register.",
    ["お忙しいところ… + よろしくお願いいたします."])
Q.q("8 Register", "Which pair of sentences keeps a consistent style in an email to a host mother?",
    "先日はありがとうございました。とても楽しかったです。", [("先日はありがとうございました。とても楽しかった。", "The second sentence switches to plain style."),
                                                          ("この前はありがとう。とても楽しかったです。", "The first sentence is casual, the second polite."),
                                                          ("先日はどうも。超楽しかった！", "Casual and slangy for a host mother.")],
    "One style throughout.", "Language control penalizes mixing です・ます and plain endings; to a host mother, keep polite style.",
    ["ございました … です → both polite."])

Q.frq(kind="Story Narration", head=r"Question 3 \textperiodcentered\ Story Narration \textperiodcentered\ 8 points \textperiodcentered\ about 15 minutes",
      mins=15,
      directions=[r"\textbf{Directions.} The four pictures present a story. Imagine you are writing the story for a student magazine. Narrate a complete story as suggested by the pictures, in their order, with logical organization and relevant details."],
      panels=["朝、ケンは天気予報を見ないで、急いで家を出る。空は晴れている。",
              "放課後、学校の玄関で外を見ると、雨がたくさん降っている。ケンは傘を持っていなくて、困っている。",
              "クラスメートのゆいが「一緒に帰ろう」と言って、ケンを自分の傘に入れる。",
              "次の日、ケンはゆいにお礼のお菓子を渡している。二人とも笑っている。"],
      model=[r"ある朝、ケンさんは寝坊してしまいました。天気予報を見る時間もなく、急いで家を出ました。空はよく晴れていたので、傘はいらないと思いました。",
             r"ところが、放課後、学校の玄関で外を見ると、雨がたくさん降っていました。「どうしよう。傘を持ってこなかった……」ケンさんは困ってしまいました。家までは歩いて二十分もかかります。",
             r"そのとき、クラスメートのゆいさんが「同じ方向だから、一緒に帰ろう」と言って、ケンさんを自分の傘に入れてくれました。二人は雨の中を話しながらゆっくり歩きました。ケンさんはとてもうれしかったです。",
             r"次の日、ケンさんはお礼に、ゆいさんが好きなお菓子を買って渡しました。「昨日は本当にありがとう」と言うと、ゆいさんは「どういたしまして」と笑いました。それ以来、ケンさんは毎朝かならず天気予報を見るようになりました。"],
      rows=[("Narrative development", 3, "All four pictures, in order, with details (oversleeping, no umbrella, sharing the umbrella, the thank-you gift) and dialogue.", "Leaving out the gift in picture 4, or describing the pictures as four unconnected scenes."),
            ("Organization", 2, "A clear beginning (leaving without checking the weather), middle (the rain and the help) and end (thanks and a lesson); varied links: ある朝, ところが, そのとき, 次の日, それ以来.", "Only そして; no ending."),
            ("Language control", 3, "Varied grammar (～てしまう, ～ないで, ～てくれる, ～ながら, ～ようになる, noun modification) and a culturally relevant practice (a small thank-you gift, お礼) in consistent です・ます style.", "Mixed plain and polite endings; wrong particles; basic vocabulary only.")],
      tips=[r"ところが turns picture 2 into a surprise; ～てくれました shows the favor from Yui's side; お礼 of a small gift is a culturally relevant practice used naturally; それ以来……ようになりました gives the story an ending that shows change."])

GUIDE, QSET = G, Q
