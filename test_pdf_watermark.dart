import 'dart:io';
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;

void main() {
  final pdf = pw.Document();
  pdf.addPage(
    pw.MultiPage(
      pageTheme: pw.PageTheme(
        buildBackground: (pw.Context context) {
          return pw.Center(
            child: pw.Text("WATERMARK", style: pw.TextStyle(fontSize: 40)),
          );
        },
      ),
      build: (pw.Context context) {
        return [pw.Text("Hello")];
      }
    )
  );
  print("OK");
}
