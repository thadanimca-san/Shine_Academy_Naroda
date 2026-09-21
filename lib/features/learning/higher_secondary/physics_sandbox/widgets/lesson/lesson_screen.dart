import 'package:flutter/material.dart';
import '../../models/lesson.dart';
import '../../theme/tokens.dart';
import '../bevel_button.dart';
import '../soft_card.dart';
import 'block_view.dart';
import 'practice_view.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Keeps each stage's state (sliders, quiz progress) alive while swiping.
class _KeepAlivePage extends StatefulWidget {
  final Widget child;
  const _KeepAlivePage({required this.child});

  @override
  State<_KeepAlivePage> createState() => _KeepAlivePageState();
}

class _KeepAlivePageState extends State<_KeepAlivePage>
    with AutomaticKeepAliveClientMixin {
  @override
  bool get wantKeepAlive => true;

  @override
  Widget build(BuildContext context) {
    super.build(context);
    return widget.child;
  }
}

/// The discovery-first lesson shell:
/// Wonder → Lab → Understand → Derive → Practice.
///
/// Stages are freely navigable — the order is a suggestion, never a cage.
class LessonScreen extends StatefulWidget {
  final Lesson lesson;
  const LessonScreen({super.key, required this.lesson});

  @override
  State<LessonScreen> createState() => _LessonScreenState();
}

enum _Stage { wonder, lab, understand, derive, practice }

class _LessonScreenState extends State<LessonScreen> {
  _Stage _stage = _Stage.wonder;
  int? _predicted;
  bool _revealed = false;
  bool _visitedLab = false;
  late final PageController _pages = PageController();

  static const _meta = {
    _Stage.wonder: (icon: Icons.psychology_alt_outlined, label: '1. Intro'),
    _Stage.lab: (icon: Icons.science_outlined, label: '2. Lab'),
    _Stage.understand: (icon: Icons.lightbulb_outline_rounded, label: '3. Understand'),
    _Stage.derive: (icon: Icons.functions_rounded, label: '4. Derive'),
    _Stage.practice: (icon: Icons.stairs_outlined, label: '5. Practice'),
  };

  void _go(_Stage s) {
    _pages.animateToPage(s.index, duration: Motion.base, curve: Motion.ease);
  }

  void _onPage(int i) => setState(() {
        _stage = _Stage.values[i];
        if (_stage == _Stage.lab) _visitedLab = true;
      });

  @override
  void dispose() {
    _pages.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Legacy-style colored top nav: title + numbered swipeable stage tabs,
    // so students always know where they are and what comes next.
    return Scaffold(
      appBar: AppBar(
        backgroundColor: widget.lesson.accentColor ?? Palette.primaryDeep,
        foregroundColor: Colors.white,
        titleSpacing: 0,
        title: Text(widget.lesson.title,
            style: Type.heading.copyWith(color: Colors.white)),
        bottom: PreferredSize(
          preferredSize: const Size.fromHeight(46),
          child: _stageBar(),
        ),
      ),
      body: PageView(
        controller: _pages,
        onPageChanged: _onPage,
        children: [
          _keepAlive(_wonderStage()),
          _keepAlive(_labStage()),
          _keepAlive(_contentStage(
              widget.lesson.concept.map((b) => BlockView(block: b)).toList())),
          _keepAlive(_deriveStage()),
          _keepAlive(PracticeView(
              questions: widget.lesson.questions, revision: widget.lesson.revision)),
        ],
      ),
    );
  }

  Widget _keepAlive(Widget child) => _KeepAlivePage(child: child);

  // ── Stage navigation: colored top bar, numbered like the classic flow ──
  Widget _stageBar() {
    return SizedBox(
      height: 46,
      child: SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        padding: const EdgeInsets.symmetric(horizontal: Gap.x2),
        child: Row(
          children: [for (final s in _Stage.values) _stageTab(s)],
        ),
      ),
    );
  }

  Widget _stageTab(_Stage s) {
    final selected = _stage == s;
    final meta = _meta[s]!;
    return InkWell(
      onTap: () => _go(s),
      child: AnimatedContainer(
        duration: Motion.fast,
        padding: const EdgeInsets.symmetric(horizontal: Gap.x3),
        decoration: BoxDecoration(
          border: Border(
            bottom: BorderSide(
              color: selected ? Palette.accent : Colors.transparent,
              width: 3,
            ),
          ),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(meta.icon,
                size: 16,
                color: selected ? Colors.white : Colors.white.withValues(alpha: 0.55)),
            const SizedBox(width: 6),
            Text(
              meta.label,
              style: Type.label.copyWith(
                fontSize: 11.5,
                letterSpacing: 0.3,
                color: selected ? Colors.white : Colors.white.withValues(alpha: 0.55),
              ),
            ),
          ],
        ),
      ),
    );
  }

  // ── 1. Wonder ─────────────────────────────────────────────────────
  Widget _wonderStage() {
    final p = widget.lesson.prediction;
    return ListView(
      padding: EdgeInsets.fromLTRB(
          Gap.x5, Gap.x4, Gap.x5, Gap.x6 + MediaQuery.paddingOf(context).bottom),
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(Gap.x5),
          decoration: BoxDecoration(
            gradient: const LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              colors: [Palette.primary, Palette.primaryDeep],
            ),
            borderRadius: BorderRadius.circular(Corner.lg),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(TrilingualService.instance.getUIText('THE BIG QUESTION'),
                  style: Type.label.copyWith(color: Colors.white.withValues(alpha: 0.7), fontSize: 10)),
              const SizedBox(height: Gap.x3),
              Text(widget.lesson.bigQuestion,
                  style: Type.title.copyWith(color: Colors.white, fontSize: 20, height: 1.35)),
            ],
          ),
        ),
        const SizedBox(height: Gap.x4),
        Text(widget.lesson.whyItMatters, style: Type.body),
        const SizedBox(height: Gap.x5),
        SoftCard(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Icon(Icons.casino_outlined, size: 16, color: Palette.accent),
                  const SizedBox(width: Gap.x2),
                  Text(TrilingualService.instance.getUIText('MAKE YOUR PREDICTION'), style: Type.label.copyWith(fontSize: 10.5)),
                ],
              ),
              const SizedBox(height: Gap.x3),
              Text(p.scenario, style: Type.bodyStrong.copyWith(fontSize: 14.5)),
              const SizedBox(height: Gap.x3),
              for (var i = 0; i < p.options.length; i++) _predictionOption(p, i),
              const SizedBox(height: Gap.x2),
              if (_predicted != null && !_revealed)
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(Gap.x3),
                  decoration: BoxDecoration(
                    color: Palette.accentSoft,
                    borderRadius: BorderRadius.circular(Corner.md),
                  ),
                  child: Text(
                    _visitedLab
                        ? 'You\'ve experimented — ready to check your prediction?'
                        : 'Prediction locked in. Now head to the Lab and test it for real.',
                    style: Type.caption.copyWith(color: const Color(0xFF92400E)),
                  ),
                ),
              if (_predicted != null && !_revealed) ...[
                const SizedBox(height: Gap.x3),
                BevelButton(
                  label: _visitedLab ? 'Reveal the answer' : 'Open the Lab',
                  icon: _visitedLab ? Icons.visibility_rounded : Icons.science_outlined,
                  color: _visitedLab ? Palette.primary : Palette.stage,
                  onPressed: () => _visitedLab
                      ? setState(() => _revealed = true)
                      : _go(_Stage.lab),
                ),
              ],
              if (_revealed) _revealCard(p),
            ],
          ),
        ),
      ],
    );
  }

  Widget _predictionOption(PredictionPrompt p, int i) {
    final picked = _predicted == i;
    final showTruth = _revealed;
    Color border = picked ? Palette.primary : Palette.border;
    Color bg = picked ? Palette.primarySoft : Palette.surface;
    if (showTruth && i == p.correctIndex) {
      border = Palette.success;
      bg = Palette.successSoft;
    } else if (showTruth && picked) {
      border = Palette.danger;
      bg = Palette.dangerSoft;
    }
    return Padding(
      padding: const EdgeInsets.only(bottom: Gap.x2),
      child: InkWell(
        borderRadius: BorderRadius.circular(Corner.md),
        onTap: _revealed ? null : () => setState(() => _predicted = i),
        child: AnimatedContainer(
          duration: Motion.fast,
          padding: const EdgeInsets.symmetric(horizontal: Gap.x4, vertical: Gap.x3),
          decoration: BoxDecoration(
            color: bg,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(color: border, width: picked || (showTruth && i == p.correctIndex) ? 1.5 : 1),
          ),
          child: Row(
            children: [
              Icon(
                picked ? Icons.radio_button_checked_rounded : Icons.radio_button_off_rounded,
                size: 18,
                color: picked ? Palette.primary : Palette.textFaint,
              ),
              const SizedBox(width: Gap.x3),
              Expanded(child: Text(p.options[i], style: Type.body.copyWith(fontSize: 14))),
            ],
          ),
        ),
      ),
    );
  }

  Widget _revealCard(PredictionPrompt p) {
    final wasRight = _predicted == p.correctIndex;
    return Container(
      width: double.infinity,
      margin: const EdgeInsets.only(top: Gap.x2),
      padding: const EdgeInsets.all(Gap.x4),
      decoration: BoxDecoration(
        color: wasRight ? Palette.successSoft : Palette.infoSoft,
        borderRadius: BorderRadius.circular(Corner.md),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(wasRight ? 'YOUR INTUITION WAS RIGHT 🎯' : 'SURPRISED? THAT\'S THE GOOD PART 💡',
              style: Type.label.copyWith(
                  fontSize: 10, color: wasRight ? Palette.success : Palette.info)),
          const SizedBox(height: Gap.x2),
          Text(p.reveal, style: Type.body.copyWith(fontSize: 13.5)),
        ],
      ),
    );
  }

  // ── 2. Lab ────────────────────────────────────────────────────────
  Widget _labStage() {
    return Column(
      children: [
        _experimentsStrip(),
        Expanded(
          child: widget.lesson.sandboxBuilder != null
              ? widget.lesson.sandboxBuilder!(context)
              :  Center(
                  child: Padding(
                    padding: EdgeInsets.all(32),
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(Icons.science_outlined, size: 64, color: Colors.grey),
                        SizedBox(height: 16),
                        Text(TrilingualService.instance.getUIText('Interactive sandbox coming soon!'),
                          style: TextStyle(fontSize: 16, color: Colors.grey),
                          textAlign: TextAlign.center,
                        ),
                      ],
                    ),
                  ),
                ),
        ),
      ],
    );
  }

  Widget _experimentsStrip() {
    return Container(
      width: double.infinity,
      margin: const EdgeInsets.fromLTRB(Gap.x4, Gap.x2, Gap.x4, 0),
      padding: const EdgeInsets.symmetric(horizontal: Gap.x4, vertical: Gap.x3),
      decoration: BoxDecoration(
        color: Palette.accentSoft,
        borderRadius: BorderRadius.circular(Corner.md),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(TrilingualService.instance.getUIText('TRY THIS'), style: Type.label.copyWith(fontSize: 9.5, color: const Color(0xFF92400E))),
          const SizedBox(height: Gap.x1),
          Text(
            widget.lesson.experiments.join('   ·   '),
            style: Type.caption.copyWith(fontSize: 12, color: const Color(0xFF78350F)),
          ),
        ],
      ),
    );
  }

  // ── 3/4. Content stages ───────────────────────────────────────────
  Widget _contentStage(List<Widget> children) {
    return ListView(
      padding: EdgeInsets.fromLTRB(
          Gap.x5, Gap.x4, Gap.x5, Gap.x6 + MediaQuery.paddingOf(context).bottom),
      children: children,
    );
  }

  Widget _deriveStage() {
    return _contentStage([
      for (var i = 0; i < widget.lesson.derivation.length; i++)
        _derivationStep(i, widget.lesson.derivation[i]),
      const SizedBox(height: Gap.x2),
      SoftCard(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(Icons.summarize_outlined, size: 16, color: Palette.primary),
                const SizedBox(width: Gap.x2),
                Text(TrilingualService.instance.getUIText('FORMULA SHEET'), style: Type.label.copyWith(fontSize: 10.5)),
              ],
            ),
            const SizedBox(height: Gap.x3),
            for (final f in widget.lesson.formulas)
              Padding(
                padding: const EdgeInsets.only(bottom: Gap.x3),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(f.label, style: Type.caption.copyWith(fontSize: 12)),
                    const SizedBox(height: 3),
                    Container(
                      width: double.infinity,
                      padding: const EdgeInsets.symmetric(horizontal: Gap.x3, vertical: Gap.x2),
                      decoration: BoxDecoration(
                        color: Palette.stage,
                        borderRadius: BorderRadius.circular(Corner.sm),
                      ),
                      child: Text(f.expression,
                          style: Type.mono.copyWith(color: const Color(0xFF7EF5C1), fontSize: 14)),
                    ),
                    if (f.condition != null) ...[
                      const SizedBox(height: 3),
                      Text(f.condition!, style: Type.caption.copyWith(fontSize: 11)),
                    ],
                  ],
                ),
              ),
          ],
        ),
      ),
    ]);
  }

  Widget _derivationStep(int i, DerivationStep step) {
    return Padding(
      padding: const EdgeInsets.only(bottom: Gap.x4),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: 26,
            height: 26,
            margin: const EdgeInsets.only(top: 2),
            decoration: BoxDecoration(color: Palette.primarySoft, shape: BoxShape.circle),
            alignment: Alignment.center,
            child: Text('${i + 1}',
                style: Type.label.copyWith(fontSize: 12, color: Palette.primary)),
          ),
          const SizedBox(width: Gap.x3),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(step.title, style: Type.bodyStrong),
                const SizedBox(height: Gap.x2),
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(Gap.x3),
                  decoration: BoxDecoration(
                    color: Palette.stage,
                    borderRadius: BorderRadius.circular(Corner.sm),
                  ),
                  child: Text(step.math,
                      style: Type.mono.copyWith(color: const Color(0xFF7EF5C1), fontSize: 13.5)),
                ),
                if (step.note != null) ...[
                  const SizedBox(height: Gap.x2),
                  Text(step.note!, style: Type.caption.copyWith(fontSize: 12.5)),
                ],
              ],
            ),
          ),
        ],
      ),
    );
  }
}
