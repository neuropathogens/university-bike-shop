from .model import Guide, Q, Section

NC = "NO CHANGE"
STEM = "Which choice results in a grammatically acceptable sentence?"

intro = Section(
    title="Conventions at a Glance",
    key="cse-intro",
    body=r"""
\textbf{What it tests.} Whether each sentence obeys the rules of standard written English: sentence structure,
punctuation, and usage (verbs, pronouns, modifiers, agreement, idioms). These items have one objectively correct
answer---no judgment about style or purpose is needed.

\textbf{Weight.} 38--43\% of the section, about 19--21 of the 50 questions. Paced at 42 seconds per item, these
should be your \emph{fastest} points: most take 15--25 seconds once the rules are automatic.

\textbf{The four-step method.}
\begin{enumerate}[leftmargin=1.6em]
\item Read the \emph{whole} sentence, not just the underlined part. Errors usually depend on words outside the underline.
\item Scan the four choices vertically. \emph{What changes} between them tells you which rule is being tested.
\item Apply that rule and eliminate. Do not ``listen'' for what sounds right---check the rule.
\item If two choices are grammatically identical (period vs.\ semicolon between two clauses), neither can be the
unique answer. If several choices are correct, take the shortest one that keeps the meaning.
\end{enumerate}

\textbf{Signal table.}\par\smallskip
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.47\linewidth}X@{}}
\toprule \textit{If the choices differ in\dots} & \textit{Go to} \\ \midrule
periods, semicolons, commas + \emph{and/but}, no punctuation & \S\ref{sec:boundaries}, \S\ref{sec:semicolons} \\
commas around a phrase; \emph{that} vs.\ \emph{which} & \S\ref{sec:commas1} \\
commas in lists, between adjectives, or before a verb & \S\ref{sec:commas2} \\
apostrophes; \emph{its/it's}, \emph{their/they're} & \S\ref{sec:apostrophes} \\
singular vs.\ plural verbs (\emph{is/are}, \emph{has/have}) & \S\ref{sec:sva} \\
verb tense or form (\emph{had gone}, \emph{would have}) & \S\ref{sec:tense} \\
pronouns (\emph{it/they}, \emph{I/me}, \emph{who/whom}) & \S\ref{sec:pronouns} \\
the order of words after an introductory phrase & \S\ref{sec:modifiers} \\
\emph{-ing} vs.\ \emph{to} forms; \emph{-er/-est}; \emph{-ly} & \S\ref{sec:parallel} \\
prepositions (\emph{to/with/of}) & \S\ref{sec:idioms} \\ \bottomrule
\end{tabularx}
""",
)

boundaries = Section(
    title="Sentence Boundaries: Fragments, Run-ons, and Comma Splices",
    key="boundaries", tag="Sentence boundaries", cat="CSE", stem=STEM,
    body=r"""
\textbf{Rule.} An \emph{independent clause} (IC) has a subject, a verb, and a complete thought. Two ICs may be joined
only by a period, a semicolon, a comma \emph{plus} a FANBOYS conjunction (\emph{for, and, nor, but, or, yet, so}), a
colon (if the second explains the first), or a single dash.
\begin{itemize}
\item \textbf{Comma splice:} IC, IC. \quad \textbf{Run-on:} IC IC. \quad Both are always wrong.
\item \textbf{Fragment:} a ``sentence'' with no main verb (\emph{The library opening next month.}), or a dependent clause
standing alone (\emph{Which she later sold.} / \emph{Because the ovens failed.}).
\item A dependent clause (begins with \emph{although, because, while, when, if, which, who}) attaches to an IC with a
comma or no punctuation---never a semicolon or period.
\end{itemize}
\textbf{Test.} Cover the punctuation and ask: can each side stand alone as a sentence?
""",
    questions=[
        Q(context=r"The marathon begins at \ul{dawn, runners} gather near the starting line an hour early.",
          choices=[NC, "dawn; runners", "dawn runners", "dawn, with runners"], ans=1,
          why=r"Both halves are independent clauses. A comma alone makes a splice; no punctuation makes a run-on; "
              r"``with runners gather'' is ungrammatical. A semicolon correctly joins two ICs."),
        Q(context=r"Lena spent the summer restoring a 1970s \ul{sailboat. Which she} later sold to a marine museum.",
          choices=[NC, "sailboat; which she", "sailboat, which she", "sailboat. Which, she"], ans=2,
          why=r"``Which she later sold\dots'' is a dependent (relative) clause and cannot stand alone. Attach it with a "
              r"comma; a semicolon also requires an IC on both sides."),
        Q(context=r"The new library \ul{opening} next month on Alder Street.",
          choices=[NC, "which opens", "opens", "and opening"], ans=2,
          why=r"The subject needs a finite main verb. ``Opening,'' ``which opens,'' and ``and opening'' all leave a "
              r"fragment with no main verb."),
        Q(context=r"Although the trail was \ul{steep, the} hikers reached the summit before noon.",
          choices=[NC, "steep; the", "steep. The", "steep the"], ans=0,
          why=r"``Although the trail was steep'' is a dependent clause; a comma correctly links it to the IC. "
              r"A semicolon or period would strand it as a fragment."),
    ],
)

semicolons = Section(
    title="Semicolons, Colons, and Dashes",
    key="semicolons", tag="Semicolons / colons", cat="CSE", stem=STEM,
    body=r"""
\textbf{Semicolon (;).} Period-strength. Needs an IC on \emph{both} sides. Second use: separating list items that
already contain commas (\emph{Austin, Texas; Denver, Colorado; and Portland, Oregon}).

\textbf{Colon (:).} Needs a complete IC \emph{before} it; what follows explains, defines, or lists. After the colon
may come a single word, a phrase, a list, or another IC.
\begin{itemize}
\item Never after a verb or preposition: \emph{The kit includes: a tent} \(\times\). \quad Never after \emph{such as,
including, like}.
\end{itemize}
\textbf{Dashes.} A single dash works like a colon (emphatic explanation). A \emph{pair} of dashes works like a pair of
commas around nonessential information---and the pair must match (dash\dots dash, never dash\dots comma).
""",
    questions=[
        Q(context=r"The camping kit \ul{includes: a} tent, a stove, and two sleeping bags.",
          choices=[NC, "includes a", "includes; a", "includes, a"], ans=1,
          why=r"``The camping kit includes'' is not a complete thought, so no colon. Nothing separates a verb from "
              r"its objects."),
        Q(context=r"Maya had one goal for the \ul{season: qualifying} for the state championship.",
          choices=[NC, "season; qualifying", "season qualifying", "season---qualifying,"], ans=0,
          why=r"The colon follows a complete IC and introduces what the ``one goal'' was. A semicolon needs an IC after "
              r"it; the dash version adds a stray comma."),
        Q(context=r"The band's tour stops in Austin, \ul{Texas, Denver,} Colorado; and Portland, Oregon.",
          choices=[NC, "Texas; Denver,", "Texas; Denver;", "Texas Denver,"], ans=1,
          why=r"List items contain internal commas (city, state), so the items are separated by semicolons while the "
              r"city--state commas stay."),
        Q(context=r"The bakery closed \ul{early; because} the ovens failed.",
          choices=[NC, "early. Because", "early because", "early: because"], ans=2,
          why=r"``Because the ovens failed'' is a dependent clause. It cannot follow a semicolon or stand alone after a "
              r"period; attach it directly."),
    ],
)

commas1 = Section(
    title="Commas I: Nonessential Elements and Introductions",
    key="commas1", tag="Commas: nonessential / intro", cat="CSE", stem=STEM,
    body=r"""
\textbf{Rule.} Information that can be removed without changing the sentence's core meaning is \emph{nonessential}
and is set off by a matched pair of commas (or dashes, or parentheses---never mixed).
\begin{itemize}
\item \textbf{Deletion test:} remove the phrase. If the sentence still makes sense and still identifies the same
thing, it is nonessential \(\rightarrow\) commas.
\item \textbf{Essential} information tells you \emph{which one}. No commas: \emph{The architect Zaha Hadid designed\dots}
\item \emph{That} clauses are always essential: never commas. \emph{Which} clauses on the ACT are usually nonessential.
\item \textbf{Introductory} words, phrases, and dependent clauses take a comma: \emph{After the storm passed, the\dots}
\end{itemize}
\textbf{Trap.} Half a pair: \emph{My grandmother, who grew up in Taipei still cooks\dots} The phrase opened by a comma
must be closed by a comma.
""",
    questions=[
        Q(context=r"My \ul{grandmother, who grew up in Taipei} still makes scallion pancakes every Sunday.",
          choices=[NC, "grandmother, who grew up in Taipei,", "grandmother who grew up in Taipei,",
                   "grandmother---who grew up in Taipei,"], ans=1, layout="list",
          why=r"The clause is nonessential (``my grandmother'' is already identified), so it needs a matched pair of "
              r"commas. A dash--comma pair is mismatched."),
        Q(context=r"The \ul{architect, Zaha Hadid,} designed the aquatics center for the 2012 London Olympics.",
          choices=[NC, "architect Zaha Hadid", "architect, Zaha Hadid", "architect Zaha Hadid,"], ans=1,
          why=r"The name tells you \emph{which} architect, so it is essential: no commas. A single comma on one side is "
              r"never correct."),
        Q(context=r"The \ul{trail, that leads to the waterfall, is} closed for repairs.",
          choices=[NC, "trail that leads to the waterfall, is", "trail that leads to the waterfall is",
                   "trail, that leads to the waterfall is"], ans=2, layout="list",
          why=r"\emph{That} introduces an essential clause, which never takes commas. A lone comma before ``is'' would "
              r"also split subject from verb."),
        Q(context=r"\ul{After the storm passed the} volunteers began clearing debris from the beach.",
          choices=[NC, "After, the storm passed the", "After the storm, passed the", "After the storm passed, the"],
          ans=3, layout="list",
          why=r"An introductory dependent clause ends with a comma. Without it, readers first parse ``passed the "
              r"volunteers.''"),
    ],
)

commas2 = Section(
    title="Commas II: Lists, Adjectives, and Unnecessary Commas",
    key="commas2", tag="Commas: lists / unnecessary", cat="CSE", stem=STEM,
    body=r"""
\textbf{Use a comma} between three or more list items (the ACT consistently uses the comma before \emph{and}), and
between \emph{coordinate} adjectives---ones you could join with \emph{and} or reverse (\emph{a long, exhausting climb}).
No comma between cumulative adjectives (\emph{three old brick houses}).

\textbf{Never use a comma}
\begin{itemize}
\item between a subject and its verb (\emph{The students who finished early, were} \(\times\));
\item between a verb and its object, or after \emph{such as / like / including};
\item before \emph{and} when it joins only two verbs that share a subject (\emph{She sliced the mangoes and arranged them});
\item between the last adjective and its noun, or after a FANBOYS conjunction (\emph{but, the\dots} \(\times\)).
\end{itemize}
\textbf{Default.} When in doubt, no comma. Unneeded commas are tested far more often than missing ones.
""",
    questions=[
        Q(context=r"The students who finished the experiment \ul{early, were} allowed to leave.",
          choices=[NC, "early, were,", "early were", "early; were"], ans=2,
          why=r"The subject is the whole phrase ``The students who finished the experiment early''; no punctuation "
              r"separates a subject from its verb."),
        Q(context=r"The chef sliced the \ul{mangoes, and arranged} them in a fan around the plate.",
          choices=[NC, "mangoes and arranged", "mangoes; and arranged", "mangoes. And arranged"], ans=1,
          why=r"``Sliced\dots and arranged'' share one subject (the chef). A comma before \emph{and} belongs only "
              r"between two independent clauses; the other choices create errors."),
        Q(context=r"The expedition faced a \ul{long, exhausting} climb to the ridge.",
          choices=[NC, "long exhausting,", "long, exhausting,", "long; exhausting"], ans=0,
          why=r"``Long'' and ``exhausting'' are coordinate (``long and exhausting'' works), so a comma separates them---but "
              r"never a comma between the final adjective and the noun."),
        Q(context=r"Many desert animals, \ul{such as, jackrabbits and kit foxes,} release heat through their large ears.",
          choices=[NC, "such as jackrabbits, and kit foxes,", "such as jackrabbits and kit foxes",
                   "such as jackrabbits and kit foxes,"], ans=3, layout="list",
          why=r"No comma after \emph{such as}; two items joined by \emph{and} take no comma; the nonessential phrase "
              r"opened after ``animals'' must be closed with a comma."),
    ],
)

apostrophes = Section(
    title="Apostrophes and Possessives",
    key="apostrophes", tag="Apostrophes", cat="CSE", stem=STEM,
    body=r"""
\textbf{Nouns.} Singular possessive: \emph{company's}. Plural ending in \emph{s}: \emph{teams'}. Irregular plural:
\emph{children's}. A plural that owns nothing takes \emph{no} apostrophe: \emph{volunteers arrived}.

\textbf{Pronouns never use apostrophes for possession:} \emph{its, their, whose, yours, ours}. With an apostrophe they
are contractions: \emph{it's} = it is, \emph{they're} = they are, \emph{who's} = who is.

\textbf{Test.} Is the word followed by something it owns? Then possessive. Then ask: one owner or more? For
\emph{it's/they're}, expand the contraction and see whether the sentence still works.
""",
    questions=[
        Q(context=r"The \ul{companys'} new headquarters will open in March.",
          choices=[NC, "companies", "company's", "companies's"], ans=2,
          why=r"One company owns the headquarters: singular possessive. ``Companies'' is a plain plural; "
              r"``companies's'' never occurs."),
        Q(context=r"The museum updated \ul{it's} website so visitors could buy tickets online.",
          choices=[NC, "its'", "their", "its"], ans=3,
          why=r"``It's'' = it is. The possessive is ``its'' (no apostrophe); ``their'' doesn't agree with the singular "
              r"``museum''; ``its''' does not exist."),
        Q(context=r"Both \ul{teams'} coaches agreed to delay the game.",
          choices=[NC, "team's", "teams", "teams's"], ans=0,
          why=r"``Both'' signals two teams, and the teams own the coaches: plural possessive = \emph{teams'}."),
        Q(context=r"Dozens of \ul{volunteer's} arrived early to set up tables for the fundraiser.",
          choices=[NC, "volunteers'", "volunteers", "volunteer"], ans=2,
          why=r"``Dozens of'' requires a plural, and the volunteers own nothing in the sentence: no apostrophe."),
    ],
)

sva = Section(
    title="Subject--Verb Agreement",
    key="sva", tag="Subject--verb agreement", cat="CSE", stem=STEM,
    body=r"""
\textbf{Rule.} A verb agrees with its true subject, not with the nearest noun.
\begin{itemize}
\item \textbf{Cross out} prepositional phrases and nonessential clauses between subject and verb:
\emph{The collection [of rare maps] is\dots}
\item \textbf{Inverted sentences} put the subject after the verb: \emph{Behind the mill stand two oaks.}
Also \emph{There is/are}, \emph{Among the finalists was\dots}
\item \textbf{Singular:} each, every, either, neither, anyone, everyone, a collective noun (team, committee,
family), and a gerund phrase (\emph{Restoring bikes requires\dots}).
\item \textbf{Compound} subjects joined by \emph{and} are plural; with \emph{or/nor}, the verb matches the nearer subject.
\end{itemize}
""",
    questions=[
        Q(context=r"The collection of rare maps \ul{are} on display through August.",
          choices=[NC, "is", "were", "have been"], ans=1,
          why=r"The subject is ``collection'' (singular); ``of rare maps'' is a prepositional phrase. The other "
              r"choices are plural."),
        Q(context=r"Behind the old mill \ul{stands} two oak trees that are more than three hundred years old.",
          choices=[NC, "is standing", "has stood", "stand"], ans=3,
          why=r"Inverted order: the subject ``two oak trees'' follows the verb. Plural subject \(\rightarrow\) ``stand.''"),
        Q(context=r"Each of the paintings in the exhibit \ul{were} created by a student.",
          choices=[NC, "have been", "was", "are"], ans=2,
          why=r"``Each'' is singular; ignore ``of the paintings in the exhibit.'' Past context \(\rightarrow\) ``was.''"),
        Q(context=r"Restoring old bicycles \ul{requires} patience and a good set of tools.",
          choices=[NC, "require", "are requiring", "have required"], ans=0,
          why=r"The subject is the gerund phrase ``Restoring old bicycles,'' which is singular; ``bicycles'' is the "
              r"object inside the phrase."),
    ],
)

tense = Section(
    title="Verb Tense and Form",
    key="tense", tag="Verb tense / form", cat="CSE", stem=STEM,
    body=r"""
\textbf{Consistency.} Match the tense of the surrounding sentences unless a time marker signals a shift.
\begin{itemize}
\item \textbf{Past perfect} (\emph{had} + participle): an action finished before another past action.
\emph{By the time crews arrived, the fire had spread.}
\item \textbf{Present perfect} (\emph{has/have} + participle): began in the past, continues now. \emph{Since 2010, she has coached\dots}
\item \textbf{Irregular participles:} had gone, swum, begun, written, drunk, ridden, chosen---never \emph{had went}.
\item \textbf{\emph{Would have}, never \emph{would of}.} Past conditional: \emph{If he had practiced, he would have won}
(no \emph{would} in the \emph{if} clause).
\end{itemize}
""",
    questions=[
        Q(context=r"By the time the firefighters arrived, the blaze \ul{has spread} to the barn.",
          choices=[NC, "had spread", "spreads", "will have spread"], ans=1,
          why=r"``By the time the firefighters arrived'' sets a past reference point; an action completed before it takes "
              r"the past perfect."),
        Q(context=r"Before the race, she had \ul{swam} the length of the lake twice.",
          choices=[NC, "swimmed", "swum", "swims"], ans=2,
          why=r"After \emph{had}, use the past participle: swim--swam--swum."),
        Q(context=r"If the team had practiced penalty kicks, it \ul{would of} won the final.",
          choices=[NC, "will have", "would had", "would have"], ans=3,
          why=r"``Would of'' is a mishearing of ``would've.'' A past contrary-to-fact condition takes "
              r"\emph{had practiced\dots would have won}."),
        Q(context=r"In 1969, the flight controllers in Houston monitored every second of the descent and \ul{celebrates} "
                  r"when the lunar module touched down.",
          choices=[NC, "celebrated", "has celebrated", "will celebrate"], ans=1,
          why=r"The sentence narrates a past event and pairs the verb with ``monitored''; it must also be simple past."),
    ],
)

pronouns = Section(
    title="Pronouns: Agreement, Case, and Clarity",
    key="pronouns", tag="Pronouns", cat="CSE", stem=STEM,
    body=r"""
\textbf{Agreement.} A pronoun matches its antecedent in number: a company, team, or committee is \emph{it/its}, not
\emph{they/their}.

\textbf{Case.} Subjects: \emph{I, he, she, we, they, who}. Objects: \emph{me, him, her, us, them, whom}.
\begin{itemize}
\item \textbf{Drop the other person:} \emph{gave the award to Priya and [me]} \(\rightarrow\) \emph{gave the award to me}.
\item \textbf{Who vs.\ whom:} answer the clause with \emph{he/him}. \emph{The panel honored him} \(\rightarrow\) \emph{whom}.
\item \emph{Myself} only when \emph{I} appears earlier in the same clause (\emph{I taught myself}).
\end{itemize}
\textbf{Clarity.} If a pronoun could point to two nouns, replace it with the noun.
\emph{Who} is for people; \emph{which} for things; \emph{that} for either (essential clauses).
""",
    questions=[
        Q(context=r"The committee announced \ul{their} decision after a two-hour meeting.",
          choices=[NC, "its", "it's", "they're"], ans=1,
          why=r"``Committee'' is a singular collective noun, so the possessive is ``its.'' ``It's'' = it is."),
        Q(context=r"The coach gave the award to Priya and \ul{I} at the banquet.",
          choices=[NC, "myself", "me", "we"], ans=2,
          why=r"Object of the preposition ``to'': drop ``Priya and'' \(\rightarrow\) ``gave the award to me.'' ``Myself'' needs "
              r"an ``I'' earlier in the clause."),
        Q(context=r"The scientist \ul{who} the panel honored had spent forty years studying coral reefs.",
          choices=[NC, "which", "whose", "whom"], ans=3,
          why=r"Inside the clause, the panel honored \emph{him} \(\rightarrow\) object form ``whom.'' ``Which'' is for things; "
              r"``whose'' shows possession."),
        Q(context=r"When Marcus handed the trophy to Eli, \ul{he} smiled for the cameras.",
          choices=[NC, "Eli", "it", "him"], ans=1,
          why=r"``He'' could mean Marcus or Eli. Naming the person removes the ambiguity; ``it'' and ``him'' are wrong "
              r"in meaning or case."),
    ],
)

modifiers = Section(
    title="Modifiers: Misplaced and Dangling",
    key="modifiers", tag="Modifiers", cat="CSE", stem=STEM,
    body=r"""
\textbf{Rule.} A modifier describes whatever it sits next to.
\begin{itemize}
\item An \textbf{introductory phrase} (\emph{Hiking through the canyon,} / \emph{Built in 1891,}) must be followed
immediately by the noun it describes. Ask: \emph{who or what} is doing the hiking? That noun goes right after the comma.
\item A \textbf{misplaced} modifier in mid-sentence (\emph{brought rice to the diner that was steaming}) must be moved
next to its target (\emph{a steaming plate of rice}).
\end{itemize}
\textbf{Speed tip.} When the choices rearrange a whole clause after an introductory phrase, this is the rule. Find
the choice that starts with the right noun; the rest is usually fine.
""",
    questions=[
        Q(context=r"Hiking through the canyon, \ul{the rock formations amazed the students}.",
          choices=[NC, "the students were amazed by the rock formations",
                   "amazement filled the students at the rock formations",
                   "the rock formations were amazing to the students"], ans=1,
          why=r"``Hiking through the canyon'' must describe the noun right after the comma. Only the students can hike."),
        Q(context=r"Built in 1891, \ul{tourists still flock to the observatory} every summer.",
          choices=[NC, "every year tourists still flock to the observatory", "the observatory still draws tourists",
                   "tourists, who still flock to the observatory,"], ans=2,
          why=r"``Built in 1891'' describes the observatory, so ``the observatory'' must immediately follow the comma."),
        Q(context=r"The waiter brought \ul{a plate of fried rice to the diner that was steaming}.",
          choices=[NC, "a plate of fried rice to the steaming diner",
                   "to the diner, steaming, a plate of fried rice",
                   "a steaming plate of fried rice to the diner"], ans=3,
          why=r"``That was steaming'' sits next to ``the diner,'' so it seems to describe the person. Put the modifier "
              r"next to ``plate.''"),
        Q(context=r"Exhausted after the double shift, \ul{the nurse fell asleep} on the train home.",
          choices=[NC, "sleep overtook the nurse", "the train carried the sleeping nurse", "the nurse's eyes closed"],
          ans=0,
          why=r"``Exhausted after the double shift'' correctly describes the nurse, who follows the comma. The other "
              r"choices make sleep, the train, or the eyes ``exhausted.''"),
    ],
)

parallel = Section(
    title="Parallelism and Comparisons",
    key="parallel", tag="Parallelism / comparison", cat="CSE", stem=STEM,
    body=r"""
\textbf{Parallelism.} Items in a list, or linked by paired conjunctions (\emph{not only\dots but also},
\emph{either\dots or}, \emph{both\dots and}, \emph{not\dots but}), share one grammatical form:
\emph{drafting, analyzing, and presenting}.

\textbf{Comparisons.}
\begin{itemize}
\item Compare like with like: \emph{Austin's population grew faster than \textbf{that of} Dallas} (population vs.\ population).
\item Two things \(\rightarrow\) comparative (\emph{-er}, \emph{more}); three or more \(\rightarrow\) superlative (\emph{-est}, \emph{most}).
\item Adverbs modify verbs and adjectives (\emph{played beautifully}); adjectives modify nouns. \emph{Good} is an
adjective; \emph{well} is the adverb.
\end{itemize}
""",
    questions=[
        Q(context=r"The internship involves drafting reports, analyzing data, and \ul{to present} findings to clients.",
          choices=[NC, "presentation of", "presenting", "the presenting of"], ans=2,
          why=r"The list is built on \emph{-ing} verbs: drafting, analyzing, presenting."),
        Q(context=r"The population of Austin grew faster last decade than \ul{Dallas}.",
          choices=[NC, "that of Dallas", "the city of Dallas", "Dallas, the city"], ans=1,
          why=r"Compare population with population. ``Than Dallas'' compares Austin's population to a city."),
        Q(context=r"Of the two proposals, the second is the \ul{most practical}.",
          choices=[NC, "practicalest", "more practical", "most practically"], ans=2,
          why=r"Two items \(\rightarrow\) comparative ``more,'' not superlative ``most.''"),
        Q(context=r"The pianist played the final movement so \ul{beautiful} that the audience stood before the last "
                  r"note faded.",
          choices=[NC, "beautifuller", "more beautiful", "beautifully"], ans=3,
          why=r"The word modifies the verb ``played,'' so it must be an adverb."),
    ],
)

idioms = Section(
    title="Idioms and Prepositions",
    key="idioms", tag="Idioms", cat="CSE", stem=STEM,
    body=r"""
\textbf{Rule.} Many words take one fixed preposition. No logic decides it; you have to know the pairing.

\smallskip
\begin{tabularx}{\linewidth}{@{}XXX@{}}
opposed \textbf{to} & consistent \textbf{with} & focus \textbf{on} \\
capable \textbf{of} & comply \textbf{with} & responsible \textbf{for} \\
in contrast \textbf{to} & different \textbf{from} & prior \textbf{to} \\
try \textbf{to} (not \emph{try and}) & regardless (not \emph{irregardless}) & interested \textbf{in} \\
\end{tabularx}

\smallskip
\textbf{Between / among.} \emph{Between} for two; \emph{among} for three or more.
\textbf{Test.} Read the phrase without the rest of the sentence: \emph{opposed against}, \emph{consistent to}---which
pairing have you heard in formal writing?
""",
    questions=[
        Q(context=r"Residents were opposed \ul{against} the new highway.",
          choices=[NC, "with", "for", "to"], ans=3, why=r"Idiom: \emph{opposed to}."),
        Q(context=r"The new regulations are consistent \ul{to} federal law.",
          choices=[NC, "with", "on", "by"], ans=1, why=r"Idiom: \emph{consistent with}."),
        Q(context=r"The prize money was divided \ul{between} the five finalists.",
          choices=[NC, "within", "among", "amongst each of"], ans=2,
          why=r"Five people \(\rightarrow\) \emph{among}. \emph{Between} is for two."),
        Q(context=r"The study focused \ul{on} how sleep affects memory.",
          choices=[NC, "at", "to", "for"], ans=0, why=r"Idiom: \emph{focus on}."),
    ],
)

mixed = Section(
    title="Mixed Conventions Passage",
    key="cse-mixed", tag="", cat="CSE",
    intro=r"Work this passage at test pace (about 5 minutes). Every item is a Conventions question; identify the rule "
          r"before choosing.",
    passage_label="PASSAGE", passage_title="Before Sunrise at Moreno's Bakery",
    passage=r"""
At three in the morning, while most of the town \ul{sleep}@@, the ovens at Moreno's Bakery are already roaring.
Luis \ul{Moreno, who}@@ has run the bakery for twenty-two years, starts every morning the same \ul{way, he}@@
checks the sourdough starter his grandfather brought from Oaxaca. The \ul{starters'}@@ tangy smell fills the
kitchen within minutes.

By five o'clock, Luis and his daughter Ana have shaped more than four hundred rolls. \ul{Working quickly, the dough
is divided}@@ into portions that weigh exactly ninety grams. Ana says the hardest part of the job is not the hours
but \ul{to keep}@@ every batch consistent. Customers notice when a loaf is even slightly different, and \ul{they
let Luis know}@@ before they leave.
""",
    questions=[
        Q(stem=STEM, choices=[NC, "are sleeping", "sleeps", "have slept"], ans=2, rule="Subject--verb agreement",
          why=r"``Most of the town'' takes its number from ``town'' (singular) \(\rightarrow\) ``sleeps.''"),
        Q(stem=STEM, choices=[NC, "Moreno who", "Moreno, whom", "Moreno, which"], ans=0,
          rule="Commas: nonessential / intro",
          why=r"The clause is nonessential; this comma opens it and the comma after ``years'' closes it. ``Whom'' is an "
              r"object form; ``which'' is for things."),
        Q(stem=STEM, choices=[NC, "way: he", "way he", "way, and, he"], ans=1, rule="Semicolons / colons",
          why=r"Two ICs joined by a comma alone = splice. A colon works because the second clause explains "
              r"``the same way.''"),
        Q(stem=STEM, choices=[NC, "starters", "starter's", "starters's"], ans=2, rule="Apostrophes",
          why=r"One starter owns the smell: singular possessive."),
        Q(stem=STEM, choices=[NC, "Working quickly, the dough gets divided",
                              "The dough, working quickly, is divided",
                              "Working quickly, they divide the dough"], ans=3, rule="Modifiers",
          why=r"The dough cannot work quickly. The people working (Luis and Ana) must follow the introductory phrase."),
        Q(stem=STEM, choices=[NC, "keeping", "having kept", "to have kept"], ans=1, rule="Parallelism / comparison",
          why=r"``Not the hours but keeping'': the paired items must match. ``Keeping every batch consistent'' is a "
              r"noun phrase, like ``the hours.''"),
        Q(stem=STEM, choices=[NC, "it lets Luis know", "Luis is let know by them", "they lets Luis know"], ans=0,
          rule="Pronouns",
          why=r"``They'' clearly refers to ``Customers'' (plural). ``It'' doesn't agree; ``lets'' doesn't agree with "
              r"``they''; the passive version is ungrammatical."),
    ],
)

GUIDE = Guide(
    slug="1-ACT-English-Conventions",
    kicker="ACT English · Study Guide 1 of 4",
    title="Conventions of Standard English",
    subtitle="Sentence structure, punctuation, and usage",
    short="Conventions of Standard English",
    abstract=r"""Conventions of Standard English is 38--43\% of the enhanced ACT English section---roughly 19--21 of
the 50 questions you face in 35 minutes. Unlike the other two categories, every item here has one rule-based answer.
This guide reduces the category to eleven rules, each stated with the tests and traps the ACT uses, followed
by four practice items written in ACT format (an underlined portion, a question stem, and four choices with
\textsc{no change} first). A mixed passage at the end rehearses switching between rules at test pace. Answer letters
alternate A--D and F--J as on the real test. The answer key on the final pages gives an answers-only strip for quick
checking and a table explaining each answer and naming its rule; tally your misses by rule and reread those sections.""",
    sections=[intro, boundaries, semicolons, commas1, commas2, apostrophes, sva, tense, pronouns, modifiers,
              parallel, idioms, mixed],
)
