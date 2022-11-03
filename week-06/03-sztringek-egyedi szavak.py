def egyedi_szavakat_kivalaszt(szoveg):
    eredmeny = set()
    for szo in szoveg.lower().replace(',', '').replace('.', '').split():
        if szo not in eredmeny:
            eredmeny.add(szo)
    return sorted(eredmeny)

def egyedi_szavakat_kivalaszt2(szoveg):
    return sorted({szo for szo in szoveg.lower().replace(',', '').replace('.', '').split()})



szoveg = """
Nem minden fajta szarka farka tarkabarka, csak a tarka farkú szarka fajta tarkabarka, 
mert ha minden fajta szarka farka tarkabarka volna, akkor minden szarka fajta tarkabarka 
farkú szarka fajta volna.
"""

print(egyedi_szavakat_kivalaszt2(szoveg))