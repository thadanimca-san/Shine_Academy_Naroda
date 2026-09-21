import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// A Punnett-square generator for a monohybrid cross: pick each parent's
/// genotype for a trait (e.g. Tall T / short t) and see the offspring
/// genotype and phenotype ratio predicted by Mendel's laws.
class HeredityEvolutionSimulationWidget extends StatefulWidget {
  const HeredityEvolutionSimulationWidget({super.key});

  @override
  State<HeredityEvolutionSimulationWidget> createState() => _HeredityEvolutionSimulationWidgetState();
}

class _HeredityEvolutionSimulationWidgetState extends State<HeredityEvolutionSimulationWidget> {
  // true = Tt (heterozygous), false = TT (pure dominant), 'tt' handled via two bools per parent allele
  String _parent1 = 'Tt';
  String _parent2 = 'Tt';

  static const _genotypeOptions = ['TT', 'Tt', 'tt'];

  List<String> _alleles(String genotype) => genotype.split('');

  @override
  Widget build(BuildContext context) {
    final p1 = _alleles(_parent1);
    final p2 = _alleles(_parent2);
    final offspring = <String>[];
    for (final a in p1) {
      for (final b in p2) {
        final pair = [a, b]..sort((x, y) => x == 'T' ? -1 : 1);
        offspring.add(pair.join());
      }
    }
    final tallCount = offspring.where((o) => o.contains('T')).length;
    final shortCount = offspring.length - tallCount;

    return SimFrame(
      title: "Mendel's Monohybrid Cross",
      icon: Icons.grain,
      accent: Colors.green.shade700,
      description: 'Pick each parent\'s genotype for plant height (T = tall, dominant; t = short, recessive) and see the offspring ratio.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Expanded(
                child: DropdownButtonFormField<String>(
                  initialValue: _parent1,
                  decoration: const InputDecoration(labelText: 'Parent 1', isDense: true, border: OutlineInputBorder()),
                  items: _genotypeOptions.map((g) => DropdownMenuItem(value: g, child: Text(g))).toList(),
                  onChanged: (val) => setState(() => _parent1 = val!),
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: DropdownButtonFormField<String>(
                  initialValue: _parent2,
                  decoration: const InputDecoration(labelText: 'Parent 2', isDense: true, border: OutlineInputBorder()),
                  items: _genotypeOptions.map((g) => DropdownMenuItem(value: g, child: Text(g))).toList(),
                  onChanged: (val) => setState(() => _parent2 = val!),
                ),
              ),
            ],
          ),
          const SizedBox(height: 14),
          Table(
            border: TableBorder.all(color: Colors.grey.shade300),
            children: [
              TableRow(children: [
                _cell('', header: true),
                ...p2.map((b) => _cell(b, header: true)),
              ]),
              for (final a in p1)
                TableRow(children: [
                  _cell(a, header: true),
                  ...p2.map((b) {
                    final pair = [a, b]..sort((x, y) => x == 'T' ? -1 : 1);
                    return _cell(pair.join());
                  }),
                ]),
            ],
          ),
          const SizedBox(height: 14),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Tall (T_)', value: '$tallCount / ${offspring.length}', color: Colors.green),
            SimMetric(label: 'Short (tt)', value: '$shortCount / ${offspring.length}', color: Colors.brown),
          ]),
        ],
      ),
    );
  }

  Widget _cell(String text, {bool header = false}) {
    return Container(
      height: 40,
      alignment: Alignment.center,
      color: header ? Colors.green.shade50 : Colors.white,
      child: Text(text, style: TextStyle(fontWeight: header ? FontWeight.bold : FontWeight.normal, color: text.contains('T') ? Colors.green.shade800 : Colors.brown)),
    );
  }
}
