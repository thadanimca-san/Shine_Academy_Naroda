import '../../models/lesson.dart';
import '../../simulators/photoelectric_effect_sandbox.dart';
import '../../theme/tokens.dart';

/// Photoelectric Effect — the experiment that proved light is also a particle.
final Lesson photoelectricEffectLesson = Lesson(
  topicId: 'photoelectric-effect',
  title: 'Photoelectric Effect',
  accentColor: Palette.chModern,
  bigQuestion:
      'Shine a dim violet light on a metal plate and electrons fly out instantly. Shine an intensely bright red light on the SAME plate for hours and nothing happens — not one electron. If light is a wave carrying energy smoothly, brightness should always win eventually. Why does colour matter more than brightness?',
  whyItMatters:
      'The photoelectric effect is the experiment that cracked open quantum mechanics: it showed that light, which Maxwell\'s equations described perfectly as a wave, ALSO behaves as a stream of particles (photons) when it interacts with matter. Einstein won his Nobel Prize for explaining it, not for relativity. NEET and JEE test this topic heavily — the stopping-potential-vs-frequency graph and Einstein\'s equation are near-guaranteed marks every year.',
  prediction: const PredictionPrompt(
    scenario:
        'A metal has work function φ. You shine light BELOW the threshold frequency ν₀ on it, and no electrons come out. You then crank the intensity of this same low-frequency light up to maximum, far brighter than before. What happens?',
    options: [
      'Electrons now get ejected, since more energy is being delivered per second',
      'Still no electrons are ejected, no matter how bright the light gets',
      'Electrons are ejected but with lower kinetic energy than before',
      'The metal heats up and melts instead of ejecting electrons',
    ],
    correctIndex: 1,
    reveal:
        'Still nothing. In the lab, set the frequency slider below the threshold mark and push intensity to maximum — zero electrons appear. Each photon individually carries only hν of energy; if that is less than the work function φ, no single photon can free an electron, and piling up MORE such photons (higher intensity) does not let them combine forces. Only raising the FREQUENCY (energy per photon) crosses the threshold.',
  ),
  experiments: [
    'Set frequency below threshold ν₀ and max out intensity — confirm zero electrons are ejected',
    'Raise frequency just above ν₀ and watch electrons finally start appearing',
    'Above threshold, increase intensity and watch the RATE of ejected electrons rise (more current) while max KE stays fixed',
    'Above threshold, increase frequency (keep intensity fixed) and watch the ejected electrons move faster (higher max KE) though their rate barely changes',
    'Increase the work function φ (a "harder" metal) and see the threshold frequency ν₀ shift higher',
    'Read the stopping potential V₀ meter and confirm eV₀ always equals the computed max KE',
  ],
  concept: const [
    ContentBlock.paragraph(
      'When light of suitable frequency falls on a clean metal surface, electrons are ejected from it — this is the photoelectric effect (discovered by Hertz, studied in detail by Lenard). By 1900 three observations about it flatly refused to fit the classical wave picture of light, in which energy is spread continuously across the wavefront and should simply accumulate with time and intensity.',
      title: 'An effect classical physics could not explain',
    ),
    ContentBlock.bullets([
      'Threshold frequency: emission happens ONLY if the light\'s frequency exceeds a minimum ν₀ (different for each metal) — no amount of low-frequency light, however intense, ejects a single electron',
      'Instantaneous emission: electrons are ejected within nanoseconds of illumination, even at very low intensity — a wave should need measurable time to "pour" enough energy into an electron',
      'Kinetic energy is independent of intensity: brighter light (above threshold) ejects MORE electrons, but each one comes out with the SAME maximum kinetic energy — intensity controls quantity, not speed',
    ], title: 'Three facts wave theory could not explain'),
    ContentBlock.paragraph(
      'Einstein (1905) proposed that light itself is quantised: it travels as discrete packets of energy called PHOTONS, each carrying energy E = hν, where h = 6.63×10⁻³⁴ J·s is Planck\'s constant and ν is the frequency. A beam of light is a stream of these photons; "intensity" simply means more photons per second, not more energy per photon.',
      title: 'Einstein\'s photon picture',
    ),
    ContentBlock.formula('E_photon = hν = hc/λ', title: 'PHOTON ENERGY'),
    ContentBlock.paragraph(
      'In this picture, one photon interacts with one electron in an all-or-nothing collision. A minimum energy — the WORK FUNCTION φ — is needed just to free the electron from the metal\'s surface. If hν < φ, the photon simply cannot do the job, no matter how many such photons arrive per second. If hν > φ, the electron is freed instantly (explaining instantaneous emission) and keeps the leftover energy as kinetic energy.',
      title: 'One photon, one electron: the work function',
    ),
    ContentBlock.formula('hν = φ + KE_max     (Einstein\'s photoelectric equation)',
        title: 'EINSTEIN\'S PHOTOELECTRIC EQUATION'),
    ContentBlock.formula('φ = hν₀', title: 'WORK FUNCTION IN TERMS OF THRESHOLD FREQUENCY'),
    ContentBlock.paragraph(
      'The maximum kinetic energy of ejected electrons is measured using the STOPPING POTENTIAL V₀ — the reverse voltage just large enough to stop even the fastest electrons from reaching the collector. Since work done against this field equals the electron\'s KE, eV₀ = KE_max exactly.',
      title: 'Measuring KE: the stopping potential',
    ),
    ContentBlock.formula('eV₀ = KE_max = hν − φ', title: 'STOPPING POTENTIAL'),
    ContentBlock.paragraph(
      'Rearranging Einstein\'s equation gives V₀ = (h/e)ν − φ/e — a straight line if you plot stopping potential V₀ against frequency ν. The SLOPE of this line is h/e (letting you measure Planck\'s constant from a simple experiment!), and the line\'s intercept on the ν-axis is the threshold frequency ν₀. This graph is one of the most frequently tested figures in JEE and NEET.',
      title: 'The V₀ vs ν graph — a favourite exam figure',
    ),
    ContentBlock.bullets([
      'Slope of the V₀–ν line = h/e (same for every metal — a universal constant)',
      'x-intercept = threshold frequency ν₀ (different for each metal, ∝ work function)',
      'y-intercept (if extended) corresponds to −φ/e',
      'Line shifts sideways for different metals but keeps the same slope',
    ], title: 'Reading the graph'),
    ContentBlock.realLife(
      'Photoelectric sensors trigger automatic doors and streetlights, photomultiplier tubes in scientific instruments detect single photons, and the same photon-absorption principle (adapted for semiconductors) underlies solar cells and digital camera sensors.',
    ),
    ContentBlock.mistake(
      'Thinking that more intense light gives electrons more kinetic energy. Intensity only increases the NUMBER of photons arriving per second, hence the number of electrons ejected per second (photoelectric current) — never their individual maximum kinetic energy. Only a higher frequency (more energetic photons) raises KE_max.',
    ),
    ContentBlock.mistake(
      'Forgetting that not every ejected electron has the maximum KE — electrons near the surface lose no energy escaping and reach KE_max, but electrons from deeper below lose some energy along the way and emerge slower. KE_max = hν − φ is a ceiling, not the energy of every single electron.',
    ),
    ContentBlock.example(
      'A metal with work function φ = 2.0 eV is illuminated with light of wavelength 400 nm. Find the maximum kinetic energy of the ejected electrons (in eV) and the stopping potential.\n\nPhoton energy: E = hc/λ = (6.63×10⁻³⁴ × 3×10⁸)/(400×10⁻⁹) = 4.97×10⁻¹⁹ J.\nConvert to eV: 4.97×10⁻¹⁹ / 1.6×10⁻¹⁹ ≈ 3.1 eV.\n\nKE_max = hν − φ = 3.1 − 2.0 = 1.1 eV.\nStopping potential: V₀ = KE_max/e = 1.1 V.',
    ),
    ContentBlock.jeeTip(
      'Memorise hc = 1240 eV·nm (a huge shortcut). Photon energy in eV = 1240/λ(nm). For λ = 400 nm, E = 1240/400 = 3.1 eV instantly — no need to juggle joules and 10⁻¹⁹ conversions mid-exam.',
    ),
    ContentBlock.neetNote(
      'NEET loves the qualitative distinctions: photoelectric current (number of electrons/sec) depends on INTENSITY; stopping potential / max KE depends only on FREQUENCY; there is NO time lag between illumination and emission (instantaneous); and below ν₀, absolutely no emission occurs at any intensity. Also remember: photoelectric current is directly proportional to intensity (at a fixed frequency above threshold), a straight-line graph through the origin.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Light arrives as photons, each carrying a fixed quantum of energy',
      math: 'E_photon = hν',
      note: 'Planck\'s constant h = 6.63×10⁻³⁴ J·s connects frequency to energy.',
    ),
    DerivationStep(
      title: 'A minimum energy is needed to free an electron from the metal',
      math: 'Work function φ = hν₀',
      note: 'φ is a property of the metal\'s surface — different for each metal.',
    ),
    DerivationStep(
      title: 'Energy conservation for one photon-electron collision',
      math: 'hν = φ + KE_max',
      note: 'The leftover energy after paying the "exit cost" φ becomes the electron\'s kinetic energy.',
    ),
    DerivationStep(
      title: 'Express KE_max via the stopping potential',
      math: 'KE_max = eV₀   ⟹   eV₀ = hν − φ',
      note: 'V₀ is the reverse voltage that just barely stops the fastest electrons from completing the circuit.',
    ),
    DerivationStep(
      title: 'Rearrange into the straight-line graph form',
      math: 'V₀ = (h/e)·ν − φ/e',
      note: 'Plotting V₀ against ν gives a straight line of slope h/e and ν-intercept ν₀ = φ/h.',
    ),
  ],
  formulas: const [
    FormulaEntry('Photon energy', 'E = hν = hc/λ'),
    FormulaEntry('Handy shortcut', 'E(eV) = 1240 / λ(nm)'),
    FormulaEntry('Work function', 'φ = hν₀'),
    FormulaEntry('Einstein\'s photoelectric equation', 'hν = φ + KE_max'),
    FormulaEntry('Stopping potential', 'eV₀ = KE_max = hν − φ'),
    FormulaEntry('V₀–ν graph', 'V₀ = (h/e)ν − φ/e', condition: 'slope = h/e, x-intercept = ν₀'),
    FormulaEntry('Planck\'s constant', 'h = 6.63×10⁻³⁴ J·s = 4.136×10⁻¹⁵ eV·s'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The photoelectric effect shows that light behaves as:',
      options: [
        'Purely a wave, with no particle behaviour',
        'A stream of particles (photons), each of energy hν',
        'A continuous fluid of energy',
        'Neither a wave nor a particle',
      ],
      correctIndex: 1,
      solution:
          'Photoelectric emission requires individual photon-electron collisions, each photon carrying a fixed quantum hν — proving light has particle nature alongside its well-known wave nature.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Below the threshold frequency, increasing the intensity of light on a metal surface:',
      options: [
        'Ejects electrons with higher kinetic energy',
        'Ejects more electrons per second, all slow',
        'Ejects no electrons at all, regardless of intensity',
        'Eventually ejects electrons after a time delay',
      ],
      correctIndex: 2,
      solution:
          'Below ν₀, each individual photon carries less energy than the work function, so no single photon can free an electron — piling on more such photons (more intensity) cannot compensate.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A metal has a work function of 2.5 eV. What is its threshold wavelength? (Use hc = 1240 eV·nm)',
      options: ['310 nm', '496 nm', '620 nm', '1240 nm'],
      correctIndex: 1,
      solution:
          'λ₀ = hc/φ = 1240/2.5 = 496 nm.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'Light of wavelength 300 nm falls on a metal with work function 2.0 eV. Find the maximum kinetic energy of the photoelectrons (use hc = 1240 eV·nm).',
      options: ['1.0 eV', '2.13 eV', '4.13 eV', '0.13 eV'],
      correctIndex: 1,
      solution:
          'Photon energy = 1240/300 = 4.13 eV. KE_max = hν − φ = 4.13 − 2.0 = 2.13 eV.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'In an experiment, stopping potential V₀ is plotted against frequency ν for a given metal. The slope of the resulting straight line equals:',
      options: ['h', 'h/e', 'e/h', 'φ/e'],
      correctIndex: 1,
      solution:
          'From V₀ = (h/e)ν − φ/e, the slope of V₀ vs ν is h/e — the same value for every metal, which is how Millikan experimentally measured Planck\'s constant.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'For a fixed frequency of incident light (above threshold), doubling the intensity of light will:',
      options: [
        'Double the maximum kinetic energy of photoelectrons',
        'Double the photoelectric current (electrons ejected per second)',
        'Have no effect on anything',
        'Halve the stopping potential',
      ],
      correctIndex: 1,
      solution:
          'Intensity ∝ number of photons arriving per second ∝ number of electrons ejected per second (photocurrent), at a fixed frequency. Max KE depends only on frequency, not intensity.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Light of frequency ν₁ produces photoelectrons of stopping potential V₁; light of frequency ν₂ (>ν₁) produces stopping potential V₂. The work function of the metal is:',
      options: [
        'e(V₂ν₁ − V₁ν₂)/(ν₂ − ν₁)',
        'e(V₁ν₂ − V₂ν₁)/(ν₂ − ν₁)',
        'e(V₂ − V₁)/(ν₂ − ν₁)',
        'e(V₁ + V₂)/(ν₁ + ν₂)',
      ],
      correctIndex: 0,
      solution:
          'eV₁ = hν₁ − φ and eV₂ = hν₂ − φ. Solve simultaneously: subtract to get h = e(V₂−V₁)/(ν₂−ν₁); substitute back into eV₁ = hν₁ − φ and solve for φ, giving φ = e(V₂ν₁ − V₁ν₂)/(ν₂ − ν₁).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'The threshold wavelength of a metal is 500 nm. Light of wavelength 250 nm falls on it. The stopping potential (in volts) is approximately (hc = 1240 eV·nm):',
      options: ['1.24 V', '2.48 V', '4.96 V', '0.62 V'],
      correctIndex: 1,
      solution:
          'φ = hc/λ₀ = 1240/500 = 2.48 eV. Photon energy at 250 nm = 1240/250 = 4.96 eV. KE_max = 4.96 − 2.48 = 2.48 eV, so V₀ = 2.48 V.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'Which observation about the photoelectric effect could NOT be explained by the classical wave theory of light?',
      options: [
        'Light travels in straight lines',
        'Existence of a threshold frequency below which no emission occurs',
        'Light can be reflected and refracted',
        'Light shows interference patterns',
      ],
      correctIndex: 1,
      solution:
          'Classical wave theory predicted emission should occur at ANY frequency given enough time/intensity — it could not explain why emission fails completely below a sharp threshold frequency, or why emission is instantaneous, or why KE_max is independent of intensity.',
    ),
  ],
  revision: [
    'Photon energy E = hν = hc/λ; handy shortcut E(eV) = 1240/λ(nm).',
    'Einstein\'s equation: hν = φ + KE_max, where φ = hν₀ is the work function.',
    'Below threshold frequency ν₀: zero emission at ANY intensity. Above ν₀: intensity controls electron COUNT, frequency controls max KE.',
    'Stopping potential: eV₀ = KE_max = hν − φ.',
    'V₀ vs ν graph is a straight line; slope = h/e (universal), x-intercept = ν₀ (metal-specific).',
    'Emission is instantaneous — no measurable time lag, which a wave picture could not explain.',
    'This effect proved light has particle (photon) nature in addition to its wave nature.',
  ],
  sandboxBuilder: (_) => const PhotoelectricEffectSandbox(),
);
