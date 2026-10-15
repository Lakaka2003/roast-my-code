import sys
import re
from rich.console import Console
from rich.table import Table

console = Console()

def roast_code(lines):
    roasts = []
    for i, line in enumerate(lines):
        line_num = i + 1
        line_stripped = line.strip()
        
        if not line_stripped or line_stripped.startswith('#'):
            if re.search(r'#.*TODO', line, re.IGNORECASE):
                roasts.append((str(line_num), line_stripped, "That 'TODO' is just there to make you feel better. You'll never fix it."))
            continue

        # Rule: Single-letter variables
        if re.match(r'^[a-zA-Z]\s*=', line_stripped):
            roasts.append((str(line_num), line_stripped, "Single-letter variable? Are you a programmer or playing Hangman?"))
        
        # Rule: Bare except
        if line_stripped == "except:":
            roasts.append((str(line_num), line_stripped, "Sweeping errors under the rug with a bare 'except:'. Brave, but irresponsible."))
            
        # Rule: Pass statement
        if line_stripped == "pass":
            roasts.append((str(line_num), line_stripped, "'pass'? Just like your career will pass you by."))
            
        # Rule: Primitive debugging
        if re.search(r'print\(\s*["\'](test|here|123|hello|a|debug)["\']\s*\)', line_stripped, re.IGNORECASE):
            roasts.append((str(line_num), line_stripped, "Debugging with print('test')? There are tools for that, caveman."))
            
        # Rule: Infinite loops
        if line_stripped == "while True:":
            roasts.append((str(line_num), line_stripped, "Infinite loop. Just like the time you're wasting rewriting this code."))

        # ADVANCED RULE 1: eval() security risk
        if re.search(r'\beval\s*\(', line_stripped):
            roasts.append((str(line_num), line_stripped, "Using eval()? Do you want to get hacked? Because that's how you get hacked."))

        # ADVANCED RULE 2: Redundant boolean comparison
        if re.search(r'==\s*(True|False)', line_stripped):
            roasts.append((str(line_num), line_stripped, "Using '== True'? What's next, 'if (True == True) == True'?"))

        # ADVANCED RULE 3: Global variables
        if line_stripped.startswith("global "):
            roasts.append((str(line_num), line_stripped, "Global variables? What year is this, 1995?"))

        # ADVANCED RULE 4: Unsafe file handling (without 'with')
        if re.search(r'=\s*open\(', line_stripped) and "with " not in line:
            roasts.append((str(line_num), line_stripped, "Opening a file without 'with'? Don't forget to close it... oh wait, you probably forgot."))

        # ADVANCED RULE 5: Deep nesting (too many indentations)
        indentation_level = len(line) - len(line.lstrip())
        if indentation_level >= 16:  # 4 levels of indentation (4 spaces each)
            shortened = line_stripped[:35] + "..." if len(line_stripped) > 35 else line_stripped
            roasts.append((str(line_num), shortened, "Deeply nested code. Are we writing Python or drawing a pyramid?"))

    return roasts

def main():
    if len(sys.argv) < 2:
        console.print("[bold red]Error: You didn't provide a file for me to judge![/bold red]")
        console.print("Usage: [cyan]python3 roast.py <filename.py>[/cyan]")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        roasts = roast_code(lines)
        
        if not roasts:
            console.print(f"[bold green]Incredible! I couldn't find any major mistakes in '{filename}'.[/bold green]")
        else:
            console.print(f"[bold red]I analyzed '{filename}' and it's awful. Here is what I found:[/bold red]\n")
            
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Line", style="dim", width=5)
            table.add_column("Your Code", width=35)
            table.add_column("Verdict (Roast)", style="bold yellow")
            
            for r in roasts:
                table.add_row(r[0], r[1], r[2])
                
            console.print(table)
            
    except FileNotFoundError:
        console.print(f"[bold red]Error: File '{filename}' was not found.[/bold red]")

if __name__ == "__main__":
    main()
