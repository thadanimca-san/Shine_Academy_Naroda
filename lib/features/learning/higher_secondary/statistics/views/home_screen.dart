import 'package:flutter/material.dart';

import '../models/board_model.dart';
import '../widgets/branding_header_widget.dart';
import 'student_topic_screen.dart';
import 'teacher_paper_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Landing screen after activation: pick Board + Class, then choose
/// whether you're a student (practice) or teacher (paper generator).
class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  Board _board = Board.gseb;
  int _schoolClass = 11;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(TrilingualService.instance.getUIText('Statistics — Class 11 & 12'))),
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
                    items: [
                      DropdownMenuItem(value: Board.gseb, child: Text(TrilingualService.instance.getUIText('GSEB'))),
                      DropdownMenuItem(value: Board.cbse, child: Text(TrilingualService.instance.getUIText('CBSE'))),
                    ],
                    onChanged: (v) => setState(() => _board = v!),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: DropdownButtonFormField<int>(
                    decoration: const InputDecoration(labelText: 'Class', border: OutlineInputBorder()),
                    initialValue: _schoolClass,
                    items: [
                      DropdownMenuItem(value: 11, child: Text(TrilingualService.instance.getUIText('Class 11'))),
                      DropdownMenuItem(value: 12, child: Text(TrilingualService.instance.getUIText('Class 12'))),
                    ],
                    onChanged: (v) => setState(() => _schoolClass = v!),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 32),
            Card(
              child: ListTile(
                leading: Icon(Icons.school, size: 36, color: Colors.indigo),
                title: Text(TrilingualService.instance.getUIText('I am a Student')),
                subtitle: Text(TrilingualService.instance.getUIText('Practice topics with instant feedback and unlimited questions')),
                trailing: Icon(Icons.arrow_forward_ios),
                onTap: () => Navigator.of(context).push(MaterialPageRoute(
                  builder: (_) => StudentTopicScreen(board: _board, schoolClass: _schoolClass),
                )),
              ),
            ),
            const SizedBox(height: 12),
            Card(
              child: ListTile(
                leading: Icon(Icons.assignment, size: 36, color: Colors.teal),
                title: Text(TrilingualService.instance.getUIText('I am a Teacher')),
                subtitle: Text(TrilingualService.instance.getUIText('Generate worksheets & fully-worked answer keys')),
                trailing: Icon(Icons.arrow_forward_ios),
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
