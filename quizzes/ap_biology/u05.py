from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part

S1 = Sec("Meiosis (5.1)", ["5.1"], r"""
Meiosis turns one diploid cell ($2n$) into four haploid cells ($n$), the gametes or spores of sexual life cycles. DNA is replicated once, then the cell divides twice.

\begin{compare}{Division}{What separates}{Result}
Meiosis I & homologous chromosomes (one from each parent) pair up, then separate in anaphase I & two haploid cells, each chromosome still made of two sister chromatids \\
Meiosis II & sister chromatids separate, as in mitosis & four haploid cells \\
\end{compare}

\begin{compare}{Feature}{Mitosis}{Meiosis}
Divisions & one & two \\
Daughter cells & two, diploid, genetically identical & four, haploid, genetically different \\
Homologs pair & no & yes (prophase I), with crossing over \\
Role & growth, repair, asexual reproduction & sexual reproduction \\
\end{compare}
""", checks=[
    Q("5.1 Chromosome number", r"An organism has a diploid number $2n = 8$. How many chromosomes are in each cell at the end of meiosis I, and in each gamete?",
      r"$4$ and $4$", [r"$8$ and $4$", r"$4$ and $2$", r"$8$ and $8$"],
      r"Meiosis I separates homologs, halving the number to $4$ (each still with two chromatids); meiosis II separates chromatids, leaving $4$ chromosomes per gamete.",
      [r"The reduction happens in meiosis I."],
      [r"the number is already halved by the end of meiosis I.",
       r"meiosis II separates chromatids, not chromosomes, so the count stays $4$.",
       r"gametes are haploid."]),
])

S2 = Sec("Meiosis and genetic diversity (5.2)", ["5.2"], r"""
Three processes make each gamete, and each offspring, genetically unique:
\begin{terms}
Crossing over & in prophase I, non-sister chromatids of homologous chromosomes exchange segments, making new combinations of alleles on one chromosome \\
Independent assortment & in metaphase I each homologous pair lines up independently, so a cell with $n$ pairs can make $2^n$ combinations of chromosomes ($2^{23} \approx 8$ million in humans) \\
Random fertilization & any sperm can fertilize any egg \\
\end{terms}

\textbf{Errors.} Nondisjunction, the failure of homologs (meiosis I) or sister chromatids (meiosis II) to separate, gives gametes with an extra or missing chromosome; fertilization then produces aneuploidy, such as trisomy 21 (Down syndrome).
""", checks=[
    Q("5.2 Independent assortment", r"Ignoring crossing over, how many different combinations of maternal and paternal chromosomes can a human ($n = 23$) produce in its gametes?",
      r"$2^{23}$, about $8$ million", [r"$23$", r"$46$", r"$23^2 = 529$"],
      r"Each of the $23$ pairs orients independently, giving $2$ choices per pair: $2^{23} = 8\,388\,608$.",
      [r"Two orientations per pair, multiplied over all pairs."],
      [r"counts the pairs, not the combinations.",
       r"counts the chromosomes in a diploid cell.",
       r"squares the number of pairs instead of raising 2 to that power."]),
])

S3 = Sec("Mendelian genetics (5.3)", ["5.3"], r"""
\begin{terms}
Law of segregation & each individual has two alleles of a gene, which separate into different gametes \\
Law of independent assortment & alleles of genes on different chromosomes (or far apart on one) sort into gametes independently \\
Monohybrid cross & $Aa \times Aa$ gives $1\ AA : 2\ Aa : 1\ aa$ genotypes and $3:1$ phenotypes \\
Dihybrid cross & $AaBb \times AaBb$ gives $9:3:3:1$ phenotypes \\
Testcross & cross with a homozygous recessive to reveal an unknown genotype \\
Probability & multiply for ``and'' (independent events), add for ``or'' (mutually exclusive events) \\
\end{terms}

\textbf{Pedigrees.} An autosomal recessive trait can appear in children of unaffected (carrier) parents and often skips generations; an autosomal dominant trait appears in every generation, and every affected child has an affected parent.
""", checks=[
    Q("5.3 Dihybrid probability", r"Two parents are both $AaBb$, and the genes assort independently. What is the probability that a child is $aabb$?",
      r"$\tfrac{1}{16}$", [r"$\tfrac14$", r"$\tfrac18$", r"$\tfrac{9}{16}$"],
      r"$P(aa) = \tfrac14$ and $P(bb) = \tfrac14$; for both, multiply: $\tfrac{1}{16}$.",
      [r"Independent genes: multiply probabilities."],
      [r"is the probability for one gene only.",
       r"uses $\tfrac12$ for one gene, as if that cross were a testcross.",
       r"is the probability of showing both dominant traits."]),
])

S4 = Sec("Non-Mendelian genetics (5.4)", ["5.4"], r"""
\begin{compare}{Pattern}{What happens}{Example}
Linked genes & genes close together on one chromosome are inherited together unless crossing over separates them; recombination frequency ($\%$ recombinant offspring) gives map distance & body color and wing shape in fruit flies \\
Sex-linked (X-linked) & genes on the X chromosome; males (XY) express a recessive allele with only one copy & hemophilia, red--green color blindness \\
Incomplete dominance & heterozygote is intermediate & red $\times$ white snapdragons give pink \\
Codominance and multiple alleles & both alleles expressed; more than two alleles in the population & ABO blood types ($I^A$, $I^B$, $i$) \\
Polygenic traits & many genes each add a little, giving continuous variation & human height, skin color \\
Nonnuclear inheritance & genes in mitochondria and chloroplasts pass in the egg's cytoplasm & mitochondrial disorders inherited from the mother \\
\end{compare}
""", checks=[
    Q("5.4 X-linked trait", r"A woman who is a carrier of red--green color blindness (an X-linked recessive trait) has children with a man with normal vision. What is the probability that a son will be color-blind?",
      r"$\tfrac12$", [r"$\tfrac14$", r"$0$", r"$1$"],
      r"A son gets his Y from his father and one of his mother's two X chromosomes, half of which carry the allele.",
      [r"$X^BX^b \times X^BY$: sons are $X^BY$ or $X^bY$ with equal chance."],
      [r"is the probability that a child of unknown sex is a color-blind son.",
       r"the son's only X comes from his carrier mother.",
       r"only half of the mother's eggs carry the allele."]),
])

S5 = Sec("Environmental effects on phenotype (5.5)", ["5.5"], r"""
A phenotype comes from both genotype and environment. \textbf{Phenotypic plasticity} is one genotype giving different phenotypes in different environments:
\begin{itemize}
\item hydrangea flowers are blue in acidic soil and pink in alkaline soil;
\item Himalayan rabbits and Siamese cats have dark fur on their cooler extremities, because the enzyme that makes the pigment works only below body temperature;
\item in many turtles, the incubation temperature of the egg determines the sex;
\item people with the genotype for phenylketonuria (PKU) avoid its effects with a low-phenylalanine diet.
\end{itemize}
""", checks=[
    Q("5.5 Plasticity", r"Cuttings from a single hydrangea plant produce blue flowers when planted in acidic soil and pink flowers in alkaline soil. What does this show?",
      r"The environment affects how a genotype is expressed.", [r"The soil causes mutations in the flower-color gene.", r"The plants inherited different alleles from their parent.", r"Flower color is a sex-linked trait."],
      r"The cuttings are genetically identical; only the environment differs.",
      [r"Same genotype, different phenotypes."],
      [r"soil pH changes pigment chemistry, not DNA sequence.",
       r"cuttings are clones of one plant.",
       r"sex linkage does not explain an effect of soil."]),
])

QS = [
    Set("Meiosis and diversity (5.1--5.2)", [
        Q("5.1 Separating homologs", r"During which phase do homologous chromosomes separate?",
          r"anaphase I", [r"anaphase II", r"anaphase of mitosis", r"prophase I"],
          r"Homologs pair in prophase I and are pulled to opposite poles in anaphase I.",
          [r"Meiosis I: homologs. Meiosis II: sister chromatids."],
          [r"separates sister chromatids.",
           r"mitosis separates sister chromatids; homologs do not pair.",
           r"homologs pair and cross over then; they separate later."]),
        Q("5.2 Crossing over", r"When and between which structures does crossing over occur?",
          r"in prophase I, between non-sister chromatids of homologous chromosomes", [r"in prophase II, between sister chromatids", r"in anaphase I, between non-homologous chromosomes", r"during S phase, between the two strands of DNA"],
          r"Paired homologs exchange segments of non-sister chromatids, recombining alleles.",
          [r"Recombination needs two different homologs."],
          [r"sister chromatids are identical, so exchanges between them change nothing.",
           r"homologs, not non-homologs, cross over, and before anaphase.",
           r"replication copies DNA; it does not exchange segments between chromosomes."]),
        Q("5.2 Nondisjunction", r"A pair of homologous chromosomes fails to separate in meiosis I, but meiosis II is normal. What is the chromosome content of the four gametes?",
          r"two have an extra chromosome and two are missing one", [r"all four are normal", r"one has an extra chromosome, one is missing one, and two are normal", r"all four have an extra chromosome"],
          r"Both homologs go to one cell in meiosis I; meiosis II then gives two $n + 1$ gametes from that cell and two $n - 1$ gametes from the other.",
          [r"An error in meiosis I affects every gamete."],
          [r"the error in meiosis I affects all four products.",
           r"is the result of nondisjunction in meiosis II.",
           r"the missing chromosomes must end up somewhere: two cells lack them."]),
        Q("5.1 Comparing divisions", r"Which describes a result of meiosis but not of mitosis?",
          r"daughter cells that are haploid and genetically different from one another", [r"daughter cells genetically identical to the parent", r"two daughter cells", r"replication of DNA before division"],
          r"Meiosis halves the chromosome number and shuffles alleles; mitosis keeps both the number and the alleles.",
          [r"Meiosis: $4$ haploid, varied cells."],
          [r"describes mitosis.",
           r"mitosis gives two cells; meiosis gives four.",
           r"DNA is replicated once before both kinds of division."]),
    ]),
    Set("A testcross with two genes (5.3--5.4)", [
        Q("5.3 Expected ratio", r"If the two genes assorted independently, what ratio of the four phenotypes would be expected among the offspring?",
          r"$1:1:1:1$", [r"$9:3:3:1$", r"$3:1$", r"$1:2:1$"],
          r"$BbVv$ makes four kinds of gametes in equal numbers if the genes assort independently; the $bbvv$ male contributes only $bv$, so each gamete type shows up as its own phenotype.",
          [r"Testcross: offspring phenotypes mirror the heterozygote's gametes."],
          [r"is the ratio from a dihybrid cross of two heterozygotes.",
           r"is a monohybrid ratio.",
           r"is the genotype ratio of a monohybrid cross."]),
        Q("5.4 Recombinants", r"Which offspring are recombinants?",
          r"gray body, vestigial wings and black body, normal wings", [r"gray body, normal wings and black body, vestigial wings", r"all gray-bodied offspring", r"all offspring with vestigial wings"],
          r"The female received $BV$ from one parent and $bv$ from the other; offspring with new combinations ($Bv$, $bV$) come from crossing over, and they are the less common classes.",
          [r"Parental classes are the most frequent."],
          [r"those are the parental combinations.",
           r"half of the gray-bodied flies are parental.",
           r"half of the vestigial flies are parental."]),
        Q("5.4 Recombination frequency", r"What is the recombination frequency between the two genes?",
          r"$17\%$", [r"$50\%$", r"$8.5\%$", r"$83\%$"],
          r"$(206 + 185)/2300 = 391/2300 = 0.17$.",
          [r"Recombinants divided by total offspring."],
          [r"is the value expected for unlinked genes.",
           r"counts only one recombinant class.",
           r"is the parental fraction."], sort=True),
        Q("5.4 Conclusion", r"What do the results show about the two genes?",
          r"They are linked, about $17$ map units apart on the same chromosome.", [r"They are on different chromosomes and assort independently.", r"They are the same gene.", r"They are X-linked, since the parents differ in sex."],
          r"Parental types far outnumber recombinants, so the genes travel together on one chromosome; $1\%$ recombination $\approx 1$ map unit.",
          [r"Unlinked: about $50\%$ recombinant. Here: $17\%$."],
          [r"independent assortment would give about $1:1:1:1$.",
           r"they control different traits.",
           r"the results show linkage, not sex linkage; both sexes received both traits alike."]),
    ], stim=r"""In fruit flies, gray body ($B$) is dominant to black body ($b$), and normal wings ($V$) are dominant to vestigial wings ($v$). A female heterozygous for both genes, who received $BV$ from one parent and $bv$ from the other, is crossed with a black, vestigial male ($bbvv$). The offspring are:

\medskip
\begin{tabular}{@{}lc@{}}\toprule
Phenotype & Number \\ \midrule
Gray body, normal wings & 965 \\
Black body, vestigial wings & 944 \\
Gray body, vestigial wings & 206 \\
Black body, normal wings & 185 \\ \bottomrule
\end{tabular}""", stim_title="Questions 5--8"),
    Set("Patterns of inheritance (5.3--5.5)", [
        Q("5.3 Three children", r"Two parents are both heterozygous ($Aa$) for a gene with a dominant allele $A$. What is the probability that all three of their children show the dominant phenotype?",
          r"$\tfrac{27}{64}$", [r"$\tfrac34$", r"$\tfrac{9}{16}$", r"$\tfrac{1}{64}$"],
          r"Each child has a $\tfrac34$ chance; the children are independent, so $\left(\tfrac34\right)^3 = \tfrac{27}{64}$.",
          [r"Multiply for ``and''."],
          [r"is the probability for one child.",
           r"is the probability for two children.",
           r"is the probability that all three show the recessive phenotype."]),
        Q("5.4 Incomplete dominance", r"In snapdragons, red ($C^RC^R$) crossed with white ($C^WC^W$) gives pink offspring. What phenotypes are expected from crossing two pink plants?",
          r"$1$ red $: 2$ pink $: 1$ white", [r"all pink", r"$3$ red $: 1$ white", r"$1$ red $: 1$ white"],
          r"$C^RC^W \times C^RC^W$ gives $1\ C^RC^R : 2\ C^RC^W : 1\ C^WC^W$; with incomplete dominance each genotype has its own phenotype.",
          [r"Phenotype ratio equals genotype ratio."],
          [r"pink plants are heterozygous, so their offspring segregate.",
           r"is a complete-dominance ratio.",
           r"leaves out the heterozygotes."]),
        Q("5.4 Blood types", r"A man with type A blood ($I^Ai$) and a woman with type B blood ($I^Bi$) have a child. What is the probability that the child has type O blood?",
          r"$\tfrac14$", [r"$0$", r"$\tfrac12$", r"$\tfrac34$"],
          r"Type O is $ii$: $\tfrac12$ chance of $i$ from each parent, so $\tfrac14$.",
          [r"Possible children: $I^AI^B$, $I^Ai$, $I^Bi$, $ii$, each $\tfrac14$."],
          [r"both parents carry $i$.",
           r"is the chance of receiving $i$ from one parent.",
           r"is the chance of not being type O."]),
        Q("5.4 Hemophilia", r"A woman who is a carrier for hemophilia (X-linked recessive) and a man without hemophilia have a daughter. What is the probability that the daughter has hemophilia?",
          r"$0$", [r"$\tfrac14$", r"$\tfrac12$", r"$1$"],
          r"Every daughter receives her father's normal X, so none can be affected; half will be carriers.",
          [r"$X^HX^h \times X^HY$: daughters are $X^HX^H$ or $X^HX^h$."],
          [r"is the probability that a child of unknown sex is an affected son.",
           r"is the probability that a daughter is a carrier.",
           r"the father's normal X prevents it."]),
        Q("5.4 Mitochondrial inheritance", r"A disorder caused by a mutation in mitochondrial DNA appears in all the children of affected women but none of the children of affected men. Why?",
          r"Mitochondria are passed to offspring in the egg's cytoplasm, not by sperm.", [r"The gene is on the Y chromosome.", r"The gene is X-linked recessive.", r"Men cannot carry mitochondrial DNA."],
          r"Offspring inherit mitochondria from the mother, so mitochondrial traits follow the maternal line.",
          [r"Maternal (cytoplasmic) inheritance."],
          [r"a Y-linked trait would pass from fathers to sons.",
           r"an X-linked trait can pass from father to daughters.",
           r"men's cells contain mitochondria, but their sperm do not pass them on."]),
        Q("5.5 Temperature and fur", r"Himalayan rabbits have white bodies with black ears, nose and feet. If a patch of fur on the back is shaved and kept cold while it regrows, it grows in black. What explains this?",
          r"The enzyme that makes black pigment is active only at lower temperatures, as in the rabbit's extremities.", [r"Cold causes a mutation in the pigment gene.", r"The shaved fur is inherited differently.", r"Black fur grows only where the skin is damaged."],
          r"A temperature-sensitive enzyme links phenotype to environment: same genotype, different color where cooler.",
          [r"Phenotypic plasticity."],
          [r"the DNA is unchanged.",
           r"inheritance is the same over the whole body.",
           r"the effect follows temperature, not damage."]),
    ]),
]

UNIT = Unit(5, "heredity", "Heredity", "8--11\\%", "5.1--5.5",
    abstract=r"""Unit 5 covers how traits are passed on: meiosis and how it differs from mitosis, the sources of genetic diversity (crossing over, independent assortment, random fertilization) and the consequences of nondisjunction, Mendel's laws and probability, pedigrees, non-Mendelian patterns (linkage, sex linkage, incomplete dominance, codominance, multiple alleles, polygenic and nonnuclear inheritance), and environmental effects on phenotype. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5], qsections=QS,
    frq=FRQ("Analyze Data", 4, r"""In a plant species, purple flowers ($P$) are dominant to white ($p$), and smooth seeds ($S$) are dominant to wrinkled ($s$). Plants heterozygous for both genes ($PpSs$) were crossed with each other, and the $1600$ offspring were scored. The null hypothesis is that the two genes assort independently.

\medskip
\begin{tabular}{@{}lc@{}}\toprule
Phenotype & Observed \\ \midrule
Purple, smooth & 891 \\
Purple, wrinkled & 302 \\
White, smooth & 290 \\
White, wrinkled & 117 \\ \bottomrule
\end{tabular}

\medskip
$\chi^2 = \sum \dfrac{(o - e)^2}{e}$. Critical values at $p = 0.05$: $3.84$ (1 degree of freedom), $5.99$ (2), $7.81$ (3), $9.49$ (4).""", [
        Part("A", 1, r"\textbf{Calculate} the expected number of white, wrinkled offspring if the null hypothesis is true.",
             r"$\tfrac1{16} \times 1600 = 100$ (the $9:3:3:1$ ratio gives $900$, $300$, $300$, $100$).",
             r"Using a $1:1:1:1$ ratio ($400$)."),
        Part("B", 1, r"\textbf{Calculate} the chi-square value for these data.",
             r"$\chi^2 = \dfrac{81}{900} + \dfrac{4}{300} + \dfrac{100}{300} + \dfrac{289}{100} = 0.09 + 0.01 + 0.33 + 2.89 = 3.3$ (accept $3.32$--$3.34$).",
             r"Dividing by the observed instead of the expected counts."),
        Part("C", 1, r"Using the critical values, \textbf{evaluate} the null hypothesis.",
             r"With $4 - 1 = 3$ degrees of freedom the critical value is $7.81$; $3.3 < 7.81$, so the null hypothesis is not rejected: the data are consistent with independent assortment.",
             r"Using $1$ or $4$ degrees of freedom; saying the null hypothesis is ``proven.''"),
        Part("D", 1, r"\textbf{Explain} how the behavior of chromosomes during meiosis accounts for the result in part C.",
             r"The two genes are on different chromosomes (or far apart on one); in metaphase I each homologous pair lines up independently of the others, so alleles of the two genes are sorted into gametes in all combinations equally often.",
             r"Explaining with crossing over alone, or with mitosis."),
    ], mins=10),
    frq_topic="a chi-square test of a dihybrid cross",
)
