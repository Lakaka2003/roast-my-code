import argparse
from rich.console import Console
from rich.table import Table
from rules import roast_code

console = Console()

def main():
    # Setup argparse for professional CLI arguments
    parser = argparse.ArgumentParser(
        description="🌶️  Roast My Code - A sarcastic Python static analysis tool."
    )
    
    parser.add_argument("filename", help="The Python file you want me to judge")
    parser.add_argument("--strict", action="store_true", help="Only show major architectural and security flaws")
    
    args = parser.parse_args()
    filename = args.filename

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        # Pass the flag to our validation logic
        roasts = roast_code(lines, strict=args.strict)
        
        if not roasts:
            console.print(f"[bold green]Incredible! I couldn't find any mistakes in '{filename}'.[/bold green]")
        else:
            mode_text = "[bold red](STRICT MODE)[/bold red] " if args.strict else ""
            console.print(f"{mode_text}[bold red]I analyzed '{filename}' and it's awful. Here is what I found:[/bold red]\n")
            
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
