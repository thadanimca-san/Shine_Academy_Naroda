import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class ExampleWidget extends StatelessWidget {
  final Map<String, dynamic> data;

  const ExampleWidget({super.key, required this.data});

  @override
  Widget build(BuildContext context) {
    final lang = 'en';
    final title = data['title'] ?? '';
    final problemMap = data['problem'] as Map<String, dynamic>? ?? {};
    final problem = problemMap[lang] ?? problemMap['en'] ?? '';
    final steps = data['steps'] as List<dynamic>? ?? [];
    final finalAnswer = data['final_answer'] ?? '';

    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: Colors.orange[50],
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.orange[200]!, width: 1.5),
        boxShadow: [
          BoxShadow(
            color: Colors.orange.withValues(alpha: 0.1),
            blurRadius: 15,
            offset: const Offset(0, 8),
          )
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                padding: const EdgeInsets.all(8),
                decoration: BoxDecoration(
                  color: Colors.orange[100],
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Icon(Icons.lightbulb_rounded, color: Colors.orange),
              ),
              const SizedBox(width: 16),
              Expanded(
                child: Text(
                  title,
                  style: GoogleFonts.poppins(
                    fontSize: 22,
                    fontWeight: FontWeight.w700,
                    color: Colors.orange[900],
                    letterSpacing: -0.5,
                  ).adaptToLanguage(),
                ),
              ),
            ],
          ),
          const SizedBox(height: 16),
          Text(
            problem,
            style: GoogleFonts.inter(
              fontSize: 16,
              fontWeight: FontWeight.w500,
              color: Theme.of(context).colorScheme.onSurface,
            ).adaptToLanguage(),
          ),
          const SizedBox(height: 16),
          const Divider(),
          const SizedBox(height: 8),
          Text(TrilingualService.instance.getUIText("Solution Steps:"), style: GoogleFonts.poppins(fontWeight: FontWeight.bold)),
          const SizedBox(height: 8),
          ...steps.map((stepData) {
            return Padding(
              padding: const EdgeInsets.only(bottom: 12),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  CircleAvatar(
                    radius: 12,
                    backgroundColor: Colors.orange[200],
                    child: Text(
                      "${stepData['step']}",
                      style: TextStyle(fontSize: 12, color: Theme.of(context).colorScheme.onSurface),
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          stepData['text'] ?? '',
                          style: GoogleFonts.inter(fontSize: 14, color: Theme.of(context).colorScheme.onSurfaceVariant).adaptToLanguage(),
                        ),
                          if (stepData['calculation'] != null)
                            Text(
                              stepData['calculation'],
                              style: GoogleFonts.robotoMono(fontSize: 14, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface).adaptToLanguage(),
                            ),
                      ],
                    ),
                  ),
                ],
              ),
            );
          }),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              gradient: LinearGradient(
                colors: [Colors.orange[100]!, Colors.orange[50]!],
              ),
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: Colors.orange[300]!),
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(TrilingualService.instance.getUIText("Final Answer:"), style: GoogleFonts.poppins(fontWeight: FontWeight.bold, fontSize: 16, color: Colors.orange[900])),
                Text(
                  finalAnswer,
                  style: GoogleFonts.robotoMono(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.green[800]).adaptToLanguage(),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
