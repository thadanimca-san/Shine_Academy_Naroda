import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:path_drawing/path_drawing.dart';
import '../../../../foundation/theme/app_colors.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class AnimatedDiagramWidget extends StatefulWidget {
  final Map<String, dynamic> data;

  const AnimatedDiagramWidget({super.key, required this.data});

  @override
  State<AnimatedDiagramWidget> createState() => _AnimatedDiagramWidgetState();
}

class _AnimatedDiagramWidgetState extends State<AnimatedDiagramWidget> with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  List<Path> _paths = [];
  double _speedMultiplier = 1.0;
  bool _isPlaying = false;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 4),
    );

    _controller.addStatusListener((status) {
      if (status == AnimationStatus.completed) {
        if (mounted) setState(() => _isPlaying = false);
      }
    });

    final List<dynamic> rawPaths = widget.data['content']?['paths'] ?? [];
    for (var pathStr in rawPaths) {
      _paths.add(parseSvgPathData(pathStr));
    }
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _togglePlay() {
    if (_controller.isAnimating) {
      _controller.stop();
      setState(() => _isPlaying = false);
    } else {
      if (_controller.isCompleted) _controller.reset();
      _controller.duration = Duration(milliseconds: (4000 / _speedMultiplier).round());
      _controller.forward();
      setState(() => _isPlaying = true);
    }
  }

  void _setSpeed(double speed) {
    setState(() {
      _speedMultiplier = speed;
      if (_controller.isAnimating) {
        _controller.duration = Duration(milliseconds: (4000 / _speedMultiplier).round());
        _controller.forward(from: _controller.value);
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.symmetric(vertical: 16),
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: AppColors.primary.withValues(alpha: 0.3), width: 2),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Text(
            widget.data['content']?['title'] ?? 'Animated Diagram',
            style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: AppColors.primary),
            textAlign: TextAlign.center,
          ),
          if (widget.data['content']?['description'] != null)
            Padding(
              padding: const EdgeInsets.only(top: 8.0, bottom: 16.0),
              child: Text(
                widget.data['content']!['description'],
                style: TextStyle(fontSize: 16, color: Theme.of(context).colorScheme.onSurface),
                textAlign: TextAlign.center,
              ),
            ),
          const SizedBox(height: 16),
          
          Container(
            height: 300,
            width: double.infinity,
            decoration: BoxDecoration(
              color: Colors.grey[50],
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: Colors.grey[300]!),
            ),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, child) {
                return CustomPaint(
                  painter: _PathPainter(_paths, _controller.value, widget.data['content']?['stroke_color']),
                  size: Size.infinite,
                );
              },
            ),
          ),
          
          const SizedBox(height: 24),
          
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              IconButton(
                icon: Icon(_isPlaying ? Icons.pause_circle_filled : Icons.play_circle_fill),
                color: AppColors.primary,
                iconSize: 48,
                onPressed: _togglePlay,
              ),
              const SizedBox(width: 24),
              Text(TrilingualService.instance.getUIText("Speed:"), style: TextStyle(fontWeight: FontWeight.bold)),
              const SizedBox(width: 8),
              _buildSpeedButton(1.0, "1x"),
              const SizedBox(width: 8),
              _buildSpeedButton(2.0, "2x"),
              const SizedBox(width: 8),
              _buildSpeedButton(4.0, "4x"),
            ],
          )
        ],
      ),
    );
  }

  Widget _buildSpeedButton(double speed, String label) {
    final isSelected = _speedMultiplier == speed;
    return InkWell(
      onTap: () => _setSpeed(speed),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
        decoration: BoxDecoration(
          color: isSelected ? AppColors.primary : Colors.grey[200],
          borderRadius: BorderRadius.circular(16),
        ),
        child: Text(
          label,
          style: TextStyle(
            color: isSelected ? Colors.white : Colors.black87,
            fontWeight: FontWeight.bold,
          ),
        ),
      ),
    );
  }
}

class _PathPainter extends CustomPainter {
  final List<Path> paths;
  final double progress;
  final String? colorHex;

  _PathPainter(this.paths, this.progress, this.colorHex);

  @override
  void paint(Canvas canvas, Size size) {
    Color strokeColor = Colors.blue;
    if (colorHex != null) {
      try { strokeColor = Color(int.parse(colorHex!.replaceAll('#', '0xFF'))); } catch (_) {}
    }

    final paint = Paint()
      ..color = strokeColor
      ..style = PaintingStyle.stroke
      ..strokeWidth = 4.0
      ..strokeCap = StrokeCap.round
      ..strokeJoin = StrokeJoin.round;

    for (var path in paths) {
      final bounds = path.getBounds();
      if (bounds.isEmpty) continue;

      final scaleX = size.width / (bounds.width > 0 ? bounds.width + 40 : 100);
      final scaleY = size.height / (bounds.height > 0 ? bounds.height + 40 : 100);
      final scale = scaleX < scaleY ? scaleX : scaleY;

      final matrix = Matrix4.identity()
        ..translate(
          (size.width - bounds.width * scale) / 2 - bounds.left * scale,
          (size.height - bounds.height * scale) / 2 - bounds.top * scale,
        )
        ..scale(scale, scale);

      final scaledPath = path.transform(matrix.storage);

      for (final metric in scaledPath.computeMetrics()) {
        final length = metric.length;
        final extractPath = metric.extractPath(0.0, length * progress);
        canvas.drawPath(extractPath, paint);
      }
    }
  }

  @override
  bool shouldRepaint(_PathPainter oldDelegate) {
    return oldDelegate.progress != progress || oldDelegate.paths != paths;
  }
}
