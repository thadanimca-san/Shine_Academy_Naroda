import 'package:flutter/material.dart';

import '../models/correlation_model.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Renders a list of (X, Y) paired observations as a two-column table,
/// matching how GSEB/CBSE correlation problems present the data.
class XyPairsWidget extends StatelessWidget {
  final List<XYPair> pairs;

  const XyPairsWidget({super.key, required this.pairs});

  @override
  Widget build(BuildContext context) {
    return Table(
      border: TableBorder.all(color: Colors.grey.shade300),
      columnWidths: const {0: FlexColumnWidth(1), 1: FlexColumnWidth(1)},
      children: [
        TableRow(children: [
          Padding(padding: EdgeInsets.all(6), child: Text(TrilingualService.instance.getUIText('X'), style: TextStyle(fontWeight: FontWeight.bold))),
          Padding(padding: EdgeInsets.all(6), child: Text(TrilingualService.instance.getUIText('Y'), style: TextStyle(fontWeight: FontWeight.bold))),
        ]),
        for (final p in pairs)
          TableRow(children: [
            Padding(padding: const EdgeInsets.all(6), child: Text(_fmt(p.x))),
            Padding(padding: const EdgeInsets.all(6), child: Text(_fmt(p.y))),
          ]),
      ],
    );
  }

  String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2);
  }
}
