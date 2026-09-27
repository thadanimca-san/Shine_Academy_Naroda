# Technical Debt Register

*This document permanently tracks every shortcut, temporary implementation, hack, or workaround used in Shine Academy EduOS.*

## Known Technical Debt

1. **Large Switch Statement in `block_validator.dart`**
   - *Description:* The `validateBlock` function uses a massive hardcoded `switch` statement instead of a scalable Registry Pattern or `freezed` unions.
   - *Risk:* Low, but highly annoying to maintain as we add 100+ block types.
   
2. **`pubspec.yaml` Asset Whitelisting**
   - *Description:* Every new JSON curriculum module must be manually added to `pubspec.yaml`.
   - *Risk:* High. Flutter has a limit on the number of assets. This architecture will break when we have 1,000 chapters.
   - *Solution needed:* Over-The-Air (OTA) downloading of JSON modules from a cloud server.
   
3. **Disabled DRM Screen Protector**
   - *Description:* Removed `screen_protector` plugin to allow easy Beta testing on external displays.
   - *Risk:* Critical for Phase 3 (Public Launch). Must be re-added to prevent piracy.

4. **Single Stroke Color in SVG Animator**
   - *Description:* The `AnimatedDiagramWidget` currently forces all parsed paths into a single `stroke_color`.
   - *Risk:* Low.

5. **Repeated SVG Parsing**
   - *Description:* We are using `parseSvgPathData` at runtime in the widget `initState`.
   - *Solution needed:* Pre-compile paths into a binary or highly optimized format to save CPU cycles on low-end phones.
