import 'dart:convert';
import 'dart:io';

void main() {
  final file = File('/home/ubuntu/Shine_Academy_Naroda/app_core/universal_dictionary/generated_massive_dict.json');
  final String jsonString = file.readAsStringSync();
  final Map<String, dynamic> dictData = json.decode(jsonString);
  int count = 0;
  for (var term in dictData['terms']) {
    try {
      if (term['id'] != null) {
        var map = term as Map<String, dynamic>;
        count++;
      }
    } catch(e) {
      print("Error on term index $count: $e");
      break;
    }
  }
  print("Validated $count terms.");
}
