import 'dart:io';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:path_provider/path_provider.dart';

void main() {
  testWidgets('Test native pdf package', (WidgetTester tester) async {
    final pdf = pw.Document();

    pdf.addPage(
      pw.MultiPage(
        pageFormat: PdfPageFormat.a4,
        margin: const pw.EdgeInsets.all(32),
        build: (pw.Context ctx) {
          return [
            pw.Text("Hello World", style: pw.TextStyle(fontSize: 24)),
            pw.SizedBox(height: 10),
            pw.Text("This is a test of the native pdf package."),
          ];
        },
      ),
    );

    final bytes = await pdf.save();
    print("PDF bytes generated: \${bytes.length}");
    expect(bytes.isNotEmpty, true);
  });
}
