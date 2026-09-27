import 'dart:convert';
import 'dart:io';

void main() {
  try {
    final file = File('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_stats_ch3.json');
    final content = file.readAsStringSync();
    print("Read file: ${content.length} characters");
    final data = json.decode(content);
    print("Decoded as: ${data.runtimeType}");
    
    // Simulate _normalizeData
    dynamic normalized;
    if (data is List) {
      normalized = {
        'metadata': {},
        'blocks': data,
      };
      print("Normalized array of ${data.length} blocks.");
    } else {
      normalized = data;
    }
    
    final blocks = (normalized['content'] ?? normalized['blocks']) as List? ?? [];
    print("Found ${blocks.length} blocks.");
    
    for (int i = 0; i < blocks.length; i++) {
       var b = blocks[i];
       if (b['type'] == null) {
          print("Block $i is missing type");
       }
    }
    print("Test passed successfully.");
  } catch (e, stack) {
    print("Error: $e");
    print(stack);
  }
}
