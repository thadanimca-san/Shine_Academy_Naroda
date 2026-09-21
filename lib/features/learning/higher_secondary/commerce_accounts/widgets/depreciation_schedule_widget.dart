import 'package:flutter/material.dart';

import '../models/depreciation_model.dart';
import '../models/medium_model.dart';
import '../services/localization_service.dart';

class DepreciationScheduleWidget extends StatelessWidget {
  final DepreciationSchedule schedule;
  final Medium medium;

  const DepreciationScheduleWidget({super.key, required this.schedule, this.medium = Medium.english});

  @override
  Widget build(BuildContext context) {
    final methodLabel = LocalizationService.t(
        schedule.method == DepreciationMethod.straightLine ? 'Straight Line Method (SLM)' : 'Written Down Value Method (WDV)',
        medium);
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 6),
      child: Padding(
        padding: const EdgeInsets.all(10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('${schedule.assetName} — $methodLabel @ ${schedule.ratePercent}%',
                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15)),
            const Divider(),
            Table(
              columnWidths: const {0: FlexColumnWidth(1), 1: FlexColumnWidth(2), 2: FlexColumnWidth(2), 3: FlexColumnWidth(2)},
              children: [
                TableRow(children: [
                  Padding(padding: const EdgeInsets.all(4), child: Text(LocalizationService.t('Year', medium), style: TextStyle(fontWeight: FontWeight.bold))),
                  Padding(padding: const EdgeInsets.all(4), child: Text(LocalizationService.t('Opening', medium), style: TextStyle(fontWeight: FontWeight.bold))),
                  Padding(padding: const EdgeInsets.all(4), child: Text(LocalizationService.t('Depreciation', medium), style: TextStyle(fontWeight: FontWeight.bold))),
                  Padding(padding: const EdgeInsets.all(4), child: Text(LocalizationService.t('Closing', medium), style: TextStyle(fontWeight: FontWeight.bold))),
                ]),
                for (final row in schedule.rows)
                  TableRow(children: [
                    Padding(padding: const EdgeInsets.all(4), child: Text('${row.year}')),
                    Padding(padding: const EdgeInsets.all(4), child: Text(_fmt(row.openingBalance))),
                    Padding(padding: const EdgeInsets.all(4), child: Text(_fmt(row.depreciationAmount))),
                    Padding(padding: const EdgeInsets.all(4), child: Text(_fmt(row.closingBalance))),
                  ]),
              ],
            ),
          ],
        ),
      ),
    );
  }

  String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return '₹${isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2)}';
  }
}
