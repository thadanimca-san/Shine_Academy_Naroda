import 'package:flutter/material.dart';

import '../data/syllabus_data.dart';
import '../models/syllabus.dart';
import '../services/greeting_engine.dart';
import '../services/profile_service.dart';
import '../services/progress_service.dart';
import '../theme/tokens.dart';
import '../widgets/about_sheet.dart';
import '../widgets/chapter_card.dart';
import '../widgets/soft_card.dart';
import '../widgets/topic_tile.dart';
import 'sim_host.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final TextEditingController _search = TextEditingController();
  String get _query => _search.text.trim().toLowerCase();

  @override
  void initState() {
    super.initState();
    ProgressService.instance.addListener(_onProgress);
    _search.addListener(() => setState(() {}));
  }

  @override
  void dispose() {
    ProgressService.instance.removeListener(_onProgress);
    _search.dispose();
    super.dispose();
  }

  void _onProgress() {
    if (mounted) setState(() {});
  }

  void _openTopic(Topic topic) {
    FocusScope.of(context).unfocus();
    Navigator.of(context).push(SimHost.route(topic));
  }

  // ── Smart greeting (personal, physics-flavored, time-aware) ───────
  ({String hello, String line}) _greeting() {
    final progress = ProgressService.instance;
    final last = progress.lastTopicId == null ? null : topicById(progress.lastTopicId!);
    final g = GreetingEngine.compose(
      profile: ProfileService.instance,
      progress: progress,
      lastTopicTitle: last?.title,
    );
    return (hello: g.headline, line: g.subline);
  }

  // ── Search ────────────────────────────────────────────────────────
  List<(Topic, Chapter)> _searchResults() {
    final q = _query;
    final out = <(Topic, Chapter)>[];
    for (final c in syllabus) {
      for (final t in c.topics) {
        final haystack = '${t.title} ${t.tagline} ${c.title} ${c.unit}'.toLowerCase();
        if (haystack.contains(q)) out.add((t, c));
      }
    }
    return out;
  }

  @override
  Widget build(BuildContext context) {
    final progress = ProgressService.instance;
    final greeting = _greeting();
    final lastTopic = progress.lastTopicId == null ? null : topicById(progress.lastTopicId!);
    final bottomInset = MediaQuery.paddingOf(context).bottom;

    return Scaffold(
      body: GestureDetector(
        behavior: HitTestBehavior.translucent,
        onTap: () => FocusScope.of(context).unfocus(),
        child: CustomScrollView(
          keyboardDismissBehavior: ScrollViewKeyboardDismissBehavior.onDrag,
          slivers: [
            SliverPadding(
              padding: EdgeInsets.fromLTRB(
                  Gap.x5, MediaQuery.paddingOf(context).top + Gap.x5, Gap.x5, Gap.x2),
              sliver: SliverToBoxAdapter(child: _header(greeting)),
            ),
            SliverPadding(
              padding: const EdgeInsets.fromLTRB(Gap.x5, Gap.x3, Gap.x5, Gap.x2),
              sliver: SliverToBoxAdapter(child: _searchField()),
            ),
            if (_query.isNotEmpty)
              SliverPadding(
                padding: const EdgeInsets.fromLTRB(Gap.x5, Gap.x2, Gap.x5, Gap.x4),
                sliver: SliverToBoxAdapter(child: _searchList()),
              )
            else ...[
              if (lastTopic != null && lastTopic.isAvailable)
                SliverPadding(
                  padding: const EdgeInsets.fromLTRB(Gap.x5, Gap.x3, Gap.x5, Gap.x1),
                  sliver: SliverToBoxAdapter(child: _continueCard(lastTopic)),
                ),
              SliverPadding(
                padding: const EdgeInsets.fromLTRB(Gap.x5, Gap.x3, Gap.x5, 0),
                sliver: SliverToBoxAdapter(child: _statsStrip(progress)),
              ),
              ..._syllabusSlivers(lastTopic),
              SliverToBoxAdapter(child: _footer()),
            ],
            SliverToBoxAdapter(child: SizedBox(height: bottomInset + Gap.x4)),
          ],
        ),
      ),
    );
  }

  Widget _header(({String hello, String line}) greeting) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(greeting.hello, style: Type.display),
              const SizedBox(height: Gap.x2),
              Text(greeting.line, style: Type.body.copyWith(color: Palette.textMuted)),
            ],
          ),
        ),
        const SizedBox(width: Gap.x3),
        Semantics(
          button: true,
          label: 'About Shine Academy',
          child: InkWell(
            borderRadius: BorderRadius.circular(Corner.pill),
            onTap: () => showAboutSheet(context),
            child: Container(
              width: 42,
              height: 42,
              decoration: BoxDecoration(
                color: Palette.primarySoft,
                shape: BoxShape.circle,
                border: Border.all(color: Palette.border),
              ),
              child: Icon(Icons.school_rounded, color: Palette.primary, size: 21),
            ),
          ),
        ),
      ],
    );
  }

  Widget _searchField() {
    return Container(
      decoration: BoxDecoration(
        color: Palette.surface,
        borderRadius: BorderRadius.circular(Corner.lg),
        border: Border.all(color: Palette.border),
      ),
      child: TextField(
        controller: _search,
        textInputAction: TextInputAction.search,
        style: Type.body.copyWith(color: Palette.textStrong),
        decoration: InputDecoration(
          hintText: 'Search any concept — “friction”, “orbits”, “gas laws”…',
          hintStyle: Type.body.copyWith(color: Palette.textFaint, fontSize: 14),
          prefixIcon: Icon(Icons.search_rounded, color: Palette.textFaint),
          suffixIcon: _query.isEmpty
              ? null
              : IconButton(
                  icon: Icon(Icons.close_rounded, size: 18, color: Palette.textMuted),
                  onPressed: _search.clear,
                ),
          border: InputBorder.none,
          contentPadding: const EdgeInsets.symmetric(horizontal: Gap.x4, vertical: 14),
        ),
      ),
    );
  }

  Widget _searchList() {
    final results = _searchResults();
    if (results.isEmpty) {
      return Padding(
        padding: const EdgeInsets.symmetric(vertical: Gap.x10),
        child: Column(
          children: [
            Icon(Icons.travel_explore_rounded, size: 40, color: Palette.textFaint),
            const SizedBox(height: Gap.x3),
            Text('Nothing matched “${_search.text.trim()}”', style: Type.bodyStrong),
            const SizedBox(height: Gap.x1),
            Text(TrilingualService.instance.getUIText('Try a chapter name or a simpler word, like “waves” or “heat”.'),
                textAlign: TextAlign.center, style: Type.caption),
          ],
        ),
      );
    }
    return SoftCard(
      padding: const EdgeInsets.symmetric(horizontal: Gap.x2, vertical: Gap.x1),
      child: Column(
        children: [
          for (final (t, c) in results)
            TopicTile(
              topic: t,
              tint: c.tint,
              visited: ProgressService.instance.isVisited(t.id),
              onOpen: () => _openTopic(t),
            ),
        ],
      ),
    );
  }

  Widget _continueCard(Topic topic) {
    final chapter = chapterOf(topic);
    return SoftCard(
      onTap: () => _openTopic(topic),
      color: Palette.primary,
      padding: const EdgeInsets.all(Gap.x4),
      child: Row(
        children: [
          Container(
            width: 44,
            height: 44,
            decoration: BoxDecoration(
              color: Colors.white.withValues(alpha: 0.16),
              borderRadius: BorderRadius.circular(Corner.md),
            ),
            child: Icon(topic.icon, color: Colors.white, size: 22),
          ),
          const SizedBox(width: Gap.x3),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(TrilingualService.instance.getUIText('CONTINUE LEARNING'),
                    style: Type.label.copyWith(color: Colors.white.withValues(alpha: 0.75), fontSize: 10)),
                const SizedBox(height: 3),
                Text(topic.title,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: Type.heading.copyWith(color: Colors.white)),
                const SizedBox(height: 2),
                Text(chapter.title,
                    style: Type.caption.copyWith(color: Colors.white.withValues(alpha: 0.75))),
              ],
            ),
          ),
          Icon(Icons.play_circle_fill_rounded, color: Colors.white, size: 32),
        ],
      ),
    );
  }

  Widget _statsStrip(ProgressService progress) {
    final labsReady = allTopics.where((t) => t.isAvailable).length;
    return Row(
      children: [
        _stat('${progress.visitedCount}', 'topics explored'),
        const SizedBox(width: Gap.x3),
        _stat('$labsReady', 'labs ready'),
        const SizedBox(width: Gap.x3),
        _stat('${syllabus.length}', 'chapters'),
      ],
    );
  }

  Widget _stat(String value, String label) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: Gap.x3),
        decoration: BoxDecoration(
          color: Palette.surface,
          borderRadius: BorderRadius.circular(Corner.md),
          border: Border.all(color: Palette.border),
        ),
        child: Column(
          children: [
            Text(value, style: Type.title.copyWith(color: Palette.primary)),
            const SizedBox(height: 2),
            Text(label, style: Type.caption.copyWith(fontSize: 11)),
          ],
        ),
      ),
    );
  }

  List<Widget> _syllabusSlivers(Topic? lastTopic) {
    final slivers = <Widget>[];
    String? currentUnit;
    for (final chapter in syllabus) {
      if (chapter.unit != currentUnit) {
        currentUnit = chapter.unit;
        slivers.add(SliverPadding(
          padding: const EdgeInsets.fromLTRB(Gap.x5, Gap.x6, Gap.x5, Gap.x2),
          sliver: SliverToBoxAdapter(
            child: Text(currentUnit.toUpperCase(), style: Type.label),
          ),
        ));
      }
      final holdsLast =
          lastTopic != null && chapter.topics.any((t) => t.id == lastTopic.id);
      slivers.add(SliverPadding(
        padding: const EdgeInsets.fromLTRB(Gap.x5, Gap.x1, Gap.x5, Gap.x2),
        sliver: SliverToBoxAdapter(
          child: ChapterCard(
            chapter: chapter,
            initiallyExpanded: holdsLast,
            onOpenTopic: _openTopic,
          ),
        ),
      ));
    }
    return slivers;
  }

  Widget _footer() {
    return Padding(
      padding: const EdgeInsets.only(top: Gap.x6),
      child: Center(
        child: TextButton.icon(
          onPressed: () => showAboutSheet(context),
          icon: Icon(Icons.stars_rounded, size: 15, color: Palette.accent),
          label: Text(TrilingualService.instance.getUIText('Shine Academy, Naroda · About'),
              style: Type.caption.copyWith(color: Palette.textMuted)),
        ),
      ),
    );
  }
}
