import re

path = '/home/ubuntu/Shine_Academy_Naroda/lib/foundation/navigation/app_router.dart'
with open(path, 'r') as f:
    content = f.read()

replacement = """
        GoRoute(
          path: '/curriculum/:grade/:subject',
          builder: (context, state) {
            final grade = state.pathParameters['grade']!;
            return SubjectListScreen(curriculumId: grade);
          },
        ),
        GoRoute(
          path: '/curriculum/:grade/:subject/chapters',
          builder: (context, state) {
            final grade = state.pathParameters['grade']!;
            final subject = state.pathParameters['subject']!;
            return ChapterListScreen(curriculumId: grade, subjectId: subject);
          },
        ),
        GoRoute(
          path: '/curriculum/:grade/:subject/chapter/:chapterId',
          builder: (context, state) {
            final chapterId = state.pathParameters['chapterId']!;
            return ChapterDetailScreen(assetPath: chapterId);
          },
        ),
        GoRoute(
          path: '/learning/engine/:chapterId',
          builder: (context, state) {
            return const PedagogyEngineScreen();
          },
        ),
        GoRoute(
          path: '/learning/engine/gold/:chapterId',
          builder: (context, state) {
            final chapterId = state.pathParameters['chapterId']!;
            return GoldStandardChapterView(moduleId: chapterId);
          },
        ),
        GoRoute(
          path: '/assessment/engine/:chapterId',
          builder: (context, state) {
            final chapterId = state.pathParameters['chapterId']!;
            return ExamEngineScreen(moduleId: chapterId);
          },
        ),
        GoRoute(
          path: '/assessment/bank/:chapterId',
          builder: (context, state) {
            final chapterId = state.pathParameters['chapterId']!;
            return QuestionBankScreen(moduleId: chapterId);
          },
        ),
        GoRoute(
          path: '/assessment/paper',
          builder: (context, state) {
            return const QuestionPaperViewScreen(questions: [], title: "Test");
          },
        ),
"""

pattern = r"GoRoute\(\s*path: '/curriculum/:grade/:subject',.*?builder: \(context, state\) \{.*?return QuestionPaperViewScreen\(paper: paper\);\s*},\s*\),"

content = re.sub(pattern, replacement.strip() + ',', content, flags=re.DOTALL)

with open(path, 'w') as f:
    f.write(content)
