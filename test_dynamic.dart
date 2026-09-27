void main() {
  Map<String, dynamic> termMap = {
    "term": { "english": "School" }
  };
  
  try {
    final termEn = termMap['term']?['english']?.toString().toLowerCase() ?? '';
    print("termEn: $termEn");
  } catch(e) {
    print("Error: $e");
  }
}
