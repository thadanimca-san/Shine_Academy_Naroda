# Universal Reward Engine Architecture

Gamification belongs to EduOS globally, not to individual subjects. 

## Responsibilities
- **XP (Experience Points):** Granted for completing blocks and passing assessments.
- **Coins:** Granted for perfect streaks. Used to unlock premium avatars or themes.
- **Badges / Achievements:** E.g., "Math Wizard", "Early Bird".
- **Streaks:** Daily login tracking to build habit.
- **Voice Rewards:** The dynamic TTS engine ("Mast Hai!", "Shining Bright!") that reacts to user success.
- **Leaderboards:** Local (class-wide) and Global rankings.

## Implementation Strategy
A global singleton `RewardService` that listens to `BlockCompletedEvents` emitted by the Learning Engine. It maintains state locally in SQLite (or SharedPreferences) and eventually syncs to the Cloud via the Analytics Engine.
