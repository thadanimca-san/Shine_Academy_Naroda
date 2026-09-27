import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'dart:io';

void main() async {
  try {
    final pdf = pw.Document(
      // Let's see if this compiles
      // documentOptions: PdfDocumentOptions(...) or something?
    );
    pdf.addPage(pw.Page(build: (pw.Context context) => pw.Center(child: pw.Text("Hello World"))));
    print("Success");
  } catch (e) {
    print(e);
  }
}
