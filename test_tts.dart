void main() {
  String text = "A small bushy-tailed rodent.";
  String fullTtsText = "Squirrel. A small bushy-tailed rodent.";
  String progressText = "Squirrel. A small bushy-tailed rodent.";
  
  String targetText = fullTtsText;
  
  print("Condition 1: ${progressText.isEmpty}");
  print("Condition 2: ${!targetText.toLowerCase().contains(progressText.toLowerCase().trim())}");
  
  int offsetAdjustment = fullTtsText.indexOf(text);
  print("offsetAdjustment: $offsetAdjustment");
  
  // Test reading the word "small"
  // "Squirrel. A small bushy-tailed rodent."
  // 012345678901234567
  // "small" starts at index 12, ends at 17
  int startOffset = 12;
  int endOffset = 17;
  
  int start = startOffset - offsetAdjustment;
  int end = endOffset - offsetAdjustment;
  print("start: $start, end: $end");
  print("text length: ${text.length}");
  
  if (start < 0 || end > text.length || start >= end) {
    print("OUT OF BOUNDS!");
  } else {
    print("Highlighted: '${text.substring(start, end)}'");
  }
}
