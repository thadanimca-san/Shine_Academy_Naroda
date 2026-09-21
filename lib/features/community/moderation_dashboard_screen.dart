import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../foundation/theme/app_colors.dart';
import '../../../foundation/theme/brand_app_bar.dart';
import 'services/moderation_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class ModerationDashboardScreen extends StatefulWidget {
  const ModerationDashboardScreen({super.key});

  @override
  State<ModerationDashboardScreen> createState() => _ModerationDashboardScreenState();
}

class _ModerationDashboardScreenState extends State<ModerationDashboardScreen> {
  void _approve(String id) {
    setState(() {
      ModerationService.instance.approveSubmission(id);
    });
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text(TrilingualService.instance.getUIText("Approved! Sent to public Community Spotlight.")), backgroundColor: Colors.green),
    );
  }

  void _reject(String id) {
    setState(() {
      ModerationService.instance.rejectAndPurgeSubmission(id);
    });
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text(TrilingualService.instance.getUIText("Rejected & Deleted permanently.")), backgroundColor: Colors.red),
    );
  }

  @override
  Widget build(BuildContext context) {
    final pending = ModerationService.instance.pendingSubmissions;
    final approved = ModerationService.instance.approvedSubmissions;

    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: const BrandAppBar(title: 'Admin: Moderation Panel'),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text("Pending Reviews (${pending.length})", style: GoogleFonts.inter(fontSize: 20, fontWeight: FontWeight.bold)),
            const SizedBox(height: 12),
            if (pending.isEmpty)
              Text(TrilingualService.instance.getUIText("No pending reviews to moderate."), style: TextStyle(color: Colors.grey))
            else
              ...pending.map((sub) => Card(
                color: Colors.orange.shade50,
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(sub.authorName, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                          Chip(label: Text(sub.category), backgroundColor: Colors.white),
                        ],
                      ),
                      const SizedBox(height: 12),
                      Text(sub.content, style: TextStyle(fontSize: 16)),
                      const SizedBox(height: 16),
                      Row(
                        children: [
                          Expanded(
                            child: ElevatedButton.icon(
                              onPressed: () => _approve(sub.id),
                              icon: Icon(Icons.check),
                              label: Text(TrilingualService.instance.getUIText("Approve")),
                              style: ElevatedButton.styleFrom(backgroundColor: Colors.green, foregroundColor: Colors.white),
                            ),
                          ),
                          const SizedBox(width: 16),
                          Expanded(
                            child: ElevatedButton.icon(
                              onPressed: () => _reject(sub.id),
                              icon: Icon(Icons.delete),
                              label: Text(TrilingualService.instance.getUIText("Reject & Delete")),
                              style: ElevatedButton.styleFrom(backgroundColor: Colors.red, foregroundColor: Colors.white),
                            ),
                          ),
                        ],
                      )
                    ],
                  ),
                ),
              )),

            const SizedBox(height: 40),
            
            Text("Public Spotlight Board (${approved.length})", style: GoogleFonts.inter(fontSize: 20, fontWeight: FontWeight.bold)),
            const SizedBox(height: 12),
            if (approved.isEmpty)
              Text(TrilingualService.instance.getUIText("No approved reviews yet."), style: TextStyle(color: Colors.grey))
            else
              ...approved.map((sub) => Card(
                color: Colors.white,
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(sub.authorName, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                          Chip(label: Text(sub.category), backgroundColor: AppColors.primary.withOpacity(0.1)),
                        ],
                      ),
                      const SizedBox(height: 12),
                      Text(sub.content, style: TextStyle(fontSize: 16)),
                    ],
                  ),
                ),
              )),
          ],
        ),
      ),
    );
  }
}
