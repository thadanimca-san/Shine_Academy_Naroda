import 'package:flutter/material.dart';
import '../../models/lesson.dart';
import '../../theme/tokens.dart';
import '../bevel_button.dart';
import '../fx/confetti_burst.dart';
import '../fx/lottie_fx.dart';
import '../soft_card.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Sequential practice flow: pick a track, answer question by question with
/// full solutions, finish with a score and quick-revision card.
class PracticeView extends StatefulWidget {
  final List<PracticeQuestion> questions;
  final List<String> revision;
  const PracticeView({super.key, required this.questions, required this.revision});

  @override
  State<PracticeView> createState() => _PracticeViewState();
}

class _PracticeViewState extends State<PracticeView> {
  ExamTrack? _track; // null = mixed
  int _index = 0;
  int? _picked;
  int _correct = 0;
  bool _finished = false;

  List<PracticeQuestion> get _pool => _track == null
      ? widget.questions
      : widget.questions
          .where((q) => q.track == _track || q.track == ExamTrack.both)
          .toList();

  void _restart([ExamTrack? track]) {
    setState(() {
      _track = track;
      _index = 0;
      _picked = null;
      _correct = 0;
      _finished = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    final pool = _pool;
    return ListView(
      padding: EdgeInsets.fromLTRB(
          Gap.x5, Gap.x4, Gap.x5, Gap.x6 + MediaQuery.paddingOf(context).bottom),
      children: [
        _trackPicker(),
        const SizedBox(height: Gap.x4),
        if (_finished)
          _summary(pool.length)
        else if (pool.isEmpty)
          SoftCard(child: Text(TrilingualService.instance.getUIText('No questions in this track yet.'), style: Type.body))
        else
          _questionCard(pool[_index], pool.length),
      ],
    );
  }

  Widget _trackPicker() {
    Widget chip(String label, ExamTrack? value, Color color) {
      final selected = _track == value;
      return Expanded(
        child: GestureDetector(
          onTap: () => _restart(value),
          child: AnimatedContainer(
            duration: Motion.fast,
            padding: const EdgeInsets.symmetric(vertical: 10),
            decoration: BoxDecoration(
              color: selected ? color : Palette.surface,
              borderRadius: BorderRadius.circular(Corner.pill),
              border: Border.all(color: selected ? color : Palette.border),
            ),
            alignment: Alignment.center,
            child: Text(label,
                style: Type.caption.copyWith(
                    fontWeight: FontWeight.w700,
                    color: selected ? Colors.white : Palette.textMuted)),
          ),
        ),
      );
    }

    return Row(
      children: [
        chip('Mixed', null, Palette.primary),
        const SizedBox(width: Gap.x2),
        chip('NEET', ExamTrack.neet, Palette.neet),
        const SizedBox(width: Gap.x2),
        chip('JEE', ExamTrack.jee, Palette.jee),
      ],
    );
  }

  Widget _questionCard(PracticeQuestion q, int total) {
    final answered = _picked != null;
    return SoftCard(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Text('QUESTION ${_index + 1} OF $total', style: Type.label.copyWith(fontSize: 10)),
              const Spacer(),
              _difficultyBadge(q.difficulty),
            ],
          ),
          const SizedBox(height: Gap.x3),
          Text(q.question, style: Type.bodyStrong.copyWith(fontSize: 15, height: 1.5)),
          const SizedBox(height: Gap.x4),
          for (var i = 0; i < q.options.length; i++) _option(q, i, answered),
          if (answered) ...[
            const SizedBox(height: Gap.x3),
            Stack(
              alignment: Alignment.topCenter,
              clipBehavior: Clip.none,
              children: [
                _solution(q),
                if (_picked == q.correctIndex)
                  Positioned(
                    top: -60,
                    child: ConfettiBurst(key: ValueKey('confetti_$_index')),
                  ),
              ],
            ),
            const SizedBox(height: Gap.x4),
            BevelButton(
              label: _index + 1 >= total ? 'See my score' : 'Next question',
              onPressed: () => setState(() {
                if (_index + 1 >= total) {
                  _finished = true;
                } else {
                  _index++;
                  _picked = null;
                }
              }),
            ),
          ],
        ],
      ),
    );
  }

  Widget _option(PracticeQuestion q, int i, bool answered) {
    final isCorrect = i == q.correctIndex;
    final isPicked = _picked == i;

    Color border = Palette.border;
    Color bg = Palette.surface;
    Widget? trailing;
    if (answered) {
      if (isCorrect) {
        border = Palette.success;
        bg = Palette.successSoft;
        trailing = Icon(Icons.check_circle_rounded, size: 18, color: Palette.success);
      } else if (isPicked) {
        border = Palette.danger;
        bg = Palette.dangerSoft;
        trailing = Icon(Icons.cancel_rounded, size: 18, color: Palette.danger);
      }
    }

    return Padding(
      padding: const EdgeInsets.only(bottom: Gap.x2),
      child: InkWell(
        borderRadius: BorderRadius.circular(Corner.md),
        onTap: answered
            ? null
            : () => setState(() {
                  _picked = i;
                  if (isCorrect) _correct++;
                }),
        child: AnimatedContainer(
          duration: Motion.fast,
          padding: const EdgeInsets.symmetric(horizontal: Gap.x4, vertical: Gap.x3),
          decoration: BoxDecoration(
            color: bg,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(color: border, width: answered && (isCorrect || isPicked) ? 1.5 : 1),
          ),
          child: Row(
            children: [
              Text(String.fromCharCode(65 + i),
                  style: Type.label.copyWith(fontSize: 12, color: Palette.textMuted)),
              const SizedBox(width: Gap.x3),
              Expanded(child: Text(q.options[i], style: Type.body.copyWith(fontSize: 14))),
              if (trailing != null) trailing,
            ],
          ),
        ),
      ),
    );
  }

  Widget _solution(PracticeQuestion q) {
    final gotIt = _picked == q.correctIndex;
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(Gap.x4),
      decoration: BoxDecoration(
        color: gotIt ? Palette.successSoft : Palette.infoSoft,
        borderRadius: BorderRadius.circular(Corner.md),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(gotIt ? 'CORRECT — HERE\'S WHY' : 'SOLUTION',
              style: Type.label.copyWith(
                  fontSize: 10, color: gotIt ? Palette.success : Palette.info)),
          const SizedBox(height: Gap.x2),
          Text(q.solution, style: Type.body.copyWith(fontSize: 13.5)),
        ],
      ),
    );
  }

  Widget _difficultyBadge(Difficulty d) {
    final (label, color) = switch (d) {
      Difficulty.basic => ('BASIC', Palette.info),
      Difficulty.exam => ('EXAM LEVEL', Palette.accent),
      Difficulty.advanced => ('ADVANCED', Palette.danger),
    };
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
      decoration: BoxDecoration(
        color: color.withValues(alpha: 0.12),
        borderRadius: BorderRadius.circular(Corner.pill),
      ),
      child: Text(label, style: Type.label.copyWith(fontSize: 9, color: color)),
    );
  }

  Widget _summary(int total) {
    final ratio = total == 0 ? 0.0 : _correct / total;
    final (headline, sub) = switch (ratio) {
      >= 0.9 => ('Outstanding! 🏆', 'This topic is close to mastered. Revisit in a week to lock it in.'),
      >= 0.6 => ('Solid work 💪', 'Check the solutions you missed, then run the lab once more.'),
      _ => ('Good attempt 🌱', 'Head back to the Understand stage — the concepts will click.'),
    };
    return Column(
      children: [
        SoftCard(
          child: Column(
            children: [
              if (ratio >= 0.6)
                LottieBadge(LottieFx.successCheck,
                    size: 84, fallbackIcon: Icons.check_circle_rounded),
              Text('$_correct / $total', style: Type.display.copyWith(color: Palette.primary, fontSize: 34)),
              const SizedBox(height: Gap.x2),
              Text(headline, style: Type.title),
              const SizedBox(height: Gap.x2),
              Text(sub, textAlign: TextAlign.center, style: Type.caption.copyWith(fontSize: 13)),
              const SizedBox(height: Gap.x4),
              BevelButton.quiet(
                label: 'Try again',
                icon: Icons.refresh_rounded,
                expanded: false,
                onPressed: () => _restart(_track),
              ),
            ],
          ),
        ),
        const SizedBox(height: Gap.x4),
        SoftCard(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Icon(Icons.bolt_rounded, size: 16, color: Palette.accent),
                  const SizedBox(width: Gap.x2),
                  Text(TrilingualService.instance.getUIText('QUICK REVISION'), style: Type.label.copyWith(fontSize: 10.5)),
                ],
              ),
              const SizedBox(height: Gap.x3),
              for (final r in widget.revision)
                Padding(
                  padding: const EdgeInsets.only(bottom: Gap.x2),
                  child: Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(top: 6),
                        child: Icon(Icons.check_rounded, size: 14, color: Palette.success),
                      ),
                      const SizedBox(width: Gap.x2),
                      Expanded(child: Text(r, style: Type.body.copyWith(fontSize: 13.5))),
                    ],
                  ),
                ),
            ],
          ),
        ),
      ],
    );
  }
}
