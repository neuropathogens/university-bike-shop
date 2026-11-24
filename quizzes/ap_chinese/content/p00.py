from ap_chinese.model import Doc

STEM = "00-exam-playbook"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Part 0: The Revised Exam and the Task Playbook", r"Part 0 \textperiodcentered\ Study Guide",
        abstract=r"""This guide is written for the revised AP Chinese Language and Culture course (effective fall 2026) and its first exam, in May 2027, which runs entirely in Bluebook. It sets out what each of the four free-response tasks and ten multiple-choice task types asks you to do, how the free-response tasks are scored, and the language that moves a response up a scoring row. Read it before the unit guides: every unit guide ends with a task kit that assumes the rubrics here. Characters are simplified throughout; on the exam you may read and write in simplified or traditional. Sources: the College Board AP Chinese exam page and the Course and Exam Description (CED), effective fall 2026. Check AP Central for any later change.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 12+ \qquad Rubric rows I still mix up: \blank[10em]",
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
Unit 2 & Language and Culture: customs and celebrations, linguistics, Chinese in the world. \\
Unit 3 & Art and Creativity: architecture, artistic heritage, beauty and aesthetics, fashion and design, literature, visual and performing arts. \\
Unit 4 & Science and Technology: innovations, personal technology and communication, science in everyday life, societal impacts. \\
Unit 5 & Contemporary Life: education and career, entertainment and media, food and health, pop culture, sports and leisure, travel. \\
Unit 6 & Global Contexts: global communication, the natural world, history, policy and planning, transportation. \\
\end{terms}

\subsection{The three skill categories}
\textbf{1 Interpretive communication} (all of Section II): 1.A recognize explicit meaning (details, data points and trends); 1.B interpret meaning (main idea, audience, point of view and tone, organization, word meaning from context); 1.C synthesize and infer (connect sources, draw conclusions, infer what is implied).
\textbf{2 Interpersonal and presentational communication} (Section I): 2.A language for the purpose and context, including register; 2.B comprehensibility (circumlocution, self-correction, pronunciation, written conventions); 2.C sharing ideas, examples and sources; 2.D organization and cohesive devices.
\textbf{3 Cultural understanding}: 3.A describe, compare and reflect on cultural \emph{products}, \emph{practices} and \emph{perspectives}.

\begin{keyidea}[Products, practices, perspectives]
A \textbf{product} is a thing people make (a dish, a song, a building, an app). A \textbf{practice} is what people do (how a holiday is celebrated, how guests are greeted). A \textbf{perspective} is the value or belief that explains the product or practice (respect for elders, the wish for reunion). Two rubric rows reward linking a product or practice to the perspective behind it.
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
                   ("2 minutes", "2 minutes matches no task on the revised exam; the old Cultural Presentation lasted 2 minutes.")],
    "Q&A: four questions, each heard twice, 40 s each.",
    "The Project Q&A plays four recorded questions about your presentation and research. Each is heard twice, and you have 40 seconds to answer each.",
    ["Know the clock for each speaking task before exam day: 3 + 3 minutes for the presentation, 40 seconds per Q&A answer."])
G.q("1 Skills", r"Explaining that families gather for 团圆饭 on New Year's Eve \emph{because} reunion is highly valued connects a practice to a",
    "perspective", [("product", "A product is a made thing, such as the dumplings themselves; the value of reunion is not a thing."),
                    ("register", "Register is the level of formality of your language, not a cultural concept."),
                    ("cohesive device", "A cohesive device is a linking word such as 因此 or 不但…而且.")],
    "The value behind a practice = a perspective.",
    "Perspectives are the values, beliefs and ideas that explain why people make certain products or follow certain practices.",
    ["Gathering for the reunion dinner is a practice.", "“Reunion is highly valued” is the reason behind it: a perspective."])

G.sec("Multiple choice: the ten task types")
G.tex(r"""
Every set is built on one source. The listening sources are heard, the reading sources are read; you see the questions on screen. Each listening set has five questions. Reading has six sets: Article (0--2 sets), Article and Chart (1--2), Correspondence (1--2), Literary Text (0--2) and Promotional Material (1--2).

\begin{compare}{Task type}{The source}{What the questions target}
\multicolumn{3}{@{}l}{\textsf{\textbf{Part A: Listening (one set of each)}}}\\
Audio and Chart & A short audio report with a chart or graph. & Data points, trends, and how the audio and chart fit together. \\
Audio Report & A news-style or radio report. & Main idea, details, the speaker's purpose. \\
Conversation & Two or more people talking. & Each speaker's view, what they decide, what will happen next. \\
Instructional Guidance & Instructions or an announcement (a teacher, a guide, a store). & Steps, sequence, conditions, who must do what. \\
Presentation & A talk, lecture or podcast segment. & Organization, examples, the speaker's conclusion. \\
\multicolumn{3}{@{}l}{\textsf{\textbf{Part B: Reading}}}\\
Article & A news or feature article. & Main idea, details, point of view. \\
Article and Chart & An article with a table, chart or graph. & Reading the data, connecting it to the text. \\
Correspondence & A letter, email or message. & Purpose, requests, relationship of writer and reader. \\
Literary Text & A story or essay excerpt. & Character, feeling, implied meaning, word meaning. \\
Promotional Material & An ad, flyer or notice. & Audience, offer, conditions, dates and prices. \\
\end{compare}

\subsection{Method}
\textbf{Read the questions first} when the screen allows; they tell you what to listen or read for. \textbf{Listen for structure words} (首先, 另外, 但是, 总之) because they mark where answers sit. \textbf{Answer from the source}, not from what is generally true: a choice that is true about China but not stated or implied in the source is wrong. With charts, \textbf{read the title, units and dates} before the numbers; most chart errors are unit errors (百分之 vs.\ 人数) and year errors.

\begin{trap}
In this series the listening sets are printed as transcripts, because a PDF cannot play audio. Read each transcript once at normal speed and do not reread before answering. On the exam you will hear each source; practice with real audio (AP Classroom, Chinese podcasts and news) as well.
\end{trap}
""")
G.q("2 Task types", "Which of these is a reading task type, not a listening one?",
    "Literary Text", [("Instructional Guidance", "Instructional Guidance is a listening set: an announcement or set of instructions you hear."),
                      ("Audio and Chart", "Audio and Chart is a listening set: an audio report paired with a chart."),
                      ("Presentation", "Presentation is a listening set: a talk or lecture you hear.")],
    "Literary Text is one of the five reading types.",
    "Listening: Audio and Chart, Audio Report, Conversation, Instructional Guidance, Presentation. Reading: Article, Article and Chart, Correspondence, Literary Text, Promotional Material.",
    ["Sort the ten task types by section; only Literary Text is in reading."])
G.q("2 Method", "A reading choice says something true about Chinese culture that the passage never mentions. It is",
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
其实 & qíshí & actually (what follows corrects what came before) \\
不过 / 但是 / 可是 & búguò / dànshì / kěshì & but (the speaker's real point usually follows) \\
总之 / 总而言之 & zǒngzhī / zǒng ér yán zhī & in short (a summary: main-idea answer) \\
看来 & kànlái & it seems (an inference) \\
难怪 & nánguài & no wonder (gives a reason already implied) \\
既然 & jìrán & since (given that) \\
只好 / 不得不 & zhǐhǎo / bùdébù & have no choice but to \\
恐怕 & kǒngpà & I'm afraid that (a polite negative) \\
\end{vocab}

\begin{trap}
Tone questions turn on small words. 居然 and 竟然 (\emph{unexpectedly}) signal surprise; 终于 (\emph{finally}) signals relief after waiting; 只好 signals reluctance; 何必 (\emph{why bother}) signals disapproval.
\end{trap}
""")
G.q("3 1.B Tone", r"A speaker says: 我等了他一个小时，他\textbf{居然}说忘了。 The speaker's attitude is best described as",
    "surprised and annoyed", [("grateful", "Nothing in the sentence thanks anyone; waiting an hour for someone who forgot is not a reason for gratitude."),
                              ("relieved", "终于 would signal relief after waiting; 居然 signals that something unexpected (and here unwelcome) happened."),
                              ("indifferent", "居然 marks the event as surprising, so the speaker clearly cares.")],
    "居然 = unexpectedly: surprise, here at something unwelcome.",
    "居然 and 竟然 mark an outcome the speaker did not expect. Combined with waiting an hour, the surprise is an unhappy one.",
    ["我等了他一个小时: the speaker waited a long time.", "他居然说忘了: he unexpectedly says he forgot. Surprise plus annoyance."])
G.q("3 1.C Inference", r"A message ends: 既然你明天要考试，那我们周末再去看电影吧。 What can be inferred?",
    "The movie is postponed because of the test", [("The writer is taking a test tomorrow", "既然你明天要考试 says the reader (你) has the test, not the writer."),
                                                   ("They will see the movie tonight", "周末再去 moves the movie to the weekend."),
                                                   ("The writer does not like movies", "The writer proposes going to the movie on the weekend, so this is unsupported.")],
    "既然 (since) + 再 (later) = postponing for that reason.",
    "既然 introduces a fact both people accept; the main clause draws the conclusion. 再 with a later time means “then, at that later time.”",
    ["既然你明天要考试: since you have a test tomorrow.", "那我们周末再去: then we'll go on the weekend instead."])

G.sec("Story Narration")
G.tex(r"""
You see four pictures and write a complete story that follows them in order. Plan for about 15 of the 30 writing minutes. The CED sets no length; 200--300 characters gives room for detail and cohesion without sloppy errors.

\begin{compare}{Row (points)}{To earn the top score}{What drops you a point}
Narrative development (3) & A complete story consistent with all four pictures, with relevant details or dialogue. & Skipping or misreading a picture (2 if at least three are used; 1 if only one or two); no details. \\
Organization (2) & Clear beginning, middle and end; logical progression; effective cohesive devices. & Parts hard to follow; only 然后 and 和 as links. \\
Language control (3) & Wide vocabulary including idioms or culturally relevant expressions; a variety of grammar; no errors that impede comprehension. & Basic vocabulary and structures; errors that occasionally block meaning. \\
\end{compare}

\subsection{A five-step method}
\begin{enumerate}[leftmargin=2em]
\item \textbf{Name the characters and the setting} in one line (有一天，小明和妈妈去超市买东西。).
\item \textbf{One to three sentences per picture}, in picture order. Say what happens \emph{and} why or how people feel.
\item \textbf{Link the pictures} with time and logic words: 有一天，刚……就……，正在……的时候，突然，没想到，于是，结果，最后.
\item \textbf{Add one line of dialogue} and \textbf{one feeling} (他着急得不得了。).
\item \textbf{End with a resolution or a lesson} (从那以后，他再也不……了。). Leave two minutes to check 的/得/地, 了 and characters.
\end{enumerate}

\begin{keyidea}[Picture-to-sentence frames]
正在……的时候，突然…… \quad 一……就…… \quad 没想到…… \quad 只好…… \quad 于是…… \quad 原来…… (it turned out that) \quad 结果…… \quad 从那以后……
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
    "有一天…… 正在……的时候，突然…… 于是…… 结果……",
    [("然后…… 然后…… 然后…… 然后……", "Repeating 然后 links the events, but cohesive devices that are limited and repeated earn 1, not 2, for organization."),
     ("和…… 和…… 和…… 和……", "和 joins nouns, not clauses; it cannot link the events of a story."),
     ("因为…… 因为…… 因为…… 因为……", "Every link gives a reason; there is no sense of time, surprise or result.")],
    "Varied time, surprise and result links = effective cohesive devices.",
    "Organization rewards a clear beginning, middle and end with a variety of cohesive devices.",
    ["有一天 sets the scene; 正在……的时候，突然 introduces the problem; 于是 gives the reaction; 结果 the outcome."])

G.sec("Email Response")
G.tex(r"""
You read an email from a friend or community member and reply in Chinese. The email always contains \textbf{two requests or questions}; the top score requires clear, direct answers to both, with details or examples. Plan for about 15 minutes.

\begin{compare}{Row (points)}{To earn the top score}{What drops you a point}
Message development (3) & Clearly and directly answers both requests, with relevant details or examples. & Answering only one request (2 at most); answering without giving the requested information (1). \\
Organization (2) & Logical flow; a greeting and a closing; effective cohesive devices. & No greeting or closing; ideas in a list. \\
Language control (3) & Wide vocabulary including culturally relevant expressions; variety of grammar; consistently appropriate register; no impeding errors. & Register that shifts (你 then 您) or is wrong for the reader; frequent errors. \\
\end{compare}

\subsection{Register}
To a friend: 小明，你好！\ldots 祝你一切顺利！\quad To a teacher, an elder or a community member: 王老师，您好！ / 李阿姨，您好！\ldots 谢谢您！祝您身体健康！ / 此致敬礼！ Keep one register from start to finish; switching between 你 and 您 is penalized under language control.

\subsection{A four-part plan}
\begin{enumerate}[leftmargin=2em]
\item \textbf{Greeting and thanks}: 收到你的邮件很高兴。/ 谢谢您的来信。
\item \textbf{Request 1}: restate it in a few words, answer it, give two reasons or details (首先……其次……).
\item \textbf{Request 2}: the same (至于你问的……, as for what you asked).
\item \textbf{Closing}: an offer or a wish (如果还有问题，随时告诉我。祝你……), then your name.
\end{enumerate}
""")
G.q("5 Rubric", "An email reply answers the first question with two good reasons but never addresses the second. Message development can earn at most",
    "2 of 3", [("3 of 3", "3 requires clear, direct answers to both requests."),
               ("1 of 3", "1 is for a response that does not provide the requested information at all; this one answers one request well."),
               ("0 of 3", "0 is for an irrelevant reply or one that only restates the prompt.")],
    "One of two requests answered = 2 at most.",
    "Message development: 3 answers both requests with details; 2 addresses at least one request.",
    ["One request is fully answered, one ignored: the 2 descriptor."])
G.q("5 Register", "Your neighbor 陈奶奶 emails to ask you to tutor her grandson. Which opening and closing fit the register?",
    "陈奶奶，您好！…… 祝您身体健康！", [("陈奶奶，你好！…… 拜拜！", "你 and 拜拜 are casual; to an older community member use 您 and a polite wish."),
                                     ("嗨！…… 回头见！", "嗨 and 回头见 are what you would write to a friend your own age."),
                                     ("陈奶奶，您好！…… 下次聊，拜拜！", "The opening is right, but the closing drops to a casual register; shifting register is penalized.")],
    "Elder + community member → 您, polite wish, no shift.",
    "Language control rewards a consistently appropriate register. To an elder, use 您 throughout and close with a respectful wish such as 祝您身体健康.",
    ["Identify the reader: an older neighbor.", "Choose 您 for the greeting and keep it formal in the closing."])

G.sec("The course project: Presentation, Q\\&A and the PPR")
G.tex(r"""
The College Board releases the Course Project Packet in January of the exam year (January 2027). For 2026--27 the project looks at \textbf{music} as a lens on cultural products, practices and perspectives; you choose a topic within Chinese-speaking communities. Over about fifteen class periods you explore sources, choose \textbf{three factors to explain, at least one of them a cultural perspective}, research them, and practice.

\subsection{The Personalized Project Reference (PPR)}
The PPR is a word- or character-limited outline that you write yourself and submit in the AP Digital Portfolio by \textbf{April 30, 2027}. You get a printed copy on exam day to refer to. You may not read it aloud word for word, so write keywords, not sentences. Your teacher may advise on choosing keywords but may not write the wording or the examples. Check the project packet for the exact limit.

\subsection{Q1 Project Presentation (11 points)}
\begin{compare}{Row (points)}{To earn the top score}{What drops you a point}
Task execution (2) & At least three factors, each explained with detail and specific examples from your research. & Listing factors; explaining only one or two; relying on anecdotes or general knowledge. \\
Cultural understanding (2) & Specific examples that show how a perspective relates to a product or practice. & Examples with no link to the perspective behind them. \\
Organization (2) & Clear structure and logical progression; varied cohesive devices. & Ideas that jump; the same link word every time. \\
Language control (3) & Wide vocabulary with culturally relevant expressions; varied grammar; no impeding errors. & Basic structures; errors that block meaning. \\
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
Opening, 20 s: topic and the three factors (我的研究题目是……。我想从三个方面来介绍：……). Each factor, 45 s: claim, one researched example with its source (根据……的报道), and the perspective behind it (这反映了……的观念). Conclusion, 20 s: what the factors show together and one comparison (跟美国相比……).
\end{keyidea}
""")
G.q("6 PPR", "Which use of the Personalized Project Reference is allowed on exam day?",
    "glancing at keywords to keep the presentation organized",
    [("reading the full script aloud", "Students may refer to the PPR but may not read from it verbatim."),
     ("asking the teacher to rewrite it on exam morning", "Teachers may advise on keywords during the project but may not write its wording or examples, and it is submitted by April 30."),
     ("adding new pages of notes in the exam room", "You receive a printed copy of the PPR you submitted; you cannot add to it on exam day.")],
    "PPR = your own keyword outline; refer to it, don't read it.",
    "The PPR is a limited outline you submit by April 30 and receive in print on exam day. It supports a spoken presentation, so verbatim reading is not allowed.",
    ["Keywords, not sentences: that is what the word limit forces anyway."])
G.q("6 Rubric", "A presentation names three factors but explains only one with researched detail. For task execution it earns",
    "1 of 2", [("2 of 2", "2 requires detailed explanation of at least three factors from research."),
               ("0 of 2", "It does address the prompt with factors and one detailed explanation, which is the 1 descriptor."),
               ("3 of 3", "Task execution is out of 2, not 3.")],
    "Listing factors but explaining only one or two = 1.",
    "Task execution: 2 = at least three factors explained with detail from research; 1 = factors listed with only one or two explained in detail, or reliance on anecdote.",
    ["Three named, one explained: the 1 descriptor."])
G.q("6 Rubric", r"Which Q\&A answer best earns the cultural understanding point?",
    "在中国，很多年轻人在KTV唱歌，这反映了重视集体活动的观念；在美国，朋友聚会更常在家里。",
    [("我很喜欢听中文歌，因为很好听。", "This is a personal preference with no cultural product, practice or perspective explained."),
     ("中国有很多歌手。", "A bare fact with no comparison and no link to a perspective."),
     ("我研究了很多资料，花了很长时间。", "Describes your process, not the culture.")],
    "Comparison + perspective linked to a practice = cultural understanding 2.",
    "The Q&A cultural understanding row rewards, in at least one answer, a comparison or a reflection on how a perspective relates to a product or practice.",
    ["The KTV answer names a practice (singing together), a perspective (valuing group activities) and a comparison (the U.S.)."])

G.sec("Language control: structures that raise the score")
G.tex(r"""
Every free-response rubric has a language control row worth 3 points. The top descriptor asks for \emph{a variety of grammatical structures} with no errors that impede comprehension. Each structure below should appear naturally at least once in your practice writing.

\begin{compare}{Structure}{Pattern}{Example}
把 & S + 把 + O + V + result & 他把作业忘在家里了。 \\
被 & S + 被 (+ agent) + V + result & 我的自行车被朋友骑走了。 \\
是……的 & stresses when, where, how of a past event & 我是坐高铁来的。 \\
Result complement & V + 完/好/到/懂/错 & 你听懂了吗？我看错了。 \\
Potential complement & V + 得/不 + complement & 太远了，我们走不到。 \\
Degree complement & V + 得 + description & 她唱得非常好听。 \\
Directional complement & V + 上来/下去/起来/出来 & 他从楼上跑下来了。 \\
连……都/也 & even & 他连一个汉字都不认识。 \\
除了……以外，还/都 & besides / except & 除了中文以外，她还学日语。 \\
一……就 & as soon as & 我一到家就给你打电话。 \\
越来越 / 越……越…… & more and more & 天气越来越冷。/ 越练越好。 \\
不但……而且 & not only \ldots\ but also & 这家店不但便宜，而且很干净。 \\
虽然……但是 & although & 虽然很累，但是很开心。 \\
只要……就 / 只有……才 & as long as / only if & 只有多练习，才能说得流利。 \\
\end{compare}

\begin{trap}
的, 得 and 地 all sound \emph{de}. 的 before a noun (我的书), 得 after a verb for degree or potential (说得很快, 看得懂), 地 before a verb (认真地学习). Mixing them is the most common language control error in typed answers, because the input method offers all three.
\end{trap}
""")
G.q("7 Complements", r"Choose the correct sentence: ``She sings very well.''",
    "她唱歌唱得很好。", [("她唱歌唱的很好。", "After a verb, the degree complement uses 得, not 的."),
                      ("她很好地唱歌唱。", "This scrambles the pattern; the degree complement follows the verb: V + 得 + 很好."),
                      ("她唱歌很好得。", "得 comes between the verb and the description, never at the end.")],
    "Degree complement: (V + O) + V + 得 + description.",
    "When a verb has an object, repeat the verb before 得: 唱歌唱得很好. The description of how well comes after 得.",
    ["Verb with object: 唱歌.", "Repeat the verb + 得 + 很好."])
G.q("7 Cohesion", "Which sentence uses a cohesive device beyond 和, 但是 and 因为, the kind the rubrics call effective?",
    "这个活动不但很有意思，而且能帮助社区里的老人。",
    [("这个活动很有意思和能帮助老人。", "和 cannot join two clauses or verb phrases in Chinese; use 而且 or 也."),
     ("这个活动很有意思。这个活动能帮助老人。", "Two separate sentences with no link at all."),
     ("因为这个活动很有意思，因为能帮助老人。", "Repeating 因为 does not connect the ideas logically.")],
    "不但……而且 = a stronger, varied cohesive device.",
    "The CED notes that strong responses use cohesive devices beyond 和, 但是 and 因为. 不但……而且 adds a second, stronger point.",
    ["和 links nouns only.", "不但 A，而且 B adds B as a further point."])

G.sec("Cohesive devices and register")
G.tex(r"""
\begin{compare}{Function}{Informal (speech, email to a friend)}{Formal (presentation, email to an elder)}
First, next & 先……然后…… & 首先……其次……再次…… \\
Adding & 还有，而且 & 此外，另外，不仅如此 \\
Contrast & 可是，不过 & 然而，尽管……仍然…… \\
Cause, result & 因为……所以…… & 由于……因此……；之所以……是因为…… \\
Example & 比如说 & 例如，以……为例 \\
Concluding & 反正，总的来说 & 总之，总而言之，由此可见 \\
Citing a source & 我看到一篇文章说…… & 根据……的报道 / 据……统计 \\
\end{compare}

\subsection{Circumlocution}
When a word is missing, describe it instead of stopping: 就是那种……的东西 (it's the kind of thing that\ldots), 一种用来……的工具 (a tool used for\ldots), 意思是…… (it means\ldots). The Q\&A language control row explicitly rewards circumlocution and paraphrase.
""")
G.q("8 Register", "In a formal project presentation, which phrase best introduces a statistic from your research?",
    "据一项调查统计，……", [("我觉得好像是……", "Hedged personal opinion, not a cited source; the rubric rewards researched, specific information."),
                          ("我朋友说……", "A friend's comment is an anecdote, not research."),
                          ("反正……", "反正 means “anyway”; it is informal and dismissive.")],
    "据……统计 = formal source citation.",
    "Presentation task execution rewards specific information from research; citing it with 据……统计 or 根据……的报道 also shows appropriate formal register.",
    ["Choose the formal citing frame."])
G.q("8 Circumlocution", r"In the Q\&A you forget the word 乐器 (\emph{musical instrument}). The best move is to say",
    "就是一种用来演奏音乐的东西", [("（stay silent and wait for the next question）", "Silence loses task execution and fluency; keep the exchange going."),
                               ("music thing", "Switching to English does not help comprehensibility in Chinese."),
                               ("我不知道，下一个问题", "Giving up leaves the prompt unanswered.")],
    "Describe it: circumlocution keeps the answer going.",
    "Language control in the Q&A rewards communication strategies such as circumlocution and paraphrasing.",
    ["一种用来……的东西 = “a kind of thing used for …”."])

G.sec("A study plan", "A study plan")
G.tex(r"""
\begin{compare}{When}{Do this}{Using}
Now -- January & One unit every two to three weeks: read the guide, take its checks, then its question set. Write one email or story a week and score it with the rubric. & Unit guides and question sets 1--6 \\
January -- April & Project: read the packet, pick three factors (one a perspective), research, draft the PPR keywords, time 3-minute run-throughs, rehearse Q\&A answers aloud for 40 seconds. & Part 0 \S6, Unit 3 (music) \\
April & Submit the PPR by April 30. Full timed listening and reading practice with real audio. & AP Classroom, this series \\
May & Two timed writing pairs (30 minutes each); one recorded presentation a day in the last week. & Part 0 \S\S4--6 \\
\end{compare}
""")

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Part 0: Language Control Drill", r"Part 0 \textperiodcentered\ Question Set",
        abstract=r"""Every free-response task on the AP Chinese exam is scored partly on language control: a variety of grammar with no errors that block meaning. The items drill the structures that most often decide that row (把 and 被, aspect markers, complements, 的/得/地, comparisons, and the paired connectors) and the register choices that the email and presentation rubrics check. A Story Narration task with a scoring guide and a model response closes the set. All items are original.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Story: \blank\ / 8 \qquad Target: 20+ MCQ and 6+ story \qquad Pace: 40 s per item",
        short="Part 0", sub="Language Control Drill")

Q.sec("把 and 被")
Q.q("7 把", r"Choose the best way to say: ``Please put the books on the table.''",
    "请把书放在桌子上。", [("请放书在桌子上。", "Verb + object + 在 + place (放书在桌子上) is English word order; with both an object and a destination, use 把书放在桌子上."),
                          ("请书把放在桌子上。", "把 comes before its object: 把书, not 书把."),
                          ("请把书放。", "A 把 sentence needs a result or destination after the verb; 放 alone is incomplete.")],
    "把 + O + V + location: 把书放在桌子上.",
    "Use 把 when the action moves or changes a definite object; the verb must be followed by a result, such as a location.",
    ["Object: 书, moved by the action → 把书.", "Verb + destination: 放在桌子上."])
Q.q("7 把", r"Which sentence is correct?",
    "我已经把作业写完了。", [("我已经把作业写了完。", "The result complement attaches directly to the verb: 写完, then 了."),
                          ("我已经写把作业完了。", "把 + object must come before the verb."),
                          ("我把已经作业写完了。", "Adverbs such as 已经 go before 把, not between 把 and its object.")],
    "Adverb + 把 + O + V + result + 了.",
    "In a 把 sentence, adverbs and negation come before 把; the verb carries a result (完).",
    ["已经 → before 把.", "写完了: verb + result + 了."])
Q.q("7 被", r"``My phone was taken by my little brother.''",
    "我的手机被弟弟拿走了。", [("我的手机被弟弟拿。", "A 被 sentence also needs a result or complement after the verb (拿走了)."),
                            ("弟弟被我的手机拿走了。", "This says the brother was taken by the phone: the roles are reversed."),
                            ("我的手机把弟弟拿走了。", "把 marks the object of the action, so this says the phone took the brother.")],
    "Receiver + 被 + agent + V + result.",
    "被 marks a passive: the subject receives the action; the agent follows 被.",
    ["Receiver: 我的手机.", "被弟弟 + 拿走了."])
Q.q("7 被", r"Which sentence best describes something unfortunate that happened?",
    "我的自行车被偷了。", [("我的自行车偷了。", "Without 被, this reads as if the bicycle did the stealing."),
                          ("我的自行车是偷的。", "是……的 here would mean the bicycle was obtained by stealing."),
                          ("我把自行车偷了。", "This says I stole the bicycle.")],
    "被 often marks an unwelcome event.",
    "The 被 passive is typically used for events that are unpleasant for the subject: stolen, criticized, caught in the rain.",
    ["The bicycle suffered the action → 被偷了."])

Q.sec("Aspect: 了, 过, 着")
Q.q("7 了 过", r"``I have been to Beijing twice.''",
    "我去过北京两次。", [("我去了北京两次过。", "过 attaches to the verb, and the frequency 两次 follows the verb phrase; 过 never ends the sentence."),
                       ("我过去北京两次。", "过去 here means “go over” or “the past,” not the experiential marker."),
                       ("我去北京两次了过。", "Neither marker belongs at the end; 过 follows the verb.")],
    "V + 过 = have done (experience).",
    "过 after a verb marks a past experience; the number of times (两次) follows the verb + 过.",
    ["Experience → 去过.", "Frequency after it → 两次."])
Q.q("7 了 过", r"Fill the blank: 昨天我买\blank一件新衣服。",
    "了", [("过", "过 marks a life experience; buying a specific shirt yesterday is a completed single event, so 了."),
          ("着", "着 marks an ongoing state (门开着), not a completed purchase."),
          ("的", "的 cannot follow the verb here to mark completion.")],
    "Completed action with a quantified object → V + 了.",
    "了 after the verb marks a completed action, especially with a quantified object (一件新衣服).",
    ["Yesterday + one purchase completed → 买了一件."])
Q.q("7 着", r"``The door is open.'' (describing its state)",
    "门开着。", [("门开了过。", "过 marks experience and does not combine with 了 this way."),
                ("门在开。", "在 + V describes an action in progress (someone is opening it), not a resulting state."),
                ("门开过。", "This says the door has been opened before.")],
    "V + 着 = continuing state.",
    "着 after a verb describes a state that continues: 门开着, 他穿着红色的衣服.",
    ["We describe how the door is → 开着."])

Q.sec("Complements")
Q.q("7 Complements", r"``It's too dark; I can't see the words clearly.''",
    "太黑了，我看不清楚字。", [("太黑了，我不看清楚字。", "不 before the verb means “won't look”; inability is V + 不 + complement."),
                              ("太黑了，我没看清楚字。", "没看清楚 says I didn't see clearly on one occasion, not that I am unable to."),
                              ("太黑了，我看清楚不了字。", "The potential form inserts 不 between verb and complement: 看不清楚.")],
    "Potential complement: V + 不 + result = cannot.",
    "The potential complement V + 得/不 + result says whether a result can be achieved: 看得清楚 / 看不清楚.",
    ["Can't achieve “clear” by looking → 看不清楚."])
Q.q("7 Complements", r"Fill the blank: 老师说得太快了，我没听\blank。",
    "懂", [("得", "听得 would need a complement after it; 没 + V + result is the pattern here."),
          ("着", "着 marks a continuing state, not understanding."),
          ("过", "没听过 means “have never heard,” which does not fit a teacher speaking right now.")],
    "Result complement: 听懂 = understand by listening.",
    "Result complements say what the action achieved: 听懂, 看完, 找到. Negate with 没.",
    ["Too fast → didn't understand → 没听懂."])
Q.q("7 Complements", r"``He ran up the stairs.'' (toward the speaker, who is upstairs)",
    "他跑上楼来了。", [("他跑楼上了来。", "The place 楼 sits between 上 and 来 in a compound directional complement."),
                      ("他上来跑楼了。", "The verb comes first: 跑 + 上 + place + 来."),
                      ("他跑上去楼了。", "去 means away from the speaker; the speaker is upstairs, so 来.")],
    "V + 上 + place + 来 (toward speaker).",
    "Compound directional complements: the place goes before 来/去; 来 = toward the speaker.",
    ["Running upward → 跑上; place 楼; toward speaker → 来."])

Q.sec("的, 得, 地")
Q.q("7 的得地", r"Fill the blanks: 她认真\blank 写了一封很长\blank 信。",
    "地 / 的", [("的 / 地", "Reversed: 地 links an adverbial to a verb (认真地写); 的 links a modifier to a noun (很长的信)."),
               ("得 / 的", "得 follows a verb (写得很认真), not an adverbial before it."),
               ("的 / 得", "得 never comes between an adjective and a noun.")],
    "地 before a verb; 的 before a noun.",
    "Adjective + 地 + verb describes how an action is done; modifier + 的 + noun describes a thing.",
    ["认真 + verb 写 → 地.", "很长 + noun 信 → 的."])
Q.q("7 的得地", r"Which sentence is correct?",
    "他汉字写得很漂亮。", [("他汉字写的很漂亮。", "After a verb, a description of how well uses 得."),
                         ("他汉字写地很漂亮。", "地 comes before a verb, not after it."),
                         ("他很漂亮得写汉字。", "得 follows the verb; it cannot precede it.")],
    "V + 得 + degree.",
    "Degree complements use 得 after the verb: 写得很漂亮.",
    ["The verb 写 is described → 写得."])

Q.sec("Comparisons and focus")
Q.q("7 Comparison", r"``This bookstore is much bigger than that one.''",
    "这家书店比那家大得多。", [("这家书店比那家很大。", "很 cannot modify the adjective in a 比 comparison; use 得多 or 多了 after it."),
                             ("这家书店比那家非常大。", "非常 is also not allowed before the adjective in a 比 sentence."),
                             ("这家书店大比那家得多。", "比 + compared item comes before the adjective.")],
    "A 比 B + adj + 得多.",
    "In 比 comparisons, degree is shown after the adjective (得多, 一点儿, 多了), never with 很 or 非常 before it.",
    ["比那家 + 大 + 得多."])
Q.q("7 Comparison", r"``My Chinese is not as good as my sister's.''",
    "我的中文没有姐姐的好。", [("我的中文不比姐姐的好。", "不比 means “no better than” and implies they are about the same, not that mine is worse."),
                             ("我的中文比姐姐的不好。", "Negation does not go before the adjective in a 比 sentence."),
                             ("我的中文没有好姐姐的。", "The adjective follows the compared item: 没有 + B + adj.")],
    "A 没有 B (那么) + adj = A is not as … as B.",
    "没有 is the standard negative comparison: A 没有 B 好.",
    ["Not as good as → 没有 + 姐姐的 + 好."])
Q.q("7 是的", r"``I came by high-speed train.'' (stressing how)",
    "我是坐高铁来的。", [("我坐高铁来了的。", "了 and 的 together are wrong here; 是……的 frames the detail without 了."),
                       ("我是来坐高铁。", "Missing the final 的; this sounds like “I am here to take the train.”"),
                       ("我来的是坐高铁。", "The frame is 是 + detail + verb + 的.")],
    "是 + how/when/where + V + 的 for a known past event.",
    "是……的 highlights a detail (time, place, manner) of an event already known to have happened.",
    ["The coming is known; the manner is stressed → 是坐高铁来的."])
Q.q("7 连都", r"``He didn't even drink a sip of water.''",
    "他连一口水都没喝。", [("他一口水连都没喝。", "连 goes before the emphasized item: 连一口水."),
                         ("他连一口水没都喝。", "都 comes before the negative: 都没喝."),
                         ("他都连一口水没喝。", "The order is 连 + item + 都/也 + verb.")],
    "连 + item + 都/也 + (没) V.",
    "连……都 stresses an extreme case: not even the smallest amount.",
    ["连一口水 + 都没喝."])

Q.sec("Connectors")
Q.q("8 Cohesion", r"Fill the blank: \blank 多练习，\blank 能说得流利。 (only if \ldots\ then)",
    "只有 / 才", [("只要 / 才", "只要 (as long as) pairs with 就, not 才."),
                ("只有 / 就", "只有 (only if) pairs with 才."),
                ("虽然 / 才", "虽然 (although) pairs with 但是; it is not a condition.")],
    "只有……才 = only if; 只要……就 = as long as.",
    "只有 names the one necessary condition and pairs with 才; 只要 names a sufficient condition and pairs with 就.",
    ["Necessary condition → 只有……才."])
Q.q("8 Cohesion", r"Fill the blank: \blank 外面下大雨，比赛\blank 照常进行。",
    "尽管 / 仍然", [("因为 / 所以", "Heavy rain is not a reason the game goes ahead as usual; the relation is concession."),
                  ("如果 / 就", "如果 makes it hypothetical; the rain is actually falling."),
                  ("不但 / 而且", "不但……而且 adds a stronger point; rain and the game going ahead contrast.")],
    "尽管 A，仍然 B = even though A, still B.",
    "尽管……仍然 (or 还是) is a formal concession pair, a step up from 虽然……但是.",
    ["Rain vs. game goes ahead → concession."])
Q.q("8 Cohesion", r"Fill the blank: 我\blank 喜欢这家餐厅，\blank 因为菜好吃，\blank 因为服务很好。",
    "之所以 / 是 / 也是", [("因为 / 所以 / 也", "所以 introduces a result, but the reasons come second in this sentence."),
                         ("虽然 / 但是 / 也", "These are concession words, but the sentence gives reasons."),
                         ("不但 / 而且 / 还", "不但……而且 adds points but cannot frame “because A and because B.”")],
    "之所以 [result]，是因为 [reason].",
    "之所以 A，是因为 B puts the result first and the reason second, a formal way to explain.",
    ["Result: 我喜欢这家餐厅.", "Reasons: 是因为……，也是因为……."])
Q.q("8 Cohesion", r"Which sentence best concludes a presentation?",
    "总而言之，音乐不仅是娱乐，也反映了人们的价值观。",
    [("还有，音乐是娱乐。", "还有 adds another point; it does not conclude."),
     ("比如说，我喜欢听音乐。", "比如说 introduces an example."),
     ("然后，我们来看第二个方面。", "然后 moves to the next point; it is a transition, not a conclusion.")],
    "总而言之 = in conclusion.",
    "Formal concluding devices (总之, 总而言之, 由此可见) signal the end of an argument and score as effective cohesion.",
    ["Look for the concluding device and a summarizing claim."])

Q.sec("Register")
Q.q("8 Register", r"Replying to an email from your teacher 李老师, which sentence keeps the right register?",
    "谢谢您的建议，我会认真考虑的。", [("谢啦，我想想。", "谢啦 is slangy; to a teacher, use 谢谢您."),
                                    ("你的建议还行吧。", "你 and 还行 are too casual and slightly dismissive."),
                                    ("OK，我知道了，拜拜。", "Mixing English and 拜拜 is informal.")],
    "Teacher → 您 + polite verbs.",
    "Language control in the email rubric requires a consistently appropriate register.",
    ["Reader is a teacher → 您, 谢谢, 认真考虑."])
Q.q("8 Register", r"Which closing suits an email to a friend your age?",
    "有空再聊，祝你考试顺利！", [("此致敬礼！", "此致敬礼 is a formal letter closing for teachers and officials."),
                              ("祝您身体健康，万事如意！", "您 and this formal wish suit an elder, not a classmate."),
                              ("敬请回复。", "敬请 (respectfully request) is formal correspondence language.")],
    "Friend → 你 + friendly wish.",
    "To a friend, a warm informal closing with 你 fits; formal closings would shift register.",
    ["Peer → informal: 有空再聊，祝你……"])

Q.frq(kind="Story Narration", head=r"Question 3 \textperiodcentered\ Story Narration \textperiodcentered\ 8 points \textperiodcentered\ about 15 minutes",
      mins=15,
      directions=[r"\textbf{Directions.} The four pictures present a story. Imagine you are writing the story for a student magazine. Narrate a complete story as suggested by the pictures, in their order, with logical organization and relevant details."],
      panels=["小明背着书包，站在公共汽车站，看着手表，很着急。远处一辆公共汽车开走了。",
              "小明在路边看见一位老奶奶，她提着很多东西，东西掉了一地。",
              "小明帮老奶奶把东西捡起来，送她过马路。",
              "小明跑进教室，老师站在门口。老师手里拿着一封感谢信，笑着看他。"],
      model=[r"星期一早上，小明起晚了。他背着书包跑到车站的时候，公共汽车刚刚开走。他看了看手表，着急得不得了：``完了，第一节课就要考试了！''",
             r"正在他不知道怎么办的时候，他突然看见路边有一位老奶奶。老奶奶提着很多东西，一不小心，苹果和鸡蛋掉了一地。",
             r"小明想：``考试虽然重要，但是帮助别人更重要。''于是他马上跑过去，帮老奶奶把东西一个一个捡起来，然后又扶着她慢慢地过了马路。老奶奶拉着他的手说：``好孩子，谢谢你！''",
             r"等小明跑到学校的时候，已经迟到了二十分钟。他低着头走进教室，以为老师一定会批评他。没想到，老师笑着拿出一封信，原来是老奶奶的孙子刚刚给学校打电话，说要感谢一位穿校服的学生。老师说：``小明，考试你可以下午补考。今天你给大家上了最好的一课。''从那以后，小明每天都早起十分钟，可是他也一直记得：助人为乐，比什么都重要。"],
      rows=[("Narrative development", 3, "All four pictures, in order, with details (the watch, the spilled food, crossing the street, the letter) and dialogue.", "Leaving out the letter in picture 4, or telling the pictures as four unconnected descriptions."),
            ("Organization", 2, "A clear beginning (missed bus), middle (helping) and end (the surprise); varied links: 的时候，正在……的时候，突然，于是，然后，没想到，原来，从那以后.", "Only 然后; no ending."),
            ("Language control", 3, "Varied grammar (把, 得, 着, potential and result complements, 虽然……但是, 以为) and a culturally relevant expression (助人为乐).", "的/得/地 confusion; missing 了; basic vocabulary only.")],
      tips=[r"The model uses 没想到 and 原来 to turn picture 4 into a twist, which is what makes the ending feel complete. 以为 (wrongly thought) sets up the surprise. 助人为乐 (to find joy in helping others) is a culturally relevant expression used naturally, not tacked on."])

GUIDE, QSET = G, Q
