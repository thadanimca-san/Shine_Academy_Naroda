import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shine_academy_naroda/core/engine/universal_pdf_engine.dart';
import 'package:shine_academy_naroda/features/common/widgets/tts_interactive_text.dart';
import 'package:flutter_markdown/flutter_markdown.dart';

void main() {
  testWidgets('Test PDF Generation with Math', (WidgetTester tester) async {
    List<Widget> widgets = [];
    for (int i=0; i<5; i++) {
      widgets.add(TtsInteractiveText(isPdfMode: true, text: "Force \$F = ma\$ is $i"));
    }
    
    // We cannot use await generatePdfFromWidgets because it uses path_provider, but we can call generatePdfBytesFromWidgets
    final bytes = await UniversalPdfEngine.generatePdfBytesFromWidgets(
      title: 'Test',
      widgets: widgets,
    );
    
    expect(bytes.isNotEmpty, true);
    print("PDF bytes generated: \${bytes.length}");
  });
}
