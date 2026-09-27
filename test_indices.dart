void main() {
  int blocksLength = 14;
  bool showHint = true;
  bool deoNotEmpty = true;
  bool showDeo = false;
  
  int itemCount = blocksLength + (showHint ? 1 : 0) + (deoNotEmpty && !showDeo ? 1 : 0);
  print("Item Count: $itemCount");
  
  int gatewayIndex = blocksLength + (showHint ? 1 : 0);
  
  for (int index = 0; index < itemCount; index++) {
    if (showHint && index == 0) {
      print("Index $index -> Hint");
      continue;
    }
    
    if (deoNotEmpty && !showDeo && index == gatewayIndex) {
      print("Index $index -> Gateway");
      continue;
    }
    
    int actualIndex = showHint ? index - 1 : index;
    print("Index $index -> Block $actualIndex");
  }
}
