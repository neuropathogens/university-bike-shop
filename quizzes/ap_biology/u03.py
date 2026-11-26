import math

from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part
from ap_sci.figs import Graph


def bell(peak, center, width):
    return lambda t: peak * math.exp(-((t - center) / width) ** 2) if t <= center else peak * math.exp(-((t - center) / (width * 0.45)) ** 2)


TEMP = Graph(r"Temperature ($^\circ$C)", r"Reaction rate (relative units)", x=(0, 100, 10), y=(0, 120, 20), series=[],
             curves=[("enzyme A", bell(90, 37, 16), 0), ("enzyme B", bell(80, 75, 20), 1)], legend_pos="ne")


def energy(barrier):
    return lambda t: 80 - 50 / (1 + math.exp(-(t - 5) * 1.6)) + barrier * math.exp(-((t - 5) / 1.1) ** 2)


ENERGY = Graph(r"Progress of the reaction", r"Free energy (kJ/mol)", x=(0, 10, 1), y=(0, 200, 40), series=[], xticks=[],
               curves=[("without enzyme", energy(125), 0), ("with enzyme", energy(65), 1)])

S1 = Sec("Enzymes (3.1)", ["3.1"], r"""
Enzymes are biological catalysts, almost all proteins. An enzyme speeds a reaction by lowering its \textbf{activation energy}, the energy needed to reach the unstable transition state. It does not change the free energy of the reactants or products, so it does not change $\Delta G$ or which direction is favored, and it is not used up.

\begin{terms}
Active site & a pocket whose shape and chemical character (from its R groups) fit a specific substrate \\
Induced fit & binding changes the active site's shape slightly, straining the substrate's bonds or bringing reactants together \\
Specificity & a change in the active site's shape or charge, by mutation or by conditions, can prevent binding \\
\end{terms}
""", checks=[
    Q("3.1 How enzymes work", r"How does an enzyme increase the rate of a reaction?",
      r"by lowering the activation energy of the reaction", [r"by making the reaction release more free energy", r"by raising the temperature of the reactants", r"by changing the reaction from endergonic to exergonic"],
      r"Binding in the active site stabilizes the transition state, so less energy is needed to reach it; $\Delta G$ is unchanged.",
      [r"Same start and end energies; a lower hill between them."],
      [r"$\Delta G$ depends only on reactants and products.",
       r"enzymes work at the cell's temperature.",
       r"an enzyme cannot change $\Delta G$."]),
])

S2 = Sec("Environmental impacts on enzyme function (3.2)", ["3.2"], r"""
\begin{compare}{Factor}{Effect on rate}{Why}
Temperature & rises to an optimum, then falls sharply & faster collisions at first; above the optimum the enzyme denatures \\
pH & greatest at an optimum pH & H$^+$ concentration changes the charges of R groups and so the active site's shape \\
Substrate concentration & rises, then levels off & at high concentration every active site is occupied (saturation) \\
Competitive inhibitor & lowers the rate; overcome by more substrate & competes for the active site \\
Noncompetitive (allosteric) inhibitor & lowers the maximum rate; not overcome by more substrate & binds elsewhere and changes the active site's shape \\
\end{compare}

Many enzymes need \textbf{cofactors} (metal ions) or \textbf{coenzymes} (organic molecules such as vitamins). In \textbf{feedback inhibition}, the end product of a pathway inhibits an early enzyme allosterically, so the cell makes only as much product as it needs.
""", checks=[
    Q("3.2 Competitive inhibition", r"A drug slows an enzyme-catalyzed reaction, but adding more substrate restores the original maximum rate. What kind of inhibitor is the drug?",
      r"a competitive inhibitor that binds the active site", [r"a noncompetitive inhibitor that binds an allosteric site", r"a denaturing agent that unfolds the enzyme", r"a cofactor that the enzyme requires"],
      r"Enough substrate outcompetes a competitive inhibitor for the active site.",
      [r"Overcome by substrate: competitive."],
      [r"more substrate cannot reverse a shape change caused at another site.",
       r"a denatured enzyme stays inactive whatever the substrate concentration.",
       r"a cofactor would increase the rate, not slow it."]),
])

S3 = Sec("Cellular energy (3.3)", ["3.3"], r"""
Cells must constantly take in energy to maintain order (the second law of thermodynamics). Reactions that release free energy are \textbf{exergonic} ($\Delta G < 0$); those that need an input are \textbf{endergonic} ($\Delta G > 0$).

\textbf{Energy coupling.} Cells drive endergonic reactions by coupling them to exergonic ones, usually the hydrolysis of ATP to ADP and phosphate. Often the phosphate is transferred to a reactant or protein (phosphorylation), making the next step favorable. Pathways are sequences of steps, each catalyzed by its own enzyme, with the product of one step the substrate of the next.
""", checks=[
    Q("3.3 Energy coupling", r"An endergonic reaction in a cell is made to proceed. Which is the most likely way the cell does this?",
      r"It couples the reaction to the hydrolysis of ATP.", [r"It adds an enzyme, which supplies the needed energy.", r"It lowers the cell's temperature.", r"It reverses the second law of thermodynamics."],
      r"The free energy released by ATP hydrolysis, often through phosphorylation of a reactant, makes the overall coupled process exergonic.",
      [r"Coupled $\Delta G$ = sum of the two; it must be negative."],
      [r"enzymes lower activation energy but supply no energy.",
       r"cooling slows reactions and supplies no energy.",
       r"the second law always holds; the cell pays for order with energy."]),
])

S4 = Sec("Photosynthesis (3.4)", ["3.4"], r"""
\[ 6\,\mathrm{CO_2} + 6\,\mathrm{H_2O} \xrightarrow{\text{light}} \mathrm{C_6H_{12}O_6} + 6\,\mathrm{O_2} \]

\begin{compare}{Stage}{Where}{What happens}
Light-dependent reactions & thylakoid membranes & chlorophyll in photosystems II and I absorbs light and excites electrons; water is split, releasing O$_2$; electrons pass along an electron transport chain that pumps H$^+$ into the thylakoid space; H$^+$ flows back through ATP synthase, making ATP (chemiosmosis); electrons end up reducing NADP$^+$ to NADPH \\
Calvin cycle & stroma & the enzyme rubisco fixes CO$_2$ to an organic molecule; ATP and NADPH from the light reactions reduce it to the sugar G3P, used to build glucose and other molecules \\
\end{compare}

Photosynthesis evolved in prokaryotes (cyanobacteria); its O$_2$ changed Earth's atmosphere and made aerobic respiration possible.
""", checks=[
    Q("3.4 Source of oxygen", r"A plant is given water containing the heavy oxygen isotope ${}^{18}\mathrm{O}$ and normal CO$_2$. Where will the ${}^{18}\mathrm{O}$ appear?",
      r"in the O$_2$ released by the plant", [r"in the glucose made by the plant", r"in the CO$_2$ taken in by the plant", r"nowhere; it stays in the water"],
      r"Water is split in the light reactions of photosystem II, and its oxygen atoms are released as O$_2$.",
      [r"The O$_2$ of photosynthesis comes from water, not CO$_2$."],
      [r"the oxygen in glucose comes from CO$_2$.",
       r"the plant takes in CO$_2$; it does not make it from this water.",
       r"water's oxygen is released in the light reactions."]),
])

S5 = Sec("Cellular respiration (3.5)", ["3.5"], r"""
\[ \mathrm{C_6H_{12}O_6} + 6\,\mathrm{O_2} \to 6\,\mathrm{CO_2} + 6\,\mathrm{H_2O} + \text{energy (ATP and heat)} \]

\begin{compare}{Stage}{Where}{Products}
Glycolysis & cytosol & glucose split into 2 pyruvate; net 2 ATP and 2 NADH \\
Pyruvate oxidation and Krebs cycle & mitochondrial matrix & CO$_2$ released; NADH, FADH$_2$ and a little ATP \\
Electron transport chain and oxidative phosphorylation & inner mitochondrial membrane & electrons from NADH and FADH$_2$ pass along carriers to O$_2$ (the final acceptor), forming water; the energy pumps H$^+$ into the intermembrane space; H$^+$ flowing back through ATP synthase makes most of the ATP \\
\end{compare}

\textbf{Without oxygen}, the electron transport chain stops and NAD$^+$ runs out. \textbf{Fermentation} (lactic acid in muscle, ethanol and CO$_2$ in yeast) regenerates NAD$^+$ so glycolysis can continue, yielding only 2 ATP per glucose.

\begin{trap}
In both organelles ATP synthase is driven by a H$^+$ gradient, but the gradients point opposite ways relative to the organelle: in mitochondria H$^+$ is pumped out of the matrix into the intermembrane space; in chloroplasts, into the thylakoid space.
\end{trap}
""", checks=[
    Q("3.5 Final electron acceptor", r"What is the final electron acceptor of the electron transport chain in aerobic respiration?",
      r"oxygen", [r"NAD$^+$", r"carbon dioxide", r"pyruvate"],
      r"O$_2$ accepts electrons (and H$^+$) at the end of the chain, forming water.",
      [r"No O$_2$: the chain backs up and stops."],
      [r"NAD$^+$ accepts electrons earlier, in glycolysis and the Krebs cycle.",
       r"CO$_2$ is a waste product, not an acceptor.",
       r"pyruvate accepts electrons only in fermentation."]),
    Q("3.5 Cyanide", r"Cyanide blocks the last protein of the electron transport chain. What happens in a cell exposed to cyanide?",
      r"O$_2$ use and oxidative phosphorylation stop, and the cell must rely on glycolysis for ATP.", [r"ATP production increases, because more electrons build up.", r"Glycolysis stops, but oxidative phosphorylation continues.", r"Only the Krebs cycle is affected."],
      r"With the chain blocked, no H$^+$ gradient is made, so ATP synthase stops; NADH accumulates, slowing the Krebs cycle too, and only glycolysis (with fermentation) still makes ATP.",
      [r"Blocked chain: no gradient, no oxidative phosphorylation."],
      [r"electrons backing up cannot pump protons.",
       r"glycolysis is the one pathway that continues.",
       r"blocking the chain stops the gradient and hence ATP synthase."]),
])

QS = [
    Set("Temperature and enzyme activity (3.1--3.2)", [
        Q("3.2 Optimum", r"What is the optimum temperature of enzyme A?",
          r"about $37^\circ$C", [r"about $20^\circ$C", r"about $50^\circ$C", r"about $75^\circ$C"],
          r"Enzyme A's rate peaks near $37^\circ$C, normal human body temperature.",
          [r"Optimum: the temperature of the highest rate."],
          [r"the rate is still rising there.",
           r"enzyme A is already denaturing there.",
           r"is enzyme B's optimum."]),
        Q("3.2 Above the optimum", r"Why does the activity of enzyme A fall steeply above about $45^\circ$C?",
          r"The enzyme denatures: weak bonds holding its shape break, changing the active site.", [r"The substrate molecules move too slowly to collide.", r"The enzyme is used up in the reaction.", r"The products of the reaction break down."],
          r"High temperature disrupts the hydrogen bonds and other interactions that hold the protein's shape.",
          [r"Rising speed cannot help a misshapen active site."],
          [r"molecules move faster, not slower, at higher temperatures.",
           r"enzymes are not consumed.",
           r"the drop reflects the enzyme, not the products."]),
        Q("3.2 Below the optimum", r"Why is enzyme A's rate lower at $20^\circ$C than at $37^\circ$C?",
          r"Molecules move more slowly, so enzyme and substrate collide less often.", [r"The enzyme is denatured at $20^\circ$C.", r"The enzyme's active site is permanently damaged by cold.", r"The enzyme has a different amino acid sequence at $20^\circ$C."],
          r"At lower temperatures there are fewer collisions with enough energy; warming the enzyme restores its activity.",
          [r"Cold slows; heat denatures."],
          [r"cold slows enzymes without unfolding them.",
           r"the effect is reversible on warming.",
           r"the sequence is set by the gene."]),
        Q("3.2 Enzyme B", r"Enzyme B most likely comes from",
          r"a bacterium that lives in hot springs", [r"a human liver cell", r"a fish from polar waters", r"a plant growing in a temperate forest"],
          r"Its optimum near $75^\circ$C suits an organism living at high temperatures.",
          [r"Enzymes are adapted to their organism's environment."],
          [r"human enzymes work best near $37^\circ$C.",
           r"enzymes of cold-water fish have low optima.",
           r"temperate plants live far below $75^\circ$C."]),
    ], fig=TEMP, stim=r"The graph shows the rate of the same reaction catalyzed by two different enzymes, A and B, at different temperatures (at the same pH and substrate concentration).",
        stim_title="Questions 1--4"),
    Set("Regulation and energy (3.2--3.3)", [
        Q("3.2 Noncompetitive inhibition", r"An inhibitor binds to an enzyme at a site other than the active site. Which describes its effect?",
          r"It changes the shape of the active site, and adding more substrate does not restore the maximum rate.", [r"It blocks the active site, but more substrate overcomes it.", r"It increases the enzyme's affinity for its substrate.", r"It has no effect, because it does not bind the active site."],
          r"An allosteric (noncompetitive) inhibitor alters the enzyme's shape, reducing activity whatever the substrate concentration.",
          [r"Binding elsewhere, effect everywhere."],
          [r"describes a competitive inhibitor.",
           r"an inhibitor lowers activity.",
           r"binding at another site can still change the active site."]),
        Q("3.2 Feedback inhibition", r"In a pathway $A \to B \to C \to D$, product $D$ binds to the enzyme that converts $A$ to $B$ and inhibits it. What is the benefit to the cell?",
          r"It stops making $D$ when $D$ is plentiful, saving resources.", [r"It speeds the pathway when $D$ is plentiful.", r"It destroys excess $D$.", r"It converts $D$ back into $A$."],
          r"Feedback inhibition matches production to need: high $D$ shuts the first step, and low $D$ releases it.",
          [r"Negative feedback on the first committed step."],
          [r"it slows the pathway.",
           r"inhibition does not break $D$ down.",
           r"the pathway does not run backward."]),
        Q("3.3 Free energy", r"An enzyme catalyzes an exergonic reaction. Which is true?",
          r"The reaction releases free energy, and the enzyme does not change how much.", [r"The reaction requires free energy, which the enzyme supplies.", r"The enzyme makes the reaction release more free energy.", r"The reaction cannot occur without ATP."],
          r"Exergonic means $\Delta G < 0$; the enzyme lowers activation energy but leaves $\Delta G$ unchanged.",
          [r"Enzymes change rates, not energies of reactants and products."],
          [r"describes an endergonic reaction.",
           r"enzymes do not change $\Delta G$.",
           r"exergonic reactions release energy; they do not need ATP."]),
    ]),
    Set("Photosynthesis and respiration (3.4--3.5)", [
        Q("3.4 Light and the Calvin cycle", r"A plant that has been in bright light is moved into darkness. What happens to the Calvin cycle?",
          r"It soon stops, because the light reactions stop supplying ATP and NADPH.", [r"It continues indefinitely, because it does not need light.", r"It speeds up, because it is the ``dark reactions.''", r"It reverses and releases CO$_2$."],
          r"The Calvin cycle needs no light directly, but it consumes ATP and NADPH made only in the light.",
          [r"Light reactions supply the energy carriers the Calvin cycle uses."],
          [r"its supply of ATP and NADPH runs out.",
           r"``light-independent'' does not mean it works best in the dark.",
           r"it does not run backward."]),
        Q("3.5 Proton gradient", r"In a mitochondrion, where is the H$^+$ concentration highest while the electron transport chain is working?",
          r"in the intermembrane space", [r"in the matrix", r"in the cytosol", r"in the thylakoid space"],
          r"The chain pumps H$^+$ from the matrix into the intermembrane space; H$^+$ flows back into the matrix through ATP synthase.",
          [r"Pumped out of the matrix; returns through ATP synthase."],
          [r"the matrix is where the H$^+$ is pumped from.",
           r"the outer membrane lets small ions through, but the gradient is across the inner membrane.",
           r"thylakoids are in chloroplasts."]),
        Q("3.5 Fermentation", r"What is the main function of fermentation for a cell without oxygen?",
          r"to regenerate NAD$^+$ so glycolysis can keep making ATP", [r"to make large amounts of ATP", r"to produce oxygen", r"to run the electron transport chain"],
          r"Glycolysis needs NAD$^+$; fermentation passes electrons from NADH to pyruvate (or a product of it), freeing NAD$^+$.",
          [r"Fermentation itself makes no ATP."],
          [r"fermentation yields only the 2 ATP of glycolysis.",
           r"no fermentation pathway makes oxygen.",
           r"without oxygen the chain cannot run."]),
        Q("3.5 An uncoupler", r"The chemical DNP makes the inner mitochondrial membrane leaky to H$^+$. What happens in cells treated with DNP?",
          r"O$_2$ use continues but ATP synthesis falls, and more energy is released as heat.", [r"O$_2$ use stops and ATP synthesis rises.", r"Glycolysis stops at once.", r"ATP synthase pumps H$^+$ faster."],
          r"Electron transport still runs and uses O$_2$, but H$^+$ leaks back without passing through ATP synthase, so the energy becomes heat instead of ATP.",
          [r"Gradient dissipated: transport continues, coupling lost."],
          [r"the electron transport chain is not blocked.",
           r"glycolysis does not need the proton gradient.",
           r"ATP synthase is driven by the gradient, which is lost."]),
        Q("3.5 Locations", r"In a eukaryotic cell, where do glycolysis, the Krebs cycle and the electron transport chain take place?",
          r"cytosol; mitochondrial matrix; inner mitochondrial membrane", [r"mitochondrial matrix; cytosol; outer mitochondrial membrane", r"cytosol; inner mitochondrial membrane; mitochondrial matrix", r"chloroplast stroma; mitochondrial matrix; thylakoid membrane"],
          r"Glycolysis needs no organelle; the Krebs cycle enzymes are in the matrix; the chain's carriers are embedded in the inner membrane.",
          [r"Cristae fold the inner membrane to hold more chains."],
          [r"swaps the first two and misplaces the chain.",
           r"swaps the Krebs cycle and the chain.",
           r"mixes in photosynthetic locations."]),
        Q("3.4 Chemiosmosis", r"Which feature do photosynthesis and cellular respiration share?",
          r"ATP synthase uses the energy of a H$^+$ gradient across a membrane to make ATP.", [r"Both release O$_2$.", r"Both take place in the mitochondria.", r"Both use rubisco to fix CO$_2$."],
          r"Chemiosmosis makes most of the ATP in both chloroplasts (thylakoid membrane) and mitochondria (inner membrane).",
          [r"Electron transport $\to$ H$^+$ gradient $\to$ ATP synthase."],
          [r"respiration consumes O$_2$.",
           r"photosynthesis takes place in chloroplasts.",
           r"rubisco works only in the Calvin cycle."]),
    ]),
]

UNIT = Unit(3, "cellular-energetics", "Cellular Energetics", "12--16\\%", "3.1--3.5",
    abstract=r"""Unit 3 covers how cells capture and use energy: enzyme structure and catalysis, the effects of temperature, pH, substrate and inhibitors on enzyme activity, free energy and energy coupling with ATP, photosynthesis (the light reactions and the Calvin cycle) and cellular respiration (glycolysis, the Krebs cycle, oxidative phosphorylation) and fermentation. Both photosynthesis and respiration make most of their ATP by chemiosmosis. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5], qsections=QS,
    frq=FRQ("Analyze Model or Visual Representation", 4, r"""The model shows the free energy of the reactants and products of a reaction in a cell, and the energy of the transition state, when the reaction occurs without an enzyme and with the enzyme that catalyzes it in the cell. The reactants have a free energy of about $80$ kJ/mol and the products about $30$ kJ/mol.

[[fig]]""", [
        Part("A", 1, r"\textbf{Describe} the difference between the two curves in the model.",
             r"The peak (transition state) is lower with the enzyme: the activation energy is lower (about $40$ instead of about $100$ kJ/mol), while the energies of the reactants and products are the same.",
             r"Saying the enzyme changes the energy of the products."),
        Part("B", 1, r"\textbf{Explain} how binding to the enzyme produces the difference you described in part A.",
             r"Binding of the substrate in the active site (induced fit) strains the substrate's bonds, orients reactants correctly, or provides a favorable chemical environment, stabilizing the transition state so less energy is needed to reach it.",
             r"Saying the enzyme supplies energy to the reaction."),
        Part("C", 1, r"Using the model, \textbf{represent} the change in free energy ($\Delta G$) for the reaction by stating its value and sign, and \textbf{identify} whether the reaction is exergonic or endergonic.",
             r"$\Delta G \approx 30 - 80 = -50$ kJ/mol: negative, so the reaction is exergonic (and the value is the same with or without the enzyme).",
             r"Using the height of a peak to find $\Delta G$."),
        Part("D", 1, r"Cells commonly couple reactions like this one to endergonic reactions. \textbf{Explain} how coupling allows an endergonic reaction to occur in a cell.",
             r"If the free energy released by the exergonic reaction (for example ATP hydrolysis, often through phosphorylation of a reactant) exceeds the free energy the endergonic reaction requires, the coupled process has an overall negative $\Delta G$ and proceeds.",
             r"Saying the enzyme provides the energy for the endergonic reaction."),
    ], mins=10, fig=ENERGY),
    frq_topic="an energy diagram for a catalyzed reaction",
)
