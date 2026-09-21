import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../../core/services/gamification_service.dart';

class PlayerProfileCard extends StatelessWidget {
  const PlayerProfileCard({super.key});

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<int>(
      valueListenable: GamificationService.instance.levelNotifier,
      builder: (context, level, _) {
        return ValueListenableBuilder<int>(
          valueListenable: GamificationService.instance.xpNotifier,
          builder: (context, xp, _) {
            return ValueListenableBuilder<int>(
              valueListenable: GamificationService.instance.streakNotifier,
              builder: (context, streak, _) {
                
                // Calculate progress to next level
                int currentLevelBaseXp = (level - 1) * GamificationService.xpPerLevel;
                int xpIntoCurrentLevel = xp - currentLevelBaseXp;
                double progress = xpIntoCurrentLevel / GamificationService.xpPerLevel;

                String rankName = _getRankName(level);

                return Container(
                  padding: const EdgeInsets.all(20),
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      colors: [Colors.indigo.shade800, Colors.indigo.shade600],
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                    ),
                    borderRadius: BorderRadius.circular(20),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.indigo.withValues(alpha: 0.3),
                        blurRadius: 15,
                        offset: const Offset(0, 8),
                      )
                    ],
                  ),
                  child: Column(
                    children: [
                      Row(
                        children: [
                          // Avatar with Circular Progress
                          SizedBox(
                            height: 80,
                            width: 80,
                            child: Stack(
                              fit: StackFit.expand,
                              children: [
                                CircularProgressIndicator(
                                  value: progress,
                                  strokeWidth: 6,
                                  backgroundColor: Colors.white.withValues(alpha: 0.2),
                                  valueColor: const AlwaysStoppedAnimation<Color>(Colors.amber),
                                ),
                                Center(
                                  child: CircleAvatar(
                                    radius: 32,
                                    backgroundColor: Colors.indigo.shade100,
                                    child: Icon(Icons.person, size: 40, color: Colors.indigo),
                                  ),
                                ),
                                Positioned(
                                  bottom: 0,
                                  right: 0,
                                  child: Container(
                                    padding: const EdgeInsets.all(4),
                                    decoration: BoxDecoration(
                                      color: Colors.amber,
                                      shape: BoxShape.circle,
                                    ),
                                    child: Text(
                                      '$level',
                                      style: GoogleFonts.poppins(
                                        fontSize: 12,
                                        fontWeight: FontWeight.bold,
                                        color: Colors.indigo.shade900,
                                      ),
                                    ),
                                  ),
                                )
                              ],
                            ),
                          ),
                          const SizedBox(width: 20),
                          // User details
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  rankName,
                                  style: GoogleFonts.poppins(
                                    fontSize: 20,
                                    fontWeight: FontWeight.bold,
                                    color: Colors.white,
                                  ),
                                ),
                                const SizedBox(height: 4),
                                Text(
                                  '$xp XP',
                                  style: GoogleFonts.inter(
                                    fontSize: 14,
                                    color: Colors.white.withValues(alpha: 0.8),
                                    fontWeight: FontWeight.w600,
                                  ),
                                ),
                                const SizedBox(height: 8),
                                Row(
                                  children: [
                                    Icon(
                                      streak > 0 ? Icons.local_fire_department : Icons.local_fire_department_outlined,
                                      color: streak > 0 ? Colors.orange : Colors.white54,
                                      size: 16,
                                    ),
                                    const SizedBox(width: 4),
                                    Text(
                                      '$streak Day Streak',
                                      style: GoogleFonts.inter(
                                        fontSize: 12,
                                        color: streak > 0 ? Colors.orange.shade100 : Colors.white54,
                                        fontWeight: FontWeight.bold,
                                      ),
                                    ),
                                  ],
                                )
                              ],
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 16),
                      // Progress Bar details
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(
                            'Level $level',
                            style: GoogleFonts.inter(color: Colors.white70, fontSize: 12),
                          ),
                          Text(
                            'Level ${level + 1}',
                            style: GoogleFonts.inter(color: Colors.white70, fontSize: 12),
                          ),
                        ],
                      ),
                      const SizedBox(height: 8),
                      ClipRRect(
                        borderRadius: BorderRadius.circular(10),
                        child: LinearProgressIndicator(
                          value: progress,
                          minHeight: 8,
                          backgroundColor: Colors.white.withValues(alpha: 0.2),
                          valueColor: const AlwaysStoppedAnimation<Color>(Colors.amber),
                        ),
                      ),
                      const SizedBox(height: 8),
                      Text(
                        '${GamificationService.xpPerLevel - xpIntoCurrentLevel} XP to next level',
                        style: GoogleFonts.inter(color: Colors.white70, fontSize: 11),
                      ),
                    ],
                  ),
                );
              },
            );
          },
        );
      },
    );
  }

  String _getRankName(int level) {
    if (level < 2) return "Novice Scholar";
    if (level < 5) return "Apprentice";
    if (level < 10) return "Adept Learner";
    if (level < 20) return "Academic Knight";
    if (level < 50) return "Master of Wisdom";
    return "Grandmaster";
  }
}
