import 'dart:io';

import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

import '../data/branding.dart';

/// Shows the Shine Academy Naroda logo + tagline if the logo asset has
/// been placed on disk; falls back to a text-only banner otherwise so
/// the app never breaks while the asset is pending. Tapping it opens the
/// academy's website.
class BrandingHeaderWidget extends StatelessWidget {
  const BrandingHeaderWidget({super.key});

  @override
  Widget build(BuildContext context) {
    final logoFile = File(Branding.logoAssetPath);
    final hasLogo = logoFile.existsSync();

    return InkWell(
      onTap: () => launchUrl(Uri.parse(Branding.websiteUrl), mode: LaunchMode.externalApplication),
      borderRadius: BorderRadius.circular(8),
      child: Padding(
        padding: const EdgeInsets.symmetric(vertical: 8, horizontal: 12),
        child: Row(
          children: [
            if (hasLogo)
              Image.asset(Branding.logoAssetPath, height: 40)
            else
              Icon(Icons.school, size: 32, color: Colors.indigo),
            const SizedBox(width: 10),
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(Branding.academyName,
                    style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                Text(Branding.tagline, style: TextStyle(fontSize: 11, color: Colors.grey)),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
