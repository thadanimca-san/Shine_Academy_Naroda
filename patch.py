import re

with open('lib/features/assessment/exam_engine_screen.dart', 'r') as f:
    content = f.read()

content = content.replace('''        } catch (e) {
          // 3. Fallback to very old Assessment Engine
          allQuestions = await AssessmentEngine.instance.extractQuestionsForModule(
            widget.moduleId, 
            ['quiz', 'true_false']
          );
        }''', '''        } catch (e) {
          throw Exception("CRITICAL MOCK TEST ERROR: " + e.toString());
        }''')

with open('lib/features/assessment/exam_engine_screen.dart', 'w') as out:
    out.write(content)

print("Patched fallback logic!")
