/// NavigationMemoryService
///
/// Saves the student's current route URI just before they navigate away to
/// the Dictionary tab. The Dictionary screen reads this value and shows a
/// prominent "Return to previous location" banner.
///
/// Usage:
///   // Before going to Dictionary:
///   NavigationMemoryService.instance.saveCurrentLocation(currentPath);
///
///   // From Dictionary screen to go back:
///   final uri = NavigationMemoryService.instance.returnLocation.value;
///   NavigationMemoryService.instance.clearReturnLocation();
///   context.go(uri);
library;

import 'package:flutter/foundation.dart';

class NavigationMemoryService {
  // ─── Singleton ─────────────────────────────────────────────────────────────
  static final NavigationMemoryService instance = NavigationMemoryService._();
  NavigationMemoryService._();

  // ─── State ─────────────────────────────────────────────────────────────────

  /// The URI the student was at before tapping the Dictionary tab.
  /// Null means "no saved location" (Dictionary was opened from Home, etc.)
  final ValueNotifier<String?> returnLocation = ValueNotifier<String?>(null);

  /// Human-readable label derived from the saved URI, e.g. "English Chapter".
  /// Used by the Dictionary screen to display a friendly return button.
  final ValueNotifier<String?> returnLabel = ValueNotifier<String?>(null);

  // ─── API ───────────────────────────────────────────────────────────────────

  /// Call this BEFORE navigating to the Dictionary.
  /// [uri] is the current route, e.g. '/curriculum/class3/english/chapter/ch1'.
  /// [label] is an optional friendly display name for the return button.
  void saveCurrentLocation(String uri, {String? label}) {
    returnLocation.value = uri;
    returnLabel.value = label ?? _labelFromUri(uri);
  }

  /// Call this after the student has returned to their previous location,
  /// or when they navigate somewhere else from the Dictionary.
  void clearReturnLocation() {
    returnLocation.value = null;
    returnLabel.value = null;
  }

  // ─── Helpers ───────────────────────────────────────────────────────────────

  /// Derives a short human-readable label from a route URI.
  String _labelFromUri(String uri) {
    if (uri.contains('/chapter/')) {
      // e.g. /curriculum/gseb_class3/english/chapter/eng_ch01
      final parts = uri.split('/');
      // Try to extract something meaningful
      final chapterIndex = parts.indexOf('chapter');
      if (chapterIndex != -1 && chapterIndex + 1 < parts.length) {
        final chapterId = parts[chapterIndex + 1];
        // Extract a friendly name: remove underscores, capitalise
        final friendly = chapterId
            .replaceAll('_', ' ')
            .split(' ')
            .map((w) => w.isNotEmpty
                ? '${w[0].toUpperCase()}${w.substring(1)}'
                : w)
            .join(' ');
        return friendly;
      }
      return 'Chapter';
    }
    if (uri.contains('/curriculum/')) {
      return 'Curriculum';
    }
    if (uri.contains('/learning')) {
      return 'Learning';
    }
    if (uri.contains('/assessment')) {
      return 'Assessment';
    }
    return 'Previous Screen';
  }
}
