import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../foundation/theme/app_colors.dart';
import 'ai_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class AiTutorScreen extends StatefulWidget {
  final Map<String, dynamic> blockContext;

  const AiTutorScreen({super.key, required this.blockContext});

  @override
  State<AiTutorScreen> createState() => _AiTutorScreenState();
}

class _AiTutorScreenState extends State<AiTutorScreen> {
  final TextEditingController _controller = TextEditingController();
  final List<Map<String, dynamic>> _messages = [];
  final ScrollController _scrollController = ScrollController();
  bool _isTyping = false;

  @override
  void initState() {
    super.initState();
    // Initial greeting
    String title = widget.blockContext['title'] ?? 'this topic';
    _messages.add({
      'isUser': false,
      'text': "Hi! I'm your personal AI Tutor. I see you're studying '$title'. How can I help you today?"
    });
  }

  void _sendMessage(String text) async {
    if (text.trim().isEmpty) return;

    setState(() {
      _messages.add({'isUser': true, 'text': text});
      _isTyping = true;
    });
    _controller.clear();
    _scrollToBottom();

    String response = await AiService.getResponse(text, widget.blockContext);
    
    if (mounted) {
      setState(() {
        _isTyping = false;
        _messages.add({'isUser': false, 'text': response});
      });
      _scrollToBottom();
    }
  }
  
  void _scrollToBottom() {
    Future.delayed(const Duration(milliseconds: 100), () {
      if (_scrollController.hasClients) {
        _scrollController.animateTo(
          _scrollController.position.maxScrollExtent,
          duration: const Duration(milliseconds: 300),
          curve: Curves.easeOut,
        );
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: AppColors.background,
        borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
      ),
      child: Column(
        children: [
          // Header
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Row(
                  children: [
                    CircleAvatar(
                      backgroundColor: Colors.purple.shade100,
                      child: Icon(Icons.auto_awesome, color: Colors.purple.shade700),
                    ),
                    const SizedBox(width: 12),
                    Text(TrilingualService.instance.getUIText('AI Tutor'),
                      style: GoogleFonts.poppins(fontSize: 18, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
                    ),
                  ],
                ),
                IconButton(
                  icon: Icon(Icons.close),
                  onPressed: () => Navigator.pop(context),
                )
              ],
            ),
          ),
          
          // Chat Messages
          Expanded(
            child: ListView.builder(
              controller: _scrollController,
              padding: const EdgeInsets.all(16),
              itemCount: _messages.length + (_isTyping ? 1 : 0),
              itemBuilder: (context, index) {
                if (index == _messages.length && _isTyping) {
                  return _buildTypingIndicator();
                }
                
                final msg = _messages[index];
                return _buildMessageBubble(msg['text'], msg['isUser']);
              },
            ),
          ),

          // Quick Action Chips
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            padding: const EdgeInsets.symmetric(horizontal: 16),
            child: Row(
              children: [
                _buildActionChip("Simplify this"),
                const SizedBox(width: 8),
                _buildActionChip("Gujarati"),
                const SizedBox(width: 8),
                _buildActionChip("Hindi"),
                const SizedBox(width: 8),
                _buildActionChip("Real life example"),
              ],
            ),
          ),
          const SizedBox(height: 8),

          // Input Field
          Container(
            padding: EdgeInsets.only(
              left: 16,
              right: 16,
              top: 12,
              bottom: MediaQuery.of(context).viewInsets.bottom + 12,
            ),
            color: Colors.white,
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    decoration: InputDecoration(
                      hintText: 'Ask your doubt...',
                      hintStyle: GoogleFonts.inter(color: Colors.grey),
                      filled: true,
                      fillColor: Colors.grey.shade100,
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(24),
                        borderSide: BorderSide.none,
                      ),
                      contentPadding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                    ),
                    onSubmitted: _sendMessage,
                  ),
                ),
                const SizedBox(width: 8),
                CircleAvatar(
                  backgroundColor: AppColors.primary,
                  child: IconButton(
                    icon: Icon(Icons.send, color: Colors.white, size: 20),
                    onPressed: () => _sendMessage(_controller.text),
                  ),
                ),
              ],
            ),
          )
        ],
      ),
    );
  }

  Widget _buildActionChip(String label) {
    return ActionChip(
      label: Text(label, style: GoogleFonts.inter(fontSize: 13, color: Colors.purple.shade700, fontWeight: FontWeight.w600)),
      backgroundColor: Colors.purple.shade50,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16), side: BorderSide(color: Colors.purple.shade200)),
      onPressed: () => _sendMessage(label),
    );
  }

  Widget _buildMessageBubble(String text, bool isUser) {
    return Align(
      alignment: isUser ? Alignment.centerRight : Alignment.centerLeft,
      child: Container(
        margin: const EdgeInsets.only(bottom: 12),
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        constraints: BoxConstraints(maxWidth: MediaQuery.of(context).size.width * 0.75),
        decoration: BoxDecoration(
          color: isUser ? AppColors.primary : Colors.white,
          borderRadius: BorderRadius.only(
            topLeft: const Radius.circular(16),
            topRight: const Radius.circular(16),
            bottomLeft: Radius.circular(isUser ? 16 : 0),
            bottomRight: Radius.circular(isUser ? 0 : 16),
          ),
          boxShadow: [
            if (!isUser)
              BoxShadow(color: Colors.grey.withValues(alpha: 0.1), blurRadius: 5, offset: const Offset(0, 2))
          ],
        ),
        child: Text(
          text,
          style: GoogleFonts.inter(
            color: isUser ? Colors.white : AppColors.textPrimary,
            fontSize: 15,
            height: 1.4
          ),
        ),
      ),
    );
  }

  Widget _buildTypingIndicator() {
    return Align(
      alignment: Alignment.centerLeft,
      child: Container(
        margin: const EdgeInsets.only(bottom: 12),
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: const BorderRadius.only(
            topLeft: Radius.circular(16),
            topRight: Radius.circular(16),
            bottomRight: Radius.circular(16),
          ),
          boxShadow: [BoxShadow(color: Colors.grey.withValues(alpha: 0.1), blurRadius: 5, offset: const Offset(0, 2))],
        ),
        child: Text(TrilingualService.instance.getUIText('AI is thinking...'), style: GoogleFonts.inter(color: Colors.grey, fontStyle: FontStyle.italic)),
      ),
    );
  }
}
