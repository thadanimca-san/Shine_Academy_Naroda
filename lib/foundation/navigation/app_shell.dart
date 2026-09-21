import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../../core/services/trilingual_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class AppShell extends StatelessWidget {
  final Widget child;

  const AppShell({super.key, required this.child});

  int _calculateSelectedIndex(BuildContext context) {
    final String location = GoRouterState.of(context).uri.toString();
    if (location.startsWith('/learning')) return 1;
    if (location.startsWith('/assessment')) return 2;
    if (location.startsWith('/community')) return 3;
    return 0; // dashboard
  }

  void _onItemTapped(int index, BuildContext context) {
    switch (index) {
      case 0:
        context.go('/');
        break;
      case 1:
        context.go('/learning');
        break;
      case 2:
        context.go('/assessment');
        break;
      case 3:
        context.go('/community');
        break;
    }
  }

  @override
  Widget build(BuildContext context) {
    final int currentIndex = _calculateSelectedIndex(context);

    // to a BottomNavigationBar for this initial foundation.
    return ListenableBuilder(
      listenable: TrilingualService.instance,
      builder: (context, _) {
        final ts = TrilingualService.instance;
        return Scaffold(
          body: child,
          bottomNavigationBar: NavigationBar(
            selectedIndex: currentIndex,
            onDestinationSelected: (index) => _onItemTapped(index, context),
            destinations: [
              NavigationDestination(
                icon: Icon(Icons.dashboard_outlined),
                selectedIcon: Icon(Icons.dashboard),
                label: ts.getUIText(TrilingualService.instance.getUIText('Home')),
              ),
              NavigationDestination(
                icon: Icon(Icons.menu_book_outlined),
                selectedIcon: Icon(Icons.menu_book),
                label: ts.getUIText(TrilingualService.instance.getUIText('Learning')),
              ),
              NavigationDestination(
                icon: Icon(Icons.quiz_outlined),
                selectedIcon: Icon(Icons.quiz),
                label: ts.getUIText(TrilingualService.instance.getUIText('Assessment')),
              ),
              NavigationDestination(
                icon: Icon(Icons.forum_outlined),
                selectedIcon: Icon(Icons.forum),
                label: ts.getUIText(TrilingualService.instance.getUIText('Community')),
              ),
            ],
          ),
        );
      },
    );
  }
}
