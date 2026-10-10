import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:translator/translator.dart';
import 'package:shine_academy_naroda/core/services/presentation_service.dart';
import 'learning_ui_strings.dart';

class TrilingualService extends ChangeNotifier {
  static final TrilingualService instance = TrilingualService._internal();
  TrilingualService._internal();

  late SharedPreferences _prefs;
  final GoogleTranslator _googleTranslator = GoogleTranslator();
  
  // The primary language the user selected during onboarding (en, hi, gu). 
  // Null if they haven't selected yet.
  String? _primaryLanguage;
  
  // The current active language shown on screen.
  // This defaults to primaryLanguage but can be temporarily changed via toggle.
  String _activeViewLanguage = 'en';

  bool _isInitialized = false;

  String? get primaryLanguage => _primaryLanguage;
  String get activeViewLanguage => _activeViewLanguage;
  bool get isInitialized => _isInitialized;

  Future<void> init() async {
    if (_isInitialized) return;
    _prefs = await SharedPreferences.getInstance();
    
    _primaryLanguage = _prefs.getString('primary_language');
    _activeViewLanguage = _primaryLanguage ?? 'en';
    
    _isInitialized = true;
    notifyListeners();
  }

  Future<void> setPrimaryLanguage(String langCode) async {
    _primaryLanguage = langCode;
    _activeViewLanguage = langCode;
    await _prefs.setString('primary_language', langCode);
    notifyListeners();
  }

  void setActiveViewLanguage(String langCode) {
    if (_activeViewLanguage != langCode) {
      _activeViewLanguage = langCode;
      notifyListeners();
    }
  }

  bool _hasPlaceholderList(dynamic list, String targetLang) {
    if (list is! List) return true;
    if (list.isEmpty) return true;
    final placeholder = '[${targetLang == 'hi' ? 'HINDI' : 'GUJARATI'}]';
    return list.any((item) => item.toString().contains(placeholder));
  }

  /// Translates blocks dynamically at runtime if the target language is not English
  /// and the translation is missing from the JSON payload.
  Future<void> preTranslateBlocks(List<dynamic> blocks, {bool isDictionary = false}) async {
    final targetLang = _activeViewLanguage;
    if (targetLang == 'en') return;
    
    final fields = isDictionary 
        ? ['word', 'meaning', 'example_sentence', 'etymology']
        : ['body', 'title', 'question', 'feedback_correct', 'term', 'definition', 'tip', 'guidance'];

    final listFields = ['examples', 'synonyms', 'antonyms', 'options'];

    for (var block in blocks) {
      if (block is! Map<String, dynamic>) continue;

      // Translate direct string fields
      for (var field in fields) {
        if (block.containsKey(field) && block[field] != null && block[field].toString().isNotEmpty) {
          final localizedKey = '${field}_$targetLang';
          if (!block.containsKey(localizedKey) || block[localizedKey].toString().contains('[${targetLang == 'hi' ? 'HINDI' : 'GUJARATI'}]')) {
            try {
              final translation = await _googleTranslator.translate(block[field].toString(), to: targetLang);
              block[localizedKey] = translation.text;
            } catch (e) {
              debugPrint('Translation error for $field: $e');
            }
          }
        }
      }

      // Translate array fields (e.g. options, synonyms)
      for (var listField in listFields) {
         if (block.containsKey(listField) && block[listField] is List) {
           final localizedKey = '${listField}_$targetLang';
           if (!block.containsKey(localizedKey) || _hasPlaceholderList(block[localizedKey], targetLang)) {
              List<String> translatedList = [];
              for (var item in block[listField]) {
                 try {
                   final translation = await _googleTranslator.translate(item.toString(), to: targetLang);
                   translatedList.add(translation.text);
                 } catch (e) {
                   translatedList.add(item.toString());
                 }
              }
              block[localizedKey] = translatedList;
           }
         }
      }
    }
  }

  /// Universal text getter for educational JSON blocks.
  /// Usage: TrilingualService.instance.getLocalizedText(content, 'body')
  String getLocalizedText(Map<String, dynamic> content, String baseKey) {
    final lang = _activeViewLanguage;
    
    // e.g. body_hi or body_gu
    final String localizedKey = '${baseKey}_$lang';
    
    if (lang != 'en' && content.containsKey(localizedKey) && content[localizedKey] != null && content[localizedKey].toString().isNotEmpty) {
      return content[localizedKey].toString();
    }
    
    // Fallback to English (the base key like 'body')
    if (content.containsKey(baseKey) && content[baseKey] != null && content[baseKey].toString().isNotEmpty) {
      return content[baseKey].toString();
    }
    
    if (content.containsKey('${baseKey}_en') && content['${baseKey}_en'] != null && content['${baseKey}_en'].toString().isNotEmpty) {
      return content['${baseKey}_en'].toString();
    }

    // Fallback: If 'body' requested but block uses 'content' (or vice versa)
    final altKey = baseKey == 'body' ? 'content' : (baseKey == 'content' ? 'body' : null);
    if (altKey != null) {
      final altLocalizedKey = '${altKey}_$lang';
      if (lang != 'en' && content.containsKey(altLocalizedKey) && content[altLocalizedKey] != null && content[altLocalizedKey].toString().isNotEmpty) {
        return content[altLocalizedKey].toString();
      }
      if (content.containsKey(altKey) && content[altKey] != null && content[altKey] is String && content[altKey].toString().isNotEmpty) {
        return content[altKey].toString();
      }
    }

    return ''; // Return empty instead of null for safer UI rendering
  }

  // --- UI LOCALIZATION ---
  static const Map<String, Map<String, String>> _uiTranslations = {
    'Home': {
      'en': 'Home',
      'hi': 'मुख्य पृष्ठ',
      'gu': 'મુખ્ય પૃષ્ઠ',
    },
    'Learning': {
      'en': 'Learning',
      'hi': 'सीखना',
      'gu': 'શીખવું',
    },
    'Assessment': {
      'en': 'Assessment',
      'hi': 'मूल्यांकन',
      'gu': 'મૂલ્યાંકન',
    },
    'Community': {
      'en': 'Community',
      'hi': 'समुदाय',
      'gu': 'સમુદાય',
    },
    'SECTION A (Objective Type)': {
      'en': 'SECTION A (Objective Type)',
      'hi': 'खंड अ (वस्तुनिष्ठ प्रकार)',
      'gu': 'વિભાગ A (હેતુલક્ષી પ્રકાર)',
    },
    'SECTION B (Descriptive Type)': {
      'en': 'SECTION B (Descriptive Type)',
      'hi': 'खंड ब (वर्णनात्मक प्रकार)',
      'gu': 'વિભાગ B (વર્ણનાત્મક પ્રકાર)',
    },
    'General Instructions:': {
      'en': 'General Instructions:',
      'hi': 'सामान्य निर्देश:',
      'gu': 'સામાન્ય સૂચનાઓ:',
    },
    '1. All questions are compulsory. There are no internal choices.': {
      'en': '1. All questions are compulsory. There are no internal choices.',
      'hi': '1. सभी प्रश्न अनिवार्य हैं। कोई आंतरिक विकल्प नहीं है।',
      'gu': '1. બધા પ્રશ્નો ફરજિયાત છે. કોઈ આંતરિક વિકલ્પો નથી.',
    },
    '2. The paper is divided into Section A (Objective) and Section B (Subjective).': {
      'en': '2. The paper is divided into Section A (Objective) and Section B (Subjective).',
      'hi': '2. प्रश्न पत्र खंड अ (वस्तुनिष्ठ) और खंड ब (विषयनिष्ठ) में विभाजित है।',
      'gu': '2. પ્રશ્નપત્ર વિભાગ A (હેતુલક્ષી) અને વિભાગ B (વર્ણનાત્મક) માં વહેંચાયેલું છે.',
    },
    '3. Figures to the right indicate marks allocated to the question.': {
      'en': '3. Figures to the right indicate marks allocated to the question.',
      'hi': '3. दाईं ओर दिए गए अंक प्रश्न के लिए निर्धारित अंक दर्शाते हैं।',
      'gu': '3. જમણી બાજુના આંકડા પ્રશ્ન માટે ફાળવેલા ગુણ દર્શાવે છે.',
    },
    '4. Write your answers neatly in the provided answer supplement.': {
      'en': '4. Write your answers neatly in the provided answer supplement.',
      'hi': '4. प्रदान की गई उत्तर पुस्तिका में अपने उत्तर स्पष्ट रूप से लिखें।',
      'gu': '4. આપેલી ઉત્તરવહીમાં તમારા જવાબો સ્પષ્ટ રીતે લખો.',
    },
    '(True / False)': {
      'en': '(True / False)',
      'hi': '(सही / गलत)',
      'gu': '(સાચું / ખોટું)',
    },
    'Core Concepts': {
      'en': 'Core Concepts',
      'hi': 'मूल अवधारणाएं (Core Concepts)',
      'gu': 'મૂળભૂત સંકલ્પનાઓ (Core Concepts)',
    },
    'TAKE CHAPTER QUIZ': {
      'en': 'TAKE CHAPTER QUIZ',
      'hi': 'अध्याय प्रश्नोत्तरी लें',
      'gu': 'પ્રકરણ પ્રશ્નોત્તરી લો',
    },
    'THINK ABOUT IT': {
      'en': 'THINK ABOUT IT',
      'hi': 'इसके बारे में सोचें',
      'gu': 'તેના વિશે વિચારો',
    },
    'Start': {
      'en': 'Start',
      'hi': 'शुरू करें',
      'gu': 'શરૂ કરો',
    },
    'Stop': {
      'en': 'Stop',
      'hi': 'रोकें',
      'gu': 'રોકો',
    },
    'Very Slow': {
      'en': 'Very Slow',
      'hi': 'बहुत धीमा',
      'gu': 'ખૂબ ધીમું',
    },
    'Slow': {
      'en': 'Slow',
      'hi': 'धीमा',
      'gu': 'ધીમું',
    },
    'Medium': {
      'en': 'Medium',
      'hi': 'मध्यम',
      'gu': 'મધ્યમ',
    },
    '1. Curriculum Setup': {
      'en': '1. Curriculum Setup',
      'hi': '1. पाठ्यक्रम सेटअप',
      'gu': '1. અભ્યાસક્રમ સેટઅપ',
    },
    '2. Select Chapters': {
      'en': '2. Select Chapters',
      'hi': '2. अध्याय चुनें',
      'gu': '2. પ્રકરણો પસંદ કરો',
    },
    'Advanced Paper Generator': {
      'en': 'Advanced Paper Generator',
      'hi': 'उन्नत पेपर जनरेटर',
      'gu': 'અદ્યતન પેપર જનરેટર',
    },
    'Select Board': {
      'en': 'Select Board',
      'hi': 'बोर्ड चुनें',
      'gu': 'બોર્ડ પસંદ કરો',
    },
    'Select Class': {
      'en': 'Select Class',
      'hi': 'कक्षा चुनें',
      'gu': 'વર્ગ પસંદ કરો',
    },
    'Select Subject': {
      'en': 'Select Subject',
      'hi': 'विषय चुनें',
      'gu': 'વિષય પસંદ કરો',
    },
    'Chapters': {
      'en': 'Chapters',
      'hi': 'अध्याय',
      'gu': 'પ્રકરણો',
    },
    'Deselect All': {
      'en': 'Deselect All',
      'hi': 'सभी को अचयनित करें',
      'gu': 'બધા નાપસંદ કરો',
    },
    'Select All': {
      'en': 'Select All',
      'hi': 'सभी चुनें',
      'gu': 'બધા પસંદ કરો',
    },
    'Generate Paper': {
      'en': 'Generate Paper',
      'hi': 'पेपर जनरेट करें',
      'gu': 'પેપર જનરેટ કરો',
    },
    'No subjects found for this curriculum.': {
      'en': 'No subjects found for this curriculum.',
      'hi': 'इस पाठ्यक्रम के लिए कोई विषय नहीं मिला।',
      'gu': 'આ અભ્યાસક્રમ માટે કોઈ વિષય મળ્યા નથી.',
    },
    'No chapters found.': {
      'en': 'No chapters found.',
      'hi': 'कोई अध्याय नहीं मिला।',
      'gu': 'કોઈ પ્રકરણો મળ્યા નથી.',
    },
    'Please select at least one chapter!': {
      'en': 'Please select at least one chapter!',
      'hi': 'कृपया कम से कम एक अध्याय चुनें!',
      'gu': 'કૃપા કરીને ઓછામાં ઓછું એક પ્રકરણ પસંદ કરો!',
    },
    'No questions found for the selected chapters and types.': {
      'en': 'No questions found for the selected chapters and types.',
      'hi': 'चयनित अध्यायों के लिए कोई प्रश्न नहीं मिला।',
      'gu': 'પસંદ કરેલ પ્રકરણો માટે કોઈ પ્રશ્નો મળ્યા નથી.',
    },
  };

  /// Fetch translated UI strings (e.g., 'Home', 'Start', 'Stop')
  String getUIText(String key) {
    final lang = _activeViewLanguage;
    if (_uiTranslations.containsKey(key)) {
      final translations = _uiTranslations[key]!;
      if (translations.containsKey(lang)) {
        return translations[lang]!;
      }
    }
    final learningLabel = learningUiTranslations[key]?[lang];
    if (learningLabel != null) return learningLabel;
    return key; // Fallback to key
  }
}

// ── Dynamic Font Scaling Extension ──
extension TrilingualTextStyle on TextStyle {
  /// Dynamically boosts the font size, adjusts line height, and applies the correct
  /// Noto Sans Google Font if the active language is Hindi or Gujarati,
  /// ensuring they remain readable on large digital panels.
  TextStyle adaptToLanguage() {
    double? newFontSize = this.fontSize;
    if (newFontSize != null) {
      if (PresentationService.isPresentationMode.value) {
        newFontSize = 27.0; // 25% smaller than original 36.0
      } else {
        newFontSize += 2.0;
      }
    }

    if (TrilingualService.instance.activeViewLanguage == 'hi') {
      return this.copyWith(
        fontSize: newFontSize,
        fontFamily: 'NotoSansDevanagari',
      );
    } else if (TrilingualService.instance.activeViewLanguage == 'gu') {
      return this.copyWith(
        fontSize: newFontSize,
        fontFamily: 'NotoSansGujarati',
      );
    }
    return this.copyWith(fontSize: newFontSize);
  }
}
