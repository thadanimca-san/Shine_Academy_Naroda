import 'package:flutter/material.dart';

import '../models/medium_model.dart';
import '../models/problem_model.dart';
import '../widgets/branding_header_widget.dart';
import 'student_topic_screen.dart';
import 'teacher_paper_screen.dart';

/// Landing screen after activation: pick Board + Class + Medium, then
/// choose whether you're a student (practice) or teacher (paper
/// generator).
class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  Board _board = Board.cbse;
  int _schoolClass = 11;
  Medium _medium = Medium.english;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Accountancy — Class 11 & 12')),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const BrandingHeaderWidget(),
            const SizedBox(height: 20),
            Row(
              children: [
                Expanded(
                  child: DropdownButtonFormField<Board>(
                    decoration: const InputDecoration(labelText: 'Board', border: OutlineInputBorder()),
                    initialValue: _board,
                    items: const [
                      DropdownMenuItem(value: Board.gseb, child: Text('GSEB')),
                      DropdownMenuItem(value: Board.cbse, child: Text('CBSE')),
                    ],
                    onChanged: (v) => setState(() => _board = v!),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: DropdownButtonFormField<int>(
                    decoration: const InputDecoration(labelText: 'Class', border: OutlineInputBorder()),
                    initialValue: _schoolClass,
                    items: const [
                      DropdownMenuItem(value: 11, child: Text('Class 11')),
                      DropdownMenuItem(value: 12, child: Text('Class 12')),
                    ],
                    onChanged: (v) => setState(() => _schoolClass = v!),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),
            DropdownButtonFormField<Medium>(
              decoration: const InputDecoration(labelText: 'Medium of Instruction', border: OutlineInputBorder()),
              initialValue: _medium,
              items: const [
                DropdownMenuItem(value: Medium.english, child: Text('English')),
                DropdownMenuItem(value: Medium.gujarati, child: Text('ગુજરાતી (Gujarati)')),
              ],
              onChanged: (v) => setState(() => _medium = v!),
            ),
            const SizedBox(height: 32),
            Card(
              child: ListTile(
                leading: const Icon(Icons.school, size: 36, color: Colors.indigo),
                title: const Text('I am a Student'),
                subtitle: const Text('Practice topics with instant feedback and unlimited questions'),
                trailing: const Icon(Icons.arrow_forward_ios),
                onTap: () => Navigator.of(context).push(MaterialPageRoute(
                  builder: (_) => StudentTopicScreen(board: _board, schoolClass: _schoolClass, medium: _medium),
                )),
              ),
            ),
            const SizedBox(height: 12),
            Card(
              child: ListTile(
                leading: const Icon(Icons.assignment, size: 36, color: Colors.teal),
                title: const Text('I am a Teacher'),
                subtitle: const Text('Generate question papers & fully-worked answer keys'),
                trailing: const Icon(Icons.arrow_forward_ios),
                onTap: () => Navigator.of(context).push(MaterialPageRoute(
                  builder: (_) => const TeacherPaperScreen(),
                )),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
