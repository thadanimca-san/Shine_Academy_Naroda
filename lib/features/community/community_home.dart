import 'package:flutter/material.dart';
import 'moderation_dashboard_screen.dart';
import '../../foundation/theme/brand_app_bar.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class CommunityHome extends StatelessWidget {
  const CommunityHome({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const BrandAppBar(title: 'Community'),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(TrilingualService.instance.getUIText('Forums, chat, and discussions will go here.')),
            const SizedBox(height: 40),
            ElevatedButton.icon(
              onPressed: () {
                Navigator.push(context, MaterialPageRoute(builder: (context) => const ModerationDashboardScreen()));
              },
              icon: Icon(Icons.admin_panel_settings),
              label: Text(TrilingualService.instance.getUIText('Admin: Moderation Dashboard')),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.red.shade900,
                foregroundColor: Colors.white,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
