import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';

/// Central catalogue of Lottie animations bundled in assets/lottie/.
/// Drop new .json files there (e.g. generated via the Lottie creator MCP)
/// and add a constant — every screen then reuses the same asset by name.
abstract final class LottieFx {
  // Feedback & brand
  static const successCheck = 'assets/lottie/success_check.json';
  static const atomOrbit = 'assets/lottie/atom_orbit.json';

  // Particles
  static const electron = 'assets/lottie/electron.json';
  static const proton = 'assets/lottie/proton.json';
  static const neutron = 'assets/lottie/neutron.json';
  static const photon = 'assets/lottie/photon.json';
  static const molecule = 'assets/lottie/molecule.json';

  // Mechanics
  static const ball = 'assets/lottie/ball.json';
  static const car = 'assets/lottie/car.json';
  static const pendulumBob = 'assets/lottie/pendulum_bob.json';
  static const spring = 'assets/lottie/spring.json';
  static const rocket = 'assets/lottie/rocket.json';
  static const planetEarth = 'assets/lottie/planet_earth.json';
  static const satellite = 'assets/lottie/satellite.json';

  // Thermal
  static const flame = 'assets/lottie/flame.json';
  static const iceCube = 'assets/lottie/ice_cube.json';

  // Electricity & magnetism
  static const barMagnet = 'assets/lottie/bar_magnet.json';
  static const battery = 'assets/lottie/battery.json';
  static const bulb = 'assets/lottie/bulb.json';
  static const capacitorPlates = 'assets/lottie/capacitor_plates.json';

  // Optics
  static const convexLens = 'assets/lottie/convex_lens.json';
  static const concaveLens = 'assets/lottie/concave_lens.json';
  static const mirrorConcave = 'assets/lottie/mirror_concave.json';
  static const prism = 'assets/lottie/prism.json';
  static const candle = 'assets/lottie/candle.json';
}

/// Plays a bundled Lottie animation with a graceful fallback icon if the
/// asset fails to parse — the UI never breaks because of a bad animation.
class LottieBadge extends StatelessWidget {
  final String asset;
  final double size;
  final bool repeat;
  final IconData fallbackIcon;

  const LottieBadge(
    this.asset, {
    super.key,
    this.size = 96,
    this.repeat = false,
    this.fallbackIcon = Icons.auto_awesome_rounded,
  });

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: size,
      height: size,
      child: Lottie.asset(
        asset,
        repeat: repeat,
        fit: BoxFit.contain,
        errorBuilder: (_, __, ___) =>
            Icon(fallbackIcon, size: size * 0.6, color: Colors.amber),
      ),
    );
  }
}
