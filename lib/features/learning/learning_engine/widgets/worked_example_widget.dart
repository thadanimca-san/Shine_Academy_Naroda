import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../../core/widgets/presentation_builder.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class WorkedExampleWidget extends StatelessWidget {
  final Map<String, dynamic> data;

  const WorkedExampleWidget({super.key, required this.data});

  @override
  Widget build(BuildContext context) {
    final payload = data['data'] ?? data;
    final title = payload['title'] ?? 'Worked Example';
    final problem = payload['problem'] ?? '';
    final given = payload['given'];
    final formula = payload['formula'];
    final steps = payload['steps'] as List<dynamic>? ?? [];
    final answer = payload['answer'];

    return PresentationBuilder(
      builder: (context, scale) {
        return Container(
          margin: const EdgeInsets.only(bottom: 24),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(20),
            border: Border.all(color: Colors.teal.shade200, width: 2),
            boxShadow: [
              BoxShadow(
                color: Colors.teal.withValues(alpha: 0.1),
                blurRadius: 15,
                offset: const Offset(0, 8),
              )
            ],
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              // Header
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                decoration: BoxDecoration(
                  color: Colors.teal.shade50,
                  borderRadius: const BorderRadius.vertical(top: Radius.circular(18)),
                  border: Border(bottom: BorderSide(color: Colors.teal.shade200, width: 2)),
                ),
                child: Row(
                  children: [
                    Icon(Icons.lightbulb_outline, color: Colors.teal.shade700),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Text(
                        title,
                        style: GoogleFonts.poppins(
                          fontSize: 18 * scale,
                          fontWeight: FontWeight.bold,
                          color: Colors.teal.shade900,
                        ),
                      ),
                    ),
                  ],
                ),
              ),

              Padding(
                padding: const EdgeInsets.all(20),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Problem Statement
                    if (problem.isNotEmpty) ...[
                      Text(
                        problem,
                        style: GoogleFonts.inter(
                          fontSize: 16 * scale,
                          fontWeight: FontWeight.bold,
                          color: Theme.of(context).colorScheme.onSurface,
                        ),
                      ),
                      const SizedBox(height: 16),
                      Divider(color: Colors.grey.shade200),
                      const SizedBox(height: 16),
                    ],

                    // Given Information
                    if (given != null && given.toString().isNotEmpty) ...[
                      _buildSectionLabel('GIVEN:', scale),
                      const SizedBox(height: 4),
                      Text(
                        given.toString(),
                        style: GoogleFonts.inter(fontSize: 15 * scale, color: Theme.of(context).colorScheme.onSurface),
                      ),
                      const SizedBox(height: 16),
                    ],

                    // Formula Used
                    if (formula != null && formula.toString().isNotEmpty) ...[
                      _buildSectionLabel('FORMULA:', scale),
                      const SizedBox(height: 4),
                      Container(
                        padding: const EdgeInsets.all(12),
                        decoration: BoxDecoration(
                          color: Colors.blue.shade50,
                          borderRadius: BorderRadius.circular(8),
                          border: Border.all(color: Colors.blue.shade100),
                        ),
                        child: Text(
                          formula.toString(),
                          style: GoogleFonts.firaCode(fontSize: 14 * scale, color: Colors.blue.shade900),
                        ),
                      ),
                      const SizedBox(height: 16),
                    ],

                    // Step-by-Step Solution
                    if (steps.isNotEmpty) ...[
                      _buildSectionLabel('SOLUTION:', scale),
                      const SizedBox(height: 8),
                      ...steps.asMap().entries.map((entry) {
                        return Padding(
                          padding: const EdgeInsets.only(bottom: 12),
                          child: Row(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Container(
                                width: 24 * scale,
                                height: 24 * scale,
                                decoration: BoxDecoration(
                                  color: Colors.teal.shade100,
                                  shape: BoxShape.circle,
                                ),
                                child: Center(
                                  child: Text(
                                    '\${entry.key + 1}',
                                    style: GoogleFonts.poppins(
                                      fontSize: 12 * scale,
                                      fontWeight: FontWeight.bold,
                                      color: Colors.teal.shade900,
                                    ),
                                  ),
                                ),
                              ),
                              const SizedBox(width: 12),
                              Expanded(
                                child: Padding(
                                  padding: EdgeInsets.only(top: 2 * scale),
                                  child: Text(
                                    entry.value.toString(),
                                    style: GoogleFonts.inter(
                                      fontSize: 15 * scale,
                                      color: Theme.of(context).colorScheme.onSurface,
                                      height: 1.5,
                                    ),
                                  ),
                                ),
                              ),
                            ],
                          ),
                        );
                      }),
                      const SizedBox(height: 12),
                    ],

                    // Final Answer
                    if (answer != null && answer.toString().isNotEmpty) ...[
                      Divider(color: Colors.grey.shade200),
                      const SizedBox(height: 16),
                      Container(
                        width: double.infinity,
                        padding: const EdgeInsets.all(16),
                        decoration: BoxDecoration(
                          color: Colors.green.shade50,
                          borderRadius: BorderRadius.circular(12),
                          border: Border.all(color: Colors.green.shade200),
                        ),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(TrilingualService.instance.getUIText('FINAL ANSWER'),
                              style: GoogleFonts.poppins(
                                fontSize: 12 * scale,
                                fontWeight: FontWeight.bold,
                                color: Colors.green.shade800,
                                letterSpacing: 1,
                              ),
                            ),
                            const SizedBox(height: 4),
                            Text(
                              answer.toString(),
                              style: GoogleFonts.inter(
                                fontSize: 16 * scale,
                                fontWeight: FontWeight.bold,
                                color: Colors.green.shade900,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ],
                ),
              ),
            ],
          ),
        );
      },
    );
  }

  Widget _buildSectionLabel(String text, double scale) {
    return Text(
      text,
      style: GoogleFonts.poppins(
        fontSize: 12 * scale,
        fontWeight: FontWeight.bold,
        color: Colors.grey.shade500,
        letterSpacing: 1.2,
      ),
    );
  }
}
