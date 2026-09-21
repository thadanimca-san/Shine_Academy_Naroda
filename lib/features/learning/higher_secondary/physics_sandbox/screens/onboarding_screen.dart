import 'package:flutter/material.dart';
import '../services/profile_service.dart';
import '../theme/tokens.dart';
import '../widgets/bevel_button.dart';
import 'home_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// First-run flow: who are you, what are you aiming at.
/// Two light steps — no accounts, no friction, straight into the lab.
class OnboardingScreen extends StatefulWidget {
  const OnboardingScreen({super.key});

  @override
  State<OnboardingScreen> createState() => _OnboardingScreenState();
}

class _OnboardingScreenState extends State<OnboardingScreen> {
  final _nameController = TextEditingController();
  final _pageController = PageController();
  int _page = 0;
  ExamTarget _exam = ExamTarget.both;
  ClassLevel _level = ClassLevel.eleven;

  @override
  void dispose() {
    _nameController.dispose();
    _pageController.dispose();
    super.dispose();
  }

  bool get _nameOk => _nameController.text.trim().length >= 2;

  void _next() {
    FocusScope.of(context).unfocus();
    _pageController.nextPage(duration: Motion.slow, curve: Motion.ease);
  }

  Future<void> _finish() async {
    await ProfileService.instance.save(
      name: _nameController.text,
      exam: _exam,
      classLevel: _level,
    );
    if (!mounted) return;
    Navigator.of(context).pushReplacement(
      MaterialPageRoute(builder: (_) => const HomeScreen()),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Column(
          children: [
            const SizedBox(height: Gap.x4),
            _stepDots(),
            Expanded(
              child: PageView(
                controller: _pageController,
                physics: const NeverScrollableScrollPhysics(),
                onPageChanged: (i) => setState(() => _page = i),
                children: [_nameStep(), _goalStep()],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _stepDots() {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        for (var i = 0; i < 2; i++)
          AnimatedContainer(
            duration: Motion.base,
            curve: Motion.ease,
            margin: const EdgeInsets.symmetric(horizontal: 4),
            width: _page == i ? 22 : 8,
            height: 8,
            decoration: BoxDecoration(
              color: _page == i ? Palette.primary : Palette.border,
              borderRadius: BorderRadius.circular(Corner.pill),
            ),
          ),
      ],
    );
  }

  Widget _hero(IconData icon) {
    return Container(
      width: 92,
      height: 92,
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: [Palette.primary, Palette.primaryDeep],
        ),
        borderRadius: BorderRadius.circular(Corner.xl),
        boxShadow: [
          BoxShadow(
            color: Palette.primary.withValues(alpha: 0.3),
            blurRadius: 24,
            offset: const Offset(0, 8),
          ),
        ],
      ),
      child: Icon(icon, color: Colors.white, size: 44),
    );
  }

  Widget _nameStep() {
    return ListView(
      padding: const EdgeInsets.symmetric(horizontal: Gap.x6, vertical: Gap.x6),
      children: [
        Center(child: _hero(Icons.rocket_launch_rounded)),
        const SizedBox(height: Gap.x6),
        Text(TrilingualService.instance.getUIText('Welcome to the lab.'),
            textAlign: TextAlign.center, style: Type.display.copyWith(fontSize: 28)),
        const SizedBox(height: Gap.x3),
        Text(TrilingualService.instance.getUIText('Physics Sandbox turns every JEE & NEET concept into an experiment you run yourself. First things first —'),
          textAlign: TextAlign.center,
          style: Type.body.copyWith(color: Palette.textMuted),
        ),
        const SizedBox(height: Gap.x8),
        Text(TrilingualService.instance.getUIText('WHAT SHOULD WE CALL YOU?'), style: Type.label),
        const SizedBox(height: Gap.x2),
        Container(
          decoration: BoxDecoration(
            color: Palette.surface,
            borderRadius: BorderRadius.circular(Corner.lg),
            border: Border.all(color: Palette.border),
          ),
          child: TextField(
            controller: _nameController,
            textCapitalization: TextCapitalization.words,
            style: Type.bodyStrong.copyWith(fontSize: 16),
            onChanged: (_) => setState(() {}),
            onSubmitted: (_) => _nameOk ? _next() : null,
            decoration: InputDecoration(
              hintText: 'Your name',
              hintStyle: Type.body.copyWith(color: Palette.textFaint),
              prefixIcon: Icon(Icons.badge_outlined, color: Palette.textFaint),
              border: InputBorder.none,
              contentPadding:
                  const EdgeInsets.symmetric(horizontal: Gap.x4, vertical: 16),
            ),
          ),
        ),
        const SizedBox(height: Gap.x6),
        BevelButton(
          label: 'Continue',
          icon: Icons.arrow_forward_rounded,
          onPressed: _nameOk ? _next : null,
        ),
      ],
    );
  }

  Widget _goalStep() {
    return ListView(
      padding: const EdgeInsets.symmetric(horizontal: Gap.x6, vertical: Gap.x6),
      children: [
        Center(child: _hero(Icons.track_changes_rounded)),
        const SizedBox(height: Gap.x6),
        Text('Where are you headed, ${_nameController.text.trim().split(' ').first}?',
            textAlign: TextAlign.center, style: Type.display.copyWith(fontSize: 24)),
        const SizedBox(height: Gap.x3),
        Text(TrilingualService.instance.getUIText('We\'ll tune questions, tips and difficulty to your target. You can explore everything either way.'),
          textAlign: TextAlign.center,
          style: Type.body.copyWith(color: Palette.textMuted),
        ),
        const SizedBox(height: Gap.x8),
        Text(TrilingualService.instance.getUIText('MY TARGET EXAM'), style: Type.label),
        const SizedBox(height: Gap.x2),
        Row(children: [
          _choice('JEE', _exam == ExamTarget.jee, Palette.jee,
              () => setState(() => _exam = ExamTarget.jee)),
          const SizedBox(width: Gap.x2),
          _choice('NEET', _exam == ExamTarget.neet, Palette.neet,
              () => setState(() => _exam = ExamTarget.neet)),
          const SizedBox(width: Gap.x2),
          _choice('Both', _exam == ExamTarget.both, Palette.primary,
              () => setState(() => _exam = ExamTarget.both)),
        ]),
        const SizedBox(height: Gap.x6),
        Text(TrilingualService.instance.getUIText('I\'M CURRENTLY IN'), style: Type.label),
        const SizedBox(height: Gap.x2),
        Row(children: [
          _choice('Class 11', _level == ClassLevel.eleven, Palette.primary,
              () => setState(() => _level = ClassLevel.eleven)),
          const SizedBox(width: Gap.x2),
          _choice('Class 12', _level == ClassLevel.twelve, Palette.primary,
              () => setState(() => _level = ClassLevel.twelve)),
          const SizedBox(width: Gap.x2),
          _choice('Dropper', _level == ClassLevel.dropper, Palette.primary,
              () => setState(() => _level = ClassLevel.dropper)),
        ]),
        const SizedBox(height: Gap.x8),
        BevelButton.go(
          label: 'Enter the lab',
          icon: Icons.science_rounded,
          onPressed: _finish,
        ),
        const SizedBox(height: Gap.x3),
        Center(
          child: Text(TrilingualService.instance.getUIText('Powered by Shine Academy, Naroda'),
              style: Type.caption.copyWith(fontSize: 11.5)),
        ),
      ],
    );
  }

  Widget _choice(String label, bool selected, Color color, VoidCallback onTap) {
    return Expanded(
      child: GestureDetector(
        onTap: onTap,
        child: AnimatedContainer(
          duration: Motion.fast,
          padding: const EdgeInsets.symmetric(vertical: 13),
          decoration: BoxDecoration(
            color: selected ? color : Palette.surface,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(color: selected ? color : Palette.border, width: 1.2),
          ),
          alignment: Alignment.center,
          child: Text(
            label,
            style: Type.bodyStrong.copyWith(
              fontSize: 13.5,
              color: selected ? Colors.white : Palette.textMuted,
            ),
          ),
        ),
      ),
    );
  }
}
