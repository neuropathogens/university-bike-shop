from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part

S1 = Sec("Plate tectonics (4.1)", ["4.1"], r"""
Earth's lithosphere is broken into plates that move a few centimeters a year over the hot, slowly flowing mantle.
\begin{compare}{Boundary}{Motion}{Features}
Convergent & plates move toward each other & subduction zones, deep trenches, volcanoes (the Andes, Japan), mountain ranges where continents collide (the Himalayas) \\
Divergent & plates move apart & mid-ocean ridges and seafloor spreading, rift valleys (East Africa) \\
Transform & plates slide past each other & frequent earthquakes (the San Andreas Fault) \\
\end{compare}
Most volcanoes and earthquakes occur along plate boundaries, such as the Pacific Ring of Fire; hot spots (Hawaii) form volcanoes in the middle of plates. Tectonic activity shapes landforms, the distribution of minerals and the hazards people face.
""", checks=[
    Q("4.1 Convergent boundary", r"An oceanic plate is subducting beneath a continental plate. Which features are most likely to form?",
      r"a deep ocean trench and a chain of volcanoes on the continent", [r"a mid-ocean ridge with new seafloor", r"a rift valley", r"a transform fault with no volcanoes"],
      r"The denser oceanic plate sinks, forming a trench; melting at depth feeds volcanoes on the overriding plate (the Andes).",
      [r"Subduction: trench plus volcanic arc."],
      [r"ridges form at divergent boundaries.",
       r"rift valleys form where plates pull apart.",
       r"transform faults are where plates slide past each other."]),
])

S2 = Sec("Soil formation, erosion and properties (4.2--4.3)", ["4.2", "4.3"], r"""
Soil forms as parent rock is weathered (physically by freezing and thawing, chemically by acids, biologically by roots and lichens) and as organic matter accumulates. Soils develop in layers (horizons): O (organic litter), A (topsoil, rich in humus), B (subsoil, where minerals accumulate) and C (weathered parent material). Wind and water erode topsoil, especially when vegetation is removed; topsoil forms far more slowly than it can be lost.

\begin{compare}{Particle}{Size}{Effect on soil}
Sand & largest & large pores: high permeability, drains fast, holds little water or nutrients \\
Silt & medium & intermediate \\
Clay & smallest & tiny pores: low permeability, holds water and nutrients but can waterlog \\
\end{compare}
A \textbf{loam} (a mixture, about $40\%$ sand, $40\%$ silt, $20\%$ clay) balances drainage with water and nutrient retention and is best for most crops. Fertility also depends on organic matter, nutrients and pH. The soil texture triangle classifies a soil from its percentages of sand, silt and clay.
""", checks=[
    Q("4.3 Sandy soil", r"Compared with a clay soil, a sandy soil typically has",
      r"higher permeability and lower water-holding capacity", [r"lower permeability and higher water-holding capacity", r"more nutrients and better aeration", r"smaller particles and more pore space between them"],
      r"Large sand grains leave large pores: water drains through quickly and little is retained.",
      [r"Sand: fast drainage. Clay: high retention."],
      [r"describes clay.",
       r"sand holds fewer nutrients.",
       r"sand particles are the largest."]),
])

S3 = Sec("Earth's atmosphere (4.4)", ["4.4"], r"""
The atmosphere is about $78\%$ nitrogen, $21\%$ oxygen and $1\%$ argon, with small but important amounts of water vapor and carbon dioxide (about $0.04\%$).
\begin{terms}
Troposphere & $0$ to about $12$ km; nearly all weather and most of the air's mass; temperature falls with height \\
Stratosphere & about $12$ to $50$ km; contains the ozone layer, which absorbs ultraviolet radiation; temperature rises with height \\
Mesosphere & temperature falls again; meteors burn up \\
Thermosphere & very thin and hot; the aurora \\
\end{terms}
""", checks=[
    Q("4.4 Layers", r"In which layer of the atmosphere does nearly all weather occur?",
      r"the troposphere", [r"the stratosphere", r"the mesosphere", r"the thermosphere"],
      r"The troposphere holds most of the atmosphere's mass and water vapor.",
      [r"Weather: troposphere. Ozone layer: stratosphere."],
      [r"the stratosphere contains the ozone layer and is stable.",
       r"the mesosphere is far above the weather.",
       r"the thermosphere is very thin."]),
])

S4 = Sec("Global wind patterns and watersheds (4.5--4.6)", ["4.5", "4.6"], r"""
\textbf{Wind patterns} come from uneven heating of Earth's surface. Warm, moist air rises at the equator, cools and drops rain (rainforests); the dry air sinks near $30^\circ$ N and S (deserts). These Hadley cells, together with the cells nearer the poles and the \textbf{Coriolis effect} (deflection caused by Earth's rotation), produce the trade winds and the westerlies.

A \textbf{watershed} is all the land that drains into a particular river, lake or bay. Its area, slope, soil, vegetation and land use control how much water runs off and what it carries. Clearing vegetation, paving and farming in a watershed increase runoff, erosion and pollution downstream.
""", checks=[
    Q("4.5 Deserts at 30 degrees", r"Many of the world's large deserts lie near $30^\circ$ N and $30^\circ$ S latitude. Why?",
      r"Dry air that rose at the equator and lost its moisture sinks there.", [r"These latitudes receive the most direct sunlight.", r"Ocean currents are coldest at these latitudes.", r"Mountains surround all these deserts."],
      r"In the Hadley cell, air that rains out over the tropics descends near $30^\circ$, warming and drying as it sinks.",
      [r"Rising air: rain. Sinking air: dry."],
      [r"the most direct sunlight is at the equator.",
       r"cold currents contribute in some places, but not this pattern.",
       r"many large deserts are not surrounded by mountains."]),
])

S5 = Sec("Solar radiation, seasons, geography and climate (4.7--4.8)", ["4.7", "4.8"], r"""
\textbf{Insolation} is greatest at the equator, where sunlight strikes most directly, and least near the poles, where the same light spreads over more area. \textbf{Seasons} are caused by the $23.5^\circ$ tilt of Earth's axis, which changes how directly each hemisphere receives sunlight during the year, not by changes in Earth's distance from the Sun.

Geography modifies climate:
\begin{itemize}
\item \textbf{Rain shadow}: moist air forced up a mountain cools and drops rain on the windward side; the leeward side is dry.
\item Oceans moderate coastal climates because water has a high specific heat; ocean currents carry heat (the Gulf Stream warms western Europe).
\item Albedo, the reflectivity of a surface, affects warming: ice and snow reflect most sunlight; forests and oceans absorb more.
\end{itemize}
""", checks=[
    Q("4.8 Rain shadow", r"The western side of a coastal mountain range receives heavy rain, while the eastern side is very dry. Prevailing winds blow from the west. Which explains this?",
      r"Air rising over the mountains cools and drops its moisture on the western side, so dry air descends on the eastern side.", [r"The eastern side is closer to the ocean.", r"The eastern side receives less sunlight.", r"Clouds cannot cross mountains."],
      r"This is the rain shadow effect.",
      [r"Windward wet, leeward dry."],
      [r"the ocean is on the western (windward) side.",
       r"sunlight is not the cause.",
       r"clouds do cross, but after losing much of their water."]),
])

S6 = Sec("El Ni\\~no and La Ni\\~na (4.9)", ["4.9"], r"""
Normally, trade winds blow warm surface water westward across the equatorial Pacific toward Indonesia and Australia, and cold, nutrient-rich water \textbf{upwells} along the coast of South America, supporting rich fisheries.

\textbf{El Ni\~no}: the trade winds weaken or reverse, warm water spreads east, and upwelling off South America is suppressed. Fisheries there collapse; Peru and Ecuador get heavy rains, while Indonesia and Australia have drought; weather shifts worldwide. \textbf{La Ni\~na} is the opposite: stronger trade winds, stronger upwelling, cooler water in the eastern Pacific. Together these are the El Ni\~no--Southern Oscillation (ENSO).
""", checks=[
    Q("4.9 Upwelling", r"During an El Ni\~no event, what happens to upwelling off the coast of Peru?",
      r"It decreases, because warm surface water lies over the cold, deeper water.", [r"It increases, because trade winds are stronger.", r"It is unchanged, because upwelling depends only on tides.", r"It increases, because the water is warmer."],
      r"A layer of warm, less dense water caps the cold water, and weaker winds no longer push surface water away from the coast.",
      [r"El Ni\~no: weak trade winds, warm water east, less upwelling."],
      [r"describes La Ni\~na.",
       r"upwelling is driven by winds and density differences.",
       r"warmer surface water suppresses upwelling."]),
])

QS = [
    Set("Plate tectonics (4.1)", [
        Q("4.1 Divergent boundary", r"Along the Mid-Atlantic Ridge, new oceanic crust forms as magma rises. What type of plate boundary is this?",
          r"divergent", [r"convergent", r"transform", r"subduction"],
          r"Plates moving apart let magma rise to form new crust: seafloor spreading.",
          [r"Spreading: divergent."],
          [r"convergent boundaries destroy or crumple crust.",
           r"transform boundaries slide past each other.",
           r"subduction occurs at convergent boundaries."]),
        Q("4.1 Earthquakes", r"Why does California have frequent earthquakes but few active volcanoes along the San Andreas Fault?",
          r"It is a transform boundary, where plates slide past each other without subduction.", [r"It is a divergent boundary.", r"It is a hot spot.", r"It is far from any plate boundary."],
          r"Friction as plates grind past each other causes earthquakes; with no subduction there is little melting.",
          [r"Transform: earthquakes, not volcanoes."],
          [r"divergent boundaries produce volcanism.",
           r"hot spots produce volcanoes.",
           r"it lies right on a plate boundary."]),
    ]),
    Set("Three soils (4.2--4.3)", [
        Q("4.3 Fastest drainage", r"Which soil has the highest permeability?",
          r"Soil 1", [r"Soil 2", r"Soil 3", r"They are all equal."],
          r"Soil 1 is mostly sand and has the fastest infiltration rate, $25$ cm/h.",
          [r"More sand, larger pores, faster drainage."],
          [r"is a loam with moderate drainage.",
           r"is mostly clay and drains very slowly.",
           r"their infiltration rates differ by a factor of $250$."]),
        Q("4.3 Waterlogging", r"Which soil is most likely to become waterlogged after heavy rain?",
          r"Soil 3", [r"Soil 1", r"Soil 2", r"none of them"],
          r"Soil 3 is $60\%$ clay, with tiny pores and an infiltration rate of only $0.1$ cm/h.",
          [r"Clay holds water and drains slowly."],
          [r"sandy soil drains quickly.",
           r"loam drains moderately.",
           r"clay soils waterlog easily."]),
        Q("4.3 Best for crops", r"Why is soil 2 the best choice for most crops?",
          r"It drains well enough for roots to get air but holds enough water and nutrients.", [r"It has the highest infiltration rate.", r"It holds the most water.", r"It contains no clay."],
          r"Soil 2 is a loam: a balance of particle sizes gives both drainage and retention.",
          [r"Loam balances the extremes."],
          [r"that is soil 1, which dries out.",
           r"that is soil 3, which waterlogs.",
           r"it contains $20\%$ clay."]),
        Q("4.3 Infiltration time", r"About how long would it take $5.0$ cm of water ponded on soil 2 to soak in?",
          r"$2.0$ hours", [r"$12.5$ hours", r"$0.5$ hours", r"$50$ hours"],
          r"$5.0\ \mathrm{cm} \div 2.5\ \mathrm{cm/h} = 2.0$ h.",
          [r"Depth divided by infiltration rate."],
          [r"multiplies instead of dividing.",
           r"inverts the ratio.",
           r"uses soil 3's rate."], sort=True),
    ], stim=r"""Students measured the texture and properties of three soils.

\medskip
\begin{tabular}{@{}lccc@{}}\toprule
 & Soil 1 & Soil 2 & Soil 3 \\ \midrule
Sand (\%) & 85 & 40 & 10 \\
Silt (\%) & 10 & 40 & 30 \\
Clay (\%) & 5 & 20 & 60 \\
Infiltration (cm/h) & 25 & 2.5 & 0.1 \\
Water held (\% by mass) & 8 & 25 & 40 \\ \bottomrule
\end{tabular}""", stim_title="Questions 3--6"),
    Set("Atmosphere, winds, climate and ENSO (4.4--4.9)", [
        Q("4.4 Ozone", r"The ozone layer, which absorbs most of the Sun's ultraviolet radiation, is found in which layer of the atmosphere?",
          r"the stratosphere", [r"the troposphere", r"the mesosphere", r"the thermosphere"],
          r"Ozone is concentrated about $15$ to $35$ km up, in the stratosphere.",
          [r"Ozone absorbing UV is why the stratosphere warms with height."],
          [r"ozone near the ground is a pollutant, not the protective layer.",
           r"the mesosphere lies above it.",
           r"the thermosphere lies far above it."]),
        Q("4.7 Seasons", r"What causes Earth's seasons?",
          r"the tilt of Earth's axis, which changes how directly sunlight strikes each hemisphere through the year", [r"changes in Earth's distance from the Sun", r"changes in the Sun's energy output", r"the rotation of Earth on its axis"],
          r"Earth is actually closest to the Sun in January, during the Northern Hemisphere's winter.",
          [r"Tilt, not distance."],
          [r"the distance changes only slightly and does not match the seasons.",
           r"solar output varies very little.",
           r"rotation causes day and night."]),
        Q("4.5 Coriolis effect", r"Why do winds in the Northern Hemisphere curve to the right of their direction of motion?",
          r"Earth's rotation deflects moving air (the Coriolis effect).", [r"Mountains always block winds from the left.", r"The Sun pulls winds toward it.", r"Ocean currents push the winds."],
          r"Because Earth rotates, air moving across its surface is deflected: right in the Northern Hemisphere, left in the Southern.",
          [r"Coriolis: rotation."],
          [r"mountains affect local winds only.",
           r"the Sun drives winds by heating, not by pulling.",
           r"winds drive ocean currents, not the reverse."]),
        Q("4.8 Coastal climate", r"A coastal city has milder winters and cooler summers than an inland city at the same latitude. Why?",
          r"The ocean's high specific heat moderates temperature changes near the coast.", [r"Coastal cities receive less sunlight.", r"Inland cities have more ozone.", r"Coastal air has no water vapor."],
          r"Water warms and cools slowly, so nearby air stays closer to the ocean's temperature.",
          [r"High specific heat buffers temperature."],
          [r"they receive similar sunlight at the same latitude.",
           r"ozone does not explain local temperature.",
           r"coastal air is usually humid."]),
        Q("4.6 Watershed", r"Which change in a watershed would most increase the amount of sediment reaching the river?",
          r"clearing forest on steep slopes for development", [r"planting vegetation along stream banks", r"restoring wetlands near the river", r"reducing the area of paved surfaces"],
          r"Without roots and leaf cover, soil on steep slopes erodes and washes downhill.",
          [r"Vegetation holds soil."],
          [r"riparian plants trap sediment.",
           r"wetlands slow water and trap sediment.",
           r"less pavement reduces runoff."]),
    ]),
]

UNIT = Unit(4, "earth-systems-resources", "Earth Systems and Resources", "10--15\\%", "4.1--4.9",
    abstract=r"""Unit 4 covers the physical Earth: plate tectonics, soil formation, erosion and soil properties, the structure and composition of the atmosphere, global wind patterns and the Coriolis effect, watersheds, solar radiation and the seasons, how geography shapes climate (rain shadows, oceans, albedo), and El Ni\~no and La Ni\~na. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6], qsections=QS,
    frq=FRQ("Analyze and interpret quantitative data", 10, r"""The table shows the average sea surface temperature anomaly (the difference from the long-term average) off the coast of Peru and the catch of Peruvian anchovy in six years. The data are illustrative.

\medskip
\begin{tabular}{@{}ccc@{}}\toprule
Year & SST anomaly ($^\circ$C) & Anchovy catch (million tonnes) \\ \midrule
1 & $-0.5$ & 8.6 \\
2 & $-0.8$ & 8.9 \\
3 & $+2.3$ & 7.7 \\
4 & $+2.1$ & 1.7 \\
5 & $-1.2$ & 8.7 \\
6 & $-0.9$ & 11.3 \\ \bottomrule
\end{tabular}""", [
        Part("(a)(i)", 1, r"\textbf{Identify} the year with the largest positive sea surface temperature anomaly.",
             r"Year 3 ($+2.3^\circ$C).",
             r"Naming year 4, which had the lowest catch."),
        Part("(a)(ii)", 1, r"\textbf{Describe} the relationship between the temperature anomaly and the anchovy catch.",
             r"The catch is lowest after years with large positive (warm) anomalies, and high in cool years; the drop appears in the year after warming begins (years 3--4).",
             r"Saying the catch rises with temperature."),
        Part("(b)(i)", 1, r"\textbf{Identify} the climate phenomenon that causes large positive temperature anomalies off Peru.",
             r"El Ni\~no (the El Ni\~no--Southern Oscillation).",
             r"Naming La Ni\~na."),
        Part("(b)(ii)", 1, r"\textbf{Explain} how warmer surface water leads to fewer anchovy.",
             r"Warm surface water suppresses the upwelling of cold, nutrient-rich deep water, so fewer nutrients reach the sunlit surface; phytoplankton productivity falls, and the anchovy, which feed on plankton, starve, move away or reproduce poorly.",
             r"Saying the warm water ``cooks'' the fish."),
        Part("(b)(iii)", 1, r"\textbf{Explain} the role of the trade winds in this change.",
             r"Normally trade winds push warm surface water west, letting cold water upwell along South America; during El Ni\~no the trade winds weaken, warm water spreads east, and upwelling slows.",
             r"Saying the trade winds become stronger."),
        Part("(c)(i)", 1, r"\textbf{Calculate} the percent change in the anchovy catch from year 3 to year 4.",
             r"$(1.7 - 7.7)/7.7 \times 100 = -78\%$ (a decrease of about $78\%$).",
             r"Dividing by the year 4 catch."),
        Part("(c)(ii)", 1, r"\textbf{Identify} one other organism that would likely decline when anchovy populations crash.",
             r"Seabirds (such as boobies and pelicans), sea lions, or predatory fish that eat anchovy.",
             r"Naming the phytoplankton, which decline first, not as a result."),
        Part("(c)(iii)", 1, r"\textbf{Describe} one effect of El Ni\~no on weather in another part of the world.",
             r"For example: drought in Indonesia and Australia; heavy rain and flooding in coastal Peru and Ecuador; wetter winters in the southern United States.",
             r"Describing ocean temperature off Peru again."),
        Part("(d)(i)", 1, r"\textbf{Propose} one fisheries management strategy that could help the anchovy population recover after an El Ni\~no event.",
             r"For example: lower catch quotas or close the fishery during and after El Ni\~no years; protect spawning areas; set minimum size limits.",
             r"``Stop El Ni\~no.''"),
        Part("(d)(ii)", 1, r"\textbf{Justify} how your strategy would help the population recover.",
             r"Linked to (d)(i): reducing fishing when the stock is already low leaves more adults to reproduce, so the population can rebuild when cool, nutrient-rich conditions return.",
             r"A justification unrelated to the strategy."),
    ], mins=23),
    frq_topic="El Niño and the anchovy fishery",
)
