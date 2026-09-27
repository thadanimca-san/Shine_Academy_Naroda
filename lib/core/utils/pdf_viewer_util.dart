import 'dart:io';
import 'dart:typed_data';
import 'package:flutter/foundation.dart';
import 'package:path_provider/path_provider.dart';
import 'package:open_filex/open_filex.dart';

class PdfViewerUtil {
  static Future<void> openPdfBytes(Uint8List bytes, String filename) async {
    try {
      final dir = await getTemporaryDirectory();
      final file = File('${dir.path}/$filename');
      await file.writeAsBytes(bytes, flush: true);
      final result = await OpenFilex.open(file.path);
      debugPrint('OpenFilex result: ${result.message}');
    } catch (e) {
      debugPrint('Error opening PDF: $e');
    }
  }
}
