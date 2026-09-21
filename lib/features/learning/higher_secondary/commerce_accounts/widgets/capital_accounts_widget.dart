import 'package:flutter/material.dart';

import '../models/medium_model.dart';
import '../models/partnership_model.dart';
import '../services/localization_service.dart';

/// Renders partners' capital accounts as a columnar table — the format
/// GSEB/CBSE Class 12 expects for Admission/Retirement/Death answers,
/// with one column per partner and rows for each adjustment.
class CapitalAccountsWidget extends StatelessWidget {
  final List<CapitalAccountRow> rows;
  final Medium medium;

  const CapitalAccountsWidget({super.key, required this.rows, this.medium = Medium.english});

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 6),
      child: Padding(
        padding: const EdgeInsets.all(10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(LocalizationService.t("Partners' Capital Accounts", medium), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
            const Divider(),
            SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: DataTable(
                columns: [
                  DataColumn(label: Text(LocalizationService.t('Particulars', medium))),
                  DataColumn(label: Text(LocalizationService.t('Balance b/d', medium))),
                  DataColumn(label: Text(LocalizationService.t('Goodwill Dr', medium))),
                  DataColumn(label: Text(LocalizationService.t('Goodwill Cr', medium))),
                  DataColumn(label: Text(LocalizationService.t('Balance c/d', medium))),
                ],
                rows: [
                  for (final row in rows)
                    DataRow(cells: [
                      DataCell(Text(row.partnerName, style: TextStyle(fontWeight: FontWeight.bold))),
                      DataCell(Text(_fmt(row.openingBalance))),
                      DataCell(Text(row.goodwillDebit > 0 ? _fmt(row.goodwillDebit) : '-')),
                      DataCell(Text(row.goodwillCredit > 0 ? _fmt(row.goodwillCredit) : '-')),
                      DataCell(Text(_fmt(row.closingBalance), style: TextStyle(fontWeight: FontWeight.bold))),
                    ]),
                ],
              ),
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
