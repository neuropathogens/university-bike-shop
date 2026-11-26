from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph, Series

ISLANDS = Graph(r"Island area (km$^2$)", r"Number of bird species", x=(0, 100, 20), y=(0, 50, 10),
                series=[Series("near the mainland", [(1, 12), (5, 20), (10, 25), (50, 38), (100, 45)]),
                        Series("far from the mainland", [(1, 5), (5, 10), (10, 13), (50, 22), (100, 27)])],
                legend_pos="nw", width=4.2)

S1 = Sec("Biodiversity and ecosystem services (2.1--2.2)", ["2.1", "2.2"], r"""
\textbf{Biodiversity} exists at three levels: genetic diversity within a population, species diversity in a community, and habitat (ecosystem) diversity. Species diversity has two parts: \textbf{richness} (the number of species) and \textbf{evenness} (how equally individuals are spread among them). Populations with more genetic diversity are better able to survive diseases and environmental change; a population bottleneck (a sharp drop in numbers) reduces genetic diversity.

\textbf{Ecosystem services} are the benefits people get from ecosystems:
\begin{terms}
Provisioning & goods taken directly: food, timber, fresh water, medicines \\
Regulating & natural control of conditions: climate regulation by carbon storage, flood and storm-surge protection, water purification, pollination \\
Cultural & recreation, tourism, education, spiritual value \\
Supporting & processes that make the others possible: nutrient cycling, soil formation, primary productivity \\
\end{terms}
Human activities that damage ecosystems (deforestation, filling wetlands) can cost far more in lost services than they earn.
""", checks=[
    Q("2.1 Evenness", r"Forest A has four tree species with $25$ trees each. Forest B has the same four species, with $85$, $5$, $5$ and $5$ trees. Which statement is correct?",
      r"They have the same species richness, but forest A has greater species evenness.", [r"Forest B has greater richness because it has more trees of one species.", r"Forest A has greater richness and the same evenness.", r"They are equally diverse in every way."],
      r"Both have four species (equal richness); A's individuals are spread equally, so it is more even and more diverse overall.",
      [r"Richness: how many species. Evenness: how equal their numbers."],
      [r"richness counts species, not individuals.",
       r"both have four species.",
       r"their evenness differs."]),
])

S2 = Sec("Island biogeography (2.3)", ["2.3"], r"""
The theory of \textbf{island biogeography} explains the number of species on an island as a balance between immigration and extinction:
\begin{itemize}
\item \textbf{Larger islands} hold more species: more habitat, more resources, larger populations that are less likely to die out.
\item \textbf{Islands nearer the mainland} hold more species: they receive more immigrants.
\end{itemize}
The theory also applies to ``habitat islands'' such as patches of forest surrounded by farmland or cities. Fragmentation into small, isolated patches loses species, especially specialists and large animals that need wide ranges. Island species often evolve to fill many niches (adaptive radiation) and are especially vulnerable to invasive species.
""", checks=[
    Q("2.3 Island size and distance", r"Which island would the theory of island biogeography predict to have the most species?",
      r"a large island near the mainland", [r"a small island near the mainland", r"a large island far from the mainland", r"a small island far from the mainland"],
      r"Large size lowers extinction rates; nearness raises immigration rates.",
      [r"Big and close: most species."],
      [r"small islands lose species to extinction more often.",
       r"distance reduces immigration.",
       r"both small size and distance reduce species number."]),
])

S3 = Sec("Ecological tolerance and natural disruptions (2.4--2.5)", ["2.4", "2.5"], r"""
\textbf{Ecological tolerance} is the range of conditions (temperature, salinity, pH, sunlight) an organism or population can survive. Near the middle of the range is the optimal zone; toward the edges is a \textbf{zone of physiological stress}, where individuals survive but grow and reproduce poorly; beyond it is the zone of intolerance, where they die. Coral bleaching in unusually warm water is an example of conditions moving outside a species' tolerance.

\textbf{Natural disruptions} can be periodic (seasons, tides), episodic (droughts, El Ni\~no) or random (volcanic eruptions, hurricanes, wildfires). Over geological time, sea level and climate have changed with ice ages; organisms respond by adapting, migrating or dying out. Some disruptions, such as wildfire in grasslands and some forests, are part of normal ecosystem function.
""", checks=[
    Q("2.4 Tolerance", r"A species of fish survives in water from $10$ to $30^\circ$C and reproduces best from $18$ to $24^\circ$C. At $28^\circ$C the fish are most likely",
      r"in the zone of physiological stress: alive, but growing and reproducing poorly", [r"in the optimal zone, reproducing at their highest rate", r"in the zone of intolerance, where they die", r"unaffected, because temperature does not affect fish"],
      r"$28^\circ$C is within the survival range but outside the optimal range.",
      [r"Optimal, stress, intolerance."],
      [r"the optimal range ends at $24^\circ$C.",
       r"the fish survive up to $30^\circ$C.",
       r"fish are ectotherms; temperature strongly affects them."]),
])

S4 = Sec("Adaptations and ecological succession (2.6--2.7)", ["2.6", "2.7"], r"""
Organisms adapt to environmental change through natural selection. Species with short generation times and large populations (bacteria, insects) can adapt quickly; species with long generation times and small populations (large mammals, slow-growing trees) adapt slowly and are more likely to go extinct when conditions change rapidly.

\textbf{Ecological succession} is the gradual change in a community after a disturbance.
\begin{compare}{Type}{Starting point}{Sequence}
Primary & bare rock or new land with no soil (after a lava flow or a retreating glacier) & pioneer species (lichens, mosses) weather rock and build soil, then grasses, shrubs, and finally trees \\
Secondary & soil remains (after a fire, a flood or an abandoned farm) & faster: grasses and weeds, then shrubs, then trees \\
\end{compare}
Pioneer species grow fast and tolerate harsh conditions; later species compete better. Biodiversity, biomass and soil depth generally increase through succession, toward a stable (climax) community; NPP is often highest in the middle stages.
""", checks=[
    Q("2.7 Secondary succession", r"A farm field is abandoned and gradually becomes a forest. Why is this called secondary succession?",
      r"The soil was already present, so the community did not have to start from bare rock.", [r"It is the second time the field has been farmed.", r"The first species to arrive were trees.", r"It happens only after a volcanic eruption."],
      r"Secondary succession begins where soil remains, so it proceeds faster than primary succession.",
      [r"Primary: no soil. Secondary: soil remains."],
      [r"the name refers to the soil, not to farming history.",
       r"trees come late in the sequence.",
       r"a lava flow leaves bare rock: primary succession."]),
])

QS = [
    Set("Biodiversity and its value (2.1--2.2)", [
        Q("2.1 Genetic diversity", r"Cheetahs have very little genetic diversity, the result of a population bottleneck thousands of years ago. Why does this put them at risk?",
          r"A new disease or environmental change could affect nearly all individuals the same way.", [r"Low genetic diversity makes them run more slowly.", r"Bottlenecks increase the number of predators.", r"Low genetic diversity always causes extinction within a few generations."],
          r"With little variation, few individuals are likely to carry traits that let them survive a new challenge.",
          [r"Variation is a buffer against change."],
          [r"speed is not the issue.",
           r"a bottleneck is a drop in numbers, not a change in predators.",
           r"it raises risk; it does not guarantee extinction."]),
        Q("2.2 Provisioning", r"Harvesting timber from a forest is an example of which kind of ecosystem service?",
          r"provisioning", [r"regulating", r"cultural", r"supporting"],
          r"Provisioning services are goods taken directly from ecosystems.",
          [r"Goods: provisioning."],
          [r"regulating services control conditions, such as flooding.",
           r"cultural services are recreational or spiritual.",
           r"supporting services, such as soil formation, underlie the others."]),
        Q("2.2 Mangroves", r"Coastal mangrove forests reduce flooding and erosion when storms push seawater ashore. This is an example of",
          r"a regulating service", [r"a provisioning service", r"a cultural service", r"ecological succession"],
          r"The mangroves moderate a natural process (storm surge), protecting coasts.",
          [r"Protection and control: regulating."],
          [r"no good is being harvested.",
           r"this is not recreational or spiritual.",
           r"succession is a change in a community over time."]),
        Q("2.2 Costs of loss", r"A wetland that filters runoff before it reaches a city's reservoir is drained to build housing. What is a likely economic consequence?",
          r"The city may need to spend more to treat its drinking water.", [r"The city's water will need no treatment.", r"The reservoir will hold more water.", r"Fish populations in the reservoir will increase."],
          r"The wetland provided a free water-purification service; replacing it with treatment plants costs money.",
          [r"Lost services have economic costs."],
          [r"removing a natural filter adds pollutants.",
           r"wetlands also store floodwater; their loss does not enlarge the reservoir.",
           r"more pollution usually harms fish."]),
    ]),
    Set("Islands (2.3)", [
        Q("2.3 Most species", r"Which island would you expect to have the most species of land birds?",
          r"Island P", [r"Island Q", r"Island R", r"Island S"],
          r"Island P is the largest and also the closest to the mainland.",
          [r"Large and near."],
          [r"is small, so its extinction rate is higher.",
           r"is far from the mainland and small.",
           r"is large but far, so it receives fewer immigrants than P."]),
        Q("2.3 Distance", r"Islands Q and S are the same size. Why would Q be expected to have more species?",
          r"Q is closer to the mainland, so more species immigrate to it.", [r"Q has a lower extinction rate because it is larger.", r"Q is farther from the mainland, so fewer predators reach it.", r"Q has fewer species because it is closer."],
          r"With equal area, the difference is distance, which controls the immigration rate.",
          [r"Same size: compare distance."],
          [r"the islands are the same size.",
           r"Q is the closer island.",
           r"closer islands have more species."]),
        Q("2.3 Habitat islands", r"A large forest is cut into several small patches separated by farmland. Based on island biogeography, what is the most likely effect on forest species?",
          r"Each patch will support fewer species than the original forest, and species needing large areas may disappear.", [r"Each patch will gain species from the farmland.", r"The total number of forest species will increase.", r"There will be no effect, because the trees remain."],
          r"Small, isolated patches act like small, distant islands: higher extinction, lower immigration.",
          [r"Fragmentation creates habitat islands."],
          [r"farmland species are not forest species.",
           r"fragmentation usually reduces species.",
           r"the patches are smaller and isolated."]),
    ], stim=r"""The table describes four islands of similar habitat off the same coast.

\medskip
\begin{tabular}{@{}lcc@{}}\toprule
Island & Area (km$^2$) & Distance from mainland (km) \\ \midrule
P & 500 & 10 \\
Q & 20 & 10 \\
R & 20 & 200 \\
S & 20 & 50 \\ \bottomrule
\end{tabular}""", stim_title="Questions 5--7"),
    Set("Tolerance, disruption, adaptation and succession (2.4--2.7)", [
        Q("2.4 Coral bleaching", r"Corals expel the algae that live in their tissues when sea temperatures stay above their normal range for weeks. This bleaching shows corals",
          r"outside their range of tolerance for temperature", [r"in their optimal temperature range", r"undergoing primary succession", r"adapting instantly to warmer water"],
          r"Warm water stresses the coral--algae mutualism; prolonged stress can kill the coral.",
          [r"Beyond the optimal range: stress or death."],
          [r"bleaching is a stress response.",
           r"succession is a change in community over time.",
           r"adaptation takes many generations."]),
        Q("2.5 Natural disruption", r"Which is an example of a random (unpredictable) natural disruption to an ecosystem?",
          r"a volcanic eruption", [r"the change of seasons", r"daily tides", r"the yearly flooding of a river"],
          r"Eruptions occur without a regular period.",
          [r"Periodic, episodic or random."],
          [r"seasons are periodic.",
           r"tides are periodic.",
           r"yearly floods are periodic."]),
        Q("2.6 Rate of adaptation", r"Which population is most likely to adapt quickly to a rapidly changing climate?",
          r"a large population of insects that produce several generations a year", [r"a small population of elephants", r"a small population of slow-growing trees", r"a large population of whales"],
          r"Many individuals and short generations mean more variation and faster natural selection.",
          [r"Short generation time, large population."],
          [r"few individuals and long generations slow adaptation.",
           r"long generation times slow adaptation.",
           r"whales have long generation times."]),
        Q("2.7 Pioneer species", r"Which organisms are typically the first to colonize bare rock left by a retreating glacier?",
          r"lichens and mosses", [r"oak and maple trees", r"grazing mammals", r"shrubs with deep roots"],
          r"Pioneer species tolerate harsh conditions and begin breaking down rock to form soil.",
          [r"Primary succession starts with pioneers."],
          [r"trees need soil, which comes later.",
           r"grazers need plants to eat first.",
           r"shrubs need some soil."]),
        Q("2.7 Trends", r"As succession proceeds from a recently burned area toward a mature forest, which generally increases?",
          r"biodiversity and the amount of biomass", [r"the proportion of pioneer species", r"the amount of bare ground", r"soil erosion"],
          r"Later stages have more complex structure, more species and more stored biomass.",
          [r"Succession builds complexity."],
          [r"pioneers are replaced by competitors.",
           r"vegetation covers the ground.",
           r"roots and leaf litter reduce erosion."]),
        Q("2.6 Natural selection", r"After a drought, the surviving plants of a species have deeper roots on average than before. What is the best explanation?",
          r"Plants with heritable deep roots were more likely to survive and reproduce.", [r"The plants grew deeper roots because they needed water, and passed this on.", r"The drought caused mutations for deep roots.", r"Shallow-rooted plants became deep-rooted."],
          r"Selection acts on existing heritable variation in root depth.",
          [r"Variation, then selection."],
          [r"traits acquired during life are not inherited.",
           r"mutations are random, not caused by need.",
           r"individual plants do not evolve."]),
    ]),
]

UNIT = Unit(2, "living-world-biodiversity", "The Living World: Biodiversity", "6--8\\%", "2.1--2.7",
    abstract=r"""Unit 2 covers biodiversity: genetic, species and habitat diversity, richness and evenness, the ecosystem services that biodiversity provides, island biogeography and habitat fragmentation, ecological tolerance, natural disruptions, adaptation, and primary and secondary succession. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4], qsections=QS,
    frq=FRQ("Design an investigation", 10, r"""Researchers counted the land bird species on islands of different sizes, some near the mainland and some far from it. The graph shows their results.

[[fig]]""", [
        Part("(a)(i)", 1, r"\textbf{Describe} the relationship between island area and the number of bird species shown in the graph.",
             r"For both groups, larger islands have more bird species, with the increase slowing at larger areas.",
             r"Describing only one data point."),
        Part("(a)(ii)", 1, r"\textbf{Explain} why islands far from the mainland have fewer species than near islands of the same size.",
             r"Fewer birds reach distant islands, so the immigration rate is lower, while the extinction rate is similar.",
             r"Saying distant islands are colder or poorer without reference to immigration."),
        Part("(b)(i)", 1, r"Students want to investigate whether the area of meadow patches in a city park affects the number of insect species. \textbf{Identify} a testable hypothesis for the investigation.",
             r"For example: larger meadow patches support more insect species than smaller patches.",
             r"A question rather than a testable statement, or a hypothesis about birds."),
        Part("(b)(ii)", 1, r"\textbf{Identify} the independent variable.",
             r"The area of the meadow patch.",
             r"Naming the number of insect species."),
        Part("(b)(iii)", 1, r"\textbf{Identify} the dependent variable.",
             r"The number of insect species (species richness) in each patch.",
             r"Naming the patch area."),
        Part("(b)(iv)", 1, r"\textbf{Describe} one variable that should be held constant, and why.",
             r"For example: the time of day and weather during sampling (insect activity varies with them), the sampling effort (the same number of sweeps or traps per patch), or the type of vegetation.",
             r"Naming a variable without why it matters, or naming the independent variable."),
        Part("(b)(v)", 1, r"\textbf{Describe} a method for measuring the dependent variable.",
             r"For example: in each patch, take the same number of sweep-net sweeps (or set the same number of pitfall traps for the same time), then sort and count the different insect species collected.",
             r"``Count the insects,'' with no standardized method."),
        Part("(c)", 1, r"\textbf{Describe} one ecosystem service that insects in the meadow provide.",
             r"Pollination of flowering plants and crops; decomposition and nutrient cycling; food for birds and other animals; pest control by predatory insects.",
             r"Naming a service without describing it."),
        Part("(d)(i)", 1, r"\textbf{Propose} a solution that would reduce the loss of species caused by dividing habitat into small, isolated patches.",
             r"For example: connect patches with habitat corridors (strips of meadow or hedgerows); protect larger continuous areas.",
             r"Moving all the insects to one patch."),
        Part("(d)(ii)", 1, r"\textbf{Justify} how your solution would reduce species loss.",
             r"Linked to (d)(i): corridors let individuals move between patches, increasing immigration and gene flow and rescuing small populations from local extinction, like making islands ``closer.''",
             r"A justification unrelated to the proposed solution."),
    ], mins=23, fig=ISLANDS),
    frq_topic="island size, distance and bird species",
)
