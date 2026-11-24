from ap_wl.model import Doc

STEM = "02-language-culture"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 2: Language and Culture", r"Unit 2 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 2 asks how language and customs express identity, how traditions are kept and changed, and how Japanese lives in communities around the world. Its recommended contexts are customs and celebrations, linguistics, and Japanese in the world. This guide gives the seasonal events most often tested (New Year, Setsubun, Hinamatsuri, Children's Day, Tanabata, Obon), the three writing systems, loanwords and made-in-Japan English, dialects, Nikkei communities from Hawaii to Brazil, the basics of keigo and hearsay, and a Story Narration kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Events I can explain: \blank[10em]",
        short="Unit 2", sub="Language and Culture")

G.sec("Celebrations and seasonal events")
G.tex(r"""
\begin{vocab}
お正月（しょうがつ） & New Year & the biggest family holiday \\
初詣（はつもうで） & first shrine or temple visit of the year & \\
お年玉（おとしだま） & New Year money for children & in small decorated envelopes \\
年賀状（ねんがじょう） & New Year's card & delivered on January 1 \\
節分（せつぶん） & Setsubun, February 3 & throwing beans: 鬼は外、福は内 \\
ひな祭り & Girls' Day, March 3 & dolls displayed for daughters' health \\
こどもの日 & Children's Day, May 5 & carp streamers (こいのぼり) \\
七夕（たなばた） & Star Festival, July 7 & wishes written on paper strips \\
お盆（ぼん） & Obon, mid-August & ancestors' spirits are welcomed home; Bon dances \\
\end{vocab}

\begin{compare}{Event}{Practice}{Perspective often cited}
年賀状 & sending cards to friends, relatives, teachers and colleagues & keeping relationships alive and starting the year with good wishes \\
お盆 & returning to one's hometown, visiting family graves & honoring ancestors; family continuity \\
七夕 & writing wishes on strips of paper and hanging them on bamboo & hope, effort toward a goal \\
\end{compare}
""")
G.q("1 Events", r"What is お年玉?",
    "money given to children at New Year", [("a New Year's card", "That is 年賀状."),
                                            ("the first shrine visit of the year", "That is 初詣."),
                                            ("a special New Year dish", "New Year dishes are おせち料理.")],
    "お年玉 = New Year money.", "Children receive お年玉 from parents, grandparents and relatives in small envelopes.",
    ["お年玉 → money for children."])
G.q("1 Events", r"During お盆 many people travel to their hometowns and visit family graves. Which perspective does this practice most directly reflect?",
    "Honoring ancestors and keeping family ties across generations.", [("Summer vacation is for traveling abroad.", "The practice centers on the hometown."),
                                                                       ("Graves should be moved to big cities.", "No."),
                                                                       ("Only grandparents should remember ancestors.", "Whole families take part.")],
    "お盆 ↔ ancestors and family.", "Practice (returning home, visiting graves) ↔ perspective (respect for ancestors, family continuity).",
    ["お盆 → ancestors' spirits welcomed home."])
G.q("1 Events", r"On which day do people throw beans and shout 鬼は外、福は内?",
    "節分", [("ひな祭り", "Girls' Day: dolls, March 3."),
            ("七夕", "Star Festival: wishes on bamboo, July 7."),
            ("こどもの日", "Children's Day: carp streamers, May 5.")],
    "節分 → 豆まき.", "On Setsubun (February 3) families throw roasted beans to drive out demons and invite good fortune.",
    ["鬼は外 (demons out), 福は内 (fortune in)."])

G.sec("Writing and words")
G.tex(r"""
\begin{vocab}
ひらがな & hiragana & grammar endings, native words \\
カタカナ & katakana & loanwords, foreign names, emphasis, sounds \\
漢字（かんじ） & kanji & 2,136 常用漢字 for general use \\
外来語（がいらいご） & loanword & テレビ, パン (from Portuguese) \\
和製英語（わせいえいご） & made-in-Japan English & サラリーマン (office worker), ガソリンスタンド (gas station) \\
方言（ほうげん） & dialect & 関西弁: めっちゃ, あかん, おおきに \\
標準語（ひょうじゅんご） & standard Japanese & based on Tokyo speech \\
\end{vocab}

\textbf{Three scripts in one sentence.} 私はアメリカから来ました uses kanji (私, 来), hiragana (は, から, ました) and katakana (アメリカ). Writers choose among them for meaning, clarity and tone: katakana can make a word feel modern or emphatic.

\begin{trap}
和製英語 words look English but are not used that way in English: a ノートパソコン is a laptop, a マンション is a condominium, and a クレーム is a complaint, not a claim.
\end{trap}
""")
G.q("2 Writing", r"Which script is normally used to write loanwords such as コンピューター?",
    "katakana", [("hiragana", "Hiragana is used for grammatical endings and native words."),
                 ("kanji", "Kanji are used for native and Chinese-derived words."),
                 ("romaji", "Romaji (Latin letters) is not the normal script for loanwords.")],
    "Loanwords → katakana.", "Katakana marks foreign loanwords, foreign names and sound effects.",
    ["コンピューター is written in katakana."])
G.q("2 Writing", r"A Japanese friend says her father is a サラリーマン. What does he most likely do?",
    "He works for a company as an office employee.", [("He sells salads.", "A sound-based misreading."),
                                                     ("He is paid only in salt.", "A false etymology."),
                                                     ("He is a professional athlete.", "No.")],
    "和製英語: salary + man.", "サラリーマン is made-in-Japan English for a salaried company employee.",
    ["salary + man → office worker."])

G.sec("Japanese in the world")
G.tex(r"""
\begin{compare}{Place}{History}{Today}
Hawaii & large-scale immigration of plantation workers from 1885 & Japanese words in Hawaii English (\emph{bento}, \emph{shoyu}) \\
Brazil & the ship Kasato Maru brought the first immigrants in 1908 & the largest Japanese-descended community outside Japan \\
United States mainland & immigration from the late 1800s; wartime incarceration of Japanese Americans (1942--45) & Little Tokyo in Los Angeles, Japantown in San Francisco \\
Worldwide & & millions of learners of Japanese; anime and manga spread words like \emph{emoji}, \emph{karaoke}, \emph{kawaii} \\
\end{compare}

\textbf{日系人 (Nikkei)} are emigrants from Japan and their descendants. Many communities keep festivals such as Obon dances and New Year mochi-pounding, sometimes long after the language has faded in daily use.
""")
G.q("3 World", r"Where is the largest Japanese-descended community outside Japan?",
    "Brazil", [("Hawaii", "Hawaii has a large Nikkei community, but Brazil's is larger."),
               ("Germany", "No."),
               ("Australia", "No.")],
    "Brazil, from 1908.", "Immigration to Brazil began with the Kasato Maru in 1908.",
    ["笠戸丸 (Kasato Maru), 1908 → Brazil."])
G.q("3 World", r"Which English word came from Japanese and spread worldwide through phones and texting?",
    "emoji", [("emotion", "Emotion is Latin-derived; emoji is not related to it."),
              ("tycoon", "Tycoon does come from Japanese (大君) but spread much earlier, not through phones."),
              ("typhoon", "Typhoon has a different, older history.")],
    "絵 (picture) + 文字 (character).", "Emoji were created for Japanese mobile phones in the late 1990s.",
    ["絵文字 → emoji."])

G.sec("Structures: keigo basics and hearsay")
G.tex(r"""
\begin{compare}{Type}{Use}{Examples}
尊敬語 (honorific) & raises the other person's action & 言う→おっしゃる, 行く/来る/いる→いらっしゃる, 食べる→召し上がる, 見る→ご覧になる \\
謙譲語 (humble) & lowers your own action toward the other person & 言う→申す, 行く/来る→参る, 訪ねる→伺う, もらう→いただく \\
丁寧語 (polite) & です・ます & 行きます, 学生です \\
Hearsay ～そうだ & I heard that (plain form + そうだ) & 明日は雨が降るそうです。 \\
Appearance ～そうだ & looks like (stem + そうだ) & 雨が降りそうです。おいしそうです。 \\
～らしい & apparently, it seems (from what I hear or see) & 先生は来週日本へ帰るらしいです。 \\
\end{compare}

\begin{trap}
降るそうです (I heard it will rain) and 降りそうです (it looks like it's about to rain) differ only in the verb form before そう. Listening questions often test this difference.
\end{trap}
""")
G.q("4 Keigo", r"Which is the honorific (尊敬語) form of 言う, used for a teacher's speech?",
    "おっしゃる", [("申す", "申す is humble: for your own speech."),
                  ("言われる", "This is the passive (or a lighter honorific), not the standard honorific."),
                  ("言います", "Polite only, not honorific.")],
    "言う → おっしゃる.", "Honorifics raise the other person's action: 先生がおっしゃいました.",
    ["Teacher's action → 尊敬語 → おっしゃる."])
G.q("4 Hearsay", r"A friend says 明日は雪が降るそうです。 What does she mean?",
    "She heard that it will snow tomorrow.", [("It looks like it is about to snow now.", "That would be 雪が降りそうです (stem + そう)."),
                                             ("She wants it to snow tomorrow.", "That would be 降ってほしい."),
                                             ("It never snows here.", "No.")],
    "Plain form + そうだ = hearsay.", "Dictionary form 降る + そう reports information heard from someone else.",
    ["降る (plain) + そうです → I heard."])

G.sec("Task kit: the Story Narration")
G.tex(r"""
Unit 2 stories often happen at a festival, a shrine, a New Year visit or a homestay. Two things lift them: \textbf{consistent past-tense narration} and \textbf{culturally relevant expressions}, including onomatopoeia.

\begin{compare}{Purpose}{Expressions}{Example}
Time & ある日、その日、次の日、～とき & お祭りの日、二人は浴衣を着て出かけました。 \\
Surprise & ところが、急に、～と（discovery） & 家に帰ると、財布がありませんでした。 \\
Feeling & ドキドキする、ワクワクする、ほっとする、びっくりする & 財布が見つかって、ほっとしました。 \\
Sounds and manner & ザーザー（heavy rain）、キラキラ（sparkling）、ぺこりと（a quick bow） & 雨がザーザー降っていました。 \\
Cultural courtesy & お礼を言う、頭を下げる、おじぎをする & マイクさんは何度も頭を下げました。 \\
\end{compare}

\begin{trap}
Keep the narration in one tense and one style. A story that slides from 行きました into 行く and back reads as careless; dialogue in quotation marks 「」 may use plain style.
\end{trap}
""")
G.q("5 Story", r"Which sentence uses an onomatopoeic expression correctly?",
    "雨がザーザー降っていたので、ケンさんはお寺で雨宿りをしました。", [("雨がキラキラ降っていたので、雨宿りをしました。", "キラキラ means sparkling, not heavy rain."),
                                                                  ("雨がペコペコ降っていたので、雨宿りをしました。", "ペコペコ describes hunger or bowing repeatedly."),
                                                                  ("雨がワクワク降っていたので、雨宿りをしました。", "ワクワク describes excitement.")],
    "ザーザー = pouring rain.", "Onomatopoeia are culturally relevant expressions the language row rewards when used accurately.",
    ["ザーザー → heavy rain."])
G.q("5 Story", r"Which ending best gives a story a resolution?",
    "それ以来、マイクさんは日本の人の親切を忘れたことがありません。", [("そして、マイクさんは財布を落としました。", "This introduces a problem, not a resolution."),
                                                                  ("マイクさんは浴衣を着ます。", "Present tense, and no resolution."),
                                                                  ("お祭りは毎年あります。", "A general fact, not an ending to the story.")],
    "それ以来 + lasting change.", "A strong ending shows what changed or what the character learned.",
    ["それ以来 (ever since) → resolution."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 2: Language and Culture: Question Set", r"Unit 2 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (a Presentation and an Audio and Chart for listening, a Literary Text and an Article for reading) on made-in-Japan English, a New Year memory, the Kansai dialect and who takes part in seasonal events, followed by a Story Narration (8 points) with a scoring guide and a model story. Questions are in English, as on the exam; listening sources are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 15 minutes for the story.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Story: \blank\ / 8 \qquad Target: 15+ MCQ and 6+ story",
        short="Unit 2", sub="Language and Culture")

Q.sec("Listening: Presentation")
Q.src(r"Listening 1 \textperiodcentered\ Presentation (transcript) \textperiodcentered\ 「和製英語の話」", [
    r"（先生）みなさん、「ノートパソコン」「ペットボトル」「サラリーマン」は英語だと思いますか。実は、どれも英語を話す人には通じないことが多いんです。こういう言葉を「和製英語」と言います。",
    r"（先生）和製英語は、英語の言葉を組み合わせたり、短くしたりして、日本で作られました。たとえば「パソコン」は「パーソナル・コンピューター」を短くした言葉です。",
    r"（先生）どうして和製英語が多いのでしょうか。一つの理由は、新しい物や考え方が入ってきたとき、カタカナの言葉のほうが新しくておしゃれに聞こえるからです。",
    r"（先生）ですから、留学するときは気をつけてください。でも、和製英語は間違いではありません。日本人が外国の言葉を自分たちの生活に合わせて使ってきた、創造的な日本語なんです。",
], 5)
Q.q("1.B.1 Main idea", "What is the main topic of the presentation?",
    "Japanese words made from English that English speakers may not understand", [("how to learn English vocabulary quickly", "No."),
                                                                                    ("the history of computers in Japan", "Computers are only an example."),
                                                                                    ("mistakes that Japanese students make in English class", "She says these words are not mistakes.")],
    "和製英語.", "Main idea (1.B.1): introduced and named in the first paragraph.",
    ["こういう言葉を「和製英語」と言います."])
Q.q("1.A.1 Detail", r"According to the teacher, how was the word パソコン made?",
    "by shortening the English words personal computer", [("by translating a Chinese word", "No."),
                                                         ("by combining two Japanese words", "No."),
                                                         ("by borrowing it from French", "No.")],
    "短くした.", "Detail (1.A.1).",
    ["「パーソナル・コンピューター」を短くした言葉."])
Q.q("1.C.3 Inference", "Why, according to the teacher, are katakana words often chosen for new things?",
    "They sound new and stylish.", [("They are shorter than all kanji words.", "Not her reason."),
                                    ("They are required by law.", "No."),
                                    ("Older people prefer them.", "Not stated.")],
    "新しくておしゃれに聞こえる.", "Detail/inference: her stated reason.",
    ["カタカナの言葉のほうが新しくておしゃれに聞こえる."])
Q.q("1.B.4 Organization", "How is the presentation organized?",
    "It asks a question, defines a term, gives a reason, then draws a conclusion.", [("It tells a personal story about studying abroad.", "No story."),
                                                                                     ("It compares Japanese and Chinese.", "No comparison."),
                                                                                     ("It lists rules for using katakana.", "No list of rules.")],
    "Question → definition → reason → conclusion.", "Organization (1.B.4): たとえば, どうして, ですから mark the steps.",
    ["…と思いますか → …と言います → どうして → ですから."])
Q.q("1.B.3 Point of view", r"What is the teacher's attitude toward 和製英語?",
    "She sees it as a creative part of Japanese.", [("She thinks it should be eliminated.", "She says it is not a mistake."),
                                                    ("She is embarrassed by it.", "No."),
                                                    ("She thinks only young people use it.", "Not stated.")],
    "創造的な日本語.", "Point of view (1.B.3): でも … 間違いではありません.",
    ["間違いではありません … 創造的な日本語なんです."])

Q.sec("Reading: Literary Text")
Q.src(r"Reading 1 \textperiodcentered\ Literary Text \textperiodcentered\ 「おせちと大吉」（短い物語）", [
    r"毎年、大みそかになると、祖母の台所は朝から忙しかった。黒豆、だて巻き、えび。祖母は一つ一つの料理の意味を教えてくれた。「黒豆は、まめに働けるように。えびは、腰が曲がるまで長生きできるように。」",
    r"元日の朝、家族みんなでおせちを食べたあと、近くの神社へ初詣に行った。私はおみくじを引いた。「凶」だった。泣きそうになった私に、祖母は笑って言った。「凶が出たら、あとはよくなるだけだよ。」",
    r"祖母がいなくなって五年になる。今年、私は初めて一人でおせちを作った。黒豆は少し硬かった。でも、娘に料理の意味を説明しながら、私は祖母の声を聞いているような気がした。",
], 5)
Q.q("1.A.1 Detail", r"According to the grandmother, what does the shrimp in おせち stand for?",
    "a long life", [("hard work", "That is the black beans (まめに働く)."),
                    ("good grades", "Not mentioned."),
                    ("a rich harvest", "Not mentioned.")],
    "えび → 長生き.", "Detail (1.A.1): the bent back of the shrimp is like an old person's.",
    ["えびは、腰が曲がるまで長生きできるように."])
Q.q("1.B.3 Tone", r"How did the grandmother respond when the narrator drew 凶 (bad luck)?",
    "She reassured her with humor.", [("She scolded her.", "She laughed."),
                                      ("She cried too.", "The narrator almost cried, not the grandmother."),
                                      ("She told her to draw again until she got good luck.", "Not stated.")],
    "笑って … よくなるだけだよ.", "Tone (1.B.3): optimism and warmth.",
    ["凶が出たら、あとはよくなるだけだよ."])
Q.q("1.C.3 Inference", "What does the final paragraph suggest?",
    "The narrator is passing on her grandmother's tradition to her own daughter.", [("The narrator has stopped making New Year food.", "She made it this year."),
                                                                                   ("The grandmother is visiting this year.", "She died five years ago."),
                                                                                   ("The daughter cooked the meal alone.", "The narrator cooked it.")],
    "娘に料理の意味を説明しながら.", "Inference (1.C.3): the tradition continues across generations.",
    ["初めて一人でおせちを作った … 娘に … 説明しながら."])
Q.q("1.B.5 Word meaning", r"In the story, 祖母がいなくなって五年になる most likely means",
    "it has been five years since the grandmother died", [("the grandmother moved away five years ago", "In context (her voice, memory), いなくなる is a gentle way to say she died."),
                                                         ("the grandmother is five years old", "No."),
                                                         ("the grandmother will leave in five years", "The tense is past.")],
    "A softened expression for death.", "Word meaning (1.B.5): Japanese often uses indirect expressions such as いなくなる or 亡くなる.",
    ["…声を聞いているような気がした → she is gone."])
Q.q("1.C.2 Conclusion", r"Why does the narrator feel she can hear her grandmother's voice?",
    "Explaining the dishes' meanings repeats what her grandmother once told her.", [("Her grandmother called her on the phone.", "No."),
                                                                                    ("Her daughter sounds like the grandmother.", "Not stated."),
                                                                                    ("She was listening to a recording.", "No.")],
    "Same words, new generation.", "Conclusions (1.C.2): the explanation echoes paragraph 1.",
    ["祖母は … 意味を教えてくれた ↔ 娘に料理の意味を説明しながら."])

Q.sec("Reading: Article")
Q.src(r"Reading 2 \textperiodcentered\ Article \textperiodcentered\ 「関西弁は元気？」", [
    r"「めっちゃ」「あかん」「ほんま」。テレビのお笑い番組の影響で、関西弁の言葉は全国で知られるようになった。東京の高校生でも「めっちゃおいしい」と言う人は多い。",
    r"一方で、大阪の若者の中には、就職の面接では標準語を使う人も多い。「関西弁はフレンドリーだけど、面接ではまじめに見られたいから」と大学生の田中さんは言う。",
    r"言語学者の小林さんは、「方言はなくなっていません。使う場面が変わっただけです。家族や友だちと話すときの方言は、その人がどこから来たかを表す大切なアイデンティティです」と話す。",
], 5)
Q.q("1.A.1 Detail", "How did Kansai words spread across Japan, according to the article?",
    "through television comedy programs", [("through school textbooks", "Not mentioned."),
                                           ("through government campaigns", "Not mentioned."),
                                           ("through business meetings", "Business settings are where some avoid the dialect.")],
    "お笑い番組の影響.", "Detail (1.A.1).",
    ["テレビのお笑い番組の影響で…全国で知られるようになった."])
Q.q("1.C.3 Inference", "Why does Ms. Tanaka use standard Japanese in job interviews?",
    "She wants to make a serious impression.", [("She cannot speak Kansai dialect.", "She is from Osaka."),
                                                ("Interviews are held in Tokyo only.", "Not stated."),
                                                ("Kansai dialect is forbidden by law.", "No.")],
    "まじめに見られたい.", "Inference (1.C.3): register choice depends on the situation.",
    ["面接ではまじめに見られたいから."])
Q.q("1.B.3 Point of view", "What is Mr. Kobayashi's view of dialects?",
    "They have not disappeared; they are used in different situations and express identity.", [("They are disappearing quickly.", "He says the opposite."),
                                                                                                ("They should be replaced by standard Japanese.", "No."),
                                                                                                ("They are used only on television.", "No.")],
    "なくなっていません / アイデンティティ.", "Point of view (1.B.3).",
    ["方言はなくなっていません。使う場面が変わっただけです."])
Q.q("1.B.4 Organization", r"What is the function of 一方で at the start of the second paragraph?",
    "It introduces a contrasting situation.", [("It gives an example of the first paragraph.", "It introduces a contrast."),
                                              ("It summarizes the article.", "No."),
                                              ("It changes the topic completely.", "Same topic.")],
    "一方で = on the other hand.", "Organization (1.B.4): spreading nationwide vs. avoided in interviews.",
    ["全国で使われる ↔ 面接では標準語."])
Q.q("1.C.2 Conclusion", "Which conclusion does the article support?",
    "Speakers choose between dialect and standard Japanese depending on the situation.", [("Everyone in Japan speaks Kansai dialect now.", "Too strong."),
                                                                                          ("Standard Japanese is disappearing.", "No."),
                                                                                          ("Young people in Osaka no longer understand their dialect.", "No.")],
    "Code-switching by situation.", "Conclusions (1.C.2): interviews vs. family and friends.",
    ["使う場面が変わっただけ."])

Q.sec("Listening: Audio and Chart")
Q.src(r"Listening 2 \textperiodcentered\ Audio and Chart (transcript) \textperiodcentered\ ラジオ「年中行事アンケート」", [
    r"（アナウンサー）全国の千人に、去年どの年中行事に参加したかを聞きました。一番多かったのは初詣で、どの年代でも半分以上の人が行っています。",
    r"（アナウンサー）おもしろいのは花見です。二十代の参加が一番多く、友だちや会社の仲間と公園に集まる人が多いようです。",
    r"（アナウンサー）一方、七夕に参加した人は、子どものいる三十代と四十代で多くなっています。保育園や幼稚園で、子どもと一緒に願い事を書く家庭が多いからでしょう。",
], 5, table=(["行事", "20代", "30--40代", "60代以上"], [["初詣", "58\\%", "66\\%", "72\\%"], ["花見", "61\\%", "45\\%", "38\\%"], ["七夕", "12\\%", "34\\%", "9\\%"]]),
      note="去年参加した人の割合（架空のデータ）")
Q.q("1.A.2 Data", "According to the chart, which group took part in 初詣 the most?",
    "people aged 60 and over", [("people in their 20s", "58%."),
                                ("people in their 30s and 40s", "66%."),
                                ("All groups equally", "The numbers differ.")],
    "72%.", "Data (1.A.2): read across the 初詣 row.",
    ["58 < 66 < 72."])
Q.q("1.C.1 Connect", "Which chart figure matches the announcer's comment about 花見?",
    "61% of people in their 20s", [("72% of people 60 and over", "That is 初詣."),
                                   ("34% of people in their 30s and 40s", "That is 七夕."),
                                   ("38% of people 60 and over", "That is 花見, but not the highest group.")],
    "花見 highest in the 20s.", "Connect (1.C.1).",
    ["二十代の参加が一番多く ↔ 61%."])
Q.q("1.C.3 Inference", "Why does the announcer think 七夕 is popular with people in their 30s and 40s?",
    "Many have young children who write wishes at daycare or kindergarten.", [("They have more vacation in July.", "Not mentioned."),
                                                                             ("They grew up without 七夕.", "Not stated."),
                                                                             ("七夕 is held at companies.", "No.")],
    "子どものいる三十代と四十代.", "Inference (1.C.3): the announcer's own explanation (でしょう).",
    ["保育園や幼稚園で、子どもと一緒に願い事を書く家庭が多い."])
Q.q("1.A.1 Detail", r"According to the report, who do people in their 20s usually go to 花見 with?",
    "friends or coworkers", [("their grandparents", "Not mentioned."),
                             ("their teachers", "Not mentioned."),
                             ("alone", "No.")],
    "友だちや会社の仲間.", "Detail (1.A.1).",
    ["友だちや会社の仲間と公園に集まる."])
Q.q("1.C.2 Conclusion", "Which conclusion is supported by both the chart and the report?",
    "Participation in seasonal events depends partly on age and life stage.", [("Young people no longer take part in any events.", "61% of people in their 20s went to 花見."),
                                                                                ("七夕 is the most popular event.", "It is the least popular in the chart."),
                                                                                ("Older people never go to 花見.", "38% did.")],
    "Age and life stage matter.", "Conclusions (1.C.2): each event peaks in a different group.",
    ["初詣 → 60+, 花見 → 20s, 七夕 → 30–40s."])

Q.frq(kind="Story Narration", head=r"Question 3 \textperiodcentered\ Story Narration \textperiodcentered\ 8 points \textperiodcentered\ about 15 minutes",
      mins=15,
      directions=[r"\textbf{Directions.} The four pictures present a story. Imagine you are writing the story for a student magazine. Narrate a complete story as suggested by the pictures, in their order, with logical organization and relevant details."],
      panels=["夏祭りの日、留学生のマイクとホストブラザーのけんたが、浴衣を着て神社のお祭りに行く。",
              "マイクは金魚すくいに夢中になっている。そのとき、ポケットから財布が落ちる。",
              "帰る前に、マイクは財布がないことに気づく。二人は困った顔で交番に行く。",
              "お巡りさんがマイクに財布を渡す。中のお金はそのまま。マイクはびっくりして、頭を下げている。"],
      model=[r"ある夏の夜、留学生のマイクさんはホストブラザーのけんたさんと、近くの神社の夏祭りに行きました。二人とも、ホストマザーが用意してくれた浴衣を着ていました。神社には屋台がたくさん並んでいて、マイクさんはワクワクしました。",
             r"マイクさんが一番気に入ったのは金魚すくいでした。何度やっても金魚がすくえなくて、すっかり夢中になってしまいました。ところが、そのとき、ポケットから財布が落ちたことに、マイクさんは気づきませんでした。",
             r"帰る前にたこ焼きを買おうとすると、財布がありません。「どうしよう！　パスポートのコピーも入っているのに……」マイクさんは真っ青になりました。けんたさんは「大丈夫。交番に行ってみよう」と言って、マイクさんを近くの交番に連れて行ってくれました。",
             r"交番に着くと、お巡りさんが「これですか」と言って、財布を見せてくれました。お祭りに来ていた人が届けてくれたそうです。中のお金もカードも、そのままでした。マイクさんはびっくりして、何度も頭を下げました。それ以来、マイクさんは、落とし物を見つけたら自分もかならず交番に届けることにしています。"],
      rows=[("Narrative development", 3, "All four pictures, in order, with details (the yukata, goldfish scooping, the missing wallet, the police box, the money untouched) and dialogue.", "Leaving out the police box or the returned wallet; describing the pictures one by one with no story."),
            ("Organization", 2, "A clear beginning (the festival), middle (losing the wallet) and end (getting it back and a lesson); varied links: ある夏の夜, ところが, そのとき, ～と, それ以来.", "Only そして; no ending."),
            ("Language control", 3, "Varied grammar (～てくれる, ～てしまう, ～ことに気づく, ～ようとする, hearsay ～そうだ, ～ことにしている) and culturally relevant words (浴衣, 屋台, 金魚すくい, 交番, 頭を下げる) in consistent です・ます narration.", "Switching tense or style; wrong particles; basic vocabulary only.")],
      tips=[r"ところが and ～ことに気づきませんでした set up the problem without telling it too early; hearsay 届けてくれたそうです explains how the wallet came back; 交番 and the untouched money are culturally relevant details, and それ以来 gives the story a lesson."])

GUIDE, QSET = G, Q
