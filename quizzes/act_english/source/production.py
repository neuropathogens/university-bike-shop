from .model import Guide, Q, Section

NC = "NO CHANGE"

intro = Section(
    title="Production of Writing at a Glance",
    key="pow-intro",
    body=r"""
\textbf{What it tests.} Big-picture editing: whether a writer's choices serve the passage. Two strands:
\emph{topic development} (purpose, relevance, adding or deleting material, choices that accomplish a stated goal)
and \emph{organization, unity, and cohesion} (transitions, sentence and paragraph order, introductions and conclusions).

\textbf{Weight.} 38--43\% of the section, about 19--21 of the 50 questions. These items take longer than
Conventions items because you must hold the paragraph's point in mind. Budget 45--60 seconds; bank the time
from fast grammar items.

\textbf{The governing principle.} The question stem defines the job. The right answer is not the best-written
sentence; it is the one that does \emph{exactly} what the stem asks. Underline the goal words in the stem
(\emph{most specific}, \emph{emphasize the danger}, \emph{contrast}, \emph{introduce}) and test each choice against them.

\textbf{Signal table.}\par\smallskip
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.55\linewidth}X@{}}
\toprule \textit{If the stem says\dots} & \textit{Go to} \\ \midrule
``most logical transition'' / ``NOT acceptable'' & \S\ref{sec:transitions} \\
``Should the writer make this addition?'' / ``kept or deleted?'' & \S\ref{sec:relevance} \\
``most specific,'' ``best emphasizes,'' ``accomplishes this purpose'' & \S\ref{sec:purpose} \\
``most logical placement,'' ``order of paragraphs'' & \S\ref{sec:organization} \\
``most effectively introduces / concludes / transitions from the preceding paragraph'' & \S\ref{sec:cohesion} \\
\bottomrule
\end{tabularx}
""",
)

transitions = Section(
    title="Transitions: Logic First, Then the Word",
    key="transitions", tag="Transitions", cat="POW",
    stem="Which choice provides the most logical transition?",
    body=r"""
\textbf{Method.} Cover the transition. Read the sentence before and the sentence after, and name their relationship
in one word. Then choose the transition that signals it.

\smallskip
\begin{tabularx}{\linewidth}{@{}p{0.25\linewidth}X@{}}
\textbf{Contrast} & however, nevertheless, yet, in contrast, on the other hand, instead, still \\
\textbf{Cause/effect} & therefore, thus, consequently, as a result, so, in response \\
\textbf{Addition} & moreover, furthermore, in addition, also, likewise, similarly \\
\textbf{Example} & for example, for instance, specifically \\
\textbf{Time/sequence} & then, later, meanwhile, since then, eventually, finally, gradually \\
\textbf{Emphasis/restating} & in fact, indeed, in other words \\
\end{tabularx}

\smallskip
\textbf{Traps.} (1) Synonyms cancel out: if three choices mean the same thing, none of them is right---or, on a
``NOT acceptable'' item, the odd one out is the answer. (2) When the two sentences have no special relationship,
\emph{deleting} the transition is often best. (3) \emph{However}, \emph{therefore}, and \emph{for example} are not
conjunctions: between two independent clauses they need a semicolon or period in front.
""",
    questions=[
        Q(context=r"Most species of bats rely on echolocation to find food. \ul{Similarly,} fruit bats in the genus "
                  r"\emph{Pteropus} navigate mainly by sight and smell.",
          choices=[NC, "However,", "Therefore,", "For instance,"], ans=1,
          why=r"The second sentence is an exception to the first (most bats echolocate; these do not) \(\rightarrow\) contrast."),
        Q(context=r"The spring rains arrived three weeks late. \ul{Nevertheless,} farmers in the valley delayed planting "
                  r"their corn.",
          choices=[NC, "In contrast,", "As a result,", "For example,"], ans=2,
          why=r"The late rain caused the delay \(\rightarrow\) cause/effect. ``Nevertheless'' would signal an unexpected "
              r"outcome, but delay is the expected one."),
        Q(context=r"Some everyday materials were invented by accident. \ul{Thus,} Velcro was inspired by burrs that clung "
                  r"to an engineer's dog during a hike in the Alps.",
          choices=[NC, "In contrast,", "Nevertheless,", "For example,"], ans=3,
          why=r"Velcro is one instance of an accidental invention \(\rightarrow\) example."),
        Q(context=r"The new greenhouse cut the school's heating costs. \ul{In addition,} it gave biology classes a place "
                  r"to grow seedlings year-round.",
          choices=[NC, "However,", "Instead,", "Otherwise,"], ans=0,
          why=r"The second sentence adds a second benefit \(\rightarrow\) addition."),
        Q(context=r"The museum's attendance doubled after it stopped charging admission; \ul{consequently,} the board "
                  r"voted to keep the free-admission policy.",
          stem=r"Which of the following alternatives to the underlined portion would NOT be acceptable?",
          choices=["as a result,", "nevertheless,", "therefore,", "thus,"], ans=1,
          why=r"Rising attendance is the reason for keeping the policy (cause/effect). Three choices say ``because of "
              r"this''; ``nevertheless'' signals contrast and is the odd one out."),
        Q(context=r"The forecast called for clear \ul{skies, however,} a thunderstorm rolled in by noon.",
          stem="Which choice results in a grammatically acceptable sentence?", rule="Transitions (punctuation)",
          choices=[NC, "skies; however,", "skies, however", "skies however,"], ans=1,
          why=r"``However'' is not a conjunction. When it begins the second of two independent clauses, it needs a "
              r"semicolon (or period) before it and a comma after it."),
        Q(context=r"The museum opens at nine o'clock. \ul{In other words,} the caf\'e inside serves breakfast until eleven.",
          choices=[NC, "For example,", "Consequently,", r"DELETE the underlined portion and capitalize \emph{the}."],
          ans=3, layout="list",
          why=r"The two facts are simply listed: no restatement, example, or cause. When no special relationship "
              r"exists, delete the transition."),
    ],
)

relevance = Section(
    title="Relevance: Add, Delete, Keep",
    key="relevance", tag="Add / delete", cat="POW",
    body=r"""
\textbf{The question.} ``Should the writer make this addition?'' or ``Should the sentence be kept or deleted?''
Two choices say Yes/Kept, two say No/Deleted, each with a reason.

\textbf{Method.}
\begin{enumerate}[leftmargin=1.6em]
\item State the paragraph's specific focus in a few words (not the topic---the \emph{point}).
\item Decide Yes or No: does the sentence directly support that point? Interesting but off-focus details go.
\item Choose between the two remaining reasons. The right reason must be \emph{true}: it has to describe what
the sentence actually does. A ``Yes'' with a false reason is wrong.
\end{enumerate}
\textbf{Traps.} A reason that is accurate about the world but not about the passage; ``it repeats information''
when nothing was repeated; ``it contradicts'' when nothing was contradicted.
""",
    questions=[
        Q(context=r"\sn{1} In 1913, Henry Ford introduced the moving assembly line at his Highland Park plant in "
                  r"Michigan. \sn{2} The change cut the time needed to build a Model T from more than twelve hours to "
                  r"about ninety minutes. \sn{3} Ford also experimented with soybeans as a source of plastic for car "
                  r"parts. \sn{4} Lower production costs allowed Ford to drop the car's price, putting automobiles "
                  r"within reach of millions of families.",
          stem=r"The writer is considering deleting Sentence 3. Should the sentence be kept or deleted?",
          choices=[r"Kept, because it shows that Ford's interest in innovation extended beyond the assembly line.",
                   r"Kept, because it explains how Ford was able to lower the price of the Model T.",
                   r"Deleted, because it interrupts the paragraph's focus on how the assembly line affected "
                   r"production time and prices.",
                   r"Deleted, because it contradicts the claim that Ford reduced production time."], ans=2,
          why=r"Sentences 1, 2, and 4 form a cause-and-effect chain: assembly line \(\rightarrow\) faster production "
              r"\(\rightarrow\) lower prices. The soybean detail breaks the chain. Choice ``explains how Ford lowered the "
              r"price'' misdescribes the sentence."),
        Q(context=r"Tardigrades, microscopic animals often called water bears, are among the hardiest creatures on "
                  r"Earth. They can survive temperatures near absolute zero and pressures several times greater than "
                  r"those at the bottom of the deepest ocean trench.",
          stem=r"At this point, the writer is considering adding the following sentence: \emph{In 2007, researchers "
               r"sent tardigrades into orbit, where many survived direct exposure to the vacuum of space.} "
               r"Should the writer make this addition?",
          choices=[r"Yes, because it provides another example supporting the claim that tardigrades are "
                   r"exceptionally hardy.",
                   r"Yes, because it explains why tardigrades are called water bears.",
                   r"No, because it shifts the focus from tardigrades to space exploration.",
                   r"No, because it repeats information stated earlier in the paragraph."], ans=0,
          why=r"The paragraph claims tardigrades are extremely hardy and lists extreme conditions they survive; space "
              r"is one more. Nothing earlier mentions space, so it is not repetitive, and the focus stays on "
              r"tardigrades."),
        Q(context=r"\sn{1} Our neighborhood's community garden started with just six raised beds. \sn{2} Within two "
                  r"years, it had grown to forty beds tended by families from twelve countries. \sn{3} Many of "
                  r"those families grow vegetables that are hard to find in local stores, such as bitter melon "
                  r"and Thai chili peppers. \sn{4} On Saturday mornings, gardeners swap seeds and recipes at a table "
                  r"near the gate.",
          stem=r"The writer is considering deleting Sentence 3. Should the sentence be kept or deleted?",
          choices=[r"Kept, because it explains how the garden grew from six beds to forty.",
                   r"Kept, because it gives a specific detail showing how the garden reflects the backgrounds of "
                   r"the families who tend it.",
                   r"Deleted, because it introduces a topic unrelated to the garden.",
                   r"Deleted, because the information is already stated in Sentence 2."], ans=1,
          why=r"The paragraph's point is that families from many countries share the garden; naming vegetables "
              r"from home supports it. The sentence says nothing about the garden's growth."),
        Q(context=r"Glass frogs, found in the rainforests of Central and South America, have translucent skin on "
                  r"their bellies through which their hearts and other organs are visible. When they sleep, many "
                  r"glass frogs hide most of their red blood cells in their livers, making their bodies even more "
                  r"transparent.",
          stem=r"At this point, the writer is considering adding the following sentence: \emph{Rainforests cover "
               r"about six percent of Earth's land surface.} Should the writer make this addition?",
          choices=[r"Yes, because it explains where glass frogs live.",
                   r"Yes, because it shows why transparency helps the frogs survive.",
                   r"No, because it contradicts the claim that glass frogs live in Central and South America.",
                   r"No, because it gives a general fact about rainforests that is unrelated to the paragraph's "
                   r"focus on the frogs' transparency."], ans=3,
          why=r"The paragraph is about how glass frogs achieve transparency; a statistic about rainforest area is "
              r"off-focus. It does not contradict anything."),
    ],
)

purpose = Section(
    title=r"Purpose: ``Which Choice Best Accomplishes\dots''",
    key="purpose", tag="Writer's goal", cat="POW",
    body=r"""
\textbf{Rule.} Read the goal in the stem literally and test each choice against it. Every choice is usually
grammatical and true; three simply do a different job.
\begin{itemize}
\item \textbf{``Most specific / vivid / concrete''} \(\rightarrow\) numbers, names, sensory detail. Vague words
(\emph{a lot}, \emph{very}, \emph{things}) lose.
\item \textbf{``Best emphasizes X''} \(\rightarrow\) the choice must be \emph{about} X, not merely compatible with it.
\item \textbf{``Contrast'' / ``comparison''} \(\rightarrow\) the choice must address the same features named in the
other half of the contrast.
\item \textbf{``Suppose the writer's primary purpose had been\dots''} \(\rightarrow\) decide whether the essay
actually does that job. The answer is frequently No, because the essay does something narrower or different.
Then pick the reason that accurately describes the essay.
\end{itemize}
""",
    questions=[
        Q(context=r"The hurricane \ul{caused a lot of damage to} the small coastal town.",
          stem=r"Which choice provides the most specific description of the storm's effect on the town?",
          choices=[NC, "was very destructive to", "tore the roofs from more than two hundred homes in",
                   "affected many people in"], ans=2, layout="list",
          why=r"Only this choice gives a concrete, measurable detail; the others are vague restatements."),
        Q(context=r"\ul{Computers come in many shapes and sizes.} Today, a single smartphone holds far more computing "
                  r"power than the guidance computer that carried astronauts to the Moon. Engineers can now fit "
                  r"billions of transistors onto a chip smaller than a fingernail.",
          stem=r"Which choice most effectively introduces the main idea of the paragraph?",
          choices=[NC, "Many people use smartphones every day.", "The first Moon landing took place in 1969.",
                   "Over the past fifty years, computers have become dramatically smaller and more powerful."],
          ans=3, layout="list",
          why=r"Both supporting details show computers shrinking while gaining power. The other choices are too broad "
              r"or name a single detail."),
        Q(context=r"The old stadium had splintered wooden bleachers and no roof; the new stadium, by contrast, "
                  r"\ul{opened in 2024}.",
          stem=r"Given that all the choices are accurate, which one most effectively completes the contrast set up "
               r"in this sentence?",
          choices=[NC, "seats 40,000 fans in cushioned chairs beneath a retractable roof",
                   "was designed by a local architecture firm", "hosts concerts as well as games"], ans=1,
          layout="list",
          why=r"The contrast concerns seating and roofing; only this choice addresses both."),
        Q(context=r"My grandfather's first radio was a crystal set he built from a kit when he was twelve. He "
                  r"remembers lying awake at night, headphones pressed to his ears, listening to baseball games "
                  r"broadcast from hundreds of miles away. Decades later, he still talks about those summer nights "
                  r"as the moment he fell in love with the game.",
          stem=r"Suppose the writer's primary purpose had been to explain how crystal radios convert radio signals "
               r"into sound. Would this paragraph accomplish that purpose?",
          choices=[r"Yes, because it describes the kit the grandfather used to build his radio.",
                   r"Yes, because it explains that the radio could receive signals from hundreds of miles away.",
                   r"No, because it focuses on the grandfather's memories of listening to the radio rather than on "
                   r"how the device works.",
                   r"No, because it suggests that crystal radios could not receive baseball broadcasts."], ans=2,
          why=r"The paragraph is a memory, not a technical explanation. Both ``Yes'' reasons cite true details that "
              r"still explain nothing about how the device works; the last ``No'' reason is false."),
        Q(context=r"The climbers picked their way across the glacier, \ul{stopping often to rest}.",
          stem=r"Which choice most effectively emphasizes the danger of the crossing?",
          choices=[NC, "stepping around hidden crevasses more than a hundred feet deep", "following their guide",
                   "talking about the view"], ans=1, layout="list",
          why=r"Only hidden, hundred-foot crevasses convey danger; the others describe ordinary activity."),
    ],
)

organization = Section(
    title="Organization: Sentence and Paragraph Order",
    key="organization", tag="Placement / order", cat="POW",
    body=r"""
\textbf{Rule.} Logical order is built from clues inside the sentences. Look for:
\begin{itemize}
\item \textbf{Reference words}---\emph{this, these, that, such, there, its, the device}. A sentence that says
\emph{its trunk} must follow the sentence that introduces the tree.
\item \textbf{Time markers}---\emph{first, then, by November, later, finally}. Put events in chronological order.
\item \textbf{General \(\rightarrow\) specific.} A claim comes before the example that supports it.
\item \textbf{Set-up \(\rightarrow\) payoff.} A paragraph that raises a question precedes the one that answers it.
\end{itemize}
\textbf{Method.} Find the reference word in the sentence being moved, locate what it refers to, and test the
answer choice by reading the paragraph in that order. Check both neighbors: the sentence must fit with what comes
before \emph{and} after.
""",
    questions=[
        Q(context=r"\sn{1} The first step in building the canoe was selecting the right cedar log. \sn{2} After weeks "
                  r"of searching, Joseph found a tree that had fallen in a winter storm. \sn{3} Then he and his "
                  r"cousins hollowed out the log using adzes and controlled fires. \sn{4} Finally, they steamed the "
                  r"hull so the sides could be spread wider.",
          stem=r"The writer wants to add the following sentence to the paragraph: \emph{Its trunk was straight, "
               r"nearly free of knots, and wide enough for two paddlers to sit side by side.} The sentence would "
               r"most logically be placed after:",
          choices=["Sentence 1.", "Sentence 2.", "Sentence 3.", "Sentence 4."], ans=1,
          why=r"``Its trunk'' needs a tree to refer to; the tree first appears in Sentence 2. The description also "
              r"explains why this tree was chosen, so it belongs before the hollowing begins."),
        Q(context=r"\sn{1} Monarch butterflies begin their southward migration in late summer. \sn{2} By November, "
                  r"millions of them have reached the fir forests of central Mexico. \sn{3} Some travel more than "
                  r"2,500 miles from Canada and the northern United States. \sn{4} There, they cluster on the "
                  r"branches so densely that the trees appear orange.",
          stem=r"For the sake of logic and cohesion, Sentence 3 should be placed:",
          choices=["where it is now.", "before Sentence 1.", "after Sentence 1.", "after Sentence 4."], ans=2,
          why=r"``There'' in Sentence 4 must point to the forests in Sentence 2, so nothing can sit between them. "
              r"After Sentence 1, the distance detail follows the start of the trip and precedes the arrival."),
        Q(context=r"\sn{1} That first planting has since grown into one of the nation's best-known traditions; today, "
                  r"the National Cherry Blossom Festival celebrates both the trees and the friendship they "
                  r"represent.\par\smallskip"
                  r"\sn{2} Each spring, the cherry trees around Washington, D.C.'s Tidal Basin burst into bloom, "
                  r"drawing more than a million visitors. Few of those visitors know how the trees got there.\par\smallskip"
                  r"\sn{3} The trees arrived in 1912 as a gift from the mayor of Tokyo. That March, First Lady Helen "
                  r"Taft and the wife of the Japanese ambassador planted the first two trees.",
          stem=r"Which order of the three paragraphs is most logical?",
          choices=["1, 2, 3 (as they are now)", "1, 3, 2", "2, 3, 1", "3, 1, 2"], ans=2,
          why=r"Paragraph 2 raises a question (how did the trees get there?), Paragraph 3 answers it, and Paragraph "
              r"1's ``That first planting'' points back to the planting in Paragraph 3."),
    ],
)

cohesion = Section(
    title="Cohesion: Introductions, Conclusions, and Bridges",
    key="cohesion", tag="Intro / conclusion / bridge", cat="POW",
    body=r"""
\textbf{Topic sentences} state the point that every later sentence in the paragraph supports. Test a choice by
asking whether \emph{all} of the paragraph's details fit under it---not just one of them.

\textbf{Conclusions} restate or extend the paragraph's (or essay's) main idea. A new, minor fact is never a
conclusion. When the stem says ``connect back to the first paragraph,'' find the specific idea there and choose the
choice that echoes it.

\textbf{Bridges between paragraphs} must touch \emph{both} sides: something from the end of the preceding paragraph
and something from the new one. A choice that mentions only one side fails.
""",
    questions=[
        Q(context=r"When I started volunteering at the animal shelter, I expected to spend my afternoons playing with "
                  r"puppies. Instead, I spent most of my time with older dogs that had been overlooked for months. I "
                  r"learned to sit quietly in their kennels until they trusted me enough to approach. \ul{The shelter "
                  r"is open seven days a week.}",
          stem=r"Which choice most effectively concludes the paragraph by reflecting its main idea?",
          choices=[NC, "Those slow, quiet afternoons taught me that trust is earned, not demanded.",
                   "Puppies are usually adopted within a few days.", "Some dogs are afraid of loud noises."], ans=1,
          layout="list",
          why=r"The paragraph is about what the narrator learned from slowly earning the dogs' trust. The other "
              r"choices add new, minor facts."),
        Q(context=r"\ul{Bees are insects.} In a single day, a colony's foragers can visit thousands of blossoms, "
                  r"carrying the pollen that allows apple, almond, and blueberry crops to produce fruit. Without them, "
                  r"farmers would have to pollinate many crops by hand, a slow and expensive process.",
          stem=r"Which choice most effectively introduces the paragraph?",
          choices=[NC, "Honey has been used as a food for thousands of years.",
                   "Honeybees play an essential role in the production of many crops.",
                   "Some bees live alone rather than in colonies."], ans=2, layout="list",
          why=r"Every detail concerns bees pollinating crops; the topic sentence must state that idea. The others "
              r"are about honey or solitary bees."),
        Q(context=r"\textit{[The preceding paragraph ends:]} Yellow fever and malaria killed thousands of workers "
                  r"during France's failed attempt to build the Panama Canal in the 1880s.\par\smallskip"
                  r"\ul{The canal connects two oceans.} When the United States took over the project in 1904, "
                  r"Dr.\ William Gorgas launched a campaign to drain standing water and destroy the mosquitoes that "
                  r"carried both diseases.",
          stem=r"Which choice provides the most effective transition from the preceding paragraph to this one?",
          choices=[NC, "Ships today pay tolls to use the canal.", "France had also built the Suez Canal.",
                   "The United States was determined not to repeat that tragedy."], ans=3, layout="list",
          why=r"The bridge must link the French deaths (``that tragedy'') to the American campaign (``determined not "
              r"to repeat''). The other choices touch neither side."),
    ],
)

mixed = Section(
    title="Mixed Production of Writing Passage",
    key="pow-mixed", tag="", cat="POW",
    intro=r"Work this passage at test pace (about 5--6 minutes). Read the whole passage, answering items as you reach "
          r"their boxes; save the final item until you have finished reading.",
    passage_label="PASSAGE", passage_title="The Library on Wheels",
    passage=r"""
When the county closed the library branch in Millbrook, residents worried that children in the small farming town
would lose access to books. \ul{Therefore,}@@ the library board had a plan: a converted school bus, painted bright
blue and lined with shelves, would visit Millbrook every Tuesday afternoon.

The bookmobile carries about three thousand books, two laptops with internet access, and a small printer. Its
driver, Carol Jenkins, is also a trained librarian. \ul{Jenkins grew up in a city two hundred miles away.}@@ She
knows most of her regular visitors by name and often sets aside new titles she thinks they will enjoy.

\sn{1} On a typical Tuesday, the first visitors arrive before the bus has even parked. \sn{2} Teenagers come next,
many of them to use the laptops for homework. \sn{3} Parents with toddlers are usually first in line, hoping to
catch the weekly story hour. \sn{4} By evening, the regulars are farmers stopping by after work to return books on
tractor repair and pick up the latest mysteries.@@

The bookmobile has also become a gathering place. \ul{People like it a lot.}@@ Neighbors who rarely see one another
during harvest season linger on the folding chairs Jenkins sets out, trading news and recipes.

Last spring, the bus's engine failed, and the library could not afford repairs. \ul{For instance,}@@ residents
organized a pancake breakfast that raised enough money to replace it within a month. \ul{The bus is blue.}@@@@
""",
    questions=[
        Q(stem="Which choice provides the most logical transition?",
          choices=[NC, "For example,", "Similarly,", "However,"], ans=3, rule="Transitions",
          why=r"Residents feared losing access; the board had a solution \(\rightarrow\) contrast."),
        Q(stem=r"The writer is considering deleting the underlined sentence. Should it be kept or deleted?",
          choices=[r"Kept, because it explains why Jenkins became a librarian.",
                   r"Kept, because it shows that Jenkins knows the town well.",
                   r"Deleted, because it distracts from the paragraph's focus on the services Jenkins provides.",
                   r"Deleted, because it contradicts the claim that Jenkins is a trained librarian."],
          ans=2, rule="Add / delete",
          why=r"The paragraph is about what the bookmobile and its driver offer visitors; her hometown is off-focus. "
              r"It does not show she knows the town (if anything, the opposite)."),
        Q(stem=r"For the sake of logic and cohesion, Sentence 3 should be placed:",
          choices=["where it is now.", "before Sentence 1.", "after Sentence 1.", "after Sentence 4."], ans=2,
          rule="Placement / order",
          why=r"``The first visitors arrive'' \(\rightarrow\) parents ``first in line'' \(\rightarrow\) teenagers ``next'' "
              r"\(\rightarrow\) farmers ``by evening.'' Sentence 3 must precede ``next.''"),
        Q(stem=r"Which choice most effectively supports the claim made in the preceding sentence?",
          choices=[NC, "Some Tuesdays, more people come to talk than to borrow books.",
                   "The bus gets about eight miles per gallon.", "Many towns have bookmobiles."], ans=1,
          rule="Writer's goal",
          why=r"The claim is that the bookmobile is a gathering place; people coming to talk rather than borrow is "
              r"direct evidence."),
        Q(stem="Which choice provides the most logical transition?",
          choices=[NC, "Otherwise,", "Similarly,", "In response,"], ans=3, rule="Transitions",
          why=r"The fundraiser was a reaction to the engine failure \(\rightarrow\) cause/response. A pancake "
              r"breakfast is not an example of the failure."),
        Q(stem=r"Which choice most effectively concludes the essay by connecting back to the residents' worry "
               r"described in the first paragraph?",
          choices=[NC, "Millbrook's children, it turns out, did not lose their library; it simply learned to come "
                       "to them.", "The library board meets on the first Monday of each month.",
                   "Pancake breakfasts are a popular fundraiser in rural areas."], ans=1, layout="list",
          rule="Intro / conclusion / bridge",
          why=r"The first paragraph's worry was that children would lose access to books; only this choice answers it."),
        Q(stem=r"Suppose the writer's primary purpose had been to describe how a public service adapted to meet a "
               r"community's needs. Would this essay accomplish that purpose?",
          choices=[r"Yes, because it describes how the library replaced a closed branch with a bookmobile that "
                   r"serves Millbrook residents in several ways.",
                   r"Yes, because it explains how library buses are built and equipped.",
                   r"No, because it focuses mainly on the career of the bus driver.",
                   r"No, because it describes only the fundraiser that replaced the engine."], ans=0,
          rule="Writer's goal",
          why=r"The essay does exactly this: branch closes \(\rightarrow\) bookmobile serves children, teens, farmers, and "
              r"neighbors. The other reasons misdescribe the essay."),
    ],
)

GUIDE = Guide(
    slug="2-ACT-English-Production-of-Writing",
    kicker="ACT English · Study Guide 2 of 4",
    title="Production of Writing",
    subtitle="Topic development, organization, unity, and cohesion",
    short="Production of Writing",
    abstract=r"""Production of Writing is 38--43\% of the enhanced ACT English section---roughly 19--21 of 50
questions. These are the ``editor's judgment'' items: choosing transitions, deciding whether a sentence should be
added or deleted, picking the choice that accomplishes a stated goal, ordering sentences and paragraphs, and judging
introductions and conclusions. Because every enhanced ACT item now carries a question stem, the stem is the key: it
names the job, and the right answer is the one that does that job. This guide gives a method for each item type,
practice items in ACT format, and a full mixed passage. The answer key on the final pages lists answers only, then
explains each answer and names its rule.""",
    sections=[intro, transitions, relevance, purpose, organization, cohesion, mixed],
)
