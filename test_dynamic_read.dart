void main() {
  Map<String, dynamic> word = {
    'term': {
      'english': 'apple',
      'hindi': 'सेब'
    },
    'definition': {
      'simple': {
        'en': 'A fruit'
      }
    }
  };

  try {
    // word['term'] is dynamic
    // we must cast it to Map
    var term = word['term'];
    if (term is Map) {
      String en = term['english']?.toString().toLowerCase() ?? '';
      print("English: $en");
    } else {
      print("term is not map");
    }
  } catch (e) {
    print("Error: $e");
  }
}
