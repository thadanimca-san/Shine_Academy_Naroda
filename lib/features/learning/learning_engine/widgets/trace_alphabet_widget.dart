import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import '../../../../foundation/theme/app_colors.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _AlwaysWinPanGestureRecognizer extends PanGestureRecognizer {
  @override
  void addPointer(PointerDownEvent event) {
    super.addPointer(event);
    resolve(GestureDisposition.accepted);
  }
}

class TraceAlphabetWidget extends StatefulWidget {
  final Map<String, dynamic> data;

  const TraceAlphabetWidget({super.key, required this.data});

  @override
  State<TraceAlphabetWidget> createState() => _TraceAlphabetWidgetState();
}

class _TraceAlphabetWidgetState extends State<TraceAlphabetWidget> with SingleTickerProviderStateMixin {
  List<Offset?> _points = [];
  bool _isDone = false;
  late AnimationController _controller;
  late Animation<double> _scaleAnimation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 600));
    _scaleAnimation = Tween<double>(begin: 1.0, end: 1.2).animate(
      CurvedAnimation(parent: _controller, curve: Curves.elasticOut),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _markDone() {
    setState(() => _isDone = true);
    _controller.forward(from: 0.0);
  }

  void _clear() {
    setState(() {
      _points.clear();
      _isDone = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    final letter = widget.data['letter'] ?? 'A';

    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: Colors.grey.shade300, width: 2),
      ),
      child: Column(
        children: [
          Text(TrilingualService.instance.getUIText('Trace the Letter!'),
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface),
          ),
          const SizedBox(height: 24),
          Stack(
            alignment: Alignment.center,
            children: [
              // Constrained Background Box
              Container(
                width: 300,
                height: 300,
                decoration: BoxDecoration(
                  color: Colors.grey.shade50,
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(color: Colors.grey.shade300, width: 2),
                ),
                alignment: Alignment.center,
                child: ScaleTransition(
                  scale: _scaleAnimation,
                  child: Padding(
                    padding: const EdgeInsets.all(24.0),
                    child: FittedBox(
                      fit: BoxFit.contain,
                      child: Text(
                        letter,
                        style: TextStyle(
                          fontSize: letter.length > 1 ? 150 : 250,
                          fontWeight: FontWeight.w900,
                          color: _isDone ? Colors.green : Colors.grey.shade400,
                          fontFamily: 'monospace',
                        ),
                      ),
                    ),
                  ),
                ),
              ),
              if (!_isDone)
                // Constrained Drawing Area perfectly aligned with the Background Box
                SizedBox(
                  width: 300,
                  height: 300,
                  child: Builder(
                    builder: (innerContext) => RawGestureDetector(
                      gestures: {
                        _AlwaysWinPanGestureRecognizer: GestureRecognizerFactoryWithHandlers<_AlwaysWinPanGestureRecognizer>(
                          () => _AlwaysWinPanGestureRecognizer(),
                          (_AlwaysWinPanGestureRecognizer instance) {
                            instance.onStart = (details) {
                              RenderBox renderBox = innerContext.findRenderObject() as RenderBox;
                              setState(() {
                                _points.add(renderBox.globalToLocal(details.globalPosition));
                              });
                            };
                            instance.onUpdate = (details) {
                              RenderBox renderBox = innerContext.findRenderObject() as RenderBox;
                              setState(() {
                                _points.add(renderBox.globalToLocal(details.globalPosition));
                              });
                            };
                            instance.onEnd = (details) {
                              setState(() {
                                _points.add(null);
                              });
                            };
                          },
                        ),
                      },
                      child: ClipRRect(
                        borderRadius: BorderRadius.circular(20),
                        child: CustomPaint(
                          painter: _DrawingPainter(_points),
                          size: const Size(300, 300),
                        ),
                      ),
                    ),
                  ),
                ),
            ],
          ),
          const SizedBox(height: 24),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              TextButton.icon(
                onPressed: _clear,
                icon: Icon(Icons.refresh),
                label: Text(TrilingualService.instance.getUIText('Clear')),
                style: TextButton.styleFrom(foregroundColor: Colors.red),
              ),
              FilledButton.icon(
                onPressed: _isDone ? null : _markDone,
                icon: Icon(Icons.star),
                label: Text(TrilingualService.instance.getUIText('I did it!')),
                style: FilledButton.styleFrom(
                  backgroundColor: Colors.green,
                  padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class _DrawingPainter extends CustomPainter {
  final List<Offset?> points;

  _DrawingPainter(this.points);

  @override
  void paint(Canvas canvas, Size size) {
    Paint paint = Paint()
      ..color = Colors.orange
      ..strokeCap = StrokeCap.round
      ..strokeWidth = 15.0;

    for (int i = 0; i < points.length - 1; i++) {
      if (points[i] != null && points[i + 1] != null) {
        canvas.drawLine(points[i]!, points[i + 1]!, paint);
      }
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => true;
}
