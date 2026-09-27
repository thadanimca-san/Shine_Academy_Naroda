import '../models/medium_model.dart';

/// Central Gujarati translation dictionary for the app's fixed UI/domain
/// vocabulary (account names, statement labels, common phrases used in
/// solver reasoning). English remains the single internal source of
/// truth everywhere (generators and solvers always produce English) —
/// this service only translates at render time, via [t]. This keeps the
/// solver/generator logic simple and testable while still giving
/// Gujarati-medium students a fully translated experience.
///
/// Extending Gujarati support to a new topic means adding that topic's
/// vocabulary to [_dictionary] — the lookup and fallback behaviour never
/// needs to change.
class LocalizationService {
  LocalizationService._();

  /// Translates [english] to Gujarati if [medium] is Gujarati and a
  /// translation exists; otherwise returns [english] unchanged. Falling
  /// back to English for anything untranslated means partial topic
  /// coverage never breaks or blanks out the UI — it just shows English
  /// for the parts not yet translated.
  static String t(String english, Medium medium) {
    if (medium == Medium.english) return english;
    return _dictionary[english] ?? english;
  }

  /// Translates a full sentence/phrase by replacing every known English
  /// term found inside it with its Gujarati equivalent, for strings that
  /// are built dynamically (e.g. solver reasoning with interpolated
  /// numbers) rather than being one fixed phrase from [_dictionary].
  static String translatePhrase(String english, Medium medium) {
    if (medium == Medium.english) return english;
    var result = english;
    for (final entry in _sortedDictionaryEntries) {
      result = result.replaceAll(entry.key, entry.value);
    }
    return result;
  }

  static List<MapEntry<String, String>> get _sortedDictionaryEntries {
    // Longer keys first, so "Trial Balance" is replaced before "Balance"
    // would otherwise be able to partially match inside it.
    final entries = _dictionary.entries.toList()
      ..sort((a, b) => b.key.length.compareTo(a.key.length));
    return entries;
  }

  static const Map<String, String> _dictionary = {
    // --- Account names ---
    'Cash': 'રોકડ',
    'Bank': 'બેંક',
    'Furniture': 'ફર્નિચર',
    'Machinery': 'મશીનરી',
    'Building': 'મકાન',
    'Purchases': 'ખરીદી',
    'Sales': 'વેચાણ',
    'Purchases Return': 'ખરીદ પરત',
    'Sales Return': 'વેચાણ પરત',
    'Capital': 'મૂડી',
    'Drawings': 'ઉપાડ',
    'Rent': 'ભાડું',
    'Salary': 'પગાર',
    'Commission Received': 'મળેલ કમિશન',
    'Commission Paid': 'ચૂકવેલ કમિશન',
    'Interest Received': 'મળેલ વ્યાજ',
    'Interest Paid': 'ચૂકવેલ વ્યાજ',
    'Discount Allowed': 'આપેલ વટાવ',
    'Discount Received': 'મળેલ વટાવ',
    'Bad Debts': 'ડૂબત દેવું',
    'Stationery': 'સ્ટેશનરી',
    'Carriage Inwards': 'આવક ભાડું',
    'Carriage Outwards': 'જાવક ભાડું',
    'Bank Loan': 'બેંક લોન',

    // --- Account category labels ---
    'Asset': 'મિલકત',
    'Liability': 'દેવું',
    'Income/Revenue': 'આવક',
    'Expense': 'ખર્ચ',

    // --- Golden rules (traditional classification) ---
    'Personal': 'વ્યક્તિગત',
    'Real': 'વાસ્તવિક',
    'Nominal': 'નામાકીય',
    'Golden Rule': 'સુવર્ણ નિયમ',
    'Debit the receiver, Credit the giver': 'લેનારને ઉધાર કરો, આપનારને જમા કરો',
    'Debit what comes in, Credit what goes out': 'આવે તે ઉધાર કરો, જાય તે જમા કરો',
    'Debit all expenses and losses, Credit all incomes and gains': 'બધા ખર્ચ અને નુકસાન ઉધાર કરો, બધી આવક અને નફો જમા કરો',

    // --- Common transaction phrases ---
    'Started business with cash': 'રોકડથી ધંધો શરૂ કર્યો',
    'Purchased goods for cash': 'રોકડેથી માલ ખરીદ્યો',
    'Sold goods for cash': 'રોકડેથી માલ વેચ્યો',
    'Paid rent': 'ભાડું ચૂકવ્યું',
    'Paid salary': 'પગાર ચૂકવ્યો',
    'Received commission': 'કમિશન મળ્યું',
    'Purchased furniture for cash': 'રોકડેથી ફર્નિચર ખરીદ્યું',
    'Withdrew cash for personal use': 'અંગત ઉપયોગ માટે રોકડ ઉપાડી',
    'on credit': 'ઉધાર',
    'To': 'ને',

    // --- Statement/table headers ---
    'Journal': 'આમનોંધ',
    'Ledger': 'ખાતાવહી',
    'Trial Balance': 'મેળવણી પત્રક',
    'Debit': 'ઉધાર',
    'Credit': 'જમા',
    'Account': 'ખાતું',
    'Amount': 'રકમ',
    'Particulars': 'વિગત',
    'Total': 'કુલ',
    'Balance': 'બાકી',

    // --- Common UI ---
    'Check My Entry': 'મારી નોંધ તપાસો',
    'Check My Answers': 'મારા જવાબો તપાસો',
    'Show Solution': 'ઉકેલ બતાવો',
    'Hide Solution': 'ઉકેલ છુપાવો',
    'Show Full Solution': 'સંપૂર્ણ ઉકેલ બતાવો',
    'Hide Full Solution': 'સંપૂર્ણ ઉકેલ છુપાવો',
    'Show Explanation': 'સમજૂતી બતાવો',
    'Hide Explanation': 'સમજૂતી છુપાવો',
    'New Problem': 'નવો દાખલો',
    'Correct': 'સાચું',
    'Not quite': 'બરાબર નથી',
    'Check': 'તપાસો',

    // --- Cash Book ---
    'Cash Book': 'રોકડ ચોપડો',
    'Double Column Cash Book': 'બે સ્તંભ રોકડ ચોપડો',
    'Receipts': 'આવક',
    'Payments': 'ખર્ચ',
    'Disc.': 'વટાવ',
    'Opening Cash Balance': 'શરૂઆતની રોકડ બાકી',
    'Opening Bank Balance': 'શરૂઆતની બેંક બાકી',
    'Prepare a Double Column Cash Book from the following transactions':
        'નીચેના વ્યવહારો પરથી બે સ્તંભ રોકડ ચોપડો તૈયાર કરો',
    'To Balance b/d': 'બાકી લાવ્યા',
    'By Balance c/d': 'બાકી લઈ ગયા',

    // --- Depreciation ---
    'Depreciation': 'ઘસારો',
    'Straight Line Method (SLM)': 'સીધી રેખા પદ્ધતિ (SLM)',
    'Written Down Value Method (WDV)': 'લખેલ ઘટતી કિંમત પદ્ધતિ (WDV)',
    'Year': 'વર્ષ',
    'Opening': 'શરૂઆતની બાકી',
    'Closing': 'અંતિમ બાકી',
    'A': 'એક',
    'was purchased for': 'ની કિંમતે ખરીદવામાં આવ્યું',
    'Calculate depreciation for': 'ઘસારો ગણો',
    'years under the': 'વર્ષ માટે, પદ્ધતિ',

    // --- Rectification ---
    'Rectification of Errors': 'ભૂલ સુધારણા',
    'Pass rectifying journal entries for the following errors': 'નીચેની ભૂલો માટે સુધારાની આમનોંધ પાસ કરો',
    'One-Sided Error': 'એકતરફી ભૂલ',
    'Two-Sided Error': 'બંનેતરફી ભૂલ',
    'One-sided error — routed through Suspense A/c.': 'એકતરફી ભૂલ — સંદેહ ખાતા મારફતે સુધારેલ.',
    'Two-sided error — entry balances directly, no Suspense A/c needed.':
        'બંનેતરફી ભૂલ — નોંધ સીધી સરભર થાય છે, સંદેહ ખાતાની જરૂર નથી.',
    'This error affects only one side of the trial balance, so the difference is routed through Suspense A/c.':
        'આ ભૂલ મેળવણી પત્રકની ફક્ત એક બાજુને અસર કરે છે, તેથી તફાવત સંદેહ ખાતા મારફતે સુધારવામાં આવે છે.',
    'This error affects both sides equally, so the rectifying entry balances directly without Suspense A/c.':
        'આ ભૂલ બંને બાજુને સરખી અસર કરે છે, તેથી સુધારાની નોંધ સંદેહ ખાતા વગર સીધી સરભર થાય છે.',

    // --- BRS ---
    'Bank Reconciliation Statement': 'બેંક મેળવણી પત્રક',
    'Balance as per Cash Book': 'રોકડ ચોપડા મુજબ બાકી',
    'Balance as per Pass Book': 'પાસબુક મુજબ બાકી',
    'Add': 'ઉમેરો',
    'Less': 'બાદ',
    'The following differences were found. Prepare a Bank Reconciliation Statement and find the Balance as per Pass Book:':
        'નીચેના તફાવતો મળી આવ્યા. બેંક મેળવણી પત્રક તૈયાર કરો અને પાસબુક મુજબ બાકી શોધો:',
    'From the following particulars, prepare a Bank Reconciliation Statement and find the':
        'નીચેની વિગતો પરથી બેંક મેળવણી પત્રક તૈયાર કરો અને શોધો',

    // --- Final Accounts ---
    'Final Accounts': 'અંતિમ ખાતાં',
    'Trading Account': 'વેપાર ખાતું',
    'Profit & Loss Account': 'નફા-નુકસાન ખાતું',
    'Balance Sheet': 'પાકું સરવૈયું',
    'Opening Stock': 'શરૂઆતનો સ્ટોક',
    'Closing Stock': 'અંતિમ સ્ટોક',
    'Wages': 'મજૂરી',
    'Gross Profit': 'ઢોબો નફો',
    'Gross Loss': 'ઢોબી ખોટ',
    'Net Profit': 'ચોખ્ખો નફો',
    'Net Loss': 'ચોખ્ખી ખોટ',
    'Debtors': 'દેવાદારો',
    'Creditors': 'લેણદારો',
    'Adjustments': 'ગોઠવણો',
    'Liabilities': 'દેવાં',
    'Assets': 'મિલકતો',
    'Gross Profit c/d': 'ઢોબો નફો લઈ ગયા',
    'Gross Loss c/d': 'ઢોબી ખોટ લઈ ગયા',
    'Net Profit (to Capital)': 'ચોખ્ખો નફો (મૂડીમાં)',
    'Net Loss (to Capital)': 'ચોખ્ખી ખોટ (મૂડીમાંથી)',
    'Balance Sheet tallies': 'પાકું સરવૈયું મળે છે',
    'Balance Sheet does NOT tally': 'પાકું સરવૈયું મળતું નથી',
    'From the following Trial Balance and adjustments, prepare the Trading Account, Profit & Loss Account, and Balance Sheet':
        'નીચેના મેળવણી પત્રક અને ગોઠવણો પરથી વેપાર ખાતું, નફા-નુકસાન ખાતું અને પાકું સરવૈયું તૈયાર કરો',
    'From the following Trial Balance and adjustments, prepare the Trading Account, '
            'Profit & Loss Account, and Balance Sheet:':
        'નીચેના મેળવણી પત્રક અને ગોઠવણો પરથી વેપાર ખાતું, નફા-નુકસાન ખાતું અને પાકું સરવૈયું તૈયાર કરો:',

    // --- Partnership ---
    'Partnership Accounts': 'ભાગીદારી ખાતાં',
    'Admission': 'સ્વીકૃતિ',
    'Retirement': 'નિવૃત્તિ',
    'Death': 'મરણ',
    'Dissolution': 'વિસર્જન',
    'Goodwill': 'પ્રતિષ્ઠા',
    'Capital Account': 'મૂડી ખાતું',
    'New Profit Sharing Ratio': 'નવો નફા વહેંચણી ગુણોત્તર',
    'Sacrificing Ratio': 'ત્યાગ ગુણોત્તર',
    'Gaining Ratio': 'લાભ ગુણોત્તર',
    'Realisation Account': 'વસૂલાત ખાતું',
    "Partners' Capital Accounts": 'ભાગીદારોના મૂડી ખાતાં',
    'Balance b/d': 'બાકી લાવ્યા',
    'Goodwill Dr': 'પ્રતિષ્ઠા ઉધાર',
    'Goodwill Cr': 'પ્રતિષ્ઠા જમા',
    'Profit transferred to Capital A/cs': 'નફો મૂડી ખાતાંમાં ટ્રાન્સફર',
    'Loss transferred to Capital A/cs': 'ખોટ મૂડી ખાતાંમાંથી ટ્રાન્સફર',
    'Prepare the Realisation Account and show the final settlement with partners.':
        'વસૂલાત ખાતું તૈયાર કરો અને ભાગીદારો સાથે અંતિમ પતાવટ બતાવો.',

    // --- Company Accounts / Share Issue ---
    'Issue of Shares': 'શેરોનું વેચાણ',
    'Share Capital': 'શેર મૂડી',
    'Application': 'અરજી',
    'Allotment': 'ફાળવણી',
    'First Call': 'પ્રથમ હપ્તો',
    'Final Call': 'અંતિમ હપ્તો',
    'Forfeiture': 'જપ્તી',
    'Reissue': 'પુનઃવેચાણ',
    'Total Capital Raised': 'કુલ એકત્રિત મૂડી',
    'Securities Premium': 'સિક્યોરિટીઝ પ્રીમિયમ',
    'Capital Reserve (from reissue)': 'મૂડી અનામત (પુનઃવેચાણમાંથી)',

    // --- Cash Flow ---
    'Cash Flow Statement': 'રોકડ પ્રવાહ પત્રક',
    'Operating Activities': 'સંચાલન પ્રવૃત્તિઓ',
    'Investing Activities': 'રોકાણ પ્રવૃત્તિઓ',
    'Financing Activities': 'ધિરાણ પ્રવૃત્તિઓ',
    'Net Increase in Cash': 'રોકડમાં ચોખ્ખો વધારો',
    'Closing Cash and Bank Balance': 'અંતિમ રોકડ અને બેંક બાકી',
    'Opening Cash and Bank Balance': 'શરૂઆતની રોકડ અને બેંક બાકી',
    'Net Profit before Tax': 'કરવેરા પહેલાનો ચોખ્ખો નફો',
    'Depreciation for the year': 'વર્ષનો ઘસારો',
    'Machinery Purchased': 'ખરીદેલ મશીનરી',
    'Machinery Sold': 'વેચેલ મશીનરી',
    'Loan Raised': 'લીધેલ લોન',
    'Loan Repaid': 'ચૂકવેલ લોન',
    'Shares Issued for Cash': 'રોકડ સામે વેચેલ શેર',
    'A. Cash Flow from Operating Activities': 'અ. સંચાલન પ્રવૃત્તિઓમાંથી રોકડ પ્રવાહ',
    'B. Cash Flow from Investing Activities': 'બ. રોકાણ પ્રવૃત્તિઓમાંથી રોકડ પ્રવાહ',
    'C. Cash Flow from Financing Activities': 'ક. ધિરાણ પ્રવૃત્તિઓમાંથી રોકડ પ્રવાહ',
    'Net Increase/Decrease in Cash (A+B+C)': 'રોકડમાં ચોખ્ખો વધારો/ઘટાડો (અ+બ+ક)',
    'Add: Opening Cash and Bank Balance': 'ઉમેરો: શરૂઆતની રોકડ અને બેંક બાકી',
    'From the following information, prepare a Cash Flow Statement (Indirect Method) for the year:':
        'નીચેની માહિતી પરથી વર્ષ માટે રોકડ પ્રવાહ પત્રક (પરોક્ષ પદ્ધતિ) તૈયાર કરો:',

    // --- Mock Test ---
    'Mock Test': 'નમૂના કસોટી',
    'Submit Test': 'કસોટી સુપરત કરો',
    'Time Remaining': 'બાકી સમય',
  };
}
