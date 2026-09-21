import 'package:flutter/material.dart';

import '../models/cash_book_model.dart';
import '../models/medium_model.dart';
import '../services/cash_book_solver.dart';
import '../services/localization_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Renders a Double Column Cash Book as the classic two-sided
/// Receipts | Payments table with Cash, Bank and Discount columns.
class CashBookTableWidget extends StatelessWidget {
  final List<CashBookTransaction> transactions;
  final double openingCash;
  final double openingBank;
  final Medium medium;

  const CashBookTableWidget({
    super.key,
    required this.transactions,
    required this.openingCash,
    required this.openingBank,
    this.medium = Medium.english,
  });

  @override
  Widget build(BuildContext context) {
    final totals = CashBookSolver.solve(transactions, openingCash: openingCash, openingBank: openingBank);
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 6),
      child: Padding(
        padding: const EdgeInsets.all(10),
        child: SingleChildScrollView(
          scrollDirection: Axis.horizontal,
          child: DataTable(
            columnSpacing: 16,
            columns: [
              DataColumn(label: Text(LocalizationService.t('Receipts', medium))),
              DataColumn(label: Text(LocalizationService.t('Disc.', medium))),
              DataColumn(label: Text(LocalizationService.t('Cash', medium))),
              DataColumn(label: Text(LocalizationService.t('Bank', medium))),
              DataColumn(label: Text(LocalizationService.t('Payments', medium))),
              DataColumn(label: Text(LocalizationService.t('Disc.', medium))),
              DataColumn(label: Text(LocalizationService.t('Cash', medium))),
              DataColumn(label: Text(LocalizationService.t('Bank', medium))),
            ],
            rows: [
              DataRow(cells: [
                DataCell(Text(LocalizationService.t('To Balance b/d', medium))),
                DataCell(Text(TrilingualService.instance.getUIText(''))),
                DataCell(Text(_fmt(openingCash))),
                DataCell(Text(_fmt(openingBank))),
                DataCell(Text(TrilingualService.instance.getUIText(''))),
                DataCell(Text(TrilingualService.instance.getUIText(''))),
                DataCell(Text(TrilingualService.instance.getUIText(''))),
                DataCell(Text(TrilingualService.instance.getUIText(''))),
              ]),
              for (final tx in transactions) ..._rowsFor(tx),
              DataRow(cells: [
                DataCell(Text(TrilingualService.instance.getUIText(''))),
                DataCell(Text(_fmt(totals.totalDiscountAllowed), style: TextStyle(fontWeight: FontWeight.bold))),
                DataCell(Text(TrilingualService.instance.getUIText(''))),
                DataCell(Text(TrilingualService.instance.getUIText(''))),
                DataCell(Text(LocalizationService.t('By Balance c/d', medium))),
                DataCell(Text(_fmt(totals.totalDiscountReceived), style: TextStyle(fontWeight: FontWeight.bold))),
                DataCell(Text(_fmt(totals.closingCashBalance), style: TextStyle(fontWeight: FontWeight.bold))),
                DataCell(Text(_fmt(totals.closingBankBalance), style: TextStyle(fontWeight: FontWeight.bold))),
              ]),
            ],
          ),
        ),
      ),
    );
  }

  List<DataRow> _rowsFor(CashBookTransaction tx) {
    final rows = <DataRow>[];
    if (tx.receiptRow != null) {
      final r = tx.receiptRow!;
      rows.add(DataRow(cells: [
        DataCell(Text('To ${LocalizationService.translatePhrase(r.particulars, medium)}')),
        DataCell(Text(r.discountAmount != null ? _fmt(r.discountAmount!) : '')),
        DataCell(Text(r.cashAmount != null ? _fmt(r.cashAmount!) : '')),
        DataCell(Text(r.bankAmount != null ? _fmt(r.bankAmount!) : '')),
        DataCell(Text(TrilingualService.instance.getUIText(''))),
        DataCell(Text(TrilingualService.instance.getUIText(''))),
        DataCell(Text(TrilingualService.instance.getUIText(''))),
        DataCell(Text(TrilingualService.instance.getUIText(''))),
      ]));
    }
    if (tx.paymentRow != null) {
      final p = tx.paymentRow!;
      rows.add(DataRow(cells: [
        DataCell(Text(TrilingualService.instance.getUIText(''))),
        DataCell(Text(TrilingualService.instance.getUIText(''))),
        DataCell(Text(TrilingualService.instance.getUIText(''))),
        DataCell(Text(TrilingualService.instance.getUIText(''))),
        DataCell(Text('By ${LocalizationService.translatePhrase(p.particulars, medium)}')),
        DataCell(Text(p.discountAmount != null ? _fmt(p.discountAmount!) : '')),
        DataCell(Text(p.cashAmount != null ? _fmt(p.cashAmount!) : '')),
        DataCell(Text(p.bankAmount != null ? _fmt(p.bankAmount!) : '')),
      ]));
    }
    return rows;
  }

  String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2);
  }
}
