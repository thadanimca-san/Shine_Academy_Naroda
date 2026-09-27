import 'dart:convert';
import 'dart:io';

void main() {
  final file = File('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class7_science_ch1.json');
  final jsonString = file.readAsStringSync();
  final data = json.decode(jsonString);
  print("Root keys: ${data.keys}");
  
  final contentBlocks = (data['content'] ?? data['blocks']) as List? ?? [];
  print("Found ${contentBlocks.length} blocks");
  
  for (var rawBlock in contentBlocks) {
    print("\n--- Raw Block Type: ${rawBlock['type']} ---");
    print("Raw Block keys: ${rawBlock.keys}");
    if (rawBlock['content'] != null) {
        print("Raw Content type: ${rawBlock['content'].runtimeType}");
        if (rawBlock['content'] is Map) {
            print("Raw Content keys: ${(rawBlock['content'] as Map).keys}");
        }
    }
  }
}
