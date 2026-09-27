import 'dart:convert';
import 'dart:io';
void main() async {
  try {
    final file = File('app_core/universal_dictionary/generated_massive_dict.json');
    final content = await file.readAsString();
    final data = json.decode(content);
    print("Loaded ${data['terms'].length} terms");
  } catch (e) {
    print("Error: $e");
  }
}
