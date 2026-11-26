from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph, Series

TILL = Graph(r"Tillage practice", r"Soil loss (t/ha per year)", x=(0, 1, 1), y=(0, 20, 5), kind="bar",
             cats=["Conventional / tillage", "Reduced / tillage", "No-till", "No-till with / cover crop"],
             series=[Series("soil loss", [18, 9, 3, 1])], legend=False, width=4.6)

S1 = Sec("The commons, clearcutting and sustainable forestry (5.1, 5.2, 5.17)", ["5.1", "5.2", "5.17"], r"""
\textbf{The tragedy of the commons}: when a resource is shared and open to all (a pasture, a fishery, the air), each user gains from taking more, while the cost of depletion is shared by everyone, so the resource tends to be overused. Remedies include regulation, quotas, permits and private or community management.

\textbf{Clearcutting} removes all the trees from an area at once. It is cheap and efficient, but it destroys habitat, exposes soil to erosion (silting streams and raising their temperature as shade is lost), releases stored carbon, and reduces the area's ability to absorb water.

\textbf{Sustainable forestry} aims to keep forests productive indefinitely: selective cutting of individual trees, replanting with native species, protecting old-growth stands, prescribed burns to reduce fuel buildup, integrated pest management, and using recycled wood products.
""", checks=[
    Q("5.2 Clearcutting", r"Which is an environmental consequence of clearcutting a forest on a hillside next to a stream?",
      r"more soil erosion, which increases sediment in the stream", [r"lower stream temperatures from increased shade", r"less runoff during rainstorms", r"more carbon stored on the site"],
      r"Without roots and leaf cover, soil washes downhill into the stream; loss of shade also warms the water.",
      [r"Roots hold soil; canopy shades streams."],
      [r"clearcutting removes shade, so streams warm.",
       r"bare ground increases runoff.",
       r"cutting and decomposition release stored carbon."]),
])

S2 = Sec("The Green Revolution, agricultural practices and irrigation (5.3--5.5)", ["5.3", "5.4", "5.5"], r"""
The \textbf{Green Revolution} (from the 1950s) greatly raised crop yields with high-yield varieties, synthetic fertilizers, pesticides, irrigation and mechanization, and later genetically modified crops. The costs include heavy fossil-fuel use, fertilizer runoff, pesticide resistance, loss of crop genetic diversity in monocultures, and soil degradation.

\textbf{Practices.} Tilling loosens soil and controls weeds but leaves it exposed to erosion; slash-and-burn clears forest for short-lived fertility; synthetic fertilizers act fast but leach and run off, while organic fertilizers (manure, compost) release nutrients slowly and improve soil.

\begin{compare}{Irrigation method}{Approximate efficiency}{Notes}
Furrow & about $65\%$ & cheap; much water lost to evaporation and runoff \\
Flood & about $80\%$ & can waterlog soil \\
Spray & $75$--$95\%$ & more expensive; uses energy to pump \\
Drip & over $95\%$ & delivers water directly to roots; costly to install \\
\end{compare}
Over-irrigation causes \textbf{waterlogging} and, in dry climates, \textbf{salinization}: as water evaporates it leaves salts that build up in the soil. Pumping groundwater faster than it recharges depletes aquifers (the Ogallala Aquifer) and, near coasts, draws in seawater.
""", checks=[
    Q("5.5 Salinization", r"In an arid region, irrigated fields gradually become less productive, and a white crust appears on the soil. What is the most likely cause?",
      r"salinization: salts left behind as irrigation water evaporates", [r"acid rain from nearby factories", r"too much organic matter in the soil", r"nitrogen fixation by bacteria"],
      r"Irrigation water contains dissolved salts; in hot, dry climates the water evaporates and the salts accumulate.",
      [r"Evaporation concentrates salts."],
      [r"acid rain does not leave a white salt crust.",
       r"organic matter improves soil.",
       r"nitrogen fixation adds a nutrient, not salt."]),
])

S3 = Sec("Pest control and integrated pest management (5.6, 5.14)", ["5.6", "5.14"], r"""
Pesticides protect crops but can kill beneficial organisms (pollinators, predators of pests), run off into water, and lead to pesticide-resistant pests through natural selection, so ever more or stronger pesticides are needed. Genetically modified crops can carry their own toxins (Bt crops) or tolerate herbicides, with similar risks of resistance.

\textbf{Integrated pest management (IPM)} combines methods to keep pests below damaging levels with minimal chemicals: monitoring pest populations, biological control (natural predators and parasites), crop rotation, intercropping, physical barriers, and targeted pesticide use only when needed. It reduces costs, resistance and harm to nontarget species, but takes more knowledge and labor.
""", checks=[
    Q("5.6 Resistance", r"A pesticide controls a crop pest well for a few years and then becomes less effective. Which best explains this?",
      r"Individual pests with resistance survived and reproduced, so resistance spread in the population.", [r"The pesticide breaks down faster in later years.", r"The pests learned to avoid the pesticide.", r"The pesticide caused each pest to mutate."],
      r"Natural selection favors resistant individuals, so the resistance allele becomes common.",
      [r"Selection for resistance."],
      [r"the chemical is unchanged.",
       r"learning is not inherited.",
       r"mutations are random, not caused by the pesticide."]),
])

S4 = Sec("Meat production, fishing and aquaculture (5.7, 5.8, 5.16)", ["5.7", "5.8", "5.16"], r"""
\textbf{Meat production.} Concentrated animal feeding operations (CAFOs) produce meat cheaply on little land, but concentrate manure (water pollution, E.\ coli, odor), use antibiotics (resistant bacteria) and require grain grown elsewhere. Free-range grazing avoids some of these problems but can overgraze land, causing erosion and desertification. Because of the 10\% rule, it takes far more land, water and energy to produce a calorie of meat than a calorie of grain.

\textbf{Overfishing} removes fish faster than they reproduce; fisheries can collapse, and bottom trawling destroys seafloor habitat and catches bycatch (unwanted species). \textbf{Aquaculture} (fish farming) uses little land and fuel and supplies much of the world's fish, but can pollute water with wastes and antibiotics, spread disease to wild fish, and let farmed fish escape; feeding carnivorous farmed fish may require catching wild fish for fishmeal.
""", checks=[
    Q("5.7 Feeding efficiency", r"Why does producing $1$ kg of beef require much more land than producing $1$ kg of grain?",
      r"Cattle use most of the energy in their feed for their own metabolism, so many kilograms of grain are needed for each kilogram of beef.", [r"Cattle need more water than any other organism.", r"Grain cannot grow on grazing land.", r"Beef contains no energy."],
      r"Only about $10\%$ of the energy in feed ends up stored in the animal's body.",
      [r"Moving up a trophic level costs energy."],
      [r"water is part of it, but the main reason is energy loss.",
       r"some grazing land could grow grain, some could not; this is not the main reason.",
       r"beef is energy-rich; the energy came from the feed."]),
])

S5 = Sec("Mining, urbanization and urban runoff (5.9, 5.10, 5.13)", ["5.9", "5.10", "5.13"], r"""
\textbf{Mining.} Surface mining (strip mining, mountaintop removal, open pits) is cheaper and safer for workers but removes vegetation and soil; subsurface mining reaches deeper deposits but is more dangerous. Both create tailings and can cause acid mine drainage. As the richest ores are used up, lower-grade ores must be mined, increasing waste and energy. Reclamation restores mined land.

\textbf{Urbanization} replaces vegetation with impervious surfaces (roads, roofs, parking lots): rainwater runs off instead of soaking in, causing flooding and carrying pollutants into streams, while groundwater is not recharged. Cities are warmer than their surroundings (the urban heat island). Sprawl increases driving and habitat loss; coastal cities pumping groundwater can suffer saltwater intrusion.

\textbf{Reducing urban runoff:} permeable pavement, rain gardens and green roofs, planting trees, and building more densely near public transit.
""", checks=[
    Q("5.13 Permeable pavement", r"A city replaces some parking lots with permeable pavement. What is the main environmental benefit?",
      r"More rainwater infiltrates the ground, reducing runoff and flooding and recharging groundwater.", [r"It increases the urban heat island effect.", r"It increases the amount of runoff entering streams.", r"It makes parking lots more slippery."],
      r"Water passes through the pavement into the soil instead of flowing over it.",
      [r"Infiltration instead of runoff."],
      [r"permeable surfaces tend to reduce heat compared with asphalt.",
       r"it reduces runoff.",
       r"permeable pavement drains water away from the surface."]),
])

S6 = Sec("Ecological footprints, sustainability and sustainable agriculture (5.11, 5.12, 5.15)", ["5.11", "5.12", "5.15"], r"""
An \textbf{ecological footprint} is the area of land and water needed to provide the resources a person or population uses and absorb its wastes; a carbon footprint counts the greenhouse gases emitted. People in wealthier countries generally have much larger footprints.

\textbf{Sustainability} means meeting present needs without compromising the ability of future generations to meet theirs; a \textbf{sustainable yield} is the amount of a renewable resource that can be taken without reducing its future supply. Environmental indicators (biodiversity, food production, atmospheric CO$_2$, human population, resource depletion) show whether a society is on a sustainable path.

\begin{terms}
Contour plowing and terracing & furrows or steps across slopes slow runoff and erosion \\
Windbreaks & rows of trees reduce wind erosion \\
No-till and cover crops & keep the soil covered and add organic matter \\
Crop rotation & alternating crops (including nitrogen-fixing legumes) restores nutrients and breaks pest cycles \\
Rotational grazing & moving livestock lets pasture recover \\
Lime & raises the pH of acidic soils \\
\end{terms}
""", checks=[
    Q("5.15 Contour plowing", r"A farmer on hilly land plows furrows that follow the contours of the slope rather than running up and down it. What is the main benefit?",
      r"The furrows slow water running downhill, reducing soil erosion.", [r"The furrows increase runoff, keeping fields dry.", r"It adds nitrogen to the soil.", r"It prevents pests from reaching the crops."],
      r"Each furrow acts as a small dam that slows water and lets it soak in.",
      [r"Across the slope, not down it."],
      [r"it reduces runoff.",
       r"legumes, not plowing direction, add nitrogen.",
       r"plowing direction does not stop pests."]),
])

QS = [
    Set("Shared resources and forests (5.1, 5.2, 5.17)", [
        Q("5.1 Tragedy of the commons", r"Several herders share an unregulated pasture. Each adds animals because the extra profit goes to him, while the cost of overgrazing is shared. This is an example of",
          r"the tragedy of the commons", [r"sustainable yield", r"integrated pest management", r"ecological succession"],
          r"Individually rational choices deplete a shared resource.",
          [r"Shared, open-access resource, overused."],
          [r"a sustainable yield would avoid depletion.",
           r"IPM is a method of pest control.",
           r"succession is a change in a community over time."]),
        Q("5.17 Sustainable forestry", r"Which practice is an example of sustainable forestry?",
          r"selectively cutting mature trees and replanting with native species", [r"clearcutting large areas every few years", r"replacing native forest with a single fast-growing species", r"preventing all fires, including small natural ones"],
          r"Selective cutting keeps forest cover and habitat; replanting natives maintains the forest for the future.",
          [r"Harvest without depleting."],
          [r"frequent clearcutting degrades soil and habitat.",
           r"monoculture plantations lose biodiversity.",
           r"suppressing all fires lets fuel build up, risking severe fires."]),
        Q("5.1 Remedy", r"Which policy is most likely to prevent the overfishing of an open-access fishery?",
          r"setting and enforcing catch limits (quotas)", [r"subsidizing larger fishing boats", r"allowing anyone to fish without limits", r"increasing the use of bottom trawls"],
          r"Limiting the total catch keeps the harvest at or below a sustainable yield.",
          [r"Regulate access to the commons."],
          [r"subsidies increase fishing pressure.",
           r"open access is the cause of the problem.",
           r"trawling increases damage."]),
    ]),
    Set("Irrigation efficiency (5.5)", [
        Q("5.5 Furrow irrigation", r"A field's crop needs $600$ m$^3$ of water to reach its roots. How much water must be applied by furrow irrigation?",
          r"about $920$ m$^3$", [r"$390$ m$^3$", r"$600$ m$^3$", r"about $1200$ m$^3$"],
          r"Only $65\%$ reaches the crop: $600/0.65 = 923$ m$^3$.",
          [r"Applied $=$ needed $\div$ efficiency."],
          [r"multiplies by the efficiency instead of dividing.",
           r"assumes $100\%$ efficiency.",
           r"assumes $50\%$ efficiency."], sort=True),
        Q("5.5 Savings", r"How much water would switching this field from furrow to drip irrigation save?",
          r"about $290$ m$^3$", [r"about $920$ m$^3$", r"about $630$ m$^3$", r"about $30$ m$^3$"],
          r"Drip: $600/0.95 = 632$ m$^3$. Furrow: $923$ m$^3$. Savings $\approx 291$ m$^3$.",
          [r"Compute both, then subtract."],
          [r"is the furrow amount.",
           r"is the drip amount.",
           r"is the drip loss only."], sort=True),
        Q("5.5 Choosing a method", r"A farm in a dry region with expensive water wants to reduce water use and the risk of salinization. Which method is best?",
          r"drip irrigation", [r"flood irrigation", r"furrow irrigation", r"applying extra water to wash salts down"],
          r"Drip delivers water to roots with little evaporation, so less water is used and fewer salts accumulate.",
          [r"Most efficient method."],
          [r"flood irrigation wastes water and can waterlog soil.",
           r"furrow irrigation is the least efficient.",
           r"extra water raises costs and can waterlog soil."]),
    ], stim=r"""The table gives the approximate percentage of applied water that reaches crop roots for four irrigation methods.

\medskip
\begin{tabular}{@{}lc@{}}\toprule
Method & Water reaching crops (\%) \\ \midrule
Furrow & 65 \\
Flood & 80 \\
Spray & 90 \\
Drip & 95 \\ \bottomrule
\end{tabular}""", stim_title="Questions 4--6"),
    Set("Pests, food, mining, cities and sustainability (5.3--5.16)", [
        Q("5.14 IPM", r"Which practice is part of integrated pest management?",
          r"releasing ladybugs to eat aphids and spraying only when monitoring shows pests above a threshold", [r"spraying broad-spectrum pesticide on a fixed schedule", r"planting the same crop every year", r"removing all hedgerows around fields"],
          r"IPM combines biological control and monitoring to minimize chemical use.",
          [r"Monitor, then act with the least harmful method."],
          [r"scheduled spraying ignores pest levels.",
           r"monoculture year after year helps pests build up.",
           r"hedgerows shelter natural predators of pests."]),
        Q("5.3 Green Revolution", r"Which is a drawback of the Green Revolution?",
          r"increased dependence on fossil fuels for fertilizers, pesticides and machinery", [r"lower crop yields per hectare", r"more genetic diversity among crops", r"less use of irrigation"],
          r"High yields depend on energy-intensive inputs, and monocultures reduce crop diversity.",
          [r"Higher yields, higher inputs."],
          [r"yields rose sharply.",
           r"monocultures reduced diversity.",
           r"irrigation increased."]),
        Q("5.7 CAFOs", r"Which is an environmental problem associated with concentrated animal feeding operations?",
          r"large amounts of manure that can contaminate nearby water", [r"overgrazing of open rangeland", r"low meat production per hectare", r"increased habitat for wild predators"],
          r"Thousands of animals in a small area concentrate wastes, which can leak from lagoons or run off fields.",
          [r"Concentration of wastes."],
          [r"overgrazing is a problem of free-range grazing.",
           r"CAFOs produce a lot of meat on little land.",
           r"CAFOs do not create habitat."]),
        Q("5.16 Aquaculture", r"Which is an advantage of aquaculture compared with fishing in the open ocean?",
          r"It produces a large amount of food in a small area with relatively little fuel.", [r"It never causes water pollution.", r"Farmed fish never spread disease to wild fish.", r"It requires no feed."],
          r"Farms concentrate production; the trade-offs are wastes, disease and escapes.",
          [r"High yield per area."],
          [r"fish farms can release wastes and chemicals.",
           r"disease can spread to wild populations.",
           r"farmed fish must be fed, sometimes with fishmeal."]),
        Q("5.9 Mining", r"As the richest deposits of a metal ore are used up, what typically happens?",
          r"Lower-grade ores are mined, producing more waste and using more energy per tonne of metal.", [r"Mining stops completely.", r"The metal becomes renewable.", r"Mining produces less waste."],
          r"Less metal per tonne of rock means more rock moved and processed.",
          [r"Declining ore grade."],
          [r"demand usually continues.",
           r"metals are nonrenewable.",
           r"lower-grade ores produce more waste."]),
        Q("5.10 Urban runoff", r"After a city grows, a nearby stream floods more often after storms. What is the most likely cause?",
          r"More impervious surfaces send rainwater quickly into the stream instead of letting it soak in.", [r"The city's buildings block rainfall.", r"The urban heat island causes more rain to fall into the stream.", r"Groundwater rises because of increased infiltration."],
          r"Roads and roofs prevent infiltration, so runoff reaches the stream faster and in larger amounts.",
          [r"Pavement increases runoff."],
          [r"buildings do not reduce rainfall.",
           r"the heat island is not the main cause of flooding.",
           r"paving reduces infiltration."]),
        Q("5.11 Footprint", r"Which change would most reduce a household's ecological footprint?",
          r"eating less meat and driving less", [r"buying a larger house", r"flying more often", r"using more single-use plastic"],
          r"Meat and transportation are among the largest parts of most footprints in wealthy countries.",
          [r"Less land, energy and emissions."],
          [r"a larger house needs more energy and materials.",
           r"flying adds large carbon emissions.",
           r"plastics add resource use and waste."]),
    ]),
]

UNIT = Unit(5, "land-water-use", "Land and Water Use", "10--15\\%", "5.1--5.17",
    abstract=r"""Unit 5 covers how people use land and water: the tragedy of the commons, clearcutting and sustainable forestry, the Green Revolution and agricultural practices, irrigation methods and their problems, pest control and integrated pest management, meat production, overfishing and aquaculture, mining, urbanization and urban runoff, ecological footprints, and sustainability and sustainable agriculture. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6], qsections=QS,
    frq=FRQ("Design an investigation", 10, r"""A soil conservation study measured average annual soil loss from farm fields managed with four tillage practices. The results are shown in the graph.

[[fig]]""", [
        Part("(a)(i)", 1, r"\textbf{Identify} the practice that resulted in the least soil loss.",
             r"No-till with a cover crop (about $1$ t/ha per year).",
             r"Naming no-till alone."),
        Part("(a)(ii)", 1, r"\textbf{Explain} why conventional tillage leads to more soil loss than no-till.",
             r"Tilling breaks up the soil and buries crop residue, leaving bare, loose soil exposed to wind and rain; no-till leaves residue and roots that protect and hold the soil.",
             r"Saying tilling ``removes'' soil directly."),
        Part("(b)(i)", 1, r"A student plans to investigate whether planting a winter cover crop reduces the amount of nitrate that runs off farm plots. \textbf{Identify} a testable hypothesis.",
             r"For example: plots with a winter cover crop will have lower nitrate concentrations in their runoff than plots without a cover crop.",
             r"A hypothesis about soil loss rather than nitrate."),
        Part("(b)(ii)", 1, r"\textbf{Identify} the independent variable.",
             r"Whether a winter cover crop is planted (presence or absence of the cover crop).",
             r"Naming nitrate concentration."),
        Part("(b)(iii)", 1, r"\textbf{Identify} the dependent variable.",
             r"The nitrate concentration (or total nitrate) in runoff from the plots.",
             r"Naming the cover crop."),
        Part("(b)(iv)", 1, r"\textbf{Identify} an appropriate control for the investigation.",
             r"Plots managed the same way (same soil, slope, fertilizer and main crop) but with no cover crop.",
             r"A control that differs in more than one way."),
        Part("(b)(v)", 1, r"\textbf{Describe} a method for collecting the data.",
             r"For example: set up several replicate plots of each type on similar slopes; after each rainfall, collect runoff in a trough at the bottom of each plot and measure its nitrate concentration with a test kit or lab analysis; average the results.",
             r"No replication, or no way of collecting runoff."),
        Part("(c)", 1, r"\textbf{Describe} one environmental problem caused by nitrate runoff from farms.",
             r"Eutrophication of lakes, rivers and coastal waters: algal blooms die and decompose, using up dissolved oxygen and creating hypoxic dead zones that kill fish; nitrate in drinking water can also harm infants.",
             r"Naming a problem without describing it."),
        Part("(d)(i)", 1, r"\textbf{Propose} another farming practice that would reduce soil erosion on sloping fields.",
             r"For example: contour plowing, terracing, strip cropping, windbreaks, or planting perennial crops.",
             r"Repeating no-till or cover crops."),
        Part("(d)(ii)", 1, r"\textbf{Justify} how your practice reduces erosion.",
             r"Linked to (d)(i): e.g., contour furrows or terraces slow water flowing downhill, giving it time to soak in and reducing its power to carry soil away.",
             r"A justification unrelated to the proposed practice."),
    ], mins=23, fig=TILL),
    frq_topic="tillage practices and cover crops",
)
