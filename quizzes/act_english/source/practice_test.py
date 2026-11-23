from .model import Guide, Q, Section

NC = "NO CHANGE"
G = "Which choice results in a grammatically acceptable sentence?"
T = "Which choice provides the most logical transition?"
C = "Which choice is most concise?"
TONE = "Which choice best maintains the style and tone of the essay?"
W = "Which choice is most precise in context?"

playbook = Section(
    title="Test-Day Playbook",
    key="playbook",
    body=r"""
\textbf{Format.} 50 questions in 35 minutes, about 42 seconds per question. English is always the first section.
Of the 50 items, 40 are scored and 10 are unscored field-test items mixed in without labels---so treat every item
as if it counts. Every question has a stem. The English score (1--36) is one third of your Composite, alongside
Math and Reading. There is no penalty for wrong answers: never leave a bubble blank.

\textbf{Pacing checkpoints.} This practice section has five passages of ten questions. Aim for 7 minutes per passage.

\smallskip
\begin{tabularx}{\linewidth}{@{}XXXXX@{}}
\toprule After Q10 & After Q20 & After Q30 & After Q40 & After Q50 \\ \midrule
7:00 & 14:00 & 21:00 & 28:00 & 35:00 \\ \bottomrule
\end{tabularx}

\smallskip
\textbf{The process at every box.}
\begin{enumerate}[leftmargin=1.6em]
\item Read the passage normally and stop at each boxed number. Read to the end of the sentence first.
\item Read the stem: it tells you whether this is a rule item (grammar, punctuation) or a judgment item (goal, relevance, order).
\item Scan the choices vertically to see what changes. Name the rule (Guides 1--3) before choosing.
\item Eliminate. If two choices are interchangeable, both are wrong. If all are grammatical, take the shortest that keeps the meaning.
\item Questions about the whole passage (placement, purpose) come last: answer them after you finish reading.
\end{enumerate}

\textbf{Where the points are.} Conventions and Knowledge of Language items should take 20--30 seconds; spend the
saved time on Production of Writing items that require holding a whole paragraph in mind. If an item stalls past
60 seconds, guess, mark it, and move on.

\textbf{Scoring this practice section.} Record your raw score out of 50 and the subscores on the first page. ACT
converts raw scores to the 1--36 scale with a different table for each test form, so treat the raw score as your
benchmark and track it across practice tests. When time is called, stop, even mid-passage; on test day, bubble a
guess for every unanswered item.
""",
)

p1 = Section(
    title="Passage I", key="p1", newpage=True,
    intro=r"{\sffamily\small\bfseries Start a 35-minute timer now. Work all five passages without stopping.}", passage_label="PASSAGE I",
    passage_title="The Woman Who Mapped the Ocean Floor",
    passage=r"""
In 1948, Marie Tharp joined a team of Columbia University scientists who were studying the ocean floor. She held
degrees in geology and mathematics, but \ul{women, at the time}@@ were not permitted aboard the research ships that
collected data at sea. So Tharp worked on shore, turning columns of sonar readings into detailed profiles of the
seafloor.

The work was slow and painstaking. Each sounding recorded the depth of the water at a single point, and Tharp had
to plot thousands of them by hand. \ul{Additionally,}@@ patterns began to emerge from the data. In 1952, while
studying profiles of the North Atlantic, she noticed a deep V-shaped notch running along the crest of the
Mid-Atlantic Ridge. She \ul{figured out and concluded}@@ that the notch was a rift valley, a place where the
seafloor was being pulled apart.

Her colleague Bruce Heezen at first dismissed the idea as ``girl talk.'' A rift valley would support the theory of
continental drift, which most American geologists at the time \ul{rejects}@@. Tharp, however, \ul{was persistent
and kept insisting}@@. When Heezen later compared her profiles with records of undersea earthquakes, he found that
the earthquakes clustered along the same narrow line.@@

Over the next two decades, Tharp and Heezen mapped the floors of every ocean. Their 1977 \emph{World Ocean Floor}
map, painted by the Austrian artist Heinrich Berann, \ul{showing}@@ a planet wrapped in a 40,000-mile chain of
underwater mountains. \ul{The map is still sold in some museum gift shops.}@@

Today, Tharp is recognized as one of the scientists whose work helped establish the theory of plate tectonics.
\ul{Tharps}@@ maps, once dismissed as guesswork, now hang in classrooms around the world.@@
""",
    questions=[
        Q(stem=G, choices=[NC, "women at the time,", "women, at the time,", "women; at the time"], ans=2, cat="CSE",
          rule="Commas: nonessential pair",
          why=r"``At the time'' is an interrupter opened by a comma, so it must be closed by one. A single comma "
              r"before ``were'' would split subject and verb."),
        Q(stem=T, choices=[NC, "In contrast,", "For example,", "Gradually,"], ans=3, cat="POW", rule="Transitions",
          why=r"After slow, point-by-point plotting, patterns emerged over time \(\rightarrow\) sequence. Nothing is "
              r"being added, contrasted, or exemplified."),
        Q(stem=C, choices=[NC, "figured out, concluding,", "concluded", "came to the figuring out"], ans=2, cat="KLA",
          rule="Concision / redundancy",
          why=r"``Figured out'' and ``concluded'' mean the same thing; keep the precise one."),
        Q(stem=G, choices=[NC, "rejected", "will reject", "have rejected"], ans=1, cat="CSE", rule="Verb tense",
          why=r"``At the time'' places the rejection in the past, matching the passage's past-tense narration."),
        Q(stem=C, choices=[NC, "was persistent, persisting", "kept persisting and insisting", "persisted"], ans=3,
          cat="KLA", rule="Concision / redundancy",
          why=r"``Was persistent and kept insisting'' says one idea twice; ``persisted'' says it once."),
        Q(stem=r"At this point, the writer is considering adding the following sentence: \emph{The match convinced "
               r"Heezen that Tharp had been right.} Should the writer make this addition?",
          choices=[r"Yes, because it explains what the earthquake data meant for Heezen's view of Tharp's idea.",
                   r"Yes, because it describes how records of undersea earthquakes were collected.",
                   r"No, because it repeats information stated in the preceding sentence.",
                   r"No, because it shifts the paragraph's focus from Tharp to earthquakes."], ans=0, cat="POW",
          rule="Add / delete",
          why=r"The paragraph opens with Heezen dismissing the idea; the sentence completes that arc by showing the "
              r"evidence changed his mind. The preceding sentence gives the data, not his conclusion."),
        Q(stem=G, choices=[NC, "showed", "which showed", "having shown"], ans=1, cat="CSE",
          rule="Sentence boundaries",
          why=r"The subject ``map'' needs a main verb. ``Showing,'' ``which showed,'' and ``having shown'' leave a fragment."),
        Q(stem=r"The writer is considering deleting the underlined sentence. Should it be kept or deleted?",
          choices=[r"Kept, because it shows that the map remains popular.",
                   r"Kept, because it explains how Berann painted the map.",
                   r"Deleted, because it shifts the focus from the map's scientific significance to a minor detail.",
                   r"Deleted, because it contradicts the claim that the map was published in 1977."], ans=2,
          cat="POW", rule="Add / delete",
          why=r"The paragraph and essay are about what Tharp's maps revealed; where copies are sold is trivia. "
              r"The ``Kept'' reasons are false or irrelevant."),
        Q(stem=G, choices=[NC, "Tharps'", "Tharp's", "Tharp"], ans=2, cat="CSE", rule="Apostrophes",
          why=r"One person, Tharp, owns the maps: singular possessive."),
        Q(stem=r"Suppose the writer's primary purpose had been to describe how one scientist's work changed the "
               r"understanding of Earth's structure. Would this essay accomplish that purpose?",
          choices=[r"Yes, because it explains how Tharp's maps revealed a rift valley that supported the theory of "
                   r"continental drift.",
                   r"Yes, because it focuses on the history of sonar technology.",
                   r"No, because it focuses primarily on Heezen's career.",
                   r"No, because it describes the map's artistic qualities rather than its scientific significance."],
          ans=0, cat="POW", rule="Writer's goal",
          why=r"The essay traces Tharp's discovery, its initial rejection, its confirmation, and its role in plate "
              r"tectonics. The other reasons misdescribe the essay."),
    ],
)

p2 = Section(
    title="Passage II", key="p2", newpage=True, passage_label="PASSAGE II", passage_title="Learning the Fold",
    passage=r"""
Every Lunar New Year, my grandmother turns her kitchen table into an assembly line. Bowls of filling, stacks of round
wrappers, and a dish of water for sealing the edges \ul{covers}@@ nearly every inch of the surface. For most of my
childhood, my job was simple: I carried the finished dumplings to the freezer on a floured baking sheet.

When I turned thirteen, my grandmother decided I was ready to fold. She showed me how to place a spoonful of filling
in the center of a wrapper, \ul{wet the edge with a fingertip, and pleating}@@ the dough into a crescent. Her
fingers moved so \ul{quick}@@ that the pleats seemed to appear on their own. \ul{Mine were not as good.}@@

\sn{1} I expected my grandmother to take over. \sn{2} Instead, she slid another wrapper across the table and said,
``Again.'' \sn{3} By the end of the afternoon, my pleats were still uneven, but my dumplings no longer fell apart.
\sn{4} We folded side by side for three \ul{hours, she}@@ corrected my grip whenever my thumb slipped.@@

\ul{Nevertheless,}@@ folding dumplings has become my favorite part of the holiday. I have learned that the pleats
are not only decorative; they also keep the filling \ul{sealed inside}@@ as the dumplings boil. My grandmother, who
learned to fold from her own mother in a village outside Tianjin, \ul{says, that}@@ the hands remember what the mind
forgets. I used to think this was just a saying. Now I \ul{doubt}@@ she is right.
""",
    questions=[
        Q(stem=G, choices=[NC, "cover", "is covering", "has covered"], ans=1, cat="CSE",
          rule="Subject--verb agreement",
          why=r"Three items joined by ``and'' form a plural subject; ``of filling'' and ``of water'' are prepositional "
              r"phrases. Present tense matches ``turns.''"),
        Q(stem=G, choices=[NC, "wetting the edge with a fingertip, and pleat",
                           "wet the edge with a fingertip and then pleating",
                           "wet the edge with a fingertip, and pleat"], ans=3, cat="CSE", rule="Parallelism",
          why=r"The list after ``how to'' is place, wet, pleat---all base verbs."),
        Q(stem=G, choices=[NC, "quickly", "quicker", "quickest"], ans=1, cat="CSE", rule="Adjective vs. adverb",
          why=r"The word modifies the verb ``moved,'' so it must be an adverb."),
        Q(stem=r"Which choice most vividly shows how poorly the narrator's first dumplings turned out?",
          choices=[NC, "Mine were made with the same filling.",
                   "Mine were lumpy and lopsided, and half of them burst open in the boiling water.",
                   "Mine took a while."], ans=2, layout="list", cat="POW", rule="Writer's goal",
          why=r"Only this choice gives concrete detail about the failure; it also sets up ``no longer fell apart'' "
              r"later in the essay."),
        Q(stem=G, choices=[NC, "hours; she", "hours she", "hours, she,"], ans=1, cat="CSE",
          rule="Sentence boundaries",
          why=r"Two independent clauses joined by a comma alone form a splice; a semicolon joins them correctly."),
        Q(stem=r"For the sake of logic and cohesion, Sentence 3 should be placed:",
          choices=["where it is now.", "before Sentence 1.", "after Sentence 1.", "after Sentence 4."], ans=3,
          cat="POW", rule="Placement / order",
          why=r"``By the end of the afternoon'' must follow the three hours of folding in Sentence 4; it is the "
              r"result of that practice."),
        Q(stem=T, choices=[NC, "For example,", "Since then,", "On the other hand,"], ans=2, cat="POW",
          rule="Transitions",
          why=r"The paragraph moves from that first afternoon to the years after \(\rightarrow\) time. Nothing contrasts."),
        Q(stem=C, choices=[NC, "securely sealed and safely enclosed inside", "sealed inside and enclosed",
                           "sealed and also enclosed inside"], ans=0, cat="KLA", rule="Concision / redundancy",
          why=r"``Sealed inside'' is complete; the alternatives repeat the idea of enclosure."),
        Q(stem=G, choices=[NC, "says: that", "says; that", "says that"], ans=3, cat="CSE",
          rule="Unnecessary punctuation",
          why=r"No punctuation goes between a verb and the \emph{that}-clause serving as its object."),
        Q(stem=W, choices=[NC, "deny", "suspect", "dispute"], ans=2, cat="KLA", rule="Word choice",
          why=r"``I used to think this was just a saying'' sets up a change of mind: now the narrator believes the "
              r"grandmother. ``Doubt,'' ``deny,'' and ``dispute'' express the opposite."),
    ],
)

p3 = Section(
    title="Passage III", key="p3", newpage=True, passage_label="PASSAGE III", passage_title="Boston's Great Molasses Flood",
    passage=r"""
On the afternoon of January 15, 1919, people in Boston's North End heard a sharp rattling like machine-gun fire.
Rivets were bursting from the side of a fifty-foot-tall steel tank that held more than two million gallons of
molasses. Within seconds, the tank split open, and a wave of syrup as high as twenty-five feet \ul{roars}@@ through
the neighborhood at an estimated thirty-five miles per hour.

The flood killed twenty-one people and injured about 150 more. It crushed buildings, \ul{bending}@@ the steel
supports of an elevated railway, and trapped horses in the thick, sticky mass. Rescue efforts were slow.
\ul{Similarly,}@@ as the evening air cooled, the molasses thickened, making it nearly impossible for rescuers to wade
through it.

Investigators soon discovered that the tank had been poorly built. It had leaked from the day it was first filled,
and rather than repair it, the company painted it brown so the leaks would be \ul{less noticeable and harder to
see}@@. The man who had overseen its construction was not an engineer and could not read a blueprint.@@

After a lengthy court battle, the tank's owner, the United States Industrial Alcohol Company, \ul{was}@@ found
responsible for the disaster. \ul{The case was in the news.}@@ Massachusetts soon began requiring engineers to sign
and file the calculations for large construction projects, and other states later adopted similar rules.

Today, a small plaque near Langone Park marks the site. Some longtime residents claim that on hot summer days, the
\ul{neighborhood's}@@ streets still smell faintly of molasses. The disaster may sound almost comical a century
later, but for the people of the North End, it was \ul{a total nightmare, no joke}@@.@@
""",
    questions=[
        Q(stem=G, choices=[NC, "has roared", "roared", "will roar"], ans=2, cat="CSE", rule="Verb tense",
          why=r"The event is narrated in the past (``split,'' ``were bursting''), so the paired verb is simple past."),
        Q(stem=G, choices=[NC, "having bent", "were bending", "bent"], ans=3, cat="CSE", rule="Parallelism",
          why=r"The flood crushed, bent, and trapped: three past-tense verbs in a list."),
        Q(stem=T, choices=[NC, "However,", "In part, this was because", "Despite this,"], ans=2, cat="POW",
          rule="Transitions",
          why=r"The thickening molasses explains why rescues were slow \(\rightarrow\) cause. ``Similarly'' (addition) "
              r"and the contrast words do not fit."),
        Q(stem=C, choices=[NC, "harder to see", "less noticeable, harder to see",
                           "harder to see and less noticeable to observers"], ans=1, cat="KLA",
          rule="Concision / redundancy",
          why=r"``Less noticeable'' and ``harder to see'' are the same idea; one is enough."),
        Q(stem=r"At this point, the writer is considering adding the following sentence: \emph{Molasses was "
               r"commonly used to make rum and industrial alcohol.} Should the writer make this addition?",
          choices=[r"Yes, because it explains why the company needed such a large tank.",
                   r"Yes, because it shows how investigators discovered the leaks.",
                   r"No, because it contradicts the claim that the tank leaked.",
                   r"No, because it interrupts the paragraph's focus on how poorly the tank was built."], ans=3,
          cat="POW", rule="Add / delete",
          why=r"The paragraph builds a case about flawed construction; the uses of molasses are off-focus. It "
              r"contradicts nothing."),
        Q(stem=G, choices=[NC, "were", "have been", "are"], ans=0, cat="CSE", rule="Subject--verb agreement",
          why=r"The subject is ``owner'' (singular); the company name is an appositive set off by commas. Past tense "
              r"fits the narration."),
        Q(stem=r"Which choice most effectively introduces the specific change described in the next sentence?",
          choices=[NC, "Many people still remember the flood.", "Boston is one of the oldest cities in the country.",
                   "The disaster also led to stricter rules for designing large structures."], ans=3,
          layout="list", cat="POW", rule="Intro / bridge",
          why=r"The next sentence describes new engineering requirements; only this choice sets them up."),
        Q(stem=G, choices=[NC, "neighborhoods", "neighborhoods'", "neighborhoods's"], ans=0, cat="CSE",
          rule="Apostrophes",
          why=r"One neighborhood (the North End) owns the streets: singular possessive."),
        Q(stem=TONE, choices=[NC, "a tragedy", "super bad", "the worst, like, ever"], ans=1, cat="KLA",
          rule="Style / tone",
          why=r"The essay is serious and informational; ``a tragedy'' fits. The others are slang."),
        Q(stem=r"Suppose the writer's primary purpose had been to explain how molasses is produced and used in "
               r"industry. Would this essay accomplish that purpose?",
          choices=[r"Yes, because it states that the tank held more than two million gallons of molasses.",
                   r"Yes, because it identifies the company that owned the tank.",
                   r"No, because it focuses on the flood and its aftermath rather than on how molasses is made or used.",
                   r"No, because it suggests that molasses is no longer produced."], ans=2, cat="POW",
          rule="Writer's goal",
          why=r"The essay is about a disaster and its consequences; it never explains molasses production. The last "
              r"reason is false."),
    ],
)

p4 = Section(
    title="Passage IV", key="p4", newpage=True, passage_label="PASSAGE IV", passage_title="Old Violins, New Ears",
    passage=r"""
For nearly three hundred years, violins built by Antonio Stradivari have been treated as the finest instruments ever
made. \ul{Its}@@ rich tone has been credited to everything from a secret varnish to the unusually dense wood that
grew in Europe during a cold period known as the Little Ice Age. Today, a single Stradivarius can sell for more than
ten million dollars.

In 2010, a team of researchers led by the acoustics scientist Claudia Fritz set out to test the instruments'
reputation. The team gathered twenty-one experienced violinists in a hotel room in Indianapolis \ul{and, gave}@@ each
of them six violins to play: three new instruments and three old Italian ones, two of them made by Stradivari. To
keep the players from identifying the violins by sight, the researchers dimmed the lights and \ul{took other
steps}@@.

The results surprised nearly everyone. The players could not reliably tell the old violins from the new ones.
\ul{In fact,}@@ the instrument chosen most often as the one a player would take home was new, while the one chosen
least often was a Stradivarius.

Not everyone accepted the findings. Some critics argued that a hotel room was a poor place to judge instruments
designed to fill a concert hall. \ul{Similarly,}@@ Fritz's team ran new experiments in 2012 and 2014, this time in
concert halls in Paris and New York, with audiences listening from the seats. Once again, listeners \ul{generally
preferred}@@ the new violins, which they judged to project their sound more powerfully.

The experiments have not ended the debate. Some dealers and collectors \ul{insists}@@ that a great Stradivarius
reveals its qualities only after months of playing. Others point out that a violin's value comes from its history as
much as its \ul{sound: a}@@ Stradivarius connects a musician to three centuries of great performers.@@ Whatever
science concludes, Stradivari's instruments are likely to remain \ul{mega-pricey}@@ symbols of musical history.
""",
    questions=[
        Q(stem=G, choices=[NC, "Their", "It's", "There"], ans=1, cat="CSE", rule="Pronouns",
          why=r"The antecedent is ``violins'' (plural) \(\rightarrow\) ``their.'' ``It's'' = it is; ``there'' is a place."),
        Q(stem=G, choices=[NC, "and, giving", "and gave,", "and gave"], ans=3, cat="CSE",
          rule="Unnecessary punctuation",
          why=r"``Gathered\dots and gave'' is a compound verb; no comma belongs after ``and'' or between ``gave'' and "
              r"its object."),
        Q(stem=r"Which choice gives the most specific detail about how the researchers hid the violins' identities?",
          choices=[NC, "made sure things were fair", "had the musicians wear modified welders' goggles",
                   "were very careful"], ans=2, layout="list", cat="POW", rule="Writer's goal",
          why=r"Only the goggles are a concrete method; the others are vague."),
        Q(stem=T, choices=[NC, "However,", "Nevertheless,", "Otherwise,"], ans=0, cat="POW", rule="Transitions",
          why=r"The sentence intensifies the previous one: not only could players not tell old from new, they "
              r"actually preferred a new violin \(\rightarrow\) emphasis."),
        Q(stem=T, choices=[NC, "In response,", "For example,", "Even so,"], ans=1, cat="POW", rule="Transitions",
          why=r"The new concert-hall tests answered the critics' objection \(\rightarrow\) response. Nothing is similar "
              r"or exemplified."),
        Q(stem=C, choices=[NC, "preferred and favored generally", "had a general preference and liking for",
                           "generally preferred and liked better"], ans=0, layout="list", cat="KLA",
          rule="Concision / redundancy",
          why=r"``Generally preferred'' is complete; each alternative repeats the idea of preference."),
        Q(stem=G, choices=[NC, "insist", "has insisted", "is insisting"], ans=1, cat="CSE",
          rule="Subject--verb agreement",
          why=r"``Dealers and collectors'' is a compound, plural subject \(\rightarrow\) ``insist.''"),
        Q(stem=G, choices=[NC, "sound; and a", "sound, a", "sound a"], ans=0, cat="CSE", rule="Colons",
          why=r"The colon follows a complete clause and introduces an explanation of why history adds value. The "
              r"comma creates a splice; no punctuation creates a run-on."),
        Q(stem=r"At this point, the writer is considering adding the following sentence: \emph{Cremona, the city "
               r"where Stradivari worked, is also known for its nougat.} Should the writer make this addition?",
          choices=[r"Yes, because it adds an interesting detail about Stradivari's city.",
                   r"Yes, because it explains why Stradivarius violins are valuable.",
                   r"No, because it contradicts the claim that Stradivari worked in Italy.",
                   r"No, because it is unrelated to the paragraph's discussion of why the violins remain prized."],
          ans=3, cat="POW", rule="Add / delete",
          why=r"The paragraph weighs reasons the violins are valued; candy from Cremona is irrelevant. Interesting is "
              r"not the same as relevant."),
        Q(stem=TONE, choices=[NC, "crazy expensive", "treasured", "super-duper valued"], ans=2, cat="KLA",
          rule="Style / tone",
          why=r"The essay's register is formal; ``treasured'' fits. The others are slang."),
    ],
)

p5 = Section(
    title="Passage V", key="p5", newpage=True, passage_label="PASSAGE V", passage_title="Fix It, Don't Toss It",
    passage=r"""
On a Saturday morning in a community center, a retired electrician named Gloria bends over a broken toaster while its
owner watches. Nearby, a tailor patches a pair of \ul{jeans, a teenager}@@ helps an elderly man replace a cracked
phone screen. This is a repair caf\'e, a free event where volunteers help visitors fix \ul{their}@@ broken belongings
instead of throwing them away.

The first repair caf\'e opened in Amsterdam in 2009. Its founder, Martine Postma, was a journalist who worried about
how many usable objects ended up in landfills. \ul{In contrast,}@@ the idea has spread to thousands of locations
around the world, from small towns in the Netherlands to large cities in the United States and Australia.

\sn{1} Most repairs at the caf\'e take less than an hour. \sn{2} Volunteers do not simply fix items for visitors;
they ask the owners to work alongside them. \sn{3} The goal is for visitors to leave not only with a working lamp or
zipper but also \ul{having}@@ the confidence to attempt the next repair on their own. \sn{4} That way, visitors learn
how their belongings actually work.@@

The caf\'es are also part of a larger movement. Supporters of the ``right to repair'' argue that manufacturers
\ul{make it difficult and hard}@@ to fix products by gluing parts together and refusing to sell replacement
components. \ul{Some places have done things about this.}@@

For Gloria, though, repair is less about politics than about \ul{the sheer awesomeness of}@@ fixing something with
her own hands. She has repaired hundreds of \ul{appliances---lamps, radios, coffee makers, even a 1950s jukebox,}@@
since she started volunteering.@@
""",
    questions=[
        Q(stem=G, choices=[NC, "jeans, and a teenager", "jeans a teenager", "jeans, while, a teenager"], ans=1,
          cat="CSE", rule="Sentence boundaries",
          why=r"Two independent clauses need a comma plus a conjunction; the original is a splice and the third "
              r"choice is a run-on."),
        Q(stem=G, choices=[NC, "there", "they're", "it's"], ans=0, cat="CSE", rule="Pronouns / possessives",
          why=r"The visitors own the belongings: possessive ``their.'' ``There'' is a place; ``they're'' = they are."),
        Q(stem=T, choices=[NC, "For instance,", "Nonetheless,", "Since then,"], ans=3, cat="POW",
          rule="Transitions",
          why=r"The paragraph moves from the first caf\'e in 2009 to its later spread \(\rightarrow\) time."),
        Q(stem=G, choices=[NC, "to have", "with", "they have"], ans=2, cat="CSE", rule="Parallelism",
          why=r"``Not only with a working lamp\dots but also with the confidence'': paired items must match."),
        Q(stem=r"For the sake of logic and cohesion, Sentence 4 should be placed:",
          choices=["where it is now.", "before Sentence 1.", "after Sentence 1.", "after Sentence 2."], ans=3,
          cat="POW", rule="Placement / order",
          why=r"``That way'' refers to owners working alongside volunteers (Sentence 2); learning how things work "
              r"then leads into the goal stated in Sentence 3."),
        Q(stem=C, choices=[NC, "make it difficult, hard,", "create a situation in which it is hard and difficult",
                           "make it difficult"], ans=3, layout="list", cat="KLA", rule="Concision / redundancy",
          why=r"``Difficult'' and ``hard'' are synonyms; keep one."),
        Q(stem=r"Which choice provides the most specific support for the idea that the right-to-repair movement has "
               r"gained influence?",
          choices=[NC, "Many people own smartphones.",
                   "In recent years, several U.S. states and the European Union have passed laws requiring "
                   "companies to make repair manuals and spare parts available.",
                   "Some companies make very good products."], ans=2, layout="list", cat="POW",
          rule="Writer's goal",
          why=r"Laws passed in response to the movement are concrete evidence of influence; the others are vague or "
              r"unrelated."),
        Q(stem=TONE, choices=[NC, "the satisfaction of", "how dope it is", "the mega-fun of"], ans=1, cat="KLA",
          rule="Style / tone",
          why=r"``The satisfaction of'' matches the essay's straightforward register; the others are slang."),
        Q(stem=G, choices=[NC, "appliances, lamps, radios, coffee makers, even a 1950s jukebox---",
                           "appliances---lamps, radios, coffee makers, even a 1950s jukebox",
                           "appliances---lamps, radios, coffee makers, even a 1950s jukebox---"], ans=3,
          layout="list", cat="CSE", rule="Dashes (matched pair)",
          why=r"An interruption opened with a dash must close with a dash, not a comma or nothing."),
        Q(stem=r"Suppose the writer's primary purpose had been to describe a community effort that encourages people "
               r"to repair rather than discard their belongings. Would this essay accomplish that purpose?",
          choices=[r"Yes, because it explains that repair caf\'es were invented by an electrician.",
                   r"Yes, because it describes how repair caf\'es work and connects them to a broader movement to "
                   r"make repair easier.",
                   r"No, because it focuses mainly on laws passed by the European Union.",
                   r"No, because it describes only the history of the first repair caf\'e."], ans=1, cat="POW",
          rule="Writer's goal",
          why=r"The essay does this job. The first ``Yes'' gives a false reason: the founder was a journalist."),
    ],
)

GUIDE = Guide(
    slug="4-ACT-English-Full-Practice-Section",
    kicker="ACT English · Study Guide 4 of 4",
    title="Full-Length Practice Section",
    subtitle="50 questions · 35 minutes · five passages",
    short="Full-Length Practice Section",
    subscores=True,
    abstract=r"""This is a complete, timed ACT English practice section in the enhanced format: 50 questions, 35
minutes. Its five original passages (a science biography, a personal narrative, a history piece, an arts-and-science
essay, and a community feature) carry ten questions each, distributed across the three reporting categories in
proportion to the real test: about 40\% Production of Writing, 20\% Knowledge of Language, and 40\% Conventions of
Standard English. Read the Test-Day Playbook, set a 35-minute timer, and work straight through. Write answers in the
blanks, then score with the answer key on the final pages. Each explanation is tagged with its reporting category and
rule, so every miss points you to a specific section of Guides 1--3.""",
    sections=[playbook, p1, p2, p3, p4, p5],
)
