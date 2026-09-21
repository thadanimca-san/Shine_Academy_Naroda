import 'package:flutter/material.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Consistent wrapper card used by every chapter simulation: an icon + title
/// header, an optional one-line description, and the interactive body.
class SimFrame extends StatelessWidget {
  final String title;
  final IconData icon;
  final Color accent;
  final String? description;
  final Widget child;
  final List<Widget>? actions;

  const SimFrame({
    super.key,
    required this.title,
    required this.icon,
    required this.child,
    this.accent = Colors.blue,
    this.description,
    this.actions,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 3,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(icon, color: accent),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(
                    title,
                    style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: accent),
                  ),
                ),
                if (actions != null) ...actions!,
              ],
            ),
            if (description != null) ...[
              const SizedBox(height: 4),
              Text(description!, style: TextStyle(fontSize: 12.5, color: Theme.of(context).colorScheme.onSurfaceVariant)),
            ],
            const Divider(height: 22),
            child,
          ],
        ),
      ),
    );
  }
}

/// A compact readout tile used to show a live computed value (e.g. "Speed: 4.2 m/s").
class SimMetric extends StatelessWidget {
  final String label;
  final String value;
  final Color color;

  const SimMetric({super.key, required this.label, required this.value, this.color = Colors.indigo});

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(label, style: TextStyle(fontSize: 11, color: Colors.grey), textAlign: TextAlign.center),
        const SizedBox(height: 2),
        Text(value, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: color)),
      ],
    );
  }
}

/// Row of SimMetric tiles inside a light readout panel.
class SimMetricPanel extends StatelessWidget {
  final List<SimMetric> metrics;

  const SimMetricPanel({super.key, required this.metrics});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 8),
      decoration: BoxDecoration(
        color: Colors.grey.shade50,
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: Colors.grey.shade200),
      ),
      child: Row(mainAxisAlignment: MainAxisAlignment.spaceAround, children: metrics),
    );
  }
}

/// Labeled slider control with a consistent look across simulations.
class SimSlider extends StatelessWidget {
  final String label;
  final double value;
  final double min;
  final double max;
  final int? divisions;
  final ValueChanged<double> onChanged;
  final Color activeColor;

  const SimSlider({
    super.key,
    required this.label,
    required this.value,
    required this.min,
    required this.max,
    required this.onChanged,
    this.divisions,
    this.activeColor = Colors.blue,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(label, style: TextStyle(fontSize: 12.5, fontWeight: FontWeight.w600)),
        SliderTheme(
          data: SliderTheme.of(context).copyWith(activeTrackColor: activeColor, thumbColor: activeColor),
          child: Slider(value: value, min: min, max: max, divisions: divisions, onChanged: onChanged),
        ),
      ],
    );
  }
}

/// Play / Pause / Reset transport control row for time-based animations.
class SimTransport extends StatelessWidget {
  final bool isPlaying;
  final VoidCallback onPlayPause;
  final VoidCallback onReset;
  final Color color;

  const SimTransport({
    super.key,
    required this.isPlaying,
    required this.onPlayPause,
    required this.onReset,
    this.color = Colors.blue,
  });

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Expanded(
          child: ElevatedButton.icon(
            onPressed: onPlayPause,
            icon: Icon(isPlaying ? Icons.pause : Icons.play_arrow),
            label: Text(isPlaying ? 'Pause' : 'Play'),
            style: ElevatedButton.styleFrom(backgroundColor: color, foregroundColor: Colors.white),
          ),
        ),
        const SizedBox(width: 10),
        OutlinedButton.icon(
          onPressed: onReset,
          icon: Icon(Icons.replay),
          label: Text(TrilingualService.instance.getUIText('Reset')),
        ),
      ],
    );
  }
}
