import 'package:flutter/material.dart';

import '../models/index_number_model.dart';

/// Renders the commodity price (and optional quantity) table, matching
/// how GSEB/CBSE Index Numbers problems present the data.
class CommodityTableWidget extends StatelessWidget {
  final List<CommodityPrice> commodities;
  final bool includeQuantities;

  const CommodityTableWidget({super.key, required this.commodities, required this.includeQuantities});

  @override
  Widget build(BuildContext context) {
    return Table(
      border: TableBorder.all(color: Colors.grey.shade300),
      children: [
        TableRow(children: [
          _headerCell('Commodity'),
          _headerCell('P0 (Base)'),
          _headerCell('P1 (Current)'),
          if (includeQuantities) _headerCell('Q0 (Base)'),
          if (includeQuantities) _headerCell('Q1 (Current)'),
        ]),
        for (final c in commodities)
          TableRow(children: [
            _cell(c.name),
            _cell(_fmt(c.basePrice)),
            _cell(_fmt(c.currentPrice)),
            if (includeQuantities) _cell(_fmt(c.baseQuantity)),
            if (includeQuantities) _cell(_fmt(c.currentQuantity)),
          ]),
      ],
    );
  }

  Widget _headerCell(String text) =>
      Padding(padding: const EdgeInsets.all(6), child: Text(text, style: TextStyle(fontWeight: FontWeight.bold)));

  Widget _cell(String text) => Padding(padding: const EdgeInsets.all(6), child: Text(text));

  String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2);
  }
}
