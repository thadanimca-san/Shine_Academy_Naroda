import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Hosts a bare sandbox widget (one without its own Scaffold) inside proper
/// app chrome: Material ancestor (kills the yellow debug-underline on Text),
/// colored top bar matching the lesson shell, and back navigation.
///
/// Topics hosted here have a lab but no written lesson yet — the bar shows a
/// single "Lab" stage so the layout language matches lesson screens.
class SandboxScreen extends StatelessWidget {
  final String title;
  final Widget child;
  const SandboxScreen({super.key, required this.title, required this.child});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Palette.primaryDeep,
        foregroundColor: Colors.white,
        titleSpacing: 0,
        title: Text(title, style: Type.heading.copyWith(color: Colors.white)),
        bottom: PreferredSize(
          preferredSize: const Size.fromHeight(46),
          child: Container(
            height: 46,
            alignment: Alignment.centerLeft,
            padding: const EdgeInsets.symmetric(horizontal: Gap.x4),
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: Gap.x3),
              height: 46,
              decoration: BoxDecoration(
                border: Border(bottom: BorderSide(color: Palette.accent, width: 3)),
              ),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Icon(Icons.science_outlined, size: 16, color: Colors.white),
                  const SizedBox(width: 6),
                  Text(TrilingualService.instance.getUIText('INTERACTIVE LAB'),
                      style: Type.label.copyWith(
                          fontSize: 11.5, letterSpacing: 0.3, color: Colors.white)),
                ],
              ),
            ),
          ),
        ),
      ),
      body: child,
    );
  }
}
