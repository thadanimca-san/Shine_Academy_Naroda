import 'package:flutter/material.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:shine_academy_naroda/foundation/theme/app_colors.dart';
import 'package:shine_academy_naroda/features/common/widgets/math_title.dart';

class HeadingWidget extends StatelessWidget {
  final Map<String, dynamic> data;

  const HeadingWidget({super.key, required this.data});

  @override
  Widget build(BuildContext context) {
    final title = TrilingualService.instance.getLocalizedText(data, 'title');

    return Container(
      margin: const EdgeInsets.symmetric(vertical: 24.0),
      padding: const EdgeInsets.symmetric(vertical: 8.0),
      decoration: const BoxDecoration(
        border: Border(
          bottom: BorderSide(
            color: AppColors.primary,
            width: 2.0,
          ),
        ),
      ),
      child: MathTitle(
        title,
        style: GoogleFonts.inter(
          fontSize: 24,
          fontWeight: FontWeight.bold,
          color: AppColors.primary,
        ).adaptToLanguage(),
      ),
    );
  }
}
