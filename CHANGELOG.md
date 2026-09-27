# Changelog

All notable changes to Shine Academy EduOS will be documented in this file.

## [1.0.4-beta] - 2026-08-07
### Added
- Phase 8 Architecture Documents (Master, Knowledge Graph, Pedagogy, Reward Engine).
- Universal Learning Engine Presentation Widget.
- Smart Panel Remote Control Support (`HardwareKeyboardListener`).
- Dynamic TTS Voice Rewards (Randomized pitch/rate).
- Animated SVG Diagram Tracing (`path_drawing`).

### Changed
- Shifted gamification voice away from static `.mp3` assets to `flutter_tts` to save space.

### Fixed
- Fixed `10^-9` rendering as crossed boxes in exported PDFs by embedding `NotoSansMath`.
- Fixed UI overlapping the Android Status Bar by wrapping Learning Engine in `SafeArea`.
