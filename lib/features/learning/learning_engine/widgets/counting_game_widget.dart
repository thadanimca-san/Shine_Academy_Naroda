import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../../../../foundation/theme/app_colors.dart';
import 'dart:math';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class CountingGameWidget extends StatefulWidget {
  final Map<String, dynamic> data;

  const CountingGameWidget({super.key, required this.data});

  @override
  State<CountingGameWidget> createState() => _CountingGameWidgetState();
}

class _CountingGameWidgetState extends State<CountingGameWidget> {
  late int _targetNumber;
  late String _itemEmoji;
  int _poppedCount = 0;
  late List<bool> _popped;

  @override
  void initState() {
    super.initState();
    _targetNumber = widget.data['target_number'] ?? 3;
    _itemEmoji = widget.data['item_emoji'] ?? '🎈';
    _popped = List.generate(_targetNumber, (index) => false);
  }

  void _pop(int index) {
    if (!_popped[index]) {
      HapticFeedback.lightImpact();
      setState(() {
        _popped[index] = true;
        _poppedCount++;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    bool isComplete = _poppedCount == _targetNumber;

    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: Colors.orange.withValues(alpha: 0.1),
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: Colors.orange.withValues(alpha: 0.3), width: 3),
      ),
      child: Column(
        children: [
          Text(
            isComplete ? 'Yay! You counted $_targetNumber!' : 'Pop $_targetNumber $_itemEmoji',
            style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: Colors.orange),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 16),
          Text(
            'Count: $_poppedCount / $_targetNumber',
            style: TextStyle(fontSize: 20, fontWeight: FontWeight.w600, color: Theme.of(context).colorScheme.onSurfaceVariant),
          ),
          const SizedBox(height: 32),
          Wrap(
            spacing: 20,
            runSpacing: 20,
            alignment: WrapAlignment.center,
            children: List.generate(_targetNumber, (index) {
              return GestureDetector(
                onTap: () => _pop(index),
                child: AnimatedOpacity(
                  duration: const Duration(milliseconds: 300),
                  opacity: _popped[index] ? 0.0 : 1.0,
                  child: Transform.scale(
                    scale: _popped[index] ? 1.5 : 1.0,
                    child: Text(
                      _itemEmoji,
                      style: TextStyle(fontSize: 64),
                    ),
                  ),
                ),
              );
            }),
          ),
          if (isComplete) ...[
            const SizedBox(height: 32),
            FilledButton.icon(
              onPressed: () {
                setState(() {
                  _poppedCount = 0;
                  _popped = List.generate(_targetNumber, (index) => false);
                });
              },
              icon: Icon(Icons.refresh),
              label: Text(TrilingualService.instance.getUIText('Play Again')),
              style: FilledButton.styleFrom(backgroundColor: Colors.orange),
            )
          ]
        ],
      ),
    );
  }
}
