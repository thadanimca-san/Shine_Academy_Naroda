import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:go_router/go_router.dart';
import '../../foundation/theme/app_colors.dart';
import '../../foundation/theme/brand_app_bar.dart';
import '../../core/engine/local_content_manager.dart';
import '../../core/services/mentor_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class AdminSettingsScreen extends StatefulWidget {
  const AdminSettingsScreen({super.key});

  @override
  State<AdminSettingsScreen> createState() => _AdminSettingsScreenState();
}

class _AdminSettingsScreenState extends State<AdminSettingsScreen> {
  bool _isAuthenticated = false;
  final TextEditingController _pinController = TextEditingController();
  final String _masterPin = "9999"; // Secret PIN for Admin

  List<Mentor> _mentors = [];
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadMentors();
  }

  Future<void> _loadMentors() async {
    final mentors = await MentorService.getMentors();
    setState(() {
      _mentors = mentors;
      _isLoading = false;
    });
  }

  Future<void> _saveMentors() async {
    await MentorService.updateMentors(_mentors);
    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(TrilingualService.instance.getUIText('Mentor settings saved successfully. Please restart app to see changes.'))),
      );
    }
  }

  void _verifyPin() {
    if (_pinController.text == _masterPin) {
      setState(() {
        _isAuthenticated = true;
      });
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(TrilingualService.instance.getUIText('Incorrect PIN. Access Denied.'))),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    if (!_isAuthenticated) {
      return _buildPinScreen();
    }

    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Admin Settings')),
        backgroundColor: Colors.red[800],
        foregroundColor: Colors.white,
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : ListView(
              padding: const EdgeInsets.all(16),
              children: [
                Container(
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: Colors.red[50],
                    borderRadius: BorderRadius.circular(12),
                    border: Border.all(color: Colors.red[200]!),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        children: [
                          Icon(Icons.warning_amber_rounded, color: Colors.red[800]),
                          const SizedBox(width: 8),
                          Text(TrilingualService.instance.getUIText('RESTRICTED AREA'), style: GoogleFonts.poppins(fontWeight: FontWeight.bold, color: Colors.red[800])),
                        ],
                      ),
                      const SizedBox(height: 8),
                      Text(TrilingualService.instance.getUIText('Any changes made here will instantly reflect across the entire EduOS application for all students. Update asset paths or URLs for the mentor pictures below.'),
                        style: GoogleFonts.inter(fontSize: 14, color: Colors.red[900]),
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 24),
                Card(
                  elevation: 2,
                  child: ListTile(
                    leading: Icon(Icons.edit_document, color: Colors.indigo, size: 36),
                    title: Text(TrilingualService.instance.getUIText('EduOS Content Editor (Advanced)'), style: GoogleFonts.poppins(fontWeight: FontWeight.bold)),
                    subtitle: Text(TrilingualService.instance.getUIText('Visually edit chapters, dictionary terms, questions, and curriculum structure.')),
                    trailing: Icon(Icons.arrow_forward_ios),
                    onTap: () {
                      context.push('/content_editor');
                    },
                  ),
                ),
                const SizedBox(height: 16),
                Card(
                  elevation: 2,
                  child: ListTile(
                    leading: Icon(Icons.document_scanner, color: Colors.teal, size: 36),
                    title: Text(TrilingualService.instance.getUIText('Paper Digitization Studio (100% Accuracy)'), style: GoogleFonts.poppins(fontWeight: FontWeight.bold)),
                    subtitle: Text(TrilingualService.instance.getUIText('Digitize PDFs into error-free JSON without typos.')),
                    trailing: Icon(Icons.arrow_forward_ios),
                    onTap: () {
                      context.push('/digitization_studio');
                    },
                  ),
                ),
                const SizedBox(height: 16),
                Card(
                  elevation: 2,
                  child: ListTile(
                    leading: Icon(Icons.cleaning_services, color: Colors.orange, size: 36),
                    title: Text(TrilingualService.instance.getUIText('Wipe Content Cache (Fixes Missing Data)'), style: GoogleFonts.poppins(fontWeight: FontWeight.bold)),
                    subtitle: Text(TrilingualService.instance.getUIText('Deletes all cached JSON files so the app pulls fresh from assets.')),
                    trailing: Icon(Icons.delete_forever, color: Colors.red),
                    onTap: () async {
                      await LocalContentManager.instance.wipeAllCache();
                      if (context.mounted) {
                        ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(TrilingualService.instance.getUIText('Content Cache Wiped! Restarting app is recommended.'))));
                      }
                    },
                  ),
                ),
                const SizedBox(height: 24),
                Text(TrilingualService.instance.getUIText('Manage Expert Mentors'), style: GoogleFonts.poppins(fontSize: 20, fontWeight: FontWeight.bold)),
                const SizedBox(height: 16),
                ..._mentors.asMap().entries.map((entry) {
                  int idx = entry.key;
                  Mentor mentor = entry.value;
                  return _buildMentorEditor(idx, mentor);
                }),
                const SizedBox(height: 24),
                ElevatedButton(
                  onPressed: _saveMentors,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.red[800],
                    foregroundColor: Colors.white,
                    padding: const EdgeInsets.symmetric(vertical: 16),
                  ),
                  child: Text(TrilingualService.instance.getUIText('SAVE ALL CHANGES'), style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                ),
                const SizedBox(height: 40),
              ],
            ),
    );
  }

  Widget _buildMentorEditor(int index, Mentor mentor) {
    return Card(
      margin: const EdgeInsets.only(bottom: 16),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Mentor Slot: ${mentor.id.toUpperCase()}', style: GoogleFonts.poppins(fontWeight: FontWeight.bold, color: Colors.indigo)),
            const SizedBox(height: 12),
            TextField(
              decoration: const InputDecoration(labelText: 'Display Name', border: OutlineInputBorder()),
              controller: TextEditingController(text: mentor.name)..selection = TextSelection.collapsed(offset: mentor.name.length),
              onChanged: (val) => _updateMentor(index, name: val),
            ),
            const SizedBox(height: 12),
            TextField(
              decoration: const InputDecoration(labelText: 'Qualification (e.g., MSc Chemistry)', border: OutlineInputBorder()),
              controller: TextEditingController(text: mentor.qualification)..selection = TextSelection.collapsed(offset: mentor.qualification.length),
              onChanged: (val) => _updateMentor(index, qualification: val),
            ),
            const SizedBox(height: 12),
            TextField(
              decoration: const InputDecoration(labelText: 'Role', border: OutlineInputBorder()),
              controller: TextEditingController(text: mentor.role)..selection = TextSelection.collapsed(offset: mentor.role.length),
              onChanged: (val) => _updateMentor(index, role: val),
            ),
            const SizedBox(height: 12),
            TextField(
              decoration: const InputDecoration(labelText: 'Image Path (e.g., assets/mentors/principal.jpg)', border: OutlineInputBorder()),
              controller: TextEditingController(text: mentor.imagePath)..selection = TextSelection.collapsed(offset: mentor.imagePath.length),
              onChanged: (val) => _updateMentor(index, imagePath: val),
            ),
          ],
        ),
      ),
    );
  }

  void _updateMentor(int index, {String? name, String? qualification, String? role, String? imagePath}) {
    final old = _mentors[index];
    _mentors[index] = Mentor(
      id: old.id,
      name: name ?? old.name,
      qualification: qualification ?? old.qualification,
      role: role ?? old.role,
      imagePath: imagePath ?? old.imagePath,
    );
  }

  Widget _buildPinScreen() {
    return Scaffold(
      appBar: AppBar(title: Text(TrilingualService.instance.getUIText('Admin Access'))),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(32.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(Icons.lock, size: 64, color: Colors.grey),
              const SizedBox(height: 24),
              Text(TrilingualService.instance.getUIText('Enter Administrator PIN'), style: GoogleFonts.poppins(fontSize: 20, fontWeight: FontWeight.bold)),
              const SizedBox(height: 16),
              TextField(
                controller: _pinController,
                obscureText: true,
                keyboardType: TextInputType.number,
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 24, letterSpacing: 8),
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  hintText: '****',
                ),
              ),
              const SizedBox(height: 24),
              ElevatedButton(
                onPressed: _verifyPin,
                style: ElevatedButton.styleFrom(minimumSize: const Size(double.infinity, 50)),
                child: Text(TrilingualService.instance.getUIText('UNLOCK SETTINGS')),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
