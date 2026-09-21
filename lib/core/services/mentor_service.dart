import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';

class Mentor {
  final String id;
  final String name;
  final String qualification;
  final String role;
  final String imagePath; // Can be a local asset path or an absolute file path

  Mentor({
    required this.id,
    required this.name,
    required this.qualification,
    required this.role,
    required this.imagePath,
  });

  Map<String, dynamic> toJson() => {
        'id': id,
        'name': name,
        'qualification': qualification,
        'role': role,
        'imagePath': imagePath,
      };

  factory Mentor.fromJson(Map<String, dynamic> json) => Mentor(
        id: json['id'],
        name: json['name'],
        qualification: json['qualification'],
        role: json['role'],
        imagePath: json['imagePath'],
      );
}

class MentorService {
  static const String _storageKey = 'shine_mentors';

  // Default Fallback Data (before Admin sets custom photos)
  static final List<Mentor> _defaultMentors = [
    Mentor(
      id: 'govind',
      name: 'Govind',
      qualification: 'Co-Founder',
      role: 'Principal Mentor',
      imagePath: 'assets/mentors/govind.jpg',
    ),
    Mentor(
      id: 'kajal',
      name: 'Kajal',
      qualification: 'Co-Founder',
      role: 'Head of Pedagogy',
      imagePath: 'assets/mentors/kajal.jpg',
    ),
    Mentor(
      id: 'kashish',
      name: 'Kashish',
      qualification: 'Co-Founder',
      role: 'Head of Operations',
      imagePath: 'assets/mentors/kashish.jpg',
    ),
    Mentor(
      id: 'vishal',
      name: 'Vishal',
      qualification: 'Co-Founder',
      role: 'Head of Technology',
      imagePath: 'assets/mentors/vishal.jpg',
    ),
  ];

  static Future<List<Mentor>> getMentors() async {
    final prefs = await SharedPreferences.getInstance();
    final jsonString = prefs.getString(_storageKey);

    if (jsonString != null) {
      try {
        final List<dynamic> decoded = json.decode(jsonString);
        return decoded.map((e) => Mentor.fromJson(e)).toList();
      } catch (e) {
        // Fallback on error
        return _defaultMentors;
      }
    }
    return _defaultMentors;
  }

  static Future<void> updateMentors(List<Mentor> mentors) async {
    final prefs = await SharedPreferences.getInstance();
    final List<Map<String, dynamic>> jsonList = mentors.map((m) => m.toJson()).toList();
    await prefs.setString(_storageKey, json.encode(jsonList));
  }
}
