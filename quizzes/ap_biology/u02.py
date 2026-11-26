from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph, Series

BAGS = Graph(r"Sucrose concentration in beaker (M)", r"Change in mass (\%)", x=(0, 0.8, 0.2), y=(-15, 15, 5),
             series=[Series("bags", [(0.0, 12), (0.2, 5), (0.4, 0), (0.6, -6), (0.8, -11)])])

S1 = Sec("Cell structure and function (2.1)", ["2.1"], r"""
\begin{compare}{Structure}{Function}{Found in}
Ribosomes & make proteins (free: for the cytosol; bound to rough ER: for membranes, organelles and secretion) & all cells \\
Rough ER & folds and modifies proteins made by its ribosomes & eukaryotes \\
Smooth ER & makes lipids; detoxifies; stores calcium & eukaryotes \\
Golgi complex & modifies, sorts and packages proteins into vesicles & eukaryotes \\
Lysosomes & hydrolytic enzymes digest worn-out parts and engulfed material; role in apoptosis & animal cells \\
Vacuoles & storage; the large central vacuole of plants holds water and keeps the cell turgid & eukaryotes \\
Mitochondria & cellular respiration; folded inner membrane (cristae) & eukaryotes \\
Chloroplasts & photosynthesis; stacked thylakoid membranes & plants and algae \\
\end{compare}
Prokaryotes have no nucleus or membrane-bound organelles, but have ribosomes, a plasma membrane, DNA in a nucleoid region and usually a cell wall. A protein made for secretion follows the path rough ER $\to$ transport vesicle $\to$ Golgi $\to$ secretory vesicle $\to$ plasma membrane.
""", checks=[
    Q("2.1 Secretory cells", r"Cells of the pancreas secrete large amounts of digestive enzymes, which are proteins. Which structures would you expect these cells to have in unusual abundance?",
      r"rough endoplasmic reticulum and Golgi complex", [r"smooth endoplasmic reticulum and lysosomes", r"chloroplasts and a central vacuole", r"a cell wall and a nucleoid"],
      r"Secreted proteins are made by ribosomes on the rough ER, then modified and packaged by the Golgi for export.",
      [r"Rough ER $\to$ Golgi $\to$ vesicles $\to$ exocytosis."],
      [r"smooth ER makes lipids, and lysosomes digest material.",
       r"animal cells have no chloroplasts or central vacuole.",
       r"these are features of plant or prokaryotic cells."]),
])

S2 = Sec("Cell size (2.2)", ["2.2"], r"""
A cell exchanges materials through its surface, but its needs grow with its volume. As a cell grows, volume increases faster than surface area, so the \textbf{surface area-to-volume ratio} falls:
\[ \text{cube of side } s: \quad \frac{SA}{V} = \frac{6s^2}{s^3} = \frac6s ; \qquad \text{sphere: } \frac{SA}{V} = \frac{4\pi r^2}{\tfrac43\pi r^3} = \frac3r . \]
Small cells (or cells with folds, microvilli or flattened shapes) exchange materials and heat more efficiently. Large organisms are made of many small cells rather than a few large ones.
""", checks=[
    Q("2.2 Surface area to volume", r"A cube-shaped cell $1\ \mu$m on a side grows to $2\ \mu$m on a side. By what factor does its surface area-to-volume ratio change?",
      r"It is halved.", [r"It doubles.", r"It is divided by $4$.", r"It is divided by $8$."],
      r"$SA/V = 6/s$: from $6$ to $3\ \mu\mathrm{m}^{-1}$. Surface area grows by $4$ but volume by $8$.",
      [r"$SA$: $6 \to 24\ \mu\mathrm{m}^2$. $V$: $1 \to 8\ \mu\mathrm{m}^3$."],
      [r"the ratio falls as the cell grows.",
       r"is the factor by which surface area grows.",
       r"is the factor by which volume grows."]),
])

S3 = Sec("Plasma membrane and membrane permeability (2.3--2.4)", ["2.3", "2.4"], r"""
The \textbf{fluid mosaic model}: a phospholipid bilayer with embedded and attached proteins that can move laterally. Integral proteins span the membrane (channels, carriers, pumps, receptors); peripheral proteins sit on its surface. Cholesterol in animal membranes moderates fluidity across temperatures; glycoproteins and glycolipids act in cell recognition.

\textbf{Selective permeability.} The hydrophobic interior lets small nonpolar molecules (O$_2$, CO$_2$, N$_2$) diffuse straight through. Small polar molecules such as water cross slowly (faster through aquaporins); ions and large polar molecules (glucose) need transport proteins. Cell walls (plants, fungi, most prokaryotes) are a rigid extra layer that resists bursting.
""", checks=[
    Q("2.4 Permeability", r"Which of these crosses a phospholipid bilayer most easily without a transport protein?",
      r"oxygen ($\mathrm{O_2}$)", [r"a sodium ion ($\mathrm{Na^+}$)", r"glucose", r"a protein"],
      r"Small nonpolar molecules dissolve in the hydrophobic interior of the bilayer and diffuse straight across.",
      [r"Small and nonpolar: crosses freely. Charged or large and polar: needs a protein."],
      [r"charged ions are repelled by the hydrophobic interior.",
       r"glucose is large and polar.",
       r"proteins are far too large and are moved by vesicles."]),
])

S4 = Sec("Membrane transport and facilitated diffusion (2.5--2.6)", ["2.5", "2.6"], r"""
\begin{compare}{Process}{Energy}{Direction and mechanism}
Simple diffusion & none (passive) & down a concentration gradient, straight through the bilayer \\
Facilitated diffusion & none (passive) & down a gradient, through a channel or carrier protein (ions, glucose, water via aquaporins) \\
Active transport & ATP & against a gradient, by a pump; the Na$^+$/K$^+$ ATPase moves $3$ Na$^+$ out and $2$ K$^+$ in per ATP \\
Endocytosis and exocytosis & ATP & bulk transport by vesicles (phagocytosis, secretion) \\
\end{compare}
Passive transport stops when concentrations are equal (dynamic equilibrium); active transport can maintain differences, such as the low Na$^+$ and high K$^+$ inside animal cells that make a membrane potential.
""", checks=[
    Q("2.6 Facilitated diffusion", r"Glucose moves into a muscle cell through a carrier protein, from a higher concentration outside to a lower concentration inside, without using ATP. What kind of transport is this?",
      r"facilitated diffusion", [r"active transport", r"simple diffusion", r"exocytosis"],
      r"Movement is down the concentration gradient (passive) but requires a transport protein.",
      [r"Passive plus protein: facilitated diffusion."],
      [r"active transport moves substances against a gradient using energy.",
       r"glucose cannot cross the bilayer without a protein.",
       r"exocytosis moves material out of the cell in vesicles."]),
])

S5 = Sec("Tonicity and osmoregulation (2.7)", ["2.7"], r"""
\textbf{Osmosis} is the diffusion of water across a selectively permeable membrane, toward the side with the higher solute concentration (lower water potential).

\begin{compare}{Solution outside the cell}{Animal cell}{Plant cell}
Hypotonic (lower solute) & water enters; the cell swells and may lyse & water enters; the cell becomes turgid (firm), the healthy state \\
Isotonic & no net movement & flaccid (limp) \\
Hypertonic (higher solute) & water leaves; the cell shrivels & water leaves; the membrane pulls away from the wall (plasmolysis) \\
\end{compare}

\textbf{Water potential} ($\Psi$, in bars) predicts the direction: water moves from higher $\Psi$ to lower $\Psi$.
\[ \Psi = \Psi_S + \Psi_P, \qquad \Psi_S = -iCRT , \]
with $i$ the ionization constant ($1$ for sucrose, about $2$ for NaCl), $C$ the molar concentration, $R = 0.0831$ L bar/(mol K) and $T$ in kelvins. In an open beaker $\Psi_P = 0$. Freshwater protists pump out excess water with contractile vacuoles.
""", checks=[
    Q("2.7 Solute potential", r"What is the solute potential of a $0.10$ M sucrose solution at $22^\circ$C ($295$ K)?",
      r"$-2.5$ bar", [r"$+2.5$ bar", r"$-0.18$ bar", r"$-4.9$ bar"],
      r"$\Psi_S = -iCRT = -(1)(0.10)(0.0831)(295) = -2.5$ bar.",
      [r"Sucrose does not ionize: $i = 1$."],
      [r"solute potential is negative: solutes lower water potential.",
       r"uses the Celsius temperature.",
       r"uses $i = 2$, as for NaCl."], sort=True),
    Q("2.7 Red blood cells", r"A red blood cell is placed in distilled water. What happens?",
      r"Water enters the cell, which swells and may burst.", [r"Water leaves the cell, which shrivels.", r"Nothing, because the cell is isotonic to distilled water.", r"Solutes enter the cell until the concentrations are equal."],
      r"Distilled water is hypotonic to the cell; with no cell wall, the entering water can lyse it.",
      [r"Water moves toward the higher solute concentration (inside the cell)."],
      [r"that happens in a hypertonic solution.",
       r"the cell contains solutes, so it is hypertonic to distilled water.",
       r"the membrane keeps most solutes in; water is what moves."]),
])

S6 = Sec("Mechanisms of transport (2.8)", ["2.8"], r"""
\textbf{Cotransport} (secondary active transport) uses the energy stored in one gradient to move another substance against its own gradient. For example, the Na$^+$ gradient made by the Na$^+$/K$^+$ pump drives a symporter that carries glucose into intestinal cells along with Na$^+$; in plants, a H$^+$ gradient made by proton pumps drives sucrose uptake. Blocking the pump eventually stops the cotransport, because the gradient runs down.
""", checks=[
    Q("2.8 Cotransport", r"Intestinal cells take in glucose by a Na$^+$/glucose symporter. A drug blocks the Na$^+$/K$^+$ pump in these cells. What happens to glucose uptake over time?",
      r"It decreases, because the Na$^+$ gradient that powers the symporter runs down.", [r"It increases, because more Na$^+$ stays outside the cell.", r"It is unaffected, because the symporter does not use ATP directly.", r"It stops at once, because the symporter itself hydrolyzes ATP."],
      r"Cotransport depends on the Na$^+$ gradient, which only the pump maintains.",
      [r"Pump makes the gradient; the gradient drives the symporter."],
      [r"blocking the pump lets Na$^+$ accumulate inside, so the gradient shrinks.",
       r"it does not use ATP directly, but it depends on a gradient that does.",
       r"the symporter uses the gradient, not ATP; uptake falls as the gradient fades."]),
])

S7 = Sec("Cell compartmentalization and its origins (2.9--2.10)", ["2.9", "2.10"], r"""
Internal membranes divide eukaryotic cells into compartments, so that incompatible reactions (digestion in lysosomes, synthesis in the cytosol) can run at the same time, and enzymes and substrates can be concentrated. Folded membranes (cristae, thylakoids) increase the surface area for reactions.

\textbf{Endosymbiotic theory.} Mitochondria and chloroplasts are descended from free-living prokaryotes engulfed by an ancestral cell. Evidence: they have double membranes, their own circular DNA, ribosomes resembling those of bacteria, and they divide by a process like binary fission.
""", checks=[
    Q("2.10 Endosymbiosis", r"Which observation best supports the hypothesis that mitochondria descended from free-living prokaryotes?",
      r"Mitochondria contain their own circular DNA and ribosomes similar to those of bacteria.", [r"Mitochondria are found in nearly all eukaryotic cells.", r"Mitochondria produce ATP.", r"Mitochondria are surrounded by cytoplasm."],
      r"Prokaryote-like genomes and ribosomes, along with the double membrane and fission-like division, point to a prokaryotic ancestor.",
      [r"Look for features shared with bacteria and not with the rest of the cell."],
      [r"being widespread does not show where they came from.",
       r"many processes make ATP; this says nothing about origin.",
       r"every organelle is surrounded by cytoplasm."]),
])

QS = [
    Set("Organelles and cell size (2.1--2.2)", [
        Q("2.1 Path of a secreted protein", r"Which sequence shows the path of a protein that a cell secretes?",
          r"ribosome on rough ER $\to$ rough ER $\to$ Golgi complex $\to$ vesicle $\to$ plasma membrane", [r"free ribosome $\to$ nucleus $\to$ Golgi complex $\to$ lysosome", r"Golgi complex $\to$ rough ER $\to$ vesicle $\to$ plasma membrane", r"smooth ER $\to$ mitochondrion $\to$ vesicle $\to$ plasma membrane"],
          r"Secreted proteins are made into the rough ER, modified and sorted in the Golgi, and released by exocytosis.",
          [r"The endomembrane system: ER, Golgi, vesicles."],
          [r"free ribosomes make cytosolic proteins, and secreted proteins do not enter the nucleus.",
           r"proteins move from the ER to the Golgi, not the reverse.",
           r"proteins are not made by smooth ER or processed in mitochondria."]),
        Q("2.1 Shared structures", r"Which structure is found in both prokaryotic and eukaryotic cells?",
          r"ribosomes", [r"nucleus", r"mitochondria", r"Golgi complex"],
          r"All cells make proteins, so all have ribosomes; prokaryotes lack membrane-bound organelles.",
          [r"Prokaryotes: no membrane-bound organelles."],
          [r"prokaryotic DNA is in a nucleoid, not a nucleus.",
           r"mitochondria are membrane-bound organelles.",
           r"the Golgi is part of the eukaryotic endomembrane system."]),
        Q("2.2 Most efficient exchange", r"Four cube-shaped cells have sides of $1$, $2$, $3$ and $4\ \mu$m. Which can exchange materials with its surroundings most efficiently relative to its volume?",
          r"the $1\ \mu$m cell", [r"the $2\ \mu$m cell", r"the $3\ \mu$m cell", r"the $4\ \mu$m cell"],
          r"$SA/V = 6/s$ is largest for the smallest cell: $6\ \mu\mathrm{m}^{-1}$.",
          [r"$6/1 > 6/2 > 6/3 > 6/4$."],
          [r"its ratio is $3$, half the smallest cell's.",
           r"its ratio is $2$.",
           r"its ratio is $1.5$, the smallest."]),
        Q("2.2 Root hairs", r"Root hair cells have long, thin extensions into the soil. How does this shape help the plant?",
          r"It increases the surface area for absorbing water and minerals without greatly increasing volume.", [r"It decreases the surface area to reduce water loss.", r"It increases the cell's volume so it can store more water.", r"It anchors the plant but has no effect on absorption."],
          r"Thin projections greatly raise the surface area-to-volume ratio, the same strategy as intestinal microvilli.",
          [r"More membrane surface, more transport proteins, faster uptake."],
          [r"it increases surface area.",
           r"thin projections add surface far faster than volume.",
           r"root hairs are the main site of water and mineral uptake."]),
    ]),
    Set("A dialysis-bag experiment (2.7)", [
        Q("2.7 Gaining mass", r"In which beakers did water move into the bags?",
          r"$0.0$ M and $0.2$ M", [r"$0.6$ M and $0.8$ M", r"$0.4$ M only", r"all five beakers"],
          r"The bags gained mass where the beaker solution was hypotonic to the $0.4$ M sucrose inside.",
          [r"Positive change in mass: net water in."],
          [r"those bags lost mass; water moved out.",
           r"that bag's mass did not change: the solutions were isotonic.",
           r"the bags in hypertonic solutions lost water."]),
        Q("2.7 Losing mass", r"Why did the bag in the $0.8$ M beaker lose mass?",
          r"The solution outside had a lower water potential, so water moved out of the bag by osmosis.", [r"Sucrose moved out of the bag into the beaker.", r"Sucrose moved into the bag from the beaker.", r"The bag's water evaporated."],
          r"The dialysis tubing is impermeable to sucrose but permeable to water; water moved from the higher water potential (inside) to the lower (outside).",
          [r"Higher solute concentration means lower water potential."],
          [r"sucrose is too large to cross this dialysis tubing.",
           r"sucrose entering would make the bag gain mass, and sucrose cannot cross.",
           r"all the bags were submerged; the trend matches concentration, not evaporation."]),
        Q("2.7 Predicting", r"Based on the trend, what change in mass is most likely for a bag in a $1.0$ M sucrose solution?",
          r"about $-16\%$", [r"about $-5\%$", r"about $0\%$", r"about $+16\%$"],
          r"Above $0.4$ M the bags lose about $5$--$6\%$ per $0.2$ M; extending the line from $-11\%$ at $0.8$ M gives roughly $-16\%$.",
          [r"Extend the roughly linear trend one more step."],
          [r"is less loss than at $0.6$ M, against the trend.",
           r"would need the outside solution to be isotonic ($0.4$ M).",
           r"a more concentrated outside solution draws water out, not in."]),
        Q("2.7 Water potential", r"What is the water potential of the $0.2$ M sucrose solution in its open beaker at $295$ K?",
          r"$-4.9$ bar", [r"$+4.9$ bar", r"$-2.5$ bar", r"$-0.37$ bar"],
          r"Open beaker: $\Psi_P = 0$, so $\Psi = \Psi_S = -(1)(0.2)(0.0831)(295) = -4.9$ bar.",
          [r"$\Psi = \Psi_S + \Psi_P$."],
          [r"solute potential is negative.",
           r"is the value for $0.1$ M.",
           r"uses $22$ (degrees Celsius) instead of $295$ K."], sort=True),
        Q("2.7 Variables", r"What is the independent variable in this experiment?",
          r"the sucrose concentration of the solution in the beaker", [r"the percent change in mass of the bags", r"the sucrose concentration inside the bags", r"the time the bags were left in the beakers"],
          r"The students deliberately varied the beaker's concentration and measured the effect on mass.",
          [r"Independent: what is changed. Dependent: what is measured."],
          [r"is the dependent variable.",
           r"was held constant at $0.4$ M.",
           r"was held constant at $30$ minutes."]),
    ], fig=BAGS, stim=r"Students fill five dialysis bags (permeable to water, not to sucrose) with $0.4$ M sucrose, weigh them, and place each in a beaker of sucrose solution of a different concentration. After $30$ minutes they reweigh the bags. The graph shows the percent change in mass.",
        stim_title="Questions 5--9"),
    Set("Membranes and transport (2.3--2.10)", [
        Q("2.5 Sodium--potassium pump", r"Which describes one cycle of the Na$^+$/K$^+$ pump?",
          r"$3$ Na$^+$ pumped out and $2$ K$^+$ pumped in, using one ATP", [r"$3$ Na$^+$ pumped in and $2$ K$^+$ pumped out, using one ATP", r"$2$ Na$^+$ and $2$ K$^+$ moved down their gradients with no ATP", r"$1$ Na$^+$ exchanged for $1$ K$^+$ by facilitated diffusion"],
          r"The pump moves both ions against their gradients, keeping Na$^+$ high outside and K$^+$ high inside.",
          [r"Unequal charge movement helps make the inside negative."],
          [r"reverses the directions.",
           r"the pump works against the gradients and needs ATP.",
           r"the pump is active transport and moves unequal numbers."]),
        Q("2.3 Cholesterol", r"What is the role of cholesterol in animal cell membranes?",
          r"It moderates membrane fluidity, keeping the membrane from becoming too fluid when warm or too rigid when cold.", [r"It forms channels that let ions cross.", r"It stores energy for the cell.", r"It makes the membrane permeable to large polar molecules."],
          r"Cholesterol molecules wedge between phospholipids, restraining their movement at high temperature and preventing tight packing at low temperature.",
          [r"A fluidity buffer."],
          [r"channels are formed by proteins.",
           r"energy storage is the job of fats and glycogen.",
           r"cholesterol does not open the bilayer to large polar molecules."]),
        Q("2.5 Blocking ATP production", r"A poison stops a cell from making ATP. Which process will be directly affected?",
          r"pumping Na$^+$ out of the cell against its gradient", [r"diffusion of O$_2$ into the cell", r"diffusion of CO$_2$ out of the cell", r"osmosis of water through aquaporins"],
          r"Active transport needs ATP; diffusion and osmosis are passive.",
          [r"Only processes against a gradient need ATP directly."],
          [r"simple diffusion needs no energy.",
           r"simple diffusion needs no energy.",
           r"osmosis is passive."]),
        Q("2.7 Plasmolysis", r"A plant cell is placed in a concentrated salt solution. What is observed under the microscope?",
          r"The plasma membrane pulls away from the cell wall as the cell loses water.", [r"The cell bursts.", r"The cell wall dissolves.", r"The central vacuole enlarges."],
          r"In a hypertonic solution water leaves the cell; the protoplast shrinks but the rigid wall keeps its shape (plasmolysis).",
          [r"Hypertonic outside: water out."],
          [r"bursting happens to wall-less cells in hypotonic solutions.",
           r"salt does not dissolve cellulose.",
           r"the vacuole shrinks as water leaves."]),
        Q("2.9 Compartments", r"Lysosomes contain hydrolytic enzymes that work best at pH $5$, while the cytosol is near pH $7$. What advantage does this compartmentalization give the cell?",
          r"Digestion can occur inside lysosomes without damaging other parts of the cell.", [r"It allows the enzymes to work fastest in the cytosol.", r"It lets the cell make ATP inside lysosomes.", r"It prevents the cell from digesting anything."],
          r"Enzymes that escape into the neutral cytosol are much less active, protecting the cell; inside the acidic lysosome they work well.",
          [r"Separate compartments allow incompatible conditions to coexist."],
          [r"the enzymes are adapted to the acidic lysosome, not the neutral cytosol.",
           r"ATP is made in mitochondria (and the cytosol), not lysosomes.",
           r"lysosomes do digest material, safely contained."]),
    ]),
]

UNIT = Unit(2, "cells", "Cells", "10--13\\%", "2.1--2.10",
    abstract=r"""Unit 2 covers how cells are built and how they control what crosses their boundaries: organelles and the endomembrane system, cell size and the surface area-to-volume ratio, the fluid mosaic model and selective permeability, passive and active transport, osmosis, tonicity and water potential, cotransport, and the evidence that compartments and organelles arose by endosymbiosis. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6, S7], qsections=QS,
    frq=FRQ("Interpreting and Evaluating Experimental Results", 9, r"""Students cut cylinders (cores) of the same size from one potato. They weighed groups of five cores and placed each group in a beaker of sucrose solution of a different concentration at $22^\circ$C. After $24$ hours they blotted and reweighed the cores. The table shows the mean percent change in mass ($\pm 2\,SE_{\bar x}$).

\medskip
\begin{tabular}{@{}cc@{}}\toprule
Sucrose (M) & Change in mass (\%) \\ \midrule
0.0 & $+18 \pm 2$ \\
0.2 & $+7 \pm 2$ \\
0.4 & $-3 \pm 2$ \\
0.6 & $-12 \pm 3$ \\
0.8 & $-20 \pm 3$ \\
1.0 & $-24 \pm 3$ \\ \bottomrule
\end{tabular}""", [
        Part("A", 1, r"\textbf{Describe} the movement of water when a potato core is placed in a hypotonic solution.",
             r"Water moves by osmosis into the potato cells, from the solution (higher water potential) to the cells (lower water potential).",
             r"Saying solutes move into the cells."),
        Part("B", 3, r"(i) \textbf{Identify} the dependent variable. (ii) \textbf{Explain} why the students recorded the percent change in mass rather than the change in mass in grams. (iii) \textbf{Identify} one variable that should be held constant.",
             r"1 pt: the percent change in mass of the cores. 1 pt: the cores did not all start with exactly the same mass, so the percent change lets results be compared fairly. 1 pt: any one of temperature, time in solution, core size or surface area, source of the potato, volume of solution.",
             r"Naming the sucrose concentration (the independent variable) in (i)."),
        Part("C", 3, r"(i) Using the data, \textbf{estimate} the sucrose concentration that is isotonic to the potato cells. (ii) \textbf{Calculate} the solute potential of a sucrose solution of that concentration at $22^\circ$C ($295$ K), using $\Psi_S = -iCRT$ with $R = 0.0831$ L bar/(mol K). (iii) \textbf{Determine} whether the mean changes in mass at $0.6$ M and $0.8$ M are significantly different.",
             r"1 pt: about $0.34$ M (between $0.2$ and $0.4$ M, where the change in mass would be zero; accept $0.3$--$0.4$ M). 1 pt: $\Psi_S = -(1)(0.34)(0.0831)(295) \approx -8.3$ bar (consistent with the estimate in (i)). 1 pt: yes: the intervals $-15$ to $-9\%$ and $-23$ to $-17\%$ do not overlap.",
             r"Using $22$ for $T$; claiming significance from the means alone without the error bars."),
        Part("D", 2, r"The students boil a new set of cores for $10$ minutes, which destroys their membranes, and then repeat the $1.0$ M trial. \textbf{Predict} how the percent change in mass will compare with $-24\%$, and \textbf{justify} your prediction.",
             r"1 pt: the boiled cores will lose much less mass (a change much closer to zero). 1 pt: with the membranes destroyed, the cells are no longer selectively permeable; sucrose can enter as freely as water moves, so no osmotic gradient holds and little net water leaves.",
             r"Predicting more loss because ``boiling removes water.''"),
    ], mins=25),
    frq_topic="potato cores in sucrose solutions",
)
