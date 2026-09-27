import re

with open('lib/features/dictionary/dictionary_popup.dart', 'r') as f:
    content = f.read()

# Replace show() and remove StatefulWidget classes
idx = content.find('  static void show(BuildContext context, String termId) {')
if idx != -1:
    content = content[:idx] + """  static void show(BuildContext context, String termId) {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) {
        return FutureBuilder<_LookupResult>(
          future: _lookup(termId),
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return _buildContainer(
                context,
                const Center(
                  child: CircularProgressIndicator(color: AppColors.primary),
                ),
              );
            }

            final result = snapshot.data!;
            if (result.found) {
              return _buildContainer(
                context,
                _buildTermDetail(context, result.term!),
              );
            } else {
              return _buildContainer(
                context,
                _buildNotFound(context, result.query, result.nearest),
              );
            }
          },
        );
      },
    );
  }

  static Widget _buildContainer(BuildContext context, Widget child) {
    return Container(
      constraints: BoxConstraints(
        maxHeight: MediaQuery.of(context).size.height * 0.85,
      ),
      decoration: const BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          // Handle
          Center(
            child: Container(
              margin: const EdgeInsets.only(top: 12, bottom: 8),
              width: 40,
              height: 4,
              decoration: BoxDecoration(
                color: Colors.grey.shade300,
                borderRadius: BorderRadius.circular(2),
              ),
            ),
          ),
          Flexible(
            child: SingleChildScrollView(
              padding: const EdgeInsets.fromLTRB(24, 8, 24, 32),
              child: child,
            ),
          ),
        ],
      ),
    );
  }
}
"""
    # Remove the broken debug block from earlier in _buildNotFound
    broken_block = '''        
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Text("DEBUG INFO", style: TextStyle(fontWeight: FontWeight.bold, color: Colors.red.shade900, fontSize: 10)),
              Text("Raw Query: '$query'", style: const TextStyle(fontSize: 10)),
              Text("Cleaned: '$cleaned'", style: const TextStyle(fontSize: 10)),
              Text("Loaded Terms: $loadedCount", style: const TextStyle(fontSize: 10, color: Colors.blue)),
            ],
          ),
        ),'''
    content = content.replace(broken_block, '        const SizedBox(height: 24),')
    
    # Add a fallback message to _buildNotFound
    text_to_replace = """        Text(
          'This word is not in our dictionary yet.',
          style: GoogleFonts.inter(fontSize: 14, color: Colors.black54),
          textAlign: TextAlign.center,
        ),"""
    new_text = """        Text(
          'This word is not in our dictionary yet.',
          style: GoogleFonts.inter(fontSize: 14, color: Colors.black54),
          textAlign: TextAlign.center,
        ),
        if (query == '_' || query.isEmpty) ...[
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: Colors.blue.shade50,
              borderRadius: BorderRadius.circular(8),
            ),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Icon(Icons.info_outline, size: 20, color: Colors.blue.shade700),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(
                    'Tip: Text selection failed on this device. Please use the dictionary search icon at the top of the screen instead.',
                    style: TextStyle(fontSize: 12, color: Colors.blue.shade900),
                  ),
                ),
              ],
            ),
          ),
        ],"""
    content = content.replace(text_to_replace, new_text)

    with open('lib/features/dictionary/dictionary_popup.dart', 'w') as f:
        f.write(content)
    print("Successfully reverted and fixed dictionary_popup.dart")
else:
    print("Could not find static void show(")

