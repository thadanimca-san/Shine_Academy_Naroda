import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'bevel_button.dart';

/// The mandatory control bar for every simulation:
/// ▶ Start (or ⏸ Pause while running) + ↺ Reset.
///
/// Sliders remain live at all times; these buttons own time itself.
class SimControls extends StatelessWidget {
  final bool running;
  final VoidCallback onStart;
  final VoidCallback onPause;
  final VoidCallback onReset;

  /// Optional label override for the start action (e.g. 'Launch', 'Release').
  final String startLabel;

  const SimControls({
    super.key,
    required this.running,
    required this.onStart,
    required this.onPause,
    required this.onReset,
    this.startLabel = 'Start',
  });

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Expanded(
          child: running
              ? BevelButton(
                  label: 'Pause',
                  icon: Icons.pause_rounded,
                  color: Palette.accent,
                  onPressed: onPause,
                )
              : BevelButton.go(
                  label: startLabel,
                  icon: Icons.play_arrow_rounded,
                  onPressed: onStart,
                ),
        ),
        const SizedBox(width: Gap.x3),
        BevelButton.quiet(
          label: 'Reset',
          icon: Icons.replay_rounded,
          expanded: false,
          onPressed: onReset,
        ),
      ],
    );
  }
}
