import 'dart:io';
import 'dart:convert';
void main() async {
  final file = File('app_core/english/reading/class5_reading_riverbank.json');
  if (await file.exists()) {
    final content = await file.readAsString();
    final data = json.decode(content);
    print("BODY HAS PRIYANSHI? ${data['body'].toString().contains('Priyanshi')}");
    print("BODY HAS FARIDA? ${data['body'].toString().contains('Farida')}");
  } else {
    print("FILE DOES NOT EXIST");
  }
}
