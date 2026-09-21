import 'package:flutter/material.dart';
import '../../../../foundation/theme/app_colors.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class PresentationWidget extends StatefulWidget {
  final Map<String, dynamic> data;

  const PresentationWidget({super.key, required this.data});

  @override
  State<PresentationWidget> createState() => _PresentationWidgetState();
}

class _PresentationWidgetState extends State<PresentationWidget> {
  int _currentIndex = 0;
  late List<String> _items;

  @override
  void initState() {
    super.initState();
    _items = List<String>.from(widget.data['content']?['items'] ?? []);
  }

  void _next() {
    if (_currentIndex < _items.length - 1) {
      setState(() => _currentIndex++);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.symmetric(vertical: 16),
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: AppColors.primary.withValues(alpha: 0.3), width: 2),
        boxShadow: [
          BoxShadow(
            color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.05),
            blurRadius: 10,
            offset: const Offset(0, 4),
          )
        ]
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Text(
            widget.data['content']?['title'] ?? 'Presentation',
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: AppColors.primary),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 24),
          for (int i = 0; i <= _currentIndex; i++)
            Padding(
              padding: const EdgeInsets.only(bottom: 16),
              child: AnimatedOpacity(
                opacity: 1.0,
                duration: const Duration(milliseconds: 500),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(TrilingualService.instance.getUIText("• "), style: TextStyle(fontSize: 22, color: AppColors.accent)),
                    Expanded(child: Text(_items[i], style: TextStyle(fontSize: 18, height: 1.5).adaptToLanguage())),
                  ],
                ),
              ),
            ),
          if (_currentIndex < _items.length - 1)
            Align(
              alignment: Alignment.centerRight,
              child: ElevatedButton.icon(
                onPressed: _next,
                icon: Icon(Icons.arrow_forward),
                label: Text(TrilingualService.instance.getUIText('Next')),
                style: ElevatedButton.styleFrom(backgroundColor: AppColors.primary, foregroundColor: Colors.white),
              ),
            )
          else
            Padding(
              padding: EdgeInsets.only(top: 16),
              child: Center(child: Text(TrilingualService.instance.getUIText('End of Presentation'), style: TextStyle(color: Colors.grey, fontStyle: FontStyle.italic))),
            )
        ],
      ),
    );
  }
}
