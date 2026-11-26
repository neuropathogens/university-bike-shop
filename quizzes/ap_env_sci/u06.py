from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part

S1 = Sec("Resources, consumption and fuel types (6.1--6.3)", ["6.1", "6.2", "6.3"], r"""
\textbf{Nonrenewable} resources form far more slowly than we use them: fossil fuels (coal, oil, natural gas) and nuclear fuels. \textbf{Renewable} resources are replenished on human timescales; some are \emph{depletable} if overused (biomass, such as wood), while others are effectively \emph{nondepletable} (solar, wind, geothermal, tidal).

Developed countries use far more energy per person than developing countries, mostly from fossil fuels; as countries industrialize, their energy use rises. Many people in developing countries rely on wood, charcoal or dung for cooking and heating, which contributes to deforestation and indoor air pollution.

\begin{terms}
Coal & ranks from peat and lignite (low energy, more moisture) to bituminous and anthracite (high carbon, most energy); dirtiest to burn \\
Crude oil & refined into gasoline, diesel, jet fuel and other products \\
Natural gas & mostly methane; produces the least CO$_2$ and air pollution of the fossil fuels per unit energy \\
Cogeneration & using a fuel to produce both electricity and useful heat, raising efficiency \\
\end{terms}
""", checks=[
    Q("6.1 Classifying resources", r"Which energy source is renewable but can be depleted if it is used faster than it is replaced?",
      r"wood (biomass)", [r"coal", r"solar energy", r"uranium"],
      r"Forests regrow, but harvesting them faster than they regrow depletes them.",
      [r"Depletable renewable."],
      [r"coal is nonrenewable.",
       r"solar energy cannot be depleted by use.",
       r"uranium is nonrenewable."]),
])

S2 = Sec("Fossil fuels and their distribution (6.4--6.5)", ["6.4", "6.5"], r"""
Burning a fossil fuel combines its hydrocarbons with oxygen, producing CO$_2$ and water and releasing energy. In a power plant, that heat boils water to make steam, which spins a turbine connected to a generator. Only about a third of the fuel's energy becomes electricity; the rest is lost as waste heat (often into a river or lake used for cooling).

Fossil fuels are unevenly distributed (large oil reserves in the Middle East; coal in the United States, China and Russia), which shapes trade and politics. Newer extraction methods have expanded supplies: \textbf{hydraulic fracturing} (fracking) injects water, sand and chemicals at high pressure to release natural gas from shale, raising concerns about groundwater contamination, wastewater, methane leaks and small earthquakes; oil can also be extracted from tar sands at high energy and environmental cost.
""", checks=[
    Q("6.5 Power plant energy", r"In a coal-fired power plant, what happens to most of the energy released by burning the coal?",
      r"It is lost as waste heat.", [r"It is converted to electricity.", r"It is stored in the steam permanently.", r"It is converted back into coal."],
      r"Typical efficiency is about $33$--$40\%$; the rest leaves as heat, much of it in cooling water.",
      [r"Second law: conversions are inefficient."],
      [r"only about a third becomes electricity.",
       r"the steam cools and condenses.",
       r"energy is not converted back into fuel."]),
])

S3 = Sec("Nuclear power (6.6)", ["6.6"], r"""
In a nuclear power plant, neutrons split uranium-235 nuclei (fission), releasing heat and more neutrons that sustain a controlled chain reaction; control rods absorb neutrons to regulate it. The heat makes steam to drive turbines, as in a fossil-fuel plant.

\textbf{Advantages}: no CO$_2$ or air pollutants from the reaction itself; a little fuel produces enormous energy. \textbf{Disadvantages}: spent fuel stays radioactive for thousands of years and needs long-term storage; mining uranium disturbs land; accidents (Three Mile Island 1979, Chernobyl 1986, Fukushima 2011) can release radiation; cooling water causes thermal pollution; plants are costly to build.

\textbf{Half-life} is the time for half of a radioactive sample to decay: after $n$ half-lives, $\left(\tfrac12\right)^n$ of it remains.
""", checks=[
    Q("6.6 Half-life", r"A sample contains $80$ g of a radioactive isotope with a half-life of $30$ years. How much of the isotope remains after $90$ years?",
      r"$10$ g", [r"$27$ g", r"$20$ g", r"$0$ g"],
      r"$90$ years is three half-lives: $80 \to 40 \to 20 \to 10$ g.",
      [r"Halve once per half-life."],
      [r"divides by $3$ instead of halving three times.",
       r"stops after two half-lives.",
       r"some isotope always remains after a few half-lives."], sort=True),
])

S4 = Sec("Biomass, solar, hydroelectric and geothermal energy (6.7--6.10)", ["6.7", "6.8", "6.9", "6.10"], r"""
\begin{compare}{Source}{Advantages}{Disadvantages}
Biomass and biofuels (wood, ethanol from corn or sugarcane, biodiesel) & renewable; can use wastes; often described as carbon-neutral & burning releases CO$_2$ and particulates; deforestation; corn ethanol needs land, water, fertilizer and fuel \\
Solar (photovoltaic cells; active and passive solar heating; concentrated solar power) & no emissions during operation; abundant & intermittent (night, clouds); needs storage; land and mining for materials \\
Hydroelectric (dams, run-of-river, tidal) & no emissions; reliable; reservoirs store water & dams flood habitat, block fish migration, trap sediment, change water temperature; reservoirs can release methane \\
Geothermal (power plants; ground-source heat pumps) & reliable, low emissions & power plants only where heat is near the surface; can release H$_2$S \\
\end{compare}
""", checks=[
    Q("6.9 Dams", r"Which is an environmental disadvantage of a large hydroelectric dam?",
      r"It blocks fish such as salmon from migrating upstream to spawn.", [r"It releases large amounts of sulfur dioxide.", r"It produces radioactive waste.", r"It works only when the wind blows."],
      r"Dams fragment rivers; fish ladders help only partly. Reservoirs also flood habitat and trap sediment.",
      [r"Dams change river ecosystems."],
      [r"sulfur dioxide comes from burning coal.",
       r"radioactive waste comes from nuclear power.",
       r"that describes wind power."]),
])

S5 = Sec("Hydrogen fuel cells, wind energy and energy conservation (6.11--6.13)", ["6.11", "6.12", "6.13"], r"""
A \textbf{hydrogen fuel cell} combines hydrogen and oxygen to produce electricity, with water as the only exhaust. But hydrogen must first be produced (usually from natural gas, or by electrolysis using electricity), and storing and distributing it is difficult, so its environmental benefit depends on how the hydrogen is made.

\textbf{Wind turbines} produce no emissions while running and can share land with farming, but wind is intermittent, turbines can kill birds and bats, and some people object to their noise and appearance.

\textbf{Energy conservation} is usually the cheapest ``source'' of energy: insulation and efficient windows, LED lighting, efficient appliances, programmable thermostats, fuel-efficient vehicles (CAFE standards), hybrid and electric vehicles, mass transit, and smart grids that match supply and demand.
""", checks=[
    Q("6.11 Fuel cells", r"A car powered by a hydrogen fuel cell emits only water vapor. Why might it still contribute to CO$_2$ emissions?",
      r"Most hydrogen is produced from natural gas, which releases CO$_2$.", [r"Fuel cells burn gasoline as a backup.", r"Water vapor is converted into CO$_2$ in the air.", r"Hydrogen contains carbon."],
      r"The emissions move from the tailpipe to wherever the hydrogen is made, unless renewable electricity is used for electrolysis.",
      [r"Consider the whole fuel cycle."],
      [r"fuel cells do not burn gasoline.",
       r"water vapor does not become CO$_2$.",
       r"hydrogen contains no carbon."]),
])

QS = [
    Set("Energy resources and fossil fuels (6.1--6.5)", [
        Q("6.3 Natural gas", r"Why is natural gas considered the ``cleanest'' fossil fuel?",
          r"It produces less CO$_2$ and fewer air pollutants per unit of energy than coal or oil.", [r"It is renewable.", r"Burning it releases no CO$_2$.", r"It is never extracted by fracking."],
          r"Methane is mostly hydrogen--carbon bonds with little sulfur or ash, so combustion is cleaner, though it still emits CO$_2$, and leaked methane is a potent greenhouse gas.",
          [r"Cleaner, not clean."],
          [r"natural gas is a fossil fuel.",
           r"burning methane produces CO$_2$.",
           r"much natural gas is extracted by fracking."]),
        Q("6.3 Coal rank", r"Which type of coal has the highest carbon content and releases the most energy per kilogram?",
          r"anthracite", [r"lignite", r"peat", r"bituminous coal"],
          r"Greater heat and pressure over time drive out moisture and volatiles, concentrating carbon.",
          [r"Peat $\to$ lignite $\to$ bituminous $\to$ anthracite."],
          [r"lignite is low-grade, moist coal.",
           r"peat is a precursor of coal.",
           r"bituminous is below anthracite."]),
        Q("6.5 Fracking", r"Which is a concern associated with hydraulic fracturing for natural gas?",
          r"contamination of groundwater by fracking fluids or methane", [r"radioactive fuel rods", r"flooding of river valleys", r"bird deaths from spinning blades"],
          r"Fluids, wastewater and escaping methane can reach aquifers if wells leak.",
          [r"Fracking risks: water, methane, quakes."],
          [r"fuel rods are a nuclear issue.",
           r"flooding valleys is a dam issue.",
           r"blade strikes are a wind issue."]),
        Q("6.2 Consumption", r"Which statement about global energy use is correct?",
          r"Per person, developed countries use much more energy than developing countries.", [r"Most of the world's energy comes from renewable sources.", r"Energy use per person is the same in every country.", r"Developing countries use no fossil fuels."],
          r"Fossil fuels still supply most of the world's energy, and use per person is far higher in wealthy countries.",
          [r"Consumption follows wealth."],
          [r"fossil fuels dominate.",
           r"use varies enormously.",
           r"developing countries use fossil fuels too, increasingly."]),
    ]),
    Set("Household energy (6.13)", [
        Q("6.13 Annual cost", r"What does the household spend on electricity in a year?",
          r"\$1350", [r"\$135", r"\$60{,}000", r"\$9000"],
          r"$9000$ kWh at \$0.15 per kWh costs \$1350.",
          [r"Energy used times price."],
          [r"misplaces the decimal.",
           r"divides by the price.",
           r"is the number of kilowatt-hours."]),
        Q("6.13 Emissions", r"How much CO$_2$ is emitted to generate the household's electricity each year?",
          r"$9.0$ metric tons", [r"$0.90$ metric tons", r"$90$ metric tons", r"$1.0$ metric ton"],
          r"$9000\ \mathrm{kWh} \times 1.0\ \mathrm{kg/kWh} = 9000$ kg $= 9.0$ t.",
          [r"$1$ metric ton $= 1000$ kg."],
          [r"divides by $10\,000$ instead of $1000$.",
           r"multiplies by $10$.",
           r"is the emission per kWh, not per year."], sort=True),
        Q("6.13 LED savings", r"How much money would the switch to LED lighting save each year?",
          r"\$90", [r"\$600", r"\$4", r"\$900"],
          r"$600$ kWh at \$0.15 per kWh is \$90 per year.",
          [r"Energy saved times price."],
          [r"is the energy saved, in kWh.",
           r"divides by the price.",
           r"misplaces the decimal."], sort=True),
        Q("6.13 Payback", r"If the LED bulbs cost \$180 in total, how long will they take to pay for themselves?",
          r"$2.0$ years", [r"$0.5$ years", r"$3.3$ years", r"$20$ years"],
          r"Payback $=$ cost $\div$ annual savings: \$180 divided by \$90 per year is $2.0$ years.",
          [r"Cost divided by annual savings."],
          [r"inverts the ratio.",
           r"uses \$54 a year of savings.",
           r"misplaces the decimal."], sort=True),
    ], stim=r"A household uses $9000$ kWh of electricity a year at \$0.15 per kWh. Its electricity comes from a coal-fired plant that emits $1.0$ kg of CO$_2$ per kWh delivered. Replacing all its light bulbs with LEDs would save $600$ kWh a year.",
        stim_title="Questions 5--8"),
    Set("Nuclear, renewables and conservation (6.6--6.13)", [
        Q("6.6 Control rods", r"What is the function of the control rods in a nuclear reactor?",
          r"to absorb neutrons and regulate the rate of the chain reaction", [r"to cool the reactor core directly", r"to produce electricity", r"to store spent fuel"],
          r"Lowering the rods absorbs more neutrons and slows fission; raising them speeds it.",
          [r"Neutrons sustain the chain reaction."],
          [r"cooling water removes heat.",
           r"the generator produces electricity.",
           r"spent fuel goes to cooling pools and dry casks."]),
        Q("6.6 Nuclear advantage", r"Which is an advantage of nuclear power over coal-fired power?",
          r"It releases no CO$_2$ or sulfur dioxide while generating electricity.", [r"It produces no waste.", r"Its plants are cheap to build.", r"It needs no cooling water."],
          r"Fission produces heat without combustion; the problems are radioactive waste, cost and accident risk.",
          [r"No combustion, no combustion products."],
          [r"spent fuel is long-lived radioactive waste.",
           r"nuclear plants are very expensive to build.",
           r"nuclear plants need large amounts of cooling water."]),
        Q("6.8 Passive solar", r"Which is an example of passive solar design?",
          r"large south-facing windows (in the Northern Hemisphere) and thick walls that absorb heat by day and release it at night", [r"rooftop photovoltaic panels connected to the grid", r"a pump circulating water through rooftop collectors", r"mirrors concentrating sunlight on a tower"],
          r"Passive designs use the building itself, with no pumps or electronics.",
          [r"Passive: no mechanical devices."],
          [r"PV panels generate electricity actively.",
           r"pumps make it an active system.",
           r"that is concentrated solar power."]),
        Q("6.12 Wind", r"Which is a disadvantage of wind energy?",
          r"Its output varies with the wind, so it needs storage or backup.", [r"It emits large amounts of CO$_2$ while operating.", r"It produces radioactive waste.", r"It requires burning biomass."],
          r"Intermittency is the main challenge; turbines can also harm birds and bats.",
          [r"Intermittent source."],
          [r"turbines emit no CO$_2$ while running.",
           r"wind power produces no radioactive waste.",
           r"no fuel is burned."]),
        Q("6.7 Corn ethanol", r"Why is corn ethanol not truly carbon-neutral?",
          r"Growing, fertilizing, harvesting and processing the corn use fossil fuels.", [r"Ethanol contains no carbon.", r"Corn plants release CO$_2$ but absorb none.", r"Ethanol is a fossil fuel."],
          r"The CO$_2$ absorbed by the corn is offset, but fuel for machinery, fertilizer manufacture and distillation adds emissions.",
          [r"Whole life-cycle emissions."],
          [r"ethanol is C$_2$H$_5$OH.",
           r"corn absorbs CO$_2$ during photosynthesis.",
           r"ethanol is made from recently grown plants."]),
        Q("6.6 Half-life", r"A radioactive waste sample decays to $\tfrac18$ of its original radioactivity in $90$ years. What is the half-life?",
          r"$30$ years", [r"$11$ years", r"$45$ years", r"$720$ years"],
          r"$\tfrac18 = \left(\tfrac12\right)^3$: three half-lives in $90$ years.",
          [r"Count the halvings."],
          [r"divides $90$ by $8$.",
           r"assumes two half-lives.",
           r"multiplies instead of dividing."], sort=True),
    ]),
]

UNIT = Unit(6, "energy-resources-consumption", "Energy Resources and Consumption", "10--15\\%", "6.1--6.13",
    abstract=r"""Unit 6 covers energy: renewable and nonrenewable resources, patterns of global consumption, fuel types, fossil fuels (combustion, electricity generation, fracking) and their distribution, nuclear power and half-life, biomass and biofuels, solar, hydroelectric, geothermal and wind energy, hydrogen fuel cells, and energy conservation. Energy calculations (kilowatt-hours, cost, emissions, payback) appear throughout. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5], qsections=QS,
    frq=FRQ("Analyze an environmental problem doing calculations", 10, r"""A high school that uses $450\,000$ kWh of electricity a year, all from a coal-fired power plant, is considering installing solar photovoltaic panels. Each panel is rated at $0.40$ kW, and the school's location receives the equivalent of $4.5$ hours of full sunlight per day on average. Each installed panel costs \$350, and the school pays \$0.12 per kWh for electricity. The coal plant emits $0.95$ kg of CO$_2$ per kWh.""", [
        Part("(a)", 1, r"\textbf{Describe} one environmental advantage of generating electricity with solar panels rather than coal.",
             r"Solar panels release no CO$_2$, sulfur dioxide, nitrogen oxides, particulates or mercury while generating electricity (and need no mining or burning of coal).",
             r"Saying solar is ``free'' or ``renewable'' without an environmental benefit."),
        Part("(b)", 2, r"\textbf{Calculate} the electricity one panel generates in a year. Show your work.",
             r"1 pt: setup: $0.40\ \mathrm{kW} \times 4.5\ \mathrm{h/day} \times 365\ \mathrm{days/yr}$. 1 pt: $657$ kWh per year (about $660$).",
             r"Leaving out the days per year."),
        Part("(c)", 2, r"\textbf{Calculate} the number of panels needed to supply all of the school's electricity. Show your work.",
             r"1 pt: setup: $450\,000 \div 657$ (consistent with (b)). 1 pt: about $685$ panels.",
             r"Multiplying instead of dividing."),
        Part("(d)", 2, r"\textbf{Calculate} the mass of CO$_2$ emissions, in metric tons, avoided each year if solar panels supply all of the school's electricity. Show your work.",
             r"1 pt: setup: $450\,000\ \mathrm{kWh} \times 0.95\ \mathrm{kg/kWh} = 427\,500$ kg. 1 pt: about $430$ metric tons.",
             r"Answering in kilograms when tons were asked, without converting."),
        Part("(e)", 2, r"\textbf{Calculate} the payback period, in years, for the installation. Show your work.",
             r"1 pt: setup: cost $= 685 \times 350 = 239\,750$ dollars; annual savings $= 450\,000 \times 0.12 = 54\,000$ dollars. 1 pt: $239\,750 \div 54\,000 \approx 4.4$ years (consistent with (c)).",
             r"Dividing savings by cost."),
        Part("(f)", 1, r"\textbf{Identify} one disadvantage of relying on solar panels for the school's electricity.",
             r"For example: no generation at night and less on cloudy days, so storage or a grid connection is needed; high upfront cost; mining and disposal of panel materials; the space required.",
             r"A disadvantage of coal instead of solar."),
    ], mins=23),
    frq_topic="solar panels for a school",
)
