import math

from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph


def peak(height, hour, width, base):
    return lambda t: base + height * math.exp(-((t - hour) / width) ** 2)


SMOG = Graph(r"Time of day (hour)", r"Concentration (ppb)", x=(0, 24, 4), y=(0, 120, 20), series=[],
             curves=[("NO", peak(70, 7.5, 1.6, 8), 0), ("NO$_2$", peak(55, 10, 2.0, 15), 1), ("O$_3$", peak(80, 14.5, 2.6, 15), 2)],
             legend_pos="ne", width=4.2)

S1 = Sec("Introduction to air pollution (7.1)", ["7.1"], r"""
\textbf{Primary pollutants} are emitted directly: carbon monoxide (CO), nitrogen oxides (NO$_x$), sulfur dioxide (SO$_2$), particulate matter (PM), volatile organic compounds (VOCs) and lead. \textbf{Secondary pollutants} form in the atmosphere from primary ones: tropospheric ozone, sulfuric and nitric acids.

The Clean Air Act sets limits for six \textbf{criteria pollutants}: CO, lead, NO$_2$, ozone, particulate matter and SO$_2$. Burning coal releases SO$_2$, NO$_x$, CO$_2$, particulates and mercury; vehicle engines release NO$_x$, CO and VOCs. Natural sources include volcanoes (SO$_2$, particulates), wildfires and lightning (NO$_x$).
""", checks=[
    Q("7.1 Secondary pollutant", r"Which is a secondary air pollutant?",
      r"tropospheric ozone", [r"carbon monoxide", r"sulfur dioxide", r"particulate matter from a smokestack"],
      r"Ground-level ozone is not emitted directly; it forms when NO$_x$ and VOCs react in sunlight.",
      [r"Secondary: formed in the air."],
      [r"CO is emitted directly by combustion.",
       r"SO$_2$ is emitted directly.",
       r"smokestack particulates are emitted directly."]),
])

S2 = Sec("Photochemical smog and thermal inversions (7.2--7.3)", ["7.2", "7.3"], r"""
\textbf{Photochemical smog} forms on sunny days in cities with heavy traffic. Sunlight splits NO$_2$ into NO and a free oxygen atom, which joins O$_2$ to form ozone (O$_3$). At night ozone reacts with NO and is removed, but VOCs react with NO during the day, leaving more ozone to build up. A typical day: NO peaks with the morning commute, NO$_2$ a few hours later, ozone in the early afternoon. Smog irritates eyes and lungs, worsens asthma and damages plants.

A \textbf{thermal inversion} occurs when a layer of warm air sits above cooler air near the ground. The cool air cannot rise, so pollutants are trapped near the surface. Inversions are common in valleys and basins (Los Angeles, Mexico City) and on clear, calm nights.
""", checks=[
    Q("7.3 Inversion", r"Why do air pollution levels rise during a thermal inversion?",
      r"A warm air layer above cooler surface air prevents the surface air, and its pollutants, from rising and dispersing.", [r"Warm air near the ground rises faster, carrying pollutants upward.", r"Inversions increase the amount of pollution emitted.", r"Rain washes pollutants into the air."],
      r"Normally air cools with height and rising air carries pollutants away; an inversion caps the surface layer.",
      [r"Warm lid on cool air."],
      [r"describes normal conditions, which disperse pollution.",
       r"emissions are unchanged; dispersal is reduced.",
       r"rain removes pollutants from the air."]),
])

S3 = Sec("Atmospheric CO$_2$, particulates and indoor air pollutants (7.4--7.5)", ["7.4", "7.5"], r"""
CO$_2$ and particulates come from natural sources (respiration, volcanoes, fires, dust) and human ones (burning fossil fuels and biomass, construction). Fine particles (PM$_{2.5}$) reach deep into the lungs and the bloodstream and cause respiratory and heart disease; particulates also reduce visibility (haze).

\textbf{Indoor air pollution} can be worse than outdoor:
\begin{terms}
Carbon monoxide & from faulty furnaces and stoves; binds hemoglobin and can kill \\
Radon & radioactive gas from the decay of uranium in rock and soil; seeps into basements; the second leading cause of lung cancer \\
Formaldehyde & from furniture, carpets and glues \\
Asbestos and lead & in older insulation and paint \\
Smoke from cooking fires & a major health risk in developing countries that burn wood, dung or charcoal indoors \\
\end{terms}
""", checks=[
    Q("7.5 Radon", r"A family's basement tests high for radon. Where does the radon come from?",
      r"the radioactive decay of uranium in the rock and soil beneath the house", [r"the burning of natural gas in the furnace", r"vehicle exhaust", r"mold growing on the walls"],
      r"Radon gas seeps through cracks in foundations; ventilation and sealing reduce it.",
      [r"Radon: a natural radioactive gas."],
      [r"combustion produces CO, not radon.",
       r"exhaust does not contain radon.",
       r"mold releases spores, not radon."]),
])

S4 = Sec("Reduction of air pollutants (7.6)", ["7.6"], r"""
\begin{compare}{Method}{Removes}{How}
Catalytic converter & CO, NO$_x$, hydrocarbons from vehicles & converts them to CO$_2$, N$_2$ and water \\
Wet and dry scrubbers & SO$_2$ (and particulates) from smokestacks & a spray or powder of lime reacts with SO$_2$ \\
Electrostatic precipitator & particulates & charged plates attract and collect particles \\
Baghouse filter & particulates & fabric bags filter the exhaust \\
Fluidized-bed combustion & SO$_2$, NO$_x$ & burns coal at lower temperatures mixed with limestone \\
\end{compare}
Prevention also works: switching from coal to natural gas or renewables, using low-sulfur coal, vapor-recovery nozzles at gas pumps, driving less, and regulations such as the Clean Air Act and emissions trading.
""", checks=[
    Q("7.6 Scrubbers", r"Which device is used to remove sulfur dioxide from the exhaust of a coal-fired power plant?",
      r"a wet or dry scrubber", [r"a catalytic converter", r"an electrostatic precipitator", r"a vapor-recovery nozzle"],
      r"Lime or limestone in a scrubber reacts with SO$_2$, turning it into a solid that can be removed.",
      [r"SO$_2$: scrubber."],
      [r"catalytic converters treat vehicle exhaust.",
       r"precipitators remove particles, not gases.",
       r"vapor-recovery nozzles capture gasoline vapors at pumps."]),
])

S5 = Sec("Acid rain and noise pollution (7.7--7.8)", ["7.7", "7.8"], r"""
\textbf{Acid deposition.} SO$_2$ and NO$_x$ react with water and oxygen in the air to form sulfuric and nitric acids, which fall as acid rain, snow or dry particles, often far downwind. Normal rain has a pH of about $5.6$ (from dissolved CO$_2$); acid rain is lower. Each pH unit is a tenfold change in hydrogen-ion concentration.

Effects: acidified lakes and streams harm fish and amphibians; acid leaches calcium and magnesium from soil and releases toxic aluminum, damaging forests; acid erodes limestone and marble buildings. Areas with limestone bedrock or soils can neutralize (buffer) acid; areas on granite cannot. Emissions controls on power plants have greatly reduced acid rain in the United States.

\textbf{Noise pollution} from traffic, industry and ships disrupts animal communication and behavior (birds, whales), causes stress and, at high levels, hearing loss in people.
""", checks=[
    Q("7.7 pH scale", r"Rain with a pH of $4.0$ is how many times more acidic than rain with a pH of $5.0$?",
      r"$10$ times", [r"$1$ time (the same)", r"$2$ times", r"$100$ times"],
      r"The pH scale is logarithmic: one unit is a factor of $10$ in hydrogen-ion concentration.",
      [r"$10^{5 - 4} = 10$."],
      [r"the values differ by one unit.",
       r"pH is logarithmic, not linear.",
       r"$100$ times would be two pH units."], sort=True),
])

QS = [
    Set("Air pollutants (7.1)", [
        Q("7.1 Coal combustion", r"Which pollutant is released mainly by burning coal rather than by vehicles?",
          r"sulfur dioxide", [r"carbon monoxide from cold engines", r"volatile organic compounds from gasoline", r"ozone"],
          r"Coal contains sulfur, which forms SO$_2$ when burned; gasoline is low in sulfur.",
          [r"Sulfur in fuel becomes SO$_2$."],
          [r"CO comes mostly from vehicles.",
           r"VOCs come mostly from fuels, solvents and vehicles.",
           r"ozone is secondary; it is not emitted directly."]),
        Q("7.1 Criteria pollutants", r"Which substance is one of the six criteria pollutants regulated by the Clean Air Act?",
          r"lead", [r"radon", r"carbon dioxide", r"formaldehyde"],
          r"The six are carbon monoxide, lead, nitrogen dioxide, ozone, particulate matter and sulfur dioxide.",
          [r"Six criteria pollutants."],
          [r"radon is an indoor pollutant, not a criteria pollutant.",
           r"CO$_2$ is not one of the six.",
           r"formaldehyde is an indoor pollutant."]),
        Q("7.4 Fine particles", r"Why are fine particles (PM$_{2.5}$) especially harmful to human health?",
          r"They are small enough to penetrate deep into the lungs and enter the bloodstream.", [r"They are radioactive.", r"They absorb ozone and destroy it.", r"They are too large to be inhaled."],
          r"Larger particles are trapped in the nose and throat; fine particles reach the alveoli.",
          [r"Smaller: deeper."],
          [r"most particulates are not radioactive.",
           r"particles do not protect against ozone.",
           r"fine particles are easily inhaled."]),
    ]),
    Set("A day of urban smog (7.2)", [
        Q("7.2 First peak", r"Which pollutant reaches its peak concentration first in the day?",
          r"nitrogen oxide (NO)", [r"nitrogen dioxide (NO$_2$)", r"ozone (O$_3$)", r"All three peak at the same time."],
          r"NO peaks around $7$--$8$ a.m., during the morning commute, as vehicles emit it.",
          [r"Primary pollutants peak with emissions."],
          [r"NO$_2$ peaks a couple of hours later, as NO is oxidized.",
           r"ozone peaks in the early afternoon.",
           r"the peaks are hours apart."]),
        Q("7.2 Afternoon ozone", r"Why does ozone peak in the early afternoon?",
          r"Ozone forms when sunlight splits NO$_2$, and sunlight and NO$_2$ are most available by early afternoon.", [r"Vehicles emit the most ozone in the afternoon.", r"Ozone is emitted directly by power plants at midday.", r"Ozone forms only at night."],
          r"Photochemical reactions need sunlight; ozone builds up as NO$_2$ is split through the day.",
          [r"Secondary pollutant made by sunlight."],
          [r"vehicles emit NO$_x$ and VOCs, not ozone.",
           r"ozone is not emitted directly.",
           r"ozone is removed at night."]),
        Q("7.2 Ozone is secondary", r"Why is ground-level ozone called a secondary pollutant?",
          r"It forms in the atmosphere from reactions of primary pollutants.", [r"It is the second most common pollutant.", r"It is less harmful than primary pollutants.", r"It is emitted by secondary sources such as factories."],
          r"Ozone results from NO$_2$, VOCs and sunlight; it has no direct emission source.",
          [r"Secondary: formed, not emitted."],
          [r"the term is about how it forms, not how common it is.",
           r"ground-level ozone is harmful.",
           r"no source emits ozone directly in significant amounts."]),
        Q("7.6 Reducing smog", r"Which measure would most directly reduce the morning peak in the graph and the ozone that follows?",
          r"reducing vehicle emissions of nitrogen oxides with catalytic converters and less driving", [r"installing scrubbers on coal plants to remove SO$_2$", r"testing homes for radon", r"planting more trees to absorb sulfur"],
          r"Less NO$_x$ in the morning means less NO$_2$ to be split and less ozone in the afternoon.",
          [r"Cut the precursors."],
          [r"SO$_2$ is not a smog precursor in this graph.",
           r"radon is an indoor pollutant.",
           r"trees do not remove sulfur in a way that affects smog."]),
    ], fig=SMOG, stim=r"The graph shows typical concentrations of nitrogen oxide (NO), nitrogen dioxide (NO$_2$) and ozone (O$_3$) over a sunny summer day in a large city.",
        stim_title="Questions 4--7"),
    Set("Acid deposition, control and indoor air (7.3--7.8)", [
        Q("7.7 Buffering", r"Two lakes receive the same acid rain. Lake A sits on limestone bedrock and lake B on granite. Which is more likely to become acidified?",
          r"lake B, because granite cannot neutralize the acid", [r"lake A, because limestone adds acid to the water", r"both equally", r"neither, because lakes cannot become acidic"],
          r"Limestone (calcium carbonate) neutralizes acids; granite has little buffering capacity.",
          [r"Buffering capacity of the bedrock."],
          [r"limestone neutralizes acid.",
           r"the bedrock makes the difference.",
           r"many lakes on granite have been acidified."]),
        Q("7.7 Acid rain sources", r"Which pair of pollutants is mainly responsible for acid rain?",
          r"sulfur dioxide and nitrogen oxides", [r"carbon monoxide and ozone", r"methane and radon", r"lead and mercury"],
          r"They form sulfuric and nitric acids in the atmosphere.",
          [r"SO$_2$ and NO$_x$."],
          [r"these do not form strong acids.",
           r"these do not form acid rain.",
           r"these are toxic metals, not acid formers."]),
        Q("7.6 Catalytic converter", r"What does a catalytic converter in a car do?",
          r"converts CO, NO$_x$ and hydrocarbons into CO$_2$, N$_2$ and water", [r"removes CO$_2$ from exhaust", r"removes sulfur dioxide from coal smoke", r"increases the engine's fuel consumption"],
          r"Catalysts speed reactions that convert harmful gases into less harmful ones.",
          [r"Vehicle exhaust control."],
          [r"it produces CO$_2$ rather than removing it.",
           r"that is a scrubber at a power plant.",
           r"it does not aim to change fuel use."]),
        Q("7.5 Carbon monoxide", r"Why is carbon monoxide from a faulty furnace dangerous?",
          r"It binds to hemoglobin and reduces the blood's ability to carry oxygen.", [r"It is radioactive.", r"It forms acid rain indoors.", r"It is easy to smell, so people panic."],
          r"CO is colorless and odorless; detectors are needed.",
          [r"CO blocks oxygen transport."],
          [r"CO is not radioactive.",
           r"CO does not form acid rain.",
           r"CO has no smell."]),
        Q("7.3 Inversion location", r"Which location is most prone to severe thermal inversions?",
          r"a city in a valley surrounded by mountains", [r"a windy coastal plain", r"a city on a high, open plateau with strong winds", r"an island in the open ocean"],
          r"Mountains trap cool air in the valley and block winds that would mix and clear the air.",
          [r"Basins and valleys trap air."],
          [r"wind mixes the air.",
           r"strong winds disperse pollutants.",
           r"open ocean air mixes readily."]),
        Q("7.8 Noise pollution", r"Increased ship traffic raises underwater noise levels in an ocean area. Which effect on wildlife is most likely?",
          r"Whales have more difficulty communicating and finding one another.", [r"Fish grow faster.", r"Coral reefs become more resistant to bleaching.", r"Algae photosynthesize more."],
          r"Many marine animals rely on sound to communicate, navigate and find food.",
          [r"Noise masks animal signals."],
          [r"noise does not speed growth.",
           r"bleaching depends on temperature.",
           r"noise does not affect photosynthesis."]),
    ]),
]

UNIT = Unit(7, "atmospheric-pollution", "Atmospheric Pollution", "7--10\\%", "7.1--7.8",
    abstract=r"""Unit 7 covers air pollution: primary and secondary pollutants and the criteria pollutants, photochemical smog and its daily cycle, thermal inversions, atmospheric CO$_2$ and particulates, indoor air pollutants (radon, carbon monoxide), technologies and policies that reduce emissions, acid deposition and buffering, and noise pollution. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5], qsections=QS,
    frq=FRQ("Analyze and interpret quantitative data", 10, r"""The table shows national sulfur dioxide emissions in a country and the average pH of rain measured at a monitoring station downwind of its power plants. The data are illustrative.

\medskip
\begin{tabular}{@{}ccc@{}}\toprule
Year & SO$_2$ emissions (million tonnes) & Rain pH \\ \midrule
1980 & 23.5 & 4.3 \\
1990 & 21.0 & 4.4 \\
2000 & 14.8 & 4.6 \\
2010 & 7.0 & 5.0 \\
2020 & 1.8 & 5.3 \\ \bottomrule
\end{tabular}""", [
        Part("(a)(i)", 1, r"\textbf{Identify} the trend in SO$_2$ emissions from 1980 to 2020.",
             r"Emissions decreased throughout, falling most rapidly after 1990.",
             r"Describing only one interval."),
        Part("(a)(ii)", 1, r"\textbf{Describe} the relationship between SO$_2$ emissions and the pH of rain.",
             r"As emissions decreased, the pH of rain increased (the rain became less acidic): an inverse relationship.",
             r"Saying pH fell as emissions fell."),
        Part("(b)(i)", 1, r"\textbf{Identify} the main human source of SO$_2$ emissions.",
             r"Burning coal (especially high-sulfur coal) in electric power plants; also some industrial processes such as metal smelting.",
             r"Naming vehicles."),
        Part("(b)(ii)", 1, r"\textbf{Explain} how SO$_2$ emissions lead to acid rain.",
             r"SO$_2$ reacts with oxygen and water vapor in the atmosphere to form sulfuric acid, which dissolves in cloud droplets and falls as acidic rain or snow.",
             r"Saying SO$_2$ ``is'' acid rain without the reaction."),
        Part("(b)(iii)", 1, r"\textbf{Explain} why lakes on granite bedrock are harmed by acid rain more than lakes on limestone.",
             r"Limestone (calcium carbonate) neutralizes, or buffers, the acid; granite provides little buffering, so the lake water's pH falls.",
             r"Saying granite produces acid."),
        Part("(c)(i)", 1, r"\textbf{Calculate} the percent decrease in SO$_2$ emissions from 1990 to 2020.",
             r"$(21.0 - 1.8)/21.0 \times 100 \approx 91\%$.",
             r"Dividing by the 2020 value."),
        Part("(c)(ii)", 1, r"\textbf{Calculate} how many times more acidic the rain was in 1980 (pH $4.3$) than in 2020 (pH $5.3$).",
             r"One pH unit difference: $10^{1} = 10$ times more acidic.",
             r"Treating pH as linear (``$1.2$ times'')."),
        Part("(c)(iii)", 1, r"\textbf{Describe} one effect of acid rain on forest ecosystems.",
             r"Acid leaches calcium and magnesium from the soil and releases toxic aluminum, weakening trees and making them more vulnerable to disease, insects and cold; acid fog damages leaves and needles.",
             r"Naming an effect on buildings or lakes instead."),
        Part("(d)(i)", 1, r"\textbf{Propose} one technology or policy that could reduce SO$_2$ emissions from power plants further.",
             r"For example: install wet or dry scrubbers; switch to low-sulfur coal or natural gas; replace coal plants with renewable energy; tighten an emissions cap.",
             r"Catalytic converters, which treat vehicle exhaust."),
        Part("(d)(ii)", 1, r"\textbf{Justify} how your proposal would reduce emissions.",
             r"Linked to (d)(i): e.g., in a scrubber, a slurry of lime or limestone reacts with SO$_2$ in the exhaust, converting it to calcium sulfate before it leaves the smokestack.",
             r"A justification unrelated to the proposal."),
    ], mins=23),
    frq_topic="sulfur dioxide emissions and acid rain",
)
