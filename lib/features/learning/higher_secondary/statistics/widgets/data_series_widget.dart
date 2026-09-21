import 'package:flutter/material.dart';

import '../models/data_series_model.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Renders a [DataSeries] in whichever shape it holds — a plain value
/// list, a value/frequency table, or a class-interval/frequency table —
/// matching how each is presented in GSEB/CBSE textbooks.
class DataSeriesWidget extends StatelessWidget {
  final DataSeries series;

  const DataSeriesWidget({super.key, required this.series});

  @override
  Widget build(BuildContext context) {
    return switch (series.type) {
      SeriesType.individual => _buildIndividual(),
      SeriesType.discrete => _buildDiscrete(),
      SeriesType.continuous => _buildContinuous(),
    };
  }

  Widget _buildIndividual() {
    return Wrap(
      spacing: 10,
      children: [for (final v in series.individualValues) Chip(label: Text(_fmt(v)))],
    );
  }

  Widget _buildDiscrete() {
    return Table(
      border: TableBorder.all(color: Colors.grey.shade300),
      columnWidths: const {0: FlexColumnWidth(1), 1: FlexColumnWidth(1)},
      children: [
        TableRow(children: [
          Padding(padding: EdgeInsets.all(6), child: Text(TrilingualService.instance.getUIText('Value (X)'), style: TextStyle(fontWeight: FontWeight.bold))),
          Padding(padding: EdgeInsets.all(6), child: Text(TrilingualService.instance.getUIText('Frequency (f)'), style: TextStyle(fontWeight: FontWeight.bold))),
        ]),
        for (final d in series.discreteValues)
          TableRow(children: [
            Padding(padding: const EdgeInsets.all(6), child: Text(_fmt(d.value))),
            Padding(padding: const EdgeInsets.all(6), child: Text('${d.frequency}')),
          ]),
      ],
    );
  }

  Widget _buildContinuous() {
    return Table(
      border: TableBorder.all(color: Colors.grey.shade300),
      columnWidths: const {0: FlexColumnWidth(2), 1: FlexColumnWidth(1)},
      children: [
        TableRow(children: [
          Padding(padding: EdgeInsets.all(6), child: Text(TrilingualService.instance.getUIText('Class Interval'), style: TextStyle(fontWeight: FontWeight.bold))),
          Padding(padding: EdgeInsets.all(6), child: Text(TrilingualService.instance.getUIText('Frequency (f)'), style: TextStyle(fontWeight: FontWeight.bold))),
        ]),
        for (final c in series.classIntervals)
          TableRow(children: [
            Padding(padding: const EdgeInsets.all(6), child: Text('${_fmt(c.lowerBound)} - ${_fmt(c.upperBound)}')),
            Padding(padding: const EdgeInsets.all(6), child: Text('${c.frequency}')),
          ]),
      ],
    );
  }

  String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2);
  }
}
