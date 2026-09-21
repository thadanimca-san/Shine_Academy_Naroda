import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class MediaWidget extends StatelessWidget {
  final Map<String, dynamic> data;

  const MediaWidget({super.key, required this.data});

  @override
  Widget build(BuildContext context) {
    final payload = data['data'] ?? data;
    final mediaType = payload['mediaType'] ?? 'image';
    final url = payload['url'] ?? '';
    final caption = payload['caption'] ?? '';

    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.05),
            blurRadius: 10,
            offset: const Offset(0, 4),
          )
        ],
        border: Border.all(color: Colors.grey.shade200),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          ClipRRect(
            borderRadius: const BorderRadius.vertical(top: Radius.circular(16)),
            child: url.isNotEmpty
                ? (url.startsWith('http')
                    ? Image.network(
                        url,
                        fit: BoxFit.cover,
                        errorBuilder: (c, o, s) => _buildPlaceholder(),
                      )
                    : Image.asset(
                        url,
                        fit: BoxFit.cover,
                        errorBuilder: (c, o, s) => _buildPlaceholder(),
                      ))
                : _buildPlaceholder(),
          ),
          if (caption.isNotEmpty)
            Padding(
              padding: const EdgeInsets.all(16),
              child: Text(
                caption,
                textAlign: TextAlign.center,
                style: GoogleFonts.inter(
                  fontSize: 14,
                  fontStyle: FontStyle.italic,
                  color: Colors.grey.shade700,
                ),
              ),
            ),
        ],
      ),
    );
  }

  Widget _buildPlaceholder() {
    return Container(
      height: 200,
      color: Colors.grey.shade100,
      child: const Center(
        child: Icon(Icons.broken_image, size: 50, color: Colors.grey),
      ),
    );
  }
}
