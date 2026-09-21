import 'package:flutter/material.dart';
import '../services/presentation_service.dart';

class PresentationBuilder extends StatelessWidget {
  final Widget Function(BuildContext context, double scaleFactor) builder;

  const PresentationBuilder({super.key, required this.builder});

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<bool>(
      valueListenable: PresentationService.isPresentationMode,
      builder: (context, isPresentationMode, child) {
        final scale = PresentationService.getScaleFactor(context);
        return builder(context, scale);
      },
    );
  }
}
