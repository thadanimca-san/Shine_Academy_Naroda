import '../../models/chapter_model.dart';
final ChapterModel class9AtomicStructureChapter = ChapterModel(
  standard: 9, subject: "Chemistry", chapterId: "cls9_chem_atomicstructure", chapterName: "Journey Inside the Atom",
  imagePath: "assets/images/../dictionary/atom.jpg",
  concepts: ["Sub-atomic particles: electrons, protons and neutrons.", "Atomic models: Thomson, Rutherford, Bohr.", "Isotopes and isobars."],
  formulas: [
    FormulaDerivation(
      formulaName: "Maximum Electrons in a Shell (Bohr-Bury Rule)",
      expression: "Max electrons = 2n²",
      derivationSteps: [
        "Bohr and Bury proposed that each electron shell, numbered n = 1, 2, 3... (K, L, M...), can hold only a fixed maximum number of electrons.",
        "This maximum capacity is given by the formula 2n², where n is the shell number.",
        "For the K shell (n=1): 2(1)² = 2 electrons.",
        "For the L shell (n=2): 2(2)² = 8 electrons.",
        "For the M shell (n=3): 2(3)² = 18 electrons.",
      ],
    ),
    FormulaDerivation(
      formulaName: "Mass Number",
      expression: "A = Z + n",
      derivationSteps: [
        "The mass number (A) of an atom is the total count of protons and neutrons in its nucleus (these are collectively called nucleons).",
        "The atomic number (Z) is the number of protons.",
        "If n is the number of neutrons, then mass number A = Z + n.",
      ],
    ),
  ],
  fillInTheBlanks: [
    QuestionItem(id: "as1", question: "The electron was discovered by [ J. J. Thomson / E. Goldstein ].", answer: "J. J. Thomson"),
    QuestionItem(id: "as2", question: "The proton was discovered by [ E. Goldstein / J. J. Thomson ].", answer: "E. Goldstein"),
    QuestionItem(id: "as3", question: "The neutron was discovered by [ James Chadwick / Niels Bohr ].", answer: "James Chadwick"),
    QuestionItem(id: "as4", question: "An electron carries a [ negative / positive ] charge.", answer: "negative"),
    QuestionItem(id: "as5", question: "A proton carries a [ positive / negative ] charge.", answer: "positive"),
    QuestionItem(id: "as6", question: "A neutron is [ neutral / positively charged ].", answer: "neutral"),
    QuestionItem(id: "as7", question: "The alpha particle scattering experiment was performed by [ Rutherford / Bohr ].", answer: "Rutherford"),
    QuestionItem(id: "as8", question: "The number of protons in the nucleus of an atom is called its [ atomic number / mass number ].", answer: "atomic number"),
    QuestionItem(id: "as9", question: "The sum of the number of protons and neutrons in an atom is called its [ mass number / atomic number ].", answer: "mass number"),
    QuestionItem(id: "as10", question: "Atoms of the same element having the same atomic number but different mass numbers are called [ isotopes / isobars ].", answer: "isotopes"),
    QuestionItem(id: "as11", question: "Atoms of different elements having the same mass number are called [ isobars / isotopes ].", answer: "isobars"),
    QuestionItem(id: "as12", question: "According to Bohr's model, electrons revolve around the nucleus in fixed [ shells / clouds ].", answer: "shells"),
    QuestionItem(id: "as13", question: "The maximum number of electrons in the K shell (n=1) is [ 2 / 8 ].", answer: "2"),
    QuestionItem(id: "as14", question: "The maximum number of electrons in the L shell (n=2) is [ 8 / 2 ].", answer: "8"),
    QuestionItem(id: "as15", question: "The valency of an atom is determined by the number of electrons present in its [ outermost shell / nucleus ].", answer: "outermost shell"),
  ],
  numericalProblems: [
    NumericalProblem(id: "asn1", question: "Find the maximum number of electrons that can be held in the M shell (n=3) using 2n².", given: ["n = 3"], solutionSteps: ["Max electrons = 2n²", "= 2(3)²", "= 2×9 = 18"], numericAnswer: 18, unit: ""),
    NumericalProblem(id: "asn2", question: "An atom has atomic number 17 and mass number 35. Find the number of neutrons.", given: ["Z = 17", "A = 35"], solutionSteps: ["A = Z + n, so n = A − Z", "= 35 − 17", "= 18"], numericAnswer: 18, unit: "neutrons"),
    NumericalProblem(id: "asn3", question: "An atom has 11 protons and 12 neutrons. Find its mass number.", given: ["protons (Z) = 11", "neutrons = 12"], solutionSteps: ["A = Z + n", "= 11 + 12", "= 23"], numericAnswer: 23, unit: ""),
    NumericalProblem(id: "asn4", question: "Find the maximum number of electrons that can be held in the N shell (n=4).", given: ["n = 4"], solutionSteps: ["Max electrons = 2n²", "= 2(4)²", "= 2×16 = 32"], numericAnswer: 32, unit: ""),
    NumericalProblem(id: "asn5", question: "A neutral atom has 20 protons. Find the number of electrons it has.", given: ["protons = 20"], solutionSteps: ["In a neutral atom, electrons = protons.", "electrons = 20"], numericAnswer: 20, unit: "electrons"),
    NumericalProblem(id: "asn6", question: "An atom of chlorine has mass number 35 and 18 neutrons. Find its atomic number.", given: ["A = 35", "n = 18"], solutionSteps: ["A = Z + n, so Z = A − n", "= 35 − 18", "= 17"], numericAnswer: 17, unit: ""),
    NumericalProblem(id: "asn7", question: "An atom has electron configuration 2, 8, 5 (in K, L, M shells). Find its total number of electrons (atomic number).", given: ["K=2, L=8, M=5"], solutionSteps: ["Total electrons = 2+8+5", "= 15"], numericAnswer: 15, unit: ""),
  ],
  revisionNotes: [
    RevisionNote(
      title: '1. Discovery of Sub-atomic Particles',
      iconKey: 'theory',
      points: [
        'J. J. Thomson discovered the electron (negative charge) using cathode ray tube experiments.',
        'E. Goldstein discovered the proton (positive charge) using canal ray/discharge tube experiments.',
        'James Chadwick discovered the neutron (no charge), much later than the electron and proton.',
        'Every atom is electrically neutral: number of electrons = number of protons.',
      ],
    ),
    RevisionNote(
      title: '2. Atomic Models',
      iconKey: 'organelles',
      points: [
        'Thomson\'s model: "plum pudding" — positive charge spread throughout, with electrons embedded like plums.',
        'Rutherford\'s alpha-particle scattering experiment: most alpha particles passed straight through gold foil, some deflected, a few bounced back — proving atoms are mostly empty space with a small, dense, positively charged nucleus.',
        'Bohr\'s model: electrons revolve around the nucleus in fixed, defined circular paths called shells/energy levels (not anywhere randomly), without losing energy.',
        'Shells are named K, L, M, N... starting from the one closest to the nucleus (n = 1, 2, 3, 4...).',
      ],
    ),
    RevisionNote(
      title: '3. Distribution of Electrons in Shells',
      iconKey: 'division',
      points: [
        'Bohr-Bury rule: maximum electrons in a shell = 2n² (n = shell number).',
        'K shell (n=1): max 2 electrons. L shell (n=2): max 8. M shell (n=3): max 18. N shell (n=4): max 32.',
        'The outermost shell can hold a maximum of 8 electrons (except when it\'s the only shell — then max 2).',
        'Electrons fill inner shells first, then move to outer shells only once inner ones are full.',
      ],
    ),
    RevisionNote(
      title: '4. Atomic Number, Mass Number & Valency',
      iconKey: 'muscle',
      points: [
        'Atomic number (Z) = number of protons in the nucleus. Defines which element it is.',
        'Mass number (A) = total number of protons + neutrons (nucleons) in the nucleus. A = Z + n.',
        'Valency = the combining capacity of an atom, determined by the number of electrons in its outermost shell.',
        'If the outermost shell has ≤4 electrons, valency = that number. If it has >4, valency = 8 − that number.',
      ],
    ),
    RevisionNote(
      title: '5. Isotopes & Isobars',
      iconKey: 'plant_growth',
      points: [
        'Isotopes: atoms of the SAME element (same atomic number/protons) but DIFFERENT mass numbers (different neutrons). E.g. carbon-12 and carbon-14.',
        'Isotopes have the same chemical properties (same electron arrangement) but different physical properties (different mass).',
        'Isobars: atoms of DIFFERENT elements that happen to have the SAME mass number.',
        'Uses of isotopes: nuclear fuel (Uranium-235), treating cancer/goitre (radioactive isotopes), and as tracers in medicine.',
      ],
    ),
  ],
);
