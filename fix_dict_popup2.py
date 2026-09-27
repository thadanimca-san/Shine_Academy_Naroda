with open('lib/features/dictionary/dictionary_popup.dart.bak', 'r') as f:
    bak_content = f.read()

# Extract _buildNotFound and _buildTermDetail
buildNotFound_idx = bak_content.find('  static Widget _buildNotFound(')
buildTermDetail_idx = bak_content.find('  static Widget _buildTermDetail(')
buildContainer_idx = bak_content.find('  static Widget _buildContainer(') # Assuming it's below them
end_idx = bak_content.find('class _DictionaryPopupContent extends StatefulWidget {')

extracted_methods = bak_content[buildNotFound_idx:end_idx]

# We need to remove the broken debug block from extracted_methods
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
extracted_methods = extracted_methods.replace(broken_block, '        const SizedBox(height: 24),')

# Add fallback message
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
extracted_methods = extracted_methods.replace(text_to_replace, new_text)

# We also need to strip out _buildContainer from extracted_methods because we already added it
idx_container = extracted_methods.find('  static Widget _buildContainer(')
if idx_container != -1:
    extracted_methods = extracted_methods[:idx_container]

# Read current file
with open('lib/features/dictionary/dictionary_popup.dart', 'r') as f:
    current = f.read()

# Insert the methods before the final closing brace
final_brace_idx = current.rfind('}')
if final_brace_idx != -1:
    current = current[:final_brace_idx] + extracted_methods + '\n}\n'

with open('lib/features/dictionary/dictionary_popup.dart', 'w') as f:
    f.write(current)
    print("Methods appended successfully")
