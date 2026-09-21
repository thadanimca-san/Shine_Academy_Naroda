import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Entropy & Second Law Sandbox — a chamber divided by a removable partition.
/// Gas starts crammed into the left half; releasing the partition lets it
/// spread irreversibly to fill the whole box. A live entropy-vs-time graph
/// climbs and plateaus, and a "reverse?" toggle demonstrates that watching
/// the molecules spontaneously re-crowd into one half never happens.
class EntropySandbox extends StatefulWidget {
  const EntropySandbox({super.key});

  @override
  State<EntropySandbox> createState() => _EntropySandboxState();
}

class _Particle {
  Offset pos;
  Offset vel;
  _Particle({required this.pos, required this.vel});
}

class _EntropySandboxState extends State<EntropySandbox>
    with SingleTickerProviderStateMixin {
  bool _released = false;
  bool _reverseAttempt = false;
  late final List<_Particle> _particles;
  late final Ticker _ticker;
  Duration _last = Duration.zero;
  final List<double> _entropyHistory = [0];
  double _simTime = 0;
  final _rng = math.Random(3);

  static const double _boxW = 300, _boxH = 170;

  @override
  void initState() {
    super.initState();
    _particles = List.generate(30, (i) {
      final angle = _rng.nextDouble() * 2 * math.pi;
      return _Particle(
        pos: Offset(8 + _rng.nextDouble() * (_boxW / 2 - 16), 8 + _rng.nextDouble() * (_boxH - 16)),
        vel: Offset(math.cos(angle), math.sin(angle)) * 55,
      );
    });
    _ticker = createTicker(_tick)..start();
  }

  @override
  void dispose() {
    _ticker.dispose();
    super.dispose();
  }

  void _tick(Duration elapsed) {
    final dt = math.min((elapsed - _last).inMicroseconds / 1e6, 0.032);
    _last = elapsed;
    setState(() {
      for (final p in _particles) {
        var next = p.pos + p.vel * dt;
        double vx = p.vel.dx;
        double vy = p.vel.dy;
        final rightWall = _released ? _boxW : _boxW / 2;
        if (next.dx < 4 || next.dx > rightWall - 4) vx = -vx;
        if (next.dy < 4 || next.dy > _boxH - 4) vy = -vy;
        p.vel = Offset(vx, vy);
        next = Offset(next.dx.clamp(4, rightWall - 4), next.dy.clamp(4, _boxH - 4));
        p.pos = next;
      }
      if (_released && !_reverseAttempt) {
        _simTime += dt;
        // Entropy proxy: rises as particles spread from half-box to full-box,
        // then plateaus once mixed (models S = k ln(Ω) approach to equilibrium).
        final fractionSpread = (_particles.where((p) => p.pos.dx > _boxW / 2).length / _particles.length)
            .clamp(0.0, 0.5) * 2; // 0 (all left) -> 1 (evenly spread)
        final target = fractionSpread;
        final last = _entropyHistory.last;
        final newVal = last + (target - last) * 0.04;
        _entropyHistory.add(newVal.clamp(0.0, 1.0));
        if (_entropyHistory.length > 240) _entropyHistory.removeAt(0);
      }
    });
  }

  void _release() {
    setState(() {
      _released = true;
      _reverseAttempt = false;
    });
  }

  void _reset() {
    setState(() {
      _released = false;
      _reverseAttempt = false;
      _simTime = 0;
      _entropyHistory
        ..clear()
        ..add(0);
      for (final p in _particles) {
        p.pos = Offset(8 + _rng.nextDouble() * (_boxW / 2 - 16), 8 + _rng.nextDouble() * (_boxH - 16));
      }
    });
  }

  void _tryReverse() {
    setState(() => _reverseAttempt = true);
  }

  @override
  Widget build(BuildContext context) {
    final currentS = _entropyHistory.last;
    return ListView(
      padding: const EdgeInsets.fromLTRB(Gap.x4, Gap.x3, Gap.x4, Gap.x4),
      children: [
        Container(
          height: 210,
          decoration: BoxDecoration(
            gradient: const LinearGradient(
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
              colors: [StageBackdrop.skyTop, StageBackdrop.skyMid, StageBackdrop.skyLow],
              stops: [0.0, 0.75, 1.0],
            ),
            borderRadius: BorderRadius.circular(Corner.lg),
          ),
          clipBehavior: Clip.antiAlias,
          child: CustomPaint(
            painter: _EntropyPainter(
                particles: _particles, released: _released, history: _entropyHistory),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Entropy S (relative)',
              currentS.toStringAsFixed(2), _released ? '↑ increasing' : '(confined)', Palette.chThermal)),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('State',
              _released ? 'expanded' : 'confined', '', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
            child: ElevatedButton(
              onPressed: _released ? null : _release,
              style: ElevatedButton.styleFrom(
                backgroundColor: Palette.chThermal,
                foregroundColor: Colors.white,
                padding: const EdgeInsets.symmetric(vertical: 12),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(Corner.md)),
              ),
              child: Text(TrilingualService.instance.getUIText('Remove partition')),
            ),
          ),
          const SizedBox(width: Gap.x3),
          Expanded(
            child: OutlinedButton(
              onPressed: _released ? _tryReverse : null,
              style: OutlinedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 12),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(Corner.md)),
              ),
              child: Text(TrilingualService.instance.getUIText('Watch it reverse?')),
            ),
          ),
          const SizedBox(width: Gap.x2),
          IconButton(
            onPressed: _reset,
            icon: Icon(Icons.refresh),
            tooltip: 'Reset',
          ),
        ]),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(
            _reverseAttempt
                ? 'You are watching closely — but the gas never spontaneously re-crowds into the left half. Every molecule still moves under the same simple mechanics, yet the astronomically unlikely "all particles happen to be on one side" configuration essentially never recurs. That one-way arrow IS the second law.'
                : 'Try it: hit "Remove partition" and watch the gas rush to fill the whole box — the entropy graph climbs and then plateaus once mixed. This free expansion is irreversible: reversing every molecule\'s velocity would technically retrace the path, but no natural process ever does that by itself.',
            style: Type.caption.copyWith(color: Palette.primaryDeep),
          ),
        ),
      ],
    );
  }

  Widget _meter(String label, String value, String unit, Color color) {
    return Container(
      padding: const EdgeInsets.all(Gap.x3),
      decoration: BoxDecoration(
        color: Palette.surface,
        borderRadius: BorderRadius.circular(Corner.md),
        border: Border.all(color: Palette.border),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(label.toUpperCase(), style: Type.label.copyWith(fontSize: 9)),
          const SizedBox(height: 6),
          Text('$value $unit',
              style: Type.bodyStrong.copyWith(
                  fontSize: 16, fontFamily: 'monospace', color: color)),
        ],
      ),
    );
  }
}

class _EntropyPainter extends CustomPainter {
  final List<_Particle> particles;
  final bool released;
  final List<double> history;
  _EntropyPainter({required this.particles, required this.released, required this.history});

  @override
  void paint(Canvas canvas, Size size) {
    StageBackdrop.paint(canvas, size, groundY: size.height);

    final boxRect = Rect.fromLTWH(size.width * 0.06, size.height * 0.06, size.width * 0.55, size.height * 0.62);
    final scaleX = boxRect.width / 300;
    final scaleY = boxRect.height / 170;

    canvas.drawRRect(RRect.fromRectAndRadius(boxRect, const Radius.circular(8)),
        Paint()..color = const Color(0x33FFFFFF)..style = PaintingStyle.stroke..strokeWidth = 2);

    if (!released) {
      final midX = boxRect.left + boxRect.width / 2;
      canvas.drawLine(Offset(midX, boxRect.top), Offset(midX, boxRect.bottom),
          Paint()..color = Colors.white..strokeWidth = 2.5);
    }

    for (final p in particles) {
      final pos = Offset(boxRect.left + p.pos.dx * scaleX, boxRect.top + p.pos.dy * scaleY);
      canvas.drawCircle(pos, 3.4, Paint()..color = const Color(0xFFF97316));
    }
    _label(canvas, released ? 'expanded (mixed)' : 'confined to left half',
        Offset(boxRect.center.dx, boxRect.top - 10), const Color(0xFFA5A9BF), 10);

    // Entropy-vs-time graph on the right.
    final graphRect = Rect.fromLTWH(size.width * 0.66, size.height * 0.08, size.width * 0.30, size.height * 0.58);
    canvas.drawRect(graphRect, Paint()..color = const Color(0x22FFFFFF));
    canvas.drawLine(Offset(graphRect.left, graphRect.bottom), Offset(graphRect.right, graphRect.bottom),
        Paint()..color = const Color(0x66FFFFFF)..strokeWidth = 1);
    canvas.drawLine(Offset(graphRect.left, graphRect.top), Offset(graphRect.left, graphRect.bottom),
        Paint()..color = const Color(0x66FFFFFF)..strokeWidth = 1);
    if (history.length > 1) {
      final path = Path();
      for (int i = 0; i < history.length; i++) {
        final x = graphRect.left + (i / (history.length - 1).clamp(1, 1 << 30)) * graphRect.width;
        final y = graphRect.bottom - history[i] * graphRect.height;
        if (i == 0) {
          path.moveTo(x, y);
        } else {
          path.lineTo(x, y);
        }
      }
      canvas.drawPath(path, Paint()
        ..color = Palette.chThermal
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.2);
    }
    _label(canvas, 'S vs time', Offset(graphRect.center.dx, graphRect.top - 10), Palette.chThermal, 10);
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fs) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(color: color, fontSize: fs, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_EntropyPainter old) => true;
}
