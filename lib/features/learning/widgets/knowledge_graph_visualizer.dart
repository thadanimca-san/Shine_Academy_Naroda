import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:shine_academy_naroda/core/engine/knowledge_graph_service.dart';
import 'package:shine_academy_naroda/foundation/theme/app_colors.dart';
import 'package:shine_academy_naroda/foundation/theme/app_typography.dart';

class KnowledgeGraphVisualizer extends StatelessWidget {
  final String nodeId;

  const KnowledgeGraphVisualizer({super.key, required this.nodeId});

  @override
  Widget build(BuildContext context) {
    if (!KnowledgeGraphService.instance.isLoaded) {
      return Center(child: CircularProgressIndicator());
    }

    final currentNode = KnowledgeGraphService.instance.nodes[nodeId];
    if (currentNode == null) {
      return Center(child: Text("Graph data not found."));
    }

    final prereqs = KnowledgeGraphService.instance.getPrerequisites(nodeId);
    final nextTopics = KnowledgeGraphService.instance.getNextTopics(nodeId);
    final usedIn = KnowledgeGraphService.instance.getUsedInChapters(nodeId);

    return SingleChildScrollView(
      child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            if (prereqs.isNotEmpty) ...[
              for (var p in prereqs) ...[
                _buildGraphNode(context, p.title, p.subtitle, Colors.grey[400]!),
                Container(height: 30, width: 2, color: AppColors.primary.withValues(alpha: 0.5)),
              ]
            ],
            
            _buildGraphNode(context, currentNode.title, "Current Topic", AppColors.primary),
            
            if (nextTopics.isNotEmpty || usedIn.isNotEmpty) ...[
              Container(height: 30, width: 2, color: AppColors.primary.withValues(alpha: 0.5)),
              
              if (nextTopics.isNotEmpty) ...[
                for (var n in nextTopics) ...[
                  _buildGraphNode(context, n.title, "Next Topic", Colors.grey[300]!),
                  if (n != nextTopics.last) Container(height: 20, width: 2, color: Colors.grey[200]),
                ]
              ],
              
              if (usedIn.isNotEmpty) ...[
                for (var u in usedIn) ...[
                  _buildGraphNode(context, u.title, "Used In", Colors.grey[300]!),
                  if (u != usedIn.last) Container(height: 20, width: 2, color: Colors.grey[200]),
                ]
              ]
            ] else ...[
               Container(height: 30, width: 2, color: Colors.grey[300]!),
               _buildGraphNode(context, "More topics coming soon", "End of Path", Colors.grey[300]!),
            ]
          ],
        ),
      ),
    );
  }

  Widget _buildGraphNode(BuildContext context, String title, String subtitle, Color color) {
    return Container(
      width: 250,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: color.withValues(alpha: 0.1),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: color, width: 2),
      ),
      child: Column(
        children: [
          Text(subtitle.toUpperCase(), 
            style: GoogleFonts.inter(
              fontSize: 10 * AppTypography.scaleFactor(context), 
              fontWeight: FontWeight.bold, 
              color: color
            )
          ),
          const SizedBox(height: 4),
          Text(title, 
            textAlign: TextAlign.center,
            style: GoogleFonts.poppins(
              fontSize: 14 * AppTypography.scaleFactor(context), 
              fontWeight: FontWeight.bold, 
              color: AppColors.textPrimary
            )
          ),
        ],
      ),
    );
  }
}
