import 'dart:math';

class AiService {
  static Future<String> getResponse(String userMessage, Map<String, dynamic> currentBlockContext) async {
    // Simulate network delay for realism
    await Future.delayed(const Duration(seconds: 1));

    String lowerMessage = userMessage.toLowerCase();
    
    // Check if the user is asking for a translation
    if (lowerMessage.contains('gujarati')) {
      return "Sure! In Gujarati, this concept is explained as: 'આ ખ્યાલ ખૂબ જ મહત્વપૂર્ણ છે. તે આપણને સમજાવે છે કે કેવી રીતે વસ્તુઓ કામ કરે છે.' (This is a simulated translation for your current topic).";
    }
    if (lowerMessage.contains('hindi')) {
      return "Absolutely! In Hindi: 'यह विषय बहुत महत्वपूर्ण है। यह हमें समझाता है कि चीजें कैसे काम करती हैं।' (Simulated translation).";
    }
    
    // Check if they want an example
    if (lowerMessage.contains('example') || lowerMessage.contains('real life')) {
      return "A great real-life example of this is when you are making tea! Just like the sugar dissolves into the water, the particles of matter are constantly moving and mixing together.";
    }

    // Check if they want it simplified
    if (lowerMessage.contains('simple') || lowerMessage.contains('easy') || lowerMessage.contains('hard')) {
      return "I completely understand! Let me break it down: \n\nThink of it like a game of Lego. The small Lego blocks are like atoms. When you stick them together, you get a bigger structure, which is the molecule! Does that make more sense?";
    }

    // Default context-aware response
    String blockTitle = currentBlockContext['title'] ?? 'this concept';
    
    final defaultResponses = [
      "That's a great question about $blockTitle! The key thing to remember here is that everything follows a specific set of rules in nature.",
      "Based on what you're reading about $blockTitle, a common misconception is that it works instantly, but it's actually a gradual process!",
      "I see you're studying $blockTitle. Have you tried drawing a small diagram? Visualizing it often helps lock the concept in your memory."
    ];

    return defaultResponses[Random().nextInt(defaultResponses.length)];
  }
}
