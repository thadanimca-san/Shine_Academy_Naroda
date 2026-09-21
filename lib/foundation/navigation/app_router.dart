import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import '../../features/assessment/assessment_home.dart';
import '../../features/community/community_home.dart';
import '../../features/dashboard/home_screen.dart';
import '../../features/dashboard/admin_settings_screen.dart';
import '../../features/dashboard/content_editor_screen.dart';
import '../../features/dashboard/paper_digitization_studio.dart';

import '../../features/welcome/language_selection_screen.dart';
import '../../features/learning/learning_home.dart';
import '../../features/splash/splash_screen.dart';
import '../../features/welcome/onboarding_screen.dart';
import '../../features/chapter/chapter_detail_screen.dart';
import '../../features/curriculum/subject_list_screen.dart';
import '../../features/curriculum/chapter_list_screen.dart';
import '../../features/learning/learning_engine/learning_engine_screen.dart';
import '../../features/learning/pedagogy_engine_screen.dart';
import '../../features/assessment/exam_engine_screen.dart';
import '../../features/assessment/question_bank_screen.dart';
import '../../features/assessment/question_paper_view_screen.dart';
import '../../features/activation/activation_screen.dart';
import '../../features/learning/tools/mt_trainer_screen.dart';

import '../../features/developer/eduos_doctor_screen.dart';
import '../../core/services/navigation_memory_service.dart';
// Import our learning apps (entry points)
import '../../features/learning/school/maths3to6/maths_main.dart' as maths3to6;
import '../../features/learning/school/english/english_main.dart' as english_sim;
import '../../features/learning/school/sci_simulation/sci_main.dart' as sci_sim;
import '../../features/learning/higher_secondary/commerce_accounts/commerce_main.dart' as commerce;
import '../../features/learning/higher_secondary/physics_sandbox/physics_main.dart' as physics;

// New 4 apps
import '../../features/learning/school/maths_simulation/maths_sim_main.dart' as maths_sim;
import '../../features/learning/higher_secondary/statistics/stats_main.dart' as stats;
import '../../features/learning/higher_secondary/english_simulation/eng_sim_main.dart' as eng_sim_hs;
import "../../features/english_simulation_11to12/english_simulation_dashboard.dart";
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
// import '../../features/learning/school/social_science_simulation/social_science_main.dart' as sst_sim;
// import '../../features/learning/school/sanskrit_simulation/sanskrit_main.dart' as sanskrit_sim;
// import '../../features/learning/school/gujarati_simulation/gujarati_main.dart' as gujarati_sim;
// import '../../features/learning/school/computer_simulation/computer_main.dart' as computer_sim;
// import '../../features/learning/school/hindi_simulation/hindi_main.dart' as hindi_sim;

final GlobalKey<NavigatorState> rootNavigatorKey = GlobalKey<NavigatorState>();
final GlobalKey<NavigatorState> _shellNavigatorKey = GlobalKey<NavigatorState>();

class ExitOverlay extends StatelessWidget {
  final Widget child;
  const ExitOverlay({super.key, required this.child});

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        child,
        Positioned(
          top: MediaQuery.of(context).padding.top + 16,
          left: 16,
          child: Material(
            color: Colors.transparent,
            child: InkWell(
              borderRadius: BorderRadius.circular(20),
              onTap: () {
                context.go('/learning');
              },
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                decoration: BoxDecoration(
                  color: Theme.of(context).colorScheme.onSurfaceVariant,
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(color: Colors.white24),
                ),
                child:  Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(Icons.arrow_back_ios_new, color: Colors.white, size: 14),
                    SizedBox(width: 8),
                    Text(TrilingualService.instance.getUIText('Back to Hub'),
                      style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
      ],
    );
  }
}

final router = GoRouter(
  navigatorKey: rootNavigatorKey,
  initialLocation: '/',
  routes: [
    GoRoute(
      path: '/',
      builder: (context, state) => const SplashScreen(),
    ),
    GoRoute(
      path: '/language_selection',
      pageBuilder: (context, state) => const MaterialPage(
        child: LanguageSelectionScreen(),
      ),
    ),
    GoRoute(
      path: '/welcome',
      builder: (context, state) => const OnboardingScreen(),
    ),
    GoRoute(
      path: '/activate',
      builder: (context, state) => const ActivationScreen(),
    ),
    GoRoute(
      path: '/dev/doctor',
      builder: (context, state) => const EduOSDoctorScreen(),
    ),
    GoRoute(
      path: '/english_simulation',
      builder: (context, state) => const HomeDashboardView(),
    ),
    ShellRoute(
      navigatorKey: _shellNavigatorKey,
      builder: (context, state, child) {
        return Scaffold(
          body: child,
          bottomNavigationBar: _buildBottomNav(context, state.uri.path),
        );
      },
      routes: [
        GoRoute(
          path: '/home',
          builder: (context, state) => const HomeScreen(),
        ),
        GoRoute(
          path: '/tools/mt_trainer',
          builder: (context, state) => const MultiplicationTableView(),
        ),
        GoRoute(
          path: '/curriculum/:grade',
          builder: (context, state) {
            final grade = state.pathParameters['grade']!;
            return SubjectListScreen(curriculumId: grade);
          },
        ),
        GoRoute(
          path: '/curriculum/:grade/:subject/chapters',
          builder: (context, state) {
            final grade = state.pathParameters['grade']!;
            final subject = state.pathParameters['subject']!;
            return ChapterListScreen(curriculumId: grade, subjectId: subject);
          },
        ),
        GoRoute(
          path: '/curriculum/:grade/:subject/chapter/:chapterId',
          builder: (context, state) {
            final chapterId = state.pathParameters['chapterId']!;
            return ChapterDetailScreen(assetPath: chapterId);
          },
        ),
        GoRoute(
          path: '/learning/engine/:chapterId',
          builder: (context, state) {
            return const PedagogyEngineScreen();
          },
        ),
        GoRoute(
          path: '/learning/engine/gold/:chapterId',
          builder: (context, state) {
            final chapterId = state.pathParameters['chapterId']!;
            return LearningEngineScreen(
              moduleId: chapterId,
              title: 'Chapter',
            );
          },
        ),
        GoRoute(
          path: '/assessment/engine/:chapterId',
          builder: (context, state) {
            final chapterId = state.pathParameters['chapterId']!;
            return ExamEngineScreen(moduleId: chapterId);
          },
        ),
        GoRoute(
          path: '/assessment/bank/:chapterId',
          builder: (context, state) {
            final chapterId = state.pathParameters['chapterId']!;
            return QuestionBankScreen(moduleId: chapterId);
          },
        ),
        GoRoute(
          path: '/assessment/paper',
          builder: (context, state) {
            return const QuestionPaperViewScreen(questions: [], title: "Test");
          },
        ),
        GoRoute(
          path: '/learning',
          builder: (context, state) => const LearningHome(),
          routes: [
            GoRoute(path: 'maths3to6', builder: (context, state) => ExitOverlay(child: maths3to6.AppGate())),
            GoRoute(path: 'english_sim', builder: (context, state) => ExitOverlay(child: english_sim.AppGate())),
            GoRoute(path: 'commerce', builder: (context, state) => ExitOverlay(child: commerce.CommerceStartupGate())),
            GoRoute(path: 'physics', builder: (context, state) => ExitOverlay(child: physics.AppGate())),
            // The 4 new apps
            GoRoute(path: 'maths_sim', builder: (context, state) => ExitOverlay(child: maths_sim.AppGate())),
            GoRoute(
              path: 'sci_sim', 
              builder: (context, state) {
                final gradeStr = state.uri.queryParameters['grade'];
                final grade = gradeStr != null ? int.tryParse(gradeStr) : null;
                return ExitOverlay(child: sci_sim.AppGate(preSelectedGrade: grade));
              }
            ),
            GoRoute(
              path: 'eng_sim_hs', 
              builder: (context, state) => ExitOverlay(child: eng_sim_hs.AppGate())
            ),
            GoRoute(
              path: 'eng3to6', 
              builder: (context, state) {
                final gradeStr = state.uri.queryParameters['grade'];
                final grade = gradeStr != null ? int.tryParse(gradeStr) : null;
                return ExitOverlay(child: english_sim.AppGate(preSelectedGrade: grade));
              }
            ),
            GoRoute(
              path: 'stats', builder: (context, state) => ExitOverlay(child: stats.StartupGate())),
            GoRoute(
              path: 'sci_sim_chapter/:chapterId',
              builder: (context, state) {
                final chapterId = state.pathParameters['chapterId']!;
                // Remove the sci_sim: prefix before searching
                final cleanId = chapterId.replaceAll('sci_sim:', '');
                final allSimChapters = [
                  ...sci_sim.allClass7Chapters,
                  ...sci_sim.allClass8Chapters,
                  ...sci_sim.allClass9Chapters,
                  ...sci_sim.allClass10Chapters,
                ];
                final chapter = allSimChapters.firstWhere(
                  (c) => c.chapterId == cleanId,
                  orElse: () => allSimChapters.first,
                );
                return ExitOverlay(child: sci_sim.ChapterDetailView(chapter: chapter));
              },
            ),
            
            
            
          ],
        ),
        GoRoute(
          path: '/assessment',
          builder: (context, state) => const AssessmentHome(),
        ),
        GoRoute(
          path: '/community',
          builder: (context, state) => const CommunityHome(),
        ),
        GoRoute(
          path: '/admin',
          builder: (context, state) => const AdminSettingsScreen(),
        ),
        GoRoute(
          path: '/admin_settings',
          builder: (context, state) => const AdminSettingsScreen(),
        ),
        GoRoute(
          path: '/content_editor',
          builder: (context, state) {
            final assetPath = state.uri.queryParameters['path'];
            return ContentEditorScreen(assetPath: assetPath);
          },
        ),
        GoRoute(
          path: '/digitization_studio',
          builder: (context, state) => const PaperDigitizationStudioScreen(),
        ),
      ], // Closes routes of ShellRoute
    ), // Closes ShellRoute
  ], // Closes routes of GoRouter
); // Closes GoRouter

Widget _buildBottomNav(BuildContext context, String currentPath) {
  int currentIndex = 0;
  if (currentPath.startsWith('/learning')) {
    currentIndex = 1;
  } else if (currentPath.startsWith('/assessment')) {
    currentIndex = 2;
  } else if (currentPath.startsWith('/community')) {
    currentIndex = 3;
  }

  return NavigationBar(
    selectedIndex: currentIndex,
    onDestinationSelected: (index) {
      switch (index) {
        case 0:
          // Navigating away from Dictionary to another tab → clear saved location
          NavigationMemoryService.instance.clearReturnLocation();
          context.go('/home');
          break;
        case 1:
          NavigationMemoryService.instance.clearReturnLocation();
          context.go('/learning');
          break;
        case 2:
          NavigationMemoryService.instance.clearReturnLocation();
          context.go('/assessment');
          break;
        case 3:
          NavigationMemoryService.instance.clearReturnLocation();
          context.go('/community');
          break;
      }
    },
    destinations: const [
      NavigationDestination(icon: Icon(Icons.home_outlined), selectedIcon: Icon(Icons.home), label: 'Home'),
      NavigationDestination(icon: Icon(Icons.menu_book_outlined), selectedIcon: Icon(Icons.menu_book), label: 'Learn'),
      NavigationDestination(icon: Icon(Icons.assignment_outlined), selectedIcon: Icon(Icons.assignment), label: 'Assess'),
      NavigationDestination(icon: Icon(Icons.people_outline), selectedIcon: Icon(Icons.people), label: 'Community'),
    ],
  );
}
