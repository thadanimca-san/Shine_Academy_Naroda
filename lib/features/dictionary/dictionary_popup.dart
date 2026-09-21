import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../foundation/theme/app_colors.dart';
import '../../core/services/tts_service.dart';
import '../../core/services/universal_dictionary_service.dart';
import '../common/widgets/tts_interactive_text.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

// Result wrapper: found term + optional nearest suggestion when not found
class _LookupResult {
  final Map<String, dynamic>? term;         // exact / best match
  final Map<String, dynamic>? nearest;      // alphabetically nearest when term==null
  final String query;

  const _LookupResult({required this.query, this.term, this.nearest});
  bool get found => term != null;
}

class UniversalDictionaryPopup {

  // ─────────────────────────────────────────────────────────────────────────
  // Core lookup — uses the in-memory UniversalDictionaryService cache.
  // Handles:
  //  • Internal ID links  (e.g. "DICT_MATTER" from DictionaryEngine)
  //  • Raw selected words (e.g. "photosynthesis" from user double-tap)
  // ─────────────────────────────────────────────────────────────────────────
  static Future<_LookupResult> _lookup(String raw) async {
    final service = UniversalDictionaryService.instance;
    await service.init();

    final String cleaned = raw
        .replaceAll(RegExp(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$'), '')
        .trim();

    if (cleaned.isEmpty) {
      return _LookupResult(query: raw);
    }
    
    // Pass 1: ID Match
    var term = await service.getTermById(raw);
    if (term == null && raw.toUpperCase() != raw) {
        term = await service.getTermById(raw.toUpperCase());
    }
    
    if (term != null) {
      return _LookupResult(query: raw, term: term);
    }
    
    // Pass 2: Search word match
    final results = await service.searchTerms(cleaned);
    if (results.isNotEmpty) {
      // Find exact match if possible
      for (final t in results) {
         final en = (t['term']?['english'] ?? '').toString().toLowerCase().trim();
         if (en == cleaned.toLowerCase()) return _LookupResult(query: raw, term: t);
      }
      return _LookupResult(query: raw, term: results.first);
    }
    
    // If not found at all
    return _LookupResult(query: raw);
  }

  static void show(BuildContext context, String termId) {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) {
        return Padding(
          padding: EdgeInsets.only(bottom: MediaQuery.of(context).viewInsets.bottom),
          child: _DictionaryPopupContent(initialQuery: termId),
        );
      },
    );
  }

  static Widget _buildNotFound(
    BuildContext context,
    String query,
    Map<String, dynamic>? nearest,
  ) {
    final nearestEn = nearest != null
        ? (nearest['term']?['english'] ?? '').toString()
        : null;
    final nearestSimple = nearest != null
        ? (() {
            final def = nearest['definition']?['simple'];
            return (def is Map ? def['en'] : def)?.toString() ?? '';
          })()
        : '';

    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Icon(Icons.search_off, size: 52, color: Colors.grey),
        const SizedBox(height: 12),
        Text(
          '"$query"',
          style: GoogleFonts.poppins(
            fontSize: 20,
            fontWeight: FontWeight.bold,
            color: AppColors.textPrimary,
          ),
        ),
        const SizedBox(height: 4),
        Text(TrilingualService.instance.getUIText('This word is not in our dictionary yet.'),
          style: GoogleFonts.inter(fontSize: 14, color: Theme.of(context).colorScheme.onSurfaceVariant),
          textAlign: TextAlign.center,
        ),
        if (query == '_' || query.isEmpty) ...[
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: Colors.blue.shade50,
              borderRadius: BorderRadius.circular(8),
            ),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Icon(Icons.info_outline, size: 20, color: Colors.blue.shade700),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(TrilingualService.instance.getUIText('Tip: Text selection failed on this device. Please use the dictionary search icon at the top of the screen instead.'),
                    style: TextStyle(fontSize: 12, color: Colors.blue.shade900),
                  ),
                ),
              ],
            ),
          ),
        ],
        const SizedBox(height: 24),

        // ── Nearest match card ─────────────────────────────────────────────
        if (nearestEn != null && nearestEn.isNotEmpty) ...[
          const SizedBox(height: 20),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: Colors.orange.shade50,
              borderRadius: BorderRadius.circular(14),
              border: Border.all(color: Colors.orange.shade200),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Icon(Icons.my_location_rounded,
                        size: 16, color: Colors.orange),
                    const SizedBox(width: 6),
                    Text(TrilingualService.instance.getUIText('Nearest word in dictionary:'),
                      style: GoogleFonts.inter(
                        fontSize: 12,
                        fontWeight: FontWeight.w600,
                        color: Colors.orange.shade800,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                Text(
                  nearestEn,
                  style: GoogleFonts.poppins(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                    color: AppColors.textPrimary,
                  ),
                ),
                if (nearestSimple.isNotEmpty) ...[
                  const SizedBox(height: 4),
                  Text(
                    nearestSimple,
                    style: GoogleFonts.inter(
                      fontSize: 14,
                      color: Theme.of(context).colorScheme.onSurface,
                      height: 1.4,
                    ),
                    maxLines: 3,
                    overflow: TextOverflow.ellipsis,
                  ),
                ],
                const SizedBox(height: 12),
                OutlinedButton.icon(
                  onPressed: () {
                    Navigator.of(context).pop();
                    show(context, nearest!['id'].toString());
                  },
                  icon: Icon(Icons.open_in_new, size: 16),
                  label: Text('View "$nearestEn"'),
                  style: OutlinedButton.styleFrom(
                    foregroundColor: Colors.orange.shade800,
                    side: BorderSide(color: Colors.orange.shade400),
                  ),
                ),
              ],
            ),
          ),
        ],

        const SizedBox(height: 20),
        ElevatedButton.icon(
          onPressed: () => Navigator.of(context).pop(),
          icon: Icon(Icons.close),
          label: Text(TrilingualService.instance.getUIText('Close')),
          style: ElevatedButton.styleFrom(
            backgroundColor: AppColors.primary,
            foregroundColor: Colors.white,
          ),
        ),
        const SizedBox(height: 8),
      ],
    );
  }

  // ─────────────────────────────────────────────────────────────────────────
  // Full term detail panel
  // ─────────────────────────────────────────────────────────────────────────
  static Widget _buildTermDetail(BuildContext context, Map<String, dynamic> item) {
    final term      = item['term']      ?? {};
    final def       = item['definition'] ?? {};
    final aiContext = item['ai_context'] ?? {};
    final examples  = item['examples']  ?? [];

    final String en = term['english']  ?? '';
    final String hi = term['hindi']    ?? term['hi'] ?? '';
    final String gu = term['gujarati'] ?? term['gu'] ?? '';

    final pronunciation = item['pronunciation'] ?? {};
    final String _rawEn = pronunciation['english'] ?? pronunciation['en'] ?? '';
    final String pronunEn = _rawEn.replaceAll(RegExp(r'^/+|-+|/+$'), '').trim();
    final String _rawHi = pronunciation['hindi'] ?? pronunciation['hi'] ?? item['pronunciation_hi'] ?? '';
    final String pronunHi = _rawHi.replaceAll(RegExp(r'^/+|-+|/+$'), '').trim();

    // Handle both plain-string and trilingual-map definitions
    final simpleRaw = def['simple'];
    final String simpleEn = simpleRaw is Map ? (simpleRaw['en'] ?? '') : (simpleRaw ?? '');
    final String simpleHi = simpleRaw is Map ? (simpleRaw['hi'] ?? '') : '';
    final String simpleGu = simpleRaw is Map ? (simpleRaw['gu'] ?? '') : '';

    final academicRaw = def['academic'];
    final String academicEn = academicRaw is Map ? (academicRaw['en'] ?? '') : (academicRaw ?? '');

    return SingleChildScrollView(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // ── Header: word + TTS button ──────────────────────────────────
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      children: [
                        Flexible(
                          child: Text(
                            en,
                            style: GoogleFonts.poppins(
                              fontWeight: FontWeight.bold,
                              fontSize: 24,
                              color: AppColors.textPrimary,
                            ),
                          ),
                        ),
                        const SizedBox(width: 8),
                        IconButton(
                          icon: Icon(Icons.volume_up, size: 22, color: Colors.blueGrey),
                          tooltip: 'Listen to Pronunciation',
                          padding: EdgeInsets.zero,
                          constraints: const BoxConstraints(),
                          onPressed: () => TTSService.instance.speak(en),
                        ),
                      ],
                    ),
                    if (pronunEn.isNotEmpty || pronunHi.isNotEmpty) ...[
                      const SizedBox(height: 2),
                      Text(
                        '/${pronunEn.isNotEmpty ? pronunEn : ''}${pronunHi.isNotEmpty && pronunEn.isNotEmpty ? ' • ' : ''}${pronunHi.isNotEmpty ? pronunHi : ''}/',
                        style: GoogleFonts.inter(
                          color: AppColors.primary,
                          fontSize: 14,
                          fontStyle: FontStyle.italic,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ],
                    if (hi.isNotEmpty || gu.isNotEmpty) ...[
                      const SizedBox(height: 4),
                      Text(
                        '$hi ${hi.isNotEmpty && gu.isNotEmpty ? '|' : ''} $gu',
                        style: GoogleFonts.notoSans(
                          color: AppColors.textSecondary,
                          fontSize: 16,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ],
                  ],
                ),
              ),
              ValueListenableBuilder<bool>(
                valueListenable: TTSService.instance.isPlayingGlobal,
                builder: (context, isPlaying, child) {
                  return IconButton(
                    icon: Icon(
                      isPlaying ? Icons.stop_circle_rounded : Icons.volume_up_rounded,
                      color: isPlaying ? Colors.red : AppColors.primary,
                      size: 28,
                    ),
                    onPressed: () {
                      if (isPlaying) {
                        TTSService.instance.stop();
                      } else {
                        TTSService.instance.speak('$en. $simpleEn');
                      }
                    },
                  );
                },
              ),
            ],
          ),

          const SizedBox(height: 16),
          const Divider(),
          const SizedBox(height: 16),

          // ── Simple meaning ─────────────────────────────────────────────
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: AppColors.primary.withValues(alpha: 0.05),
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: AppColors.primary.withValues(alpha: 0.2)),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(TrilingualService.instance.getUIText('🧠 Simple Meaning'),
                  style: GoogleFonts.inter(
                    fontWeight: FontWeight.bold,
                    color: AppColors.primary,
                    fontSize: 14,
                  ),
                ),
                const SizedBox(height: 8),
                TtsInteractiveText(
                  text: simpleEn,
                  fullTtsText: '$en. $simpleEn',
                  style: GoogleFonts.inter(
                    fontSize: 16,
                    color: Theme.of(context).colorScheme.onSurface,
                    height: 1.5,
                  ),
                ),
                if (simpleHi.isNotEmpty) ...[
                  const SizedBox(height: 8),
                  Text(simpleHi,
                      style: GoogleFonts.notoSans(
                          fontSize: 15, color: Theme.of(context).colorScheme.onSurface, height: 1.5)),
                ],
                if (simpleGu.isNotEmpty) ...[
                  const SizedBox(height: 8),
                  Text(simpleGu,
                      style: GoogleFonts.notoSans(
                          fontSize: 15, color: Theme.of(context).colorScheme.onSurface, height: 1.5)),
                ],
              ],
            ),
          ),

          // ── Examples ───────────────────────────────────────────────────
          if (examples is List && examples.isNotEmpty) ...[
            const SizedBox(height: 24),
            Text(TrilingualService.instance.getUIText('💡 Examples'),
              style: GoogleFonts.inter(
                  fontWeight: FontWeight.bold,
                  color: Theme.of(context).colorScheme.onSurface,
                  fontSize: 16),
            ),
            const SizedBox(height: 12),
            ...examples.map((ex) {
              final String exEn = ex is Map ? (ex['en'] ?? '') : ex.toString();
              final String exHi = ex is Map ? (ex['hi'] ?? '') : '';
              final String exGu = ex is Map ? (ex['gu'] ?? '') : '';
              return Container(
                margin: const EdgeInsets.only(bottom: 12),
                padding: const EdgeInsets.only(left: 12),
                decoration: BoxDecoration(
                  border: Border(
                    left: BorderSide(
                        color: AppColors.primary.withValues(alpha: 0.5), width: 3),
                  ),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(exEn,
                        style: GoogleFonts.inter(
                            fontSize: 15,
                            color: Theme.of(context).colorScheme.onSurface,
                            fontStyle: FontStyle.italic)),
                    if (exHi.isNotEmpty)
                      Text(exHi,
                          style: GoogleFonts.notoSans(
                              fontSize: 14, color: Colors.grey.shade700)),
                    if (exGu.isNotEmpty)
                      Text(exGu,
                          style: GoogleFonts.notoSans(
                              fontSize: 14, color: Colors.grey.shade700)),
                  ],
                ),
              );
            }),
          ],

          // ── Academic definition ────────────────────────────────────────
          if (academicEn.isNotEmpty) ...[
            const SizedBox(height: 16),
            Text(TrilingualService.instance.getUIText('📚 Academic Definition'),
              style: GoogleFonts.inter(
                  fontWeight: FontWeight.bold,
                  color: Colors.grey.shade700,
                  fontSize: 14),
            ),
            const SizedBox(height: 4),
            Text(academicEn,
                style: GoogleFonts.inter(
                    fontSize: 15,
                    color: Theme.of(context).colorScheme.onSurface,
                    fontStyle: FontStyle.italic)),
          ],

          // ── Common misconceptions ──────────────────────────────────────
          if (aiContext['common_misconceptions'] != null &&
              (aiContext['common_misconceptions'] as List).isNotEmpty) ...[
            const SizedBox(height: 16),
            Text(TrilingualService.instance.getUIText('⚠️ Common Misconception'),
              style: GoogleFonts.inter(
                  fontWeight: FontWeight.bold,
                  color: Colors.red.shade700,
                  fontSize: 14),
            ),
            const SizedBox(height: 4),
            Text(
              (aiContext['common_misconceptions'] as List).first.toString(),
              style: GoogleFonts.inter(
                  fontSize: 15, color: Colors.red.shade900),
            ),
          ],

          const SizedBox(height: 24),
        ],
      ),
    );
  }

// _buildContainer is removed since _DictionaryPopupContent handles it now
}


class _DictionaryPopupContent extends StatefulWidget {
  final String initialQuery;
  const _DictionaryPopupContent({required this.initialQuery});

  @override
  State<_DictionaryPopupContent> createState() => _DictionaryPopupContentState();
}

class _DictionaryPopupContentState extends State<_DictionaryPopupContent> {
  late TextEditingController _controller;
  _LookupResult? _result;
  bool _isLoading = false;

  @override
  void initState() {
    super.initState();
    _controller = TextEditingController(text: widget.initialQuery == '_' ? '' : widget.initialQuery);
    if (_controller.text.isNotEmpty) {
      _performSearch(_controller.text);
    }
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  Future<void> _performSearch(String query) async {
    if (query.trim().isEmpty) {
      setState(() {
        _result = null;
        _isLoading = false;
      });
      return;
    }
    setState(() => _isLoading = true);
    final res = await UniversalDictionaryPopup._lookup(query);
    
    if (res.term != null) {
      await TrilingualService.instance.preTranslateBlocks([res.term], isDictionary: true);
    }
    
    if (mounted) {
      setState(() {
        _result = res;
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      constraints: BoxConstraints(
        maxHeight: MediaQuery.of(context).size.height * 0.85,
      ),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          // Handle
          Center(
            child: Container(
              margin: const EdgeInsets.only(top: 12, bottom: 8),
              width: 40,
              height: 4,
              decoration: BoxDecoration(
                color: Colors.grey.shade300,
                borderRadius: BorderRadius.circular(2),
              ),
            ),
          ),
          
          // Search Bar
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 8),
            child: TextField(
              controller: _controller,
              textInputAction: TextInputAction.search,
              onSubmitted: _performSearch,
              decoration: InputDecoration(
                hintText: 'Search for a word...',
                prefixIcon: Icon(Icons.search, color: AppColors.primary),
                suffixIcon: IconButton(
                  icon: Icon(Icons.clear),
                  onPressed: () {
                    if (_controller.text.isEmpty) {
                      Navigator.of(context).pop();
                    } else {
                      _controller.clear();
                      _performSearch('');
                    }
                  },
                ),
                filled: true,
                fillColor: Colors.grey.shade100,
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(12),
                  borderSide: BorderSide.none,
                ),
                contentPadding: const EdgeInsets.symmetric(vertical: 0),
              ),
            ),
          ),

          Flexible(
            child: SingleChildScrollView(
              padding: const EdgeInsets.fromLTRB(24, 8, 24, 32),
              child: _isLoading 
                  ? const Padding(
                      padding: EdgeInsets.all(32.0),
                      child: Center(child: CircularProgressIndicator(color: AppColors.primary)),
                    )
                  : (_result == null 
                      ? const SizedBox.shrink()
                      : (_result!.found
                          ? UniversalDictionaryPopup._buildTermDetail(context, _result!.term!)
                          : UniversalDictionaryPopup._buildNotFound(context, _result!.query, _result!.nearest))),
            ),
          ),
        ],
      ),
    );
  }
}
