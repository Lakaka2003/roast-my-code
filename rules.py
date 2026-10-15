import re

def roast_code(lines, strict=False):
    roasts = []
    for i, line in enumerate(lines):
        line_num = i + 1
        line_stripped = line.strip()
        
        if not line_stripped or line_stripped.startswith('#'):
            if not strict and re.search(r'#.*TODO', line, re.IGNORECASE):
                roasts.append((str(line_num), line_stripped, "That 'TODO' is just there to make you feel better. You'll never fix it."))
            continue

        # MINOR RULES (Ignored in --strict mode)
        if not strict:
            if re.match(r'^[a-zA-Z]\s*=', line_stripped):
                roasts.append((str(line_num), line_stripped, "Single-letter variable? Are you a programmer or playing Hangman?"))
            
            if line_stripped == "pass":
                roasts.append((str(line_num), line_stripped, "'pass'? Just like your career will pass you by."))
                
            if re.search(r'print\(\s*["\'](test|here|123|hello|a|debug)["\']\s*\)', line_stripped, re.IGNORECASE):
                roasts.append((str(line_num), line_stripped, "Debugging with print('test')? There are tools for that, caveman."))

            if re.search(r'==\s*(True|False)', line_stripped):
                roasts.append((str(line_num), line_stripped, "Using '== True'? What's next, 'if (True == True) == True'?"))

        # MAJOR RULES (Always run, indicating serious logic or security flaws)
        if line_stripped == "except:":
            roasts.append((str(line_num), line_stripped, "Sweeping errors under the rug with a bare 'except:'. Brave, but irresponsible."))
            
        if line_stripped == "while True:":
            roasts.append((str(line_num), line_stripped, "Infinite loop. Just like the time you're wasting rewriting this code."))

        if re.search(r'\beval\s*\(', line_stripped):
            roasts.append((str(line_num), line_stripped, "Using eval()? Do you want to get hacked? Because that's how you get hacked."))

        if line_stripped.startswith("global "):
            roasts.append((str(line_num), line_stripped, "Global variables? What year is this, 1995?"))

        if re.search(r'=\s*open\(', line_stripped) and "with " not in line:
            roasts.append((str(line_num), line_stripped, "Opening a file without 'with'? Don't forget to close it... oh wait, you probably forgot."))

        indentation_level = len(line) - len(line.lstrip())
        if indentation_level >= 16:
            shortened = line_stripped[:35] + "..." if len(line_stripped) > 35 else line_stripped
            roasts.append((str(line_num), shortened, "Deeply nested code. Are we writing Python or drawing a pyramid?"))

    return roasts
