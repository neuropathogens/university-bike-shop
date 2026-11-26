from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part

S1 = Sec("Generalists, specialists, and r- and K-selected species (3.1--3.2)", ["3.1", "3.2"], r"""
\textbf{Generalists} have broad niches: they eat many foods and tolerate a wide range of conditions (raccoons, cockroaches). \textbf{Specialists} have narrow niches (koalas eating eucalyptus, giant pandas eating bamboo); they do well in stable conditions but are more likely to go extinct when their habitat changes.

\begin{compare}{Trait}{$r$-selected species}{$K$-selected species}
Offspring & many, small, little parental care & few, large, much parental care \\
Maturity and lifespan & early; short-lived & late; long-lived \\
Population pattern & rapid growth; often overshoots and crashes & stays near carrying capacity \\
Examples & insects, mice, weeds, many fish & elephants, whales, humans, large trees \\
Response to disturbance & recover quickly; many are invasive & recover slowly; more vulnerable to extinction \\
\end{compare}
Many species fall between the extremes.
""", checks=[
    Q("3.2 K-selected", r"Which trait is typical of a $K$-selected species?",
      r"long life, with few offspring that receive much parental care", [r"many offspring with little parental care", r"early reproduction and a short lifespan", r"rapid population growth after a disturbance"],
      r"$K$-selected species invest heavily in each offspring and live near carrying capacity.",
      [r"Few, cared-for offspring; long life."],
      [r"is an $r$-selected trait.",
       r"is an $r$-selected trait.",
       r"is typical of $r$-selected species."]),
])

S2 = Sec("Survivorship curves (3.3)", ["3.3"], r"""
A survivorship curve plots the number of survivors of a group born at the same time against age (usually on a log scale).
\begin{compare}{Type}{Pattern}{Examples}
I & high survival through most of life, then steep losses in old age & humans, elephants ($K$-selected) \\
II & a constant chance of dying at every age (a straight line on a log scale) & many birds, squirrels \\
III & very high mortality among the young; the few that survive live a long time & most fish, insects, plants ($r$-selected) \\
\end{compare}
""", checks=[
    Q("3.3 Type III", r"An oyster releases millions of eggs, and nearly all the larvae die within weeks, but the few that settle may live for years. Which survivorship curve fits?",
      r"Type III", [r"Type I", r"Type II", r"none, because oysters do not have survivorship curves"],
      r"Very high early mortality, with long survival for the few survivors, is Type III.",
      [r"Type III: $r$-selected pattern."],
      [r"Type I has high survival when young.",
       r"Type II has a constant death rate at all ages.",
       r"every species has a survivorship pattern."]),
])

S3 = Sec("Carrying capacity and population growth (3.4--3.5)", ["3.4", "3.5"], r"""
\textbf{Carrying capacity} ($K$) is the largest population an environment can sustain indefinitely, set by limiting resources such as food, water, space and nesting sites. A population growing with unlimited resources grows exponentially (a J-shaped curve); as it approaches $K$, competition slows growth and it levels off (a logistic, S-shaped curve).

A population can \textbf{overshoot} $K$ if it grows quickly and resources respond slowly; it then damages its resource base and crashes (dies back), sometimes to well below the original $K$. Reindeer introduced to St.\ Matthew Island in 1944 grew to about $6000$, overgrazed the lichens, and fell to about $40$.

Density-dependent factors (competition, disease, predation) intensify as a population grows; density-independent factors (storms, fires, cold snaps) do not depend on density.
""", checks=[
    Q("3.4 Overshoot", r"A deer population grows rapidly after its predators are removed, exceeds the amount of food available, overgrazes its range, and then declines sharply. What has happened?",
      r"The population overshot its carrying capacity and then underwent dieback.", [r"The population reached carrying capacity and remained stable.", r"The carrying capacity increased because predators were removed.", r"The population showed Type I survivorship."],
      r"Exceeding $K$ degrades resources, which then cannot support the population.",
      [r"Overshoot and dieback."],
      [r"it did not remain stable.",
       r"removing predators raised the population, not the food supply.",
       r"survivorship curves describe mortality by age."]),
])

S4 = Sec("Age structure, fertility and human population dynamics (3.6--3.8)", ["3.6", "3.7", "3.8"], r"""
\textbf{Age-structure diagrams} show the population in each age group, males on one side and females on the other. A wide base (pyramid) shows rapid growth; nearly straight sides show a stable population; a base narrower than the middle shows decline.

\textbf{Total fertility rate} (TFR) is the average number of children a woman has in her lifetime. \textbf{Replacement-level fertility} is about $2.1$ in developed countries (a little above $2$ to make up for children who die before reproducing) and higher where child mortality is high. TFR falls with greater education and employment of women, access to family planning, lower infant mortality, urbanization and later marriage. Even after TFR falls, a young population keeps growing for decades (population momentum).

\begin{keyidea}[Human population arithmetic]
\vspace{-6pt}
\[ \text{growth rate (\%)} = \frac{\text{crude birth rate} - \text{crude death rate}}{10} \]
\[ \text{doubling time (years)} \approx \frac{70}{\text{growth rate (\%)}} \]
with crude rates per $1000$ people per year. With migration: change $=$ (births $+$ immigrants) $-$ (deaths $+$ emigrants).
\end{keyidea}
Malthus argued that population would outgrow food supply; so far, technology (the Green Revolution) has raised the human carrying capacity, at environmental cost.
""", checks=[
    Q("3.8 Doubling time", r"A country has a crude birth rate of $30$ and a crude death rate of $10$ per $1000$ people per year, with no migration. About how long will its population take to double?",
      r"$35$ years", [r"$3.5$ years", r"$70$ years", r"$20$ years"],
      r"Growth rate $= (30 - 10)/10 = 2\%$; doubling time $\approx 70/2 = 35$ years.",
      [r"Rule of 70."],
      [r"uses $20\%$ as the growth rate.",
       r"would need a $1\%$ growth rate.",
       r"is the difference in rates, not a time."], sort=True),
])

S5 = Sec("The demographic transition (3.9)", ["3.9"], r"""
\begin{compare}{Stage}{Birth and death rates}{Population}
1 Preindustrial & both high & stable, small \\
2 Transitional & death rate falls (better food, sanitation, medicine); birth rate stays high & grows rapidly \\
3 Industrial & birth rate falls (urbanization, education, family planning) & growth slows \\
4 Postindustrial & both low & stable or slowly declining \\
\end{compare}
Death rates fall before birth rates because improvements in food, clean water and health care save lives quickly, while the social and economic changes that lower family size take a generation or more.
""", checks=[
    Q("3.9 Stage 2", r"In which stage of the demographic transition does a population grow most rapidly?",
      r"Stage 2, when death rates have fallen but birth rates remain high", [r"Stage 1, when birth and death rates are both high", r"Stage 4, when birth and death rates are both low", r"Stage 3, when birth rates are falling"],
      r"The gap between births and deaths is widest in Stage 2.",
      [r"Growth rate $\approx$ birth rate $-$ death rate."],
      [r"high deaths offset high births.",
       r"low births and deaths give little growth.",
       r"growth is slowing as births fall."]),
])

QS = [
    Set("Life histories (3.1--3.3)", [
        Q("3.1 Specialists", r"Why are specialist species generally more vulnerable to extinction than generalists?",
          r"They depend on a narrow range of foods or habitats, so a change to that resource can eliminate them.", [r"They reproduce faster than generalists.", r"They are always larger than generalists.", r"They live in more habitats than generalists."],
          r"A narrow niche leaves no alternatives when conditions change.",
          [r"Narrow niche, high risk."],
          [r"reproductive rate is a separate trait.",
           r"size varies; the niche is what matters.",
           r"that describes generalists."]),
        Q("3.2 Invasive species", r"Many invasive species share which set of traits?",
          r"$r$-selected traits: fast reproduction, many offspring and generalist diets", [r"$K$-selected traits: slow reproduction and few offspring", r"specialist diets and narrow tolerance ranges", r"long generation times and much parental care"],
          r"Rapid reproduction and broad tolerance let them spread quickly into new areas.",
          [r"Invasives are usually $r$-selected generalists."],
          [r"$K$-selected species spread slowly.",
           r"specialists rarely spread widely.",
           r"these are $K$-selected traits."]),
        Q("3.3 Type I", r"Which organism most likely shows a Type I survivorship curve?",
          r"an elephant", [r"a frog", r"a dandelion", r"a salmon"],
          r"Elephants have few, well-protected young, most of whom survive to old age.",
          [r"Type I: $K$-selected, high parental care."],
          [r"frogs lay many eggs; most tadpoles die (Type III).",
           r"most dandelion seeds never establish (Type III).",
           r"salmon release many eggs; few survive (Type III)."]),
    ]),
    Set("Two countries (3.6--3.9)", [
        Q("3.8 Growth rate", r"What is the annual rate of natural increase of country A?",
          r"$3.0\%$", [r"$30\%$", r"$4.6\%$", r"$0.30\%$"],
          r"$(38 - 8)/10 = 3.0\%$ per year.",
          [r"Rates per $1000$; divide the difference by $10$ for a percentage."],
          [r"forgets to divide by $10$.",
           r"adds the birth and death rates.",
           r"divides by $100$."], sort=True),
        Q("3.8 Doubling", r"About how long will country A take to double its population if this rate continues?",
          r"$23$ years", [r"$70$ years", r"$210$ years", r"$2.3$ years"],
          r"$70/3.0 \approx 23$ years.",
          [r"Rule of 70."],
          [r"is the rule's numerator, not the doubling time.",
           r"multiplies $70$ by $3.0$.",
           r"uses a growth rate of $30\%$."], sort=True),
        Q("3.6 Age structure", r"Which best describes the age-structure diagram of country B?",
          r"a base narrower than the middle, indicating a declining population", [r"a wide base, indicating rapid growth", r"a perfect pyramid", r"a diagram with no people under $15$"],
          r"Only $13\%$ are under $15$ and deaths exceed births: few young people relative to adults.",
          [r"Narrow base: few children."],
          [r"describes country A.",
           r"a pyramid has a wide base.",
           r"$13\%$ are under $15$."]),
        Q("3.9 Stages", r"Which stages of the demographic transition best match countries A and B?",
          r"A: stage 2; B: stage 4", [r"A: stage 4; B: stage 2", r"A: stage 1; B: stage 3", r"both are in stage 3"],
          r"A has high births and low deaths (stage 2); B has low births and deaths, with deaths slightly higher (stage 4).",
          [r"Compare the two rates."],
          [r"reverses them.",
           r"stage 1 has high death rates; A's is low.",
           r"their birth rates are far apart."]),
        Q("3.7 Fertility", r"Which change would most likely reduce country A's total fertility rate over the next generation?",
          r"increasing education and job opportunities for women", [r"increasing infant mortality", r"lowering the age of marriage", r"reducing access to family planning"],
          r"Educated women tend to marry later, have more economic options and use family planning, and so have fewer children.",
          [r"Education of women is one of the strongest predictors of lower TFR."],
          [r"higher infant mortality tends to raise birth rates.",
           r"earlier marriage lengthens the reproductive span.",
           r"less family planning raises TFR."]),
    ], stim=r"""The table gives demographic data for two countries.

\medskip
\begin{tabular}{@{}lcc@{}}\toprule
Measure & Country A & Country B \\ \midrule
Crude birth rate (per 1000) & 38 & 9 \\
Crude death rate (per 1000) & 8 & 11 \\
Total fertility rate & 5.0 & 1.4 \\
Population under age 15 & 45\% & 13\% \\ \bottomrule
\end{tabular}""", stim_title="Questions 4--8"),
    Set("Carrying capacity and human population (3.4--3.8)", [
        Q("3.7 Replacement fertility", r"Why is replacement-level fertility a little more than $2.0$ children per woman?",
          r"Some children die before reaching reproductive age.", [r"Every couple needs to replace more than two people.", r"Men have more children than women.", r"Immigration always adds people."],
          r"Two children replace the parents; a little extra covers deaths before adulthood.",
          [r"About $2.1$ in developed countries."],
          [r"two people need two replacements.",
           r"every child has one mother and one father.",
           r"replacement fertility ignores migration."]),
        Q("3.6 Momentum", r"A country's total fertility rate falls to replacement level, yet its population keeps growing for several decades. Why?",
          r"A large share of its people are young and have yet to have their children.", [r"Its death rate has risen.", r"Its total fertility rate is actually zero.", r"Replacement-level fertility always causes growth."],
          r"Population momentum: many future parents are already born.",
          [r"A wide-based age structure keeps growing."],
          [r"a rising death rate would slow growth.",
           r"replacement level is about $2.1$, not zero.",
           r"once the age structure evens out, growth stops."]),
        Q("3.5 Logistic growth", r"A population's growth slows as it approaches the carrying capacity of its environment. What causes the slowing?",
          r"Limiting resources become scarcer, increasing competition.", [r"Birth rates always rise.", r"The environment's carrying capacity keeps increasing.", r"Density-independent factors stop acting."],
          r"As the population nears $K$, each individual gets fewer resources, lowering births and raising deaths.",
          [r"Density-dependent limits."],
          [r"births fall as resources run short.",
           r"$K$ is set by the environment.",
           r"density-independent factors are unrelated to approaching $K$."]),
        Q("3.8 Migration", r"A town of $10\,000$ people has $150$ births, $80$ deaths, $40$ immigrants and $60$ emigrants in a year. What is its population at the end of the year?",
          r"$10\,050$", [r"$10\,070$", r"$10\,110$", r"$9\,950$"],
          r"Change $= (150 + 40) - (80 + 60) = 50$.",
          [r"Births and immigrants add; deaths and emigrants subtract."],
          [r"leaves out migration.",
           r"leaves out emigration.",
           r"has the sign reversed: it subtracts the gains from the losses."], sort=True),
        Q("3.8 Malthus", r"Thomas Malthus predicted that human population growth would outrun the food supply. Why has this not happened on a global scale so far?",
          r"Technology such as the Green Revolution greatly increased food production.", [r"Human population has stopped growing.", r"Humans need less food than Malthus assumed.", r"Food production grows exponentially without any inputs."],
          r"Fertilizers, irrigation and high-yield crops raised the human carrying capacity, though with environmental costs.",
          [r"Technology raised $K$."],
          [r"population is still growing.",
           r"food needs per person did not fall.",
           r"higher yields depend on energy, water and fertilizer."]),
    ]),
]

UNIT = Unit(3, "populations", "Populations", "10--15\\%", "3.1--3.9",
    abstract=r"""Unit 3 covers populations: generalist and specialist species, $r$- and $K$-selected life histories, survivorship curves, carrying capacity, overshoot and logistic growth, age-structure diagrams, total fertility rate, the arithmetic of human population growth (growth rates and the rule of 70), and the demographic transition. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5], qsections=QS,
    frq=FRQ("Analyze an environmental problem doing calculations", 10, r"""A country has a population of $50$ million. Its crude birth rate is $25$ per $1000$ per year, its crude death rate is $7$ per $1000$ per year, and net migration adds $50\,000$ people a year. On average, each person in the country uses $1200$ m$^3$ of water per year.""", [
        Part("(a)", 1, r"\textbf{Describe} one reason that, during the demographic transition, death rates fall before birth rates.",
             r"Improvements in food supply, clean water, sanitation and medicine lower death rates quickly, while the social and economic changes that lead people to have fewer children (education, urbanization, family planning) take longer.",
             r"Saying birth rates rise."),
        Part("(b)", 2, r"\textbf{Calculate} the country's rate of natural increase, as a percentage. Show your work.",
             r"1 pt: setup: $(25 - 7)/10$. 1 pt: $1.8\%$ per year.",
             r"Forgetting to convert from per-$1000$ to percent."),
        Part("(c)", 2, r"\textbf{Calculate} the doubling time of the population at this rate of natural increase. Show your work.",
             r"1 pt: setup: $70/1.8$. 1 pt: about $39$ years (accept answers consistent with (b)).",
             r"Dividing $1.8$ by $70$."),
        Part("(d)", 2, r"\textbf{Calculate} the population at the end of one year, including migration. Show your work.",
             r"1 pt: births $= 50\,000\,000 \times 0.025 = 1\,250\,000$; deaths $= 50\,000\,000 \times 0.007 = 350\,000$; change $= 1\,250\,000 - 350\,000 + 50\,000 = 950\,000$. 1 pt: $50\,950\,000$ (about $51.0$ million).",
             r"Leaving out migration, or adding the death rate."),
        Part("(e)", 2, r"\textbf{Calculate} the additional water, in cubic meters per year, needed to supply the people added in that year. Show your work.",
             r"1 pt: setup: $950\,000 \times 1200$ (consistent with (d)). 1 pt: $1.14 \times 10^9$ m$^3$ per year.",
             r"Multiplying the whole population by $1200$."),
        Part("(f)", 1, r"\textbf{Propose} one realistic policy the government could adopt to slow the country's population growth.",
             r"For example: expand education and job opportunities for girls and women; improve access to family planning; provide pensions so families rely less on children for old-age support; reduce infant mortality.",
             r"Coercive or unrealistic measures (``ban children'')."),
    ], mins=23),
    frq_topic="population growth and water demand",
)
