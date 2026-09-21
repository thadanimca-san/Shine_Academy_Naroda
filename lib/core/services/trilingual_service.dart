import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:translator/translator.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import 'package:shine_academy_naroda/core/services/presentation_service.dart';

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
      return GoogleFonts.notoSans(
        fontSize: newFontSize,
        fontWeight: this.fontWeight,
        color: this.color,
        height: this.height,
      );
    } else if (TrilingualService.instance.activeViewLanguage == 'gu') {
      return GoogleFonts.notoSansGujarati(
        fontSize: newFontSize,
        fontWeight: this.fontWeight,
        color: this.color,
        height: this.height,
      );
    }
    return this;
  }
}
