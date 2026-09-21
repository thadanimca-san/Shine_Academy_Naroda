import 'package:flutter/material.dart';
import 'dart:math';
import '../../learning/school/english/services/speech_service.dart';
import '../../../foundation/theme/app_colors.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../community/widgets/review_submission_dialog.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class MastHaiDialog extends StatefulWidget {
  const MastHaiDialog({super.key});

  @override
  State<MastHaiDialog> createState() => _MastHaiDialogState();
}

class _MastHaiDialogState extends State<MastHaiDialog> with TickerProviderStateMixin {
  late TabController _tabController;

  // TAB 1: MOTIVATION
  bool _isPlaying = false;
  late AnimationController _pulseController;
  
  final List<Map<String, String>> _variants = [
    {
      "title": "Marathi",
      "nativeText": "हे तर मस्त आहे।\nशाइन अकैडमी नरोडामधून शिकावेच लागेल!",
      "hindiText": "यह तो मस्त है। शाइन अकैडमी नरोडा से सीखना ही पड़ेगा!"
    },
    {
      "title": "Gujarati",
      "nativeText": "आ तो मस्त छे।\nशाइन अकैडमी नरोडा मांथी शीखवुं ज पड़शे!",
      "hindiText": "यह तो मस्त है। शाइन अकैडमी नरोडा से सीखना ही पड़ेगा!"
    },
    {
      "title": "Punjabi",
      "nativeText": "एह तां मस्त है।\nशाइन अकैडमी नरोडा तों सिक्खणा ही पवेगा!",
      "hindiText": "यह तो मस्त है। शाइन अकैडमी नरोडा से सीखना ही पड़ेगा!"
    },
    {
      "title": "Bengali",
      "nativeText": "एटा तो दारुन।\nशाइन अकैडमी नरोडा थेके शिखतेइ होबे!",
      "hindiText": "यह तो मस्त है। शाइन अकैडमी नरोडा से सीखना ही पड़ेगा!"
    },
    {
      "title": "Hindi",
      "nativeText": "यह तो एकदम मस्त है।\nशाइन अकैडमी नरोडा से सीखना ही पड़ेगा!",
      "hindiText": "यह तो एकदम मस्त है। शाइन अकैडमी नरोडा से सीखना ही पड़ेगा!"
    },
    {
      "title": "Haryanvi",
      "nativeText": "यो तो कसूता है!\nशाइन अकैडमी नरोडा तै सीखना ही पड़ैगा!",
      "hindiText": "यह तो एकदम मस्त है। शाइन अकैडमी नरोडा से सीखना ही पड़ेगा!"
    },
    {
      "title": "Marwadi",
      "nativeText": "आ तो घणी चोखी बात है!\nशाइन अकैडमी नरोडा सूं सीखणो ही पड़सी!",
      "hindiText": "यह तो एकदम मस्त है। शाइन अकैडमी नरोडा से सीखना ही पड़ेगा!"
    },
    {
      "title": "Sindhi",
      "nativeText": "ही त ज़बरदस्त आहे!\nशाइन अकैडमी नरोडा मां सिखणो ई पोंदो!",
      "hindiText": "यह तो एकदम मस्त है। शाइन अकैडमी नरोडा से सीखना ही पड़ेगा!"
    },
    {
      "title": "Bhojpuri",
      "nativeText": "ई त गज़बे बा!\nशाइन अकैडमी नरोडा से सीखे के ही पड़ी!",
      "hindiText": "यह तो एकदम मस्त है। शाइन अकैडमी नरोडा से सीखना ही पड़ेगा!"
    }
  ];
  
  late Map<String, String> _selectedVariant;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 3, vsync: this);

    _selectedVariant = _variants[Random().nextInt(_variants.length)];
    
    _pulseController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 800),
    )..repeat(reverse: true);
  }

  @override
  void dispose() {
    _tabController.dispose();
    _pulseController.dispose();
    if (_isPlaying) {
      SpeechService.instance.stop();
    }
    super.dispose();
  }

  Future<void> _playCelebrityVoice() async {
    setState(() {
      _isPlaying = true;
    });

    final random = Random();
    double pitch = 0.5 + random.nextDouble() * 1.5;
    double rate = 0.4 + random.nextDouble() * 0.4;

    await SpeechService.instance.speakWithSettings(
      text: _selectedVariant['hindiText']!,
      pitch: pitch,
      speechRate: rate,
      language: "en-IN"
    );

    if (mounted) {
      setState(() => _isPlaying = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Dialog(
      backgroundColor: Colors.transparent,
      elevation: 0,
      child: Container(
        height: 550, // Fixed height for tabs
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(24),
          boxShadow: [
            BoxShadow(
              color: AppColors.primary.withValues(alpha: 0.5),
              blurRadius: 30,
              spreadRadius: 5,
            ),
          ],
        ),
        child: Column(
          children: [
            // Tabs Header
            Container(
              decoration: BoxDecoration(
                color: Colors.grey.shade100,
                borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
              ),
              child: TabBar(
                controller: _tabController,
                labelColor: AppColors.primary,
                unselectedLabelColor: Colors.grey,
                indicatorColor: AppColors.primary,
                indicatorWeight: 4,
                tabs: const [
                  Tab(icon: Icon(Icons.star), text: "Motivation"),
                  Tab(icon: Icon(Icons.music_note), text: "Music"),
                  Tab(icon: Icon(Icons.menu_book), text: "Literature"),
                ],
              ),
            ),
            
            // Tab Views
            Expanded(
              child: TabBarView(
                controller: _tabController,
                children: [
                  _buildLegendsTab(),
                  _buildMusicTab(),
                  _buildLiteratureTab(),
                ],
              ),
            ),
            
            const Divider(height: 1),
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 8),
              child: TextButton(
                onPressed: () {
                  if (_isPlaying) SpeechService.instance.stop();
                  Navigator.of(context).pop();
                },
                style: TextButton.styleFrom(foregroundColor: Colors.grey.shade600),
                child: Text(TrilingualService.instance.getUIText("Continue Practicing"), style: TextStyle(fontWeight: FontWeight.bold)),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildLegendsTab() {
    return Padding(
      padding: const EdgeInsets.all(16),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Stack(
            alignment: Alignment.center,
            children: [
              ScaleTransition(
                scale: Tween<double>(begin: 0.8, end: 1.2).animate(
                  CurvedAnimation(parent: _pulseController, curve: Curves.easeInOut),
                ),
                child: Container(
                  width: 80,
                  height: 80,
                  decoration: BoxDecoration(
                    color: Colors.amber.withValues(alpha: 0.3),
                    shape: BoxShape.circle,
                  ),
                ),
              ),
              Text(TrilingualService.instance.getUIText('🔥'), style: TextStyle(fontSize: 48)),
            ],
          ),
          const SizedBox(height: 12),
          Text(
            _selectedVariant['nativeText']!,
            textAlign: TextAlign.center,
            style: TextStyle( // Use default font which supports regional scripts better than Poppins
              fontSize: 24,
              fontWeight: FontWeight.bold,
              color: AppColors.primary,
              height: 1.3,
            ),
          ),
          const SizedBox(height: 8),
          Text(
            _selectedVariant['hindiText']!,
            textAlign: TextAlign.center,
            style: GoogleFonts.notoSans(
              fontSize: 14,
              fontWeight: FontWeight.w500,
              color: Colors.grey.shade700,
            ),
          ),
          const SizedBox(height: 4),
          Text(
            "Language: ${_selectedVariant['title']!}",
            textAlign: TextAlign.center,
            style: GoogleFonts.notoSans(
              fontSize: 12,
              fontStyle: FontStyle.italic,
              color: Colors.grey.shade500,
            ),
          ),
          const SizedBox(height: 8),
          Text(TrilingualService.instance.getUIText("Incredible! You got 8 right in a row!"),
            style: TextStyle(fontSize: 16, color: Colors.grey.shade600, fontWeight: FontWeight.w600),
          ),
          const Spacer(),
          if (!_isPlaying)
            ElevatedButton.icon(
              onPressed: _playCelebrityVoice,
              icon: Icon(Icons.headphones),
              label: Flexible(child: Text(TrilingualService.instance.getUIText("Listen to Audio"), textAlign: TextAlign.center)),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.orange,
                foregroundColor: Colors.white,
                padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(30)),
              ),
            )
          else
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const SizedBox(width: 20, height: 20, child: CircularProgressIndicator(strokeWidth: 3, color: AppColors.primary)),
                const SizedBox(width: 12),
                Flexible(child: Text(TrilingualService.instance.getUIText("Playing audio..."), style: TextStyle(fontWeight: FontWeight.bold, color: AppColors.primary))),
              ],
            ),
        ],
      ),
    );
  }

  Future<void> _playSong() async {
    setState(() {
      _isPlaying = true;
    });

    await SpeechService.instance.playAudio('assets/audio/ruk_jana_short.mp3');

    if (mounted) {
      setState(() => _isPlaying = false);
    }
  }

  Widget _buildMusicTab() {
    return Padding(
      padding: const EdgeInsets.all(24),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(Icons.music_note, size: 64, color: Colors.purple),
          const SizedBox(height: 24),
          Text(TrilingualService.instance.getUIText("Ruk jana nahi tu kahi haar ke,\nKaanton pe chalke milenge saaye bahaar ke..."),
            textAlign: TextAlign.center,
            style: GoogleFonts.poppins(fontSize: 18, fontStyle: FontStyle.italic, fontWeight: FontWeight.bold, color: Colors.purple.shade700),
          ),
          const SizedBox(height: 16),
          Text(TrilingualService.instance.getUIText("- Classic Indian Motivation"), style: TextStyle(color: Colors.grey.shade600)),
          const Spacer(),
          if (!_isPlaying)
            ElevatedButton.icon(
              onPressed: _playSong,
              icon: Icon(Icons.play_arrow),
              label: Text(TrilingualService.instance.getUIText("Play Song Snippet")),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.purple,
                foregroundColor: Colors.white,
                padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(30)),
              ),
            )
          else
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const SizedBox(width: 20, height: 20, child: CircularProgressIndicator(strokeWidth: 3, color: Colors.purple)),
                const SizedBox(width: 12),
                Flexible(child: Text(TrilingualService.instance.getUIText("Singing..."), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.purple))),
              ],
            ),
        ],
      ),
    );
  }

  Widget _buildLiteratureTab() {
    return Padding(
      padding: const EdgeInsets.all(24),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(Icons.menu_book, size: 64, color: Colors.teal),
          const SizedBox(height: 24),
          Text(TrilingualService.instance.getUIText("कोशिश करने वालों की कभी हार नहीं होती,\nलहरों से डरकर नौका पार नहीं होती।"),
            textAlign: TextAlign.center,
            style: GoogleFonts.poppins(fontSize: 18, fontStyle: FontStyle.italic, fontWeight: FontWeight.bold, color: Colors.teal.shade700),
          ),
          const SizedBox(height: 16),
          Text(TrilingualService.instance.getUIText("- Harivansh Rai Bachchan"), style: TextStyle(color: Colors.grey.shade600)),
          const Spacer(),
          ElevatedButton.icon(
            onPressed: () {
              // Open the Moderated Review Submission Form
              showDialog(
                context: context,
                builder: (context) => const ReviewSubmissionDialog(),
              );
            },
            icon: Icon(Icons.edit),
            label: Text(TrilingualService.instance.getUIText("Submit Review / Story")),
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.teal,
              foregroundColor: Colors.white,
              padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(30)),
            ),
          )
        ],
      ),
    );
  }
}
