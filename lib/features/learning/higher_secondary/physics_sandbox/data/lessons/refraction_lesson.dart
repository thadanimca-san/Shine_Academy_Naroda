import '../../models/lesson.dart';
import '../../simulators/refraction_sandbox.dart';
import '../../theme/tokens.dart';

/// Refraction — Snell's law, refractive index, and total internal reflection.
final Lesson refractionLesson = Lesson(
  topicId: 'refraction',
  title: 'Refraction',
  accentColor: Palette.chOptics,
  bigQuestion:
      'Shine a beam of light from water toward the surface at a steep, glancing angle and it doesn\'t just dim — past a certain angle, it stops exiting the water entirely and reflects back inside, perfectly, as if the water surface had suddenly become a mirror. What angle triggers this switch, and why does it happen so abruptly?',
  whyItMatters:
      'Refraction explains why straws look bent in water, how lenses and prisms work, why diamonds sparkle, and how optical fibres carry the entire internet across oceans using total internal reflection. Snell\'s law is tested constantly in NEET and JEE, both as direct numericals and embedded inside lens/prism problems — and total internal reflection is one of the most application-rich topics in the whole optics syllabus.',
  prediction: const PredictionPrompt(
    scenario:
        'Light travels inside a denser medium (like water or glass) and hits the boundary with a rarer medium (like air) at increasing angles from the normal. At some critical angle, what happens to the refracted ray?',
    options: [
      'It just gets dimmer and dimmer, but always partially exits',
      'At the critical angle, the refracted ray grazes along the boundary (90° refraction); beyond it, ALL light reflects back inside (total internal reflection)',
      'The refracted ray bends back toward the normal instead of away from it',
      'Nothing special happens — refraction continues normally at all angles',
    ],
    correctIndex: 1,
    reveal:
        'At the critical angle θc, Snell\'s law gives a refraction angle of exactly 90° — the refracted ray skims along the surface. Push the incidence angle any higher and there is no possible refraction angle at all, so 100% of the light reflects internally. In the lab, increase the incidence angle inside the denser medium and watch the refracted ray bend toward 90°, then vanish entirely as the beam switches to full internal reflection past θc.',
  ),
  experiments: [
    'Increase the angle of incidence in the denser medium and watch the refracted ray bend farther from the normal',
    'Push the angle up to the critical angle and watch the refracted ray graze along the boundary at 90°',
    'Go past the critical angle and observe 100% total internal reflection — no light exits at all',
    'Switch the refractive index of the medium and watch the critical angle change accordingly',
    'Compare apparent depth vs real depth by viewing an object through the denser medium at different n values',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Refraction is the bending of light as it crosses the boundary between two media of different optical density, caused by a change in the speed of light. Light slows down when entering a denser (higher refractive index) medium and speeds up when leaving it — this speed change is the root cause of the bending, not some mysterious property of the boundary itself.',
      title: 'Why light bends: a change in speed',
    ),
    ContentBlock.formula('n₁ sinθ₁ = n₂ sinθ₂', title: 'SNELL\'S LAW'),
    ContentBlock.formula('n = c/v', title: 'REFRACTIVE INDEX'),
    ContentBlock.paragraph(
      'The refractive index n of a medium is defined as the ratio of the speed of light in vacuum (c) to its speed in that medium (v) — a higher n means light travels slower in that medium. Snell\'s law n₁sinθ₁ = n₂sinθ₂ says that as light crosses into a medium of higher n (slower speed), it bends TOWARD the normal (θ decreases); crossing into a medium of lower n (faster speed), it bends AWAY from the normal.',
      title: 'The refractive index sets the bending amount',
    ),
    ContentBlock.formula('Apparent depth = Real depth / n', title: 'APPARENT DEPTH'),
    ContentBlock.paragraph(
      'When you look down into a swimming pool, the bottom appears shallower than it really is — this is because light rays from the pool bottom refract as they exit the water into air, bending away from the normal, making the rays appear to diverge from a point closer to the surface than the actual bottom. The apparent depth is always real depth divided by the medium\'s refractive index (viewed from a rarer medium).',
      title: 'Why the pool looks shallower than it is',
    ),
    ContentBlock.formula('sinθc = 1/n (medium 2 = air, n₁ = n)', title: 'CRITICAL ANGLE'),
    ContentBlock.paragraph(
      'Total internal reflection can only happen when light travels from a DENSER medium toward a RARER one (e.g. water to air, glass to air) — never the other way. The critical angle θc is the specific angle of incidence (in the denser medium) at which the refracted ray would exit at exactly 90°; for any angle of incidence GREATER than θc, refraction becomes geometrically impossible and ALL the light reflects internally, with 100% efficiency (far better than any ordinary mirror).',
      title: 'Total internal reflection',
    ),
    ContentBlock.bullets([
      'TIR requires: (1) light going from denser to rarer medium, (2) angle of incidence greater than the critical angle',
      'Higher refractive index n → smaller critical angle → TIR happens more easily',
      'TIR reflects light with essentially no loss, unlike ordinary mirrors which absorb some light',
    ]),
    ContentBlock.realLife(
      'Diamonds sparkle brilliantly because of their very high refractive index (n ≈ 2.42), giving them a small critical angle (~24°) — light entering a well-cut diamond undergoes multiple total internal reflections before exiting, creating intense sparkle. Optical fibres exploit total internal reflection to guide light along thin glass strands over huge distances with almost no loss, forming the backbone of the internet. Mirages on hot roads happen because layers of air at different temperatures/densities create a gradient of refractive index, bending light from the sky upward into your eyes so it looks like a pool of water on the road.',
    ),
    ContentBlock.mistake(
      'Believing total internal reflection can happen going from a rarer to a denser medium (like air into water). TIR is strictly a one-way phenomenon — it can ONLY occur when light attempts to leave a denser medium for a rarer one. Going the other way, refraction always exists (light bends toward the normal) and there is no critical angle limit.',
    ),
    ContentBlock.mistake(
      'Confusing apparent depth (a phenomenon from viewing across a refractive boundary) with actual physical depth. The apparent depth formula (real depth/n) applies specifically to near-normal viewing; extreme oblique angles distort the simple formula further. Also, remember apparent depth < real depth only when viewing from the RARER side looking into the denser medium.',
    ),
    ContentBlock.example(
      'Light travels from glass (n = 1.5) into air. Find the critical angle for total internal reflection.\n\nsinθc = n₂/n₁ = 1/1.5 = 0.667.\nθc = sin⁻¹(0.667) ≈ 41.8°.\n\nAny ray hitting the glass-air boundary from inside the glass at more than about 42° from the normal undergoes total internal reflection.',
    ),
    ContentBlock.jeeTip(
      'For a combination of refractions (e.g. light crossing several parallel slabs of different media), use n₁sinθ₁ = n₂sinθ₂ = n₃sinθ₃ = … repeatedly — the quantity n·sinθ is conserved across EVERY boundary in a stack of parallel-faced media, even though θ changes at each interface. This shortcut avoids computing intermediate angles explicitly.',
    ),
    ContentBlock.neetNote(
      'NEET often tests direct critical-angle numericals: sinθc = 1/n, so a substance with n = 1.33 (water) has θc ≈ 48.8°, while n = 1.5 (glass) has θc ≈ 41.8° — higher refractive index means smaller critical angle, and TIR is EASIER to achieve. Also remember that optical fibres use a core with higher n than the cladding specifically to keep light totally internally reflected as it bounces along the fibre.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Consider a wavefront crossing a boundary between two media (Huygens\' construction)',
      math: 'Wave speed v₁ in medium 1, v₂ in medium 2 (v₁ ≠ v₂)',
      note: 'Different parts of the wavefront reach the boundary at slightly different times, causing the direction to bend.',
    ),
    DerivationStep(
      title: 'Relate the path lengths travelled by two edges of the wavefront',
      math: 'Using geometry of the wavefront and the incidence/refraction angles: sinθ₁/v₁ = sinθ₂/v₂',
    ),
    DerivationStep(
      title: 'Introduce refractive index n = c/v for each medium',
      math: 'v₁ = c/n₁,  v₂ = c/n₂',
    ),
    DerivationStep(
      title: 'Substitute and simplify',
      math: 'sinθ₁·n₁/c = sinθ₂·n₂/c  →  n₁ sinθ₁ = n₂ sinθ₂',
      note: 'Snell\'s law, derived from the wave nature of light and the change in speed across the boundary.',
    ),
    DerivationStep(
      title: 'Find the critical angle by setting the refraction angle to 90°',
      math: 'n₁ sinθc = n₂ sin(90°) = n₂  →  sinθc = n₂/n₁',
      note: 'Valid only when n₁ > n₂ (denser to rarer); for n₂ = 1 (air), sinθc = 1/n₁.',
    ),
  ],
  formulas: const [
    FormulaEntry('Snell\'s law', 'n₁ sinθ₁ = n₂ sinθ₂'),
    FormulaEntry('Refractive index', 'n = c/v'),
    FormulaEntry('Relative refractive index', 'n₂₁ = n₂/n₁ = v₁/v₂'),
    FormulaEntry('Apparent depth', 'd_apparent = d_real / n'),
    FormulaEntry('Critical angle', 'sinθc = n₂/n₁', condition: 'n₁ > n₂, TIR possible'),
    FormulaEntry('Critical angle (to air)', 'sinθc = 1/n'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'When light travels from air into glass, it bends:',
      options: ['Away from the normal', 'Toward the normal', 'Does not bend', 'Reverses direction'],
      correctIndex: 1,
      solution: 'Glass has a higher refractive index than air, so light slows down and bends toward the normal (Snell\'s law).',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Total internal reflection can occur when light travels:',
      options: ['From a rarer to a denser medium', 'From a denser to a rarer medium, beyond the critical angle', 'In any medium at any angle', 'Only in a vacuum'],
      correctIndex: 1,
      solution: 'TIR requires light going from denser to rarer medium, at an angle of incidence greater than the critical angle.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'The refractive index of water is 1.33. The critical angle for water-to-air is approximately:',
      options: ['30°', '41°', '49°', '60°'],
      correctIndex: 2,
      solution: 'sinθc = 1/n = 1/1.33 ≈ 0.752. θc = sin⁻¹(0.752) ≈ 48.8°, closest to 49°.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A coin lies at the bottom of a pool of water (n=1.33) with real depth 60 cm. Its apparent depth when viewed from directly above is approximately:',
      options: ['45 cm', '60 cm', '80 cm', '30 cm'],
      correctIndex: 0,
      solution: 'Apparent depth = real depth/n = 60/1.33 ≈ 45.1 cm.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A ray of light passes from medium 1 (n=1.5) into medium 2 (n=1.0) at an angle of incidence 30°. The angle of refraction is:',
      options: ['30°', '41.8°', '48.6°', '19.5°'],
      correctIndex: 2,
      solution: 'n₁sinθ₁=n₂sinθ₂ → 1.5×sin30° = 1×sinθ₂ → sinθ₂ = 1.5×0.5 = 0.75 → θ₂ = sin⁻¹(0.75) ≈ 48.6°.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A substance has critical angle 30° for light going into air. Its refractive index is:',
      options: ['1.5', '2.0', '1.33', '0.5'],
      correctIndex: 1,
      solution: 'sinθc = 1/n → n = 1/sin30° = 1/0.5 = 2.0.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Diamond has a refractive index of about 2.42. Its critical angle is approximately:',
      options: ['24°', '35°', '42°', '55°'],
      correctIndex: 0,
      solution: 'sinθc = 1/2.42 ≈ 0.413. θc = sin⁻¹(0.413) ≈ 24.4°, explaining diamond\'s intense sparkle from repeated TIR.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Light passes through three parallel slabs of media with refractive indices n₁, n₂, n₃, entering the first at angle θ₁. The relationship connecting the exit angle θ₃ (back into the original medium n₁) to θ₁ is:',
      options: ['θ₃ depends on n₂ but not n₁', 'θ₃ = θ₁ always (for parallel-faced slabs with the same entry/exit medium)', 'θ₃ > θ₁ always', 'θ₃ is undefined'],
      correctIndex: 1,
      solution: 'For parallel-faced slabs, n·sinθ is conserved at every interface; if the ray exits back into the SAME medium n₁, then n₁sinθ₃ = n₁sinθ₁ → θ₃ = θ₁, regardless of the intermediate media.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'Optical fibres transmit light over long distances with minimal loss primarily because of:',
      options: [
        'The glass core absorbs and re-emits light efficiently',
        'Total internal reflection at the core-cladding boundary, where the core has higher refractive index',
        'The fibre is transparent',
        'Light travels faster inside a fibre than in vacuum',
      ],
      correctIndex: 1,
      solution: 'The fibre core has a higher refractive index than the surrounding cladding, so light hitting the boundary beyond the critical angle undergoes repeated total internal reflection, trapping it inside with near-zero loss.',
    ),
  ],
  revision: [
    'Snell\'s law: n₁sinθ₁ = n₂sinθ₂ — light bends toward the normal entering a denser medium, away from it entering a rarer one.',
    'Refractive index n = c/v; higher n means slower light speed in that medium.',
    'Apparent depth = real depth/n — this is why pools look shallower than they really are.',
    'Total internal reflection: only denser→rarer, only beyond the critical angle, sinθc = n₂/n₁ (=1/n for exit to air).',
    'Diamonds sparkle due to high n (small critical angle, ~24°) causing repeated internal reflections.',
    'Optical fibres guide light via TIR: core has higher n than cladding.',
    'n·sinθ is conserved across every boundary in a stack of parallel-faced media.',
  ],
  sandboxBuilder: (_) => const RefractionSandbox(),
);
