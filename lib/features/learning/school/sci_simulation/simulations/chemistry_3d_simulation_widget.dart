import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class Chemistry3DSimulationWidget extends StatefulWidget {
  const Chemistry3DSimulationWidget({super.key});

  @override
  State<Chemistry3DSimulationWidget> createState() => _Chemistry3DSimulationWidgetState();
}

class _Chemistry3DSimulationWidgetState extends State<Chemistry3DSimulationWidget> with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  double _rotationAngle = 0.0;
  String selectedMolecule = "Water (H₂O)";

  final Map<String, List<Map<String, dynamic>>> molecules = {
    "Water (H₂O)": [
      {"name": "Oxygen", "color": Colors.red, "x": 0.0, "y": -20.0, "size": 50.0},
      {"name": "Hydrogen", "color": Colors.blue, "x": -50.0, "y": 30.0, "size": 30.0},
      {"name": "Hydrogen", "color": Colors.blue, "x": 50.0, "y": 30.0, "size": 30.0},
    ],
    "Carbon Dioxide (CO₂)": [
      {"name": "Oxygen", "color": Colors.red, "x": -70.0, "y": 0.0, "size": 40.0},
      {"name": "Carbon", "color": Colors.grey, "x": 0.0, "y": 0.0, "size": 50.0},
      {"name": "Oxygen", "color": Colors.red, "x": 70.0, "y": 0.0, "size": 40.0},
    ],
  };

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 10))
      ..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 4,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(Icons.view_in_ar, color: Colors.deepPurple),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(TrilingualService.instance.getUIText('3D Molecular Structure Sandbox'),
                    style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                    overflow: TextOverflow.ellipsis,
                  ),
                ),
                const SizedBox(width: 8),
                DropdownButton<String>(
                  value: selectedMolecule,
                  items: molecules.keys.map((String key) {
                    return DropdownMenuItem<String>(
                      value: key,
                      child: Text(key, style: TextStyle(fontSize: 14)),
                    );
                  }).toList(),
                  onChanged: (val) {
                    if (val != null) setState(() => selectedMolecule = val);
                  },
                ),
              ],
            ),
            const Divider(height: 24),
            Center(
              child: GestureDetector(
                onPanUpdate: (details) {
                  setState(() {
                    _rotationAngle += details.delta.dx * 0.02;
                  });
                },
                child: Container(
                  height: 220,
                  width: double.infinity,
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      colors: [Colors.deepPurple.shade900, Colors.indigo.shade800],
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                    ),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: AnimatedBuilder(
                    animation: _controller,
                    builder: (context, child) {
                      double angle = _rotationAngle + (_controller.value * 2 * math.pi);
                      return Stack(
                        alignment: Alignment.center,
                        children: [
                          Positioned(
                            bottom: 12,
                            child: Text(TrilingualService.instance.getUIText('Drag horizontally to rotate 3D view'),
                              style: TextStyle(color: Colors.white70, fontSize: 12),
                            ),
                          ),
                          ...molecules[selectedMolecule]!.map((atom) {
                            double currentX = atom['x'] * math.cos(angle);
                            return Transform(
                              transform: Matrix4.identity()
                                ..setEntry(3, 2, 0.001)
                                ..rotateY(angle),
                              alignment: Alignment.center,
                              child: Transform.translate(
                                offset: Offset(currentX, atom['y']),
                                child: Container(
                                  width: atom['size'],
                                  height: atom['size'],
                                  decoration: BoxDecoration(
                                    color: atom['color'],
                                    shape: BoxShape.circle,
                                    boxShadow: [
                                      BoxShadow(
                                        color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.5),
                                        blurRadius: 10,
                                        offset: const Offset(4, 4),
                                      ),
                                    ],
                                    gradient: RadialGradient(
                                      colors: [Colors.white, atom['color']],
                                      center: const Alignment(-0.3, -0.3),
                                    ),
                                  ),
                                  child: Center(
                                    child: Text(
                                      atom['name'][0],
                                      style: TextStyle(
                                        color: Colors.white,
                                        fontWeight: FontWeight.bold,
                                      ),
                                    ),
                                  ),
                                ),
                              ),
                            );
                          }),
                        ],
                      );
                    },
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
