import 'package:flutter/material.dart';
import '../../../../foundation/theme/app_colors.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class ColorCanvasWidget extends StatefulWidget {
  final Map<String, dynamic> data;

  const ColorCanvasWidget({super.key, required this.data});

  @override
  State<ColorCanvasWidget> createState() => _ColorCanvasWidgetState();
}

class _ColorCanvasWidgetState extends State<ColorCanvasWidget> {
  Color? _selectedColor;
  Color _shapeFillColor = Colors.white;

  final List<Color> _palette = [
    Colors.red,
    Colors.blue,
    Colors.green,
    Colors.yellow,
    Colors.purple,
    Colors.orange,
  ];

  @override
  Widget build(BuildContext context) {
    // We will just use an Icon to represent the shape for simplicity.
    final String shapeStr = widget.data['shape'] ?? 'star';
    IconData shapeIcon;
    switch (shapeStr.toLowerCase()) {
      case 'apple':
        shapeIcon = Icons.apple;
        break;
      case 'heart':
        shapeIcon = Icons.favorite;
        break;
      case 'sun':
        shapeIcon = Icons.wb_sunny;
        break;
      case 'car':
        shapeIcon = Icons.directions_car;
        break;
      case 'tree':
        shapeIcon = Icons.park;
        break;
      case 'house':
        shapeIcon = Icons.home;
        break;
      case 'rainbow':
        shapeIcon = Icons.cloud; // fallback
        break;
      case 'ball':
        shapeIcon = Icons.sports_soccer;
        break;
      case 'boat':
        shapeIcon = Icons.directions_boat;
        break;
      case 'scenery':
        shapeIcon = Icons.landscape;
        break;
      case 'dog':
        shapeIcon = Icons.pets;
        break;
      case 'hand':
        shapeIcon = Icons.front_hand;
        break;
      case 'face':
        shapeIcon = Icons.face;
        break;
      case 'cat':
        shapeIcon = Icons.pets;
        break;
      case 'star':
      default:
        shapeIcon = Icons.star;
        break;
    }

    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: Colors.grey.shade300, width: 2),
      ),
      child: Column(
        children: [
          Text(TrilingualService.instance.getUIText('Color the Shape!'),
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface),
          ),
          const SizedBox(height: 32),
          
          // The Canvas / Shape
          GestureDetector(
            onTap: () {
              if (_selectedColor != null) {
                setState(() {
                  _shapeFillColor = _selectedColor!;
                });
              }
            },
            child: Container(
              width: 200,
              height: 200,
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(20),
                border: Border.all(color: Theme.of(context).colorScheme.onSurfaceVariant, width: 2, style: BorderStyle.solid),
                boxShadow: [BoxShadow(color: Theme.of(context).colorScheme.onSurface.withOpacity(0.12), blurRadius: 10)],
              ),
              child: Center(
                child: Icon(
                  shapeIcon,
                  size: 150,
                  color: _shapeFillColor == Colors.white ? Colors.grey[200] : _shapeFillColor,
                ),
              ),
            ),
          ),
          
          const SizedBox(height: 32),
          Text(TrilingualService.instance.getUIText('Pick a Color:'), style: TextStyle(fontSize: 18, fontWeight: FontWeight.w600)),
          const SizedBox(height: 16),
          
          // The Palette
          Wrap(
            spacing: 12,
            runSpacing: 12,
            alignment: WrapAlignment.center,
            children: _palette.map((color) {
              final isSelected = _selectedColor == color;
              return GestureDetector(
                onTap: () {
                  setState(() {
                    _selectedColor = color;
                  });
                },
                child: Container(
                  width: 50,
                  height: 50,
                  decoration: BoxDecoration(
                    color: color,
                    shape: BoxShape.circle,
                    border: Border.all(
                      color: isSelected ? Colors.black87 : Colors.transparent,
                      width: 4,
                    ),
                    boxShadow: [
                      if (isSelected)
                        BoxShadow(color: Theme.of(context).colorScheme.onSurface.withOpacity(0.26), blurRadius: 8, spreadRadius: 2)
                    ],
                  ),
                ),
              );
            }).toList(),
          ),
          
          const SizedBox(height: 24),
          TextButton.icon(
            onPressed: () {
              setState(() {
                _shapeFillColor = Colors.white;
                _selectedColor = null;
              });
            },
            icon: Icon(Icons.refresh),
            label: Text(TrilingualService.instance.getUIText('Start Over')),
          )
        ],
      ),
    );
  }
}
