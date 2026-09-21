import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'common/sim_frame.dart';

enum _JointType { ball, hinge, pivot, fixed }

class _JointInfo {
  final String label;
  final String description;
  const _JointInfo(this.label, this.description);
}

const _jointInfo = {
  _JointType.ball: _JointInfo(
    'Shoulder — Ball & Socket',
    'The rounded top of the upper-arm bone fits into a shallow hollow of the shoulder bone, letting the arm move forward, backward, sideways, and in full circles.',
  ),
  _JointType.hinge: _JointInfo(
    'Elbow / Knee — Hinge',
    'Bends and straightens in one direction only, like a door hinge. The kneecap sits in front of the knee\'s hinge joint to protect it.',
  ),
  _JointType.pivot: _JointInfo(
    'Neck — Pivot',
    'Connects the skull to the backbone, letting the head rotate side to side like a doorknob turning in its socket — try shaking your head "no".',
  ),
  _JointType.fixed: _JointInfo(
    'Skull — Fixed',
    'The flat bones of the skull are locked together and cannot move at all, permanently protecting the brain even while the rest of the body moves.',
  ),
};

/// Tap through the four joint types found in the human skeleton and watch
/// each one animate its own characteristic motion — ball-and-socket
/// rotation, a hinge bending in one plane, a pivot turning side to side,
/// and a fixed joint that doesn't move at all.
class JointsSimulationWidget extends StatefulWidget {
  const JointsSimulationWidget({super.key});

  @override
  State<JointsSimulationWidget> createState() => _JointsSimulationWidgetState();
}

class _JointsSimulationWidgetState extends State<JointsSimulationWidget>
    with SingleTickerProviderStateMixin {
  _JointType _joint = _JointType.ball;
  late final AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 1600))..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final info = _jointInfo[_joint]!;
    return SimFrame(
      title: 'Skeleton & Joints',
      icon: Icons.accessibility_new,
      accent: const Color(0xFFC2455B),
      description: 'Tap a joint to watch it move — try the matching motion on yourself too.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: _JointType.values.map((j) {
              final isSelected = _joint == j;
              return ChoiceChip(
                label: Text(_jointInfo[j]!.label, style: TextStyle(fontSize: 11.5, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: const Color(0xFFC2455B),
                backgroundColor: const Color(0xFFC2455B).withValues(alpha: 0.15),
                onSelected: (_) => setState(() => _joint = j),
              );
            }).toList(),
          ),
          const SizedBox(height: 14),
          Container(
            height: 200,
            width: double.infinity,
            decoration: BoxDecoration(
              color: const Color(0xFFF7E5E8),
              borderRadius: BorderRadius.circular(14),
              border: Border.all(color: Colors.grey.shade300),
            ),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) => CustomPaint(
                size: Size.infinite,
                painter: _JointPainter(joint: _joint, t: _controller.value),
              ),
            ),
          ),
          const SizedBox(height: 12),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.grey.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade200)),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(info.label, style: TextStyle(fontWeight: FontWeight.bold, color: Color(0xFF9C3448), fontSize: 14)),
                const SizedBox(height: 4),
                Text(info.description, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _JointPainter extends CustomPainter {
  final _JointType joint;
  final double t; // 0..1 looping animation phase

  _JointPainter({required this.joint, required this.t});

  static const _bone = Color(0xFFC2455B);
  static const _boneDeep = Color(0xFF9C3448);

  @override
  void paint(Canvas canvas, Size size) {
    final cx = size.width / 2;
    final cy = size.height / 2;
    final bonePaint = Paint()..color = _bone;
    final boneDeepPaint = Paint()..color = _boneDeep;

    switch (joint) {
      case _JointType.ball:
        // Drawn as a simple, unmistakable human upper-body silhouette (head
        // + torso) with one arm swinging at the shoulder, so this reads as
        // anatomy at a glance rather than an abstract ball-on-a-stick shape.
        final bodyScale = (size.shortestSide / 200).clamp(0.6, 1.4);
        final headR = 17.0 * bodyScale;
        final torsoW = 62.0 * bodyScale;
        final torsoH = 70.0 * bodyScale;
        final headCenter = Offset(cx, cy - torsoH * 0.55 - headR * 0.6);
        final torsoTop = headCenter.dy + headR * 0.9;
        final torsoRect = Rect.fromLTWH(cx - torsoW / 2, torsoTop, torsoW, torsoH);
        final shoulder = Offset(cx - torsoW * 0.42, torsoTop + torsoH * 0.12);

        final bodyPaint = Paint()..color = _boneDeep.withValues(alpha: 0.28);
        // Head.
        canvas.drawCircle(headCenter, headR, bodyPaint);
        // Torso.
        canvas.drawRRect(RRect.fromRectAndRadius(torsoRect, Radius.circular(torsoW * 0.32)), bodyPaint);
        // Still (non-swinging) arm on the far side, for visual balance.
        canvas.drawRRect(
          RRect.fromRectAndRadius(Rect.fromLTWH(cx + torsoW * 0.3, torsoTop + torsoH * 0.15, 10 * bodyScale, torsoH * 0.75), Radius.circular(5 * bodyScale)),
          bodyPaint,
        );

        // Shoulder joint (the ball-and-socket itself).
        canvas.drawCircle(shoulder, 10 * bodyScale, boneDeepPaint..color = _boneDeep.withValues(alpha: 0.4));
        canvas.drawCircle(shoulder, 5.5 * bodyScale, boneDeepPaint..color = _boneDeep);

        // Swinging arm: a natural front-to-back range, hanging down at rest.
        final ang = _easeInOutHold(t) * 80 - 20; // -20..60 deg from vertical
        canvas.save();
        canvas.translate(shoulder.dx, shoulder.dy);
        canvas.rotate(ang * math.pi / 180);
        final armLen = torsoH * 0.85;
        canvas.drawRRect(RRect.fromRectAndRadius(Rect.fromLTWH(-5 * bodyScale, 0, 10 * bodyScale, armLen), Radius.circular(5 * bodyScale)), bonePaint);
        canvas.drawCircle(Offset(0, armLen), 6 * bodyScale, bonePaint); // hand
        canvas.restore();
        break;

      case _JointType.hinge:
        // Drawn as a leg (thigh + shin) bending at the knee, so the motion
        // reads as a real hinge joint rather than a floating rod.
        final bodyScale = (size.shortestSide / 200).clamp(0.6, 1.4);
        final hipY = cy - 78 * bodyScale;
        final kneeY = cy - 8 * bodyScale;
        final limbW = 15.0 * bodyScale;
        final bend = _easeInOutHold(t) * 100; // 0..100 deg, with a brief pause at each end
        // Hip anchor.
        canvas.drawRRect(RRect.fromRectAndRadius(Rect.fromLTWH(cx - limbW / 2, hipY, limbW, kneeY - hipY), Radius.circular(limbW / 2)), bonePaint);
        // Knee joint marker.
        canvas.drawCircle(Offset(cx, kneeY), limbW * 0.42, boneDeepPaint..color = _boneDeep.withValues(alpha: 0.5));
        // Shin, rotating at the knee.
        canvas.save();
        canvas.translate(cx, kneeY);
        canvas.rotate(bend * math.pi / 180);
        final shinLen = 78.0 * bodyScale;
        canvas.drawRRect(RRect.fromRectAndRadius(Rect.fromLTWH(-limbW / 2, 0, limbW, shinLen), Radius.circular(limbW / 2)), bonePaint);
        canvas.drawOval(Rect.fromCenter(center: Offset(0, shinLen + 6 * bodyScale), width: limbW * 1.6, height: limbW * 0.9), bonePaint); // foot
        canvas.restore();
        // Kneecap, drawn on top so it always faces forward like the textbook description.
        canvas.drawCircle(Offset(cx, kneeY - limbW * 0.15), limbW * 0.3, boneDeepPaint..color = _boneDeep.withValues(alpha: 0.85));
        break;

      case _JointType.pivot:
        // Drawn as a head atop the neck/spine, rotating side to side —
        // matches "shaking your head no" described in the info panel.
        final bodyScale = (size.shortestSide / 200).clamp(0.6, 1.4);
        final neckTopY = cy - 6 * bodyScale;
        final ang = (_easeInOutHold(t) - 0.5) * 90; // -45..45 deg
        // Shoulders/neck base (static, for context).
        canvas.drawRRect(
          RRect.fromRectAndRadius(Rect.fromLTWH(cx - 34 * bodyScale, neckTopY + 34 * bodyScale, 68 * bodyScale, 40 * bodyScale), Radius.circular(16 * bodyScale)),
          Paint()..color = _boneDeep.withValues(alpha: 0.22),
        );
        canvas.drawRRect(
          RRect.fromRectAndRadius(Rect.fromLTWH(cx - 9 * bodyScale, neckTopY, 18 * bodyScale, 40 * bodyScale), Radius.circular(9 * bodyScale)),
          boneDeepPaint..color = _boneDeep.withValues(alpha: 0.45),
        );
        // Rotating head.
        canvas.save();
        canvas.translate(cx, neckTopY);
        canvas.rotate(ang * math.pi / 180);
        canvas.drawCircle(Offset.zero, 30 * bodyScale, bonePaint);
        // A simple ear/nose marker (not a face) shows rotation direction clearly.
        canvas.drawRect(Rect.fromCenter(center: Offset(28 * bodyScale, 0), width: 5 * bodyScale, height: 12 * bodyScale), boneDeepPaint..color = _boneDeep.withValues(alpha: 0.7));
        canvas.restore();
        break;

      case _JointType.fixed:
        // Drawn as a simple skull outline with a visible suture line —
        // static, reinforcing that this joint does not move at all.
        final bodyScale = (size.shortestSide / 200).clamp(0.6, 1.4);
        final skullCenter = Offset(cx, cy - 8 * bodyScale);
        canvas.drawCircle(skullCenter, 40 * bodyScale, bonePaint);
        canvas.drawRRect(
          RRect.fromRectAndRadius(Rect.fromLTWH(cx - 14 * bodyScale, skullCenter.dy + 26 * bodyScale, 28 * bodyScale, 20 * bodyScale), Radius.circular(6 * bodyScale)),
          bonePaint,
        ); // jaw
        final suturePaint = Paint()
          ..color = _boneDeep.withValues(alpha: 0.75)
          ..style = PaintingStyle.stroke
          ..strokeWidth = 2;
        final suture = Path()
          ..moveTo(skullCenter.dx - 30 * bodyScale, skullCenter.dy - 18 * bodyScale)
          ..quadraticBezierTo(skullCenter.dx - 6 * bodyScale, skullCenter.dy - 30 * bodyScale, skullCenter.dx + 4 * bodyScale, skullCenter.dy - 12 * bodyScale)
          ..quadraticBezierTo(skullCenter.dx + 14 * bodyScale, skullCenter.dy, skullCenter.dx + 32 * bodyScale, skullCenter.dy - 4 * bodyScale);
        canvas.drawPath(suture, suturePaint);
        break;
    }
  }

  /// A smooth 0..1 oscillation that eases in/out of each extreme and holds
  /// briefly there, instead of a raw cosine's constant-speed sweep through
  /// the middle — reads as a deliberate, joint-like motion rather than a
  /// mechanical wobble.
  double _easeInOutHold(double t) {
    final phase = (t * 2) % 2; // 0..2, one full there-and-back cycle
    final leg = phase <= 1 ? phase : 2 - phase; // 0..1..0 triangle wave
    // Smoothstep for gentle ease at each end.
    return leg * leg * (3 - 2 * leg);
  }

  @override
  bool shouldRepaint(covariant _JointPainter oldDelegate) => oldDelegate.t != t || oldDelegate.joint != joint;
}
