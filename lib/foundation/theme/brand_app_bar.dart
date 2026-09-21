import 'package:flutter/material.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class BrandAppBar extends StatelessWidget implements PreferredSizeWidget {
  final String title;
  final List<Widget>? actions;
  final PreferredSizeWidget? bottom;
  
  const BrandAppBar({super.key, required this.title, this.actions, this.bottom});

  @override
  Widget build(BuildContext context) {
    return AppBar(
      // We add the logo to the left side (leading) or right before the title.
      // Using a Row in title allows us to keep it beautifully aligned.
      title: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        mainAxisSize: MainAxisSize.min,
        children: [
          Image.asset(
            'assets/shineacademynarodalogo.jpg',
            height: 32, // Perfect size for AppBar
            fit: BoxFit.contain,
          ),
          const SizedBox(width: 8),
          Flexible(
            child: Text(
              title,
              overflow: TextOverflow.ellipsis,
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
          ),
        ],
      ),
      backgroundColor: Colors.indigo,
      foregroundColor: Colors.white, // Ensure text is white on indigo
      centerTitle: true,
      elevation: 2,
      shadowColor: Colors.black26,
      actions: [
        ListenableBuilder(
          listenable: TrilingualService.instance,
          builder: (context, _) {
            final activeLang = TrilingualService.instance.activeViewLanguage;
            
            Widget buildLangChip(String label, String code) {
              final isActive = activeLang == code;
              return GestureDetector(
                onTap: () => TrilingualService.instance.setActiveViewLanguage(code),
                child: Container(
                  margin: const EdgeInsets.symmetric(horizontal: 2),
                  padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                  decoration: BoxDecoration(
                    color: isActive ? Colors.white : Colors.transparent,
                    borderRadius: BorderRadius.circular(4),
                    border: Border.all(
                      color: isActive ? Colors.transparent : Colors.white54,
                      width: 1,
                    ),
                  ),
                  child: Text(
                    label,
                    style: TextStyle(
                      color: isActive ? Colors.indigo : Colors.white,
                      fontWeight: FontWeight.bold,
                      fontSize: 12,
                    ),
                  ),
                ),
              );
            }

            return Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                buildLangChip('EN', 'en'),
                buildLangChip('HI', 'hi'),
                buildLangChip('GU', 'gu'),
                const SizedBox(width: 8),
              ],
            );
          },
        ),
        if (actions != null) ...actions!,
        const SizedBox(width: 8),
      ],
      bottom: bottom,
    );
  }

  @override
  Size get preferredSize {
    final bottomHeight = bottom?.preferredSize.height ?? 0.0;
    return Size.fromHeight(kToolbarHeight + bottomHeight);
  }
}
