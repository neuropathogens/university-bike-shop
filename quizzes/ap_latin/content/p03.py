from ap_wl.model import Doc

STEM = "03-pliny-ghosts-trajan-calpurnia"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 3: Pliny's Letters: Ghosts, Trajan and Calpurnia", r"Unit 3 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 3 reads Pliny's letter to Sura about ghosts (7.27), his official correspondence with the emperor Trajan about citizenship for his doctor (10.5--7) and about aqueducts (10.37, 10.90), and two letters to his wife Calpurnia (6.4, 6.7), with Teacher's Choice prose alongside. This guide sets out each letter's structure and key Latin, the contexts the exam asks about (belief in the supernatural, patronage and citizenship, provincial government and engineering, marriage and absence), the shifts of register among the letters, and a Translation kit for Pliny's prose. Latin is quoted without macrons from a public-domain text. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Latin I can cite: \blank[10em]",
        short="Unit 3", sub="Pliny's Letters: Ghosts, Trajan and Calpurnia")

G.sec("Letter 7.27: do ghosts exist?")
G.tex(r"""
\textbf{The question.} Pliny asks Sura whether he thinks ghosts (\emph{phantasmata}) are real and have their own form and power, or are empty images shaped by our fear (7.27.1). He tells three stories.

\begin{compare}{Story}{What happens}{Key Latin}
Curtius Rufus (2--3) & in Africa, a woman of superhuman size predicts his future; everything comes true & ``mulieris figura humana grandior pulchriorque'' \\
Athenodorus (4--11) & a philosopher rents a cheap haunted house in Athens, writes calmly, follows a chained ghost to the courtyard; bones are dug up and buried; the haunting ends & ``iubet sterni sibi in prima domus parte, poscit pugillares stilum lumen'' \\
Pliny's household (12--14) & a freedman and a slave boy dream that their hair is cut, and wake shorn; Pliny reads it as a sign he escaped prosecution under Domitian & ``non fui reus, futurus, si Domitianus \ldots\ diutius vixisset'' \\
\end{compare}

\textbf{Ending.} Pliny asks Sura to argue both sides if he likes, but to come down firmly on one, ``ne me suspensum incertumque dimittas''.
""")
G.q("1 Letter 7.27", r"Why does Athenodorus rent the house in Athens?",
    "He is not afraid; the low price makes him suspicious, and after learning the story he rents it all the more.", [
        ("He does not know it is haunted.", "He asks and is told everything."),
        ("The city gives it to him for free.", "He rents it."),
        ("He wants to sell it later.", "No.")],
    "immo tanto magis conducit.", "A philosopher tests the ghost with reason and calm.",
    ["quia suspecta vilitas."])
G.q("1 Letter 7.27", r"Why does Athenodorus keep writing while the chains rattle?",
    "so that his idle mind would not imagine phantoms and fears", [("to record the ghost's words", "He writes to keep his mind occupied."),
                                                                  ("to finish a letter to Pliny", "No."),
                                                                  ("because he cannot hear", "He hears the noise.")],
    "ne vacua mens … fingeret.", "Purpose clause: reason against fear.",
    ["ipse ad scribendum animum oculos manum intendit."])

G.sec("Letters to Trajan: citizenship and aqueducts")
G.tex(r"""
\begin{compare}{Letter}{Content}{Context}
10.5 & Pliny, saved from a dangerous illness by his doctor (\emph{iatraliptes}) Harpocras, asks Trajan to grant him Roman citizenship & patronage: a favor repays a debt of gratitude \\
10.6 & he thanks Trajan, then learns that an Egyptian must first receive citizenship of Alexandria & legal status in the empire; Pliny admits his mistake \\
10.7 & Trajan agrees, though he grants Alexandrian citizenship rarely, and asks for the doctor's district & the emperor's reply: brief, practical \\
10.37 & Nicomedia has wasted vast sums on two unfinished aqueducts; Pliny proposes arches of stone and brick and asks for an engineer or architect & provincial government; Roman engineering \\
10.90 & Sinope lacks water; a supply could be brought 16 miles; Pliny is testing the soft ground & public health and amenity \\
\end{compare}

\textbf{Register.} Pliny addresses Trajan as \emph{domine}, thanks his \emph{indulgentia}, and closes with flattery: the work is ``saeculo tuo \ldots\ dignissimam'' (10.37.3).
""")
G.q("2 Trajan", r"Why does Pliny ask Trajan to grant citizenship to Harpocras?",
    "to repay the doctor who cared for him through a life-threatening illness", [("because Harpocras was a famous senator", "He was an Egyptian freedman."),
                                                                                  ("because Trajan was ill", "No."),
                                                                                  ("to punish him", "No.")],
    "gratitude and patronage.", "Pliny can repay his doctor only through the emperor's kindness.",
    ["usque ad periculum vitae vexatus."])
G.q("2 Trajan", r"What does Pliny ask Trajan to send to Nicomedia?",
    "a water engineer or an architect", [("more money", "He says much money was already wasted."),
                                         ("soldiers", "No."),
                                         ("a new governor", "Pliny is the governor.")],
    "vel aquilegem vel architectum.", "So that the failure does not happen again.",
    ["ne rursus eveniat quod accidit."])

G.sec("Letters to Calpurnia: 6.4 and 6.7")
G.tex(r"""
\textbf{6.4.} Pliny regrets that his duties kept him from accompanying Calpurnia to Campania for her health; he worries about her and asks her to write once or even twice a day: ``Numquam sum magis de occupationibus meis questus''.

\textbf{6.7.} Calpurnia writes that she is deeply affected by his absence and that her only comfort is to hold his books in his place. Pliny is pleased, and rereads her letters as if new; yet they only inflame his longing: ``licet hoc ita me delectet ut torqueat''.

\begin{compare}{Feature}{Example}{Effect}
Paradox & ``ita me delectet ut torqueat'' & love as pleasure and pain, an elegiac motif \\
Exchange of letters & her books, his letters to her & the letter as substitute for presence \\
Intimate register & short sentences, exclamation, ``Vale'' & contrast with the letters to Trajan \\
\end{compare}
""")
G.q("3 Calpurnia", r"What comfort does Calpurnia find in Pliny's absence (6.7)?",
    "holding his books as if they were him", [("writing poetry", "Not stated."),
                                              ("visiting his mother", "No."),
                                              ("reading Livy", "No.")],
    "quod pro me libellos meos teneas.", "His books stand in for him.",
    ["saepe etiam in vestigio meo colloces."])
G.q("3 Calpurnia", r"What does \emph{licet hoc ita me delectet ut torqueat} express?",
    "that her letters both delight and torment him", [("that he forbids her to write", "He asks her to write often."),
                                                      ("that her letters bore him", "No."),
                                                      ("that he wants to stop writing", "No.")],
    "Paradox.", "Pleasure and pain together: a motif from love poetry.",
    ["ita … ut: result."])

G.sec("Contexts and registers across the letters")
G.tex(r"""
\begin{compare}{Context}{What to know}{Letter}
Belief in the supernatural & educated Romans debated whether ghosts were real; proper burial (\emph{rite conditis manibus}) quieted the dead & 7.27 \\
Domitian & emperor 81--96 CE, remembered as a tyrant; Pliny presents himself as having narrowly escaped & 7.27.14 \\
Citizenship & \emph{ius Quiritium} for freed persons; Roman citizenship as a privilege granted by the emperor & 10.5--7 \\
Provincial government & Pliny as Trajan's legate in Bithynia-Pontus, reporting on finances and public works & 10.37, 10.90 \\
Marriage & companionate ideals in Pliny's self-portrait as husband & 6.4, 6.7 \\
\end{compare}
""")
G.q("4 Contexts", r"Why was the ghost's haunting ended in 7.27?",
    "The bones found in chains were given proper burial.", [("Athenodorus left the house.", "He stayed and investigated."),
                                                            ("A priest drove the ghost out.", "No."),
                                                            ("The house was destroyed.", "It was lived in afterward.")],
    "rite conditis manibus.", "Proper burial gives peace to the restless dead.",
    ["collecta publice sepeliuntur."])

G.sec("Task kit: the Translation (Q2) on Pliny")
G.tex(r"""
\begin{terms}
Find every verb & mark main verbs, participles, infinitives; note tense and voice \\
Keep the structure & a participle stays a participle (``having asked''), an ablative absolute stays one (``when the price had been heard'') \\
Translate every word & small words (\emph{ac, immo, tamen}) are often whole segments \\
Historical present & you may translate in the present or the past, but be consistent \\
Literal over elegant & the segment is scored for accuracy, not style \\
\end{terms}
""")
G.q("5 Translation", r"In a translation, \emph{iubet sterni sibi} is best rendered",
    "he orders (a bed) to be spread for himself", [("he orders himself to lie down", "Sterni is passive; sibi is dative."),
                                                   ("he spreads out for himself", "Iubet is the main verb."),
                                                   ("he was ordered to sleep", "Iubet is active.")],
    "passive infinitive + dative.", "sterni: present passive infinitive of sterno.",
    ["iubet + sterni."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 3: Pliny's Letters: Ghosts, Trajan and Calpurnia: Question Set", r"Unit 3 \textperiodcentered\ Question Set",
        abstract=r"""Three sets and four discrete questions in the exam's formats: a long set on 7.27.5--6 (the haunted house in Athens), a short syllabus set on 6.7.2--3, a short sight set in adapted Latin about Rome's water supply, and four discrete sight sentences, followed by a Translation question (15 points) on 7.27.7 with the segment-by-segment scoring guide. Questions are in English, as on the exam; Latin is quoted without macrons. Allow about 25 minutes for the multiple choice and 15 for the translation.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Translation: \blank\ / 15 \qquad Target: 15+ MCQ and 12+ translation",
        short="Unit 3", sub="Pliny's Letters: Ghosts, Trajan and Calpurnia")

Q.sec("Long set: Pliny, Epistulae 7.27")
Q.src(r"Long set (syllabus prose) \textperiodcentered\ Pliny, \emph{Epistulae} 7.27.5--6", [
    r"Erat Athenis spatiosa et capax domus sed infamis et pestilens. Per silentium noctis sonus ferri, et si attenderes acrius, strepitus vinculorum longius primo, deinde e proximo reddebatur: mox apparebat idolon, senex macie et squalore confectus, promissa barba horrenti capillo; cruribus compedes, manibus catenas gerebat quatiebatque. Inde inhabitantibus tristes diraeque noctes per metum vigilabantur; vigiliam morbus et crescente formidine mors sequebatur.",
], 10, note="Athenae, -arum, f. pl.: Athens (locative Athenis). idolon, n.: ghost. macies, -ei, f.: thinness. squalor, -oris, m.: filth. compedes, -um, f. pl.: shackles.")
Q.q("1.C Summary", r"How is the house described in the first sentence?",
    "large and roomy, but notorious and deadly", [("small but beautiful", "Spatiosa et capax = spacious and roomy."),
                                                  ("new and cheap", "No."),
                                                  ("abandoned and ruined", "Not yet stated.")],
    "spatiosa et capax … sed infamis et pestilens.", "Two pairs of adjectives, joined by sed.",
    ["sed marks the contrast."])
Q.q("2.A Style", r"The first sentence is built on",
    "a contrast between two pairs of adjectives", [("a simile", "No comparison."),
                                                   ("a rhetorical question", "No."),
                                                   ("asyndeton of verbs", "No.")],
    "Balanced antithesis.", "Good qualities vs. bad reputation.",
    ["spatiosa et capax / infamis et pestilens."])
Q.q("1.D Translation", r"\emph{si attenderes acrius} is best translated",
    "if you listened more closely", [("if you had listened most sharply", "Acrius is comparative; the tense is imperfect."),
                                    ("when he listened more sharply", "Attenderes is second person."),
                                    ("if you will listen to the sharper sound", "No.")],
    "General ``you'' + imperfect subjunctive.", "Comparative adverb acrius.",
    ["acriter → acrius."])
Q.q("1.C Summary", r"How does the sound of the chains change?",
    "It is heard far away at first, then from close by.", [("It is loud at first, then stops.", "No."),
                                                           ("It moves from the house to the street.", "No."),
                                                           ("It is heard only in the morning.", "Per silentium noctis.")],
    "longius primo, deinde e proximo.", "Approach of the ghost.",
    ["primo … deinde."])
Q.q("1.A Meaning", r"\emph{macie et squalore confectus} describes the old man as",
    "worn out by thinness and filth", [("made of iron and chains", "No."),
                                       ("finished with his work", "Confectus here = exhausted."),
                                       ("dressed in fine clothes", "The opposite.")],
    "confectus = worn out.", "Ablatives of cause with confectus.",
    ["macies, squalor."])
Q.q("1.B Grammar", r"\emph{promissa barba horrenti capillo} contains",
    "two ablatives of description", [("two ablative absolutes", "These describe the ghost's appearance."),
                                     ("two datives of possession", "Ablative case."),
                                     ("an indirect statement", "No.")],
    "Ablative of description.", "with a long beard, with bristling hair.",
    ["barba (abl.), capillo (abl.)."])
Q.q("1.C Summary", r"What did the ghost carry and shake?",
    "shackles on his legs and chains on his hands", [("a sword and a shield", "No."),
                                                     ("a lamp and a tablet", "Those are Athenodorus's."),
                                                     ("the bones of his body", "No.")],
    "cruribus compedes, manibus catenas.", "cruribus, manibus: on his legs, on his hands.",
    ["compedes, catenas."])
Q.q("1.D Translation", r"\emph{tristes diraeque noctes per metum vigilabantur} is best translated",
    "sad and dreadful nights were spent awake in fear", [("sad nights watched the fearful people", "Vigilabantur is passive."),
                                                         ("they watched sad and dreadful nights through a window", "No."),
                                                         ("fear kept the nights sad", "Not the structure.")],
    "Passive: nights were spent awake.", "inhabitantibus: dative of agent/reference.",
    ["vigilo → vigilabantur."])
Q.q("2.A Style", r"\emph{vigiliam morbus et crescente formidine mors sequebatur} presents",
    "a climax: sleeplessness leads to illness, and illness to death", [("a reversal: death leads to sleep", "No."),
                                                                       ("a simile comparing fear to illness", "No."),
                                                                       ("a list of the ghost's actions", "It lists the inhabitants' suffering.")],
    "Gradation.", "vigilia → morbus → mors.",
    ["each step worse than the last."])
Q.q("1.B Grammar", r"\emph{crescente formidine} is",
    "an ablative absolute: ``as fear grew''", [("an ablative of means: ``by growing fear''", "Present participle + noun, set off: ablative absolute."),
                                               ("a dative", "No."),
                                               ("an indirect statement", "No.")],
    "Ablative absolute.", "Simultaneous action.",
    ["crescente (pres. part.)."])

Q.sec("Short set: Pliny, Epistulae 6.7")
Q.src(r"Short set (syllabus prose) \textperiodcentered\ Pliny, \emph{Epistulae} 6.7.2--3", [
    r"invicem ego epistulas tuas lectito atque identidem in manus quasi novas sumo. Sed eo magis ad desiderium tui accendor.",
], 3, note="lectito, -are: to read again and again. identidem: repeatedly.")
Q.q("1.C Summary", r"What does Pliny do with Calpurnia's letters?",
    "He reads them over and over, as if they were new.", [("He burns them.", "No."),
                                                          ("He sends them back.", "No."),
                                                          ("He shows them to Trajan.", "No.")],
    "lectito … quasi novas.", "Detail.",
    ["identidem in manus … sumo."])
Q.q("1.A Meaning", r"\emph{accendor} literally means",
    "I am set on fire", [("I set fire", "Passive."),
                         ("I climb", "That is ascendo."),
                         ("I am refused", "No.")],
    "accendo, passive.", "Metaphor: inflamed with longing.",
    ["accendor = I am kindled."])
Q.q("2.A Style", r"The metaphor in \emph{ad desiderium tui accendor} presents longing as",
    "a fire", [("a journey", "No."),
               ("a wound", "No."),
               ("a storm", "No.")],
    "Fire of love.", "A common image of desire.",
    ["accendor → fire."])

Q.sec("Short set: sight prose")
Q.src(r"Short set (sight prose, adapted) \textperiodcentered\ Rome's aqueducts", [
    r"Aquae, quae per tot arcus in urbem ducuntur, non solum ad usum civium sed etiam ad salubritatem pertinent; nam sine aqua copiosa morbi celeriter crescunt.",
], 3, note="Latin adapted for this practice. salubritas, -atis, f.: healthiness.")
Q.q("1.C Summary", r"According to the passage, what do the aqueducts provide besides water for use?",
    "health for the city", [("defense against enemies", "No."),
                            ("beauty for the temples", "Not stated."),
                            ("income for the emperor", "No.")],
    "ad salubritatem pertinent.", "Detail.",
    ["non solum … sed etiam."])
Q.q("1.B Grammar", r"\emph{quae per tot arcus in urbem ducuntur} is",
    "a relative clause describing aquae", [("a purpose clause", "No ut."),
                                           ("an indirect question", "No."),
                                           ("an ablative absolute", "No.")],
    "quae → aquae.", "Relative clause: which are led into the city.",
    ["quae (nom. pl. fem.)."])
Q.q("1.C Summary", r"Why, according to the passage, is plentiful water necessary?",
    "Without it, diseases spread quickly.", [("Without it, fires cannot be put out.", "Not stated."),
                                             ("Without it, the baths close.", "Not stated."),
                                             ("Without it, crops fail.", "Not stated.")],
    "sine aqua … morbi crescunt.", "Detail.",
    ["nam gives the reason."])

Q.sec("Discrete sight questions")
Q.q("1.D Translation", r"\emph{Medicus aegrum tam diligenter curavit ut mox convalesceret.} This sentence means",
    "The doctor cared for the sick man so diligently that he soon recovered.", [("The doctor cared for the sick man diligently in order to recover.", "Tam … ut marks result."),
                                                                                ("The sick man cared for the doctor.", "Roles reversed."),
                                                                                ("The doctor recovered after caring for the sick man.", "Subject of convalesceret is aegrum's referent.")],
    "Result clause.", "tam … ut + subjunctive.",
    ["tam diligenter … ut."])
Q.q("1.B Grammar", r"In \emph{Rogo te ut mihi quam saepissime scribas}, \emph{ut \ldots\ scribas} is",
    "an indirect command", [("a result clause", "Rogo introduces a request."),
                            ("an indirect statement", "No infinitive."),
                            ("a temporal clause", "No.")],
    "rogo ut + subjunctive.", "``I ask you to write to me as often as possible.''",
    ["verb of asking + ut."])
Q.q("1.A Meaning", r"In \emph{Imperator legato epistulam rescripsit}, \emph{rescripsit} means",
    "wrote back", [("wrote again the same letter", "Rescribo = to write in reply."),
                   ("erased", "No."),
                   ("read", "No.")],
    "re- + scribo.", "Trajan's replies are rescripta.",
    ["rescribo = reply in writing."])
Q.q("1.D Translation", r"\emph{Domo deserta, nemo noctem ibi agere audebat.} This sentence means",
    "Since the house had been deserted, no one dared to spend the night there.", [("No one deserted the house at night.", "Domo deserta is an ablative absolute."),
                                                                                  ("The house dared no one to spend the night.", "No."),
                                                                                  ("No one spent the night in the deserted house because of the noise.", "Adds unstated detail.")],
    "Ablative absolute + audeo.", "agere noctem = to spend the night.",
    ["domo deserta."])

Q.frq(kind="Translation", head=r"Question 2 \textperiodcentered\ Translation \textperiodcentered\ 15 points \textperiodcentered\ about 15 minutes", mins=15,
      directions=[r"Translate the passage below as literally as possible."],
      sources=[dict(title=r"Pliny, \emph{Epistulae} 7.27.7", paras=[
          r"Venit Athenas philosophus Athenodorus, legit titulum auditoque pretio, quia suspecta vilitas, percunctatus omnia docetur ac nihilo minus, immo tanto magis conducit. Ubi coepit advesperascere, iubet sterni sibi in prima domus parte, poscit pugillares stilum lumen.",
          r"\emph{titulus, -i, m.}: notice (of sale or rent) \quad \emph{vilitas, -atis, f.}: cheapness \quad \emph{percunctor, -ari}: to inquire \quad \emph{advesperascit}: it grows dark \quad \emph{pugillares, -ium, m. pl.}: writing tablets"])],
      model=[r"The philosopher Athenodorus came to Athens; he read the notice and, when the price had been heard, because the cheapness was suspicious, having asked about everything, he is told (the story), and nevertheless, indeed all the more, he rents (the house). When it began to grow dark, he orders a bed to be spread for himself in the front part of the house; he asks for writing tablets, a stylus, a lamp."],
      rows=[("1 Venit Athenas", 1, "came to Athens", "in Athens"),
            ("2 philosophus Athenodorus", 1, "the philosopher Athenodorus", ""),
            ("3 legit titulum", 1, "he read the notice", "he chose"),
            ("4 auditoque pretio", 1, "and when the price had been heard", "hearing the price (active)"),
            ("5 quia suspecta vilitas", 1, "because the cheapness was suspicious", "he suspected (wrong subject)"),
            ("6 percunctatus omnia", 1, "having asked about everything", "everything having been asked (passive)"),
            ("7 docetur", 1, "he is told / he is informed", "he teaches"),
            ("8 ac nihilo minus", 1, "and nevertheless", "and nothing less (literal misreading)"),
            ("9 immo tanto magis", 1, "indeed, all the more", "omitting immo"),
            ("10 conducit", 1, "he rents (it)", "he leads"),
            ("11 Ubi coepit advesperascere", 1, "when it began to grow dark", "where"),
            ("12 iubet", 1, "he orders", "he is ordered"),
            ("13 sterni sibi", 1, "(a bed) to be spread for himself", "to spread himself"),
            ("14 in prima domus parte", 1, "in the front (first) part of the house", "in the first house"),
            ("15 poscit pugillares stilum lumen", 1, "he asks for writing tablets, a stylus, a light", "omitting an item")],
      tips=["The deponent participle percunctatus is active in meaning (having asked).", "The ablative absolute audito pretio keeps its passive sense.",
            "The historical presents (docetur, conducit, iubet, poscit) may be rendered in the present or the past, consistently."],
      ask="Write your translation, then mark each segment you rendered accurately.", lines=10)

GUIDE, QSET = G, Q
