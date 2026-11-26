from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph, Series

GROWTH = Graph(r"Time (days)", r"Paramecia per mL", x=(0, 14, 2), y=(0, 700, 100),
               series=[Series("culture", [(0, 20), (2, 62), (4, 165), (6, 335), (8, 484), (10, 560), (12, 587), (14, 596)])])

S1 = Sec("Responses to the environment (8.1)", ["8.1"], r"""
Organisms respond to information from their environment and from one another.
\begin{terms}
Taxis & directed movement toward or away from a stimulus (moths flying to light) \\
Kinesis & a change in the rate or turning of random movement in response to a stimulus (pill bugs moving more in dry places, less in damp ones) \\
Communication & visual, auditory, tactile and chemical signals (pheromones, the honeybee waggle dance, warning coloration) that change the behavior of others and can raise fitness \\
Cooperative behavior & helping relatives or the group (alarm calls, shared hunting) increases the survival of shared genes \\
Physiological responses & hibernation, estivation, seasonal coat changes; in plants, phototropism and photoperiodism \\
\end{terms}
""", checks=[
    Q("8.1 Kinesis", r"Pill bugs placed in a chamber with a damp side and a dry side move quickly and turn often on the dry side and slow down on the damp side, so they collect on the damp side. This behavior is an example of",
      r"kinesis", [r"taxis", r"learned behavior", r"phototropism"],
      r"Their movement is random in direction; only its rate changes with humidity.",
      [r"Taxis: directed. Kinesis: undirected, rate changes."],
      [r"taxis is movement directly toward or away from the stimulus.",
       r"the response is innate.",
       r"phototropism is a plant's growth toward light."]),
])

S2 = Sec("Energy flow through ecosystems (8.2)", ["8.2"], r"""
\textbf{Producers} (autotrophs) capture energy: most by photosynthesis, some (chemoautotrophs, at deep-sea vents) from inorganic chemicals. \textbf{Consumers} (heterotrophs) eat other organisms; \textbf{decomposers} break down dead matter, returning nutrients to the soil and water.

\textbf{The 10\% rule.} At each step up a food chain, only about $10\%$ of the energy is stored in the next level's biomass; most is released as heat by cellular respiration or never eaten. So food chains are short and the top level is small. Endotherms (birds, mammals) spend much more energy keeping warm than ectotherms do, so they need more food per gram of body mass.

Unlike energy, matter cycles: carbon (photosynthesis and respiration), nitrogen (fixation by bacteria into usable forms), phosphorus (weathering of rock, no atmospheric form) and water.
""", checks=[
    Q("8.2 Energy transfer", r"The producers in an ecosystem capture $10\,000$ kcal of energy. Using the $10\%$ rule, about how much reaches the tertiary consumers?",
      r"$10$ kcal", [r"$100$ kcal", r"$1000$ kcal", r"$1$ kcal"],
      r"Producers $\to$ primary ($1000$) $\to$ secondary ($100$) $\to$ tertiary ($10$ kcal).",
      [r"Divide by $10$ for each step."],
      [r"is the secondary consumers.",
       r"is the primary consumers.",
       r"takes one step too many."], sort=True),
])

S3 = Sec("Population ecology and the effect of density (8.3--8.4)", ["8.3", "8.4"], r"""
\[ \frac{dN}{dt} = r_{max}N \ \ (\text{exponential}), \qquad \frac{dN}{dt} = r_{max}N\,\frac{K - N}{K} \ \ (\text{logistic}). \]
With unlimited resources a population grows exponentially (a J-shaped curve). As resources run short, growth slows and levels off at the \textbf{carrying capacity} $K$ (an S-shaped, logistic curve). Logistic growth is fastest at $N = K/2$.

\textbf{Limiting factors.} Density-dependent factors (competition for food or space, disease, predation, waste build-up) have more effect in crowded populations. Density-independent factors (floods, fires, freezes) affect a population regardless of its size.
""", checks=[
    Q("8.3 Logistic growth", r"A population with $r_{max} = 0.50$ per year and carrying capacity $K = 1000$ has $400$ individuals. What is its growth rate, $dN/dt$?",
      r"$120$ individuals per year", [r"$200$ individuals per year", r"$80$ individuals per year", r"$300$ individuals per year"],
      r"$dN/dt = (0.50)(400)\frac{1000 - 400}{1000} = 200 \times 0.60 = 120$ per year.",
      [r"Exponential rate $r_{max}N$, reduced by the fraction of $K$ still unused."],
      [r"is the exponential rate, ignoring $K$.",
       r"multiplies by $N/K$ instead of $(K - N)/K$.",
       r"multiplies $r_{max}$ by $K - N$ instead of by $N$."], sort=True),
])

S4 = Sec("Community ecology (8.5)", ["8.5"], r"""
\begin{compare}{Interaction}{Effect on each species}{Example}
Competition & $-/-$ & two bird species eating the same seeds \\
Predation, herbivory & $+/-$ & lynx and hare; deer and shrubs \\
Parasitism & $+/-$ & tapeworm and host \\
Mutualism & $+/+$ & lichens (fungus and alga); pollinators and flowers \\
Commensalism & $+/0$ & barnacles on a whale \\
\end{compare}
A species' \textbf{niche} is its role and its use of resources. Two species cannot occupy the same niche indefinitely (competitive exclusion); they may instead divide the resources (resource partitioning). Predator and prey populations often cycle, with the predator's peaks lagging the prey's. Changes at one trophic level can cascade through others.
""", checks=[
    Q("8.5 Mutualism", r"Lichens consist of a fungus and an alga living together. The alga supplies sugars by photosynthesis, and the fungus provides water, minerals and protection. This relationship is",
      r"mutualism", [r"parasitism", r"commensalism", r"competition"],
      r"Both partners benefit ($+/+$).",
      [r"Both gain: mutualism."],
      [r"parasitism harms one partner.",
       r"commensalism leaves one partner unaffected.",
       r"competition harms both."]),
])

S5 = Sec("Biodiversity (8.6)", ["8.6"], r"""
Biodiversity includes the genetic diversity within species, the number and relative abundance of species, and the variety of ecosystems. More diverse ecosystems tend to be more resilient to disturbance. A \textbf{keystone species} has an effect far larger than its abundance suggests (sea otters eat sea urchins, which would otherwise destroy kelp forests).

\textbf{Simpson's diversity index} (on the formula sheet) is
\[ D = 1 - \sum\left(\frac{n}{N}\right)^2 , \]
with $n$ the number of individuals of each species and $N$ the total. It runs from $0$ (one species) toward $1$ (many species in similar numbers).
""", checks=[
    Q("8.6 Keystone species", r"When sea otters were hunted almost to extinction along parts of the Pacific coast, kelp forests disappeared. What is the best explanation?",
      r"Without otters, sea urchin populations grew and overgrazed the kelp.", [r"Otters fertilized the kelp, which could not grow without them.", r"Kelp and otters compete for the same food.", r"The kelp was harvested by the same hunters."],
      r"Otters are a keystone predator: by keeping urchins in check, they protect the kelp and the community that depends on it.",
      [r"A trophic cascade."],
      [r"the link is through the otters' prey.",
       r"otters eat animals; kelp makes its own food.",
       r"the effect follows the otters' removal."]),
])

S6 = Sec("Disruptions in ecosystems (8.7)", ["8.7"], r"""
Ecosystems change through natural events (volcanoes, fires, droughts, El Ni\~no) and human activity (habitat destruction, pollution, overharvesting, climate change, introduction of species). \textbf{Invasive species} often spread rapidly because their new habitat lacks the predators, parasites and competitors that held them in check. Nutrient runoff causes eutrophication: algal blooms die and their decomposition uses up the water's oxygen. Populations with genetic variation are more likely to include individuals that can survive a change; species with long generation times and little variation are especially vulnerable.
""", checks=[
    Q("8.7 Invasive species", r"Why do many invasive species increase rapidly in their new habitats?",
      r"Their new habitat lacks the predators, parasites and competitors that limited them where they evolved.", [r"They have higher mutation rates than native species.", r"They are always larger than native species.", r"They cannot be affected by density-dependent factors."],
      r"Released from natural enemies, they can outcompete native species.",
      [r"Enemy release."],
      [r"mutation rates are not the explanation.",
       r"size varies; many invaders are small.",
       r"they become limited by density eventually."]),
])

QS = [
    Set("Behavior and energy flow (8.1--8.2)", [
        Q("8.1 Communication", r"A honeybee returning from a rich patch of flowers performs a waggle dance. What is its function?",
          r"It tells other workers the direction and distance of the food.", [r"It warns other bees of a predator.", r"It attracts a mate.", r"It cools the hive."],
          r"The angle of the waggle run relative to vertical shows the direction relative to the Sun, and its length shows the distance.",
          [r"Communication that changes the behavior of others."],
          [r"bees use alarm pheromones for warning.",
           r"workers are sterile females.",
           r"fanning, not dancing, cools the hive."]),
        Q("8.2 Ten percent rule", r"Producers in a lake capture $50\,000$ kJ of energy. About how much energy reaches the secondary consumers?",
          r"$500$ kJ", [r"$5000$ kJ", r"$50$ kJ", r"$45\,000$ kJ"],
          r"$50\,000 \to 5000$ (primary) $\to 500$ kJ (secondary).",
          [r"Two steps at about $10\%$ each."],
          [r"is the primary consumers.",
           r"is the tertiary consumers.",
           r"is the energy not passed on after one step."], sort=True),
        Q("8.2 Short food chains", r"Why do food chains rarely have more than four or five trophic levels?",
          r"Most of the energy at each level is lost as heat, so too little remains to support further levels.", [r"Top predators are too large to be eaten.", r"Matter is used up after a few levels.", r"Decomposers remove the higher levels."],
          r"With about $10\%$ passed on per step, energy available shrinks a thousandfold in three steps.",
          [r"Energy flows through and is lost; matter cycles."],
          [r"size is not the limit; energy is.",
           r"matter is recycled by decomposers.",
           r"decomposers act at every level and do not remove whole levels."]),
        Q("8.2 Endotherms", r"A $20$ g mouse eats much more food per day than a $20$ g lizard. Why?",
          r"The mouse is an endotherm and uses much of its energy to keep its body warm.", [r"The lizard is a decomposer.", r"The mouse is a producer.", r"Lizards cannot digest food."],
          r"Endotherms generate body heat metabolically, so their energy needs per gram are far higher.",
          [r"Endotherm: internal heat. Ectotherm: environmental heat."],
          [r"the lizard is a consumer.",
           r"the mouse is a consumer.",
           r"lizards digest food normally."]),
    ]),
    Set("Population growth in a culture (8.3--8.4)", [
        Q("8.3 Carrying capacity", r"What is the approximate carrying capacity of the culture?",
          r"about $600$ paramecia per mL", [r"about $300$ paramecia per mL", r"about $20$ paramecia per mL", r"there is none; the population grows without limit"],
          r"The population levels off just below $600$ per mL.",
          [r"$K$: where the curve flattens."],
          [r"is where growth was fastest, about $K/2$.",
           r"is the starting population.",
           r"the curve levels off."]),
        Q("8.3 Fastest growth", r"At about what time was the population growing fastest?",
          r"around day $6$", [r"around day $0$", r"around day $12$", r"around day $14$"],
          r"The curve is steepest near day $6$, when the population is near $300$ per mL, half the carrying capacity.",
          [r"Logistic growth is fastest at $N = K/2$."],
          [r"few individuals means slow growth.",
           r"growth has slowed as the population nears $K$.",
           r"the population has nearly stopped growing."]),
        Q("8.4 Limiting factor", r"Which factor most likely slows the population's growth as it approaches carrying capacity?",
          r"competition for a limited food supply", [r"a sudden change in room temperature", r"an earthquake", r"a mutation in one paramecium"],
          r"Crowding increases competition for food: a density-dependent factor whose effect grows with population size.",
          [r"Density-dependent factors explain logistic leveling."],
          [r"a room-temperature change is density-independent.",
           r"an earthquake is density-independent.",
           r"one mutation would not slow the whole population."]),
        Q("8.3 More food", r"The experiment is repeated with twice as much food added each day. What is the most likely change?",
          r"The carrying capacity increases.", [r"The carrying capacity decreases.", r"The population grows exponentially forever.", r"The starting population doubles."],
          r"More resources support a larger population before density-dependent limits take hold.",
          [r"$K$ depends on resources."],
          [r"more food raises $K$.",
           r"some other resource or waste build-up would eventually limit growth.",
           r"the starting number is set by the experimenter."]),
    ], fig=GROWTH, stim=r"Students counted the paramecia in a culture every two days. Food was added at a constant rate. The graph shows the population density.",
        stim_title="Questions 5--8"),
    Set("Communities, biodiversity and disruption (8.5--8.7)", [
        Q("8.5 Competitive exclusion", r"Two species of barnacles need the same space on rocks in the same part of the shore. What is the most likely long-term outcome?",
          r"One species excludes the other there, or the two come to use different parts of the habitat.", [r"Both species thrive equally in the same niche.", r"Both species become extinct.", r"The two species merge into one species."],
          r"Species with identical niches cannot coexist indefinitely; one wins, or resource partitioning separates them.",
          [r"Competitive exclusion principle."],
          [r"identical niches lead to exclusion.",
           r"competition usually favors one species, not the loss of both.",
           r"competition does not merge species."]),
        Q("8.6 Simpson's index", r"A community contains $50$ individuals of species A, $30$ of species B and $20$ of species C. What is Simpson's diversity index?",
          r"$0.62$", [r"$0.38$", r"$0.50$", r"$1.0$"],
          r"$D = 1 - (0.50^2 + 0.30^2 + 0.20^2) = 1 - 0.38 = 0.62$.",
          [r"$n/N$: $0.50$, $0.30$, $0.20$."],
          [r"is the sum of squares, not $1$ minus it.",
           r"is the proportion of the most common species.",
           r"would need an infinite number of equally common species."], sort=True),
        Q("8.4 Density independence", r"A sudden hard freeze kills $80\%$ of the insects in a field, whether the population was large or small. This freeze is",
          r"a density-independent factor", [r"a density-dependent factor", r"a keystone species", r"an example of mutualism"],
          r"Its effect does not depend on how crowded the population is.",
          [r"Weather and disasters are density-independent."],
          [r"density-dependent factors grow stronger with crowding.",
           r"a keystone species is an organism.",
           r"mutualism is an interaction between species."]),
        Q("8.7 Eutrophication", r"Fertilizer runoff causes an algal bloom in a lake, followed by a fish die-off. What links the two?",
          r"When the algae die, decomposers use up much of the dissolved oxygen.", [r"The algae poison the fish with excess oxygen.", r"Fish eat the fertilizer and are poisoned.", r"The algae make the water too cold."],
          r"Decomposition of the dead algae by bacteria consumes oxygen, leaving too little for fish.",
          [r"Nutrients $\to$ bloom $\to$ decomposition $\to$ low oxygen."],
          [r"algae produce oxygen while alive; the problem is decomposition.",
           r"the fertilizer acts by feeding the algae.",
           r"algae do not cool the water."]),
    ]),
]

UNIT = Unit(8, "ecology", "Ecology", "10--15\\%", "8.1--8.7",
    abstract=r"""Unit 8 covers organisms and their environments: behavioral and physiological responses and communication, energy flow and the cycling of matter through ecosystems, exponential and logistic population growth and density-dependent and density-independent limits, interactions in communities, biodiversity and keystone species (with Simpson's diversity index), and disruptions such as invasive species and eutrophication. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6], qsections=QS,
    frq=FRQ("Scientific Investigation", 4, r"""An invasive shrub is spreading through a forest, and few native plants grow near it. Students hypothesize that the shrub's leaves release chemicals that inhibit the germination of native seeds. They grind shrub leaves in water, filter the mixture, and dilute it to make extracts at $0\%$, $25\%$, $50\%$ and $100\%$ strength. They place $50$ seeds of a native wildflower on moist filter paper in each of several dishes, add $10$ mL of one extract to each dish, and count the germinated seeds after $7$ days.""", [
        Part("A", 1, r"\textbf{Describe} one way an invasive species can reduce the populations of native species.",
             r"For example, it can outcompete native species for light, water or nutrients, especially because it lacks the predators or diseases that limited it in its native range; it may also prey on natives or release chemicals that harm them.",
             r"Saying only that invasive species are ``harmful.''"),
        Part("B", 1, r"\textbf{Identify} the control treatment in this investigation.",
             r"The dishes given the $0\%$ extract (plain water), with the same seeds, volume and conditions.",
             r"Naming the $100\%$ extract, or a variable held constant, as the control."),
        Part("C", 1, r"\textbf{Predict} the results that would support the students' hypothesis.",
             r"The percentage of seeds that germinate is lower in the extract dishes than in the control, and decreases as the extract strength increases.",
             r"Predicting more germination with extract."),
        Part("D", 1, r"\textbf{Justify} your prediction.",
             r"Stronger extracts contain a higher concentration of the inhibitory chemicals, so each seed is exposed to more inhibitor, and more seeds fail to germinate.",
             r"A justification that does not connect the strength of the extract to the amount of inhibitor."),
    ], mins=10),
    frq_topic="testing an invasive shrub's effect on germination",
)
