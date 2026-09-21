import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:go_router/go_router.dart';
import '../../foundation/theme/app_colors.dart';
import '../../foundation/theme/premium_card.dart';
import '../../core/services/profile_service.dart';
import '../../core/services/mentor_service.dart';
import '../../core/services/presentation_service.dart';
import '../gamification/widgets/player_profile_card.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../core/services/tts_platform_service.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  Map<String, String>? userProfile;
  List<Mentor> mentors = [];
  bool isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadData();
  }

  Future<void> _loadData() async {
    final profile = await ProfileService.getProfile();
    final loadedMentors = await MentorService.getMentors();
    setState(() {
      userProfile = profile;
      mentors = loadedMentors;
      isLoading = false;
    });
  }

  Future<void> _launchWhatsApp() async {
    // Actual Shine Academy WhatsApp number (with country code)
    const String phoneNumber = '919408721039'; // wa.me requires no + symbol
    const String message = 'Hi Shine Academy! I found a bug / have a suggestion while using the app...';
    
    // Using wa.me works universally (opens App on Mobile, opens Web on Desktop)
    final Uri whatsappUrl = Uri.parse(
        "https://wa.me/$phoneNumber?text=${Uri.encodeComponent(message)}");

    try {
      if (await canLaunchUrl(whatsappUrl)) {
        await launchUrl(whatsappUrl, mode: LaunchMode.externalApplication);
      } else {
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(content: Text(TrilingualService.instance.getUIText("Could not open WhatsApp. Please check your internet connection."))),
          );
        }
      }
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text("Could not open WhatsApp: $e")),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    if (isLoading) {
      return const Scaffold(body: Center(child: CircularProgressIndicator()));
    }
    
    String greeting = "Learner";
    if (userProfile != null && userProfile!['role']!.isNotEmpty) {
      if (userProfile!['role'] == 'Student') {
        String stageName = userProfile!['stage'] ?? '';
        if (stageName.contains('Pre-School')) {
          greeting = "Pre-School Student";
        } else if (stageName.contains('Primary')) {
          greeting = "Primary Student";
        } else if (stageName.contains('Higher Secondary')) {
          greeting = "Higher Secondary Student";
        } else if (stageName.contains('Secondary')) {
          greeting = "Secondary Student";
        } else if (stageName.contains('Competitive')) {
          greeting = "Competitive Aspirant";
        } else {
          greeting = "Student";
        }
      } else {
        greeting = "${userProfile!['role']}";
      }
    }
    return Scaffold(
      backgroundColor: AppColors.background,
      body: SafeArea(
        top: false,
        bottom: true,
        child: CustomScrollView(
          slivers: [
            SliverAppBar(
            expandedHeight: 220.0,
            floating: false,
            pinned: true,
            backgroundColor: AppColors.primary,
            title: Text(TrilingualService.instance.getUIText('Shine Academy Naroda'),
              style: GoogleFonts.poppins(
                fontWeight: FontWeight.bold,
                color: Colors.white,
                fontSize: 18,
              ),
            ),
            centerTitle: true,
            actions: [
              ValueListenableBuilder<bool>(
                valueListenable: PresentationService.isPresentationMode,
                builder: (context, isPresentation, child) {
                  return IconButton(
                    icon: Icon(
                      isPresentation ? Icons.desktop_windows : Icons.smartphone,
                      color: isPresentation ? Colors.yellow : Colors.white,
                    ),
                    tooltip: isPresentation ? 'Presentation Mode: ON' : 'Presentation Mode: OFF',
                    onPressed: () {
                      PresentationService.toggle();
                      ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(
                          content: Text(isPresentation ? "Standard Mode Activated" : "Presentation Mode Activated (Large Text)"),
                          duration: const Duration(seconds: 2),
                        ),
                      );
                    },
                  );
                },
              ),
              IconButton(
                icon: Icon(Icons.settings_voice, color: Colors.white),
                tooltip: 'Open TTS Settings (Fix Voice)',
                onPressed: () async {
                  await TtsPlatformService.instance.openTtsSettings();
                },
              ),
              IconButton(
                icon: Icon(Icons.manage_accounts, color: Colors.white),
                tooltip: 'Change Profile/Class',
                onPressed: () {
                  context.push('/welcome');
                },
              ),
            ],
            flexibleSpace: FlexibleSpaceBar(
              background: Container(
                decoration: BoxDecoration(
                  gradient: AppColors.primaryGradient,
                ),
                child: Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const SizedBox(height: 20),
                      GestureDetector(
                        onLongPress: () {
                          // Admin Settings Hook
                          context.push('/admin_settings');
                        },
                        child: Container(
                          width: 110,
                          height: 110,
                          decoration: BoxDecoration(
                            color: Colors.white,
                            shape: BoxShape.circle,
                            boxShadow: [
                              BoxShadow(
                                color: Theme.of(context).colorScheme.onSurface.withOpacity(0.26),
                                blurRadius: 10,
                                offset: Offset(0, 4),
                              ),
                            ],
                          ),
                          child: Padding(
                            padding: const EdgeInsets.all(12.0),
                            child: Image.asset(
                              'assets/shineacademynarodalogo.jpg',
                              fit: BoxFit.contain,
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
          SliverToBoxAdapter(
            child: Padding(
              padding: const EdgeInsets.all(20.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    "Hello, $greeting!",
                    style: GoogleFonts.poppins(
                      fontSize: 28,
                      fontWeight: FontWeight.bold,
                      color: AppColors.textPrimary,
                    ),
                  ),
                  const SizedBox(height: 8),
                  Text(TrilingualService.instance.getUIText("What would you like to learn today?"),
                    style: GoogleFonts.inter(
                      fontSize: 16,
                      color: AppColors.textSecondary,
                    ),
                  ),
                  const SizedBox(height: 30),
                  Text(TrilingualService.instance.getUIText("Quick Access"),
                    style: GoogleFonts.poppins(
                      fontSize: 20,
                      fontWeight: FontWeight.w600,
                      color: AppColors.textPrimary,
                    ),
                  ),
                  const SizedBox(height: 16),
                  _buildDynamicQuickAccess(),
                  const SizedBox(height: 30),
                  Text(TrilingualService.instance.getUIText("Your Progress"),
                    style: GoogleFonts.poppins(
                      fontSize: 20,
                      fontWeight: FontWeight.w600,
                      color: AppColors.textPrimary,
                    ),
                  ),
                  const SizedBox(height: 16),
                  const PlayerProfileCard(),
                  const SizedBox(height: 40),
                  const SizedBox(height: 32),

                  // ── SPECIAL SKILLS SECTION ──────────────────────────────
                  // Visible to ALL students regardless of class/stage
                  Text(
                    TrilingualService.instance.getUIText("Special Skills"),
                    style: GoogleFonts.poppins(
                      fontSize: 20,
                      fontWeight: FontWeight.w600,
                      color: AppColors.textPrimary,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    TrilingualService.instance.getUIText("Calculate 10× faster with ancient wisdom!"),
                    style: GoogleFonts.inter(
                      fontSize: 13,
                      color: AppColors.textSecondary,
                    ),
                  ),
                  const SizedBox(height: 16),
                  IntrinsicHeight(
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: [
                      // Abacus Card
                      Expanded(
                        child: _SpecialSkillCard(
                          title: TrilingualService.instance.getUIText("Abacus"),
                          subtitle: TrilingualService.instance.getUIText("Mental Maths\nLevel 1"),
                          icon: Icons.grid_on,
                          gradientColors: const [Color(0xFF6C3483), Color(0xFF9B59B6)],
                          onTap: () => context.push('/curriculum/abacus_level1'),
                        ),
                      ),
                      const SizedBox(width: 12),
                      // Vedic Maths Card
                      Expanded(
                        child: _SpecialSkillCard(
                          title: TrilingualService.instance.getUIText("Vedic Maths"),
                          subtitle: TrilingualService.instance.getUIText("Ancient\nSutras"),
                          icon: Icons.psychology,
                          gradientColors: const [Color(0xFFE67E22), Color(0xFFF39C12)],
                          onTap: () => context.push('/curriculum/vedic_maths_level1'),
                        ),
                      ),
                      const SizedBox(width: 12),
                      // Tables Practice Card
                      Expanded(
                        child: _SpecialSkillCard(
                          title: TrilingualService.instance.getUIText("Tables Practice"),
                          subtitle: TrilingualService.instance.getUIText("Speed\nTrainer"),
                          icon: Icons.calculate,
                          gradientColors: const [Color(0xFF3B82F6), Color(0xFF60A5FA)],
                          onTap: () => context.push('/tools/mt_trainer'),
                        ),
                      ),
                    ],
                  ),
                  ),
                  const SizedBox(height: 32),

                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(TrilingualService.instance.getUIText("Meet Your Expert Mentors"),
                        style: GoogleFonts.poppins(
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                          color: Colors.indigo[800],
                        ),
                      ),
                      Row(
                        children: [
                          Text(TrilingualService.instance.getUIText("Swipe"), style: GoogleFonts.inter(fontSize: 12, color: Colors.grey[600])),
                          Icon(Icons.arrow_forward_ios, size: 12, color: Colors.grey[600]),
                        ],
                      ),
                    ],
                  ),
                  const SizedBox(height: 16),
                  SizedBox(
                    height: 220,
                    child: ListView.builder(
                      scrollDirection: Axis.horizontal,
                      itemCount: mentors.length,
                      itemBuilder: (context, index) {
                        return _buildMentorCard(mentors[index]);
                      },
                    ),
                  ),
                  const SizedBox(height: 40),
                ],
              ),
            ),
          ),
        ],
      ),
      ),
    );
  }


  Widget _buildMentorCard(Mentor mentor) {
    return Container(
      width: 140, // Reduced from 160 to allow the 3rd card to "peek" in
      margin: const EdgeInsets.only(right: 16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.05), blurRadius: 10, offset: Offset(0, 4)),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          ClipRRect(
            borderRadius: const BorderRadius.vertical(top: Radius.circular(16)),
            child: Container(
              height: 100,
              width: double.infinity,
              color: Colors.indigo[50],
              child: mentor.imagePath.startsWith('/')
                  ? Image.asset('assets/shineacademynarodalogo.jpg', fit: BoxFit.cover) // File loading would go here if we used dart:io, but for web/app asset fallback is fine
                  : Image.asset(mentor.imagePath, fit: BoxFit.cover,
                      errorBuilder: (c, o, s) => Icon(Icons.person, size: 50, color: Colors.indigo)),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(12.0),
            child: Column(
              children: [
                Text(
                  mentor.name,
                  textAlign: TextAlign.center,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: GoogleFonts.poppins(fontWeight: FontWeight.bold, fontSize: 14, color: AppColors.textPrimary),
                ),
                const SizedBox(height: 4),
                Text(
                  mentor.qualification,
                  textAlign: TextAlign.center,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: GoogleFonts.inter(fontSize: 12, color: Colors.indigo[600], fontWeight: FontWeight.w600),
                ),
                const SizedBox(height: 4),
                Text(
                  mentor.role,
                  textAlign: TextAlign.center,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: GoogleFonts.inter(fontSize: 10, color: AppColors.textSecondary),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildDynamicQuickAccess() {
    List<Widget> cards = [];

    Widget buildCard(String title, IconData icon, Color color, String route) {
      return PremiumCard(
        color: color.withValues(alpha: 0.1),
        onTap: () => context.push(route),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, color: color, size: 40),
            const SizedBox(height: 12),
            FittedBox(
              fit: BoxFit.scaleDown,
              child: Text(
                title,
                textAlign: TextAlign.center,
                style: GoogleFonts.inter(
                  fontWeight: FontWeight.bold,
                  color: AppColors.textPrimary,
                ),
              ),
            ),
          ],
        ),
      );
    }

    String stage = userProfile?['stage'] ?? '';
    Widget roleSpecificWidgets;

    if (stage.contains('Higher Secondary')) {
      final isCommerce = (userProfile?['class'] ?? '').toLowerCase().contains('commerce');
      
      Widget hsBanner;
      List<Widget> hsCards = [];
      
      if (isCommerce) {
        hsBanner = Card(
          elevation: 4,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
          child: InkWell(
            borderRadius: BorderRadius.circular(16),
            onTap: () => context.push('/curriculum/gseb_class12_commerce'),
            child: Container(
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(16),
                gradient: const LinearGradient(
                  colors: [Color(0xFF3F51B5), Color(0xFF5C6BC0)],
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
              ),
              padding: const EdgeInsets.all(20),
              child: Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(color: Colors.white.withValues(alpha: 0.2), shape: BoxShape.circle),
                    child: Icon(Icons.school, color: Colors.white, size: 36),
                  ),
                  const SizedBox(width: 20),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(TrilingualService.instance.getUIText("Class 12 Commerce"), style: GoogleFonts.poppins(fontWeight: FontWeight.bold, fontSize: 20, color: Colors.white)),
                        const SizedBox(height: 4),
                        Text(TrilingualService.instance.getUIText("Complete Course (GSEB)"), style: GoogleFonts.inter(color: Colors.white.withValues(alpha: 0.9), fontSize: 14)),
                      ],
                    ),
                  ),
                  Icon(Icons.arrow_forward_ios, color: Colors.white),
                ],
              ),
            ),
          ),
        );
        
        hsCards = [
          SizedBox(
            width: 130,
            child: buildCard("Accounts\nSimulators", Icons.account_balance, AppColors.commerceColor, '/learning/commerce'),
          ),
          const SizedBox(width: 16),
          SizedBox(
            width: 130,
            child: buildCard("Statistics\nSimulators", Icons.bar_chart, AppColors.commerceColor, '/learning/stats'),
          ),
          const SizedBox(width: 16),
          SizedBox(
            width: 130,
            child: buildCard("English\nSimulations", Icons.language, Colors.deepPurple, '/english_simulation'),
          ),
        ];
      } else {
        // Science (NEET/JEE)
        hsBanner = Card(
          elevation: 4,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
          child: InkWell(
            borderRadius: BorderRadius.circular(16),
            onTap: () => context.push('/learning/physics'),
            child: Container(
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(16),
                gradient: const LinearGradient(
                  colors: [Color(0xFF009688), Color(0xFF4DB6AC)],
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
              ),
              padding: const EdgeInsets.all(20),
              child: Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(color: Colors.white.withValues(alpha: 0.2), shape: BoxShape.circle),
                    child: Icon(Icons.science, color: Colors.white, size: 36),
                  ),
                  const SizedBox(width: 20),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(TrilingualService.instance.getUIText("Class 11-12 Science"), style: GoogleFonts.poppins(fontWeight: FontWeight.bold, fontSize: 20, color: Colors.white)),
                        const SizedBox(height: 4),
                        Text(TrilingualService.instance.getUIText("NEET & JEE Foundation"), style: GoogleFonts.inter(color: Colors.white.withValues(alpha: 0.9), fontSize: 14)),
                      ],
                    ),
                  ),
                  Icon(Icons.arrow_forward_ios, color: Colors.white),
                ],
              ),
            ),
          ),
        );
        
        hsCards = [
          SizedBox(
            width: 130,
            child: buildCard("Physics\nSandbox", Icons.science, AppColors.physicsColor, '/learning/physics'),
          ),
          const SizedBox(width: 16),
          SizedBox(
            width: 130,
            child: buildCard("English\nSimulations", Icons.language, Colors.deepPurple, '/english_simulation'),
          ),
          const SizedBox(width: 16),
          SizedBox(
            width: 130,
            child: buildCard("Question\nPapers", Icons.auto_stories, Colors.blue, '/assessment'),
          ),
        ];
      }

      roleSpecificWidgets = Column(
        children: [
          hsBanner,
          const SizedBox(height: 16),
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            child: IntrinsicHeight(
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: hsCards,
              ),
            ),
          ),
        ],
      );
    } else if (stage.contains('Pre-School')) {
      cards.add(buildCard("Curriculum\nBrowser", Icons.explore, AppColors.primary, '/learning'));
      cards.add(const SizedBox(width: 16));
      cards.add(buildCard("Picture\nDictionary", Icons.menu_book, Colors.orange, '/dictionary'));
      roleSpecificWidgets = SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        child: IntrinsicHeight(
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: cards.map((c) => c is SizedBox ? c : SizedBox(width: 130, child: c)).toList(),
          ),
        ),
      );
    } else if (stage.contains('Primary')) {
      cards.add(buildCard("Maths\n(Class 3-6)", Icons.calculate, AppColors.mathColor, '/learning/maths3to6'));
      cards.add(const SizedBox(width: 16));
      cards.add(buildCard("Spoken\nEnglish", Icons.record_voice_over, AppColors.englishColor, '/learning/eng3to6'));

      roleSpecificWidgets = SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        child: IntrinsicHeight(
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: cards.map((c) => c is SizedBox ? c : SizedBox(width: 130, child: c)).toList(),
          ),
        ),
      );
    } else {
      // Default / Secondary (Class 9-10)
      cards.add(buildCard("Question\nPapers", Icons.auto_stories, Colors.blue, '/assessment'));
      cards.add(const SizedBox(width: 16));
      cards.add(buildCard("Science\nSimulations", Icons.science, AppColors.scienceColor, '/learning/sci_sim'));
      cards.add(const SizedBox(width: 16));
      cards.add(buildCard("NCERT Sci\n(Full Demo)", Icons.auto_stories, AppColors.englishColor, '/chapter-demo'));
      cards.add(const SizedBox(width: 16));
      cards.add(buildCard("Physics\nSandbox", Icons.science, AppColors.physicsColor, '/learning/physics'));
      roleSpecificWidgets = SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        child: IntrinsicHeight(
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: cards.map((c) => c is SizedBox ? c : SizedBox(width: 130, child: c)).toList(),
          ),
        ),
      );
    }

    return Column(
      children: [
        // UNIVERSAL PREMIUM SPOKEN ENGLISH BANNER
        Card(
          elevation: 6,
          shadowColor: Colors.pink.withValues(alpha: 0.3),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
          child: InkWell(
            borderRadius: BorderRadius.circular(16),
            onTap: () => context.push('/curriculum/govindsir_english'),
            child: Container(
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(16),
                gradient: const LinearGradient(
                  colors: [Color(0xFFE91E63), Color(0xFFFF8A65)], // Vibrant pink-orange premium gradient
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
              ),
              padding: const EdgeInsets.all(20),
              child: Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(color: Colors.white.withValues(alpha: 0.2), shape: BoxShape.circle),
                    child: Icon(Icons.record_voice_over, color: Colors.white, size: 36),
                  ),
                  const SizedBox(width: 20),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(TrilingualService.instance.getUIText("Learn English"), style: GoogleFonts.poppins(fontWeight: FontWeight.bold, fontSize: 22, color: Colors.white)),
                        const SizedBox(height: 4),
                        Text(TrilingualService.instance.getUIText("by Govind Sir (Trilingual)"), style: GoogleFonts.inter(color: Colors.white.withValues(alpha: 0.9), fontSize: 14)),
                      ],
                    ),
                  ),
                  Icon(Icons.play_circle_fill, color: Colors.white, size: 36),
                ],
              ),
            ),
          ),
        ),
        const SizedBox(height: 16),
        roleSpecificWidgets,
      ],
    );
  }
}

// ── Premium Special Skill Card for Abacus / Vedic Maths ────────────────────
class _SpecialSkillCard extends StatelessWidget {
  final String title;
  final String subtitle;
  final IconData icon;
  final List<Color> gradientColors;
  final VoidCallback onTap;

  const _SpecialSkillCard({
    required this.title,
    required this.subtitle,
    required this.icon,
    required this.gradientColors,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 6,
      shadowColor: gradientColors.first.withValues(alpha: 0.4),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      child: InkWell(
        borderRadius: BorderRadius.circular(16),
        onTap: onTap,
        child: Container(
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(16),
            gradient: LinearGradient(
              colors: gradientColors,
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
          ),
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Container(
                padding: const EdgeInsets.all(8),
                decoration: BoxDecoration(
                  color: Colors.white.withValues(alpha: 0.2),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Icon(icon, color: Colors.white, size: 24),
              ),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    title,
                    style: GoogleFonts.poppins(
                      fontWeight: FontWeight.bold,
                      fontSize: 15,
                      color: Colors.white,
                    ),
                  ),
                  Text(
                    subtitle,
                    style: GoogleFonts.inter(
                      fontSize: 11,
                      color: Colors.white.withValues(alpha: 0.85),
                      height: 1.3,
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}