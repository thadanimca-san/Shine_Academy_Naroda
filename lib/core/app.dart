import 'package:flutter/material.dart';
import '../foundation/theme/app_theme.dart';
import '../foundation/navigation/app_router.dart';
import 'services/presentation_service.dart';
import '../shared/widgets/global_dictionary_search.dart';
import 'services/trilingual_service.dart';

class ShineAcademyApp extends StatefulWidget {
  const ShineAcademyApp({super.key});

  @override
  State<ShineAcademyApp> createState() => _ShineAcademyAppState();
}

class _ShineAcademyAppState extends State<ShineAcademyApp> {
  @override
  void initState() {
    super.initState();
    // Auto-detect device type after the first frame is rendered.
    // If the screen is >= 900px wide (Android Digital Panel / IFP),
    // Presentation Mode is automatically turned ON.
    // On a regular phone it stays OFF. The user can still toggle it manually.
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (mounted) {
        PresentationService.autoDetect(context);
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<bool>(
      valueListenable: PresentationService.isPresentationMode,
      builder: (context, isPresentationMode, child) {
        return ListenableBuilder(
          listenable: TrilingualService.instance,
          builder: (context, child) {
            return MaterialApp.router(
              title: 'Shine Academy Naroda',
              debugShowCheckedModeBanner: false,
              themeMode: ThemeMode.light,
              theme: AppTheme.lightTheme,
              darkTheme: AppTheme.darkTheme,
              routerConfig: router,
              builder: (context, child) {
                // Apply global font scaling across the entire app
                final mediaQueryData = MediaQuery.of(context);
                final scaleFactor = PresentationService.getScaleFactor(context);
                
                return MediaQuery(
                  data: mediaQueryData.copyWith(
                    textScaler: TextScaler.linear(scaleFactor),
                  ),
                  // SafeArea at the app level ensures all screens respect device
                  // notches, status bars, and navigation bars automatically —
                  // no need to add SafeArea inside each individual screen.
                  child: SafeArea(
                    top: false,  // Scaffold AppBar handles top area naturally
                    bottom: false, // Scaffold BottomNavigationBar handles bottom
                    child: GlobalDictionaryWrapper(child: child!),
                  ),
                );
              },
            );
          },
        );
      },
    );
  }
}