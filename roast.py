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
        
        # Sărim peste liniile goale
        if not line_stripped:
            continue

        # Regula 1: Variabile dintr-o singură literă
        if re.match(r'^[a-zA-Z]\s*=', line_stripped):
            roasts.append((str(num_linie), line_stripped, "Variabilă dintr-o literă? Ești programator sau joci Spânzurătoarea?"))
        
        # Regula 2: except orbește
        if line_stripped == "except:":
            roasts.append((str(num_linie), line_stripped, "Ai ascuns eroarea sub preș. Curajos, dar complet iresponsabil."))
            
        # Regula 3: pass
        if line_stripped == "pass":
            roasts.append((str(num_linie), line_stripped, "'pass'? Așa o să treacă și cariera ta pe lângă tine."))
            
        # Regula 4: TODO în comentarii
        if re.search(r'#.*TODO', line_stripped, re.IGNORECASE):
            roasts.append((str(num_linie), line_stripped, "Acel 'TODO' e acolo ca să te simți tu bine. Știm amândoi că nu-l vei face."))
            
        # Regula 5: Debugging din Epoca de Piatră
        if re.search(r'print\(\s*["\'](test|aici|123|salut|a)["\']\s*\)', line_stripped, re.IGNORECASE):
            roasts.append((str(num_linie), line_stripped, "Debugging cu print('test')? Există unelte pentru asta, omule al peșterilor."))
            
        # Regula 6: Linii interminabile
        if len(line) > 100:
            scurtat = line_stripped[:40] + "..."
            roasts.append((str(num_linie), scurtat, "Linia asta e atât de lungă încât trebuie să iau un Uber până la capătul ei."))
            
        # Regula 7: Bucle infinite
        if line_stripped == "while True:":
            roasts.append((str(num_linie), line_stripped, "Buclă infinită. La fel ca timpul pe care îl pierzi rescriind codul ăsta."))

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
            
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Linia", style="dim", width=6)
            table.add_column("Codul Tău", width=40)
            table.add_column("Verdictul (Roast)", style="bold yellow")
            
            for r in roasts:
                table.add_row(r[0], r[1], r[2])
                
            console.print(table)
            
    except FileNotFoundError:
        console.print(f"[bold red]Eroare: Fișierul '{nume_fisier}' nu a fost găsit.[/bold red]")

if __name__ == "__main__":
    main()
