import os
import json

allowed_types = {
    'theory', 'formula', 'real_world_example', 'definition',
    'history', 'summary', 'memory_trick', 'short_note',
    'reveal', 'connection', 'match_column',
    'simulation', 'project', 'diagram', 'image', 'visual',
    'animation', 'revision',
    'etymology', 'timeline', 'mind_map', 'board_questions',
    'calculator', 'analogy', 'knowledge_connection', 'story',
    'story_hook',
    'markdown_table',
    'quiz', 'mcq', 'knowledge_check', 'true_false', 'quiz_multiple_choice',
    'practice_question', 'challenge_question', 'challenge', 'mastery_challenge',
    'quiz_mcq', 'quiz_question', 'numerical',
    'ai_discussion', 'ai_tutor_prompt',
    'hook', 'socratic', 'socratic_question', 'socratic_thinking', 'question_socratic',
    'discovery', 'reflection', 'mastery',
    'example', 'case_study', 'worked_example', 'trilingual_card', 'media',
    'activity', 'interactive_activity', 'flashcard', 'teacher_tip', 'common_mistakes',
    'exam_tips', 'heading', 'chapter_title', 'dictionary_link', 'nursery_rhyme',
    'trace_alphabet', 'counting_game', 'color_canvas', 'presentation', 'animated_diagram',
    'dialogue', 'cross_subject_link', 'phonics_blender', 'abacus_simulation'
}

invalid_found = set()

def check_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        blocks_to_check = []
        if isinstance(data, dict):
            if 'blocks' in data:
                blocks_to_check = data['blocks']
            elif 'modules' in data:
                for module in data.get('modules', []):
                    for chapter in module.get('chapters', []):
                        for section in chapter.get('sections', []):
                            for block in section.get('blocks', []):
                                blocks_to_check.append(block)
        elif isinstance(data, list):
            blocks_to_check = data
            
        for block in blocks_to_check:
            if not isinstance(block, dict): continue
            t = block.get('type')
            if t and t not in allowed_types:
                invalid_found.add((filepath, t, block.get('id', 'unknown')))
    except:
        pass

for root, dirs, files in os.walk('app_core'):
    for file in files:
        if file.endswith('.json'):
            check_file(os.path.join(root, file))
            
for filepath, t, bid in invalid_found:
    print(f"INVALID TYPE FOUND: '{t}' in {filepath} (block id: {bid})")
if not invalid_found:
    print("ALL TYPES ARE VALID!")
