import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A groundwater cross-section: pump water out via a well and watch the
/// water table drop; let rain recharge it back up.
class WaterResourceSimulationWidget extends StatefulWidget {
  const WaterResourceSimulationWidget({super.key});

  @override
  State<WaterResourceSimulationWidget> createState() => _WaterResourceSimulationWidgetState();
}

class _WaterResourceSimulationWidgetState extends State<WaterResourceSimulationWidget> {
  double _waterTableLevel = 0.6; // 0 = empty, 1 = full (fraction of ground height)

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'The Water Table',
      icon: Icons.water,
      accent: Colors.blue.shade700,
      description: 'Pump groundwater out through the well and watch the water table fall. Rainwater recharges it back up.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 170,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.brown.shade100, borderRadius: BorderRadius.circular(10)),
            clipBehavior: Clip.antiAlias,
            child: Stack(
              children: [
                Positioned(
                  left: 0,
                  right: 0,
                  bottom: 0,
                  height: 170 * _waterTableLevel,
                  child: Container(color: Colors.blue.withValues(alpha: 0.45)),
                ),
                Positioned(
                  left: 0,
                  right: 0,
                  bottom: 170 * _waterTableLevel - 1,
                  child: Container(height: 2, color: Colors.blue.shade800),
                ),
                Positioned(
                  top: 10,
                  right: 20,
                  child: Column(
                    children: [
                      Icon(Icons.water_drop, color: Colors.blue),
                      Container(width: 10, height: 40, color: Colors.grey.shade500),
                    ],
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Water Table', value: '${(_waterTableLevel * 100).toStringAsFixed(0)}%', color: Colors.blue),
            SimMetric(label: 'Status', value: _waterTableLevel < 0.3 ? 'Critically Low' : (_waterTableLevel < 0.6 ? 'Moderate' : 'Healthy'), color: _waterTableLevel < 0.3 ? Colors.red : Colors.green),
          ]),
          const SizedBox(height: 14),
          Row(
            children: [
              Expanded(
                child: OutlinedButton.icon(
                  onPressed: _waterTableLevel <= 0.05 ? null : () => setState(() => _waterTableLevel = (_waterTableLevel - 0.15).clamp(0.0, 1.0)),
                  icon: Icon(Icons.arrow_downward),
                  label: Text(TrilingualService.instance.getUIText('Pump Water Out')),
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: ElevatedButton.icon(
                  onPressed: _waterTableLevel >= 0.95 ? null : () => setState(() => _waterTableLevel = (_waterTableLevel + 0.15).clamp(0.0, 1.0)),
                  icon: Icon(Icons.cloudy_snowing),
                  label: Text(TrilingualService.instance.getUIText('Rainwater Recharge')),
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.blue.shade700, foregroundColor: Colors.white),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
