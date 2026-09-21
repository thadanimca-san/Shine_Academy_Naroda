import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../../core/widgets/presentation_builder.dart';
import '../../../dictionary/dictionary_popup.dart';

class DictionaryLinkWidget extends StatefulWidget {
  final Map<String, dynamic> data;
  const DictionaryLinkWidget({super.key, required this.data});

  @override
  State<DictionaryLinkWidget> createState() => _DictionaryLinkWidgetState();
}

class _DictionaryLinkWidgetState extends State<DictionaryLinkWidget> {
  Map<String, dynamic>? _termData;
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadTerm();
  }

  Future<void> _loadTerm() async {
    try {
      final termId = widget.data['term_id'] ?? 
                     (widget.data['data'] is Map ? widget.data['data']['term_id'] : null) ??
                     (widget.data['content'] is Map ? widget.data['content']['term_id'] : null);
      final jsonStr = await rootBundle.loadString('app_core/knowledge_graph/dictionary/$termId.json');
      setState(() {
        _termData = json.decode(jsonStr);
        _isLoading = false;
      });
    } catch (e) {
      setState(() {
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading) return const Padding(padding: EdgeInsets.all(20), child: CircularProgressIndicator());
    if (_termData == null) return const SizedBox.shrink();

    final term = _termData!['term']['english'];
    final def = _termData!['definition'] ?? _termData!['definitions'] ?? {};
    final simpleDef = def['simple'] ?? def['standard'] ?? 'Definition not available.';

    return PresentationBuilder(
      builder: (context, scale) {
        return Container(
          margin: const EdgeInsets.only(bottom: 20),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(12),
            border: Border.all(color: Colors.blue[100]!),
            boxShadow: [
              BoxShadow(
                color: Colors.blue.withValues(alpha: 0.05),
                blurRadius: 5,
                offset: const Offset(0, 2),
              )
            ],
          ),
          child: ListTile(
            contentPadding: const EdgeInsets.all(16),
            leading: Container(
              padding: const EdgeInsets.all(8),
              decoration: BoxDecoration(
                color: Colors.blue[50],
                shape: BoxShape.circle,
              ),
              child: Icon(Icons.menu_book, color: Colors.blue[800]),
            ),
            title: Text(
              term,
              style: GoogleFonts.poppins(fontWeight: FontWeight.bold, fontSize: 18 * scale, color: Colors.blue[900]),
            ),
            subtitle: Text(
              simpleDef,
              style: GoogleFonts.inter(fontSize: 14 * scale, color: Theme.of(context).colorScheme.onSurface),
            ),
            trailing: Icon(Icons.arrow_forward_ios, size: 16 * scale, color: Colors.grey[400]),
            onTap: () {
              final tId = widget.data['term_id'] ?? 
                          (widget.data['data'] is Map ? widget.data['data']['term_id'] : null) ??
                          (widget.data['content'] is Map ? widget.data['content']['term_id'] : null);
              if (tId != null) {
                UniversalDictionaryPopup.show(context, tId);
              }
            },
          ),
        );
      }
    );
  }
}
