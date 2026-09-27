void main() {
  String raw = "ખોરાક";
  final String cleaned = raw
      .replaceAll(RegExp(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$'), '')
      .toLowerCase()
      .trim();
  print("Raw: '$raw'");
  print("Cleaned: '$cleaned'");
}
