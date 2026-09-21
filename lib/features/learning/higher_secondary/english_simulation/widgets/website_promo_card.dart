import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A compact card promoting the Shine Academy Naroda website, styled
/// distinctly from the navy chapter cards (gold accent, globe icon) so it
/// reads as "visit our site" at a glance rather than another chapter link.
class WebsitePromoCard extends StatelessWidget {
  final String title;
  final String subtitle;
  final String url;

  const WebsitePromoCard({super.key, required this.title, required this.subtitle, required this.url});

  Future<void> _open(BuildContext context) async {
    final uri = Uri.parse(url);
    final launched = await launchUrl(uri, mode: LaunchMode.externalApplication);
    if (!launched && context.mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(TrilingualService.instance.getUIText('Could not open the link.'))),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 3,
      color: Colors.amber[50],
      child: ListTile(
        leading: Icon(Icons.language, color: Colors.amber[800], size: 36),
        title: Text(title, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
        subtitle: Text(subtitle),
        trailing: Icon(Icons.open_in_new, color: Colors.amber[800]),
        onTap: () => _open(context),
      ),
    );
  }
}
