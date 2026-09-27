void main() {
  String text = "A small bushy-tailed rodent.";
  String fullTtsText = "Squirrel. A small bushy-tailed rodent.";
  String targetText = fullTtsText;
  
  // Case A: Engine chunks by sentence. Currently reading the word "small" in the 2nd chunk.
  String progressText = "A small bushy-tailed rodent."; // Engine stripped "Squirrel. "
  int startOffset = 2; // "small" starts at index 2 in progressText
  int endOffset = 7;
  
  int chunkOffsetInFull = targetText.toLowerCase().indexOf(progressText.toLowerCase().trim());
  print("chunkOffsetInFull: $chunkOffsetInFull");
  
  if (chunkOffsetInFull != -1) {
    int globalStart = chunkOffsetInFull + startOffset;
    int globalEnd = chunkOffsetInFull + endOffset;
    
    int offsetAdjustment = 0;
    if (fullTtsText != null) {
      offsetAdjustment = fullTtsText.indexOf(text);
    }
    
    int start = globalStart - offsetAdjustment;
    int end = globalEnd - offsetAdjustment;
    
    print("start: $start, end: $end");
    if (start >= 0 && end <= text.length && start < end) {
      print("Highlighted A: '${text.substring(start, end)}'");
    }
  }
  
  // Case B: Engine sends full text
  progressText = "Squirrel. A small bushy-tailed rodent.";
  startOffset = 12; // "small" in the full string
  endOffset = 17;
  
  chunkOffsetInFull = targetText.toLowerCase().indexOf(progressText.toLowerCase().trim());
  if (chunkOffsetInFull != -1) {
    int globalStart = chunkOffsetInFull + startOffset;
    int globalEnd = chunkOffsetInFull + endOffset;
    
    int offsetAdjustment = fullTtsText.indexOf(text);
    int start = globalStart - offsetAdjustment;
    int end = globalEnd - offsetAdjustment;
    print("start: $start, end: $end");
    if (start >= 0 && end <= text.length && start < end) {
      print("Highlighted B: '${text.substring(start, end)}'");
    }
  }
}
