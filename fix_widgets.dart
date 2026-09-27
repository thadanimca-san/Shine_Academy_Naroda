import 'dart:io';

void main() {
  File f = File('lib/features/learning/school/english/widgets/dictionary_word_widgets.dart');
  String content = f.readAsStringSync();
  
  content = content.replaceAll("word['term']?['english']", "(word['term'] as Map?)?['english']");
  content = content.replaceAll("word['term']?['hindi']", "(word['term'] as Map?)?['hindi']");
  content = content.replaceAll("word['term']?['hi']", "(word['term'] as Map?)?['hi']");
  content = content.replaceAll("word['term']?['gujarati']", "(word['term'] as Map?)?['gujarati']");
  content = content.replaceAll("word['term']?['gu']", "(word['term'] as Map?)?['gu']");
  
  f.writeAsStringSync(content);
}
