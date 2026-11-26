from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph, Series

NPP = Graph(r"Ecosystem", r"NPP (g/m$^2$/yr)", x=(0, 1, 1), y=(0, 2500, 500), kind="bar",
            cats=["Tropical / rainforest", "Estuary", "Temperate / forest", "Grassland", "Open / ocean", "Desert"],
            series=[Series("NPP", [2200, 1800, 1250, 600, 125, 90])], legend=False, width=5.4, height=2.6)

S1 = Sec("Ecosystems and biomes (1.1--1.3)", ["1.1", "1.2", "1.3"], r"""
An \textbf{ecosystem} is the living community of an area together with its physical environment. Species interact by predation, competition, mutualism and commensalism; competing species often reduce competition by \textbf{resource partitioning} (using different parts of a resource, or using it at different times or places).

\textbf{Terrestrial biomes} are set mainly by average temperature and precipitation, which determine the plants that can grow and so the animals that live there.
\begin{compare}{Biome}{Climate}{Notes}
Tundra & very cold; little precipitation & permafrost; short growing season; low NPP \\
Taiga (boreal forest) & cold winters; moderate precipitation & conifers; nutrient-poor acidic soils \\
Temperate deciduous forest & four seasons; moderate rain & fertile soils; broadleaf trees \\
Temperate grassland & warm summers, cold winters; low to moderate rain & deep fertile soils; fire and grazing prevent forests \\
Savanna & warm; wet and dry seasons & grasses with scattered trees \\
Desert & very low precipitation; hot or cold & sparse plants with water-saving adaptations \\
Tropical rainforest & warm all year; very high rainfall & the highest terrestrial biodiversity and NPP; nutrient-poor soils because nutrients are held in the vegetation \\
\end{compare}

\textbf{Aquatic biomes} are set by salinity, depth, temperature, water flow and nutrients: freshwater (rivers, lakes, wetlands), estuaries where rivers meet the sea (very productive), coral reefs (warm, shallow, clear water; mutualism with algae) and the open ocean (low productivity per area, but vast).
""", checks=[
    Q("1.2 Biomes", r"A location has an average annual temperature of $25^\circ$C and receives about $15$ cm of precipitation a year. Which biome is it most likely in?",
      r"desert", [r"tropical rainforest", r"taiga", r"temperate deciduous forest"],
      r"Hot with very little precipitation: a desert.",
      [r"Temperature and precipitation together define the biome."],
      [r"a rainforest gets well over $200$ cm a year.",
       r"the taiga is cold.",
       r"temperate forests are cooler and much wetter."]),
])

S2 = Sec("Biogeochemical cycles (1.4--1.7)", ["1.4", "1.5", "1.6", "1.7"], r"""
\begin{compare}{Cycle}{Main reservoirs}{Key processes}
Carbon & sedimentary rock and fossil fuels (largest, slow), oceans, soil, biomass, atmosphere & photosynthesis removes CO$_2$; respiration, decomposition and combustion return it; oceans absorb it; burning fossil fuels moves carbon from a slow reservoir to the atmosphere quickly \\
Nitrogen & the atmosphere (N$_2$, largest), soil, organisms & fixation (N$_2$ to ammonia, by bacteria, lightning or the Haber--Bosch process); nitrification; assimilation; ammonification; denitrification (back to N$_2$) \\
Phosphorus & rocks and sediments (no gas phase) & slow weathering releases phosphate; it is often the limiting nutrient in fresh water \\
Water & oceans (largest), ice, groundwater & evaporation, transpiration, condensation, precipitation, runoff, infiltration; driven by the Sun \\
\end{compare}

\begin{trap}
Nitrogen and phosphorus are both limiting nutrients, so adding them (fertilizer runoff, sewage) causes algal blooms. But only nitrogen has an atmospheric reservoir; phosphorus moves mostly through rock, soil and water.
\end{trap}
""", checks=[
    Q("1.5 Denitrification", r"Which process returns nitrogen to the atmosphere?",
      r"denitrification by bacteria, which converts nitrate to N$_2$ gas", [r"nitrogen fixation, which converts N$_2$ to ammonia", r"assimilation of nitrate by plants", r"nitrification, which converts ammonium to nitrate"],
      r"Denitrifying bacteria, usually in low-oxygen soils, convert nitrates to N$_2$ (and N$_2$O), closing the cycle.",
      [r"Fixation takes N$_2$ out of the air; denitrification puts it back."],
      [r"fixation removes N$_2$ from the atmosphere.",
       r"assimilation moves nitrogen into organisms.",
       r"nitrification keeps nitrogen in the soil."]),
    Q("1.6 Phosphorus", r"How does the phosphorus cycle differ from the carbon and nitrogen cycles?",
      r"It has no significant atmospheric reservoir, so it cycles slowly through rock, soil and water.", [r"Its largest reservoir is the atmosphere.", r"It cycles faster than any other nutrient.", r"Organisms do not need phosphorus."],
      r"Phosphate is released by weathering of rock and moves through soil, water and organisms; with no gas phase it cycles slowly.",
      [r"No gas phase: slow, often limiting."],
      [r"that describes nitrogen.",
       r"weathering of rock makes it slow.",
       r"phosphorus is in DNA, ATP and phospholipids."]),
])

S3 = Sec("Primary productivity (1.8)", ["1.8"], r"""
\textbf{Gross primary productivity} (GPP) is the total rate at which producers capture energy by photosynthesis. Producers use part of it for their own cellular respiration (RL); the rest, stored as biomass and available to consumers, is \textbf{net primary productivity}:
\[ \text{NPP} = \text{GPP} - \text{RL}. \]
NPP is highest where light, water, warmth and nutrients are all plentiful (tropical rainforests, estuaries, wetlands) and lowest where one is scarce (deserts, tundra, the open ocean, where nutrients are scarce at the surface and light fades with depth).

\begin{example}
In a light--dark bottle experiment, water starts with $8.0$ mg/L of dissolved oxygen. After a day, a bottle kept in the light has $9.6$ mg/L (photosynthesis minus respiration: NPP $= 1.6$) and a bottle kept dark has $7.1$ mg/L (respiration only: $0.9$). So GPP $= 1.6 + 0.9 = 2.5$ mg O$_2$/L per day.
\end{example}
""", checks=[
    Q("1.8 NPP", r"The producers in a grassland have a gross primary productivity of $2500$ kcal/m$^2$/yr and use $1000$ kcal/m$^2$/yr in respiration. What is the net primary productivity?",
      r"$1500$ kcal/m$^2$/yr", [r"$3500$ kcal/m$^2$/yr", r"$2.5$ kcal/m$^2$/yr", r"$1000$ kcal/m$^2$/yr"],
      r"NPP $=$ GPP $-$ respiration $= 2500 - 1000 = 1500$ kcal/m$^2$/yr.",
      [r"Subtract what the producers use themselves."],
      [r"adds respiration instead of subtracting it.",
       r"divides GPP by respiration.",
       r"is the respiration."], sort=True),
])

S4 = Sec("Trophic levels, energy flow and food webs (1.9--1.11)", ["1.9", "1.10", "1.11"], r"""
Energy enters most ecosystems as sunlight captured by producers and passes to primary consumers (herbivores), secondary consumers and so on; decomposers and detritivores break down dead matter at every level. Only about $10\%$ of the energy at one trophic level is stored in the next (the \textbf{10\% rule}); the rest is lost as heat from respiration or never eaten. So top predators are few, and pyramids of energy always narrow upward.

A \textbf{food web} shows all the feeding links in a community. Removing one species can ripple through the web: losing a predator can let its prey overgraze; losing a prey species can force predators to switch food or decline.
""", checks=[
    Q("1.10 The 10% rule", r"Producers in an ecosystem store $20\,000$ kcal/m$^2$/yr. About how much energy is available to secondary consumers?",
      r"$200$ kcal/m$^2$/yr", [r"$2000$ kcal/m$^2$/yr", r"$20$ kcal/m$^2$/yr", r"$18\,000$ kcal/m$^2$/yr"],
      r"Two transfers at about $10\%$ each: $20\,000 \to 2000 \to 200$.",
      [r"Primary consumers get about $2000$."],
      [r"is the primary consumers.",
       r"is the tertiary consumers.",
       r"is the energy not passed on in the first step."], sort=True),
])

QS = [
    Set("Climate and biomes (1.2)", [
        Q("1.2 Tundra", r"Which location is most likely in the tundra?",
          r"Location A", [r"Location B", r"Location C", r"Location D"],
          r"Location A is far below freezing on average with little precipitation: tundra.",
          [r"Cold and dry, with permafrost."],
          [r"is warm and very wet: tropical rainforest.",
           r"is hot and dry: desert.",
           r"is temperate with moderate precipitation."]),
        Q("1.8 Highest NPP", r"Which location most likely has the highest net primary productivity?",
          r"Location B", [r"Location A", r"Location C", r"Location D"],
          r"Warmth and abundant water all year support the most photosynthesis.",
          [r"Light, water and warmth together."],
          [r"cold limits growth.",
           r"lack of water limits growth.",
           r"moderate conditions give moderate productivity."]),
        Q("1.2 Grassland", r"Location D's natural vegetation is mostly grasses rather than forest. Which factor best explains this?",
          r"Precipitation is too low to support many trees, and periodic fires and grazing keep trees from taking over.", [r"The soil is too salty for any plants.", r"The temperature is too high for trees.", r"There is no winter."],
          r"Temperate grasslands get $25$--$75$ cm of precipitation, too little for forests, and fire and grazing favor grasses.",
          [r"Moderate temperature, moderate precipitation, fire."],
          [r"grassland soils are among the most fertile.",
           r"a $10^\circ$C average is not too hot for trees.",
           r"temperate grasslands have cold winters."]),
    ], stim=r"""The table gives climate data for four locations.

\medskip
\begin{tabular}{@{}lcc@{}}\toprule
Location & Mean temperature ($^\circ$C) & Precipitation (cm/yr) \\ \midrule
A & $-12$ & 25 \\
B & 26 & 250 \\
C & 22 & 20 \\
D & 10 & 50 \\ \bottomrule
\end{tabular}""", stim_title="Questions 1--3"),
    Set("Biogeochemical cycles (1.4--1.7)", [
        Q("1.4 Fossil fuels", r"How does burning fossil fuels change the carbon cycle?",
          r"It moves carbon from a long-term reservoir into the atmosphere much faster than natural processes return it.", [r"It removes carbon from the atmosphere.", r"It converts carbon into nitrogen.", r"It has no effect, because the carbon was originally in the atmosphere."],
          r"Carbon stored for millions of years in sediments is released as CO$_2$ in decades, faster than oceans and photosynthesis can absorb it.",
          [r"Slow reservoir to fast reservoir."],
          [r"combustion releases CO$_2$.",
           r"carbon is not converted into other elements.",
           r"the rate of release is what matters."]),
        Q("1.5 Nitrogen fixation", r"Why is nitrogen fixation essential for most organisms?",
          r"Most organisms cannot use atmospheric N$_2$; fixation converts it into ammonia, a form plants can take up.", [r"It releases oxygen into the atmosphere.", r"It converts phosphate into a usable form.", r"It returns nitrogen to the atmosphere."],
          r"The triple bond of N$_2$ is broken by nitrogen-fixing bacteria (some living in legume root nodules), lightning, or industry.",
          [r"N$_2$ $\to$ NH$_3$."],
          [r"fixation does not release oxygen.",
           r"phosphorus is not fixed from the air.",
           r"that is denitrification."]),
        Q("1.7 Transpiration", r"Large-scale deforestation of a rainforest is followed by less rainfall in the region. Which part of the water cycle best explains this?",
          r"Fewer trees means less transpiration, so less water vapor returns to the air to form rain.", [r"Fewer trees means more evaporation from leaves.", r"Deforestation increases infiltration into groundwater.", r"Trees produce rain by condensation on their leaves."],
          r"Much of a rainforest's rain is recycled through transpiration; removing trees breaks that loop.",
          [r"Transpiration: water released by plants."],
          [r"evaporation from leaves is transpiration, which falls.",
           r"bare soil usually has more runoff and less infiltration.",
           r"condensation happens in the air."]),
        Q("1.6 Limiting nutrient", r"Phosphate-rich detergent runoff enters a lake, and algae grow rapidly. What does this suggest?",
          r"Phosphorus was the limiting nutrient for the algae.", [r"Nitrogen was the limiting nutrient for the algae.", r"The algae were limited by light.", r"Phosphorus is toxic to fish but not to algae."],
          r"Adding the limiting nutrient allows growth to increase until something else becomes limiting.",
          [r"Limiting factor: the one in shortest supply."],
          [r"adding phosphorus, not nitrogen, caused the growth.",
           r"adding a nutrient would not help if light were limiting.",
           r"the question concerns algal growth, not toxicity."]),
    ]),
    Set("A light--dark bottle experiment (1.8)", [
        Q("1.8 Net productivity", r"What is the net primary productivity of the water sample, in mg O$_2$/L per day?",
          r"$1.6$", [r"$2.5$", r"$0.9$", r"$9.6$"],
          r"The light bottle had photosynthesis and respiration: $9.6 - 8.0 = 1.6$ mg/L.",
          [r"Light bottle: NPP."],
          [r"is the GPP.",
           r"is the respiration.",
           r"is the final concentration, not the change."], sort=True),
        Q("1.8 Respiration", r"What was the rate of respiration?",
          r"$0.9$ mg O$_2$/L per day", [r"$1.6$ mg O$_2$/L per day", r"$2.5$ mg O$_2$/L per day", r"$7.1$ mg O$_2$/L per day"],
          r"The dark bottle had respiration only: $8.0 - 7.1 = 0.9$ mg/L.",
          [r"Dark bottle: respiration only."],
          [r"is the NPP.",
           r"is the GPP.",
           r"is the final concentration."]),
        Q("1.8 Gross productivity", r"What was the gross primary productivity?",
          r"$2.5$ mg O$_2$/L per day", [r"$1.6$ mg O$_2$/L per day", r"$0.7$ mg O$_2$/L per day", r"$17$ mg O$_2$/L per day"],
          r"GPP $=$ NPP $+$ respiration $= 1.6 + 0.9 = 2.5$ (or light minus dark, $9.6 - 7.1$).",
          [r"GPP adds back what producers respire."],
          [r"is the NPP.",
           r"subtracts respiration from NPP.",
           r"adds the two final concentrations."]),
        Q("1.8 Depth", r"The experiment is repeated with water from $30$ m deep, kept at that depth, where little light reaches. What result is most likely?",
          r"The light bottle's oxygen falls, because respiration exceeds photosynthesis.", [r"The light bottle's oxygen rises more than at the surface.", r"The dark bottle's oxygen rises.", r"Both bottles stay at $8.0$ mg/L."],
          r"With little light, GPP is less than respiration, so NPP is negative.",
          [r"Below the photic zone, producers cannot keep up with respiration."],
          [r"less light means less photosynthesis.",
           r"no photosynthesis occurs in the dark bottle.",
           r"respiration continues regardless of light."]),
    ], stim=r"Two bottles are filled with lake water that has $8.0$ mg/L of dissolved oxygen. One is kept in the light and one in the dark at the same temperature. After $24$ hours, the light bottle has $9.6$ mg/L and the dark bottle $7.1$ mg/L.",
        stim_title="Questions 8--11"),
    Set("Energy flow and food webs (1.9--1.11)", [
        Q("1.11 Removing a predator", r"Wolves are removed from an area, and the elk population grows. Over the next decade, willow and aspen trees along streams decline. What does this show?",
          r"A change at one trophic level can cascade through the food web.", [r"Elk are producers.", r"Wolves eat trees.", r"Energy increases at higher trophic levels."],
          r"Without wolves, more elk overbrowse young trees; this is a trophic cascade.",
          [r"Top-down control."],
          [r"elk are primary consumers.",
           r"wolves affect trees through elk.",
           r"energy decreases at higher levels."]),
        Q("1.9 Decomposers", r"What is the main role of decomposers in an ecosystem?",
          r"They break down dead organic matter, returning nutrients to the soil and water.", [r"They capture energy from sunlight.", r"They are the top predators.", r"They add energy to the ecosystem."],
          r"Decomposers (bacteria, fungi) recycle matter; energy is lost as heat.",
          [r"Matter cycles; energy flows."],
          [r"that is the role of producers.",
           r"decomposers feed on dead matter at every level.",
           r"no organism adds energy; producers capture it."]),
        Q("1.10 Pyramids", r"Why do pyramids of energy always have their widest level at the bottom?",
          r"Energy is lost, mostly as heat, at each transfer between trophic levels.", [r"Producers are always the largest organisms.", r"Consumers produce energy from nothing.", r"Higher trophic levels have more species."],
          r"With only about $10\%$ passed on, each level has less energy than the one below.",
          [r"Second law of thermodynamics."],
          [r"size is not the point; energy is.",
           r"energy cannot be created.",
           r"species counts do not determine energy flow."]),
    ]),
]

UNIT = Unit(1, "living-world-ecosystems", "The Living World: Ecosystems", "6--8\\%", "1.1--1.11",
    abstract=r"""Unit 1 introduces ecosystems: species interactions, terrestrial and aquatic biomes, the carbon, nitrogen, phosphorus and water cycles, primary productivity (and how to measure it), trophic levels, the 10\% rule, and food chains and webs. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4], qsections=QS,
    frq=FRQ("Analyze and interpret quantitative data", 10, r"""The graph shows the average net primary productivity (NPP) of six ecosystems.

[[fig]]""", [
        Part("(a)(i)", 1, r"\textbf{Identify} the ecosystem with the lowest NPP.",
             r"Desert (about $90$ g/m$^2$/yr).",
             r"Naming the open ocean, which is second lowest."),
        Part("(a)(ii)", 1, r"\textbf{Describe} how the NPP of the open ocean compares with that of an estuary.",
             r"The open ocean's NPP (about $125$) is far lower, roughly one-fourteenth of the estuary's (about $1800$ g/m$^2$/yr).",
             r"Saying only that it is ``lower'' without a comparison of size."),
        Part("(b)(i)", 1, r"\textbf{Identify} one factor that limits primary productivity in the open ocean.",
             r"Low nutrient concentrations in sunlit surface waters (or the lack of light below the photic zone).",
             r"Naming temperature alone."),
        Part("(b)(ii)", 1, r"\textbf{Explain} why estuaries have high NPP.",
             r"Rivers deliver nutrients from the land, and the water is shallow enough for sunlight to reach producers, so both light and nutrients are plentiful.",
             r"Saying estuaries are ``wet.''"),
        Part("(b)(iii)", 1, r"\textbf{Explain} why the open ocean accounts for a large share of Earth's total primary productivity even though its NPP per square meter is low.",
             r"It covers an enormous area (most of Earth's surface), so a low rate per square meter adds up to a large total.",
             r"Confusing productivity per area with total productivity."),
        Part("(c)(i)", 1, r"\textbf{Describe} the relationship between NPP and gross primary productivity (GPP).",
             r"NPP is GPP minus the energy producers use in their own respiration; it is the energy stored as biomass and available to consumers.",
             r"Reversing the subtraction."),
        Part("(c)(ii)", 2, r"\textbf{Describe} TWO ecosystem services provided by tropical rainforests.",
             r"One point each for any two: carbon storage (climate regulation); producing oxygen; regulating rainfall through transpiration; habitat and biodiversity; sources of medicines, food and timber; preventing soil erosion; purifying water.",
             r"Listing two examples of the same service."),
        Part("(d)(i)", 1, r"Fertilizer runoff from nearby farms is causing algal blooms in an estuary. \textbf{Propose} a realistic solution that would reduce this runoff.",
             r"For example: plant buffer strips of vegetation along streams; apply fertilizer at lower rates or at the right time; use cover crops; restore wetlands upstream.",
             r"Banning all farming."),
        Part("(d)(ii)", 1, r"\textbf{Justify} how your solution would reduce the nutrients reaching the estuary.",
             r"Linked to (d)(i): e.g., buffer-strip plants take up nitrogen and phosphorus and slow runoff so nutrients are absorbed or settle before reaching the water.",
             r"A justification unrelated to the proposed solution."),
    ], mins=23, fig=NPP),
    frq_topic="net primary productivity of six ecosystems",
)
