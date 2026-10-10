import 'package:flutter/material.dart';
import 'package:flutter_markdown/flutter_markdown.dart';
import 'package:flutter_markdown_latex/flutter_markdown_latex.dart';
import 'package:markdown/markdown.dart' as md;
import 'package:google_fonts/google_fonts.dart';
import '../../../../core/widgets/presentation_builder.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../foundation/theme/app_typography.dart';
import 'package:shine_academy_naroda/features/common/widgets/math_title.dart';

class MarkdownTableWidget extends StatelessWidget {
  final Map<String, dynamic> block;

  const MarkdownTableWidget({super.key, required this.block});

  @override
  Widget build(BuildContext context) {
    final body = TrilingualService.instance.getLocalizedText(block, 'body');
    final title = TrilingualService.instance.getLocalizedText(block, 'title');

    return PresentationBuilder(
      builder: (context, scale) {
        return Container(
          margin: const EdgeInsets.only(bottom: 24),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(16),
            border: Border.all(color: Colors.blueGrey.shade200, width: 1.5),
            boxShadow: [
              BoxShadow(
                color: Colors.blueGrey.withValues(alpha: 0.1),
                blurRadius: 10,
                offset: const Offset(0, 4),
              )
            ],
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              if (title.isNotEmpty)
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                  decoration: BoxDecoration(
                    color: Colors.blueGrey.shade50,
                    borderRadius: const BorderRadius.vertical(top: Radius.circular(14)),
                    border: Border(bottom: BorderSide(color: Colors.blueGrey.shade200, width: 1.5)),
                  ),
                  child: Row(
                    children: [
                      Icon(Icons.table_chart, color: Colors.blueGrey.shade700),
                      const SizedBox(width: 12),
                      Expanded(
                        child: MathTitle(
                          title,
                          style: GoogleFonts.poppins(
                            fontSize: 18 * scale,
                            fontWeight: FontWeight.bold,
                            color: Colors.blueGrey.shade900,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              Padding(
                padding: const EdgeInsets.all(20),
                child: MarkdownBody(
                  data: body,
                  selectable: true,
                  builders: {
                    'latex': LatexElementBuilder(),
                  },
                  extensionSet: md.ExtensionSet(
                    <md.BlockSyntax>[...md.ExtensionSet.gitHubFlavored.blockSyntaxes, LatexBlockSyntax()],
                    <md.InlineSyntax>[...md.ExtensionSet.gitHubFlavored.inlineSyntaxes, LatexInlineSyntax()],
                  ),
                  styleSheet: MarkdownStyleSheet(
                    p: AppTypography.body(context, color: Theme.of(context).colorScheme.onSurface).copyWith(height: 1.6),
                    tableBody: AppTypography.bodySmall(context, color: Theme.of(context).colorScheme.onSurface),
                    tableHead: AppTypography.bodySmall(context, color: Colors.blueGrey.shade900).copyWith(fontWeight: FontWeight.bold),
                    tableBorder: TableBorder.all(
                      color: Colors.blueGrey.shade300,
                      width: 1,
                    ),
                    tableCellsPadding: const EdgeInsets.all(12),
                    tableColumnWidth: const IntrinsicColumnWidth(),
                  ),
                ),
              ),
            ],
          ),
        );
      },
    );
  }
}
