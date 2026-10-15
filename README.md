# Roast My Code

Acesta e primul meu proiect independent. Practic, este un linter de Python, dar in loc sa iti dea erorile tehnice plictisitoare, doar face misto de tine cand scrii cod aiurea (cum ar fi sa pui variabile de o litera, sa folosesti pass sau sa faci debugging cu print).

L-am facut ca sa invat cum functioneaza modulele de regex si cum sa formatez lucruri in terminal cu libraria rich.

## Cum il instalezi

Daca vrei sa il incerci, pasii sunt destul de simpli:

1. Clonezi repo-ul si intri in folder:
git clone https://github.com/NUMELE-TAU-DE-UTILIZATOR/roast-my-code.git
cd roast-my-code

2. Faci un mediu virtual si instalezi dependintele:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Cum se foloseste

Ii dai pur si simplu un fisier python ca argument in terminal si astepti sa iti judece codul:
python3 roast.py fisierul_tau.py
