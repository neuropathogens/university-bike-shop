from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph, Series

MODEL = Graph(r"CDK1 inhibitor concentration ($\mu$M)", r"Cells in mitosis (\%)", x=(0, 10, 2), y=(0, 10, 2),
              series=[Series("mean $\\pm 2\\,SE$", [(0, 8.0, 1.0), (1, 6.2, 1.0), (2, 4.1, 0.8), (5, 1.5, 0.6), (10, 0.5, 0.4)])],
              legend=False, caption=r"Model graph: means joined by lines, with error bars of two standard errors of the mean.")

S1 = Sec("Cell communication (4.1)", ["4.1"], r"""
Cells communicate by generating, transmitting, receiving and responding to chemical signals.

\begin{compare}{Distance}{Mechanism}{Example}
Direct contact & signals pass through junctions, or surface molecules touch & gap junctions (animals), plasmodesmata (plants), immune cells recognizing antigen-presenting cells \\
Short range (local) & signal diffuses to nearby cells & paracrine growth factors; neurotransmitters across a synapse \\
Long range & hormones travel in the blood (endocrine) & insulin from the pancreas acting on liver and muscle \\
Between bacteria & quorum sensing: each cell releases a signal, and a response begins when the concentration (and so the population) is high enough & bioluminescence, biofilm formation \\
\end{compare}
""", checks=[
    Q("4.1 Endocrine signaling", r"Insulin is released by cells in the pancreas and travels in the blood to muscle and liver cells. What kind of signaling is this?",
      r"endocrine (long-distance) signaling", [r"direct contact through gap junctions", r"synaptic signaling", r"quorum sensing"],
      r"Hormones carried by the circulatory system to distant target cells are endocrine signals.",
      [r"Blood-borne hormone: endocrine."],
      [r"gap junctions connect neighboring cells directly.",
       r"synaptic signals cross the tiny gap between a neuron and its target.",
       r"quorum sensing is signaling among bacteria."]),
])

S2 = Sec("Signal transduction (4.2--4.3)", ["4.2", "4.3"], r"""
A signaling pathway has three stages.
\begin{terms}
Reception & a signal (ligand) binds a specific receptor. Hydrophilic or large ligands (epinephrine, insulin, most peptides) bind receptors in the plasma membrane: G protein-coupled receptors, receptor tyrosine kinases, ligand-gated ion channels. Small hydrophobic ligands (steroid hormones such as testosterone) cross the membrane and bind receptors inside the cell. \\
Transduction & binding changes the receptor's shape, which starts a relay: protein kinases phosphorylate the next protein in a cascade; second messengers such as cAMP or Ca$^{2+}$ spread the signal. Each step activates many molecules of the next, amplifying the signal. \\
Response & the cell changes gene expression, enzyme activity, shape, growth or division, or undergoes apoptosis (programmed cell death). \\
\end{terms}

Because each step depends on the previous one, a mutation in any component can block the response or switch it on permanently. Turning signals off matters too: phosphatases remove phosphates, and phosphodiesterase breaks down cAMP.
""", checks=[
    Q("4.2 Steroid receptors", r"Why do steroid hormones such as estrogen usually bind receptors inside the cell rather than on its surface?",
      r"They are small and nonpolar, so they can diffuse through the plasma membrane.", [r"They are too large to fit membrane receptors.", r"They are charged, so they are attracted into the nucleus.", r"They are carried inside by aquaporins."],
      r"Lipid-soluble hormones cross the hydrophobic bilayer; their receptors are in the cytoplasm or nucleus, often acting as transcription factors.",
      [r"Hydrophobic ligand: intracellular receptor."],
      [r"steroids are small molecules.",
       r"steroids are nonpolar and uncharged.",
       r"aquaporins carry water."]),
    Q("4.3 Amplification", r"One epinephrine molecule binding to a liver cell can lead to the release of millions of glucose molecules. Which explains this?",
      r"Each activated enzyme in the cascade activates many molecules of the next.", [r"Epinephrine is converted into glucose.", r"Each epinephrine molecule binds millions of receptors.", r"Glucose molecules activate more epinephrine receptors."],
      r"At each step one active molecule (receptor, G protein, adenylyl cyclase, kinase) acts on many substrate molecules, multiplying the signal.",
      [r"Amplification is a property of cascades."],
      [r"the signal triggers the release of stored glucose; it is not converted itself.",
       r"one ligand binds one receptor.",
       r"glucose is the response, not a signal in this pathway."]),
])

S3 = Sec("Feedback (4.4)", ["4.4"], r"""
\textbf{Negative feedback} reverses a change, keeping a variable near a set point (homeostasis). When blood glucose rises, the pancreas releases insulin, cells take up glucose, and glucose falls; when it falls, glucagon raises it again. Body temperature and blood calcium are regulated the same way.

\textbf{Positive feedback} amplifies a change, driving a process to completion. During childbirth, contractions push the baby against the cervix, which triggers oxytocin release, which strengthens contractions. Blood clotting and the spread of ripening by ethylene among fruits are other examples.

\begin{trap}
In type 1 diabetes, the pancreas makes too little insulin; in type 2, cells respond poorly to it. Either way the negative-feedback loop that lowers blood glucose fails.
\end{trap}
""", checks=[
    Q("4.4 Positive feedback", r"During labor, contractions of the uterus stimulate the release of oxytocin, which causes stronger contractions. This is an example of",
      r"positive feedback", [r"negative feedback", r"homeostasis", r"quorum sensing"],
      r"The response (oxytocin) increases the stimulus (contractions), amplifying it until the baby is born.",
      [r"Response reinforces the stimulus: positive feedback."],
      [r"negative feedback would reduce the contractions.",
       r"homeostasis holds a variable steady; this drives it further.",
       r"quorum sensing is bacterial signaling."]),
])

S4 = Sec("Cell cycle (4.5)", ["4.5"], r"""
\begin{compare}{Phase}{What happens}{DNA per nucleus}
G$_1$ & growth; normal functions; a cell may leave the cycle (G$_0$) & $1x$ \\
S & DNA replication: each chromosome becomes two sister chromatids & $1x \to 2x$ \\
G$_2$ & growth; preparation for division & $2x$ \\
Mitosis & prophase (chromosomes condense, spindle forms), metaphase (chromosomes line up at the middle), anaphase (sister chromatids separate to opposite poles), telophase (nuclei re-form) & $2x$ until anaphase \\
Cytokinesis & the cytoplasm divides; two genetically identical daughter cells & $1x$ each \\
\end{compare}

A human cell has $46$ chromosomes in G$_1$. After S phase it still has $46$ chromosomes, but each now has two chromatids ($92$ chromatids). Mitosis maintains the chromosome number; most of a cell's life is spent in interphase.
""", checks=[
    Q("4.5 Chromatids", r"A human cell ($2n = 46$) has just finished S phase. How many chromosomes and chromatids does it have?",
      r"$46$ chromosomes and $92$ chromatids", [r"$92$ chromosomes and $92$ chromatids", r"$23$ chromosomes and $46$ chromatids", r"$46$ chromosomes and $46$ chromatids"],
      r"Replication copies each chromosome into two sister chromatids joined at the centromere; the chromosome count stays $46$.",
      [r"Count centromeres for chromosomes."],
      [r"sister chromatids count as one chromosome until they separate in anaphase.",
       r"halving happens in meiosis, not S phase.",
       r"the DNA has been copied, so there are two chromatids per chromosome."]),
])

S5 = Sec("Regulation of the cell cycle (4.6)", ["4.6"], r"""
\textbf{Checkpoints} decide whether the cycle continues: at G$_1$ (is the cell big enough, is the DNA undamaged, are growth signals present?), at G$_2$ (is DNA replication complete and correct?) and in mitosis (are all chromosomes attached to the spindle?). The drivers are \textbf{cyclins}, whose levels rise and fall through the cycle, and \textbf{cyclin-dependent kinases} (CDKs), which are active only when bound to a cyclin and then phosphorylate target proteins that move the cell to the next phase.

\begin{terms}
External signals & growth factors stimulate division; density-dependent inhibition stops it when cells crowd \\
p53 & a tumor-suppressor protein that halts the cycle when DNA is damaged and can trigger apoptosis \\
Cancer & mutations in proto-oncogenes (accelerators stuck on) and tumor-suppressor genes (brakes lost) let cells divide without control \\
Apoptosis & orderly self-destruction that removes damaged or unneeded cells \\
\end{terms}
""", checks=[
    Q("4.6 Cyclins and CDKs", r"A mutation makes a CDK active even without its cyclin. What is the most likely effect?",
      r"The cell passes checkpoints when it should not, which can lead to uncontrolled division.", [r"The cell stops dividing permanently.", r"The cell undergoes meiosis instead of mitosis.", r"The cell's DNA can no longer be replicated."],
      r"Normally CDK activity is limited by cyclin levels; a constitutively active CDK pushes the cycle forward regardless of conditions.",
      [r"Accelerator stuck on."],
      [r"active CDKs promote division.",
       r"CDKs drive both kinds of division; this does not switch the type.",
       r"replication would still occur."]),
])

QS = [
    Set("A signaling pathway (4.2--4.3)", [
        Q("4.3 Second messenger", r"Which molecule in this pathway acts as a second messenger?",
          r"cyclic AMP", [r"epinephrine", r"glycogen phosphorylase", r"glucose"],
          r"cAMP is a small molecule made inside the cell in response to the signal; it spreads the signal to protein kinase A.",
          [r"First messenger: the hormone. Second messenger: the small internal signal."],
          [r"is the first messenger, the ligand.",
           r"is the enzyme that produces the response.",
           r"is the product released in the response."]),
        Q("4.2 Surface receptor", r"Why does epinephrine bind a receptor on the surface of the liver cell rather than entering the cell?",
          r"It is a hydrophilic molecule that cannot easily cross the hydrophobic interior of the membrane.", [r"It is a steroid hormone.", r"It is too small to stay inside the cell.", r"Liver cells have no cytoplasm."],
          r"Water-soluble signals act through membrane receptors and second messengers.",
          [r"Polar ligand: surface receptor."],
          [r"epinephrine is not a steroid; steroids enter cells.",
           r"size is not the issue; polarity is.",
           r"every cell has cytoplasm."]),
        Q("4.3 Stuck G protein", r"A mutation leaves the G protein permanently active. What is the most likely effect on the liver cell?",
          r"It releases glucose even when no epinephrine is present.", [r"It can no longer release glucose.", r"It releases glucose only when twice as much epinephrine is present.", r"There is no effect, because the receptor is normal."],
          r"Every step after the G protein is switched on regardless of the signal, so the response no longer depends on epinephrine.",
          [r"Downstream components follow the G protein."],
          [r"an active G protein turns the pathway on, not off.",
           r"the pathway no longer needs epinephrine at all.",
           r"the defect is after the receptor, so the receptor's state no longer matters."]),
        Q("4.3 Phosphodiesterase", r"Phosphodiesterase breaks down cAMP. What would a drug that blocks phosphodiesterase do to the cell's response to epinephrine?",
          r"It would prolong and strengthen the response.", [r"It would block the response.", r"It would have no effect.", r"It would make the receptor unable to bind epinephrine."],
          r"cAMP would persist, so protein kinase A would stay active longer.",
          [r"Blocking the ``off switch'' prolongs the signal."],
          [r"cAMP would accumulate, not disappear.",
           r"cAMP levels control the rest of the pathway.",
           r"phosphodiesterase acts downstream of the receptor."]),
        Q("4.2 Specificity", r"Epinephrine reaches nearly every cell in the body, but only some cells respond. Why?",
          r"Only cells with the specific receptor for epinephrine can respond.", [r"Epinephrine is destroyed before reaching most cells.", r"Only liver cells contain glycogen.", r"Cells that do not respond lack a plasma membrane."],
          r"A signal acts only on cells with a matching receptor; different cells can also respond differently to the same signal.",
          [r"Receptor presence decides the target."],
          [r"it circulates in the blood to all tissues.",
           r"muscle cells also store glycogen, and the question concerns any response.",
           r"all cells have a plasma membrane."]),
    ], stim=r"In liver cells, the hormone epinephrine binds a G protein-coupled receptor in the plasma membrane. The activated receptor activates a G protein, which activates the enzyme adenylyl cyclase; adenylyl cyclase converts ATP to cyclic AMP (cAMP). cAMP activates protein kinase A, which begins a phosphorylation cascade that activates glycogen phosphorylase. This enzyme breaks down glycogen, and glucose is released into the blood.",
        stim_title="Questions 1--5"),
    Set("Feedback (4.4)", [
        Q("4.4 Blood glucose", r"After a meal, blood glucose rises; the pancreas releases insulin; liver and muscle cells take up glucose; blood glucose falls. What kind of regulation is this?",
          r"negative feedback that maintains homeostasis", [r"positive feedback that amplifies the change", r"quorum sensing", r"a signal that acts only by direct contact"],
          r"The response (lower glucose) counteracts the stimulus (high glucose), returning it toward the set point.",
          [r"Response opposes the change: negative feedback."],
          [r"positive feedback would raise glucose further.",
           r"quorum sensing is bacterial.",
           r"insulin is an endocrine signal."]),
        Q("4.4 Blood clotting", r"When a blood vessel is damaged, platelets stick to the site and release chemicals that attract more platelets. This is an example of",
          r"positive feedback", [r"negative feedback", r"apoptosis", r"density-dependent inhibition"],
          r"Each platelet recruits more, building the clot rapidly until the wound is sealed.",
          [r"Self-reinforcing until completion."],
          [r"negative feedback would reduce platelet recruitment.",
           r"apoptosis is programmed cell death.",
           r"density-dependent inhibition slows cell division."]),
    ]),
    Set("The cell cycle and its regulation (4.5--4.6)", [
        Q("4.5 DNA content", r"A cell in G$_1$ contains $8$ pg of DNA. How much DNA does it contain in G$_2$, and how much does each daughter cell contain after mitosis and cytokinesis?",
          r"$16$ pg; $8$ pg", [r"$8$ pg; $4$ pg", r"$16$ pg; $16$ pg", r"$16$ pg; $4$ pg"],
          r"S phase doubles the DNA; mitosis divides it equally between two daughter cells, restoring the G$_1$ amount.",
          [r"G$_1$: $1x$. G$_2$: $2x$. Daughter: $1x$."],
          [r"misses the doubling in S phase.",
           r"forgets that the DNA is split between two cells.",
           r"halves twice, as in meiosis."]),
        Q("4.5 Metaphase", r"In which stage of mitosis do the chromosomes line up at the middle of the cell?",
          r"metaphase", [r"prophase", r"anaphase", r"telophase"],
          r"Spindle fibers attached at the centromeres balance each chromosome at the metaphase plate.",
          [r"Metaphase: middle."],
          [r"chromosomes condense and the spindle forms.",
           r"sister chromatids are pulled apart.",
           r"new nuclei form at the poles."]),
        Q("4.5 Time in mitosis", r"In a root tip, a student counts $200$ cells: $160$ in interphase and $40$ in stages of mitosis. The cell cycle in this tissue takes about $20$ hours. About how long does mitosis take?",
          r"$4.0$ hours", [r"$16$ hours", r"$2.0$ hours", r"$5.0$ hours"],
          r"The fraction of cells in a stage estimates the fraction of time spent in it: $40/200 = 0.20$, and $0.20 \times 20 = 4.0$ hours.",
          [r"Fraction of cells $\approx$ fraction of time."],
          [r"is the time in interphase.",
           r"halves the correct fraction.",
           r"divides $200$ by $40$."], sort=True),
        Q("4.6 p53", r"After a cell's DNA is damaged by radiation, the protein p53 accumulates and the cell stops in G$_1$. What is the role of this response?",
          r"to allow time for DNA repair, or trigger apoptosis if the damage cannot be repaired", [r"to speed the cell into S phase so the DNA can be replaced", r"to start meiosis", r"to make the cell divide more often"],
          r"p53 is a tumor suppressor: it prevents damaged DNA from being copied and passed on.",
          [r"Checkpoint at G$_1$: check the DNA before copying it."],
          [r"copying damaged DNA would pass on the damage.",
           r"somatic cells do not switch to meiosis.",
           r"p53 halts division."]),
        Q("4.6 Tumor suppressors", r"Why can a mutation that inactivates both copies of a tumor-suppressor gene contribute to cancer?",
          r"The cell loses a brake that normally stops the cycle, so it may divide without control.", [r"The cell gains a new protein that speeds division.", r"The cell can no longer replicate its DNA.", r"The cell becomes unable to undergo mitosis."],
          r"Tumor-suppressor proteins (such as p53) halt the cycle; losing them removes a control on division.",
          [r"Proto-oncogene: accelerator. Tumor suppressor: brake."],
          [r"describes a gain-of-function mutation in a proto-oncogene.",
           r"replication still occurs.",
           r"mitosis still occurs, without proper control."]),
        Q("4.6 Density-dependent inhibition", r"Normal cells grown in a dish divide until they form a single layer covering the bottom, then stop. Cancer cells keep dividing and pile up. What do the normal cells show?",
          r"density-dependent inhibition", [r"positive feedback", r"apoptosis", r"quorum sensing"],
          r"Contact with crowded neighbors (and shortage of growth factors) signals normal cells to stop dividing; cancer cells ignore these signals.",
          [r"Crowding stops normal division."],
          [r"positive feedback would accelerate division.",
           r"the cells stop dividing; they do not die.",
           r"quorum sensing is bacterial signaling."]),
    ]),
]

UNIT = Unit(4, "cell-communication-cell-cycle", "Cell Communication and Cell Cycle", "10--15\\%", "4.1--4.6",
    abstract=r"""Unit 4 covers how cells signal to one another and how they control division: cell communication over different distances, the reception, transduction and response stages of signaling pathways (with amplification by cascades and second messengers), negative and positive feedback, the phases of the cell cycle and mitosis, and its regulation by checkpoints, cyclins and CDKs, with cancer as the result when that regulation fails. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5], qsections=QS,
    frq=FRQ("Interpreting and Evaluating Experimental Results with Graphing", 9, r"""CDK1 is a cyclin-dependent kinase whose activity is required for a cell to pass from G$_2$ into mitosis. Researchers treated cultured human cells with different concentrations of a drug that inhibits CDK1. After $24$ hours they recorded the percentage of cells in mitosis (mean $\pm 2\,SE_{\bar x}$, $5$ cultures per concentration).

\medskip
\begin{tabular}{@{}cc@{}}\toprule
Drug ($\mu$M) & Cells in mitosis (\%) \\ \midrule
0 & $8.0 \pm 1.0$ \\
1 & $6.2 \pm 1.0$ \\
2 & $4.1 \pm 0.8$ \\
5 & $1.5 \pm 0.6$ \\
10 & $0.5 \pm 0.4$ \\ \bottomrule
\end{tabular}""", [
        Part("A", 1, r"\textbf{Describe} how cyclins and CDKs regulate the progression of a cell through the cell cycle.",
             r"A CDK becomes active only when bound to its cyclin; the active complex phosphorylates target proteins that move the cell past a checkpoint into the next phase (CDK1 with its cyclin triggers entry into mitosis), and cyclin breakdown inactivates the CDK.",
             r"Saying CDKs are always active, or that cyclins are kinases."),
        Part("B", 4, r"\textbf{Construct} an appropriate graph of the data. Your graph should show the mean percentage of cells in mitosis at each drug concentration, with error bars.",
             r"1 pt: axes correctly labeled with units (drug concentration in $\mu$M on the $x$-axis, cells in mitosis in \% on the $y$-axis). 1 pt: appropriate, evenly spaced scales. 1 pt: all five means plotted correctly (points, which may be joined, or bars). 1 pt: error bars of $\pm 2\,SE_{\bar x}$ drawn correctly.",
             r"Uneven scales that place $5$ and $10\ \mu$M next to each other; plotting concentration on the $y$-axis.", fig=MODEL),
        Part("C", 2, r"(i) \textbf{Describe} the relationship between the drug concentration and the percentage of cells in mitosis. (ii) \textbf{Determine} whether the percentage at $2\ \mu$M differs significantly from the percentage with no drug.",
             r"1 pt: as the concentration increases, the percentage of cells in mitosis decreases, steeply at first and then leveling off near zero. 1 pt: yes: the intervals $7.0$--$9.0\%$ and $3.3$--$4.9\%$ do not overlap.",
             r"Describing only one data point; judging significance from the means alone."),
        Part("D", 2, r"\textbf{Predict} how the percentage of cells in G$_2$ at $10\ \mu$M will compare with the percentage in untreated cells, and \textbf{justify} your prediction.",
             r"1 pt: it will be higher (cells accumulate in G$_2$). 1 pt: cells still progress through G$_1$ and S and arrive at G$_2$, but without CDK1 activity they cannot pass the G$_2$ checkpoint into mitosis, so they are held there.",
             r"Predicting fewer cells in G$_2$ because ``the drug stops the cell cycle.''"),
    ], mins=25),
    frq_topic="a CDK inhibitor and mitosis",
)
