
def szoszamlalo(szoveg):
    eredmeny = {}
    for szo in szoveg.lower().replace(',','').replace('.','').split():
        if szo in eredmeny:
            eredmeny[szo] += 1
        else:
            eredmeny[szo] =1
        
    return eredmeny

szöveg = """
Nem minden fajta szarka farka tarkabarka, csak a tarka farkú szarka fajta tarkabarka, 
mert ha minden fajta szarka farka tarkabarka volna, akkor minden szarka fajta tarkabarka 
farkú szarka fajta volna.
"""

eredmeny = szoszamlalo(szöveg)
eredmeny_rendezett = sorted(eredmeny.items(), key=lambda x:x[1],reverse=True)
print(eredmeny_rendezett)