import 'package:flutter/foundation.dart';

enum ModerationStatus { pending, approved, rejected }

class CommunitySubmission {
  final String id;
  final String authorName;
  final String category; // story, joke, review, tongue_twister
  final String content;
  final ModerationStatus status;

  CommunitySubmission({
    required this.id,
    required this.authorName,
    required this.category,
    required this.content,
    this.status = ModerationStatus.pending,
  });
}

class ModerationService {
  static final ModerationService instance = ModerationService._internal();
  ModerationService._internal();

  // In a real app, this would be a secure backend database (e.g., Firebase Firestore).
  // For Phase 2 Beta testing, we store it in memory.
  final List<CommunitySubmission> _submissions = [];

  Future<void> submitReview({
    required String authorName,
    required String category,
    required String content,
  }) async {
    // Simulate network delay
    await Future.delayed(const Duration(seconds: 1));

    final newSubmission = CommunitySubmission(
      id: DateTime.now().millisecondsSinceEpoch.toString(),
      authorName: authorName,
      category: category,
      content: content,
      status: ModerationStatus.pending, // Strict rule: Everything is pending by default!
    );

    _submissions.add(newSubmission);
    debugPrint("New Submission Received! Held in PENDING state for moderation.");
    debugPrint("Content: $content");
  }

  // Admin function to approve honest/positive reviews
  void approveSubmission(String id) {
    final index = _submissions.indexWhere((s) => s.id == id);
    if (index != -1) {
      final sub = _submissions[index];
      _submissions[index] = CommunitySubmission(
        id: sub.id,
        authorName: sub.authorName,
        category: sub.category,
        content: sub.content,
        status: ModerationStatus.approved,
      );
    }
  }

  // Admin function to instantly delete faltu/negative reviews
  void rejectAndPurgeSubmission(String id) {
    _submissions.removeWhere((s) => s.id == id);
    debugPrint("Faltu/Negative review permanently deleted from servers.");
  }

  List<CommunitySubmission> get approvedSubmissions => 
      _submissions.where((s) => s.status == ModerationStatus.approved).toList();

  List<CommunitySubmission> get pendingSubmissions => 
      _submissions.where((s) => s.status == ModerationStatus.pending).toList();
}
