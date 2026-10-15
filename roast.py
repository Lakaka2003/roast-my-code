import sys
import re
from rich.console import Console
from rich.table import Table

console = Console()

def roast_code(lines):
    roasts = []
    for i, line in enumerate(lines):
        num_linie = i + 1
        line_stripped = line.strip()

        # Regula 1: Variabile dintr-o singură literă (ex: x = 5)
        if re.match(r'^[a-zA-Z]\s*=', line_stripped):
            roasts.append((str(num_linie), line_stripped, "Variabilă dintr-o literă? Ești programator sau joci Spânzurătoarea?"))
        
        # Regula 2: prinderea tuturor erorilor orbește
        if line_stripped == "except:":
            roasts.append((str(num_linie), line_stripped, "Ai ascuns eroarea sub preș. Curajos, dar complet iresponsabil."))
            
    return roasts

def main():
    if len(sys.argv) < 2:
        console.print("[bold red]Eroare: Nu mi-ai dat niciun fișier pe care să-l judec![/bold red]")
        return

    nume_fisier = sys.argv[1]

    try:
        with open(nume_fisier, 'r', encoding='utf-8') as f:
            linii = f.readlines()
            
        roasts = roast_code(linii)
        
        if not roasts:
            console.print(f"[bold green]Incredibil! Nu am găsit nicio greșeală majoră în '{nume_fisier}'.[/bold green]")
        else:
            console.print(f"[bold red]Am analizat '{nume_fisier}' și e groaznic. Uite ce am găsit:[/bold red]\n")
            
            # Creăm un tabel frumos formatat
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Linia", style="dim", width=6)
            table.add_column("Codul Tău", width=30)
            table.add_column("Verdictul (Roast)", style="bold yellow")
            
            for r in roasts:
                table.add_row(r[0], r[1], r[2])
                
            console.print(table)
            
    except FileNotFoundError:
        console.print(f"[bold red]Eroare: Fișierul '{nume_fisier}' nu a fost găsit.[/bold red]")

if __name__ == "__main__":
    main()
