szöveg = """
Nem minden fajta szarka farka tarkabarka, csak a tarka farkú szarka fajta tarkabarka, 
mert ha minden fajta szarka farka tarkabarka volna, akkor minden szarka fajta tarkabarka 
farkú szarka fajta volna.
"""

substring = 'arka'
szoveg_lista = list(szöveg.split())

result = len([i for i in szoveg_lista if substring in i])

print(f'A szövegben az "arka" előfordulása {result} darab.')