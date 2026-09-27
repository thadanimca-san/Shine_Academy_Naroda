import re

with open('lib/features/dictionary/dictionary_popup.dart', 'r') as f:
    text = f.read()

text = text.replace("}\n\n}\n", "}\n")

state_class = """
class _DictionaryPopupContentState extends State<_DictionaryPopupContent> {
  late String _currentQuery;
  late Future<_LookupResult> _future;
  final TextEditingController _searchController = TextEditingController();

  @override
  void initState() {
    super.initState();
    _currentQuery = widget.initialTermId == '_' ? '' : widget.initialTermId;
    _searchController.text = _currentQuery;
    _future = UniversalDictionaryPopup._lookup(_currentQuery);
  }

  void _search(String query) {
    final trimmed = query.trim();
    if (trimmed.isEmpty) return;
    setState(() {
      _currentQuery = trimmed;
      _future = UniversalDictionaryPopup._lookup(_currentQuery);
    });
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<_LookupResult>(
      future: _future,
      builder: (context, snapshot) {
        Widget content;

        if (snapshot.connectionState == ConnectionState.waiting) {
          content = const SizedBox(
            height: 120,
            child: Center(child: CircularProgressIndicator()),
          );
        } else {
          final result = snapshot.data;
          if (result == null || (!result.found && result.nearest == null)) {
            content = UniversalDictionaryPopup._buildNotFound(context, _currentQuery, null);
          } else if (!result.found) {
            content = UniversalDictionaryPopup._buildNotFound(context, _currentQuery, result.nearest);
          } else {
            content = UniversalDictionaryPopup._buildTermDetail(context, result.term!);
          }
        }

        return Container(
          constraints: BoxConstraints(
            maxHeight: MediaQuery.of(context).size.height * 0.90,
          ),
          padding: EdgeInsets.only(
            left: 24,
            right: 24,
            top: 24,
            bottom: MediaQuery.of(context).viewInsets.bottom + 24,
          ),
          decoration: const BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
          ),
          child: SafeArea(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                TextField(
                  controller: _searchController,
                  decoration: InputDecoration(
                    hintText: 'Search for any word...',
                    prefixIcon: const Icon(Icons.search, color: Colors.blue),
                    suffixIcon: IconButton(
                      icon: const Icon(Icons.close),
                      onPressed: () {
                        _searchController.clear();
                      },
                    ),
                    filled: true,
                    fillColor: Colors.grey.shade100,
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(16),
                      borderSide: BorderSide.none,
                    ),
                    contentPadding: const EdgeInsets.symmetric(vertical: 0),
                  ),
                  onSubmitted: _search,
                ),
                const SizedBox(height: 16),
                Flexible(
                  child: SingleChildScrollView(
                    child: content,
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }
}
"""

with open('lib/features/dictionary/dictionary_popup.dart', 'w') as f:
    f.write(text + "\n" + state_class)

