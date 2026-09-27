import re

with open('lib/features/dictionary/dictionary_popup.dart', 'r') as f:
    content = f.read()

# We want to replace the `static void show(BuildContext context, String termId)` method 
# and add a stateful widget.

new_show = '''  static void show(BuildContext context, String termId) {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) {
        return Padding(
          padding: EdgeInsets.only(bottom: MediaQuery.of(context).viewInsets.bottom),
          child: _DictionaryPopupContent(initialQuery: termId),
        );
      },
    );
  }'''

# Replace the show method
content = re.sub(r'  static void show\(BuildContext context, String termId\) \{.*?(?=  static Widget _buildContainer)', new_show + '\n\n', content, flags=re.DOTALL)

# Add the stateful widget at the end of the file
stateful_widget = '''
class _DictionaryPopupContent extends StatefulWidget {
  final String initialQuery;
  const _DictionaryPopupContent({required this.initialQuery});

  @override
  State<_DictionaryPopupContent> createState() => _DictionaryPopupContentState();
}

class _DictionaryPopupContentState extends State<_DictionaryPopupContent> {
  late TextEditingController _controller;
  _LookupResult? _result;
  bool _isLoading = false;

  @override
  void initState() {
    super.initState();
    _controller = TextEditingController(text: widget.initialQuery == '_' ? '' : widget.initialQuery);
    if (_controller.text.isNotEmpty) {
      _performSearch(_controller.text);
    }
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  Future<void> _performSearch(String query) async {
    if (query.trim().isEmpty) {
      setState(() {
        _result = null;
        _isLoading = false;
      });
      return;
    }
    setState(() => _isLoading = true);
    final res = await UniversalDictionaryPopup._lookup(query);
    if (mounted) {
      setState(() {
        _result = res;
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
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
          
          // Search Bar
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 8),
            child: TextField(
              controller: _controller,
              textInputAction: TextInputAction.search,
              onSubmitted: _performSearch,
              decoration: InputDecoration(
                hintText: 'Search for a word...',
                prefixIcon: const Icon(Icons.search, color: AppColors.primary),
                suffixIcon: IconButton(
                  icon: const Icon(Icons.clear),
                  onPressed: () {
                    _controller.clear();
                    _performSearch('');
                  },
                ),
                filled: true,
                fillColor: Colors.grey.shade100,
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(12),
                  borderSide: BorderSide.none,
                ),
                contentPadding: const EdgeInsets.symmetric(vertical: 0),
              ),
            ),
          ),

          Flexible(
            child: SingleChildScrollView(
              padding: const EdgeInsets.fromLTRB(24, 8, 24, 32),
              child: _isLoading 
                  ? const Padding(
                      padding: EdgeInsets.all(32.0),
                      child: Center(child: CircularProgressIndicator(color: AppColors.primary)),
                    )
                  : (_result == null 
                      ? const SizedBox.shrink()
                      : (_result!.found
                          ? UniversalDictionaryPopup._buildTermDetail(context, _result!.term!)
                          : UniversalDictionaryPopup._buildNotFound(context, _result!.query, _result!.nearest))),
            ),
          ),
        ],
      ),
    );
  }
}
'''

content += stateful_widget

with open('lib/features/dictionary/dictionary_popup.dart', 'w') as f:
    f.write(content)

