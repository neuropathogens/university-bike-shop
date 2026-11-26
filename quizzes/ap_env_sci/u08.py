from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph, Series

DOSE = Graph(r"Copper concentration ($\mu$g/L)", r"Mortality after 48 h (\%)", x=(0, 60, 10), y=(0, 100, 20),
             series=[Series("Daphnia", [(0, 2), (10, 5), (20, 18), (30, 50), (40, 80), (50, 95), (60, 98)])], legend=False, width=4.0)

S1 = Sec("Sources of pollution and human impacts on ecosystems (8.1, 8.2, 8.4)", ["8.1", "8.2", "8.4"], r"""
\textbf{Point sources} release pollutants from a single, identifiable place (a factory pipe, a sewage outfall); \textbf{nonpoint sources} are diffuse (runoff from farms, lawns and streets) and much harder to regulate.

\begin{terms}
Coral reefs & harmed by warming (bleaching), sediment from erosion that blocks light, nutrient pollution, destructive fishing and ocean acidification \\
Oil spills & coat birds and mammals, kill fish and shellfish; tar balls persist; cleanup with booms, skimmers and dispersants is only partly effective \\
Ocean debris & plastics entangle animals and are swallowed; they break into microplastics that enter food webs \\
Wetlands and mangroves & filter pollutants, absorb floodwater, buffer coasts from storms and provide nurseries for fish; lost to development, dams, agriculture and pollution \\
\end{terms}
""", checks=[
    Q("8.1 Nonpoint source", r"Which is a nonpoint source of water pollution?",
      r"fertilizer washing off many farm fields after rain", [r"a pipe discharging factory wastewater into a river", r"a sewage treatment plant's outfall", r"a leaking oil tanker"],
      r"Runoff from a large area has no single point of discharge.",
      [r"Diffuse: nonpoint."],
      [r"a pipe is a point source.",
       r"an outfall is a point source.",
       r"a single ship is a point source."]),
])

S2 = Sec("Endocrine disruptors, eutrophication and thermal pollution (8.3, 8.5, 8.6)", ["8.3", "8.5", "8.6"], r"""
\textbf{Endocrine disruptors} (some pesticides such as atrazine and DDT, plasticizers such as BPA and phthalates, some medications) interfere with hormones, causing reproductive and developmental problems such as feminized male fish and frogs.

\textbf{Eutrophication}: excess nitrogen and phosphorus (from fertilizer, manure, sewage, detergents) cause algal blooms; when the algae die, decomposing bacteria use up dissolved oxygen, producing hypoxic ``dead zones'' (as in the Gulf of Mexico each summer) where fish and invertebrates die. Oligotrophic waters are nutrient-poor and clear; eutrophic waters are nutrient-rich and murky.

\textbf{Thermal pollution}: warm water discharged by power plants and factories holds less dissolved oxygen, while warmer temperatures raise organisms' metabolic rates and oxygen needs; sudden changes (thermal shock) can kill fish.
""", checks=[
    Q("8.5 Dead zones", r"Why does an algal bloom caused by fertilizer runoff lead to fish deaths?",
      r"When the algae die, bacteria decomposing them use up the dissolved oxygen.", [r"The algae release ozone that poisons fish.", r"Fertilizer is directly toxic to fish at any concentration.", r"Algae eat the fish."],
      r"Decomposition consumes oxygen, creating hypoxic water.",
      [r"Nutrients $\to$ bloom $\to$ decomposition $\to$ low oxygen."],
      [r"algae produce oxygen while alive, not ozone.",
       r"the main harm is indirect, through oxygen loss.",
       r"algae are producers."]),
])

S3 = Sec("Persistent organic pollutants, bioaccumulation and biomagnification (8.7--8.8)", ["8.7", "8.8"], r"""
\textbf{Persistent organic pollutants} (POPs) such as DDT, PCBs and dioxins break down very slowly, dissolve in fat rather than water, and can travel long distances through air and water, reaching even the Arctic.

\textbf{Bioaccumulation}: a fat-soluble toxin builds up in an organism's tissues over its lifetime, because it is absorbed faster than it is excreted. \textbf{Biomagnification}: its concentration increases at each step up a food chain, because each predator eats many prey. Top predators carry the highest concentrations: DDT thinned the eggshells of eagles, ospreys and pelicans; methylmercury makes large predatory fish such as tuna and swordfish risky to eat.
""", checks=[
    Q("8.8 Biomagnification", r"Why do top predators have the highest concentrations of DDT in their bodies?",
      r"Each predator eats many prey, and DDT is stored in fat rather than excreted, so it becomes more concentrated at each trophic level.", [r"Top predators absorb DDT directly from the air.", r"DDT breaks down faster in prey.", r"Top predators are more often sprayed with DDT."],
      r"Fat-soluble, persistent toxins pass up the food chain and concentrate.",
      [r"Biomagnification."],
      [r"most exposure is through food.",
       r"DDT is persistent everywhere.",
       r"spraying is not targeted at predators."]),
])

S4 = Sec("Solid waste disposal and waste reduction (8.9--8.10)", ["8.9", "8.10"], r"""
\begin{compare}{Method}{Advantages}{Problems}
Sanitary landfill (clay or plastic liner, leachate collection, daily soil cover, methane capture) & cheap; well regulated & takes land; leachate can contaminate groundwater; decomposition releases methane \\
Incineration & reduces volume by about $90\%$; can generate electricity & air pollution (dioxins, metals, CO$_2$); toxic ash \\
Open dumping and ocean dumping & cheap & pollution, disease, harm to wildlife \\
\end{compare}
Electronic waste contains lead, mercury and cadmium and should be recycled. The best strategy is the order: \textbf{reduce} (use less), \textbf{reuse}, \textbf{recycle} (saves energy and resources, but takes energy to collect and process). \textbf{Composting} turns food and yard waste into a soil amendment and keeps it out of landfills, where it would produce methane. Landfill methane can be collected and burned for energy.
""", checks=[
    Q("8.10 Waste hierarchy", r"Which is generally the most effective way to reduce the environmental impact of solid waste?",
      r"reducing the amount of material used in the first place", [r"recycling everything after use", r"incinerating waste to generate electricity", r"building larger landfills"],
      r"Waste that is never made needs no energy to collect, process or dispose of.",
      [r"Reduce, reuse, recycle, in that order."],
      [r"recycling is good but still uses energy and resources.",
       r"incineration produces air pollution and ash.",
       r"landfills still take land and release methane."]),
])

S5 = Sec("Sewage treatment (8.11)", ["8.11"], r"""
\begin{compare}{Stage}{Process}{Removes}
Primary & physical: screens and settling tanks & large debris and solids (sludge) \\
Secondary & biological: aerated tanks of bacteria & dissolved organic matter (lowering biochemical oxygen demand) \\
Tertiary & chemical and biological & nitrogen and phosphorus, which would cause eutrophication \\
Disinfection & chlorine, UV light or ozone & pathogens \\
\end{compare}
Sludge can be treated and used as fertilizer, landfilled or burned. In cities with combined sewers, heavy rain can overflow the system and send untreated sewage into rivers.
""", checks=[
    Q("8.11 Secondary treatment", r"What happens during secondary sewage treatment?",
      r"Bacteria break down dissolved organic matter in aerated tanks.", [r"Screens remove large objects such as sticks and plastic.", r"Chlorine kills pathogens before release.", r"Chemicals remove phosphorus to prevent eutrophication."],
      r"Secondary treatment is biological; primary is physical; tertiary removes nutrients; disinfection kills pathogens.",
      [r"Primary physical, secondary biological."],
      [r"that is primary treatment.",
       r"that is disinfection.",
       r"that is tertiary treatment."]),
])

S6 = Sec("Toxicology, pollution and human health, and infectious disease (8.12--8.15)", ["8.12", "8.13", "8.14", "8.15"], r"""
\textbf{Dose--response.} A dose--response curve plots the effect of a substance (often the percentage of a test population killed or affected) against the dose. The \textbf{LD$_{50}$} is the dose that kills $50\%$ of the test population; a lower LD$_{50}$ means a more toxic substance. Many substances have a threshold below which no effect is seen; ED$_{50}$ is the dose that produces an effect in $50\%$. Results from test animals are only estimates for humans.

\textbf{Pollution and human health.} Exposure to lead (developmental and nerve damage), mercury (nervous system), asbestos (lung disease), particulates (respiratory and heart disease) and indoor smoke shortens lives; the effects are often hard to trace because exposure is long and mixed.

\textbf{Pathogens and infectious diseases.} Many diseases are spread by vectors such as mosquitoes (malaria, West Nile virus, Zika, dengue) and ticks (Lyme disease), or by contaminated water (cholera, giardiasis), especially where sanitation is poor. Climate change can expand the ranges of vectors; habitat destruction and close contact with wildlife and livestock let new diseases emerge from animals (zoonoses such as SARS, MERS and COVID-19); overuse of antibiotics breeds resistant bacteria (tuberculosis).
""", checks=[
    Q("8.12 Comparing LD50", r"Chemical X has an oral LD$_{50}$ of $5$ mg/kg in rats, and chemical Y an LD$_{50}$ of $500$ mg/kg. Which statement is correct?",
      r"Chemical X is more toxic, because a smaller dose kills half the test animals.", [r"Chemical Y is more toxic, because its LD$_{50}$ is larger.", r"They are equally toxic.", r"LD$_{50}$ values cannot be compared."],
      r"LD$_{50}$ is the dose lethal to half the population; the lower it is, the more toxic the substance.",
      [r"Lower LD$_{50}$, higher toxicity."],
      [r"a larger LD$_{50}$ means more is needed to kill.",
       r"they differ by a factor of $100$.",
       r"measured the same way, they can be compared."]),
])

QS = [
    Set("Sources and impacts (8.1--8.4)", [
        Q("8.4 Wetlands", r"Which ecosystem service do coastal wetlands and mangroves provide?",
          r"filtering pollutants and absorbing storm surges", [r"generating hydroelectric power", r"producing fossil fuels", r"increasing the salinity of rivers"],
          r"Wetland plants and soils trap sediment and nutrients and buffer coasts from storms.",
          [r"Regulating services."],
          [r"wetlands do not generate power.",
           r"fossil fuels form over millions of years.",
           r"wetlands moderate, not raise, salinity."]),
        Q("8.2 Microplastics", r"Why are microplastics a concern in the ocean?",
          r"They are eaten by small organisms and can carry toxins up food chains.", [r"They decompose quickly into nutrients.", r"They increase dissolved oxygen.", r"They are too small to affect any organism."],
          r"Plastic fragments persist for decades, absorb pollutants and are ingested by plankton, fish and seabirds.",
          [r"Persistent and ingested."],
          [r"plastics break into smaller pieces; they do not decompose into nutrients.",
           r"plastics do not raise oxygen.",
           r"filter feeders and plankton eat them."]),
        Q("8.3 Endocrine disruptors", r"Male frogs living downstream of farms show female characteristics. Which kind of pollutant is the most likely cause?",
          r"an endocrine disruptor such as the herbicide atrazine", [r"a heavy sediment load", r"thermal pollution", r"noise pollution"],
          r"Endocrine disruptors mimic or block hormones, affecting sexual development.",
          [r"Hormone-like effects."],
          [r"sediment blocks light and smothers habitat.",
           r"warm water lowers oxygen.",
           r"noise does not change sex characteristics."]),
    ]),
    Set("DDT in a food chain (8.7--8.8)", [
        Q("8.8 Magnification factor", r"By what factor is the concentration of DDT in fish-eating birds greater than in small fish?",
          r"$50$", [r"$12.5$", r"$24.5$", r"$5$"],
          r"$25\ \mathrm{ppm} \div 0.5\ \mathrm{ppm} = 50$.",
          [r"Divide the higher concentration by the lower."],
          [r"compares the birds with the large fish.",
           r"subtracts instead of dividing.",
           r"misplaces the decimal."], sort=True),
        Q("8.8 Why it increases", r"Which best explains the pattern in the table?",
          r"DDT is stored in fatty tissue and passed up the food chain, so it becomes more concentrated at each level.", [r"DDT is produced by fish-eating birds.", r"DDT breaks down faster at higher trophic levels.", r"Water contains more DDT than any organism."],
          r"This is biomagnification: persistent, fat-soluble compounds concentrate in predators.",
          [r"Biomagnification."],
          [r"birds accumulate DDT from their prey.",
           r"concentrations rise up the chain.",
           r"water has the lowest concentration."]),
        Q("8.8 Most affected", r"Which organisms in this food chain are most at risk of harm from DDT?",
          r"the fish-eating birds", [r"the zooplankton", r"the small fish", r"the algae"],
          r"At the top of the chain they carry the highest concentration; DDT thins their eggshells, reducing hatching success.",
          [r"Top predators bear the greatest load."],
          [r"they carry low concentrations.",
           r"small fish carry less than the birds.",
           r"algae are at the bottom."]),
        Q("8.7 Persistence", r"DDT has not been used in this country for decades, yet it is still found in the food chain. Which property explains this?",
          r"DDT is persistent: it breaks down very slowly in the environment.", [r"DDT is water-soluble and quickly washed away.", r"DDT is a nutrient that organisms produce.", r"DDT is a gas that leaves the food chain quickly."],
          r"Persistent organic pollutants last for decades in sediments and fatty tissue, and can drift in from places still using them.",
          [r"POPs persist."],
          [r"DDT is fat-soluble, not water-soluble.",
           r"organisms do not make DDT.",
           r"DDT is not a gas at normal temperatures."]),
    ], stim=r"""Researchers measured DDT concentrations in a lake food chain.

\medskip
\begin{tabular}{@{}lc@{}}\toprule
Sample & DDT (ppm) \\ \midrule
Water & 0.000003 \\
Zooplankton & 0.04 \\
Small fish & 0.5 \\
Large fish & 2.0 \\
Fish-eating birds & 25 \\ \bottomrule
\end{tabular}""", stim_title="Questions 4--7"),
    Set("Water, waste and health (8.5--8.15)", [
        Q("8.6 Thermal pollution", r"A power plant discharges warm water into a river. Why can this harm fish?",
          r"Warm water holds less dissolved oxygen while fish need more oxygen at higher temperatures.", [r"Warm water contains more dissolved oxygen.", r"Warm water increases the river's pH to toxic levels.", r"Fish cannot swim in warm water."],
          r"Oxygen solubility falls as temperature rises, while metabolic rates increase.",
          [r"Less supply, more demand."],
          [r"warmer water holds less oxygen.",
           r"temperature is not mainly a pH effect.",
           r"the problem is oxygen and thermal stress."]),
        Q("8.5 Oligotrophic", r"Which describes an oligotrophic lake?",
          r"low in nutrients, with clear water and high dissolved oxygen", [r"high in nutrients, with frequent algal blooms", r"low in oxygen throughout", r"polluted by sewage"],
          r"Few nutrients mean little algae, so light penetrates deep and oxygen stays high.",
          [r"Oligotrophic: few nutrients."],
          [r"that describes a eutrophic lake.",
           r"oligotrophic lakes have plenty of oxygen.",
           r"sewage would add nutrients."]),
        Q("8.9 Landfill leachate", r"What is the purpose of the liner and leachate-collection system in a sanitary landfill?",
          r"to keep liquids that drain through the waste from contaminating groundwater", [r"to speed up the decomposition of plastics", r"to collect methane for fuel", r"to keep rainwater out of the landfill completely"],
          r"Leachate can carry metals and organic chemicals; the liner and pipes collect it for treatment.",
          [r"Protect groundwater."],
          [r"plastics decompose very slowly regardless.",
           r"methane is collected by a separate system of wells.",
           r"rain still enters; the system manages it."]),
        Q("8.10 Composting", r"Composting food and yard waste instead of sending it to a landfill reduces which greenhouse gas emission?",
          r"methane, produced when organic waste decomposes without oxygen", [r"sulfur dioxide", r"ozone", r"radon"],
          r"Landfills are anaerobic; composting is aerobic and produces mostly CO$_2$ and water.",
          [r"Anaerobic decay makes methane."],
          [r"sulfur dioxide comes from burning sulfur-containing fuels.",
           r"ozone is a secondary air pollutant.",
           r"radon comes from uranium decay."]),
        Q("8.11 Tertiary treatment", r"Which stage of sewage treatment removes nitrogen and phosphorus?",
          r"tertiary treatment", [r"primary treatment", r"secondary treatment", r"screening"],
          r"Tertiary treatment uses chemical and biological processes to remove nutrients that would cause eutrophication.",
          [r"Nutrients: tertiary."],
          [r"primary treatment removes solids by settling.",
           r"secondary treatment removes organic matter.",
           r"screening is part of primary treatment."]),
        Q("8.15 Vector-borne disease", r"Why might climate change increase the range of malaria?",
          r"Warmer temperatures let the mosquitoes that carry the parasite survive at higher latitudes and elevations.", [r"Malaria is caused by air pollution.", r"Cooler winters kill more mosquitoes.", r"Malaria spreads through contaminated drinking water."],
          r"Malaria parasites are transmitted by \emph{Anopheles} mosquitoes, whose range is limited by temperature.",
          [r"Vector range follows climate."],
          [r"malaria is caused by a parasite.",
           r"warmer, not cooler, winters favor mosquitoes.",
           r"malaria is spread by mosquitoes, not water."]),
        Q("8.14 Lead", r"Why is lead in drinking water or old paint especially harmful to children?",
          r"It damages the developing nervous system, impairing learning and behavior.", [r"It causes skin cancer.", r"It improves bone growth.", r"It is harmless in small amounts to children."],
          r"There is no known safe level of lead exposure for children.",
          [r"Neurotoxin."],
          [r"lead's main effect is neurological.",
           r"lead is toxic.",
           r"even low levels are harmful."]),
    ]),
]

UNIT = Unit(8, "aquatic-terrestrial-pollution", "Aquatic and Terrestrial Pollution", "7--10\\%", "8.1--8.15",
    abstract=r"""Unit 8 covers pollution of water and land and its effects on ecosystems and health: point and nonpoint sources, impacts on reefs, oceans and wetlands, endocrine disruptors, eutrophication, thermal pollution, persistent organic pollutants, bioaccumulation and biomagnification, solid waste and waste reduction, sewage treatment, dose--response and LD$_{50}$, pollution and human health, and pathogens and infectious diseases. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6], qsections=QS,
    frq=FRQ("Design an investigation", 10, r"""\emph{Daphnia} (water fleas) are small crustaceans often used to test water toxicity. In a laboratory study, groups of $20$ \emph{Daphnia} were exposed to different concentrations of dissolved copper for $48$ hours. The graph shows the percentage that died.

[[fig]]""", [
        Part("(a)(i)", 1, r"\textbf{Identify} the LD$_{50}$ of copper for \emph{Daphnia} in this study.",
             r"About $30\ \mu$g/L (where the curve crosses $50\%$ mortality).",
             r"Reading the concentration at $100\%$ mortality."),
        Part("(a)(ii)", 1, r"\textbf{Explain} why some \emph{Daphnia} died in the group with no copper.",
             r"Some deaths occur from natural causes or handling; the $0\ \mu$g/L group (the control) shows this background mortality, which is about $2\%$.",
             r"Saying the control was contaminated, without considering background death."),
        Part("(b)(i)", 1, r"Students want to test whether road salt (sodium chloride) runoff harms \emph{Daphnia}. \textbf{Identify} a testable hypothesis.",
             r"For example: \emph{Daphnia} exposed to higher concentrations of sodium chloride will have higher mortality (or lower heart rates) than those in fresh water.",
             r"A hypothesis about copper instead of road salt."),
        Part("(b)(ii)", 1, r"\textbf{Identify} the independent variable.",
             r"The concentration of sodium chloride.",
             r"Naming mortality."),
        Part("(b)(iii)", 1, r"\textbf{Identify} the dependent variable.",
             r"The percentage of \emph{Daphnia} that die in $48$ hours (or their heart rate).",
             r"Naming the salt concentration."),
        Part("(b)(iv)", 1, r"\textbf{Identify} an appropriate control.",
             r"A group of \emph{Daphnia} kept in the same water with no added salt, under the same conditions.",
             r"A control that differs in more than one way."),
        Part("(b)(v)", 1, r"\textbf{Describe} one way to make the results more reliable.",
             r"Use several replicate containers at each concentration, the same number of similar-aged \emph{Daphnia} per container, and the same temperature, light and time; average the results.",
             r"``Be careful'' with no specific method."),
        Part("(c)", 1, r"\textbf{Describe} one way that road salt reaches freshwater ecosystems.",
             r"Salt spread on roads in winter dissolves in melting snow and rain and is carried by runoff into storm drains, streams and lakes, or seeps into groundwater.",
             r"Naming a source without a pathway."),
        Part("(d)(i)", 1, r"\textbf{Propose} one way to reduce the amount of road salt entering streams.",
             r"For example: apply less salt using calibrated spreaders or brine pretreatment; use alternatives such as sand; build vegetated buffers or retention ponds that capture runoff.",
             r"Stopping all winter road maintenance."),
        Part("(d)(ii)", 1, r"\textbf{Justify} how your proposal reduces salt reaching streams.",
             r"Linked to (d)(i): e.g., brine pretreatment keeps ice from bonding to the road, so much less salt is needed for the same safety, and less is washed off.",
             r"A justification unrelated to the proposal."),
    ], mins=23, fig=DOSE),
    frq_topic="copper toxicity in Daphnia and road salt",
)
