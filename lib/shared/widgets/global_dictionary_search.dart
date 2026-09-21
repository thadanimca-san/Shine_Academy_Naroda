import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../core/services/universal_dictionary_service.dart';
import '../../core/services/trilingual_service.dart';
import '../../features/dictionary/dictionary_popup.dart';
import '../../foundation/navigation/app_router.dart';
import '../../foundation/theme/app_colors.dart';

class GlobalDictionaryWrapper extends StatefulWidget {
  final Widget child;
  const GlobalDictionaryWrapper({super.key, required this.child});
  @override
  State<GlobalDictionaryWrapper> createState() => _GlobalDictionaryWrapperState();
}

class _GlobalDictionaryWrapperState extends State<GlobalDictionaryWrapper> {
  Offset _position = const Offset(100, 40);
  bool _isDragging = false;
  final GlobalKey _pillKey = GlobalKey();

  bool _initialized = false;
  bool _startAnimation = false;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (!mounted) return;
      final size = MediaQuery.of(context).size;
      double pillWidth = 240.0;
      final RenderBox? renderBox = _pillKey.currentContext?.findRenderObject() as RenderBox?;
      if (renderBox != null) pillWidth = renderBox.size.width;
      
      setState(() {
        _position = Offset(size.width / 2 - pillWidth / 2, 40);
        _initialized = true;
      });

      Future.delayed(const Duration(milliseconds: 1500), () {
        if (mounted) {
          setState(() {
            _startAnimation = true;
            final double safeBottom = size.height - MediaQuery.of(context).padding.bottom - 100;
            final double targetX = size.width - pillWidth - 12.0;
            _position = Offset(targetX.clamp(12.0, size.width - pillWidth - 12.0), safeBottom);
          });
        }
      });
    });
  }

  @override
  void dispose() {
    super.dispose();
  }

  void _openGlobalSearch(BuildContext context) {
    final navigatorContext = rootNavigatorKey.currentContext;
    if (navigatorContext != null) {
      showSearch(
        context: navigatorContext,
        delegate: GlobalDictionarySearchDelegate(),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: TrilingualService.instance,
      builder: (context, _) {
        final size = MediaQuery.of(context).size;
        
        double pillWidth = 240.0;
        final RenderBox? renderBox = _pillKey.currentContext?.findRenderObject() as RenderBox?;
        if (renderBox != null) pillWidth = renderBox.size.width;

        if (!_initialized && _position.dx == 100) {
           _position = Offset(size.width / 2 - 85, 40);
        }

        return Stack(
          children: [
            widget.child, 
            AnimatedPositioned(
              duration: _isDragging || !_startAnimation ? Duration.zero : const Duration(milliseconds: 1200),
              curve: Curves.easeInOutCubic,
              left: _position.dx,
              top: _position.dy,
              child: GestureDetector(
                onPanStart: (_) { setState(() => _isDragging = true); },
                onPanUpdate: (details) { setState(() { _position += details.delta; }); },
                onPanEnd: (details) {
                  setState(() {
                    _isDragging = false;
                    double pillWidth = 240.0;
                    final RenderBox? renderBox = _pillKey.currentContext?.findRenderObject() as RenderBox?;
                    if (renderBox != null) pillWidth = renderBox.size.width;
                    
                    final bool dockLeft = (_position.dx + pillWidth / 2) < (size.width / 2);
                    final double targetX = dockLeft ? 12.0 : size.width - pillWidth - 12.0;
                    
                    final double safeTop = MediaQuery.of(context).padding.top + 10;
                    final double safeBottom = size.height - MediaQuery.of(context).padding.bottom - 60;
                    final double targetY = _position.dy.clamp(safeTop, safeBottom);
                    
                    _position = Offset(targetX, targetY);
                  });
                },
                child: Material(
                  color: Colors.transparent,
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      InkWell(
                        onTap: () => _openGlobalSearch(context),
                        borderRadius: BorderRadius.circular(30),
                        child: Container(
                          key: _pillKey,
                          constraints: BoxConstraints(maxWidth: size.width * 0.4),
                          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                          decoration: BoxDecoration(
                            color: AppColors.primary.withValues(alpha: 0.95),
                            borderRadius: BorderRadius.circular(30),
                            boxShadow: [
                              BoxShadow(
                                color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.2),
                                blurRadius: _isDragging ? 15 : 10,
                                offset: Offset(0, _isDragging ? 8 : 4),
                              ),
                            ],
                            border: Border.all(
                              color: Colors.white.withValues(alpha: 0.3),
                              width: 1,
                            ),
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Icon(Icons.search, color: Colors.white, size: 18),
                              const SizedBox(width: 8),
                              Flexible(
                                child: Text(TrilingualService.instance.getUIText('Dictionary'),
                                  style: GoogleFonts.inter(
                                    color: Colors.white,
                                    fontWeight: FontWeight.bold,
                                    fontSize: 14,
                                  ),
                                  overflow: TextOverflow.ellipsis,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ],
        );
      },
    );
  }
}

class GlobalDictionarySearchDelegate extends SearchDelegate<String?> {
  @override
  String get searchFieldLabel => 'Type a word...';

  @override
  ThemeData appBarTheme(BuildContext context) {
    final theme = Theme.of(context);
    return theme.copyWith(
      appBarTheme: AppBarTheme(
        backgroundColor: Colors.white,
        iconTheme: const IconThemeData(color: AppColors.primary),
        elevation: 0,
        toolbarTextStyle: theme.textTheme.bodyMedium,
        titleTextStyle: theme.textTheme.titleLarge,
      ),
      inputDecorationTheme: InputDecorationTheme(
        border: InputBorder.none,
        hintStyle: GoogleFonts.inter(color: Colors.grey.shade400),
      ),
    );
  }

  @override
  List<Widget>? buildActions(BuildContext context) {
    return [
      if (query.isNotEmpty)
        IconButton(
          icon: Icon(Icons.clear),
          onPressed: () {
            query = '';
            showSuggestions(context);
          },
        ),
    ];
  }

  @override
  Widget? buildLeading(BuildContext context) {
    return IconButton(
      icon: Icon(Icons.arrow_back),
      onPressed: () => close(context, null),
    );
  }

  @override
  Widget buildResults(BuildContext context) {
    return _buildFutureList();
  }

  @override
  Widget buildSuggestions(BuildContext context) {
    return _buildFutureList();
  }

  Widget _buildFutureList() {
    final String q = query.trim().toLowerCase();
    if (q.isEmpty) {
      return Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(Icons.menu_book, size: 64, color: Colors.grey.shade300),
            const SizedBox(height: 16),
            Text(TrilingualService.instance.getUIText('Search any word globally'),
              style: GoogleFonts.inter(color: Colors.grey.shade600, fontSize: 16),
            ),
          ],
        ),
      );
    }

    return FutureBuilder<List<Map<String, dynamic>>>(
      future: UniversalDictionaryService.instance.searchTerms(q),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return Center(child: CircularProgressIndicator());
        }
        if (snapshot.hasError) {
          return Center(child: Text('Error: ${snapshot.error}'));
        }
        
        final results = snapshot.data ?? [];
        if (results.isEmpty) {
          return Center(
            child: Text(
              'No words found for "$query".',
              style: GoogleFonts.inter(color: Colors.grey),
            ),
          );
        }

        return ListView.builder(
          itemCount: results.length,
          itemBuilder: (context, index) {
            final term = results[index];
            final String en = term['term']?['english'] ?? '';
            final String hi = term['term']?['hindi'] ?? term['term']?['hi'] ?? '';
            final String gu = term['term']?['gujarati'] ?? term['term']?['gu'] ?? '';
            
            final simpleRaw = term['definition']?['simple'];
            final String simpleEn = simpleRaw is Map ? (simpleRaw['en'] ?? '') : (simpleRaw ?? '');

            return ListTile(
              leading: Icon(Icons.search, color: Colors.grey),
              title: Text(
                en,
                style: GoogleFonts.poppins(
                  fontWeight: FontWeight.bold,
                  color: AppColors.textPrimary,
                ),
              ),
              subtitle: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  if (hi.isNotEmpty || gu.isNotEmpty)
                    Text(
                      '$hi ${hi.isNotEmpty && gu.isNotEmpty ? '|' : ''} $gu',
                      style: GoogleFonts.notoSans(
                        color: AppColors.textSecondary,
                        fontSize: 13,
                      ),
                    ),
                  if (simpleEn.isNotEmpty)
                    Text(
                      simpleEn,
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: GoogleFonts.inter(color: Colors.grey.shade600, fontSize: 13),
                    ),
                ],
              ),
              onTap: () {
                close(context, null);
                final navigatorContext = rootNavigatorKey.currentContext;
                if (navigatorContext != null) {
                  UniversalDictionaryPopup.show(navigatorContext, term['id'].toString());
                }
              },
            );
          },
        );
      },
    );
  }
}
