from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part

S1 = Sec("DNA and RNA structure (6.1)", ["6.1"], r"""
Heritable information is stored in DNA (and in RNA in some viruses). Prokaryotes usually have one circular chromosome plus small circular \textbf{plasmids}; eukaryotes have several linear chromosomes wound around histone proteins.

In double-stranded DNA the two strands run antiparallel ($5' \to 3'$ and $3' \to 5'$), and a purine (A or G, two rings) always pairs with a pyrimidine (T or C, one ring), which keeps the helix the same width: A with T, G with C. RNA is usually single-stranded, contains ribose and uses uracil (U) in place of thymine.
""", checks=[
    Q("6.1 Plasmids", r"Which structure is found in many bacteria but not in the nucleus of a eukaryotic cell?",
      r"small circular DNA molecules called plasmids", [r"linear chromosomes", r"DNA wound around histones", r"a nuclear envelope"],
      r"Plasmids carry extra genes (often antibiotic resistance) and are separate from the bacterial chromosome.",
      [r"Prokaryotic genome: one circular chromosome plus plasmids."],
      [r"linear chromosomes are typical of eukaryotes.",
       r"histones are typical of eukaryotic chromatin.",
       r"prokaryotes have no nuclear envelope."]),
])

S2 = Sec("DNA replication (6.2)", ["6.2"], r"""
Replication is \textbf{semiconservative}: each new double helix has one old strand and one new strand.
\begin{terms}
Helicase & unwinds the double helix at the replication fork \\
Topoisomerase & relieves the twisting ahead of the fork \\
Primase & lays down a short RNA primer, because DNA polymerase can only add to an existing $3'$ end \\
DNA polymerase & adds nucleotides to the $3'$ end, so new DNA grows only $5' \to 3'$, and proofreads \\
Leading and lagging strands & one strand is made continuously toward the fork; the other is made away from it in short Okazaki fragments \\
Ligase & joins the Okazaki fragments \\
\end{terms}
""", checks=[
    Q("6.2 Lagging strand", r"Why is one strand made in short fragments during DNA replication?",
      r"DNA polymerase can add nucleotides only to a $3'$ end, so on one template the new strand must grow away from the replication fork in pieces.", [r"Helicase cuts the strand into fragments.", r"The lagging strand is made of RNA.", r"Ligase can join only short pieces."],
      r"The two templates are antiparallel, and new DNA is made only $5' \to 3'$; the lagging strand is built backward in Okazaki fragments as the fork opens.",
      [r"Antiparallel templates plus one-way synthesis."],
      [r"helicase unwinds; it does not cut.",
       r"only the primers are RNA.",
       r"ligase joins fragments; it does not cause them."]),
])

S3 = Sec("Transcription, RNA processing and translation (6.3--6.4)", ["6.3", "6.4"], r"""
\textbf{Transcription.} RNA polymerase reads the template strand $3' \to 5'$ and builds a complementary RNA $5' \to 3'$. It makes messenger RNA (mRNA) and also transfer RNA (tRNA) and ribosomal RNA (rRNA).

\textbf{Processing in eukaryotes.} The pre-mRNA receives a $5'$ cap and a poly-A tail, and \textbf{introns} are spliced out, joining the \textbf{exons}. Alternative splicing lets one gene encode several proteins.

\textbf{Translation.} At the ribosome, each mRNA codon (three bases) pairs with the anticodon of a tRNA carrying a specific amino acid. Translation starts at AUG (methionine) and ends at a stop codon (UAA, UAG or UGA). The code is redundant (several codons per amino acid) and nearly universal. In prokaryotes translation begins while the mRNA is still being transcribed.

\textbf{Retroviruses} such as HIV use reverse transcriptase to copy their RNA genome into DNA, which is inserted into the host's genome.
""", checks=[
    Q("6.3 From template to amino acid", r"A DNA template strand contains the sequence $3'$-TAC-$5'$. Which codon is transcribed from it, and which amino acid does that codon specify?",
      r"$5'$-AUG-$3'$, methionine", [r"$5'$-UAC-$3'$, tyrosine", r"$5'$-ATG-$3'$, methionine", r"$5'$-GUA-$3'$, valine"],
      r"RNA is complementary to the template: T $\to$ A, A $\to$ U, C $\to$ G, giving AUG, the start codon for methionine.",
      [r"Template $3'$-TAC-$5'$ $\to$ mRNA $5'$-AUG-$3'$."],
      [r"copies the template instead of complementing it.",
       r"uses T, which RNA does not contain.",
       r"reverses the codon."]),
])

S4 = Sec("Regulation of gene expression and cell specialization (6.5--6.6)", ["6.5", "6.6"], r"""
\textbf{In bacteria}, genes for one pathway are often grouped in an \textbf{operon}, a single promoter and operator controlling several genes.
\begin{compare}{Operon}{Without the signal}{With the signal}
\emph{lac} (inducible) & repressor bound to the operator blocks transcription & lactose (as allolactose) binds the repressor, which releases the operator: genes on \\
\emph{trp} (repressible) & repressor inactive: genes on & tryptophan binds the repressor, which then binds the operator: genes off \\
\end{compare}
\textbf{In eukaryotes}, transcription factors bind promoters and distant enhancers; epigenetic changes alter access to DNA (histone acetylation loosens chromatin and raises transcription; DNA methylation lowers it); small RNAs block or destroy mRNA. All of an organism's cells carry the same genome, but different cell types express different sets of genes because they contain different transcription factors: that is cell specialization.
""", checks=[
    Q("6.5 The lac operon", r"\emph{E. coli} is moved from a medium without lactose to one with lactose (and no glucose). What happens to the \emph{lac} operon?",
      r"Lactose binds the repressor, which releases the operator, and the genes are transcribed.", [r"Lactose binds the operator and blocks transcription.", r"The repressor binds more tightly, and the genes are switched off.", r"Nothing changes, because the genes are always transcribed."],
      r"The \emph{lac} operon is inducible: the inducer inactivates the repressor so RNA polymerase can transcribe the genes for using lactose.",
      [r"Inducer removes the repressor."],
      [r"the repressor, not lactose, binds the operator.",
       r"lactose loosens the repressor.",
       r"without lactose the operon is repressed."]),
])

S5 = Sec("Mutations (6.7)", ["6.7"], r"""
\begin{compare}{Mutation}{Change}{Typical effect}
Silent & base substitution giving the same amino acid (redundancy of the code) & none \\
Missense & substitution giving a different amino acid & from none to severe (sickle cell) \\
Nonsense & substitution giving a stop codon & a shortened, usually nonfunctional protein \\
Frameshift & insertion or deletion of bases not in a multiple of three & every codon after it changes \\
\end{compare}
Mutations arise from errors in replication or from mutagens (UV light, some chemicals). They are the original source of genetic variation. Bacteria also gain genes by horizontal transfer (transformation, transduction by viruses, conjugation), and viruses can recombine when two infect the same cell.
""", checks=[
    Q("6.7 Frameshift", r"A single nucleotide is deleted near the beginning of a gene's coding region. What is the most likely effect?",
      r"Every codon after the deletion is read differently, usually producing a nonfunctional protein.", [r"One amino acid is replaced, and the rest of the protein is normal.", r"The protein is unchanged, because the code is redundant.", r"The protein is one amino acid shorter but otherwise normal."],
      r"Removing one base shifts the reading frame, changing all downstream codons and often creating an early stop codon.",
      [r"Codons are read in groups of three from a fixed start."],
      [r"describes a missense substitution.",
       r"redundancy protects only some substitutions.",
       r"would need a deletion of three bases."]),
])

S6 = Sec("Biotechnology (6.8)", ["6.8"], r"""
\begin{terms}
Gel electrophoresis & DNA (negatively charged by its phosphates) moves toward the positive electrode; smaller fragments move farther through the gel, so fragments separate by size, compared with a ladder of known sizes \\
PCR & cycles of heating (separate strands), cooling (primers bind) and extension (a heat-stable DNA polymerase copies the region); each cycle doubles the target, so $n$ cycles give $2^n$ copies \\
Bacterial transformation & bacteria take up a plasmid carrying a gene of interest and an antibiotic-resistance gene; growing them on the antibiotic selects the transformed cells \\
DNA sequencing & reads the order of nucleotides; used to compare genes and genomes \\
\end{terms}
""", checks=[
    Q("6.8 PCR", r"PCR starts with a single copy of a target DNA sequence. About how many copies are present after $10$ cycles?",
      r"$1024$", [r"$20$", r"$100$", r"$10$"],
      r"Each cycle doubles the number of copies: $2^{10} = 1024$.",
      [r"Exponential growth: $2^n$."],
      [r"adds two copies per cycle.",
       r"multiplies by ten.",
       r"adds one copy per cycle."], sort=True),
])

QS = [
    Set("Replication and the flow of information (6.1--6.4)", [
        Q("6.2 Semiconservative replication", r"Bacteria grown for many generations with heavy nitrogen (${}^{15}$N) are moved to a medium with light nitrogen (${}^{14}$N) and allowed to replicate once. What will the DNA be like?",
          r"All of it will be hybrid, with one heavy strand and one light strand.", [r"Half will be all heavy and half all light.", r"All of it will be light.", r"Each strand will be a random mixture of heavy and light pieces."],
          r"Each new double helix keeps one old (heavy) strand and gains one new (light) strand.",
          [r"Meselson and Stahl (1958)."],
          [r"would be conservative replication.",
           r"the old strands are kept.",
           r"would be dispersive replication."]),
        Q("6.4 Reading a message", r"An mRNA reads $5'$-AUG GCU UAA-$3'$. AUG codes for methionine, GCU for alanine, and UAA is a stop codon. What does it encode?",
          r"methionine--alanine", [r"methionine--alanine--stop amino acid", r"alanine--methionine", r"a protein three amino acids long"],
          r"Translation starts at AUG, adds alanine for GCU, and stops at UAA, which codes for no amino acid.",
          [r"Read $5' \to 3'$ from the start codon."],
          [r"stop codons do not code for an amino acid.",
           r"translation runs $5' \to 3'$ from AUG.",
           r"the stop codon adds nothing."]),
        Q("6.3 RNA processing", r"A eukaryotic gene is $8000$ nucleotides long, but its mature mRNA (excluding the cap and tail) is only $2000$ nucleotides long. What is the best explanation?",
          r"Introns were spliced out of the pre-mRNA.", [r"Only one DNA strand was transcribed.", r"Exons were removed during processing.", r"The mRNA was partly degraded by the ribosome."],
          r"Introns, often most of a gene's length, are removed; the exons are joined to form the mature mRNA.",
          [r"Exons are expressed; introns intervene."],
          [r"only one strand is always transcribed, but that does not shorten the RNA.",
           r"exons are kept.",
           r"ribosomes translate mRNA; they do not trim it."]),
        Q("6.2 Primers", r"Why does DNA replication require an RNA primer?",
          r"DNA polymerase can only add nucleotides to an existing $3'$ end.", [r"RNA primers unwind the double helix.", r"RNA primers join Okazaki fragments.", r"DNA polymerase works only on RNA templates."],
          r"Primase makes a short RNA with a free $3'$-OH from which DNA polymerase can extend.",
          [r"Polymerase extends; it cannot start from nothing."],
          [r"helicase unwinds the helix.",
           r"ligase joins fragments.",
           r"DNA polymerase copies DNA templates."]),
        Q("6.3 Transcribing a template", r"A segment of a template strand reads $3'$-TACGGA-$5'$. What mRNA is transcribed from it?",
          r"$5'$-AUGCCU-$3'$", [r"$5'$-TACGGA-$3'$", r"$5'$-ATGCCT-$3'$", r"$5'$-UCCGUA-$3'$"],
          r"Complementary bases, with U for A: T$\to$A, A$\to$U, C$\to$G, G$\to$C.",
          [r"The mRNA matches the coding strand, with U for T."],
          [r"copies the template instead of complementing it.",
           r"contains T, which RNA does not.",
           r"reverses the order."]),
    ]),
    Set("Gel electrophoresis and PCR (6.8)", [
        Q("6.8 Direction", r"Toward which electrode does DNA move in the gel, and why?",
          r"toward the positive electrode, because its phosphate groups are negatively charged", [r"toward the negative electrode, because DNA is positively charged", r"toward the positive electrode, because the bases are positively charged", r"toward whichever electrode is nearer"],
          r"The sugar--phosphate backbone carries one negative charge per nucleotide.",
          [r"Opposites attract."],
          [r"DNA is negatively charged.",
           r"the charge comes from the phosphates, and it is negative.",
           r"the direction is set by charge."]),
        Q("6.8 Estimating size", r"A fragment in the sample lane moved $2.4$ cm. What is its approximate size?",
          r"$2000$ base pairs", [r"$1000$ base pairs", r"$3000$ base pairs", r"$5000$ base pairs"],
          r"It moved as far as the $2000$-bp ladder fragment.",
          [r"Compare with the ladder."],
          [r"the $1000$-bp fragment moved farther, $3.4$ cm.",
           r"the $3000$-bp fragment moved only $1.8$ cm.",
           r"the largest fragment moved the least."]),
        Q("6.8 Separation by size", r"Why do the smaller fragments move farther than the larger ones?",
          r"Smaller fragments pass more easily through the pores of the gel.", [r"Smaller fragments carry more negative charge.", r"Larger fragments are attracted to the negative electrode.", r"Smaller fragments are made of RNA."],
          r"All DNA has about the same charge per length; the gel acts as a sieve that slows longer molecules more.",
          [r"Charge-to-mass is nearly constant, so size decides."],
          [r"charge is proportional to length, so larger fragments carry more.",
           r"all DNA moves toward the positive electrode.",
           r"they are all DNA."]),
        Q("6.8 Amplification", r"Before the gel, the students amplified a $500$-bp region from a few copies by PCR. Which step of each PCR cycle lets the primers bind?",
          r"cooling the mixture after the strands are separated", [r"heating the mixture to about $95^\circ$C", r"adding ligase", r"adding RNA polymerase"],
          r"Heating separates the strands; cooling lets the primers anneal to their complementary sequences; then the polymerase extends them.",
          [r"Denature, anneal, extend."],
          [r"heating separates the strands.",
           r"PCR uses no ligase.",
           r"PCR uses a heat-stable DNA polymerase."]),
    ], stim=r"""Students separate DNA fragments by gel electrophoresis alongside a ladder of fragments of known size. The table shows how far each ladder fragment moved.

\medskip
\begin{tabular}{@{}cc@{}}\toprule
Ladder fragment (bp) & Distance moved (cm) \\ \midrule
5000 & 1.0 \\
3000 & 1.8 \\
2000 & 2.4 \\
1000 & 3.4 \\
500 & 4.3 \\ \bottomrule
\end{tabular}""", stim_title="Questions 6--9"),
    Set("Regulation and mutation (6.5--6.7)", [
        Q("6.5 The trp operon", r"When tryptophan is plentiful, \emph{E. coli} stops making the enzymes that synthesize it. How?",
          r"Tryptophan binds the repressor, which then binds the operator and blocks transcription.", [r"Tryptophan binds RNA polymerase and destroys it.", r"Tryptophan removes the repressor from the operator.", r"The enzymes are made but immediately degraded."],
          r"The \emph{trp} operon is repressible: its end product acts as a corepressor.",
          [r"Product present: genes off."],
          [r"tryptophan acts through the repressor.",
           r"that would turn the genes on.",
           r"the control is at transcription."]),
        Q("6.6 Same genome", r"A liver cell and a neuron from the same person have the same DNA but make different proteins. Why?",
          r"Different transcription factors are active in each cell type, so different genes are expressed.", [r"The two cells have different genes.", r"Neurons have lost the genes for liver proteins.", r"Liver cells translate introns."],
          r"Cell specialization comes from regulating which genes are transcribed, not from changing the genome.",
          [r"Same genes, different expression."],
          [r"somatic cells share one genome.",
           r"the genes are present but silent.",
           r"introns are spliced out in all cells."]),
        Q("6.7 Silent mutation", r"A base substitution changes a codon from CUU to CUC. Both code for leucine. What kind of mutation is this?",
          r"silent", [r"missense", r"nonsense", r"frameshift"],
          r"Because the genetic code is redundant, the amino acid, and so the protein, is unchanged.",
          [r"Same amino acid: silent."],
          [r"a missense mutation changes the amino acid.",
           r"a nonsense mutation creates a stop codon.",
           r"a substitution does not shift the frame."]),
        Q("6.7 Nonsense mutation", r"A substitution changes the codon UGG (tryptophan) to UGA (stop) in the middle of a gene. What is the most likely result?",
          r"A shortened protein that is probably nonfunctional", [r"A protein with one different amino acid", r"A normal protein", r"A longer protein"],
          r"The new stop codon ends translation early.",
          [r"Premature stop codon."],
          [r"describes a missense mutation.",
           r"the protein is cut short.",
           r"translation stops sooner, not later."]),
        Q("6.5 Epigenetics", r"Acetylation of histones near a gene makes the chromatin less tightly packed. What is the likely effect on the gene?",
          r"Its transcription increases.", [r"Its DNA sequence changes.", r"Its transcription stops.", r"Its mRNA is no longer translated."],
          r"Looser chromatin lets transcription factors and RNA polymerase reach the DNA.",
          [r"Acetylation opens; methylation of DNA tends to close."],
          [r"epigenetic changes do not alter the sequence.",
           r"acetylation promotes transcription.",
           r"translation is not directly affected."]),
    ]),
]

UNIT = Unit(6, "gene-expression-regulation", "Gene Expression and Regulation", "12--16\\%", "6.1--6.8",
    abstract=r"""Unit 6 follows genetic information from DNA to protein and covers how its use is controlled: DNA and RNA structure, semiconservative replication, transcription and RNA processing, translation and the genetic code, operons and eukaryotic gene regulation (transcription factors, epigenetics), cell specialization, mutations and horizontal gene transfer, and the biotechnology tools that rely on these ideas (gel electrophoresis, PCR, transformation, sequencing). Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6], qsections=QS,
    frq=FRQ("Interpreting and Evaluating Experimental Results", 9, r"""In \emph{E. coli}, the \emph{lac} operon includes the gene \emph{lacZ}, which encodes the enzyme $\beta$-galactosidase. Researchers grew four strains in a medium without glucose, either without lactose or with lactose, and measured $\beta$-galactosidase activity (mean $\pm 2\,SE_{\bar x}$, arbitrary units).

\medskip
\begin{tabular}{@{}lcc@{}}\toprule
Strain & Without lactose & With lactose \\ \midrule
Wild type & $2 \pm 1$ & $980 \pm 60$ \\
Mutant 1: repressor cannot bind the operator & $960 \pm 70$ & $990 \pm 50$ \\
Mutant 2: repressor cannot bind the inducer & $3 \pm 1$ & $4 \pm 2$ \\
Mutant 3: mutation in the \emph{lacZ} coding sequence & $1 \pm 1$ & $2 \pm 1$ \\ \bottomrule
\end{tabular}""", [
        Part("A", 1, r"\textbf{Describe} the role of the repressor protein in regulating the \emph{lac} operon in wild-type cells.",
             r"When lactose is absent, the repressor binds the operator and blocks RNA polymerase from transcribing the operon's genes; when lactose (allolactose) is present, it binds the repressor, which releases the operator.",
             r"Saying the repressor destroys $\beta$-galactosidase."),
        Part("B", 3, r"(i) \textbf{Identify} the two independent variables in this experiment. (ii) \textbf{Identify} the strain that serves as the control. (iii) \textbf{Describe} the effect of lactose on $\beta$-galactosidase activity in the wild type.",
             r"1 pt: the strain (genotype) and the presence or absence of lactose. 1 pt: the wild type. 1 pt: activity rises from about $2$ to about $980$ units, roughly $500$-fold, when lactose is present.",
             r"Naming $\beta$-galactosidase activity (the dependent variable) in (i)."),
        Part("C", 3, r"(i) \textbf{Explain} the activity of mutant 1 without lactose. (ii) \textbf{Explain} the activity of mutant 2 with lactose. (iii) \textbf{Determine} whether mutant 1 and the wild type differ significantly in activity when lactose is present.",
             r"1 pt: the repressor cannot bind the operator, so transcription proceeds even without lactose (constitutive expression). 1 pt: the inducer cannot remove the repressor, so it stays on the operator and the genes are not transcribed even with lactose. 1 pt: no: the intervals $920$--$1040$ and $940$--$1040$ overlap.",
             r"Explaining mutant 2 as lacking the enzyme gene; claiming a difference from the means."),
        Part("D", 2, r"A double mutant carries both the mutation of mutant 1 and the mutation of mutant 3. \textbf{Predict} its $\beta$-galactosidase activity without lactose, and \textbf{justify} your prediction.",
             r"1 pt: low, like mutant 3 (about $1$--$2$ units). 1 pt: the repressor cannot bind the operator, so the operon is transcribed all the time, but the \emph{lacZ} coding mutation means the enzyme produced is nonfunctional (or not produced), so there is no activity to measure.",
             r"Predicting high activity because ``the operon is always on,'' ignoring the coding mutation."),
    ], mins=25),
    frq_topic="lac operon mutants",
)
