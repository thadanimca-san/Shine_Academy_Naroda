import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A pH scale you can slide from 0 to 14: the indicator strip and verdict
/// update live, plus common substance markers along the scale for context.
class Class10AcidsBasesSaltsSimulationWidget extends StatefulWidget {
  const Class10AcidsBasesSaltsSimulationWidget({super.key});

  @override
  State<Class10AcidsBasesSaltsSimulationWidget> createState() => _Class10AcidsBasesSaltsSimulationWidgetState();
}

class _Class10AcidsBasesSaltsSimulationWidgetState extends State<Class10AcidsBasesSaltsSimulationWidget> {
  double _ph = 7;

  static const _markers = [
    (1.0, 'Battery Acid'),
    (2.4, 'Lemon Juice'),
    (4.0, 'Vinegar'),
    (7.0, 'Pure Water'),
    (9.0, 'Baking Soda'),
    (12.0, 'Ammonia'),
    (14.0, 'Caustic Soda'),
  ];

  Color get _phColor {
    if (_ph < 3) return Colors.red.shade700;
    if (_ph < 6) return Colors.orange;
    if (_ph < 7.5) return Colors.green;
    if (_ph < 11) return Colors.blue;
    return Colors.indigo.shade700;
  }

  String get _verdict {
    if (_ph < 6.5) return 'Acidic';
    if (_ph > 7.5) return 'Basic';
    return 'Neutral';
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'The pH Scale',
      icon: Icons.science,
      accent: Colors.purple.shade600,
      description: 'Slide along the pH scale to see how acidity and basicity relate to everyday substances.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 46,
            width: double.infinity,
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(8),
              gradient: const LinearGradient(colors: [Colors.red, Colors.orange, Colors.yellow, Colors.green, Colors.blue, Colors.indigo, Colors.purple]),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'pH Value', value: _ph.toStringAsFixed(1), color: _phColor),
            SimMetric(label: 'Nature', value: _verdict, color: _phColor),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'pH: ${_ph.toStringAsFixed(1)}',
            value: _ph,
            min: 0,
            max: 14,
            divisions: 28,
            activeColor: _phColor,
            onChanged: (val) => setState(() => _ph = val),
          ),
          const SizedBox(height: 10),
          Text(TrilingualService.instance.getUIText('Reference Points'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12.5, color: Theme.of(context).colorScheme.onSurfaceVariant)),
          const SizedBox(height: 6),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: _markers.map((m) {
              return ActionChip(
                label: Text('${m.$2} (${m.$1})', style: TextStyle(fontSize: 11.5)),
                onPressed: () => setState(() => _ph = m.$1),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }
}
