import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// A live divisibility checker: type a number and watch each of the
/// 2, 3, 4, 5, 9, 10 check cards pop in with a staggered reveal, alongside
/// the digit-sum reasoning shown.
class PlayingNumbersSimulationWidget extends StatefulWidget {
  const PlayingNumbersSimulationWidget({super.key});

  @override
  State<PlayingNumbersSimulationWidget> createState() => _PlayingNumbersSimulationWidgetState();
}

class _PlayingNumbersSimulationWidgetState extends State<PlayingNumbersSimulationWidget> with SingleTickerProviderStateMixin {
  final TextEditingController _controller = TextEditingController(text: '4536');
  late AnimationController _animController;

  @override
  void initState() {
    super.initState();
    _animController = AnimationController(vsync: this, duration: const Duration(milliseconds: 700));
    _animController.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    _animController.dispose();
    super.dispose();
  }

  int get _digitSum {
    final n = int.tryParse(_controller.text) ?? 0;
    return n.abs().toString().split('').map(int.parse).reduce((a, b) => a + b);
  }

  @override
  Widget build(BuildContext context) {
    final n = int.tryParse(_controller.text) ?? 0;
    final checks = {
      '2': n % 2 == 0,
      '3': _digitSum % 3 == 0,
      '4': n % 100 % 4 == 0,
      '5': n % 10 == 0 || n % 10 == 5,
      '9': _digitSum % 9 == 0,
      '10': n % 10 == 0,
    };
    final entries = checks.entries.toList();

    return SimFrame(
      title: 'Divisibility Checker',
      icon: Icons.checklist,
      accent: Colors.deepPurple.shade400,
      description: 'Type a number and watch each check pop in, showing which small numbers it\'s divisible by and why.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          TextField(
            controller: _controller,
            keyboardType: TextInputType.number,
            onChanged: (_) => setState(() => _animController.forward(from: 0)),
            decoration: const InputDecoration(labelText: 'Enter a number', border: OutlineInputBorder(), isDense: true),
          ),
          const SizedBox(height: 8),
          Text('Digit sum: $_digitSum', style: TextStyle(fontSize: 12, color: Theme.of(context).colorScheme.onSurfaceVariant)),
          const SizedBox(height: 12),
          AnimatedBuilder(
            animation: _animController,
            builder: (context, _) {
              return Wrap(
                spacing: 10,
                runSpacing: 10,
                children: List.generate(entries.length, (i) {
                  final e = entries[i];
                  final start = i / entries.length * 0.6;
                  final end = start + 0.4;
                  final localT = ((_animController.value - start) / (end - start)).clamp(0.0, 1.0);
                  final eased = Curves.easeOutBack.transform(localT);
                  return Opacity(
                    opacity: eased.clamp(0.0, 1.0),
                    child: Transform.scale(
                      scale: eased.clamp(0.0, 1.0),
                      child: Container(
                        width: 70,
                        padding: const EdgeInsets.symmetric(vertical: 10),
                        decoration: BoxDecoration(color: e.value ? Colors.green.shade50 : Colors.red.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: e.value ? Colors.green.shade200 : Colors.red.shade200)),
                        child: Column(
                          children: [
                            Text('÷ ${e.key}', style: TextStyle(fontWeight: FontWeight.bold)),
                            const SizedBox(height: 4),
                            Icon(e.value ? Icons.check_circle : Icons.cancel, color: e.value ? Colors.green : Colors.red, size: 20),
                          ],
                        ),
                      ),
                    ),
                  );
                }),
              );
            },
          ),
        ],
      ),
    );
  }
}
