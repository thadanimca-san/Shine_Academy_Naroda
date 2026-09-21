import 'package:flutter/material.dart';
import '../../features/gamification/widgets/mast_hai_dialog.dart';

class StreakManagerService {
  // Singleton Pattern
  StreakManagerService._privateConstructor();
  static final StreakManagerService instance = StreakManagerService._privateConstructor();

  int _currentStreak = 0;

  int get currentStreak => _currentStreak;

  void onCorrectAnswer(BuildContext context) {
    _currentStreak++;
    
    // Trigger on every continuous multiple of 8
    if (_currentStreak > 0 && _currentStreak % 8 == 0) {
      _showMastHaiDialog(context);
    }
  }

  void onIncorrectAnswer() {
    // Reset streak on incorrect answer for continuous tracking
    _currentStreak = 0;
  }

  void resetSession() {
    _currentStreak = 0;
  }

  void _showMastHaiDialog(BuildContext context) {
    showGeneralDialog(
      context: context,
      barrierDismissible: false,
      barrierColor: Colors.black.withValues(alpha: 0.7),
      transitionDuration: const Duration(milliseconds: 400),
      pageBuilder: (context, animation, secondaryAnimation) {
        return const MastHaiDialog();
      },
      transitionBuilder: (context, animation, secondaryAnimation, child) {
        return ScaleTransition(
          scale: CurvedAnimation(parent: animation, curve: Curves.elasticOut),
          child: child,
        );
      },
    );
  }
}
