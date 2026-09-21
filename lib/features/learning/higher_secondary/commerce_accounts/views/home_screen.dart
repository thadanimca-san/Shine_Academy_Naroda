import 'package:flutter/material.dart';

import '../models/medium_model.dart';
import '../models/problem_model.dart';
import '../widgets/branding_header_widget.dart';
import 'student_topic_screen.dart';
import 'teacher_paper_screen.dart';

/// Landing screen after activation: pick Board + Class + Medium, then
/// choose whether you're a student (practice) or teacher (paper
/// generator).
import 'package:shine_academy_naroda/features/dictionary/dictionary_popup.dart';
import 'package:shine_academy_naroda/features/learning/learning_engine/learning_engine_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

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
      appBar: AppBar(title: Text(TrilingualService.instance.getUIText('Accountancy — Class 11 & 12'))),
      body: SingleChildScrollView(
        child: Padding(
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
            const SizedBox(height: 12),
            DropdownButtonFormField<Medium>(
              decoration: const InputDecoration(labelText: 'Medium of Instruction', border: OutlineInputBorder()),
              initialValue: _medium,
              items: [
                DropdownMenuItem(value: Medium.english, child: Text(TrilingualService.instance.getUIText('English'))),
                DropdownMenuItem(value: Medium.gujarati, child: Text(TrilingualService.instance.getUIText('ગુજરાતી (Gujarati)'))),
              ],
              onChanged: (v) => setState(() => _medium = v!),
            ),
            const SizedBox(height: 32),
            Card(
              child: ListTile(
                leading: Icon(Icons.school, size: 36, color: Colors.indigo),
                title: Text(TrilingualService.instance.getUIText('I am a Student')),
                subtitle: Text(TrilingualService.instance.getUIText('Practice topics with instant feedback and unlimited questions')),
                trailing: Icon(Icons.arrow_forward_ios),
                onTap: () => Navigator.of(context).push(MaterialPageRoute(
                  builder: (_) => StudentTopicScreen(board: _board, schoolClass: _schoolClass, medium: _medium),
                )),
              ),
            ),
            const SizedBox(height: 12),
            Card(
              child: ListTile(
                leading: Icon(Icons.assignment, size: 36, color: Colors.teal),
                title: Text(TrilingualService.instance.getUIText('I am a Teacher')),
                subtitle: Text(TrilingualService.instance.getUIText('Generate question papers & fully-worked answer keys')),
                trailing: Icon(Icons.arrow_forward_ios),
                onTap: () => Navigator.of(context).push(MaterialPageRoute(
                  builder: (_) => const TeacherPaperScreen(),
                )),
              ),
            ),
            const SizedBox(height: 32),
            Text(TrilingualService.instance.getUIText('Additional Resources'), style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            const SizedBox(height: 12),
            Text(TrilingualService.instance.getUIText('Class 12 - Accountancy Chapters'), style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
            const SizedBox(height: 12),
            Wrap(
              spacing: 8,
              runSpacing: 8,
              children: List.generate(13, (index) {
                final chNum = index + 1;
                return ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.indigo,
                    padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                  ),
                  child: Text('Ch $chNum', style: const TextStyle(color: Colors.white)),
                  onPressed: () {
                    Navigator.of(context, rootNavigator: true).push(
                      MaterialPageRoute(
                        builder: (context) => LearningEngineScreen(
                          moduleId: 'gseb_class12_accounts_ch$chNum',
                          title: 'Chapter',
                        ),
                      ),
                    );
                  },
                );
              }),
            ),
            const SizedBox(height: 12),
            Text(TrilingualService.instance.getUIText('Class 12 - Statistics Chapters'), style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
            const SizedBox(height: 12),
            Wrap(
              spacing: 8,
              runSpacing: 8,
              children: List.generate(2, (index) {
                final chNum = index + 1;
                return ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.deepPurple,
                    padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                  ),
                  child: Text('Stat Ch $chNum', style: const TextStyle(color: Colors.white)),
                  onPressed: () {
                    Navigator.of(context, rootNavigator: true).push(
                      MaterialPageRoute(
                        builder: (context) => LearningEngineScreen(
                          moduleId: 'gseb_class12_stats_ch$chNum',
                          title: 'Chapter',
                        ),
                      ),
                    );
                  },
                );
              }),
            ),
            const SizedBox(height: 24),
            ElevatedButton.icon(
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.teal,
                padding: const EdgeInsets.symmetric(vertical: 16),
              ),
              icon: Icon(Icons.menu_book, color: Colors.white),
              label: Text(TrilingualService.instance.getUIText('Accountancy Master Dictionary (209 Terms)'),
                style: TextStyle(fontSize: 16, color: Colors.white),
              ),
              onPressed: () {
                UniversalDictionaryPopup.show(context, '_');
              },
            ),
          ],
        ),
      ),
    ),
  );
  }
}
