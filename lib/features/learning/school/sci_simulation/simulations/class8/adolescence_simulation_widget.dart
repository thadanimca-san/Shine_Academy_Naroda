import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _Gland {
  final String name;
  final String hormone;
  final String function;
  final Color color;
  final Alignment position;

  const _Gland(this.name, this.hormone, this.function, this.color, this.position);
}

/// A tap-to-explore endocrine gland map on a simplified body outline:
/// each gland shows the hormone it releases and what that hormone does.
class AdolescenceSimulationWidget extends StatefulWidget {
  const AdolescenceSimulationWidget({super.key});

  @override
  State<AdolescenceSimulationWidget> createState() => _AdolescenceSimulationWidgetState();
}

class _AdolescenceSimulationWidgetState extends State<AdolescenceSimulationWidget> {
  static const _glands = [
    _Gland('Pituitary Gland', 'Growth hormone & others', 'The "master gland" — controls the release of hormones from most other endocrine glands.', Color(0xFF7E57C2), Alignment(0, -0.75)),
    _Gland('Thyroid Gland', 'Thyroxine', 'Regulates the body\'s metabolic rate; needs iodine to function properly.', Color(0xFF42A5F5), Alignment(0, -0.4)),
    _Gland('Adrenal Gland', 'Adrenaline', 'Prepares the body to deal with emergencies ("fight or flight").', Color(0xFFEF5350), Alignment(-0.2, 0.05)),
    _Gland('Pancreas', 'Insulin', 'Regulates blood sugar levels in the body.', Color(0xFF66BB6A), Alignment(0.2, 0.1)),
    _Gland('Testes (male)', 'Testosterone', 'Brings about male secondary sexual characteristics like facial hair and a deeper voice.', Color(0xFF26A69A), Alignment(-0.15, 0.7)),
    _Gland('Ovaries (female)', 'Estrogen', 'Brings about female secondary sexual characteristics and regulates the menstrual cycle.', Color(0xFFEC407A), Alignment(0.15, 0.7)),
  ];

  _Gland _selected = _glands[0];

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Endocrine Glands & Hormones',
      icon: Icons.emoji_people,
      accent: Colors.deepPurple.shade400,
      description: 'Tap a gland on the body outline to see the hormone it releases during puberty.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          AspectRatio(
            aspectRatio: 1.3,
            child: Container(
              decoration: BoxDecoration(color: Colors.deepPurple.shade50, borderRadius: BorderRadius.circular(12)),
              child: Stack(
                alignment: Alignment.center,
                children: [
                  Icon(Icons.accessibility_new, size: 160, color: Colors.deepPurple.shade100),
                  ..._glands.map((g) {
                    final isSelected = _selected.name == g.name;
                    return Align(
                      alignment: g.position,
                      child: GestureDetector(
                        onTap: () => setState(() => _selected = g),
                        child: Container(
                          width: 26,
                          height: 26,
                          decoration: BoxDecoration(
                            color: g.color,
                            shape: BoxShape.circle,
                            border: Border.all(color: isSelected ? Colors.black87 : Colors.white, width: isSelected ? 2.5 : 1.5),
                            boxShadow: [BoxShadow(color: Theme.of(context).colorScheme.onSurface.withOpacity(0.26), blurRadius: 3)],
                          ),
                        ),
                      ),
                    );
                  }),
                ],
              ),
            ),
          ),
          const SizedBox(height: 12),
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: _glands.map((g) {
              final isSelected = _selected.name == g.name;
              return ActionChip(
                label: Text(g.name, style: TextStyle(fontSize: 11.5, color: isSelected ? Colors.white : Colors.black87)),
                backgroundColor: isSelected ? g.color : g.color.withValues(alpha: 0.2),
                onPressed: () => setState(() => _selected = g),
              );
            }).toList(),
          ),
          const SizedBox(height: 12),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.grey.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade200)),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(_selected.name, style: TextStyle(fontWeight: FontWeight.bold, color: _selected.color, fontSize: 14)),
                const SizedBox(height: 2),
                Text('Releases: ${_selected.hormone}', style: TextStyle(fontSize: 12.5, fontStyle: FontStyle.italic)),
                const SizedBox(height: 6),
                Text(_selected.function, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
