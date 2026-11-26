from ap_sci.model import Q, Sec, Set, Unit, FRQ, Part

S1 = Sec("Structure of water and hydrogen bonding (1.1)", ["1.1"], r"""
A water molecule is \textbf{polar}: oxygen pulls the shared electrons toward itself, so the oxygen end is partly negative and the hydrogen ends partly positive. The partly positive hydrogen of one molecule is attracted to the partly negative oxygen of a neighbor: a \textbf{hydrogen bond}. Each bond is weak, but there are enormous numbers of them, and they explain water's unusual properties.

\begin{compare}{Property}{Cause}{Biological importance}
Cohesion and surface tension & hydrogen bonds between water molecules & water columns pulled up through xylem; insects walk on water \\
Adhesion & hydrogen bonds between water and other polar surfaces & capillary action in narrow tubes and soil \\
High specific heat & energy goes into breaking hydrogen bonds before temperature rises & stable body and ocean temperatures \\
High heat of vaporization & hydrogen bonds must break for a molecule to escape & evaporative cooling (sweating, transpiration) \\
Ice less dense than liquid & hydrogen bonds lock molecules into an open lattice & ice floats and insulates the water below \\
Solvent & polar and charged solutes are surrounded by water molecules & the medium for nearly all cell chemistry \\
\end{compare}
""", checks=[
    Q("1.1 Cohesion", r"Water can be pulled up through the narrow xylem vessels of a tall tree as an unbroken column. Which property of water most directly allows this?",
      r"cohesion, from hydrogen bonds between water molecules", [r"its high specific heat", r"its low density as a solid", r"its nonpolar covalent bonds"],
      r"Hydrogen bonds hold water molecules to each other, so the column is pulled up as a whole as water evaporates from the leaves (aided by adhesion to the vessel walls).",
      [r"Transpiration pulls; cohesion keeps the column together."],
      [r"specific heat affects temperature change, not the continuity of the column.",
       r"the density of ice is unrelated to transport in xylem.",
       r"water's O--H bonds are polar, which is what makes hydrogen bonding possible."]),
])

S2 = Sec("Elements of life (1.2)", ["1.2"], r"""
Living things are built mostly from carbon, hydrogen, oxygen, nitrogen, phosphorus and sulfur. Organisms take these elements from their environment and use them to build macromolecules; the atoms cycle between organisms and the environment.

\begin{terms}
Carbon & forms four covalent bonds; the backbone of every macromolecule \\
Nitrogen & in amino acids (proteins) and nitrogenous bases (nucleic acids) \\
Phosphorus & in nucleic acids (the phosphate of each nucleotide) and in phospholipids and ATP \\
Sulfur & in the amino acids cysteine and methionine (disulfide bridges in proteins) \\
\end{terms}

\begin{trap}
Carbohydrates and most lipids contain only C, H and O. A cell that runs short of nitrogen cannot make proteins or nucleic acids; one short of phosphorus cannot make DNA, RNA, ATP or membranes.
\end{trap}
""", checks=[
    Q("1.2 Elements", r"A bacterium is grown in a medium that lacks phosphorus. Which molecule will it be unable to make?",
      r"DNA", [r"glucose", r"starch", r"a saturated fatty acid"],
      r"Every nucleotide contains a phosphate group, so DNA (and RNA, ATP and phospholipids) needs phosphorus.",
      [r"Carbohydrates and fatty acids contain only carbon, hydrogen and oxygen."],
      [r"glucose contains only C, H and O.",
       r"starch is a polymer of glucose.",
       r"fatty acids contain only C, H and O."]),
])

S3 = Sec("Introduction to macromolecules (1.3)", ["1.3"], r"""
Macromolecules are polymers built from monomers joined by covalent bonds.

\begin{keyidea}[Building and breaking polymers]
\textbf{Dehydration synthesis} joins two monomers by removing a water molecule (an $-$OH from one, an $-$H from the other). \textbf{Hydrolysis} breaks the bond by adding water back. A polymer of $n$ monomers is made by $n - 1$ dehydration reactions and broken down by $n - 1$ hydrolysis reactions.
\end{keyidea}

\begin{compare}{Macromolecule}{Monomer}{Bond between monomers}
Carbohydrates & monosaccharides & glycosidic \\
Proteins & amino acids & peptide \\
Nucleic acids & nucleotides & phosphodiester \\
Lipids & (not true polymers) fatty acids and glycerol & ester \\
\end{compare}
""", checks=[
    Q("1.3 Hydrolysis", r"How many water molecules are used in completely hydrolyzing a polysaccharide made of $10$ glucose monomers into free glucose?",
      r"$9$", [r"$10$", r"$11$", r"$20$"],
      r"A chain of $10$ monomers has $9$ glycosidic bonds; each hydrolysis uses one water molecule.",
      [r"$n$ monomers, $n - 1$ bonds."],
      [r"counts monomers rather than bonds.",
       r"adds an extra bond that does not exist.",
       r"counts two water molecules per bond."]),
])

S4 = Sec("Carbohydrates (1.4)", ["1.4"], r"""
\textbf{Monosaccharides} (glucose, fructose, ribose) are the monomers; two joined by a glycosidic bond form a disaccharide (sucrose, lactose); many form a \textbf{polysaccharide}. The kind of linkage and branching decide the function:

\begin{compare}{Polysaccharide}{Structure}{Function}
Starch & glucose in $\alpha$ linkages, helical, some branching & energy storage in plants \\
Glycogen & glucose in $\alpha$ linkages, highly branched & energy storage in animals (liver, muscle) \\
Cellulose & glucose in $\beta$ linkages, straight chains that hydrogen-bond into fibers & plant cell walls; most animals cannot digest it \\
Chitin & modified glucose with nitrogen-containing groups & fungal cell walls, arthropod exoskeletons \\
\end{compare}
""", checks=[
    Q("1.4 Starch vs. cellulose", r"Starch and cellulose are both polymers of glucose, yet humans can digest starch but not cellulose. Why?",
      r"The glucose monomers are joined by different linkages, and humans lack an enzyme that hydrolyzes the linkages in cellulose.", [r"Cellulose contains nitrogen, which humans cannot digest.", r"Starch is a protein and cellulose is a carbohydrate.", r"Cellulose molecules are made of fructose, not glucose."],
      r"Enzymes are specific to the shape of their substrate; the $\beta$ linkages of cellulose do not fit human digestive enzymes, which break the $\alpha$ linkages of starch.",
      [r"Same monomer, different bond orientation, different enzyme needed."],
      [r"cellulose contains only C, H and O; chitin is the one with nitrogen.",
       r"both are carbohydrates.",
       r"both are made of glucose."]),
])

S5 = Sec("Lipids (1.5)", ["1.5"], r"""
Lipids are nonpolar (hydrophobic) molecules, not built as true polymers.
\begin{terms}
Triglycerides (fats and oils) & glycerol plus three fatty acids; long-term energy storage and insulation \\
Saturated fatty acids & no C=C double bonds; straight chains pack tightly, so fats are solid at room temperature \\
Unsaturated fatty acids & one or more C=C double bonds; cis double bonds kink the chain, which keeps oils liquid \\
Phospholipids & glycerol, two fatty acid tails and a phosphate head: amphipathic, with a hydrophilic head and hydrophobic tails, so they form bilayers in water \\
Steroids & four fused carbon rings; cholesterol (membrane fluidity), steroid hormones \\
\end{terms}
""", checks=[
    Q("1.5 Phospholipids", r"Phospholipids placed in water spontaneously form a bilayer. Which best explains why?",
      r"Their hydrophilic phosphate heads face the water while their hydrophobic fatty acid tails face each other, away from the water.", [r"Their hydrophobic heads face the water and their hydrophilic tails face each other.", r"Covalent bonds form between the tails of neighboring phospholipids.", r"They are entirely nonpolar, so they clump together away from the water."],
      r"Phospholipids are amphipathic; the arrangement that keeps polar heads in water and nonpolar tails out of it is a bilayer.",
      [r"Hydrophilic: water-loving. Hydrophobic: water-fearing."],
      [r"reverses which end is hydrophilic.",
       r"the bilayer is held by hydrophobic interactions, not covalent bonds between molecules.",
       r"the phosphate head is polar and charged."]),
])

S6 = Sec("Nucleic acids (1.6)", ["1.6"], r"""
A \textbf{nucleotide} has a five-carbon sugar, a phosphate group and a nitrogenous base. Phosphodiester bonds link the phosphate of one nucleotide to the sugar of the next, giving each strand a sugar--phosphate backbone with a $5'$ end and a $3'$ end.

\begin{compare}{Feature}{DNA}{RNA}
Sugar & deoxyribose & ribose \\
Bases & A, T, G, C & A, U, G, C \\
Structure & two antiparallel strands in a double helix; A pairs with T, G with C by hydrogen bonds & usually single-stranded \\
\end{compare}

\textbf{Base pairing} makes the two strands complementary: in double-stranded DNA the amount of A equals T and G equals C (Chargaff's rules). G--C pairs have three hydrogen bonds and A--T pairs two.
""", checks=[
    Q("1.6 Chargaff's rules", r"A sample of double-stranded DNA is $30\%$ adenine. What percentage of its bases are guanine?",
      r"$20\%$", [r"$30\%$", r"$40\%$", r"$70\%$"],
      r"A $=$ T $= 30\%$, which leaves $40\%$ for G and C together, split equally: G $= 20\%$.",
      [r"$100 - 2(30) = 40\%$ for G $+$ C."],
      [r"is the percentage of thymine.",
       r"is G and C together.",
       r"is everything that is not adenine."]),
])

S7 = Sec("Proteins (1.7)", ["1.7"], r"""
An amino acid has an amino group, a carboxyl group and a side chain (R group) on a central carbon. Peptide bonds join amino acids into a polypeptide with an amino ($N$-) terminus and a carboxyl ($C$-) terminus. The R groups (nonpolar, polar, acidic or basic) determine how the chain folds.

\begin{compare}{Level}{What holds it}{Description}
Primary & peptide bonds & the sequence of amino acids \\
Secondary & hydrogen bonds between backbone atoms & $\alpha$-helices and $\beta$-pleated sheets \\
Tertiary & interactions among R groups: hydrophobic interactions, hydrogen and ionic bonds, disulfide bridges & the overall three-dimensional shape \\
Quaternary & the same interactions between subunits & two or more polypeptides together (hemoglobin) \\
\end{compare}

\textbf{Shape determines function.} Heat, extreme pH or high salt can \textbf{denature} a protein by disrupting the weak interactions, destroying its shape and function without breaking peptide bonds. In a soluble protein, nonpolar R groups tend to be buried inside and polar ones on the surface; membrane-spanning regions are rich in nonpolar R groups.
""", checks=[
    Q("1.7 Structure and function", r"A mutation replaces a nonpolar amino acid buried in the interior of a soluble enzyme with a positively charged amino acid. What is the most likely effect?",
      r"The enzyme folds differently, which may change its shape and reduce its activity.", [r"The enzyme's primary structure stays the same.", r"The enzyme becomes more stable, because charged amino acids form stronger bonds.", r"There is no effect, because only the active site affects function."],
      r"A charged R group in the hydrophobic core disrupts the interactions that hold the tertiary structure, so the overall shape, including the active site, may change.",
      [r"Primary structure changes, so folding (tertiary structure) can change."],
      [r"a substituted amino acid changes the primary structure.",
       r"a charged group in a nonpolar core usually destabilizes the fold.",
       r"the shape of the whole protein determines the shape of the active site."]),
])

QS = [
    Set("Water and the elements of life (1.1--1.2)", [
        Q("1.1 Evaporative cooling", r"Sweating cools the body. Which property of water best explains this?",
          r"Water has a high heat of vaporization, so each gram that evaporates removes a large amount of thermal energy.", [r"Water has a low specific heat, so it cools quickly.", r"Water is a good solvent for salts in sweat.", r"Liquid water is denser than ice."],
          r"Hydrogen bonds must be broken for water molecules to evaporate; the energy comes from the skin, which cools.",
          [r"Evaporation removes the fastest-moving molecules and the energy to break their hydrogen bonds."],
          [r"water's specific heat is high, not low.",
           r"dissolving salts does not remove heat from the body.",
           r"density is unrelated to evaporative cooling."]),
        Q("1.1 Floating ice", r"Why does ice float on liquid water?",
          r"Hydrogen bonds hold molecules in ice in an open lattice, farther apart than in liquid water.", [r"Ice contains trapped air bubbles that make all ice float.", r"Water molecules in ice have less mass.", r"Liquid water has no hydrogen bonds."],
          r"In ice, every molecule forms four stable hydrogen bonds in a spacious lattice, so ice is less dense than liquid water.",
          [r"Lower density than the liquid, so it floats."],
          [r"even bubble-free ice floats.",
           r"the molecules are identical in mass.",
           r"liquid water has many hydrogen bonds; they constantly break and re-form."]),
        Q("1.2 Radioactive tracer", r"Bacteria are grown in a medium whose only source of sulfur is radioactive ${}^{35}\mathrm{S}$. In which molecules will most of the radioactivity be found?",
          r"proteins", [r"DNA", r"phospholipids", r"starch"],
          r"Sulfur is found in the amino acids cysteine and methionine, so it is built into proteins; nucleic acids, lipids and carbohydrates contain no sulfur.",
          [r"This is how Hershey and Chase labeled the protein coats of bacteriophages."],
          [r"DNA contains phosphorus, not sulfur.",
           r"phospholipids contain phosphorus, not sulfur.",
           r"starch contains only C, H and O."]),
    ]),
    Set("Fatty acids and melting points (1.5)", [
        Q("1.5 Double bonds", r"Which conclusion is best supported by comparing the $18$-carbon fatty acids?",
          r"More carbon--carbon double bonds give a lower melting point.", [r"More carbon--carbon double bonds give a higher melting point.", r"The number of double bonds has no effect on melting point.", r"Melting point depends only on the number of carbon atoms."],
          r"Stearic ($0$ double bonds, $70^\circ$C), oleic ($1$, $13^\circ$C) and linoleic ($2$, $-5^\circ$C) all have $18$ carbons; melting point falls as double bonds increase.",
          [r"Hold chain length constant and compare across double bonds."],
          [r"reverses the trend in the data.",
           r"the three $18$-carbon fatty acids differ by $75^\circ$C.",
           r"the $18$-carbon fatty acids all have the same carbon count but different melting points."]),
        Q("1.5 Chain length", r"Which comparison shows the effect of chain length on the melting point of saturated fatty acids?",
          r"lauric, palmitic and stearic acids: longer chains have higher melting points", [r"stearic and oleic acids: longer chains have lower melting points", r"oleic and linoleic acids: longer chains have higher melting points", r"palmitic and linoleic acids: chain length has no effect"],
          r"Lauric ($12$:$0$), palmitic ($16$:$0$) and stearic ($18$:$0$) are all saturated; melting point rises from $44$ to $63$ to $70^\circ$C.",
          [r"Compare molecules that differ only in the variable of interest."],
          [r"those two have the same length and differ in saturation.",
           r"those two have the same length and differ in saturation.",
           r"those two differ in both length and saturation, so the comparison is not controlled."]),
        Q("1.5 Explaining the trend", r"Which best explains why unsaturated fatty acids have lower melting points than saturated ones of the same length?",
          r"Cis double bonds put kinks in the chains, so they cannot pack closely and have fewer attractions between them.", [r"Double bonds are weaker than single bonds, so they break when heated.", r"Unsaturated fatty acids form more hydrogen bonds with each other.", r"Unsaturated fatty acids have more hydrogen atoms."],
          r"Melting overcomes the attractions between neighboring chains; kinked chains touch less, so less energy is needed.",
          [r"Melting separates molecules; it does not break covalent bonds."],
          [r"melting does not break covalent bonds within molecules.",
           r"fatty acid chains are nonpolar and do not hydrogen-bond to each other.",
           r"each double bond means fewer hydrogen atoms (``unsaturated'')."]),
        Q("1.5 Prediction", r"Linolenic acid has $18$ carbons and $3$ double bonds. Based on the data, its melting point is most likely",
          r"below $-5^\circ$C", [r"between $-5^\circ$C and $13^\circ$C", r"between $13^\circ$C and $70^\circ$C", r"above $70^\circ$C"],
          r"The trend for $18$-carbon fatty acids is lower melting points with more double bonds; a third double bond should put it below linoleic acid's $-5^\circ$C. (It is about $-11^\circ$C.)",
          [r"Extend the trend one step."],
          [r"is the range between one and two double bonds.",
           r"is the range between zero and one double bond.",
           r"is higher than even the saturated $18$-carbon fatty acid."]),
    ], stim=r"""The table gives the melting points of five fatty acids, with the number of carbon atoms and of carbon--carbon double bonds in each.

\medskip
\begin{tabular}{@{}lccc@{}}\toprule
Fatty acid & Carbons & Double bonds & Melting point ($^\circ$C) \\ \midrule
Lauric & 12 & 0 & 44 \\
Palmitic & 16 & 0 & 63 \\
Stearic & 18 & 0 & 70 \\
Oleic & 18 & 1 & 13 \\
Linoleic & 18 & 2 & $-5$ \\ \bottomrule
\end{tabular}""", stim_title="Questions 4--7"),
    Set("Macromolecules (1.3--1.7)", [
        Q("1.3 Dehydration synthesis", r"A polypeptide $50$ amino acids long is made by dehydration synthesis. How many water molecules are released?",
          r"$49$", [r"$50$", r"$51$", r"$100$"],
          r"Each peptide bond releases one water molecule; $50$ amino acids are joined by $49$ peptide bonds.",
          [r"$n - 1$ bonds for $n$ monomers."],
          [r"counts monomers rather than bonds.",
           r"adds a bond that does not exist.",
           r"counts two water molecules per bond."]),
        Q("1.4 Digesting cellulose", r"Cows can obtain energy from cellulose but humans cannot. Which is the best explanation?",
          r"Microorganisms in the cow's digestive system produce enzymes that hydrolyze the $\beta$ linkages of cellulose.", [r"Cows make cellulose out of starch in their stomachs.", r"Cellulose is a protein that only cows can digest.", r"Human digestive enzymes break cellulose into fructose, which cannot be used."],
          r"Neither cows nor humans make cellulase; cows host microbes that do, and the cow absorbs the products.",
          [r"Enzyme specificity: $\alpha$ versus $\beta$ linkages."],
          [r"cows break cellulose down; they do not convert starch into it.",
           r"cellulose is a carbohydrate.",
           r"human enzymes do not hydrolyze cellulose at all."]),
        Q("1.6 Complementary strand", r"One strand of a DNA molecule has the sequence $5'$-ATGC-$3'$. What is the sequence of the complementary strand, written $5'$ to $3'$?",
          r"$5'$-GCAT-$3'$", [r"$5'$-TACG-$3'$", r"$5'$-ATGC-$3'$", r"$5'$-UACG-$3'$"],
          r"Pairing A--T and G--C gives $3'$-TACG-$5'$; the strands are antiparallel, so written $5'$ to $3'$ it is GCAT.",
          [r"Complement, then reverse."],
          [r"is the complement written $3'$ to $5'$ but labeled backward.",
           r"is the original strand.",
           r"uses uracil, which is found in RNA, not DNA."]),
        Q("1.6 RNA vs. DNA", r"Which pair of features distinguishes RNA from DNA?",
          r"ribose sugar and the base uracil", [r"deoxyribose sugar and the base thymine", r"phosphate groups and nitrogenous bases", r"peptide bonds and amino acids"],
          r"RNA nucleotides contain ribose and use uracil in place of thymine.",
          [r"DNA: deoxyribose, T. RNA: ribose, U."],
          [r"these belong to DNA.",
           r"both nucleic acids have phosphates and bases.",
           r"these belong to proteins."]),
        Q("1.7 Secondary structure", r"Which level of protein structure consists of $\alpha$-helices and $\beta$-pleated sheets held by hydrogen bonds between backbone atoms?",
          r"secondary", [r"primary", r"tertiary", r"quaternary"],
          r"Secondary structure comes from regular hydrogen bonding along the polypeptide backbone, not between R groups.",
          [r"Backbone hydrogen bonds: secondary. R-group interactions: tertiary."],
          [r"is the amino acid sequence.",
           r"comes from interactions among R groups.",
           r"is the association of several polypeptides."]),
        Q("1.7 Denaturation", r"An enzyme is heated to $70^\circ$C and loses its activity. Which change most likely occurred?",
          r"Weak interactions holding its three-dimensional shape were disrupted, changing the shape of the active site.", [r"Its peptide bonds were hydrolyzed, breaking it into amino acids.", r"Its amino acid sequence was changed.", r"It was converted into a carbohydrate."],
          r"Heat disrupts hydrogen bonds, ionic bonds and hydrophobic interactions; the protein unfolds (denatures) but its primary structure remains.",
          [r"Denaturation changes shape, not sequence."],
          [r"heating does not usually break covalent peptide bonds.",
           r"the sequence is set by the gene and is unchanged by heat.",
           r"denaturation does not change one kind of macromolecule into another."]),
        Q("1.7 Membrane proteins", r"A protein has a region that spans the hydrophobic interior of the plasma membrane. The amino acids in that region most likely have",
          r"nonpolar R groups", [r"charged R groups", r"polar R groups", r"no R groups"],
          r"Nonpolar side chains interact favorably with the nonpolar fatty acid tails of the bilayer.",
          [r"Like dissolves like."],
          [r"charged groups would be repelled by the hydrophobic interior.",
           r"polar groups are found where the protein meets water.",
           r"every amino acid except the backbone ends has an R group."]),
    ]),
]

UNIT = Unit(1, "chemistry-of-life", "Chemistry of Life", "8--11\\%", "1.1--1.7",
    abstract=r"""Unit 1 covers the chemistry that biology depends on: hydrogen bonding and the properties of water, the elements of life and why cells need them, how dehydration synthesis and hydrolysis build and break polymers, and the structure and function of carbohydrates, lipids, nucleic acids and proteins. The recurring theme is that structure determines function. Each section ends with check questions; the key is on the last page.""",
    sections=[S1, S2, S3, S4, S5, S6, S7], qsections=QS,
    frq=FRQ("Conceptual Analysis", 4, r"""Hemoglobin is a protein made of four polypeptide subunits that carries oxygen in red blood cells. In sickle cell disease, a single change in the DNA replaces glutamic acid, an amino acid with a charged (hydrophilic) R group, with valine, an amino acid with a nonpolar (hydrophobic) R group, at position 6 of the $\beta$ subunit, which lies on the surface of the protein. When oxygen levels are low, the altered hemoglobin molecules stick to one another and form long fibers that distort red blood cells into a sickle shape.""", [
        Part("A", 1, r"\textbf{Describe} the level of protein structure that is directly changed by this mutation.",
             r"The primary structure, the sequence of amino acids, is changed (glutamic acid replaced by valine at position 6).",
             r"Naming tertiary or quaternary structure, which change as a consequence, not directly."),
        Part("B", 1, r"\textbf{Explain} why replacing a hydrophilic R group with a hydrophobic R group on the surface of the protein could cause hemoglobin molecules to stick together.",
             r"A hydrophobic R group on the surface is unfavorable in the watery cytoplasm; it associates with nonpolar regions of neighboring hemoglobin molecules (hydrophobic interactions), so the molecules aggregate.",
             r"Saying the valine forms covalent bonds with other molecules."),
        Part("C", 1, r"A different mutation replaces the same glutamic acid with lysine, an amino acid with a positively charged R group. \textbf{Predict} whether this mutation would cause hemoglobin molecules to form fibers.",
             r"It would not (or would be much less likely to) cause fibers to form.",
             r"Predicting fibers because ``any mutation changes the protein.''"),
        Part("D", 1, r"\textbf{Justify} your prediction in part C.",
             r"Lysine's R group, like glutamic acid's, is charged and hydrophilic, so the surface of the protein stays hydrophilic and does not create a hydrophobic patch that sticks to other hemoglobin molecules.",
             r"A justification that does not refer to the polarity of the R group."),
    ], mins=10),
    frq_topic="the sickle cell hemoglobin mutation",
)
