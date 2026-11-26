from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph, Series

CO2 = Graph(r"Year", r"Atmospheric CO$_2$ (ppm)", x=(1960, 2020, 10), y=(300, 420, 20),
            series=[Series("annual mean", [(1960, 317), (1970, 326), (1980, 339), (1990, 354), (2000, 370), (2010, 390), (2020, 414)])],
            legend=False, width=4.0)

S1 = Sec("Stratospheric ozone depletion and its reduction (9.1--9.2)", ["9.1", "9.2"], r"""
Ozone in the stratosphere absorbs most of the Sun's harmful ultraviolet radiation (UV-B and UV-C). Chlorofluorocarbons (CFCs), once used as refrigerants, propellants and foam-blowing agents, drift into the stratosphere, where UV light breaks them apart and frees chlorine atoms. A chlorine atom destroys ozone ($\mathrm{Cl} + \mathrm{O_3} \to \mathrm{ClO} + \mathrm{O_2}$) and is then released again, so one atom can destroy thousands of ozone molecules. Ice clouds over Antarctica in spring speed these reactions, producing the ozone ``hole.''

More UV reaching the surface causes skin cancer and cataracts and harms crops and phytoplankton. The \textbf{Montreal Protocol} (1987) phased out CFCs worldwide, and the ozone layer is slowly recovering. Their replacements, HCFCs and HFCs, harm ozone less or not at all, but many are powerful greenhouse gases, now being phased down.
""", checks=[
    Q("9.1 CFCs", r"Why can a single CFC molecule destroy many ozone molecules?",
      r"The chlorine atom it releases acts as a catalyst: it is regenerated after each reaction and attacks ozone again.", [r"CFCs are radioactive and split ozone.", r"CFCs combine with ozone to form a stable compound.", r"CFCs cool the stratosphere, freezing ozone."],
      r"Chlorine is freed again in the reaction cycle, so it can destroy ozone repeatedly.",
      [r"Catalytic destruction."],
      [r"CFCs are not radioactive.",
       r"chlorine is released, not locked up.",
       r"ozone is not frozen out."]),
])

S2 = Sec("The greenhouse effect and increases in greenhouse gases (9.3--9.4)", ["9.3", "9.4"], r"""
Sunlight passes through the atmosphere and warms Earth's surface, which emits infrared radiation. \textbf{Greenhouse gases} (water vapor, CO$_2$, methane, nitrous oxide, CFCs and other halocarbons) absorb that infrared radiation and re-emit it in all directions, including back toward the surface. The natural greenhouse effect keeps Earth about $33^\circ$C warmer than it would otherwise be; adding greenhouse gases strengthens it.

\begin{compare}{Gas}{Global warming potential (100 years)}{Main human sources}
CO$_2$ & $1$ (the reference) & burning fossil fuels, deforestation, cement \\
Methane (CH$_4$) & about $25$--$30$ & livestock, rice paddies, landfills, leaks from natural gas systems, thawing permafrost \\
Nitrous oxide (N$_2$O) & about $265$--$300$ & synthetic fertilizers, manure, fuel combustion \\
CFCs and HFCs & thousands & refrigerants, propellants \\
\end{compare}
Atmospheric CO$_2$ has risen from about $280$ ppm before industrialization to over $410$ ppm. Measurements at Mauna Loa (the Keeling curve) also show a yearly cycle: CO$_2$ falls each Northern Hemisphere summer as plants photosynthesize and rises each winter.
""", checks=[
    Q("9.4 Global warming potential", r"Methane has a global warming potential of about $28$. What does this mean?",
      r"Over $100$ years, one kilogram of methane traps about $28$ times as much heat as one kilogram of CO$_2$.", [r"Methane is $28$ times more abundant than CO$_2$.", r"Methane lasts $28$ times longer in the atmosphere than CO$_2$.", r"Methane causes $28\%$ of global warming."],
      r"GWP compares heat trapped per unit mass, relative to CO$_2$, over a set period.",
      [r"Per kilogram, relative to CO$_2$."],
      [r"CO$_2$ is far more abundant.",
       r"methane actually breaks down faster than CO$_2$ is removed.",
       r"GWP is not a share of warming."]),
])

S3 = Sec("Global climate change (9.5)", ["9.5"], r"""
Rising greenhouse gas concentrations are raising average global temperatures. Effects include melting glaciers and sea ice, sea-level rise (from melting land ice and the thermal expansion of seawater), more intense heat waves, droughts and heavy rainfall, shifting ranges and seasons for species, and threats to coastal communities and food supplies.

\textbf{Feedback loops} can amplify warming: melting ice exposes darker land and water, which absorb more sunlight (ice--albedo feedback); thawing permafrost releases methane and CO$_2$; warmer air holds more water vapor. Ice cores record past temperatures and CO$_2$, which rose and fell together through ice ages.

Responses: \textbf{mitigation} (cutting emissions through renewable energy, efficiency, carbon taxes or cap-and-trade, reforestation; international agreements such as the Paris Agreement) and \textbf{adaptation} (sea walls, drought-tolerant crops, moving infrastructure).
""", checks=[
    Q("9.5 Feedback", r"As Arctic sea ice melts, the darker ocean absorbs more sunlight, which causes more melting. This is an example of",
      r"a positive feedback loop", [r"a negative feedback loop", r"the Montreal Protocol", r"carbon sequestration"],
      r"The response (more absorption) amplifies the original change (warming): the ice--albedo feedback.",
      [r"Amplifying: positive feedback."],
      [r"negative feedback would counteract the change.",
       r"the Montreal Protocol is a treaty about ozone.",
       r"sequestration removes carbon."]),
])

S4 = Sec("Ocean warming and ocean acidification (9.6--9.7)", ["9.6", "9.7"], r"""
The oceans have absorbed most of the extra heat trapped by greenhouse gases. Warmer water causes coral bleaching (corals expel their symbiotic algae), shifts fish and plankton toward the poles, holds less dissolved oxygen, and expands, raising sea level.

The oceans also absorb about a quarter of the CO$_2$ we emit. CO$_2$ dissolves to form carbonic acid, releasing H$^+$ ions:
\[ \mathrm{CO_2 + H_2O \to H_2CO_3 \to H^+ + HCO_3^-} . \]
Ocean pH has fallen from about $8.2$ to $8.1$ since industrialization, about a $25\%$ increase in acidity. The extra H$^+$ also reduces the carbonate ions that corals, shellfish and some plankton need to build calcium carbonate shells and skeletons.
""", checks=[
    Q("9.7 Acidification", r"How does rising atmospheric CO$_2$ harm oysters and corals?",
      r"CO$_2$ dissolving in seawater lowers its pH and reduces the carbonate ions they need to build shells and skeletons.", [r"CO$_2$ makes seawater more basic, dissolving their tissues.", r"CO$_2$ blocks sunlight from reaching them.", r"CO$_2$ is directly poisonous to all marine animals."],
      r"More H$^+$ ties up carbonate as bicarbonate, making calcification harder.",
      [r"Acidification and carbonate."],
      [r"the water becomes more acidic, not basic.",
       r"CO$_2$ is transparent to visible light.",
       r"the harm comes through ocean chemistry."]),
])

S5 = Sec("Invasive species, endangered species and human impacts on biodiversity (9.8--9.10)", ["9.8", "9.9", "9.10"], r"""
\textbf{Invasive species} (zebra mussels, kudzu, cane toads, Burmese pythons, lionfish) are often generalist, $r$-selected species that thrive in new habitats lacking their natural predators, parasites and competitors; they outcompete or prey on natives. Control includes prevention (inspections, cleaning boats), early removal, and sometimes biological control.

\textbf{Endangered species} are at risk of extinction; specialists, species with small ranges or populations, $K$-selected species and those hunted for valuable parts are most vulnerable. Protection includes the Endangered Species Act, the CITES treaty on wildlife trade, captive breeding and habitat protection.

\textbf{Human impacts on biodiversity} are summarized as HIPPCO: Habitat destruction and fragmentation (the leading cause), Invasive species, Population growth, Pollution, Climate change and Overexploitation. Wildlife corridors and protected areas connected into networks reduce the effects of fragmentation.
""", checks=[
    Q("9.10 Leading threat", r"Which is the leading cause of biodiversity loss worldwide?",
      r"habitat destruction and fragmentation", [r"noise pollution", r"ozone depletion", r"hunting for sport"],
      r"Converting forests, wetlands and grasslands to farms and cities removes the places species live.",
      [r"HIPPCO: habitat first."],
      [r"noise is a minor factor overall.",
       r"ozone depletion is a smaller threat and is being reversed.",
       r"overexploitation matters, but habitat loss is the largest cause."]),
])

QS = [
    Set("The ozone layer (9.1--9.2)", [
        Q("9.2 Montreal Protocol", r"Why is the Montreal Protocol considered a successful environmental treaty?",
          r"Nearly all countries phased out CFCs, and the ozone layer has begun to recover.", [r"It reduced CO$_2$ emissions by half.", r"It banned all refrigeration.", r"It created the ozone hole."],
          r"Global cooperation cut the production of ozone-depleting substances by about $99\%$.",
          [r"A model of international cooperation."],
          [r"it addressed ozone-depleting substances, not CO$_2$.",
           r"refrigeration continued with substitute chemicals.",
           r"the treaty responded to the ozone hole."]),
        Q("9.1 UV effects", r"Which is a likely consequence of stratospheric ozone depletion?",
          r"more skin cancers and cataracts in people", [r"more photochemical smog at ground level", r"more acid rain", r"cooler surface temperatures everywhere"],
          r"Less ozone lets more UV-B reach the surface, damaging DNA and eyes.",
          [r"Less ozone above, more UV below."],
          [r"smog involves ground-level ozone, a different problem.",
           r"acid rain comes from SO$_2$ and NO$_x$.",
           r"ozone depletion is not mainly a temperature effect at the surface."]),
        Q("9.2 Replacements", r"Many CFC replacements, such as HFCs, do not harm the ozone layer. Why are they still a concern?",
          r"Many are powerful greenhouse gases.", [r"They destroy more ozone than CFCs.", r"They are radioactive.", r"They cause acid rain."],
          r"HFCs have high global warming potentials, so they are now being phased down under the Kigali Amendment.",
          [r"Fixing one problem without causing another."],
          [r"HFCs contain no chlorine to destroy ozone.",
           r"HFCs are not radioactive.",
           r"HFCs do not form acids in rain."]),
    ]),
    Set("The rise in atmospheric CO$_2$ (9.4--9.5)", [
        Q("9.4 Total increase", r"By how much did the annual mean CO$_2$ concentration increase from 1960 to 2020?",
          r"about $97$ ppm", [r"about $414$ ppm", r"about $31\%$ per decade", r"about $317$ ppm"],
          r"$414 - 317 = 97$ ppm.",
          [r"Subtract the first value from the last."],
          [r"is the 2020 value, not the change.",
           r"is not a rate shown by the data.",
           r"is the 1960 value."]),
        Q("9.4 Recent rate", r"What was the average rate of increase from 2010 to 2020?",
          r"$2.4$ ppm per year", [r"$24$ ppm per year", r"$0.24$ ppm per year", r"$41$ ppm per year"],
          r"$(414 - 390)/10 = 2.4$ ppm per year.",
          [r"Change divided by time."],
          [r"is the change over the whole decade.",
           r"divides by $100$ years.",
           r"divides the 2020 value by $10$."], sort=True),
        Q("9.4 Acceleration", r"Compare the rate of increase in the 1960s with the rate in the 2010s.",
          r"The rate increased: about $0.9$ ppm per year in the 1960s and about $2.4$ ppm per year in the 2010s.", [r"The rate decreased over time.", r"The rate stayed the same.", r"CO$_2$ fell in the 1960s and rose in the 2010s."],
          r"$1960$s: $(326 - 317)/10 = 0.9$ ppm/yr; $2010$s: $2.4$ ppm/yr.",
          [r"The curve gets steeper."],
          [r"the later decades are steeper.",
           r"the slope changes.",
           r"CO$_2$ rose in every decade."]),
        Q("9.4 Main source", r"What is the main cause of the increase shown in the graph?",
          r"burning fossil fuels", [r"volcanic eruptions", r"ocean evaporation", r"photosynthesis by phytoplankton"],
          r"Fossil-fuel combustion releases carbon stored for millions of years; deforestation adds more.",
          [r"Human emissions dominate."],
          [r"volcanoes emit far less CO$_2$ than human activity.",
           r"evaporation releases water vapor.",
           r"photosynthesis removes CO$_2$."]),
    ], fig=CO2, stim=r"The graph shows the annual mean concentration of CO$_2$ in the atmosphere, measured at Mauna Loa Observatory in Hawaii.",
        stim_title="Questions 4--7"),
    Set("Climate, oceans and biodiversity (9.3--9.10)", [
        Q("9.3 Greenhouse effect", r"Which describes how greenhouse gases warm Earth's surface?",
          r"They absorb infrared radiation emitted by the surface and re-emit some of it back toward the surface.", [r"They block incoming sunlight from reaching the surface.", r"They create holes in the ozone layer that let in more heat.", r"They produce heat by chemical reactions."],
          r"Greenhouse gases are transparent to most sunlight but absorb outgoing infrared.",
          [r"Sunlight in, infrared trapped."],
          [r"blocking sunlight would cool the surface.",
           r"ozone depletion and the greenhouse effect are different processes.",
           r"they trap heat; they do not generate it."]),
        Q("9.5 Sea-level rise", r"Which two processes are the main causes of rising sea level?",
          r"melting of land ice (glaciers and ice sheets) and thermal expansion of seawater", [r"melting of floating sea ice and increased rainfall", r"increased evaporation and decreased river flow", r"stronger tides and more earthquakes"],
          r"Floating sea ice already displaces its own weight of water, so its melting adds little; land ice and warming water add volume.",
          [r"Land ice plus expansion."],
          [r"melting floating ice barely changes sea level.",
           r"these do not raise sea level.",
           r"tides and earthquakes are not causes of long-term rise."]),
        Q("9.4 Methane sources", r"Which human activity is a major source of methane?",
          r"raising cattle and growing rice in flooded paddies", [r"using solar panels", r"recycling aluminum", r"planting forests"],
          r"Microbes in cattle digestive systems and in waterlogged rice fields produce methane.",
          [r"Anaerobic microbes make methane."],
          [r"solar panels emit no methane.",
           r"recycling does not produce methane.",
           r"forests absorb CO$_2$."]),
        Q("9.6 Coral bleaching", r"Why does ocean warming cause coral bleaching?",
          r"Heat stress causes corals to expel the symbiotic algae that give them color and much of their food.", [r"Warm water dissolves coral skeletons directly.", r"Warm water adds nutrients that kill corals.", r"Corals turn white to reflect sunlight as an adaptation."],
          r"Without the algae, corals turn white and may starve if high temperatures persist.",
          [r"The coral--algae mutualism breaks down."],
          [r"acidification, not warming, attacks carbonate skeletons.",
           r"bleaching is a stress response, not nutrient poisoning.",
           r"bleaching is a breakdown, not an adaptation."]),
        Q("9.8 Invasive species", r"Zebra mussels, introduced to the Great Lakes in ship ballast water, spread rapidly. Which trait most helped them become invasive?",
          r"high reproductive rates and no natural predators in their new habitat", [r"a narrow, specialized diet", r"long generation times", r"few offspring with much parental care"],
          r"$r$-selected traits and enemy release let invasive species spread quickly.",
          [r"Generalist, $r$-selected, no enemies."],
          [r"specialists rarely become invasive.",
           r"long generations slow spread.",
           r"that describes $K$-selected species."]),
        Q("9.9 Vulnerability", r"Which species is most vulnerable to extinction?",
          r"a large, slow-reproducing mammal that lives only on one small island", [r"a widespread insect that reproduces rapidly", r"a common weed that grows on many continents", r"a generalist bird found across a continent"],
          r"Small range, small population and slow reproduction all raise extinction risk.",
          [r"Specialized, small range, $K$-selected."],
          [r"widespread, fast-reproducing species are resilient.",
           r"widespread weeds are resilient.",
           r"widespread generalists are resilient."]),
        Q("9.10 Corridors", r"A highway divides a forest in two. Which action would best reduce its effect on wildlife populations?",
          r"building wildlife overpasses or underpasses that connect the two halves", [r"cutting more trees along the highway", r"adding more lanes to the highway", r"removing native predators"],
          r"Corridors let animals move between fragments, maintaining gene flow and access to resources.",
          [r"Reconnect fragments."],
          [r"more clearing increases fragmentation.",
           r"wider roads are harder to cross.",
           r"removing predators can cause cascades."]),
        Q("9.5 Mitigation", r"Which is an example of climate change mitigation rather than adaptation?",
          r"replacing coal power plants with wind and solar power", [r"building sea walls around a coastal city", r"planting drought-tolerant crops", r"moving homes away from flood zones"],
          r"Mitigation reduces greenhouse gas emissions; adaptation copes with the effects.",
          [r"Mitigate causes; adapt to effects."],
          [r"sea walls are adaptation.",
           r"drought-tolerant crops are adaptation.",
           r"relocation is adaptation."]),
    ]),
]

UNIT = Unit(9, "global-change", "Global Change", "15--20\\%", "9.1--9.10",
    abstract=r"""Unit 9 is the largest unit on the exam. It covers stratospheric ozone depletion and the Montreal Protocol, the greenhouse effect and the sources and warming potentials of greenhouse gases, global climate change and its feedbacks, ocean warming and acidification, invasive and endangered species, and the human causes of biodiversity loss (HIPPCO), with mitigation and adaptation. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5], qsections=QS,
    frq=FRQ("Analyze an environmental problem doing calculations", 10, r"""A student drives to school and back, a round trip of $30$ km, on each of $180$ school days a year. The car travels $12$ km per liter of gasoline, and burning $1$ liter of gasoline releases $2.3$ kg of CO$_2$. A city bus on the same route emits $0.04$ kg of CO$_2$ per passenger per kilometer. A typical tree absorbs about $22$ kg of CO$_2$ a year.""", [
        Part("(a)", 1, r"\textbf{Identify} one greenhouse gas other than CO$_2$ and one human source of it.",
             r"For example: methane from cattle, rice paddies, landfills or natural gas leaks; nitrous oxide from fertilizers; HFCs from refrigerants.",
             r"Naming a gas without a matching source."),
        Part("(b)", 2, r"\textbf{Calculate} the volume of gasoline, in liters, the student uses for the commute in a year. Show your work.",
             r"1 pt: setup: $30\ \mathrm{km/day} \times 180\ \mathrm{days} \div 12\ \mathrm{km/L}$. 1 pt: $450$ L.",
             r"Multiplying by the fuel economy instead of dividing."),
        Part("(c)", 2, r"\textbf{Calculate} the mass of CO$_2$ the commute produces in a year. Show your work.",
             r"1 pt: setup: $450\ \mathrm{L} \times 2.3\ \mathrm{kg/L}$ (consistent with (b)). 1 pt: about $1035$ kg (about $1.0$ metric ton).",
             r"Using the distance instead of the fuel."),
        Part("(d)", 2, r"\textbf{Calculate} how much less CO$_2$ would be emitted in a year if the student took the bus instead. Show your work.",
             r"1 pt: setup: bus $= 30 \times 180 \times 0.04 = 216$ kg. 1 pt: reduction $= 1035 - 216 \approx 819$ kg (consistent with (c)).",
             r"Reporting the bus emissions as the reduction."),
        Part("(e)", 2, r"\textbf{Calculate} the number of trees needed to absorb the CO$_2$ produced by driving for a year. Show your work.",
             r"1 pt: setup: $1035 \div 22$ (consistent with (c)). 1 pt: about $47$ trees.",
             r"Multiplying instead of dividing."),
        Part("(f)", 1, r"\textbf{Describe} one positive feedback loop that could accelerate global warming.",
             r"For example: melting ice exposes darker land and ocean that absorb more sunlight, causing more warming and melting (ice--albedo feedback); or thawing permafrost releases methane and CO$_2$, causing more warming and thawing.",
             r"Describing a negative feedback, or a cause of warming that is not a loop."),
    ], mins=23),
    frq_topic="the carbon footprint of a commute",
)
