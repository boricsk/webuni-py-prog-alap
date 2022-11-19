import re
from enum import Enum, auto
#A kerdestipus szamkent van megadva, ezt módositsuk szovegre a jobb olvashatosag miatt. 

class KerdesTipus(Enum):
    SZOVEGES = auto()
    EGESZ_SZAM = auto()


kerdesek_szama, pontszam = 0, 0


kerdesek_es_helyes_valaszok = [
            (KerdesTipus.SZOVEGES,'Mi Ausztria fővárosa? ','Bécs', r'^(Bécs|Wien)$'),
            (KerdesTipus.SZOVEGES,'Melyik rajzfilmben szerepel Gombóc Artúr? ','Pom Pom meséi', r'^Pom[ -]?[Pp]om( [Mm]eséi)?$'),
            (KerdesTipus.EGESZ_SZAM,'Hány fokon forr a viz? ', 100, r''),
            (KerdesTipus.SZOVEGES,'Barack angolul? ', 'peach', r'^(peach|apricot)$'),
            (KerdesTipus.SZOVEGES,'Mi a Verne vezetéknevű Francia iró keresztneve? ', 'Jules', r'^(Jules|Gyula)$'),
            ]



def kerdest_feltesz(kerdes, helyes_valasz, tipus, minta):
    valasz = input(kerdes)
    match tipus:
        case KerdesTipus.SZOVEGES:
            if bool(re.search(minta, valasz)):
                return True, 'A valasz helyes'
            else:
                return False, 'A válasz helytelen'
            
        case KerdesTipus.EGESZ_SZAM:
            valasz_szam = int(valasz)
            if valasz_szam == helyes_valasz:
                return True, 'A valasz helyes'
            else:
                return False, f'A válasz helytelen. Az eltérés : {valasz_szam - helyes_valasz}'
        
   
# for i in range(len(kerdesek_es_helyes_valaszok)):
#     kerdesek_szama +=1
#     if kerdest_feltesz(kerdesek_es_helyes_valaszok[i][0], kerdesek_es_helyes_valaszok[i][1]):
#         pontszam +=1

#Egy elegánsabb megoldás

for tipus, kerdes, valasz, minta in kerdesek_es_helyes_valaszok:
    kerdesek_szama +=1
    helyes_e, szoveges_valasz = kerdest_feltesz(kerdes, valasz, tipus, minta)
    print(szoveges_valasz)
    if helyes_e:
        pontszam +=1
    

print(f'Eredmeny: {100 * pontszam / kerdesek_szama:.3g} %')