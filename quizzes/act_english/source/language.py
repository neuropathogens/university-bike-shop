from .model import Guide, Q, Section

NC = "NO CHANGE"

intro = Section(
    title="Knowledge of Language at a Glance",
    key="kla-intro",
    body=r"""
\textbf{What it tests.} Precision and economy: saying exactly what is meant, in as few words as the meaning
requires, in a register that fits the passage. Three skills: \emph{concision}, \emph{word choice}, and
\emph{consistent style and tone}.

\textbf{Weight.} 18--23\% of the section, about 9--11 of the 50 questions. Most can be answered in under 30 seconds.

\textbf{What makes these different.} Often every choice is grammatical. You are choosing the \emph{best} expression,
so the deciding questions are: Does it repeat an idea already stated? Is it the precise word for this context? Does
it sound like the rest of the passage?

\textbf{Default rule.} When two or more choices are grammatical and say the same thing, the shortest one is
right---\emph{unless} the shorter choice drops meaning the sentence needs. ``DELETE the underlined portion'' is a
legitimate answer, and it is right more often than students expect.

\textbf{Signal table.}\par\smallskip
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.55\linewidth}X@{}}
\toprule \textit{If the choices\dots} & \textit{Go to} \\ \midrule
say the same thing at different lengths; include DELETE & \S\ref{sec:concision} \\
swap one word for a near-synonym or sound-alike & \S\ref{sec:diction} \\
range from slang to stiff formality & \S\ref{sec:tone} \\
merge two sentences, or the stem says ``combine'' & \S\ref{sec:combining} \\ \bottomrule
\end{tabularx}
""",
)

concision = Section(
    title="Concision and Redundancy",
    key="concision", tag="Concision / redundancy", cat="KLA",
    stem="Which choice expresses the idea most clearly and concisely?",
    body=r"""
\textbf{Rule.} Cut every word that repeats meaning or adds none.
\begin{itemize}
\item \textbf{Built-in redundancy:} \emph{annually each year}, \emph{return back}, \emph{past history},
\emph{first began}, \emph{each and every}, \emph{completely eliminated}, \emph{revert back}, \emph{new innovation}.
\item \textbf{Wordy phrases:} \emph{due to the fact that} \(\rightarrow\) because; \emph{in order to} \(\rightarrow\) to;
\emph{at this point in time} \(\rightarrow\) now; \emph{has the ability to} \(\rightarrow\) can.
\item \textbf{Cross-sentence redundancy:} the underlined phrase restates something already said elsewhere in the
sentence or paragraph. Read beyond the underline.
\end{itemize}
\textbf{Check.} The shortest choice must still be grammatical and keep every needed idea.
""",
    questions=[
        Q(context=r"The town's harvest festival is held \ul{annually each year} in October.",
          choices=[NC, "annually", "every year annually", "on an annual, yearly basis"], ans=1,
          why=r"``Annually'' already means ``each year''; using both is redundant."),
        Q(context=r"\ul{Due to the fact that} the bridge was icy, the school buses took a longer route.",
          choices=[NC, "Owing to the reason that", "Being as", "Because"], ans=3,
          why=r"``Because'' says the same thing in one word. ``Being as'' is nonstandard."),
        Q(context=r"The team \ul{returned back to} the locker room at halftime.",
          choices=[NC, "returned back again to", "returned to", "went and returned to"], ans=2,
          why=r"``Return'' already means ``go back''; ``back'' is redundant."),
        Q(context=r"The violinist practiced for six hours a \ul{day, spending six hours each day practicing}.",
          choices=[NC, "day, practicing for six hours daily", "day, which was a lot of practice each day",
                   r"day."], ans=3, layout="list",
          why=r"The underlined phrase repeats ``practiced for six hours a day.'' End the sentence after ``day.''"),
        Q(context=r"The new scheduling system \ul{reduced} wait times at the clinic.",
          choices=[NC, "reduced and lowered", "brought about a reduction in", "had the effect of reducing"], ans=0,
          why=r"``Reduced'' is precise; the alternatives add words without adding meaning."),
    ],
)

diction = Section(
    title="Word Choice: Precision and Commonly Confused Words",
    key="diction", tag="Word choice", cat="KLA",
    stem="Which choice is most precise in the context of the sentence?",
    body=r"""
\textbf{Rule.} The right word fits both the \emph{dictionary meaning} and the \emph{connotation} the context needs.

\smallskip
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.48\linewidth}X@{}}
\emph{affect} (verb: influence) / \emph{effect} (noun: result) & \emph{fewer} (countable) / \emph{less} (amount) \\
\emph{imply} (speaker suggests) / \emph{infer} (listener concludes) & \emph{than} (comparison) / \emph{then} (time) \\
\emph{accept} (receive) / \emph{except} (excluding) & \emph{principal} (main) / \emph{principle} (rule) \\
\emph{elicit} (draw out) / \emph{illicit} (illegal) & \emph{number} (countable) / \emph{amount} (mass) \\
\end{tabularx}

\smallskip
\textbf{Connotation.} \emph{Simple}, \emph{simplistic}, and \emph{accessible} share a meaning but not a judgment.
When the sentence praises, the word must praise.
\textbf{Method.} Read the whole sentence and predict a word of your own before reading the choices.
""",
    questions=[
        Q(context=r"The new schedule will \ul{effect} how many hours each employee works.",
          choices=[NC, "affect", "infect", "afflict"], ans=1,
          why=r"``Affect'' is the verb meaning ``to influence.'' As a verb, ``effect'' means ``to bring about,'' which does "
              r"not fit; ``infect'' and ``afflict'' change the meaning."),
        Q(context=r"There were \ul{less} applicants for the scholarship this year than last year.",
          choices=[NC, "lesser", "fewer", "lower"], ans=2,
          why=r"Applicants can be counted, so ``fewer.'' ``Less'' is for amounts (less water)."),
        Q(context=r"The detective \ul{glanced at} every page of the ledger, searching for a single missing payment.",
          choices=[NC, "scrutinized", "skimmed", "flipped"], ans=1,
          why=r"Searching for one missing payment requires close examination. The other choices suggest quick or "
              r"careless reading."),
        Q(context=r"Critics praised the senator's speech for its \ul{cheap} language, which every voter could understand.",
          choices=[NC, "simplistic", "accessible", "inferior"], ans=2,
          why=r"The sentence praises the language, so the word must be positive and mean ``easy to understand.'' "
              r"The others are negative."),
        Q(context=r"The coach's halftime speech \ul{inferred} that the team would need to play harder.",
          choices=[NC, "deduced", "concluded", "implied"], ans=3,
          why=r"A speaker implies; a listener infers. ``Deduced'' and ``concluded'' also describe what a listener does."),
    ],
)

tone = Section(
    title="Style and Tone",
    key="tone", tag="Style / tone", cat="KLA",
    stem="Which choice best maintains the style and tone of the sentence?",
    body=r"""
\textbf{Rule.} Match the register of the passage.
\begin{itemize}
\item \textbf{Formal or informational passages} reject slang and casual intensifiers: \emph{super, totally, a ton of,
kind of, freaked out, a big deal, legit}.
\item \textbf{Casual personal narratives} reject the opposite error: stiff, inflated wording
(\emph{embarked upon a perambulation} for \emph{walked}).
\item Avoid overstatement the passage cannot support (\emph{totally proves} for \emph{suggests}).
\end{itemize}
\textbf{Speed tip.} These items usually have one choice in the passage's voice and three that are too slangy or too
stiff. Eliminate by register first, then confirm the meaning.
""",
    questions=[
        Q(context=r"Marie Curie's research on radioactivity earned her Nobel Prizes in both physics and chemistry, "
                  r"\ul{which is pretty awesome}.",
          choices=[NC, "a rare distinction in the history of science", "making her a total legend",
                   "which was a big deal and stuff"], ans=1, layout="list",
          why=r"The sentence is formal and factual; the correct choice keeps that register. The others are slang."),
        Q(context=r"In its formal response, the agency stated that the inspection delays \ul{were kind of a mess}.",
          choices=[NC, "were a total disaster, honestly", "resulted from a shortage of qualified inspectors",
                   "stunk"], ans=2, layout="list",
          why=r"A formal agency statement calls for formal, specific wording; this choice also states a cause, which "
              r"the others lack."),
        Q(context=r"My little brother grabbed his skateboard and \ul{embarked upon a perambulation} to the park.",
          choices=[NC, "commenced locomotion toward", "headed to", "undertook a journey of considerable magnitude to"],
          ans=2, layout="list",
          why=r"A casual story about a little brother calls for plain words. The other choices are stiff and wordy."),
        Q(context=r"The committee's findings \ul{suggest} that the tutoring program should be expanded.",
          choices=[NC, "are like, saying", "kinda show", "totally prove"], ans=0,
          why=r"``Suggest'' matches the measured tone of a committee report. ``Totally prove'' is informal and overstates."),
    ],
)

combining = Section(
    title="Combining Sentences",
    key="combining", tag="Combining sentences", cat="KLA",
    stem="Which choice most effectively combines the sentences at the underlined portion?",
    body=r"""
\textbf{Rule.} A good combination is (1) grammatical, (2) faithful to the original meaning and logic, and
(3) free of the repetition that made the original clumsy---usually a repeated subject.

\textbf{Method.} Find what the two sentences share (the same subject, the same time). The best combination
mentions it once. Then reject choices that create a splice, insert a false relationship (\emph{but} where nothing
contrasts), or garble word order.

\textbf{Common tools.} A compound verb or object (\emph{has three hearts and blue blood}); an adjective
(\emph{wooden masks}); an \emph{as}-phrase (\emph{opened in 1937 as the longest\dots}); a relative clause
(\emph{, which\dots}).
""",
    questions=[
        Q(context=r"The Golden Gate Bridge \ul{opened in 1937. When it opened, it was} the longest suspension bridge "
                  r"in the world.",
          choices=[NC, "opened in 1937, and when it opened in 1937, it was", "opened in 1937 as",
                   "opened, in 1937, being at that time"], ans=2, layout="list",
          why=r"``Opened in 1937 as the longest suspension bridge'' says everything once. The others repeat or garble."),
        Q(context=r"Octopuses have three \ul{hearts. The octopus also has} blue blood.",
          choices=[NC, "hearts and", "hearts, and the octopus also has", "hearts, also having"], ans=1,
          why=r"The shared subject is stated once and the two objects are joined: ``have three hearts and blue blood.''"),
        Q(context=r"The museum's newest exhibit features \ul{masks from West Africa. The masks are carved from wood.}",
          choices=[NC, "masks, from West Africa, and the masks are wood carved.",
                   "masks from West Africa, the masks are carved from wood.", "wooden masks from West Africa."],
          ans=3, layout="list",
          why=r"The adjective ``wooden'' compresses the second sentence. The comma version is a splice; the other "
              r"is awkward and repetitive."),
    ],
)

mixed = Section(
    title="Mixed Knowledge of Language Passage",
    key="kla-mixed", tag="", cat="KLA",
    intro=r"Work this passage at test pace (about 4 minutes). Every item tests concision, word choice, or tone.",
    passage_label="PASSAGE", passage_title="The Return of the Gray Wolf",
    passage=r"""
In 1995, biologists released fourteen gray wolves, captured in Canada, into Yellowstone National Park. Wolves had
been absent from the park for nearly seventy years, \ul{ever since the last wolves in the park were killed and
eliminated}@@ in the 1920s.

The return of the predators \ul{alarmed}@@ some ranchers, who feared for their cattle. Park biologists, however,
were more interested in how the wolves would \ul{effect}@@ the park's elk. Without predators, elk herds had grown
large and \ul{had eaten many young willow and aspen trees, consuming them}@@ along the riverbanks.

Some researchers now credit the wolves with helping those trees recover. Others \ul{brag}@@ that human hunting and
a series of droughts also reduced the elk herds. Whatever the final verdict, the wolves' return has shown how a
single species can reshape an entire \ul{ecosystem in many different ways throughout the whole ecosystem}@@.
""",
    questions=[
        Q(stem="Which choice is most concise?",
          choices=[NC, "ever since the last ones were eliminated by being killed", "since the last of them were killed",
                   "since the last wolves were killed off and eliminated completely"], ans=2, layout="list",
          rule="Concision / redundancy",
          why=r"``Killed and eliminated'' says one thing twice, and ``in the park'' repeats ``from the park.''"),
        Q(stem="Which choice best maintains the tone of the essay?",
          choices=[NC, "bummed out", "freaked out", "weirded out"], ans=0, rule="Style / tone",
          why=r"The essay is informational; ``alarmed'' is precise and neutral. The others are slang."),
        Q(stem="Which choice is most precise in context?",
          choices=[NC, "infect", "affect", "effectuate"], ans=2, rule="Word choice",
          why=r"The verb meaning ``influence'' is ``affect.''"),
        Q(stem="Which choice is most concise?",
          choices=[NC, "had eaten many young willow and aspen trees",
                   "had consumed and eaten many young willow and aspen trees",
                   "had eaten, consuming, many young willow and aspen trees"], ans=1, layout="list",
          rule="Concision / redundancy",
          why=r"``Consuming them'' repeats ``had eaten.''"),
        Q(stem="Which choice is most precise in context?",
          choices=[NC, "boast", "confess", "point out"], ans=3, rule="Word choice",
          why=r"Researchers offering a competing explanation ``point out'' evidence. ``Brag'' and ``boast'' imply pride; "
              r"``confess'' implies guilt."),
        Q(stem="Which choice is most concise?",
          choices=[NC, "ecosystem throughout the entire area of the ecosystem", "ecosystem in ways that affect it",
                   "ecosystem"], ans=3, rule="Concision / redundancy",
          why=r"``Reshape an entire ecosystem'' already says it all; everything after ``ecosystem'' repeats it."),
    ],
)

GUIDE = Guide(
    slug="3-ACT-English-Knowledge-of-Language",
    kicker="ACT English · Study Guide 3 of 4",
    title="Knowledge of Language",
    subtitle="Concision, precise word choice, and consistent style and tone",
    short="Knowledge of Language",
    abstract=r"""Knowledge of Language is 18--23\% of the enhanced ACT English section---roughly 9--11 of 50
questions. These items reward economy and precision: cutting redundancy, choosing the exact word for the context,
keeping the passage's tone, and combining sentences cleanly. Because several choices are often grammatical, the
deciding test is meaning: does a choice repeat, distort, or mismatch the passage's voice? This guide states each rule
with its traps, gives practice items in ACT format, and ends with a mixed passage. The answer key on the final pages
lists answers only, then explains each answer and names its rule.""",
    sections=[intro, concision, diction, tone, combining, mixed],
)
