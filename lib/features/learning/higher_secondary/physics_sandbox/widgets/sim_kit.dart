import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import 'fx/stage_backdrop.dart';

/// The uniform building blocks every sandbox is assembled from.
/// One look, one behavior — no sandbox invents its own chrome.

/// Gradient-sky stage container that hosts a sandbox's canvas.
class SandboxStage extends StatelessWidget {
  final double height;
  final Widget child;
  const SandboxStage({super.key, this.height = 220, required this.child});

  @override
  Widget build(BuildContext context) {
    return Container(
      height: height,
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          begin: Alignment.topCenter,
          end: Alignment.bottomCenter,
          colors: [StageBackdrop.skyTop, StageBackdrop.skyMid, StageBackdrop.skyLow],
          stops: [0.0, 0.75, 1.0],
        ),
        borderRadius: BorderRadius.circular(Corner.lg),
      ),
      clipBehavior: Clip.antiAlias,
      child: child,
    );
  }
}

/// Live numeric readout chip.
class TelemetryChip extends StatelessWidget {
  final String label;
  final String value;
  final Color color;
  const TelemetryChip(this.label, this.value, {super.key, this.color = Palette.primary});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(Gap.x3),
      decoration: BoxDecoration(
        color: Palette.surface,
        borderRadius: BorderRadius.circular(Corner.md),
        border: Border.all(color: Palette.border),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(label.toUpperCase(), style: Type.label.copyWith(fontSize: 9)),
          const SizedBox(height: 4),
          Text(value,
              style: Type.bodyStrong.copyWith(
                  fontSize: 16, fontFamily: 'monospace', color: color)),
        ],
      ),
    );
  }
}

/// Evenly-spaced row of telemetry chips.
class TelemetryRow extends StatelessWidget {
  final List<TelemetryChip> chips;
  const TelemetryRow(this.chips, {super.key});

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        for (var i = 0; i < chips.length; i++) ...[
          if (i > 0) const SizedBox(width: Gap.x3),
          Expanded(child: chips[i]),
        ],
      ],
    );
  }
}

/// Continuous labelled slider — never disabled, even mid-run.
class SimSlider extends StatelessWidget {
  final String label;
  final double value, min, max;
  final String unit;
  final Color color;
  final int decimals;
  final ValueChanged<double> onChanged;

  const SimSlider({
    super.key,
    required this.label,
    required this.value,
    required this.min,
    required this.max,
    this.unit = '',
    this.color = Palette.primary,
    this.decimals = 1,
    required this.onChanged,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text('$label = ${value.toStringAsFixed(decimals)} $unit',
            style: Type.caption.copyWith(fontSize: 12, fontWeight: FontWeight.w600)),
        SliderTheme(
          data: SliderTheme.of(context).copyWith(
            activeTrackColor: color,
            thumbColor: color,
            overlayColor: color.withValues(alpha: 0.12),
          ),
          child: Slider(value: value.clamp(min, max), min: min, max: max, onChanged: onChanged),
        ),
      ],
    );
  }
}

/// Simulation time source with Start / Pause / Reset semantics.
/// Owns elapsed seconds `t`; the host widget rebuilds on every tick.
class SimClock {
  SimClock(this._vsync, this._onTick);

  final TickerProvider _vsync;
  final VoidCallback _onTick;
  Ticker? _ticker;
  Duration _last = Duration.zero;

  /// Elapsed simulated seconds.
  double t = 0;
  bool _running = false;
  bool get running => _running;

  void _tick(Duration elapsed) {
    t += (elapsed - _last).inMicroseconds / 1e6;
    _last = elapsed;
    _onTick();
  }

  void start() {
    if (_running) return;
    _running = true;
    _last = Duration.zero;
    _ticker = _vsync.createTicker(_tick)..start();
    _onTick();
  }

  void pause() {
    if (!_running) return;
    _running = false;
    _ticker?.dispose();
    _ticker = null;
    _onTick();
  }

  void reset() {
    _running = false;
    _ticker?.dispose();
    _ticker = null;
    t = 0;
    _onTick();
  }

  void dispose() {
    _ticker?.dispose();
    _ticker = null;
  }
}
