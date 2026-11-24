from ap_wl.model import Doc

STEM = "02-language-culture"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 2: Language and Culture", r"Unit 2 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 2 asks how language and customs express identity, and how German lives in several countries and many dialects. Its recommended contexts are customs and celebrations, linguistics, and German in the world. This guide gives the vocabulary of celebrations and of language itself, the traditions most often tested (Karneval and Fasnacht, Sankt Martin, Nikolaus, the Christmas market, the Oktoberfest, national days), German in Germany, Austria, Switzerland, Liechtenstein, Luxembourg, Belgium and South Tyrol, dialects and Swiss diglossia, compounds, anglicisms and false friends, \emph{man}, the passive and Konjunktiv I, and a Project Q\&A kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Traditions I can explain in 40 seconds: \blank[8em]",
        short="Unit 2", sub="Language and Culture")

G.sec("Celebrations and traditions")
G.tex(r"""
\begin{vocab}
feiern / das Fest & to celebrate / festival & \\
der Brauch / die Tradition & custom / tradition & \\
der Umzug / der Laternenumzug & parade / lantern procession & Sankt Martin, November 11 \\
der Weihnachtsmarkt & Christmas market & Glühwein, Lebkuchen \\
der Adventskalender & Advent calendar & \\
der Maibaum & maypole & Bavaria and Austria, May 1 \\
der Karneval / der Fasching / die Fasnacht & carnival (Rhineland / Bavaria and Austria / Switzerland and the southwest) & \\
das immaterielle Kulturerbe & intangible cultural heritage & \\
\end{vocab}

\begin{compare}{Tradition}{When and where}{Perspective it reflects}
Karneval / Fasching & starts November 11 at 11:11; peaks before Lent (Rosenmontag) & a time to turn the world upside down and mock authority \\
Sankt Martin & November 11; children's lantern processions & sharing: Martin cut his cloak in two for a beggar \\
Nikolaus & night of December 5--6; children put out a boot & generosity toward children \\
Oktoberfest & Munich, since 1810 (a royal wedding) & Bavarian identity and conviviality \\
Tag der Deutschen Einheit & October 3, reunification in 1990 & national unity after division \\
Bundesfeier & August 1, Switzerland & founding of the Confederation, local bonfires \\
\end{compare}
""")
G.q("1 Feste", r"Warum tragen Kinder am 11. November Laternen durch die Straßen?",
    "um an den heiligen Martin zu erinnern, der seinen Mantel mit einem Bettler teilte", [("um den Beginn des Sommers zu feiern", "November is not summer."),
                                                                                          ("um das Oktoberfest zu eröffnen", "The Oktoberfest is in Munich in September."),
                                                                                          ("um die Wiedervereinigung zu feiern", "That is October 3.")],
    "Sankt Martin → sharing the cloak.", "The lantern procession honors Saint Martin, who shared his cloak, a story about generosity.",
    ["11. November + Laternen → Sankt Martin."])
G.q("1 Feste", r"Which perspective does the Karneval tradition of mocking politicians on parade floats most directly reflect?",
    "For a few days, ordinary people may laugh at those in power.", [("Politicians should never be criticized.", "The floats do the opposite."),
                                                                    ("Carnival is only for children.", "Adults take part."),
                                                                    ("Festivals should be silent and serious.", "The opposite.")],
    "Satire floats ↔ the world upside down.", "Practice (satirical floats) ↔ perspective (temporary freedom to mock authority).",
    ["Rosenmontag floats → satire of the powerful."])
G.q("1 Feste", r"Das Oktoberfest feierte man zum ersten Mal",
    "1810, zur Hochzeit eines bayerischen Prinzen", [("1990, nach der Wiedervereinigung", "That is the Tag der Deutschen Einheit."),
                                                    ("im Mittelalter, als Erntefest der Mönche", "No."),
                                                    ("2000, für die Touristen", "No.")],
    "1810, royal wedding.", "The first Oktoberfest celebrated the wedding of Crown Prince Ludwig of Bavaria in 1810.",
    ["Oktoberfest → 1810."])

G.sec("German in the world")
G.tex(r"""
German is the most widely spoken first language in the European Union. It is official in Germany, Austria, Switzerland (one of four national languages), Liechtenstein, Luxembourg (with Luxembourgish and French) and Belgium (the German-speaking Community), and regional in South Tyrol, in Italy.

\begin{compare}{Place}{Feature}{Example}
Switzerland & diglossia: Swiss German dialects are spoken; standard German is written & \emph{Grüezi} (hello), \emph{das Velo} (bike) \\
Austria & its own standard vocabulary & \emph{Jänner} (January), \emph{Paradeiser} (tomato), \emph{Erdäpfel} (potatoes) \\
Germany & many dialects: Bairisch, Schwäbisch, Sächsisch, Plattdeutsch & \emph{Moin} (hello, north) \\
Luxembourg & three languages in daily life & \\
\end{compare}

\textbf{Perspective.} Dialect is a marker of regional identity, not a mistake. In German-speaking Switzerland, speaking dialect in every social situation, from the bank to parliament debates in some cantons, is normal and valued.
""")
G.q("2 Sprache", r"In welchem Land sagt man „Jänner“ für „Januar“ und „Paradeiser“ für „Tomate“?",
    "in Österreich", [("in der Schweiz", "Swiss German has its own words (Velo, Grüezi), but Jänner and Paradeiser are Austrian."),
                      ("in Norddeutschland", "No."),
                      ("in Luxemburg", "No.")],
    "Austrian standard German.", "Austria has its own standard vocabulary, especially for food and months.",
    ["Jänner, Paradeiser, Erdäpfel → Austria."])
G.q("2 Sprache", r"What does diglossia mean in German-speaking Switzerland?",
    "People speak Swiss German dialects but usually write standard German.", [("Everyone speaks French at home.", "French is another national language, not diglossia."),
                                                                             ("Dialects are forbidden in public.", "The opposite."),
                                                                             ("Standard German is never used.", "It is used in writing and formal contexts.")],
    "Diglossia = spoken dialect, written standard.", "Two varieties with different roles: dialect for speech, standard German for writing.",
    ["Schweizerdeutsch spoken + Hochdeutsch written."])

G.sec("Linguistics: compounds, borrowings, false friends")
G.tex(r"""
\begin{compare}{Topic}{What happens}{Examples}
Compounds & nouns join; the last part decides the gender & \emph{die Haustür} (das Haus + die Tür), \emph{der Fußballverein} \\
Anglicisms & English words in German & \emph{das Meeting}, \emph{downloaden}, \emph{cool} \\
Pseudo-anglicisms & ``English'' words English does not use this way & \emph{das Handy} (cell phone), \emph{der Beamer} (projector), \emph{das Public Viewing} \\
Spelling reform & 1996, revised 2006 & \emph{daß} → \emph{dass} \\
Gender-fair language & debated forms & \emph{Lehrer*innen}, \emph{Lehrerinnen und Lehrer}, \emph{Lehrkräfte} \\
\end{compare}

\begin{trap}[False friends]
\emph{bekommen} = to get (become: \emph{werden}); \emph{das Gift} = poison; \emph{also} = so, therefore; \emph{aktuell} = current; \emph{sensibel} = sensitive; \emph{der Chef} = boss; \emph{eventuell} = possibly.
\end{trap}
""")
G.q("3 Linguistik", r"Welches Genus hat das Kompositum „Fußballverein“?",
    "der, weil „Verein“ maskulin ist", [("das, weil „Fußball“ ein Spiel ist", "The first part does not decide the gender."),
                                        ("die, weil alle Komposita feminin sind", "No such rule."),
                                        ("das, weil alle Komposita neutral sind", "No such rule.")],
    "Last part decides.", "In compounds, the last noun decides the gender: der Verein → der Fußballverein.",
    ["…verein (der) → der Fußballverein."])
G.q("3 Linguistik", r"Ein Schüler schreibt: „Ich will Arzt bekommen.“ Was meint er wahrscheinlich?",
    "Ich will Arzt werden.", [("Ich will einen Arzt bekommen.", "Bekommen means to get, receive."),
                              ("Ich will einen Arzt anrufen.", "A different meaning: calling a doctor."),
                              ("Ich will den Arzt besuchen.", "Different meaning.")],
    "become = werden.", "Bekommen is a false friend: it means to get, not to become.",
    ["become → werden."])

G.sec("Structures: man, the passive and Konjunktiv I")
G.tex(r"""
\begin{compare}{Use}{Pattern}{Example}
man & people in general & Am Nikolaustag stellt man einen Stiefel vor die Tür. \\
Process passive & werden + participle & Der Maibaum wird am 1. Mai aufgestellt. \\
Passive in the past & wurde + participle & Das Oktoberfest wurde 1810 zum ersten Mal gefeiert. \\
Konjunktiv I & reported speech (news, articles) & Die Forscherin sagt, das Interesse \emph{sei} gestiegen. \\
\end{compare}

\begin{keyidea}[Why it matters]
\emph{Man} and the passive let you describe customs without naming who does them: \emph{Man backt Plätzchen; die Laternen werden selbst gebastelt}. Konjunktiv I appears in news-style reading and listening sources: it marks what someone \emph{said}, not what the writer claims.
\end{keyidea}
""")
G.q("4 Strukturen", r"Wählen Sie die richtige Form: Am 1. Mai \blank\ in vielen bayerischen Dörfern ein Maibaum aufgestellt.",
    "wird", [("ist", "Ist aufgestellt would describe a state; the custom is an action (process passive)."),
             ("hat", "Haben does not form the passive."),
             ("werden", "Ein Maibaum is singular.")],
    "werden + participle.", "The process passive uses werden + past participle.",
    ["ein Maibaum (singular) → wird … aufgestellt."])
G.q("4 Strukturen", r"In a news report: Die Bürgermeisterin sagt, das Fest sei ein großer Erfolg gewesen. What does sei signal?",
    "that the writer is reporting what the mayor said", [("that the festival will happen in the future", "Sei is not future."),
                                                       ("that the writer personally guarantees the claim", "Konjunktiv I distances the writer from the claim."),
                                                       ("that the sentence is a command", "No.")],
    "Konjunktiv I = reported speech.", "News uses Konjunktiv I (sei, habe, könne) to attribute statements.",
    ["sagt … sei → reported."])

G.sec("Task kit: the Project Q\\&A")
G.tex(r"""
The four recorded questions follow your presentation. You hear each twice and have 40 seconds to answer. Questions usually ask you to expand on a factor, give an example, compare with your own community, and reflect on what you learned.

\begin{compare}{Question type}{Opening}{Then}
Expand & Wie ich in meiner Präsentation gesagt habe, \ldots & add one new fact from your research \\
Example & Ein gutes Beispiel ist\ldots & say why it matters (perspective) \\
Compare & In meiner Gemeinschaft dagegen\ldots & one similarity or difference, then why \\
Reflect & Am meisten hat mich überrascht, dass\ldots & what it taught you about the culture \\
\end{compare}

\begin{keyidea}[The culture row in 40 seconds]
You need one answer with a cultural comparison \emph{or} a link between a perspective and a product or practice. Plan it before the exam: \emph{Nach dem Mauerfall feierten junge Leute in leeren Fabriken, was zeigt, wie wichtig ihnen Freiheit war; bei uns dagegen\ldots}
\end{keyidea}

\begin{trap}
Forty seconds is about 70--90 words. Answer the question in the first sentence, then support it. Watch word order after \emph{weil} and \emph{dass}: verb last.
\end{trap}
""")
G.q("5 Q&A", r"The interlocutor asks: Inwiefern ähnelt die Tradition, die Sie untersucht haben, einer Tradition in Ihrer Gemeinschaft? What does a strong answer need?",
    "a specific similarity or difference and what it shows about each culture", [("a summary of the whole presentation", "Repeating the presentation does not answer the question."),
                                                                                 ("a list of facts about the tradition only", "The question asks for a comparison."),
                                                                                 ("a description of how you did the research", "The research process is not the topic.")],
    "Compare + explain.", "A cultural comparison that explains what each practice reflects can earn the top culture score.",
    ["Similarity/difference → why → perspective."])
G.q("5 Q&A", r"About how many words fit in a 40-second Q\&A answer at a natural pace?",
    "70 to 90", [("15 to 20", "That is about one sentence, too short to be complete."),
                 ("200 to 250", "That would require very fast speech."),
                 ("400", "That is a full written essay.")],
    "40 s ≈ 70–90 words.", "At about two words per second, 40 seconds holds four to six sentences.",
    ["Plan: answer + example + why."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 2: Language and Culture: Question Set", r"Unit 2 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (a Presentation and an Audio and Chart for listening, a Literary Text and an Article for reading) on Swiss German, Saint Martin's Day, anglicisms and festivals, followed by a practice Project Q\&A on music, the 2026--27 project lens, with the 9-point scoring guide and model answers. The Q\&A questions are practice questions written for this set, not official prompts. As on the exam, questions and choices are in German; listening sources are printed as transcripts. All sources and data are original and fictional. Allow about 25 minutes for the multiple choice and 10 minutes for the Q\&A.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Q\&A: \blank\ / 9 \qquad Target: 15+ MCQ and 6+ Q\&A \qquad Pace: 75 s per item",
        short="Unit 2", sub="Language and Culture")

Q.sec("Listening: Presentation")
Q.src(r"Listening 1 \textperiodcentered\ Presentation (transcript) \textperiodcentered\ Ein Vortrag über Schweizerdeutsch", [
    r"(PROFESSORIN) Wer zum ersten Mal nach Zürich kommt und Deutsch gelernt hat, erlebt oft eine Überraschung: Man versteht fast nichts. Denn in der Deutschschweiz spricht man im Alltag Dialekt, und zwar überall, beim Bäcker, im Büro und oft sogar im Fernsehen.",
    r"(PROFESSORIN) Geschrieben wird dagegen meistens Hochdeutsch: in der Zeitung, in der Schule, in offiziellen Briefen. Sprachwissenschaftler nennen diese Arbeitsteilung zwischen zwei Varietäten „Diglossie“.",
    r"(PROFESSORIN) In den letzten Jahren hat sich etwas verändert. Junge Leute schreiben ihre Textnachrichten zunehmend im Dialekt, so wie sie sprechen. Manche Lehrkräfte befürchten, dass darunter das Hochdeutsch leidet. Viele Sprachforscher sehen darin aber vor allem ein Zeichen, wie lebendig die Dialekte sind.",
    r"(PROFESSORIN) Zusammenfassend kann man sagen: In der Schweiz ist der Dialekt kein Zeichen mangelnder Bildung, sondern ein Teil der Identität.",
], 5)
Q.q("1.B.1 Main idea", r"Was ist die Hauptaussage des Vortrags?",
    "In der Deutschschweiz ist der Dialekt ein selbstverständlicher Teil der Identität.", [("Schweizerdeutsch verschwindet langsam.", "The speaker describes vitality, not decline."),
                                                                                          ("In der Schweiz spricht niemand Hochdeutsch.", "Standard German is written and used formally."),
                                                                                          ("Dialekt ist ein Zeichen mangelnder Bildung.", "The conclusion says the opposite.")],
    "Conclusion = main idea.", "The concluding sentence (zusammenfassend…) states the main idea.",
    ["…kein Zeichen mangelnder Bildung, sondern ein Teil der Identität."])
Q.q("1.A.1 Detail", r"Wo wird laut Vortrag meistens Hochdeutsch verwendet?",
    "in der Zeitung, in der Schule und in offiziellen Briefen", [("beim Bäcker und im Büro", "There people speak dialect."),
                                                                ("in Textnachrichten junger Leute", "Young people increasingly write dialect there."),
                                                                ("nur im Fernsehen", "TV often uses dialect too.")],
    "Written standard.", "Detail (1.A.1).",
    ["Geschrieben wird … Hochdeutsch: in der Zeitung, in der Schule…"])
Q.q("1.B.5 Word meaning", r"Was bedeutet „Diglossie“ laut Vortrag?",
    "eine Arbeitsteilung zwischen zwei Sprachformen", [("ein Dialekt aus Zürich", "It names the relationship, not one dialect."),
                                                      ("ein Fehler beim Schreiben", "No."),
                                                      ("eine Schweizer Fernsehsendung", "No.")],
    "Defined in the source.", "Definitions inside the source answer word-meaning questions.",
    ["diese Arbeitsteilung zwischen zwei Varietäten → Diglossie."])
Q.q("1.B.3 Point of view", r"Wie sehen viele Sprachforscher das Schreiben im Dialekt?",
    "als Zeichen dafür, wie lebendig die Dialekte sind", [("als Gefahr für das Hochdeutsch", "That is some teachers' fear."),
                                                          ("als Mode, die bald verschwindet", "Not stated."),
                                                          ("als Problem nur für ältere Menschen", "No.")],
    "Viele Sprachforscher sehen darin aber…", "Point of view (1.B.3): separate the teachers' fear from the researchers' view.",
    ["…ein Zeichen, wie lebendig die Dialekte sind."])
Q.q("1.B.4 Organization", r"Wie beginnt die Professorin ihren Vortrag?",
    "mit einer typischen Überraschung für Besucher", [("mit einer Definition von Diglossie", "That comes in the second paragraph."),
                                                     ("mit einer Statistik über Zürich", "No statistic."),
                                                     ("mit einer Geschichte aus ihrer Kindheit", "No.")],
    "Hook: visitors understand almost nothing.", "Organization (1.B.4): a relatable experience, then the explanation (denn…).",
    ["…erlebt oft eine Überraschung."])

Q.sec("Reading: Literary Text")
Q.src(r"Reading 1 \textperiodcentered\ Literary Text \textperiodcentered\ „Die Laterne“ (Auszug aus einer Erzählung)", [
    r"Jedes Jahr im November roch die Küche meiner Großmutter nach Kleister und Weckmännern. Sie bestand darauf, dass wir die Laternen selbst bastelten, „wie früher“. In jenem Jahr war ich sieben, und meine Laterne sah aus wie ein zerdrückter Mond.",
    r"„Die ist die schönste“, sagte Oma trotzdem und zündete die Kerze darin an.",
    r"Am Abend gingen wir mit dem ganzen Kindergarten hinter dem Reiter her, der den heiligen Martin spielte. Wir sangen „Laterne, Laterne, Sonne, Mond und Sterne“, und ich hielt meinen zerdrückten Mond so hoch, wie ich konnte. Als ein Windstoß ihn umwarf und er Feuer fing, weinte ich nicht einmal. Oma nahm einfach ihre eigene Laterne und gab sie mir. Sie ging den Rest des Weges im Dunkeln und sang lauter als alle anderen.",
], 5)
Q.q("1.A.1 Detail", r"Was wollte die Großmutter jedes Jahr?",
    "dass die Kinder die Laternen selbst basteln", [("dass die Kinder Laternen im Geschäft kaufen", "She insisted they make them."),
                                                   ("dass die Familie zu Hause bleibt", "They join the procession."),
                                                   ("dass das Kind den Reiter spielt", "Someone else plays Saint Martin.")],
    "Sie bestand darauf, dass wir … selbst bastelten.", "Detail (1.A.1).",
    ["…dass wir die Laternen selbst bastelten, „wie früher“."])
Q.q("1.C.3 Inference", r"Warum sagt die Großmutter „Die ist die schönste“, obwohl die Laterne zerdrückt aussieht?",
    "um das Kind zu ermutigen und ihm Freude zu machen", [("weil sie schlecht sieht", "Nothing suggests that."),
                                                          ("weil sie die Laterne gekauft hat", "They made it themselves."),
                                                          ("weil sie das Kind verspotten will", "Her later act shows tenderness.")],
    "Encouragement.", "Inference (1.C.3): trotzdem shows she knows it is crooked and praises it anyway.",
    ["zerdrückter Mond … trotzdem → kindness."])
Q.q("1.B.5 Word meaning", r"Im Text ist ein „zerdrückter Mond“",
    "eine schiefe, eingedrückte Laterne", [("ein Gebäck aus der Küche", "The Weckmänner are the pastry."),
                                           ("der Mond am Himmel", "Figurative description of the lantern."),
                                           ("ein Lied für Kinder", "No.")],
    "Metaphor for the lantern.", "Word meaning (1.B.5): sah aus wie ein zerdrückter Mond describes the lantern.",
    ["meine Laterne sah aus wie ein zerdrückter Mond."])
Q.q("1.C.2 Conclusion", r"Wie passt die Handlung der Großmutter am Ende zur Geschichte des heiligen Martin?",
    "Wie Martin teilt sie, was sie hat, mit jemandem, der es braucht.", [("Wie Martin reitet sie auf einem Pferd.", "Literal misreading."),
                                                                          ("Sie verbietet dem Kind, weiter zu singen.", "She sings louder."),
                                                                          ("Sie kauft eine neue Laterne.", "She gives her own.")],
    "Giving her lantern = sharing the cloak.", "Conclusions (1.C.2): the ending mirrors the legend the procession celebrates.",
    ["gab sie mir … ging … im Dunkeln → sharing like Martin."])
Q.q("1.B.3 Tone", r"Welcher Ton herrscht in diesem Auszug vor?",
    "zärtlich und nostalgisch", [("tragisch", "The mishap ends warmly."),
                                 ("empört", "No anger."),
                                 ("sachlich-wissenschaftlich", "It is a personal memory.")],
    "Memory + tenderness.", "Tone (1.B.3): an affectionate childhood memory.",
    ["Oma's gesture → tender, nostalgic."])

Q.sec("Reading: Article")
Q.src(r"Reading 2 \textperiodcentered\ Article \textperiodcentered\ „Warum heißt das Handy Handy?“, Magazin Sprachwelt", [
    r"„Ich schick dir den Link per Handy, wir sehen uns beim Public Viewing.“ Für viele Deutsche ist dieser Satz völlig normal. Ein Engländer würde allerdings stutzen: Ein „Handy“ heißt bei ihm \emph{mobile phone}, und \emph{public viewing} bedeutet im Englischen etwas ganz anderes, nämlich die öffentliche Aufbahrung eines Verstorbenen.",
    r"Solche Wörter nennt man Scheinanglizismen: Sie klingen englisch, werden aber im Englischen nicht oder anders benutzt. „Sie zeigen, dass Deutsch englische Wörter nicht einfach kopiert, sondern sich aneignet und neu formt“, erklärt die Linguistin Sabine Krüger.",
    r"Nicht alle sind begeistert. Vereine zur Pflege der deutschen Sprache kritisieren das sogenannte „Denglisch“ in Werbung und Behörden. Krüger sieht das gelassener: „Sprachen haben schon immer voneinander geliehen. Problematisch wird es nur, wenn Menschen Texte nicht mehr verstehen, die sie betreffen.“",
], 5)
Q.q("1.B.1 Purpose", r"Was ist der Zweck des Artikels?",
    "zu erklären, was Scheinanglizismen sind, und verschiedene Haltungen dazu darzustellen", [("Englisch als Fremdsprache zu verkaufen", "No."),
                                                                                              ("das Wort „Handy“ zu verbieten", "No one proposes a ban."),
                                                                                              ("die Geschichte Englands zu erzählen", "No.")],
    "Explain + views.", "Purpose (1.B.1): definition, the linguist's view, critics, her response.",
    ["example → definition → views."])
Q.q("1.A.1 Detail", r"Was bedeutet „public viewing“ laut Artikel im Englischen?",
    "die öffentliche Aufbahrung eines Verstorbenen", [("das gemeinsame Ansehen eines Fußballspiels", "That is the German usage."),
                                                     ("ein Kinofilm im Park", "No."),
                                                     ("eine Kunstausstellung", "No.")],
    "English meaning: lying in state.", "Detail (1.A.1): the article contrasts the two meanings.",
    ["…bedeutet im Englischen … die öffentliche Aufbahrung…"])
Q.q("1.B.5 Word meaning", r"Im Artikel bedeutet „stutzen“",
    "kurz überrascht innehalten", [("lachen", "Not the meaning."),
                                   ("übersetzen", "No."),
                                   ("telefonieren", "No.")],
    "stutzen = to stop short, puzzled.", "Word meaning (1.B.5): an English speaker would be puzzled by the German usage.",
    ["Ein Engländer würde allerdings stutzen → puzzled."])
Q.q("1.B.3 Point of view", r"Wie steht Sabine Krüger zu Anglizismen?",
    "gelassen, solange die Menschen wichtige Texte verstehen", [("Sie will sie in der Werbung verbieten.", "That is the language societies' position."),
                                                               ("Sie hält sie für das Ende der deutschen Sprache.", "No."),
                                                               ("Sie meint, man solle nur noch Englisch sprechen.", "No.")],
    "gelassener … nur problematisch, wenn…", "Point of view (1.B.3).",
    ["Krüger sieht das gelassener … Problematisch wird es nur, wenn…"])
Q.q("1.C.2 Conclusion", r"Was kann man aus Krügers Aussage über Scheinanglizismen schließen?",
    "Deutsch formt fremde Wörter auf eigene Weise um.", [("Deutsch kopiert englische Wörter genau.", "She says it does not simply copy."),
                                                        ("Englisch übernimmt viele deutsche Wörter.", "Not discussed."),
                                                        ("Scheinanglizismen gibt es nur in Behörden.", "No.")],
    "sich aneignet und neu formt.", "Conclusions (1.C.2) from her quote.",
    ["nicht einfach kopiert, sondern … neu formt."])

Q.sec("Listening: Audio and Chart")
Q.src(r"Listening 2 \textperiodcentered\ Audio and Chart (transcript) \textperiodcentered\ „Welche Feste uns wichtig sind“, Jugendradio", [
    r"(MODERATOR) Ein Institut hat 2.000 Jugendliche in Deutschland zwischen 15 und 24 Jahren gefragt, welche Feste ihnen am meisten bedeuten. Die Ergebnisse überraschen.",
    r"(MODERATOR) Weihnachten liegt weiterhin vorne, aber Silvester hat stark aufgeholt: Vor zehn Jahren war es auf Platz vier, heute auf Platz zwei. Die Forscher vermuten, dass Jugendliche Silvester vor allem mit Freunden feiern und dabei mehr Freiheit haben als an Familienfesten.",
    r"(MODERATOR) Der Karneval dagegen hat verloren. Viele Jugendliche sagen, sie feierten ihn gern, aber vor allem dort, wo er Tradition hat, also im Rheinland.",
], 5, table=(["Fest", "2014", "2024"], [["Weihnachten", "1.", "1."], ["Silvester", "4.", "2."], ["Karneval", "2.", "3."], ["Ostern", "3.", "4."]]),
      note="Tabelle: Platz unter den wichtigsten Festen für Jugendliche (fiktive Daten).")
Q.q("1.A.2 Data", r"Was zeigt die Tabelle über die Veränderungen zwischen 2014 und 2024?",
    "Karneval und Ostern haben jeweils einen Platz verloren.", [("Silvester hat zwei Plätze verloren.", "It gained two places."),
                                                                ("Weihnachten hat einen Platz verloren.", "It stayed first."),
                                                                ("Nur Ostern hat verloren, und zwar zwei Plätze.", "Ostern lost one place, and Karneval also lost one.")],
    "Karneval 2→3, Ostern 3→4.", "Data (1.A.2): compare each row's two columns.",
    ["Two festivals each lost one place."])
Q.q("1.C.1 Connect", r"Wie erklärt der Bericht den Aufstieg von Silvester in der Tabelle?",
    "Jugendliche feiern Silvester mit Freunden und haben dabei mehr Freiheit.", [("Silvester wurde auf einen anderen Tag verlegt.", "No."),
                                                                                ("Ein neues Gesetz schreibt Feiern vor.", "No."),
                                                                                ("Es gibt weniger Feuerwerk.", "Not mentioned.")],
    "Table: 4. → 2.; audio: friends + freedom.", "Connect (1.C.1): the table shows the rise; the audio explains it.",
    ["…mit Freunden feiern und dabei mehr Freiheit haben…"])
Q.q("1.C.3 Inference", r"Was kann man über die Einstellung vieler Jugendlicher zum Karneval vermuten?",
    "Er ist ihnen vor allem in Regionen mit Karnevalstradition wichtig.", [("Sie feiern ihn überhaupt nicht.", "They say they like celebrating it."),
                                                                            ("Er ist ihr Lieblingsfest.", "It is third."),
                                                                            ("Sie feiern ihn lieber als Weihnachten.", "Weihnachten is first.")],
    "Regional tradition.", "Inference (1.C.3) from the stated reason (vor allem im Rheinland).",
    ["…vor allem dort, wo er Tradition hat."])
Q.q("1.A.1 Detail", r"Wie viele Jugendliche wurden befragt?",
    "2.000", [("15", "15–24 is the age range."),
              ("24", "15–24 is the age range."),
              ("10.000", "Not stated.")],
    "2,000.", "Detail (1.A.1): keep sample size and ages apart.",
    ["2.000 Jugendliche … zwischen 15 und 24."])
Q.q("1.B.1 Main idea", r"Was ist die zentrale Aussage des Berichts?",
    "Die Bedeutung der Feste für Jugendliche hat sich in zehn Jahren verändert.", [("Jugendliche feiern gar keine Feste mehr.", "They rank several."),
                                                                                  ("Ostern ist das wichtigste Fest.", "It is fourth."),
                                                                                  ("Freiheit spielt beim Feiern keine Rolle.", "It explains Silvester's rise.")],
    "Change over ten years.", "Main idea (1.B.1): two years compared and explained.",
    ["2014 vs. 2024 + reasons."])

Q.frq(kind="Project Q&A", head=r"Question 2 \textperiodcentered\ Project Q\&A (practice) \textperiodcentered\ 9 points \textperiodcentered\ 4 answers of 40 seconds", mins=8,
      directions=[r"Imagine that your project examined how music expresses identity in a German-speaking community, and that your presentation focused on Berlin's techno culture after the fall of the Wall (clubs opened in empty factories and bunkers in the early 1990s; in 2024 Berlin's techno culture was added to Germany's national register of intangible cultural heritage). You will hear four questions. Each is played twice; you have 40 seconds to answer each one. Answer in German."],
      prompt=[r"1. In Ihrer Präsentation haben Sie über die Clubs nach dem Mauerfall gesprochen. Warum war diese Musik für junge Berliner so wichtig?",
              r"2. Können Sie ein konkretes Beispiel geben, wie diese Kultur heute gelebt wird?",
              r"3. Gibt es in Ihrer Gemeinschaft eine Musik, die eine ähnliche Rolle spielt? Vergleichen Sie.",
              r"4. Was hat Sie bei Ihrer Recherche am meisten überrascht?"],
      model=[r"\textbf{1.} Nach dem Mauerfall gab es in Ost-Berlin viele leere Gebäude. Junge Leute aus Ost und West haben dort zum ersten Mal zusammen gefeiert. Die Musik war wichtig, weil sie ein Gefühl von Freiheit und Neuanfang ausgedrückt hat. Auf der Tanzfläche war egal, woher man kam.",
             r"\textbf{2.} Ja. Viele Clubs haben eine strenge Tür und erlauben keine Fotos. Das zeigt, dass die Besucher ihre Privatsphäre schützen wollen und dass jeder dort so sein darf, wie er ist. Seit 2024 gehört die Berliner Technokultur sogar zum immateriellen Kulturerbe Deutschlands.",
             r"\textbf{3.} In meiner Stadt, Detroit, spielt Techno eine ähnliche Rolle, denn dort ist er ja entstanden. Wie in Berlin wurde er in verlassenen Gebäuden gespielt. Der Unterschied ist, dass er in Detroit eher mit der afroamerikanischen Geschichte verbunden ist, während er in Berlin für die Wiedervereinigung steht.",
             r"\textbf{4.} Am meisten hat mich überrascht, dass eine elektronische Musik ohne Text so viel über Geschichte erzählen kann. Ich dachte, Techno sei nur Party, aber für viele Berliner ist er ein Symbol dafür, dass eine geteilte Stadt wieder zusammengewachsen ist."],
      rows=[("A Task", 2, "four relevant, complete answers that address each question", "answers that drift back to the presentation or stop after one sentence"),
            ("B Culture", 2, "in at least one answer, a cultural comparison (answer 3) or a perspective linked to a product or practice (answers 1 and 2)", "only describing the music (1 point)"),
            ("C Language", 3, "varied vocabulary and structures (verb-final clauses, passive, Konjunktiv I in answer 4)", "short, repetitive sentences"),
            ("D Fluency", 2, "natural pace and intonation, clear pronunciation, few pauses", "long silences, many restarts")],
      tips=["Each answer starts by answering the question directly.", "Answer 3 is a full cultural comparison: similarity, difference, and why.",
            "Answers 1 and 2 link practices (partying in empty buildings, no-photo rules) to perspectives (freedom, privacy).", "About 70–80 words each fits 40 seconds."],
      ask="Answer each question aloud in German (40 seconds each), jotting keywords first; then mark your answers.", lines=12)

GUIDE, QSET = G, Q
