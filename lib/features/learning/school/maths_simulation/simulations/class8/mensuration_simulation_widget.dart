import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A resizable cuboid/cylinder outline that eases smoothly to its new
/// dimensions whenever a slider moves, while surface area and volume
/// recompute live.
class MensurationSimulationWidget extends StatefulWidget {
  const MensurationSimulationWidget({super.key});

  @override
  State<MensurationSimulationWidget> createState() => _MensurationSimulationWidgetState();
}

class _MensurationSimulationWidgetState extends State<MensurationSimulationWidget> with SingleTickerProviderStateMixin {
  bool _isCylinder = false;
  double _l = 6, _b = 4, _h = 5;
  double _r = 3, _hCyl = 6;
  late AnimationController _controller;

  // The dimension values the shape is easing from -> to, captured whenever
  // a slider changes so the outline glides rather than snaps.
  double _fromW = 6 * 14, _fromH = 5 * 14;
  double _toW = 6 * 14, _toH = 5 * 14;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 350));
    _controller.value = 1;
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _animateTo(double w, double h) {
    final t = Curves.easeInOut.transform(_controller.value);
    final currentW = _fromW + (_toW - _fromW) * t;
    final currentH = _fromH + (_toH - _fromH) * t;
    _fromW = currentW;
    _fromH = currentH;
    _toW = w;
    _toH = h;
    _controller.forward(from: 0);
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Volume & Surface Area',
      icon: Icons.view_in_ar,
      accent: Colors.blue.shade700,
      description: 'Resize a cuboid or cylinder and watch it smoothly reshape as surface area and volume update.',
      actions: [
        ToggleButtons(
          isSelected: [!_isCylinder, _isCylinder],
          onPressed: (i) => setState(() {
            _isCylinder = i == 1;
            final dims = _isCylinder ? (_r * 24, _hCyl * 14) : (_l * 14, _h * 14);
            _fromW = dims.$1;
            _fromH = dims.$2;
            _toW = dims.$1;
            _toH = dims.$2;
            _controller.value = 1;
          }),
          borderRadius: BorderRadius.circular(8),
          selectedColor: Colors.white,
          fillColor: Colors.blue.shade700,
          constraints: const BoxConstraints(minHeight: 34, minWidth: 60),
          children: [Text(TrilingualService.instance.getUIText('Cuboid')), Text(TrilingualService.instance.getUIText('Cylinder'))],
        ),
      ],
      child: _isCylinder ? _buildCylinder() : _buildCuboid(),
    );
  }

  Widget _buildCuboid() {
    final sa = 2 * (_l * _b + _b * _h + _h * _l);
    final vol = _l * _b * _h;
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Container(
          height: 150,
          width: double.infinity,
          decoration: BoxDecoration(color: Colors.blue.shade50, borderRadius: BorderRadius.circular(10)),
          child: Center(
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final t = Curves.easeInOut.transform(_controller.value);
                final w = _fromW + (_toW - _fromW) * t;
                final h = _fromH + (_toH - _fromH) * t;
                return Container(
                  width: w,
                  height: h,
                  decoration: BoxDecoration(border: Border.all(color: Colors.blue.shade700, width: 2), color: Colors.blue.shade200),
                );
              },
            ),
          ),
        ),
        const SizedBox(height: 12),
        SimMetricPanel(metrics: [
          SimMetric(label: 'Surface Area', value: '${sa.toStringAsFixed(0)} cm²', color: Colors.deepOrange),
          SimMetric(label: 'Volume', value: '${vol.toStringAsFixed(0)} cm³', color: Colors.teal),
        ]),
        const SizedBox(height: 14),
        SimSlider(label: 'Length: ${_l.toStringAsFixed(0)} cm', value: _l, min: 1, max: 10, divisions: 9, activeColor: Colors.blue, onChanged: (v) => setState(() { _l = v; _animateTo(_l * 14, _h * 14); })),
        SimSlider(label: 'Breadth: ${_b.toStringAsFixed(0)} cm', value: _b, min: 1, max: 10, divisions: 9, activeColor: Colors.teal, onChanged: (v) => setState(() => _b = v)),
        SimSlider(label: 'Height: ${_h.toStringAsFixed(0)} cm', value: _h, min: 1, max: 10, divisions: 9, activeColor: Colors.indigo, onChanged: (v) => setState(() { _h = v; _animateTo(_l * 14, _h * 14); })),
      ],
    );
  }

  Widget _buildCylinder() {
    const pi = 3.14159265;
    final csa = 2 * pi * _r * _hCyl;
    final tsa = csa + 2 * pi * _r * _r;
    final vol = pi * _r * _r * _hCyl;
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Container(
          height: 150,
          width: double.infinity,
          decoration: BoxDecoration(color: Colors.blue.shade50, borderRadius: BorderRadius.circular(10)),
          child: Center(
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final t = Curves.easeInOut.transform(_controller.value);
                final w = _fromW + (_toW - _fromW) * t;
                final h = _fromH + (_toH - _fromH) * t;
                return Container(
                  width: w,
                  height: h,
                  decoration: BoxDecoration(border: Border.all(color: Colors.blue.shade700, width: 2), color: Colors.blue.shade200, borderRadius: BorderRadius.circular(12)),
                );
              },
            ),
          ),
        ),
        const SizedBox(height: 12),
        SimMetricPanel(metrics: [
          SimMetric(label: 'Total Surface Area', value: '${tsa.toStringAsFixed(0)} cm²', color: Colors.deepOrange),
          SimMetric(label: 'Volume', value: '${vol.toStringAsFixed(0)} cm³', color: Colors.teal),
        ]),
        const SizedBox(height: 14),
        SimSlider(label: 'Radius: ${_r.toStringAsFixed(0)} cm', value: _r, min: 1, max: 8, divisions: 7, activeColor: Colors.blue, onChanged: (v) => setState(() { _r = v; _animateTo(_r * 24, _hCyl * 14); })),
        SimSlider(label: 'Height: ${_hCyl.toStringAsFixed(0)} cm', value: _hCyl, min: 1, max: 10, divisions: 9, activeColor: Colors.indigo, onChanged: (v) => setState(() { _hCyl = v; _animateTo(_r * 24, _hCyl * 14); })),
      ],
    );
  }
}
