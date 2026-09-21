import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A compact card promoting a YouTube channel/playlist, styled distinctly
/// from the blue chapter cards (red accent, play icon) so it reads as
/// "watch a video" at a glance rather than another chapter link.
class VideoPromoCard extends StatelessWidget {
  final String title;
  final String subtitle;
  final String url;

  const VideoPromoCard({super.key, required this.title, required this.subtitle, required this.url});

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
      color: Colors.red[50],
      child: ListTile(
        leading: Icon(Icons.smart_display, color: Colors.red[700], size: 36),
        title: Text(title, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
        subtitle: Text(subtitle),
        trailing: Icon(Icons.open_in_new, color: Colors.red[700]),
        onTap: () => _open(context),
      ),
    );
  }
}
