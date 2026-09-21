import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Two side-by-side pollution sliders: as air/water pollution levels rise,
/// the sky greys out with smog and the water darkens and clouds over —
/// a direct visual link between pollutant levels and environmental impact.
class PollutionSimulationWidget extends StatefulWidget {
  const PollutionSimulationWidget({super.key});

  @override
  State<PollutionSimulationWidget> createState() => _PollutionSimulationWidgetState();
}

class _PollutionSimulationWidgetState extends State<PollutionSimulationWidget> {
  double _airPollution = 0.2;
  double _waterPollution = 0.2;

  String _levelLabel(double v) {
    if (v < 0.3) return 'Clean';
    if (v < 0.65) return 'Moderate';
    return 'Severe';
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Pollution Visualiser',
      icon: Icons.cloud,
      accent: Colors.blueGrey.shade700,
      description: 'Drag the sliders to see how rising pollution levels change the look of the sky and water.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Expanded(
                child: Column(
                  children: [
                    Text(TrilingualService.instance.getUIText('Air'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12)),
                    const SizedBox(height: 6),
                    Container(
                      height: 130,
                      decoration: BoxDecoration(
                        gradient: LinearGradient(colors: [Color.lerp(const Color(0xFF81D4FA), const Color(0xFF757575), _airPollution)!, Color.lerp(const Color(0xFFE1F5FE), const Color(0xFFBDBDBD), _airPollution)!], begin: Alignment.topCenter, end: Alignment.bottomCenter),
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: Icon(Icons.factory, color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.3 + _airPollution * 0.4), size: 40),
                    ),
                  ],
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: Column(
                  children: [
                    Text(TrilingualService.instance.getUIText('Water'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12)),
                    const SizedBox(height: 6),
                    Container(
                      height: 130,
                      decoration: BoxDecoration(
                        gradient: LinearGradient(colors: [Color.lerp(const Color(0xFF4FC3F7), const Color(0xFF4E342E), _waterPollution)!, Color.lerp(const Color(0xFF0288D1), const Color(0xFF3E2723), _waterPollution)!], begin: Alignment.topCenter, end: Alignment.bottomCenter),
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: Icon(Icons.water, color: Colors.white.withValues(alpha: 0.5), size: 40),
                    ),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Air Quality', value: _levelLabel(_airPollution), color: _airPollution < 0.3 ? Colors.green : (_airPollution < 0.65 ? Colors.orange : Colors.red)),
            SimMetric(label: 'Water Quality', value: _levelLabel(_waterPollution), color: _waterPollution < 0.3 ? Colors.green : (_waterPollution < 0.65 ? Colors.orange : Colors.red)),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Air pollution level',
            value: _airPollution,
            min: 0,
            max: 1,
            divisions: 20,
            activeColor: Colors.blueGrey,
            onChanged: (val) => setState(() => _airPollution = val),
          ),
          SimSlider(
            label: 'Water pollution level',
            value: _waterPollution,
            min: 0,
            max: 1,
            divisions: 20,
            activeColor: Colors.brown,
            onChanged: (val) => setState(() => _waterPollution = val),
          ),
        ],
      ),
    );
  }
}
