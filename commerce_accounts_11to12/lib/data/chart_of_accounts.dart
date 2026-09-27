import '../models/account_model.dart';

/// Shared pool of accounts used to generate journal problems. Kept as a
/// single source of truth so every generated transaction refers to a
/// consistent, syllabus-appropriate account name.
class ChartOfAccounts {
  ChartOfAccounts._();

  static const cash = Account(name: 'Cash', category: AccountCategory.asset);
  static const bank = Account(name: 'Bank', category: AccountCategory.asset);
  static const furniture = Account(name: 'Furniture', category: AccountCategory.asset);
  static const machinery = Account(name: 'Machinery', category: AccountCategory.asset);
  static const building = Account(name: 'Building', category: AccountCategory.asset);
  static const goods = Account(name: 'Purchases', category: AccountCategory.expense);
  static const sales = Account(name: 'Sales', category: AccountCategory.income);
  static const purchasesReturn =
      Account(name: 'Purchases Return', category: AccountCategory.income);
  static const salesReturn = Account(name: 'Sales Return', category: AccountCategory.expense);
  static const capital = Account(name: 'Capital', category: AccountCategory.capital, isPersonEntity: true);
  static const drawings = Account(name: 'Drawings', category: AccountCategory.capital, isPersonEntity: true);
  static const rentExpense = Account(name: 'Rent', category: AccountCategory.expense);
  static const salaryExpense = Account(name: 'Salary', category: AccountCategory.expense);
  static const commissionReceived =
      Account(name: 'Commission Received', category: AccountCategory.income);
  static const commissionPaid = Account(name: 'Commission Paid', category: AccountCategory.expense);
  static const interestReceived =
      Account(name: 'Interest Received', category: AccountCategory.income);
  static const interestPaid = Account(name: 'Interest Paid', category: AccountCategory.expense);
  static const discountAllowed =
      Account(name: 'Discount Allowed', category: AccountCategory.expense);
  static const discountReceived =
      Account(name: 'Discount Received', category: AccountCategory.income);
  static const badDebts = Account(name: 'Bad Debts', category: AccountCategory.expense);
  static const stationery = Account(name: 'Stationery', category: AccountCategory.expense);
  static const carriageInwards =
      Account(name: 'Carriage Inwards', category: AccountCategory.expense);
  static const carriageOutwards =
      Account(name: 'Carriage Outwards', category: AccountCategory.expense);
  static const loanFromBank = Account(name: 'Bank Loan', category: AccountCategory.liability);

  /// Named person accounts used for credit-transaction templates, e.g.
  /// "Sold goods to Ram" / "Purchased from Shyam". Category is fixed as
  /// asset (debtor) or liability (creditor) per-instance by the caller,
  /// since the same name can appear as either depending on transaction
  /// direction — see [debtor] and [creditor].
  static Account debtor(String personName) =>
      Account(name: personName, category: AccountCategory.asset, isPersonEntity: true);

  static Account creditor(String personName) =>
      Account(name: personName, category: AccountCategory.liability, isPersonEntity: true);

  static const personNames = ['Ram', 'Shyam', 'Mohan', 'Sohan', 'Priya', 'Ketan', 'Nisha', 'Amit'];

  static const assetPurchaseOptions = [furniture, machinery, building];

  static const expenseOptions = [
    rentExpense,
    salaryExpense,
    commissionPaid,
    stationery,
    carriageOutwards,
  ];

  static const incomeOptions = [commissionReceived, interestReceived];
}
