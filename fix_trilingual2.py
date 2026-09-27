import os
import re

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # str_pat matches a single string literal
    str_pat = r"(?:'[^'\\]*(?:\\.[^'\\]*)*'|\"[^\"\\]*(?:\\.[^\"\\]*)*\")"
    
    # We want to match: getUIText( <any number of strings> ) <string>
    # The inside of getUIText can just be matched as anything up to the closing `)`
    # provided that after `)` there is a string literal.
    
    # A safer way is to match `getUIText(` followed by any number of strings, `)`, and another string.
    # But since we just want to move the `)` past the next string literal if it's right after it:
    # Let's match `)` that is followed by whitespace and a string literal, but only if it's part of getUIText.
    # Actually, simpler: find `getUIText( ... ) \n "string"` and move the `)`
    
    new_content = content
    while True:
        # Match `getUIText( content_without_parens ) \s* string_literal`
        # wait, content_without_parens might contain parens? No, getUIText("...") doesn't usually contain nested unescaped parens outside strings.
        # But to be safe, let's just find `TrilingualService.instance.getUIText` and manually parse it.
        
        changed = False
        start = 0
        while True:
            idx = new_content.find('TrilingualService.instance.getUIText(', start)
            if idx == -1:
                break
            
            # Find the closing parenthesis of getUIText
            # We can use a simple parenthesis counter, keeping track of strings
            in_string = False
            string_char = None
            escape = False
            paren_count = 0
            
            closing_idx = -1
            
            for i in range(idx + len('TrilingualService.instance.getUIText('), len(new_content)):
                c = new_content[i]
                if not in_string:
                    if c in ("'", '"'):
                        in_string = True
                        string_char = c
                        escape = False
                    elif c == '(':
                        paren_count += 1
                    elif c == ')':
                        if paren_count == 0:
                            closing_idx = i
                            break
                        paren_count -= 1
                else:
                    if escape:
                        escape = False
                    elif c == '\\':
                        escape = True
                    elif c == string_char:
                        in_string = False
                        
            if closing_idx != -1:
                # We found the closing `)`. Now let's see if the next non-whitespace thing is a string literal
                next_char_idx = -1
                for i in range(closing_idx + 1, len(new_content)):
                    if not new_content[i].isspace():
                        next_char_idx = i
                        break
                        
                if next_char_idx != -1 and new_content[next_char_idx] in ("'", '"'):
                    # Found another string literal!
                    # Find the end of this string literal
                    in_string = True
                    string_char = new_content[next_char_idx]
                    escape = False
                    end_str_idx = -1
                    for i in range(next_char_idx + 1, len(new_content)):
                        c = new_content[i]
                        if escape:
                            escape = False
                        elif c == '\\':
                            escape = True
                        elif c == string_char:
                            end_str_idx = i
                            break
                            
                    if end_str_idx != -1:
                        # Move the `)` to after the string literal
                        # Replace `)` with ` `, and insert `)` after end_str_idx
                        new_content = new_content[:closing_idx] + ' ' + new_content[closing_idx+1:end_str_idx+1] + ')' + new_content[end_str_idx+1:]
                        changed = True
                        # Restart from start of file since indices changed
                        break
            
            start = idx + 1
            
        if not changed:
            break

    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")

for root, dirs, files in os.walk('lib'):
    for file in files:
        if file.endswith('.dart'):
            fix_file(os.path.join(root, file))
