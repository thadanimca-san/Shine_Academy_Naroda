import 'package:flutter/cupertino.dart' show CupertinoPageTransitionsBuilder;
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'tokens.dart';

abstract final class AppTheme {
  static ThemeData light() {
    final base = ThemeData(
      useMaterial3: true,
      colorScheme: ColorScheme.fromSeed(
        seedColor: Palette.primary,
        primary: Palette.primary,
        surface: Palette.surface,
      ),
      scaffoldBackgroundColor: Palette.bg,
      splashFactory: InkSparkle.splashFactory,
    );

    return base.copyWith(
      appBarTheme: const AppBarTheme(
        backgroundColor: Palette.bg,
        foregroundColor: Palette.textStrong,
        elevation: 0,
        scrolledUnderElevation: 0,
        centerTitle: false,
        systemOverlayStyle: SystemUiOverlayStyle(
          statusBarColor: Colors.transparent,
          statusBarIconBrightness: Brightness.dark,
          systemNavigationBarColor: Colors.transparent,
          systemNavigationBarIconBrightness: Brightness.dark,
        ),
      ),
      pageTransitionsTheme: const PageTransitionsTheme(builders: {
        TargetPlatform.android: _SharedAxisTransitionsBuilder(),
        TargetPlatform.iOS: CupertinoPageTransitionsBuilder(),
        TargetPlatform.windows: _SharedAxisTransitionsBuilder(),
        TargetPlatform.macOS: CupertinoPageTransitionsBuilder(),
        TargetPlatform.linux: _SharedAxisTransitionsBuilder(),
      }),
      sliderTheme: SliderThemeData(
        trackHeight: 4,
        activeTrackColor: Palette.primary,
        inactiveTrackColor: Palette.border,
        thumbColor: Palette.primary,
        overlayColor: Palette.primary.withValues(alpha: 0.12),
      ),
      dividerTheme: const DividerThemeData(color: Palette.border, thickness: 1),
      snackBarTheme: SnackBarThemeData(
        behavior: SnackBarBehavior.floating,
        backgroundColor: Palette.textStrong,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(Corner.md)),
      ),
      bottomSheetTheme: const BottomSheetThemeData(
        backgroundColor: Palette.surface,
        surfaceTintColor: Colors.transparent,
        showDragHandle: true,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.vertical(top: Radius.circular(Corner.xl)),
        ),
      ),
    );
  }
}

/// Subtle vertical shared-axis transition: incoming page fades in and rises
/// slightly; feels closer to Linear/Arc than the default zoom.
class _SharedAxisTransitionsBuilder extends PageTransitionsBuilder {
  const _SharedAxisTransitionsBuilder();

  @override
  Widget buildTransitions<T>(
    PageRoute<T> route,
    BuildContext context,
    Animation<double> animation,
    Animation<double> secondaryAnimation,
    Widget child,
  ) {
    final curved = CurvedAnimation(parent: animation, curve: Motion.ease);
    return FadeTransition(
      opacity: curved,
      child: SlideTransition(
        position: Tween<Offset>(begin: const Offset(0, 0.035), end: Offset.zero).animate(curved),
        child: child,
      ),
    );
  }
}
