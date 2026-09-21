import 'package:flutter/material.dart';

import '../models/board_model.dart';
import 'central_tendency_practice_screen.dart';
import 'correlation_practice_screen.dart';
import 'dispersion_practice_screen.dart';
import 'index_number_practice_screen.dart';
import 'progress_screen.dart';
import 'regression_practice_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Topic picker shown to a student after they choose Board + Class —
/// each tile launches the practice flow for that topic. New topics slot
/// in here as they're added to the app.
class StudentTopicScreen extends StatelessWidget {
  final Board board;
  final int schoolClass;

  const StudentTopicScreen({super.key, required this.board, required this.schoolClass});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Choose a Topic')),
        actions: [
          IconButton(
            icon: Icon(Icons.insights),
            tooltip: 'My Progress',
            onPressed: () => Navigator.of(context).push(MaterialPageRoute(builder: (_) => const ProgressScreen())),
          ),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Card(
            color: Colors.indigo.withValues(alpha: 0.08),
            child: ListTile(
              leading: Icon(Icons.insights, size: 36, color: Colors.indigo),
              title: Text(TrilingualService.instance.getUIText('My Progress')),
              subtitle: Text(TrilingualService.instance.getUIText('See your accuracy by topic and what needs more practice')),
              trailing: Icon(Icons.arrow_forward_ios),
              onTap: () => Navigator.of(context).push(MaterialPageRoute(builder: (_) => const ProgressScreen())),
            ),
          ),
          const SizedBox(height: 12),
          _topicTile(
            context,
            icon: Icons.bar_chart,
            color: Colors.teal,
            title: 'Measures of Central Tendency',
            subtitle: 'Mean, Median & Mode — individual, discrete & continuous series',
            onTap: () => Navigator.of(context).push(MaterialPageRoute(
              builder: (_) => CentralTendencyPracticeScreen(board: board, schoolClass: schoolClass),
            )),
          ),
          const SizedBox(height: 12),
          _topicTile(
            context,
            icon: Icons.show_chart,
            color: Colors.deepOrange,
            title: 'Measures of Dispersion',
            subtitle: 'Range, Mean Deviation, Standard Deviation & Coefficient of Variation',
            onTap: () => Navigator.of(context).push(MaterialPageRoute(
              builder: (_) => DispersionPracticeScreen(board: board, schoolClass: schoolClass),
            )),
          ),
          const SizedBox(height: 12),
          _topicTile(
            context,
            icon: Icons.scatter_plot,
            color: Colors.purple,
            title: 'Correlation',
            subtitle: "Karl Pearson's Coefficient of Correlation",
            onTap: () => Navigator.of(context).push(MaterialPageRoute(
              builder: (_) => CorrelationPracticeScreen(board: board, schoolClass: schoolClass),
            )),
          ),
          const SizedBox(height: 12),
          _topicTile(
            context,
            icon: Icons.trending_up,
            color: Colors.indigo,
            title: 'Index Numbers',
            subtitle: 'Simple Aggregative, Price Relatives, Laspeyres\' & Paasche\'s methods',
            onTap: () => Navigator.of(context).push(MaterialPageRoute(
              builder: (_) => IndexNumberPracticeScreen(board: board, schoolClass: schoolClass),
            )),
          ),
          const SizedBox(height: 12),
          _topicTile(
            context,
            icon: Icons.timeline,
            color: Colors.pink,
            title: 'Regression Analysis',
            subtitle: 'Regression lines of Y on X and X on Y using the deviation method',
            onTap: () => Navigator.of(context).push(MaterialPageRoute(
              builder: (_) => RegressionPracticeScreen(board: board, schoolClass: schoolClass),
            )),
          ),
        ],
      ),
    );
  }

  Widget _topicTile(
    BuildContext context, {
    required IconData icon,
    required Color color,
    required String title,
    required String subtitle,
    required VoidCallback onTap,
  }) {
    return Card(
      child: ListTile(
        leading: Icon(icon, size: 36, color: color),
        title: Text(title),
        subtitle: Text(subtitle),
        trailing: Icon(Icons.arrow_forward_ios),
        onTap: onTap,
      ),
    );
  }
}
