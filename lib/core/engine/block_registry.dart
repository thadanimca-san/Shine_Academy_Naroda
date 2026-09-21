import 'package:flutter/material.dart';

typedef BlockValidatorFunction = void Function(Map<String, dynamic> block);
typedef BlockBuilderFunction = Widget Function(Map<String, dynamic> block);

class BlockDefinition {
  final String type;
  final BlockValidatorFunction validator;
  final BlockBuilderFunction builder;

  const BlockDefinition({
    required this.type,
    required this.validator,
    required this.builder,
  });
}

class BlockRegistry {
  static final BlockRegistry instance = BlockRegistry._internal();
  BlockRegistry._internal();

  final Map<String, BlockDefinition> _registry = {};

  void register(BlockDefinition definition) {
    _registry[definition.type] = definition;
  }

  void registerAll(List<BlockDefinition> definitions) {
    for (var def in definitions) {
      register(def);
    }
  }

  bool hasBlock(String type) => _registry.containsKey(type);

  void validate(Map<String, dynamic> block) {
    final type = block['type'];
    if (type == null) {
      throw const FormatException("Missing 'type' in block.");
    }

    final def = _registry[type];
    if (def != null) {
      def.validator(block);
    } else {
      // If we don't have a specific validator for this block type yet, 
      // we allow it to pass so the UI can show the diagnostic error block.
    }
  }

  Widget? build(Map<String, dynamic> block) {
    final type = block['type'];
    if (type == null) return null;

    final def = _registry[type];
    if (def != null) {
      return def.builder(block);
    }
    
    return null; // Return null so LearningEngineScreen can show the diagnostic error
  }
}
