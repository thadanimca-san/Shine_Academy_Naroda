import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// A tap-to-explore checklist of which arithmetic properties (closure,
/// commutativity, associativity) hold for rational numbers under each
/// operation — each row slides and fades in with a stagger when the
/// operation changes.
class Class8RationalNumbersSimulationWidget extends StatefulWidget {
  const Class8RationalNumbersSimulationWidget({super.key});

  @override
  State<Class8RationalNumbersSimulationWidget> createState() => _RationalNumbersSimulationWidgetState();
}

class _RationalNumbersSimulationWidgetState extends State<Class8RationalNumbersSimulationWidget> with SingleTickerProviderStateMixin {
  int _opIndex = 0; // 0=add,1=sub,2=mul,3=div
  static const _ops = ['Addition', 'Subtraction', 'Multiplication', 'Division'];
  late AnimationController _controller;

  static const Map<String, List<bool>> _table = {
    // [closure, commutative, associative] per operation index
    'Addition': [true, true, true],
    'Subtraction': [true, false, false],
    'Multiplication': [true, true, true],
    'Division': [false, false, false],
  };

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 700));
    _controller.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _select(int i) {
    setState(() {
      _opIndex = i;
      _controller.forward(from: 0);
    });
  }

  @override
  Widget build(BuildContext context) {
    final op = _ops[_opIndex];
    final flags = _table[op]!;
    final labels = ['Closure', 'Commutative', 'Associative'];

    return SimFrame(
      title: 'Properties of Rational Numbers',
      icon: Icons.rule,
      accent: Colors.indigo.shade600,
      description: 'Pick an operation and watch which properties hold for rational numbers reveal themselves.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 8,
            children: _ops.asMap().entries.map((e) {
              final isSelected = e.key == _opIndex;
              return ChoiceChip(
                label: Text(e.value, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: Colors.indigo.shade600,
                backgroundColor: Colors.indigo.shade50,
                onSelected: (_) => _select(e.key),
              );
            }).toList(),
          ),
          const SizedBox(height: 14),
          AnimatedBuilder(
            animation: _controller,
            builder: (context, _) {
              return Column(
                children: List.generate(3, (i) {
                  final start = i * 0.2;
                  final end = start + 0.5;
                  final localT = ((_controller.value - start) / (end - start)).clamp(0.0, 1.0);
                  final eased = Curves.easeOutBack.transform(localT);
                  return Opacity(
                    opacity: eased.clamp(0.0, 1.0),
                    child: Transform.translate(
                      offset: Offset((1 - eased.clamp(0.0, 1.0)) * 30, 0),
                      child: _propertyRow(labels[i], flags[i]),
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

  Widget _propertyRow(String label, bool holds) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 6),
      child: Row(
        children: [
          Icon(holds ? Icons.check_circle : Icons.cancel, color: holds ? Colors.green : Colors.red, size: 22),
          const SizedBox(width: 10),
          Text(label, style: TextStyle(fontSize: 14)),
          const Spacer(),
          Text(holds ? 'Holds' : 'Does not hold', style: TextStyle(color: holds ? Colors.green.shade700 : Colors.red.shade700, fontWeight: FontWeight.w600, fontSize: 12)),
        ],
      ),
    );
  }
}
