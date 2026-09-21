import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../foundation/theme/app_colors.dart';
import '../services/moderation_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class ReviewSubmissionDialog extends StatefulWidget {
  const ReviewSubmissionDialog({super.key});

  @override
  State<ReviewSubmissionDialog> createState() => _ReviewSubmissionDialogState();
}

class _ReviewSubmissionDialogState extends State<ReviewSubmissionDialog> {
  final _contentController = TextEditingController();
  final _authorController = TextEditingController();
  String _selectedCategory = 'Review / Spotlight';
  bool _isSubmitting = false;

  final List<String> _categories = [
    'Review / Spotlight',
    'Short Story',
    'Poem',
    'Joke',
    'Tongue Twister'
  ];

  Future<void> _submit() async {
    if (_contentController.text.trim().isEmpty || _authorController.text.trim().isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(TrilingualService.instance.getUIText("Please fill all fields!"))),
      );
      return;
    }

    setState(() => _isSubmitting = true);

    await ModerationService.instance.submitReview(
      authorName: _authorController.text.trim(),
      category: _selectedCategory,
      content: _contentController.text.trim(),
    );

    if (!mounted) return;
    setState(() => _isSubmitting = false);

    Navigator.of(context).pop();
    
    // Show strict moderation message to the student
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text(TrilingualService.instance.getUIText("Submitted Successfully! 🎉")),
        content: Text(TrilingualService.instance.getUIText("Thank you for your submission!\n\n""Shine Academy maintains a strictly positive and inspiring learning environment. " 
          "Your submission has been sent to our teachers for moderation. " 
          "Once verified as honest and constructive, it will be published in the Community Spotlight for everyone to see!")
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(),
            child: Text(TrilingualService.instance.getUIText("OK, Got it!"), style: TextStyle(fontWeight: FontWeight.bold)),
          )
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Dialog(
      backgroundColor: Colors.white,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
      child: Padding(
        padding: const EdgeInsets.all(24.0),
        child: SingleChildScrollView(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Text(TrilingualService.instance.getUIText("Submit Your Spotlight"),
                textAlign: TextAlign.center,
                style: GoogleFonts.poppins(
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                  color: AppColors.primary,
                ),
              ),
              const SizedBox(height: 8),
              Text(TrilingualService.instance.getUIText("Share an honest review, an inspiring story, or a fun joke with the Shine Academy community!"),
                textAlign: TextAlign.center,
                style: TextStyle(color: Colors.grey.shade600, fontSize: 14),
              ),
              const SizedBox(height: 24),
              TextField(
                controller: _authorController,
                decoration: InputDecoration(
                  labelText: "Your Name & Class (e.g. Rahul, Class 5)",
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                  prefixIcon: Icon(Icons.person),
                ),
              ),
              const SizedBox(height: 16),
              DropdownButtonFormField<String>(
                value: _selectedCategory,
                decoration: InputDecoration(
                  labelText: "Category",
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                  prefixIcon: Icon(Icons.category),
                ),
                items: _categories.map((c) => DropdownMenuItem(value: c, child: Text(c))).toList(),
                onChanged: (val) => setState(() => _selectedCategory = val!),
              ),
              const SizedBox(height: 16),
              TextField(
                controller: _contentController,
                maxLines: 4,
                decoration: InputDecoration(
                  labelText: "Write your honest review or story here...",
                  alignLabelWithHint: true,
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                ),
              ),
              const SizedBox(height: 24),
              
              // Moderation Warning Banner
              Container(
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: Colors.orange.shade50,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: Colors.orange.shade200),
                ),
                child: Row(
                  children: [
                    Icon(Icons.security, color: Colors.orange),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Text(TrilingualService.instance.getUIText("Strict Moderation: Only positive, constructive, and clean content will be approved."),
                        style: TextStyle(color: Colors.orange.shade900, fontSize: 12, fontWeight: FontWeight.bold),
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 24),

              if (_isSubmitting)
                const Center(child: CircularProgressIndicator())
              else
                ElevatedButton(
                  onPressed: _submit,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: AppColors.primary,
                    foregroundColor: Colors.white,
                    padding: const EdgeInsets.symmetric(vertical: 16),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(30)),
                  ),
                  child: Text(TrilingualService.instance.getUIText("Submit for Review"), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                ),
              const SizedBox(height: 12),
              TextButton(
                onPressed: () => Navigator.of(context).pop(),
                child: Text(TrilingualService.instance.getUIText("Cancel")),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
