import 'dart:async';
import 'dart:math';
import 'package:flutter/material.dart';
import '../../../core/services/trilingual_service.dart';
import 'package:shine_academy_naroda/foundation/theme/app_typography.dart';

class MultiplicationTableView extends StatefulWidget {
  const MultiplicationTableView({super.key});

  @override
  State<MultiplicationTableView> createState() => _MultiplicationTableViewState();
}

class _MultiplicationTableViewState extends State<MultiplicationTableView> {
  final TextEditingController _startController = TextEditingController(text: '2');
  final TextEditingController _endController = TextEditingController(text: '10');

  int? _currentMultiplier;
  int? _currentMultiplicand;
  bool _showAnswer = false;

  // Stopwatch variables
  Stopwatch _stopwatch = Stopwatch();
  Timer? _timer;
  String _elapsedTimeStr = '0.0s';

  @override
  void dispose() {
    _startController.dispose();
    _endController.dispose();
    _timer?.cancel();
    super.dispose();
  }

  void _startTimer() {
    _stopwatch.reset();
    _stopwatch.start();
    _timer?.cancel();
    _timer = Timer.periodic(const Duration(milliseconds: 100), (timer) {
      if (_stopwatch.isRunning) {
        setState(() {
          _elapsedTimeStr = (_stopwatch.elapsedMilliseconds / 1000).toStringAsFixed(1) + 's';
        });
      }
    });
  }

  void _stopTimer() {
    _stopwatch.stop();
    _timer?.cancel();
  }

  void _generateRandomQuestion() {
    int start = int.tryParse(_startController.text) ?? 2;
    int end = int.tryParse(_endController.text) ?? 10;

    if (start > end) {
      int temp = start;
      start = end;
      end = temp;
    }

    final random = Random();
    // Pick random table number between start and end (inclusive)
    int multiplier = start + random.nextInt((end - start) + 1);
    // Multiplicand strictly from 2 to 9 (excluding 1 and 10)
    int multiplicand = 2 + random.nextInt(8); // Generates 0 to 7, +2 makes it 2 to 9

    setState(() {
      _currentMultiplier = multiplier;
      _currentMultiplicand = multiplicand;
      _showAnswer = false;
    });

    _startTimer();
  }

  void _revealAnswer() {
    if (_currentMultiplier == null) return;
    _stopTimer();
    setState(() {
      _showAnswer = true;
    });
  }

  @override
  Widget build(BuildContext context) {
    int product = (_currentMultiplier ?? 0) * (_currentMultiplicand ?? 0);

    return LayoutBuilder(
      builder: (context, constraints) {
        final bool isNarrow = constraints.maxWidth < 600;

        final controlPanel = _buildControlPanel(isNarrow);
        final displayCard = _buildDisplayCard(product, constraints, isNarrow);

        return Scaffold(
          backgroundColor: const Color(0xFF111118),
          appBar: AppBar(
            title: Text(TrilingualService.instance.getUIText('Tables Practice')),
            backgroundColor: const Color(0xFF181820),
            iconTheme: const IconThemeData(color: Colors.white),
            titleTextStyle: TextStyle(color: Colors.white, fontSize: 18 * AppTypography.scaleFactor(context), fontWeight: FontWeight.bold),
          ),
          body: isNarrow
              ? Column(
                  children: [
                    Expanded(child: displayCard),
                    SafeArea(child: controlPanel),
                  ],
                )
              : Row(
                  children: [
                    controlPanel,
                    Expanded(child: displayCard),
                  ],
                ),
        );
      },
    );
  }

  Widget _buildControlPanel(bool isNarrow) {
    return Container(
          width: isNarrow ? double.infinity : 140,
          padding: const EdgeInsets.all(8),
          decoration: BoxDecoration(
            color: const Color(0xFF181820),
            border: isNarrow
                ? const Border(top: BorderSide(color: Color(0xFF2A2A36), width: 1))
                : const Border(right: BorderSide(color: Color(0xFF2A2A36), width: 1)),
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            mainAxisSize: MainAxisSize.min,
            children: [
              Text('MT CONTROLS', style: TextStyle(color: Color(0xFFFFCC00), fontSize: 10 * AppTypography.scaleFactor(context), fontWeight: FontWeight.bold)),
              const SizedBox(height: 14),
              Text('Table Range:', style: TextStyle(color: Colors.white, fontSize: 11 * AppTypography.scaleFactor(context), fontWeight: FontWeight.bold)),
              const SizedBox(height: 6),
              Row(
                children: [
                  Expanded(
                    child: TextField(
                      controller: _startController,
                      textAlign: TextAlign.center,
                      keyboardType: TextInputType.number,
                      style: TextStyle(color: Color(0xFFFFCC00), fontSize: 12 * AppTypography.scaleFactor(context), fontWeight: FontWeight.bold),
                      decoration: InputDecoration(
                        filled: true,
                        fillColor: const Color(0xFF1A1A24),
                        contentPadding: EdgeInsets.zero,
                        border: OutlineInputBorder(borderRadius: BorderRadius.circular(4), borderSide: BorderSide.none),
                      ),
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 4),
                    child: Text('to', style: TextStyle(color: Colors.grey, fontSize: 10 * AppTypography.scaleFactor(context))),
                  ),
                  Expanded(
                    child: TextField(
                      controller: _endController,
                      textAlign: TextAlign.center,
                      keyboardType: TextInputType.number,
                      style: TextStyle(color: Color(0xFFFFCC00), fontSize: 12 * AppTypography.scaleFactor(context), fontWeight: FontWeight.bold),
                      decoration: InputDecoration(
                        filled: true,
                        fillColor: const Color(0xFF1A1A24),
                        contentPadding: EdgeInsets.zero,
                        border: OutlineInputBorder(borderRadius: BorderRadius.circular(4), borderSide: BorderSide.none),
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 16),
              SizedBox(
                width: double.infinity,
                child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: const Color(0xFF3B82F6),
                    foregroundColor: Colors.white,
                    padding: const EdgeInsets.symmetric(vertical: 10),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(6)),
                  ),
                  onPressed: _generateRandomQuestion,
                  child: Text('NEW QUESTION', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 10 * AppTypography.scaleFactor(context))),
                ),
              ),
              const SizedBox(height: 8),
              SizedBox(
                width: double.infinity,
                child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: const Color(0xFF2ED573),
                    foregroundColor: const Color(0xFF111111),
                    padding: const EdgeInsets.symmetric(vertical: 10),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(6)),
                  ),
                  onPressed: _revealAnswer,
                  child: Text('SHOW ANSWER', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 10 * AppTypography.scaleFactor(context))),
                ),
              ),
            ],
          ),
    );
  }

  Widget _buildDisplayCard(int product, BoxConstraints constraints, bool isNarrow) {
    final double cardWidth = min(constraints.maxWidth * (isNarrow ? 0.94 : 0.85), 900);
    final double cardHeight = isNarrow
        ? max(constraints.maxHeight * 0.6, 260)
        : min(constraints.maxHeight * 0.85, 500);
    final double timerFontSize = isNarrow ? 20 : 32;
    final double questionFontSize = isNarrow ? 60 : 140;

    return Center(
      child: Container(
        width: cardWidth,
        height: cardHeight,
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: const Color(0xFF181822),
          border: Border.all(color: const Color(0xFFFFCC00), width: 4),
          borderRadius: BorderRadius.circular(16),
          boxShadow: const [
            BoxShadow(color: Colors.black54, blurRadius: 12, offset: Offset(0, 4)),
          ],
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              padding: EdgeInsets.symmetric(horizontal: isNarrow ? 14 : 20, vertical: isNarrow ? 6 : 10),
              decoration: BoxDecoration(
                color: const Color(0xFF2C2C38),
                borderRadius: BorderRadius.circular(28),
                border: Border.all(color: const Color(0xFF444455)),
              ),
              child: Text(
                'Time Taken: $_elapsedTimeStr',
                style: TextStyle(color: const Color(0xFF2ED573), fontSize: timerFontSize, fontWeight: FontWeight.bold),
              ),
            ),
            const Spacer(),
            if (_currentMultiplier == null)
              Text(
                'Click "NEW QUESTION" to Start',
                style: TextStyle(color: Colors.grey, fontSize: isNarrow ? 16 : 18, fontWeight: FontWeight.w600),
                textAlign: TextAlign.center,
              )
            else
              FittedBox(
                fit: BoxFit.scaleDown,
                child: Text(
                  _showAnswer
                      ? '$_currentMultiplier x $_currentMultiplicand = $product'
                      : '$_currentMultiplier x $_currentMultiplicand',
                  style: TextStyle(
                    color: _showAnswer ? const Color(0xFF2ED573) : Colors.white,
                    fontSize: questionFontSize,
                    fontWeight: FontWeight.w900,
                    letterSpacing: 2,
                  ),
                ),
              ),
            const Spacer(),
            Text(
              'Shine Academy Naroda - MT Trainer',
              style: TextStyle(color: Color(0xFF777788), fontSize: 10 * AppTypography.scaleFactor(context)),
            ),
          ],
        ),
      ),
    );
  }
}