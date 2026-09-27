import re

with open('lib/features/learning/school/english/screens/reading_passage_screen.dart', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update _Stage enum
content = content.replace('enum _Stage { reading, questions, done }', 'enum _Stage { active, done }')

# 2. Update initial stage
content = content.replace('_Stage _stage = _Stage.reading;', '_Stage _stage = _Stage.active;')

# 3. Remove _startQuestions
content = re.sub(r'  void _startQuestions\(\) => setState\(\(\) => _stage = _Stage\.questions\);\n\n', '', content)

# 4. Update build method switch
old_switch = '''          child: switch (_stage) {
            _Stage.reading => _buildReading(context),
            _Stage.questions => _buildQuestion(context),
            _Stage.done => _buildDone(context),
          },'''

new_switch = '''          child: _stage == _Stage.done 
              ? _buildDone(context) 
              : _buildCombined(context),'''
content = content.replace(old_switch, new_switch)

# 5. Add _buildCombined method
build_combined = '''
  Widget _buildCombined(BuildContext context) {
    return Column(
      children: [
        Expanded(
          flex: 4,
          child: _buildReading(context),
        ),
        const Divider(height: 1, thickness: 2, color: AppColors.rule),
        Expanded(
          flex: 6,
          child: _buildQuestion(context),
        ),
      ],
    );
  }

  Widget _buildReading'''
content = content.replace('  Widget _buildReading', build_combined)

# 6. Update the tip in _buildReading
old_tip = '''          if (passage.glosses.isNotEmpty && _lang == _Language.english)
            const Padding(
              padding: EdgeInsets.only(bottom: 10),
              child: Text(
                'Tap any underlined word for its meaning.',
                style: TextStyle(fontSize: 11.5, color: AppColors.inkFaint, fontStyle: FontStyle.italic),
              ),
            ),'''
new_tip = '''          const Padding(
            padding: EdgeInsets.only(bottom: 10),
            child: Text(
              '💡 Tip: Long-press any word to search in the dictionary.',
              style: TextStyle(fontSize: 12.5, color: AppColors.inkFaint, fontStyle: FontStyle.italic, fontWeight: FontWeight.w600),
            ),
          ),'''
content = content.replace(old_tip, new_tip)

# 7. Remove the "Answer questions" button from _buildReading
old_button = '''          const SizedBox(height: 28),
          SizedBox(
            width: double.infinity,
            child: FilledButton(
              onPressed: _startQuestions,
              style: FilledButton.styleFrom(
                backgroundColor: AppColors.saffron,
                padding: const EdgeInsets.symmetric(vertical: 14),
              ),
              child: Text('Answer ${passage.questions.length} questions about this story'),
            ),
          ),'''
content = content.replace(old_button, '')

with open('lib/features/learning/school/english/screens/reading_passage_screen.dart', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated reading_passage_screen.dart successfully.")
