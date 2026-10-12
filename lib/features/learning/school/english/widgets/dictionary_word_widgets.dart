import 'package:flutter/material.dart';


import '../services/speech_service.dart';
import '../theme/app_theme.dart';
import '../../../../../core/services/universal_dictionary_service.dart';
import 'admin_edit_button.dart';
class DictionaryPhotoHelper {
  static final Map<String, String> _localAssets = {
    'ant': 'assets/images/ant.jpg',
    'bear': 'assets/images/bear.jpg',
    'bird': 'assets/images/bird.jpg',
    'butterfly': 'assets/images/butterfly.jpg',
    'cat': 'assets/images/cat.jpg',
    'cow': 'assets/images/cow.jpg',
    'dog': 'assets/images/dog.jpg',
    'duck': 'assets/images/duck.jpg',
    'elephant': 'assets/images/elephant.jpg',
    'glacier': 'assets/images/glacier.jpg',
    'goat': 'assets/images/goat.jpg',
    'hen': 'assets/images/hen.jpg',
    'horse': 'assets/images/horse.jpg',
    'lion': 'assets/images/lion.jpg',
    'monkey': 'assets/images/monkey.jpg',
    'mouse': 'assets/images/mouse.jpg',
    'parrot': 'assets/images/parrot.jpg',
    'rabbit': 'assets/images/rabbit.jpg',
    'tiger': 'assets/images/tiger.jpg',
  };

  static final Map<String, String> _curatedWebPhotos = {
    'bear': 'https://images.unsplash.com/photo-1530595467537-0b5996c41f2d?w=500&q=80',
    'bird': 'https://images.unsplash.com/photo-1444464666168-49d633b86797?w=500&q=80',
    'dog': 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?w=500&q=80',
    'cat': 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=500&q=80',
    'horse': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500&q=80',
    'lion': 'https://images.unsplash.com/photo-1534188753412-3e26d0d618d6?w=500&q=80',
    'duck': 'https://images.unsplash.com/photo-1555854877-bab0e564b8d5?w=500&q=80',
    'frog': 'https://images.unsplash.com/photo-1579202673506-ca3ce28943ef?w=500&q=80',
    'ladybird': 'https://images.unsplash.com/photo-1547407139-3c921a66005c?w=500&q=80',
    'ladybug': 'https://images.unsplash.com/photo-1547407139-3c921a66005c?w=500&q=80',
    'touch me not': 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&q=80',
    'touch-me-not': 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&q=80',
    'mimosa': 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&q=80',
    'parrot': 'https://images.unsplash.com/photo-1552728089-57bdde30beb3?w=500&q=80',
    'peacock': 'https://images.unsplash.com/photo-1516205651411-aef33a44f7c2?w=500&q=80',
    'apple': 'https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=500&q=80',
    'mango': 'https://images.unsplash.com/photo-1553279768-865429fa0078?w=500&q=80',
    'tree': 'https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=500&q=80',
    'mountain': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500&q=80',
    'train': 'https://images.unsplash.com/photo-1474487548417-781cb71495f3?w=500&q=80',
    'airplane': 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=500&q=80',
    'advocate': 'https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=500&q=80',
    'implication': 'https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=500&q=80',
    'analogy': 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=500&q=80',
    'consensus': 'https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=500&q=80',
    'mitigate': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=500&q=80',
    'holistic': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=500&q=80',
  };

  static String? getPhoto(String term) {
    final clean = term.trim().toLowerCase();
    // 1. Strict exact match in local assets
    if (_localAssets.containsKey(clean)) return _localAssets[clean];

    // 2. Strict exact match in curated photos (never use substring contains which matches 'advocate' to 'cat')
    if (_curatedWebPhotos.containsKey(clean)) return _curatedWebPhotos[clean];

    return null;
  }
}

/// Shared word-card tile used by both the per-topic dictionary browser and
/// the global cross-grade search screen, so a word looks the same wherever
/// it's found.
class DictionaryWordCard extends StatelessWidget {
  final Map<String, dynamic> word;
  final String? gradeLabel;

  const DictionaryWordCard({super.key, required this.word, this.gradeLabel});

  @override
  Widget build(BuildContext context) {
    final String termEn = ((word['term'] as Map?)?['english'] ?? '').toString();
    final String? photoSource = (word['media'] != null && word['media']['imagePath'] != null && word['media']['imagePath'].toString().isNotEmpty)
        ? word['media']['imagePath'].toString()
        : DictionaryPhotoHelper.getPhoto(termEn);

    Widget imageThumbnail;
    if (photoSource != null && photoSource.isNotEmpty) {
      if (photoSource.startsWith('assets/')) {
        imageThumbnail = ClipRRect(
          borderRadius: BorderRadius.circular(8),
          child: Image.asset(photoSource, width: 50, height: 50, fit: BoxFit.cover),
        );
      } else if (photoSource.startsWith('http')) {
        imageThumbnail = ClipRRect(
          borderRadius: BorderRadius.circular(8),
          child: Image.network(
            photoSource,
            width: 50,
            height: 50,
            fit: BoxFit.cover,
            errorBuilder: (ctx, err, st) => _fallbackEmoji(),
          ),
        );
      } else {
        imageThumbnail = _fallbackEmoji();
      }
    } else {
      imageThumbnail = _fallbackEmoji();
    }

    return InkWell(
      borderRadius: BorderRadius.circular(12),
      onTap: () => showModalBottomSheet(
        context: context,
        showDragHandle: true,
        builder: (_) => DictionaryWordDetailSheet(word: word),
      ),
      child: Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: AppColors.paperRaised,
          borderRadius: BorderRadius.circular(12),
          border: Border.all(color: AppColors.rule),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisSize: MainAxisSize.min,
          children: [
            Row(
              children: [
                imageThumbnail,
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text(termEn,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(fontWeight: FontWeight.w700, fontSize: 15, color: AppColors.ink)),
                      Text(((word['term'] as Map?)?['hindi'] ?? (word['term'] as Map?)?['hi'] ?? ''),
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(color: AppColors.tealDeep, fontSize: 13)),
                    ],
                  ),
                ),
                if (gradeLabel != null)
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 7, vertical: 3),
                    decoration: BoxDecoration(
                      color: AppColors.tealTint,
                      borderRadius: BorderRadius.circular(6),
                    ),
                    child: Text(gradeLabel!, style: TextStyle(fontSize: 10, color: AppColors.tealDeep, fontWeight: FontWeight.w600)),
                  ),
              ],
            ),
            const SizedBox(height: 8),
            Text(
              word['definition'] != null && word['definition']['simple'] != null 
                  ? (word['definition']['simple'] is Map ? word['definition']['simple']['en'] ?? '' : word['definition']['simple']) 
                  : '',
              maxLines: 3,
              overflow: TextOverflow.ellipsis,
              style: TextStyle(fontSize: 12.5, color: AppColors.inkSoft),
            ),
          ],
        ),
      ),
    );
  }

  Widget _fallbackEmoji() {
    return Container(
      width: 50,
      height: 50,
      alignment: Alignment.center,
      decoration: BoxDecoration(
        color: AppColors.saffronTint,
        borderRadius: BorderRadius.circular(8),
      ),
      child: (word['media'] != null && word['media']['emoji'] != null)
          ? Text(word['media']['emoji'], style: const TextStyle(fontSize: 26))
          : Icon(Icons.menu_book_outlined, color: AppColors.saffronDeep, size: 24),
    );
  }
}

class DictionaryWordDetailSheet extends StatelessWidget {
  final Map<String, dynamic> word;

  const DictionaryWordDetailSheet({super.key, required this.word});

  @override
  Widget build(BuildContext context) {
    final String termEn = ((word['term'] as Map?)?['english'] ?? '').toString();
    final String? photoSource = (word['media'] != null && word['media']['imagePath'] != null && word['media']['imagePath'].toString().isNotEmpty)
        ? word['media']['imagePath'].toString()
        : DictionaryPhotoHelper.getPhoto(termEn);

    Widget heroVisual;
    if (photoSource != null && photoSource.isNotEmpty) {
      if (photoSource.startsWith('assets/')) {
        heroVisual = ClipRRect(
          borderRadius: BorderRadius.circular(14),
          child: Image.asset(photoSource, width: double.infinity, height: 160, fit: BoxFit.cover),
        );
      } else if (photoSource.startsWith('http')) {
        heroVisual = ClipRRect(
          borderRadius: BorderRadius.circular(14),
          child: Image.network(
            photoSource,
            width: double.infinity,
            height: 160,
            fit: BoxFit.cover,
            errorBuilder: (ctx, err, st) => _fallbackHeroEmoji(),
          ),
        );
      } else {
        heroVisual = _fallbackHeroEmoji();
      }
    } else {
      heroVisual = _fallbackHeroEmoji();
    }

    return SelectionArea(
      child: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.fromLTRB(24, 8, 24, 32),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: [
              Center(child: heroVisual),
              const SizedBox(height: 16),
              Row(
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  Expanded(
                    child: Text(termEn,
                        style: TextStyle(fontSize: 24, fontWeight: FontWeight.w800, color: AppColors.ink)),
                  ),
                  const SizedBox(width: 8),
                  Text(word['part_of_speech'] ?? 'noun', style: TextStyle(fontSize: 12, color: AppColors.inkFaint)),
                  const SizedBox(width: 8),
                  FutureBuilder<String?>(
                    future: UniversalDictionaryService.instance.getSourceFileForTerm(word['id']?.toString() ?? ''),
                    builder: (context, snapshot) {
                      if (snapshot.hasData && snapshot.data != null) {
                        return AdminEditButton(
                          jsonPath: snapshot.data!,
                          data: const {},
                        );
                      }
                      return const SizedBox.shrink();
                    },
                  ),
                  IconButton(
                    icon: Icon(Icons.volume_up, color: AppColors.tealDeep),
                    tooltip: 'Hear pronunciation',
                    onPressed: () => SpeechService.instance.speak(termEn),
                  ),
                ],
              ),
              const SizedBox(height: 4),
              Text(
                '${(word['term'] as Map?)?['hindi'] ?? (word['term'] as Map?)?['hi'] ?? ''}  ·  ${(word['term'] as Map?)?['gujarati'] ?? (word['term'] as Map?)?['gu'] ?? ''}',
                style: TextStyle(fontSize: 16, color: AppColors.tealDeep, fontWeight: FontWeight.w600),
              ),
          const SizedBox(height: 12),
          Text(word['definition'] != null && word['definition']['simple'] != null 
                    ? (word['definition']['simple'] is Map ? word['definition']['simple']['en'] ?? '' : word['definition']['simple']) 
                    : '', style: TextStyle(fontSize: 15, color: AppColors.inkSoft)),
          const SizedBox(height: 10),
          
          if (word['examples'] != null && (word['examples'] as List).isNotEmpty)
            ...((word['examples'] as List).map((ex) {
              String exEn = ex is Map ? (ex['en'] ?? '') : ex.toString();
              String exHi = ex is Map ? (ex['hi'] ?? '') : '';
              String exGu = ex is Map ? (ex['gu'] ?? '') : '';
              
              return Container(
                margin: const EdgeInsets.only(bottom: 8),
                width: double.infinity,
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: AppColors.paperRaised,
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text('"$exEn"', style: TextStyle(fontStyle: FontStyle.italic, color: AppColors.inkSoft, fontSize: 14)),
                    if (exHi.isNotEmpty)
                      Padding(
                        padding: const EdgeInsets.only(top: 4),
                        child: Text(exHi, style: TextStyle(color: AppColors.inkFaint, fontSize: 13)),
                      ),
                    if (exGu.isNotEmpty)
                      Padding(
                        padding: const EdgeInsets.only(top: 2),
                        child: Text(exGu, style: TextStyle(color: AppColors.inkFaint, fontSize: 13)),
                      ),
                  ],
                ),
              );
            }).toList()),
        ],
      ),
    )));
  }

  Widget _fallbackHeroEmoji() {
    return Container(
      width: 100,
      height: 100,
      alignment: Alignment.center,
      decoration: BoxDecoration(
        color: AppColors.saffronTint,
        borderRadius: BorderRadius.circular(16),
      ),
      child: (word['media'] != null && word['media']['emoji'] != null)
          ? Text(word['media']['emoji'], style: const TextStyle(fontSize: 50))
          : Icon(Icons.menu_book_outlined, color: AppColors.saffronDeep, size: 48),
    );
  }
}
