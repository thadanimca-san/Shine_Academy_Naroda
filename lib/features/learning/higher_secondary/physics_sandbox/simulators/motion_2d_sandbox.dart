import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/sim_controls.dart';
import '../widgets/sim_kit.dart';

/// Motion in 2D — projectile launcher.
///
/// Set speed and angle, press Start, and watch the parabola build point by
/// point. The trail stays so students can compare 30° vs 60° launches and
/// discover that complementary angles share the same range.
class Motion2DSandbox extends StatefulWidget {
  const Motion2DSandbox({super.key});

  @override
  State<Motion2DSandbox> createState() => _Motion2DSandboxState();
}

class _Motion2DSandboxState extends State<Motion2DSandbox>
    with TickerProviderStateMixin {
  double _u = 25; // m/s
  double _angle = 45; // degrees
  static const double _g = 9.8;

  final List<List<Offset>> _trails = []; // finished flights (world coords)
  List<Offset> _current = [];

  late final SimClock _clock = SimClock(this, _onTick);

  double get _rad => _angle * math.pi / 180;
  double get _flightTime => 2 * _u * math.sin(_rad) / _g;
  double get _t => math.min(_clock.t, _flightTime);
  double get _x => _u * math.cos(_rad) * _t;
  double get _y => math.max(0, _u * math.sin(_rad) * _t - 0.5 * _g * _t * _t);
  double get _range => _u * _u * math.sin(2 * _rad) / _g;
  double get _hMax {
    final uy = _u * math.sin(_rad);
    return uy * uy / (2 * _g);
  }

  void _onTick() {
    if (_clock.running) {
      _current.add(Offset(_x, _y));
      if (_clock.t >= _flightTime) {
        _clock.pause();
        _trails.add(List.of(_current));
      }
    }
    setState(() {});
  }

  void _reset() {
    _trails.clear();
    _current = [];
    _clock.reset();
  }

  void _start() {
    if (_clock.t >= _flightTime) {
      // Previous flight landed — begin a fresh launch, keep the ghost trail.
      _current = [];
      _clock.reset();
    }
    _clock.start();
  }

  @override
  void dispose() {
    _clock.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(Gap.x4, Gap.x3, Gap.x4, Gap.x4),
      children: [
        SandboxStage(
          height: 230,
          child: CustomPaint(
            painter: _ProjectilePainter(
              x: _x, y: _y, angle: _rad, u: _u,
              trails: _trails, current: _current,
              inFlight: _clock.running,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        TelemetryRow([
          TelemetryChip('t time', '${_t.toStringAsFixed(1)} s'),
          TelemetryChip('height', '${_y.toStringAsFixed(1)} m', color: Palette.accent),
          TelemetryChip('range R', '${_range.toStringAsFixed(1)} m', color: Palette.success),
          TelemetryChip('h max', '${_hMax.toStringAsFixed(1)} m', color: const Color(0xFF38BDF8)),
        ]),
        const SizedBox(height: Gap.x3),
        SimSlider(
          label: 'Launch speed u',
          value: _u,
          min: 5,
          max: 40,
          unit: 'm/s',
          onChanged: (v) => setState(() => _u = v),
        ),
        SimSlider(
          label: 'Launch angle θ',
          value: _angle,
          min: 10,
          max: 80,
          unit: '°',
          decimals: 0,
          color: Palette.accent,
          onChanged: (v) => setState(() => _angle = v),
        ),
        const SizedBox(height: Gap.x2),
        SimControls(
          running: _clock.running,
          onStart: _start,
          onPause: _clock.pause,
          onReset: _reset,
          startLabel: 'Launch',
        ),
      ],
    );
  }
}

class _ProjectilePainter extends CustomPainter {
  final double x, y, angle, u;
  final List<List<Offset>> trails;
  final List<Offset> current;
  final bool inFlight;

  _ProjectilePainter({
    required this.x, required this.y, required this.angle, required this.u,
    required this.trails, required this.current, required this.inFlight,
  });

  static const _worldW = 170.0; // metres shown horizontally
  static const _worldH = 90.0;

  @override
  void paint(Canvas canvas, Size size) {
    final groundY = size.height - 22;
    final sx = size.width / _worldW;
    final sy = (groundY - 10) / _worldH;
    Offset p(Offset w) => Offset(16 + w.dx * sx, groundY - w.dy * sy);

    // Ground + distance markers
    canvas.drawLine(Offset(0, groundY), Offset(size.width, groundY),
        Paint()..color = Colors.white38..strokeWidth = 3);
    for (double m = 0; m <= _worldW; m += 30) {
      final px = 16 + m * sx;
      canvas.drawLine(Offset(px, groundY), Offset(px, groundY + 6),
          Paint()..color = Colors.white30..strokeWidth = 1.5);
      _label(canvas, '${m.round()}', Offset(px, groundY + 13), Colors.amberAccent, 9);
    }

    // Ghost trails from earlier launches
    for (final trail in trails) {
      _dots(canvas, trail, p, Colors.white24, 2);
    }
    // Current flight trail
    _dots(canvas, current, p, const Color(0xFF67E8F9), 2.5);

    // Launcher barrel
    final basePx = p(Offset.zero);
    canvas.drawLine(
        basePx,
        basePx + Offset(math.cos(angle), -math.sin(angle)) * 22,
        Paint()..color = Colors.white70..strokeWidth = 5..strokeCap = StrokeCap.round);

    // Ball
    final ball = p(Offset(x, y));
    canvas.drawCircle(ball, 7, Paint()..color = const Color(0xFFFB923C));
    canvas.drawCircle(ball + const Offset(-2, -2), 2.4,
        Paint()..color = Colors.white.withValues(alpha: 0.7));
  }

  void _dots(Canvas canvas, List<Offset> pts, Offset Function(Offset) p,
      Color color, double r) {
    final paint = Paint()..color = color;
    for (var i = 0; i < pts.length; i += 3) {
      canvas.drawCircle(p(pts[i]), r, paint);
    }
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fs) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(
              color: color.withValues(alpha: 0.8),
              fontSize: fs, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_ProjectilePainter old) => true;
}
