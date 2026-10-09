void main() {
  String text = "(a) \$\\cong\$";
  String cleanText = "";
  
  bool isBold = false;
  bool isItalic = false;

  for (int i = 0; i < text.length; i++) {
    String char = text[i];

    if (char == '\$') {
      bool isBlock = false;
      int j = i + 1;
      if (j < text.length && text[j] == '\$') {
         isBlock = true;
         j++;
      }
      int start = j;
      int end = -1;
      while (j < text.length) {
         if (text[j] == '\$') {
            if (isBlock && j + 1 < text.length && text[j+1] == '\$') {
                end = j;
                j += 2;
                break;
            } else if (!isBlock) {
                end = j;
                j++;
                break;
            }
         }
         j++;
      }
      
      if (end != -1) {
         String mathContent = text.substring(start, end);
         print("Found math: $mathContent");
         i = j - 1;
         continue;
      }
    }
  }
}
