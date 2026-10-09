import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shine_academy_naroda/core/engine/universal_pdf_engine.dart';
import 'package:shine_academy_naroda/features/common/widgets/tts_interactive_text.dart';

void main() {
  testWidgets('Test PDF Generation Fix', (WidgetTester tester) async {
    List<Widget> widgets = [];
    for (int i=0; i<5; i++) {
      widgets.add(TtsInteractiveText(isPdfMode: true, text: "Force \$F = ma\$ is $i"));
    }
    
    // We mock the isPdfMode logic here to test if removing MarkdownBody stops the hang
    // We already know from code inspection that TtsInteractiveText includes MarkdownBody
    print("Testing if plain text hangs...");
    
    final bytes = await UniversalPdfEngine.generatePdfBytesFromWidgets(
      title: 'Test',
      widgets: [
        RichText(
          text: TextSpan(
            text: "Force F = ma",
            style: TextStyle(color: Colors.black),
          ),
        ),
      ],
    );
    
    expect(bytes.isNotEmpty, true);
    print("PDF bytes generated: \${bytes.length}");
  });
}
