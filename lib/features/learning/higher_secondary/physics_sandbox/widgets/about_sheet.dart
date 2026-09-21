import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Academy identity lives here instead of occupying permanent home-screen
/// space. Opened from the small footer link.
void showAboutSheet(BuildContext context) {
  showModalBottomSheet(
    context: context,
    builder: (context) => SafeArea(
      child: Padding(
        padding: const EdgeInsets.fromLTRB(Gap.x6, 0, Gap.x6, Gap.x6),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Container(
              width: 64,
              height: 64,
              decoration: BoxDecoration(
                gradient: const LinearGradient(
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                  colors: [Palette.primary, Palette.primaryDeep],
                ),
                borderRadius: BorderRadius.circular(Corner.lg),
              ),
              child: Icon(Icons.school_rounded, color: Colors.white, size: 32),
            ),
            const SizedBox(height: Gap.x4),
            Text(TrilingualService.instance.getUIText('Shine Academy, Naroda'), style: Type.title),
            const SizedBox(height: Gap.x1),
            Text(TrilingualService.instance.getUIText('Guided by Govind Sir Thadani'), style: Type.caption.copyWith(fontSize: 13.5)),
            const SizedBox(height: Gap.x4),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: Gap.x4, vertical: Gap.x3),
              decoration: BoxDecoration(
                color: Palette.primarySoft,
                borderRadius: BorderRadius.circular(Corner.md),
              ),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Icon(Icons.phone_rounded, size: 16, color: Palette.primaryDeep),
                  const SizedBox(width: Gap.x2),
                  Text(TrilingualService.instance.getUIText('94087 21039'),
                      style: Type.bodyStrong.copyWith(color: Palette.primaryDeep, letterSpacing: 0.5)),
                ],
              ),
            ),
            const SizedBox(height: Gap.x4),
            Text(TrilingualService.instance.getUIText('Interactive physics labs built to make JEE & NEET concepts felt, not memorized.'),
              textAlign: TextAlign.center,
              style: Type.caption,
            ),
          ],
        ),
      ),
    ),
  );
}
