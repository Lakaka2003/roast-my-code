import sys
from rich.console import Console
from rich.table import Table

# Importam logica de validare din noul nostru fisier rules.py
from rules import roast_code

console = Console()

def main():
    if len(sys.argv) < 2:
        console.print("[bold red]Error: You didn't provide a file for me to judge![/bold red]")
        console.print("Usage: [cyan]python3 roast.py <filename.py>[/cyan]")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        # Folosim functia importata pentru a obtine insultele
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
