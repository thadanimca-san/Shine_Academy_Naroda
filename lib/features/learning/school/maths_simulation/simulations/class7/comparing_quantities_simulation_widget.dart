import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A shopkeeper calculator: adjust cost price and selling price to see
/// profit/loss percentage live, with an animated bar that grows or
/// shrinks to the new percentage; plus a simple-interest calculator
/// toggle whose interest bar fills the same way.
class ComparingQuantitiesSimulationWidget extends StatefulWidget {
  const ComparingQuantitiesSimulationWidget({super.key});

  @override
  State<ComparingQuantitiesSimulationWidget> createState() => _ComparingQuantitiesSimulationWidgetState();
}

class _ComparingQuantitiesSimulationWidgetState extends State<ComparingQuantitiesSimulationWidget> with SingleTickerProviderStateMixin {
  bool _showInterest = false;
  double _cp = 500;
  double _sp = 600;
  double _principal = 2000;
  double _rate = 6;
  double _time = 3;

  double _prevPct = 20;
  double _prevSi = 360;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 500));
    _controller.value = 1;
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Profit/Loss & Simple Interest',
      icon: Icons.percent,
      accent: Colors.green.shade700,
      description: 'Explore how profit/loss percentage and simple interest respond to the numbers involved.',
      actions: [
        ToggleButtons(
          isSelected: [!_showInterest, _showInterest],
          onPressed: (i) => setState(() {
            _showInterest = i == 1;
            _controller.value = 1;
          }),
          borderRadius: BorderRadius.circular(8),
          selectedColor: Colors.white,
          fillColor: Colors.green.shade700,
          constraints: const BoxConstraints(minHeight: 34, minWidth: 60),
          children: [Text(TrilingualService.instance.getUIText('Profit/Loss')), Text(TrilingualService.instance.getUIText('Interest'))],
        ),
      ],
      child: _showInterest ? _buildInterest() : _buildProfitLoss(),
    );
  }

  Widget _buildProfitLoss() {
    final diff = _sp - _cp;
    final isProfit = diff >= 0;
    final pct = (diff.abs() / _cp) * 100;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        AnimatedBuilder(
          animation: _controller,
          builder: (context, _) {
            final eased = Curves.easeOutBack.transform(_controller.value);
            final animPct = _prevPct + (pct - _prevPct) * eased;
            final barWidth = (animPct.clamp(0, 100) / 100) * 260;
            return Container(
              height: 34,
              width: double.infinity,
              padding: const EdgeInsets.symmetric(horizontal: 4),
              decoration: BoxDecoration(color: Colors.grey.shade100, borderRadius: BorderRadius.circular(8)),
              child: Align(
                alignment: Alignment.centerLeft,
                child: Container(
                  width: barWidth.clamp(4, 400),
                  height: 24,
                  alignment: Alignment.centerRight,
                  padding: const EdgeInsets.only(right: 6),
                  decoration: BoxDecoration(color: isProfit ? Colors.green.shade400 : Colors.red.shade300, borderRadius: BorderRadius.circular(6)),
                  child: Text('${animPct.toStringAsFixed(1)}%', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 11)),
                ),
              ),
            );
          },
        ),
        const SizedBox(height: 12),
        SimMetricPanel(metrics: [
          SimMetric(label: 'Cost Price', value: '₹${_cp.toStringAsFixed(0)}'),
          SimMetric(label: 'Selling Price', value: '₹${_sp.toStringAsFixed(0)}'),
          SimMetric(label: isProfit ? 'Profit %' : 'Loss %', value: '${pct.toStringAsFixed(1)}%', color: isProfit ? Colors.green : Colors.red),
        ]),
        const SizedBox(height: 14),
        SimSlider(label: 'Cost Price: ₹${_cp.toStringAsFixed(0)}', value: _cp, min: 100, max: 2000, divisions: 38, activeColor: Colors.green, onChanged: (v) => setState(() {
          _prevPct = pct;
          _cp = v;
          _controller.forward(from: 0);
        })),
        SimSlider(label: 'Selling Price: ₹${_sp.toStringAsFixed(0)}', value: _sp, min: 100, max: 2000, divisions: 38, activeColor: Colors.teal, onChanged: (v) => setState(() {
          _prevPct = pct;
          _sp = v;
          _controller.forward(from: 0);
        })),
      ],
    );
  }

  Widget _buildInterest() {
    final si = (_principal * _rate * _time) / 100;
    final maxSi = 15000.0;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        AnimatedBuilder(
          animation: _controller,
          builder: (context, _) {
            final eased = Curves.easeOutBack.transform(_controller.value);
            final animSi = _prevSi + (si - _prevSi) * eased;
            final barWidth = (animSi.clamp(0, maxSi) / maxSi) * 260;
            return Container(
              height: 34,
              width: double.infinity,
              padding: const EdgeInsets.symmetric(horizontal: 4),
              decoration: BoxDecoration(color: Colors.grey.shade100, borderRadius: BorderRadius.circular(8)),
              child: Align(
                alignment: Alignment.centerLeft,
                child: Container(
                  width: barWidth.clamp(4, 400),
                  height: 24,
                  alignment: Alignment.centerRight,
                  padding: const EdgeInsets.only(right: 6),
                  decoration: BoxDecoration(color: Colors.deepOrange.shade300, borderRadius: BorderRadius.circular(6)),
                  child: Text('₹${animSi.toStringAsFixed(0)}', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 11)),
                ),
              ),
            );
          },
        ),
        const SizedBox(height: 12),
        SimMetricPanel(metrics: [
          SimMetric(label: 'Principal', value: '₹${_principal.toStringAsFixed(0)}'),
          SimMetric(label: 'Rate', value: '${_rate.toStringAsFixed(0)}%'),
          SimMetric(label: 'Simple Interest', value: '₹${si.toStringAsFixed(0)}', color: Colors.deepOrange),
        ]),
        const SizedBox(height: 14),
        SimSlider(label: 'Principal: ₹${_principal.toStringAsFixed(0)}', value: _principal, min: 500, max: 10000, divisions: 19, activeColor: Colors.green, onChanged: (v) => setState(() {
          _prevSi = si;
          _principal = v;
          _controller.forward(from: 0);
        })),
        SimSlider(label: 'Rate: ${_rate.toStringAsFixed(0)}% per annum', value: _rate, min: 1, max: 15, divisions: 14, activeColor: Colors.teal, onChanged: (v) => setState(() {
          _prevSi = si;
          _rate = v;
          _controller.forward(from: 0);
        })),
        SimSlider(label: 'Time: ${_time.toStringAsFixed(0)} years', value: _time, min: 1, max: 10, divisions: 9, activeColor: Colors.indigo, onChanged: (v) => setState(() {
          _prevSi = si;
          _time = v;
          _controller.forward(from: 0);
        })),
      ],
    );
  }
}
