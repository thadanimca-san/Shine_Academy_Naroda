import 'dart:io';
import 'package:flutter/material.dart';
import 'package:printing/printing.dart';
import 'package:pdf/pdf.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  try {
    print('Starting PDF generation...');
    final bytes = await Printing.convertHtml(
      html: '<html><body><h1>Hello World</h1></body></html>',
      format: PdfPageFormat.a4,
    );
    print('PDF generated successfully. Bytes: ${bytes.length}');
  } catch (e, stack) {
    print('Error: $e');
    print(stack);
  }
  exit(0);
}
