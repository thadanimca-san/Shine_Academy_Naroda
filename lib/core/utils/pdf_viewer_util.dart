import 'dart:io';
import 'package:flutter/foundation.dart';
import 'package:path_provider/path_provider.dart';
import 'package:open_filex/open_filex.dart';
import 'package:printing/printing.dart';

class PdfViewerUtil {
  /// Saves the PDF and opens it in the device's PDF viewer. Many classroom
  /// panels have no PDF viewer installed, so when nothing can open the file we
  /// fall back to the system print/share sheet, where it can be saved or printed.
  static Future<void> openPdfBytes(Uint8List bytes, String filename) async {
    try {
      final dir = await getTemporaryDirectory();
      final file = File('${dir.path}/$filename');
      await file.writeAsBytes(bytes, flush: true);
      final result = await OpenFilex.open(file.path);
      debugPrint('OpenFilex result: ${result.type} ${result.message}');
      if (result.type == ResultType.done) return;
    } catch (e) {
      debugPrint('Error opening PDF: $e');
    }
    await Printing.sharePdf(bytes: bytes, filename: filename);
  }
}
