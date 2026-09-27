import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

void main() async {
  final service = TrilingualService.instance;
  // Mock active language
  service.setActiveViewLanguage('en');
  
  Map<String, dynamic> block = {
    'body': 'English text',
    'body_hi': 'Hindi text',
    'body_gu': 'Gujarati text'
  };

  print('EN: ${service.getLocalizedText(block, 'body')}');
  
  service.setActiveViewLanguage('hi');
  print('HI: ${service.getLocalizedText(block, 'body')}');
  
  service.setActiveViewLanguage('gu');
  print('GU: ${service.getLocalizedText(block, 'body')}');
  
  service.setActiveViewLanguage('en');
  print('EN again: ${service.getLocalizedText(block, 'body')}');
}
