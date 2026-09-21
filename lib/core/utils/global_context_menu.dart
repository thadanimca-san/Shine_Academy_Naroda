import 'package:flutter/material.dart';

class GlobalContextMenu {
  static TransitionBuilder get builder => (context, child) {
    // There is no standard global context menu builder in MaterialApp.
    return child!;
  };
}
