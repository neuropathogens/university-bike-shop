from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph, Series

MODEL = Graph(r"Generation", r"Frequency of resistance allele", x=(0, 20, 5), y=(0, 1.0, 0.2),
              series=[Series("sprayed", [(0, 0.05), (5, 0.18), (10, 0.47), (15, 0.78), (20, 0.92)]),
                      Series("not sprayed", [(0, 0.05), (5, 0.05), (10, 0.04), (15, 0.05), (20, 0.04)])],
              legend_pos="nw", caption=r"Model graph: both populations on one set of axes, with a key.")

S1 = Sec("Natural selection (7.1--7.2)", ["7.1", "7.2"], r"""
\textbf{Natural selection} is the major mechanism of evolution. It needs:
\begin{itemize}
\item variation among individuals in a population;
\item heritable variation (passed on in genes);
\item more offspring than can survive (competition for limited resources);
\item differential survival and reproduction: individuals whose heritable traits suit the environment leave more offspring.
\end{itemize}
Over generations, the alleles behind favorable traits become more common. \textbf{Fitness} is reproductive success: the number of offspring that survive to reproduce. Selection acts on phenotypes, but it is allele frequencies in the population that change; individuals do not evolve. What counts as favorable depends on the environment, which can change.

\begin{compare}{Type}{Which phenotypes are favored}{Example}
Directional & one extreme & larger beaks after a drought leaves only hard seeds \\
Stabilizing & intermediate & human birth weight \\
Disruptive & both extremes & seedcrackers with small or large beaks, few intermediate seeds \\
\end{compare}
""", checks=[
    Q("7.2 Antibiotic resistance", r"After a course of antibiotics, a bacterial infection returns and is now resistant to the antibiotic. Which explanation is consistent with natural selection?",
      r"A few bacteria already carried resistance alleles; the antibiotic killed the others, and the survivors reproduced.", [r"The antibiotic caused the bacteria to mutate so that they became resistant.", r"Individual bacteria learned to resist the antibiotic.", r"The bacteria became resistant because they needed to survive."],
      r"Selection acts on existing heritable variation; the antibiotic changed which variants survived, not which variants arose.",
      [r"Variation first, then selection."],
      [r"the antibiotic selects; it does not direct mutations.",
       r"resistance is inherited, not learned.",
       r"need does not create alleles."]),
])

S2 = Sec("Artificial selection (7.3)", ["7.3"], r"""
In \textbf{artificial selection}, humans choose which individuals breed, so traits humans value increase. Dog breeds, and broccoli, cabbage, kale and cauliflower from wild mustard, show how much variation selection can produce in relatively few generations, which helped persuade Darwin that natural selection could produce new forms over longer periods.
""", checks=[
    Q("7.3 Artificial selection", r"Broccoli, cabbage, kale and cauliflower were all bred from wild mustard. What does this show?",
      r"Selecting for different traits in one species can produce very different forms.", [r"Each vegetable is a separate species that evolved by natural selection.", r"Wild mustard has no genetic variation.", r"The plants changed because the farmers' needs changed their DNA."],
      r"Farmers bred plants with enlarged buds, leaves or stems; the heritable variation was already in wild mustard.",
      [r"Humans as the selective agent."],
      [r"the forms were produced by human choice, and they can still interbreed.",
       r"the variation they selected must have been present.",
       r"selection changes allele frequencies; it does not rewrite DNA on demand."]),
])

S3 = Sec("Population genetics and Hardy--Weinberg equilibrium (7.4--7.5)", ["7.4", "7.5"], r"""
Evolution is a change in the allele frequencies of a population. Besides selection, frequencies change by:
\begin{terms}
Genetic drift & random change, strongest in small populations; a \textbf{bottleneck} (a disaster kills most at random) or the \textbf{founder effect} (a few individuals start a new population) can shift frequencies sharply \\
Gene flow & movement of alleles between populations \\
Mutation & creates new alleles (slowly) \\
Nonrandom mating & changes genotype frequencies \\
\end{terms}

\textbf{Hardy--Weinberg equilibrium.} With two alleles at frequencies $p$ and $q$, a population that is large, mating randomly, with no migration, mutation or selection, keeps constant allele frequencies and genotype frequencies
\[ p + q = 1, \qquad p^2 + 2pq + q^2 = 1 . \]
Start from the homozygous recessive phenotype, whose frequency is $q^2$. If $9\%$ show a recessive trait, $q = 0.3$, $p = 0.7$, and $2pq = 0.42$ are carriers. A population whose observed frequencies differ from these predictions is evolving.
""", checks=[
    Q("7.5 Carriers", r"In a population in Hardy--Weinberg equilibrium, $9\%$ of individuals show a recessive phenotype. What fraction are heterozygous?",
      r"$0.42$", [r"$0.09$", r"$0.30$", r"$0.49$"],
      r"$q^2 = 0.09$, so $q = 0.3$ and $p = 0.7$; $2pq = 2(0.7)(0.3) = 0.42$.",
      [r"Take the square root of the recessive phenotype frequency."],
      [r"is $q^2$, the homozygous recessive frequency.",
       r"is $q$, the allele frequency.",
       r"is $p^2$, the homozygous dominant frequency."], sort=True),
])

S4 = Sec("Evidence of evolution and common ancestry (7.6--7.7)", ["7.6", "7.7"], r"""
\begin{terms}
Fossils & show change over time, dated by rock layers and radiometric dating \\
Homologous structures & similar structure, different functions, inherited from a common ancestor (human arm, whale flipper, bat wing) \\
Vestigial structures & reduced remnants of ancestral features (the human tailbone, whale pelvic bones) \\
Analogous structures & similar function from separate evolution (bird and insect wings), not evidence of close relationship \\
Molecular evidence & DNA and protein sequences: the more differences, the longer since two species shared an ancestor \\
Biogeography & the distribution of species follows their history (island species resemble those on the nearest mainland) \\
\end{terms}
\textbf{Common ancestry} explains features shared by all life (DNA, the genetic code, ribosomes, ATP) and by all eukaryotes (membrane-bound organelles, linear chromosomes, introns).
""", checks=[
    Q("7.6 Homology", r"The forelimbs of humans, whales and bats have the same set of bones but very different uses. What do they show?",
      r"homologous structures inherited from a common ancestor", [r"analogous structures that evolved independently", r"vestigial structures with no function", r"the effect of the environment on a single genotype"],
      r"Same underlying structure, modified for different functions: the signature of descent from a common ancestor.",
      [r"Homologous: shared ancestry. Analogous: shared function."],
      [r"analogous structures share function, not underlying structure.",
       r"all three limbs are fully functional.",
       r"these are different species with different genotypes."]),
])

S5 = Sec("Continuing evolution and variation in populations (7.8, 7.11)", ["7.8", "7.11"], r"""
Evolution is still happening: bacteria evolve antibiotic resistance, insects evolve pesticide resistance, viruses (influenza, SARS-CoV-2) evolve new variants. Genetic variation makes a population more likely to include individuals that survive a changed environment. Populations with little variation (cheetahs, a single potato variety in nineteenth-century Ireland) can be devastated by one new disease or change.
""", checks=[
    Q("7.11 Variation and survival", r"Why are populations with low genetic diversity more at risk from a new disease?",
      r"They are less likely to include individuals with alleles that resist the disease.", [r"They have higher mutation rates.", r"They reproduce faster.", r"They are always smaller in number."],
      r"With little variation, a disease that kills one individual is likely to kill nearly all.",
      [r"Variation is the raw material selection needs."],
      [r"low diversity does not raise mutation rates.",
       r"reproduction rate is unrelated to diversity.",
       r"a large population can still have low diversity."]),
])

S6 = Sec("Phylogeny, speciation and the origins of life (7.9--7.10, 7.12)", ["7.9", "7.10", "7.12"], r"""
\textbf{Phylogenetic trees and cladograms} show hypothesized relationships. Each branch point (node) is a common ancestor; groups are defined by \textbf{shared derived characters}; an \textbf{outgroup} lacks them and roots the tree. Trees built from DNA sequences are often more reliable than those built from anatomy, and all are revised as new data appear.

\textbf{Speciation.} In the biological species concept, a species is a group whose members can interbreed and produce fertile offspring. Reproductive isolation keeps species apart: \emph{prezygotic} barriers (different habitats, mating seasons or courtship, incompatible gametes) and \emph{postzygotic} barriers (hybrids that die or are sterile, such as mules). \emph{Allopatric} speciation follows geographic separation; \emph{sympatric} speciation happens without it, for example by polyploidy in plants in a single generation. Change may be gradual or come in rapid bursts (punctuated equilibrium); adaptive radiation follows the opening of new niches.

\textbf{Origins of life.} Earth formed about $4.6$ billion years ago; the earliest fossil cells are about $3.5$ billion years old. Experiments such as Miller and Urey's showed that organic molecules can form from simple inorganic ones under early-Earth conditions; the RNA world hypothesis proposes that RNA, which can both store information and catalyze reactions, came before DNA and proteins.
""", checks=[
    Q("7.10 Polyploidy", r"A plant cell undergoes a division error that doubles its chromosome number, producing a tetraploid plant that cannot produce fertile offspring with the diploid parents. What kind of speciation is this?",
      r"sympatric speciation", [r"allopatric speciation", r"artificial selection", r"gene flow"],
      r"Reproductive isolation arose in one generation, without any geographic separation.",
      [r"Polyploidy is a common route to sympatric speciation in plants."],
      [r"allopatric speciation requires a geographic barrier.",
       r"no human selection was involved.",
       r"gene flow joins populations; this isolates them."]),
])

QS = [
    Set("Selection (7.1--7.3, 7.8)", [
        Q("7.2 Disruptive selection", r"In a population of birds, individuals with small beaks feed on small seeds and those with large beaks on large seeds, but few medium-sized seeds are available. Which type of selection is acting on beak size?",
          r"disruptive", [r"stabilizing", r"directional", r"artificial"],
          r"Both extremes are favored over the intermediate, which can split the distribution into two peaks.",
          [r"Disruptive: both extremes win."],
          [r"stabilizing selection favors the intermediate.",
           r"directional selection favors one extreme.",
           r"no human is choosing the breeders."]),
        Q("7.2 Who evolves", r"Which statement about evolution by natural selection is correct?",
          r"Populations evolve; individuals do not.", [r"Individuals evolve during their lifetimes to suit their environment.", r"Natural selection creates new alleles when they are needed.", r"Every trait of an organism is an adaptation."],
          r"Selection changes which alleles are passed on, so a population's allele frequencies shift over generations; an individual's genes stay the same.",
          [r"Evolution: change in allele frequencies over generations."],
          [r"an individual's genotype does not change in response to the environment.",
           r"mutation produces alleles randomly; selection only sorts them.",
           r"some traits are neutral or result from drift."]),
        Q("7.8 Pesticide resistance", r"A pesticide kills $99\%$ of the insects in a field the first year it is used but only $40\%$ five years later. What is the best explanation?",
          r"Insects with heritable resistance survived and reproduced, so resistance alleles became more common.", [r"The pesticide lost its strength over five years.", r"The insects that survived developed resistance by exposure and passed it on.", r"The pesticide caused mutations for resistance in every insect."],
          r"Each application selected for the resistant minority, increasing the resistance allele's frequency.",
          [r"Rapid evolution under strong selection."],
          [r"the change is in the insects.",
           r"acquired tolerance is not inherited.",
           r"mutations arise randomly, not in response to need."]),
        Q("7.1 Fitness", r"Which individual has the highest fitness in the evolutionary sense?",
          r"a small male that leaves $12$ offspring that survive to reproduce", [r"a large male that lives $15$ years but has $2$ surviving offspring", r"the fastest runner in the population, which has no offspring", r"a strong male that wins many fights but leaves $5$ surviving offspring"],
          r"Fitness is reproductive success: the number of offspring that survive to reproduce.",
          [r"Fitness means offspring, not strength or lifespan."],
          [r"long life does not count without offspring.",
           r"speed without offspring passes on nothing.",
           r"fewer surviving offspring means lower fitness."]),
    ]),
    Set("Hardy--Weinberg in a snail population (7.4--7.5)", [
        Q("7.5 Recessive allele", r"What is the frequency of the yellow allele, $b$?",
          r"$0.40$", [r"$0.16$", r"$0.60$", r"$0.84$"],
          r"Yellow snails are $bb$: $q^2 = 160/1000 = 0.16$, so $q = \sqrt{0.16} = 0.40$.",
          [r"Start from the recessive phenotype."],
          [r"is $q^2$, the yellow phenotype frequency.",
           r"is $p$.",
           r"is the brown phenotype frequency."], sort=True),
        Q("7.5 Dominant allele", r"What is the frequency of the brown allele, $B$?",
          r"$0.60$", [r"$0.84$", r"$0.36$", r"$0.40$"],
          r"$p = 1 - q = 1 - 0.40 = 0.60$.",
          [r"$p + q = 1$."],
          [r"is the brown phenotype frequency, which includes heterozygotes.",
           r"is $p^2$.",
           r"is $q$."], sort=True),
        Q("7.5 Heterozygotes", r"About how many of the snails are heterozygous ($Bb$)?",
          r"$480$", [r"$240$", r"$360$", r"$840$"],
          r"$2pq = 2(0.60)(0.40) = 0.48$; $0.48 \times 1000 = 480$.",
          [r"Then $p^2 = 0.36$: $360$ are $BB$."],
          [r"is $pq$, missing the factor 2.",
           r"is the number of $BB$ snails.",
           r"is all the brown snails."], sort=True),
        Q("7.2 Predation", r"Birds begin to eat yellow snails more often than brown ones because yellow snails are easier to see. What will happen to $q$ over the next generations?",
          r"It will decrease.", [r"It will increase.", r"It will stay at $0.40$.", r"It will become exactly zero in one generation."],
          r"Selection against the yellow phenotype removes $b$ alleles; heterozygotes hide some, so the decline is gradual.",
          [r"Selection violates a Hardy--Weinberg condition."],
          [r"yellow snails, which carry only $b$ alleles, are being removed.",
           r"equilibrium requires no selection.",
           r"$b$ alleles survive in brown heterozygotes."]),
        Q("7.4 A storm", r"A storm kills $90\%$ of the snails at random, regardless of color. Which mechanism could most change the allele frequencies in the survivors?",
          r"genetic drift (a bottleneck)", [r"natural selection", r"gene flow", r"mutation"],
          r"A random sample of $100$ survivors may, by chance, have allele frequencies quite different from the original population.",
          [r"Random loss in a small sample: drift."],
          [r"the deaths were not related to phenotype.",
           r"no snails moved in or out.",
           r"a storm does not create alleles."]),
    ], stim=r"In a population of $1000$ snails, shell color is controlled by one gene: brown ($B$) is dominant to yellow ($b$). There are $160$ yellow snails. Assume the population is in Hardy--Weinberg equilibrium unless a question says otherwise.",
        stim_title="Questions 5--9"),
    Set("Reading a character table (7.9)", [
        Q("7.9 Outgroup", r"Which organism in the table is the outgroup for the other four?",
          r"lamprey", [r"shark", r"frog", r"mouse"],
          r"The lamprey has only vertebrae, the character shared by all five; it lacks every derived character the others share.",
          [r"The outgroup has the fewest shared derived characters."],
          [r"the shark shares jaws with the frog, lizard and mouse.",
           r"the frog shares jaws and lungs with the lizard and mouse.",
           r"the mouse has the most derived characters."]),
        Q("7.9 Closest relatives", r"Which two organisms share the most recent common ancestor?",
          r"lizard and mouse", [r"frog and lizard", r"shark and frog", r"lamprey and shark"],
          r"The lizard and mouse share the most derived characters, including the amniotic egg, which neither the frog nor the shark has.",
          [r"More shared derived characters, more recent common ancestor."],
          [r"the frog lacks the amniotic egg.",
           r"the shark lacks lungs.",
           r"the lamprey lacks jaws."]),
    ], stim=r"""The table lists which of five characters (vertebrae, jaws, lungs, amniotic egg, hair) each of five vertebrates has.

\medskip
\begin{tabular}{@{}ll@{}}\toprule
Organism & Characters present \\ \midrule
Lamprey & vertebrae \\
Shark & vertebrae, jaws \\
Frog & vertebrae, jaws, lungs \\
Lizard & vertebrae, jaws, lungs, amniotic egg \\
Mouse & vertebrae, jaws, lungs, amniotic egg, hair \\ \bottomrule
\end{tabular}""", stim_title="Questions 10--11"),
    Set("Evidence and speciation (7.6--7.12)", [
        Q("7.6 Molecular evidence", r"The protein cytochrome c differs between humans and chimpanzees by $0$ amino acids, between humans and dogs by $11$, and between humans and yeast by $44$. What does this suggest?",
          r"Humans share a more recent common ancestor with chimpanzees than with dogs, and with dogs than with yeast.", [r"Yeast evolved from dogs.", r"Cytochrome c evolves faster in humans than in other species.", r"Chimpanzees are human ancestors."],
          r"Differences accumulate over time since two lineages separated; fewer differences mean a more recent split.",
          [r"Molecular clock reasoning."],
          [r"no living species evolved from another living species.",
           r"the comparison is between pairs; it says nothing about rates in one species.",
           r"humans and chimpanzees share an ancestor; neither is the other's ancestor."]),
        Q("7.10 Reproductive barrier", r"Two populations of frogs live in the same pond, but one breeds in early spring and the other in late spring. What type of barrier is this?",
          r"a prezygotic barrier (temporal isolation)", [r"a postzygotic barrier", r"geographic isolation", r"hybrid sterility"],
          r"Breeding at different times prevents mating, so no zygote forms.",
          [r"Before the zygote: prezygotic."],
          [r"postzygotic barriers act after fertilization.",
           r"the frogs share a pond.",
           r"hybrid sterility is postzygotic."]),
        Q("7.10 Species concept", r"Horses and donkeys can mate and produce mules, which are sterile. Under the biological species concept, horses and donkeys are",
          r"separate species, because their offspring are not fertile", [r"one species, because they can mate", r"one species, because they look alike", r"separate species only if they live in different places"],
          r"A species is a group whose members interbreed and produce fertile offspring; mule sterility is a postzygotic barrier.",
          [r"Fertile offspring is the test."],
          [r"mating alone is not enough.",
           r"the concept is about reproduction, not appearance.",
           r"location is not part of the definition."]),
        Q("7.12 Miller and Urey", r"What did the Miller--Urey experiment show?",
          r"Organic molecules such as amino acids can form from simple inorganic molecules under conditions thought to resemble early Earth.", [r"Life arose from nonliving matter in a few weeks.", r"DNA was the first genetic material.", r"Early Earth's atmosphere was rich in oxygen."],
          r"Sparks through a mixture of simple gases and water produced amino acids, supporting a chemical origin of life's building blocks.",
          [r"Building blocks, not living cells."],
          [r"no living cells formed.",
           r"the experiment did not address genetic material; the RNA world hypothesis proposes RNA first.",
           r"early Earth's atmosphere had little free oxygen."]),
    ]),
]

UNIT = Unit(7, "natural-selection", "Natural Selection", "13--20\\%", "7.1--7.12",
    abstract=r"""Unit 7 is the largest unit on the exam. It covers natural and artificial selection, fitness and the patterns of selection, population genetics (drift, gene flow, mutation) and Hardy--Weinberg equilibrium, the evidence for evolution and common ancestry, continuing evolution and the value of variation, phylogenetic trees, speciation and reproductive isolation, and the origins of life. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6], qsections=QS,
    frq=FRQ("Interpreting and Evaluating Experimental Results with Graphing", 9, r"""Researchers tracked the frequency of an allele that makes mosquitoes resistant to an insecticide in two large populations of the same species. Population 1 lived in an area sprayed with the insecticide every season; population 2 lived in a similar area that was never sprayed. In the absence of insecticide, resistant mosquitoes live slightly shorter lives than susceptible ones.

\medskip
\begin{tabular}{@{}ccc@{}}\toprule
Generation & Population 1 (sprayed) & Population 2 (not sprayed) \\ \midrule
0 & 0.05 & 0.05 \\
5 & 0.18 & 0.05 \\
10 & 0.47 & 0.04 \\
15 & 0.78 & 0.05 \\
20 & 0.92 & 0.04 \\ \bottomrule
\end{tabular}""", [
        Part("A", 1, r"\textbf{Describe} how natural selection explains the change in population 1.",
             r"In the sprayed area, mosquitoes carrying the resistance allele survive and reproduce more than susceptible mosquitoes, so the allele is passed on more often and its frequency rises each generation.",
             r"Saying the insecticide causes mosquitoes to become resistant."),
        Part("B", 4, r"\textbf{Construct} an appropriate graph that shows the frequency of the resistance allele over time in both populations.",
             r"1 pt: axes labeled (generation on the $x$-axis; allele frequency on the $y$-axis). 1 pt: appropriate scales (frequency from $0$ to $1$, generations evenly spaced). 1 pt: all points for both populations plotted correctly. 1 pt: the two populations distinguished with a key or labels (a line graph, since both variables are numeric).",
             r"A bar graph for each generation; no key.", fig=MODEL),
        Part("C", 2, r"(i) Assuming Hardy--Weinberg proportions, \textbf{calculate} the expected frequency of heterozygotes in population 1 at generation $10$. (ii) \textbf{Explain} why the allele frequency in population 2 stayed about the same.",
             r"1 pt: $2pq = 2(0.47)(0.53) \approx 0.50$. 1 pt: without insecticide there is no selective advantage to resistance (and a slight disadvantage), and in a large population drift is small, so the frequency stays low.",
             r"Using $p^2$; saying population 2 did not evolve because it ``did not need to.''"),
        Part("D", 2, r"Spraying in population 1's area stops after generation $20$. \textbf{Predict} how the frequency of the resistance allele will change over the following generations, and \textbf{justify} your prediction.",
             r"1 pt: it will slowly decrease. 1 pt: without the insecticide, resistant mosquitoes have lower fitness (shorter lives, so fewer offspring) than susceptible ones, so selection now favors the susceptible allele.",
             r"Predicting no change because ``the allele is already common.''"),
    ], mins=25),
    frq_topic="the evolution of insecticide resistance",
)
