import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dictionary_popup.dart';

class UniversalSelectionArea extends StatelessWidget {
  final Widget child;

  const UniversalSelectionArea({Key? key, required this.child}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SelectionArea(
      contextMenuBuilder: (BuildContext context, SelectableRegionState selectableRegionState) {
        final List<ContextMenuButtonItem> buttonItems = selectableRegionState.contextMenuButtonItems.toList();
        final selectedText = selectableRegionState.textEditingValue.selection.textInside(selectableRegionState.textEditingValue.text);
        
        if (selectedText.trim().isNotEmpty) {
          buttonItems.insert(0, ContextMenuButtonItem(
            label: '📖 Dictionary',
            onPressed: () {
              selectableRegionState.hideToolbar();
              UniversalDictionaryPopup.show(context, selectedText.trim());
            },
          ));
        }
        
        return AdaptiveTextSelectionToolbar.buttonItems(
          anchors: selectableRegionState.contextMenuAnchors,
          buttonItems: buttonItems,
        );
      },
      child: child,
    );
  }
}
