import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/depreciation_model.dart';
import 'package:commerce_accounts_11to12/services/depreciation_solver.dart';

void main() {
  group('DepreciationSolver', () {
    test('SLM charges the same depreciation amount every year', () {
      final schedule = DepreciationSolver.computeSchedule(
        assetName: 'Machinery',
        method: DepreciationMethod.straightLine,
        originalCost: 100000,
        ratePercent: 10,
        years: 4,
      );
      for (final row in schedule.rows) {
        expect(row.depreciationAmount, closeTo(10000, 0.01));
      }
      expect(schedule.finalBookValue, closeTo(60000, 0.01));
    });

    test('WDV charges depreciation on the reducing balance each year', () {
      final schedule = DepreciationSolver.computeSchedule(
        assetName: 'Furniture',
        method: DepreciationMethod.writtenDownValue,
        originalCost: 100000,
        ratePercent: 10,
        years: 3,
      );
      expect(schedule.rows[0].depreciationAmount, closeTo(10000, 0.01)); // 10% of 100000
      expect(schedule.rows[1].depreciationAmount, closeTo(9000, 0.01)); // 10% of 90000
      expect(schedule.rows[2].depreciationAmount, closeTo(8100, 0.01)); // 10% of 81000
    });

    test('closing balance of one year is the opening balance of the next', () {
      final schedule = DepreciationSolver.computeSchedule(
        assetName: 'Vehicle',
        method: DepreciationMethod.writtenDownValue,
        originalCost: 200000,
        ratePercent: 15,
        years: 5,
      );
      for (var i = 1; i < schedule.rows.length; i++) {
        expect(schedule.rows[i].openingBalance, closeTo(schedule.rows[i - 1].closingBalance, 0.01));
      }
    });

    test('book value never goes negative or exceeds original cost', () {
      final schedule = DepreciationSolver.computeSchedule(
        assetName: 'Plant',
        method: DepreciationMethod.straightLine,
        originalCost: 80000,
        ratePercent: 20,
        years: 5,
      );
      for (final row in schedule.rows) {
        expect(row.closingBalance, lessThanOrEqualTo(schedule.originalCost));
      }
    });
  });
}
