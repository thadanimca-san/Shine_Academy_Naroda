import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../core/engine/local_content_manager.dart';
import '../../core/engine/curriculum_database.dart';
import '../../core/services/universal_dictionary_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class SearchResult {
  final List<dynamic> path;
  final String displayPath;
  final dynamic value;

  SearchResult({required this.path, required this.displayPath, required this.value});
}

class ContentEditorScreen extends StatefulWidget {
  final String? assetPath;
  const ContentEditorScreen({super.key, this.assetPath});

  @override
  State<ContentEditorScreen> createState() => _ContentEditorScreenState();
}

class _ContentEditorScreenState extends State<ContentEditorScreen> {
  Map<String, dynamic> _data = {};
  bool _isLoading = true;
  String _searchQuery = '';
  final TextEditingController _searchController = TextEditingController();

  @override
  void initState() {
    super.initState();
    _loadData();
  }

  Map<String, dynamic> _normalizeData(dynamic rawData) {
    if (rawData is List) {
      return {
        'metadata': {'title': 'Data'},
        'content': rawData,
        'blocks': rawData,
      };
    } else if (rawData is Map) {
      return rawData as Map<String, dynamic>;
    }
    return {};
  }

  Future<void> _loadData() async {
    await LocalContentManager.instance.init();
    final defaultAsset = 'app_core/learning_modules/master_curriculum.json';
    final targetAsset = widget.assetPath ?? defaultAsset;
    final fileName = targetAsset.split('/').last;

    final data = await LocalContentManager.instance.readLocalJson(targetAsset);
    if (data != null) {
      setState(() {
        _data = _normalizeData(data);
        _isLoading = false;
      });
    } else {
      try {
        final String jsonString = await DefaultAssetBundle.of(context).loadString(targetAsset);
        setState(() {
          _data = _normalizeData(json.decode(jsonString));
          _isLoading = false;
        });
      } catch (e) {
        debugPrint("Error loading from rootBundle: $e");
        setState(() {
          _isLoading = false;
        });
      }
    }
  }

  Future<void> _saveData() async {
    final defaultAsset = 'app_core/learning_modules/master_curriculum.json';
    final targetAsset = widget.assetPath ?? defaultAsset;
    final fileName = targetAsset.split('/').last;
    final success = await LocalContentManager.instance.writeLocalJson(targetAsset, _data);
    
    // LIVE UPDATE: Reload the singleton in memory so the app doesn't need to restart!
    if (success && fileName == 'master_curriculum.json') {
      await CurriculumDatabase.instance.load(forceReload: true);
    }
    if (success && targetAsset.contains('universal_dictionary')) {
      await UniversalDictionaryService.instance.init(forceReload: true);
    }

    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          duration: const Duration(seconds: 5),
          content: Text(
            success
                ? '✅ Saved! Go back and reopen the chapter to see your changes.'
                : '❌ Failed to save! Check storage permissions.',
          ),
          backgroundColor: success ? Colors.green.shade700 : Colors.red,
        ),
      );
    }
  }

  List<SearchResult> _performSearch(dynamic node, String query, List<dynamic> currentPath, String displayPath) {
    List<SearchResult> results = [];
    if (query.isEmpty) return results;

    if (node is String || node is int || node is double) {
      if (node.toString().toLowerCase().contains(query.toLowerCase())) {
        results.add(SearchResult(
          path: currentPath,
          displayPath: displayPath,
          value: node,
        ));
      }
    } else if (node is Map) {
      node.forEach((key, value) {
        // Also match keys so they can search for "gseb_class8" and find its contents
        bool keyMatches = key.toString().toLowerCase().contains(query.toLowerCase());
        
        if (keyMatches && (value is String || value is int || value is double)) {
           // If the key matches and it's a primitive, add it
           results.add(SearchResult(
             path: List.from(currentPath)..add(key),
             displayPath: displayPath.isEmpty ? key.toString() : '$displayPath > $key',
             value: value,
           ));
        }

        List<dynamic> newPath = List.from(currentPath)..add(key);
        String newDisplay = displayPath.isEmpty ? key.toString() : '$displayPath > $key';
        results.addAll(_performSearch(value, query, newPath, newDisplay));
      });
    } else if (node is List) {
      for (int i = 0; i < node.length; i++) {
        List<dynamic> newPath = List.from(currentPath)..add(i);
        String newDisplay = '$displayPath > [$i]';
        results.addAll(_performSearch(node[i], query, newPath, newDisplay));
      }
    }
    return results;
  }

  void _updateValueAtPath(List<dynamic> path, dynamic newValue) {
    dynamic current = _data;
    for (int i = 0; i < path.length - 1; i++) {
      current = current[path[i]];
    }
    setState(() {
      current[path.last] = newValue;
    });
    // Let user save manually to avoid saving broken state
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(TrilingualService.instance.getUIText('Field updated. Remember to tap Save All Changes!')), backgroundColor: Colors.orange));
  }

  void _showQuickEditDialog(SearchResult result) {
    final TextEditingController editController = TextEditingController(text: result.value.toString());
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Text(TrilingualService.instance.getUIText('Quick Edit'), style: GoogleFonts.inter(fontWeight: FontWeight.bold)),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(result.displayPath, style: GoogleFonts.inter(fontSize: 12, color: Colors.grey)),
              const SizedBox(height: 16),
              TextField(
                controller: editController,
                maxLines: null,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  labelText: 'Value',
                ),
              ),
            ],
          ),
          actions: [
            TextButton(onPressed: () => Navigator.pop(context), child: Text(TrilingualService.instance.getUIText('Cancel'))),
            ElevatedButton(
              style: ElevatedButton.styleFrom(backgroundColor: Colors.indigo, foregroundColor: Colors.white),
              onPressed: () {
                dynamic finalValue = editController.text;
                if (result.value is int) {
                  finalValue = int.tryParse(editController.text) ?? result.value;
                } else if (result.value is double) {
                  finalValue = double.tryParse(editController.text) ?? result.value;
                }
                
                _updateValueAtPath(result.path, finalValue);
                Navigator.pop(context);
              },
              child: Text(TrilingualService.instance.getUIText('Apply Change')),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    List<SearchResult> searchResults = _searchQuery.isEmpty ? [] : _performSearch(_data, _searchQuery, [], "");

    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('EduOS Content Editor')),
        backgroundColor: Colors.indigo[800],
        foregroundColor: Colors.white,
        actions: [
          IconButton(
            icon: Icon(Icons.restore),
            tooltip: 'Reset to Factory Data',
            onPressed: () async {
              final confirm = await showDialog<bool>(
                context: context,
                builder: (context) => AlertDialog(
                  title: Text(TrilingualService.instance.getUIText('Reset Content?')),
                  content: Text(TrilingualService.instance.getUIText('This will delete all your manual edits for this file and reload the default data. Are you sure?')),
                  actions: [
                    TextButton(onPressed: () => Navigator.pop(context, false), child: Text(TrilingualService.instance.getUIText('Cancel'))),
                    TextButton(onPressed: () => Navigator.pop(context, true), child: Text(TrilingualService.instance.getUIText('Reset'), style: TextStyle(color: Colors.red))),
                  ],
                ),
              );
              
              if (confirm == true) {
                setState(() => _isLoading = true);
                final targetAsset = widget.assetPath ?? 'app_core/learning_modules/master_curriculum.json';
                final fileName = targetAsset.split('/').last;
                await LocalContentManager.instance.deleteLocalJson(targetAsset);
                if (fileName == 'master_curriculum.json') {
                  await CurriculumDatabase.instance.load(forceReload: true);
                }
                await _loadData();
                if (mounted) {
                  ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(TrilingualService.instance.getUIText('Content reset to factory defaults!'))));
                }
              }
            },
          ),
          IconButton(
            icon: Icon(Icons.save),
            tooltip: 'Save All Changes',
            onPressed: _saveData,
          )
        ],
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : _data.isEmpty
              ? Center(child: Text(TrilingualService.instance.getUIText("No data found or failed to load.")))
              : Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Column(
                    children: [
                      Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: TextField(
                          controller: _searchController,
                          decoration: InputDecoration(
                            hintText: 'Search for any word, chapter, or id...',
                            prefixIcon: Icon(Icons.search),
                            suffixIcon: _searchQuery.isNotEmpty 
                                ? IconButton(
                                    icon: Icon(Icons.clear), 
                                    onPressed: () {
                                      _searchController.clear();
                                      setState(() { _searchQuery = ''; });
                                    }
                                  ) 
                                : null,
                            border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                            filled: true,
                            fillColor: Colors.white,
                          ),
                          onChanged: (val) {
                            setState(() {
                              _searchQuery = val;
                            });
                          },
                        ),
                      ),
                      if (_searchQuery.isNotEmpty)
                        Expanded(
                          child: searchResults.isEmpty 
                              ? Center(child: Text('No matches found for "$_searchQuery"', style: GoogleFonts.inter(color: Colors.grey)))
                              : ListView.builder(
                                  itemCount: searchResults.length,
                                  itemBuilder: (context, index) {
                                    final res = searchResults[index];
                                    return Card(
                                      margin: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                                      child: ListTile(
                                        title: Text(res.value.toString(), maxLines: 2, overflow: TextOverflow.ellipsis, style: GoogleFonts.inter(fontWeight: FontWeight.bold)),
                                        subtitle: Text(res.displayPath, style: GoogleFonts.inter(fontSize: 12, color: Colors.indigo)),
                                        trailing: Icon(Icons.edit, color: Colors.orange),
                                        onTap: () => _showQuickEditDialog(res),
                                      ),
                                    );
                                  },
                                ),
                        )
                      else
                        Expanded(
                          child: Column(
                            children: [
                              Padding(
                                padding: const EdgeInsets.all(8.0),
                                child: Text(TrilingualService.instance.getUIText("Visual Data Editor: Drill down into the folders to edit any text, path, or diagram. Tap Save when done."),
                                  style: GoogleFonts.inter(color: Colors.grey[700]),
                                ),
                              ),
                              Expanded(
                                child: JsonNodeViewer(
                                  label: "Master Database",
                                  data: _data,
                                  onChanged: (newData) {
                                    _data = newData;
                                  },
                                ),
                              ),
                            ],
                          ),
                        ),
                    ],
                  ),
                ),
    );
  }
}

class JsonNodeViewer extends StatefulWidget {
  final dynamic data;
  final String label;
  final ValueChanged<dynamic> onChanged;

  const JsonNodeViewer({
    super.key,
    required this.data,
    required this.label,
    required this.onChanged,
  });

  @override
  State<JsonNodeViewer> createState() => _JsonNodeViewerState();
}

class _JsonNodeViewerState extends State<JsonNodeViewer> {
  late dynamic _currentData;

  @override
  void initState() {
    super.initState();
    _currentData = widget.data;
  }

  void _update(dynamic newValue) {
    setState(() {
      _currentData = newValue;
    });
    widget.onChanged(_currentData);
  }

  @override
  Widget build(BuildContext context) {
    if (_currentData is String || _currentData is int || _currentData is double || _currentData is bool) {
      return _buildPrimitiveEditor();
    } else if (_currentData is Map) {
      return _buildMapViewer(Map<String, dynamic>.from(_currentData));
    } else if (_currentData is List) {
      return _buildListViewer(List<dynamic>.from(_currentData));
    } else {
      return Padding(
        padding: const EdgeInsets.symmetric(vertical: 4.0),
        child: Text("${widget.label}: Unsupported type (${_currentData?.runtimeType ?? 'null'})"),
      );
    }
  }

  Widget _buildPrimitiveEditor() {
    if (_currentData is String) {
      return Padding(
        padding: const EdgeInsets.symmetric(vertical: 4.0),
        child: TextFormField(
          initialValue: _currentData,
          decoration: InputDecoration(
            labelText: widget.label,
            border: const OutlineInputBorder(),
            filled: true,
            fillColor: Colors.white,
          ),
          maxLines: null,
          onChanged: (val) => _update(val),
        ),
      );
    } else if (_currentData is int || _currentData is double) {
      return Padding(
        padding: const EdgeInsets.symmetric(vertical: 4.0),
        child: TextFormField(
          initialValue: _currentData.toString(),
          decoration: InputDecoration(
            labelText: widget.label,
            border: const OutlineInputBorder(),
          ),
          keyboardType: TextInputType.number,
          onChanged: (val) {
            if (_currentData is int) {
              _update(int.tryParse(val) ?? _currentData);
            } else {
              _update(double.tryParse(val) ?? _currentData);
            }
          },
        ),
      );
    } else if (_currentData is bool) {
      return SwitchListTile(
        title: Text(widget.label, style: TextStyle(fontWeight: FontWeight.bold)),
        value: _currentData,
        onChanged: (val) => _update(val),
      );
    }
    return const SizedBox();
  }

  Widget _buildMapViewer(Map<String, dynamic> map) {
    final keys = map.keys.toList();
    return ListView.builder(
      itemCount: keys.length + 1, // +1 for add key button
      itemBuilder: (context, index) {
        if (index == keys.length) {
          return Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 8.0),
            child: ElevatedButton.icon(
              onPressed: () {
                showDialog(
                  context: context,
                  builder: (context) {
                    final keyCtrl = TextEditingController();
                    return AlertDialog(
                      title: Text(TrilingualService.instance.getUIText("Add New Field")),
                      content: TextField(
                        controller: keyCtrl,
                        decoration: const InputDecoration(labelText: 'Field Name (Key)'),
                      ),
                      actions: [
                        TextButton(onPressed: () => Navigator.pop(context), child: Text(TrilingualService.instance.getUIText("Cancel"))),
                        TextButton(onPressed: () {
                          if (keyCtrl.text.isNotEmpty) {
                            map[keyCtrl.text] = ""; // Default empty string
                            _update(map);
                            Navigator.pop(context);
                          }
                        }, child: Text(TrilingualService.instance.getUIText("Add"))),
                      ],
                    );
                  }
                );
              },
              icon: Icon(Icons.add),
              label: Text(TrilingualService.instance.getUIText('Add Field')),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.indigo.shade50),
            ),
          );
        }

        final key = keys[index];
        final value = map[key];
        
        final trailingAction = IconButton(
          icon: Icon(Icons.delete, color: Colors.red, size: 20),
          onPressed: () async {
            final conf = await showDialog<bool>(
              context: context,
              builder: (ctx) => AlertDialog(
                title: Text("Delete '$key'?"),
                actions: [
                  TextButton(onPressed: () => Navigator.pop(ctx, false), child: Text(TrilingualService.instance.getUIText("Cancel"))),
                  TextButton(onPressed: () => Navigator.pop(ctx, true), child: Text(TrilingualService.instance.getUIText("Delete"), style: TextStyle(color: Colors.red))),
                ],
              )
            );
            if (conf == true) {
              map.remove(key);
              _update(map);
            }
          },
        );

        if (value is Map || value is List) {
          return Card(
            elevation: 1,
            margin: const EdgeInsets.symmetric(vertical: 4.0),
            child: ListTile(
              leading: Icon(value is Map ? Icons.folder : Icons.list, color: Colors.indigo),
              title: Text(key, style: TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text(value is Map ? '${value.length} fields' : '${value.length} items'),
              trailing: Row(mainAxisSize: MainAxisSize.min, children: [trailingAction, Icon(Icons.arrow_forward_ios, size: 16)]),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => Scaffold(
                      appBar: AppBar(
                        title: Text(key),
                        backgroundColor: Colors.indigo[600],
                        foregroundColor: Colors.white,
                      ),
                      body: Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: JsonNodeViewer(
                          label: key,
                          data: value,
                          onChanged: (newVal) {
                            map[key] = newVal;
                            _update(map);
                          },
                        ),
                      ),
                    ),
                  ),
                );
              },
            ),
          );
        } else {
          return Stack(
            children: [
              JsonNodeViewer(
                label: key,
                data: value,
                onChanged: (newVal) {
                  map[key] = newVal;
                  _update(map);
                },
              ),
              Positioned(
                top: 0,
                right: 0,
                child: trailingAction,
              )
            ],
          );
        }
      },
    );
  }

  Widget _buildListViewer(List<dynamic> list) {
    return ListView.builder(
      itemCount: list.length + 1, // +1 for Add Item button
      itemBuilder: (context, index) {
        if (index == list.length) {
          return Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 8.0),
            child: ElevatedButton.icon(
              onPressed: () {
                showDialog(
                  context: context,
                  builder: (context) {
                    return AlertDialog(
                      title: Text(TrilingualService.instance.getUIText("Add New Item")),
                      content: Text(TrilingualService.instance.getUIText("What kind of item do you want to add?")),
                      actions: [
                        TextButton(onPressed: () {
                          list.add(""); // String
                          _update(list);
                          Navigator.pop(context);
                        }, child: Text(TrilingualService.instance.getUIText("Text"))),
                        TextButton(onPressed: () {
                          list.add({}); // Map
                          _update(list);
                          Navigator.pop(context);
                        }, child: Text(TrilingualService.instance.getUIText("Object (Block)"))),
                      ],
                    );
                  }
                );
              },
              icon: Icon(Icons.add),
              label: Text(TrilingualService.instance.getUIText('Add Item')),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.teal.shade50),
            ),
          );
        }

        final value = list[index];
        final label = 'Item $index';
        
        final trailingAction = IconButton(
          icon: Icon(Icons.delete, color: Colors.red, size: 20),
          onPressed: () async {
            final conf = await showDialog<bool>(
              context: context,
              builder: (ctx) => AlertDialog(
                title: Text(TrilingualService.instance.getUIText("Delete this item?")),
                actions: [
                  TextButton(onPressed: () => Navigator.pop(ctx, false), child: Text(TrilingualService.instance.getUIText("Cancel"))),
                  TextButton(onPressed: () => Navigator.pop(ctx, true), child: Text(TrilingualService.instance.getUIText("Delete"), style: TextStyle(color: Colors.red))),
                ],
              )
            );
            if (conf == true) {
              list.removeAt(index);
              _update(list);
            }
          },
        );
        
        if (value is Map || value is List) {
          return Card(
            elevation: 1,
            margin: const EdgeInsets.symmetric(vertical: 4.0),
            child: ListTile(
              leading: Icon(value is Map ? Icons.folder : Icons.list, color: Colors.teal),
              title: Text(label, style: TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text(value is Map ? '${value.length} fields' : '${value.length} items'),
              trailing: Row(mainAxisSize: MainAxisSize.min, children: [trailingAction, Icon(Icons.arrow_forward_ios, size: 16)]),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => Scaffold(
                      appBar: AppBar(
                        title: Text(label),
                        backgroundColor: Colors.teal[600],
                        foregroundColor: Colors.white,
                      ),
                      body: Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: JsonNodeViewer(
                          label: label,
                          data: value,
                          onChanged: (newVal) {
                            list[index] = newVal;
                            _update(list);
                          },
                        ),
                      ),
                    ),
                  ),
                );
              },
            ),
          );
        } else {
          return Stack(
            children: [
              JsonNodeViewer(
                label: label,
                data: value,
                onChanged: (newVal) {
                  list[index] = newVal;
                  _update(list);
                },
              ),
              Positioned(
                top: 0,
                right: 0,
                child: trailingAction,
              )
            ],
          );
        }
      },
    );
  }
}
