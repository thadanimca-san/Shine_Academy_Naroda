import 'package:flutter/material.dart';

import 'tts_interactive_text.dart';

/// A heading that renders inline LaTeX (`$\sqrt{2}$`) like body text does.
/// Titles without a formula stay a plain [Text], so they look exactly as before.
class MathTitle extends StatelessWidget {
  final String text;
  final TextStyle? style;

  const MathTitle(this.text, {super.key, this.style});

  @override
  Widget build(BuildContext context) => text.contains(r'$')
      ? TtsInteractiveText(text: text, style: style, enableWordTap: false)
      : Text(text, style: style);
}
