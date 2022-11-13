import re
from abc import ABC, abstractmethod
#kérdések és válaszok lista iterátorrá alakítása

class Kerdes(ABC):
    def __init__(self, kerdes, helyes_valasz) -> None:
        self.kerdes = kerdes
        self.helyes_valasz = helyes_valasz
    
    def kerdest_feltesz(self):
        valasz = input(self.kerdes + ' ')
        helyes_e, plussz_info = self._valaszt_kiertekel(valasz)
        if helyes_e:
            print('A valasz helyes')
        else:
            print(f'A válasz helytelen, a helyes válasz {self.helyes_valasz} lett volna. {plussz_info}')
        return helyes_e
    
    @abstractmethod
    def _valaszt_kiertekel(self, valasz):
        pass


class SzovegesKerdes(Kerdes):
    def __init__(self, kerdes, helyes_valasz, minta) -> None:
        super().__init__(kerdes, helyes_valasz)
        self.minta = minta
    
    def _valaszt_kiertekel(self, valasz):
        return bool(re.search(self.minta, valasz)), ''
        

class SzamKerdes(Kerdes):
    def _valaszt_kiertekel(self, valasz):
        valasz_szam = int(valasz)
        if valasz_szam == self.helyes_valasz:
            return True, ''
        else:
            return False, f'Az eltérés : {valasz_szam - self.helyes_valasz}' 

class Kerdesek:
    def __iter__(self):
        self.kerdesek_es_helyes_valaszok = [
        SzovegesKerdes('Mi Ausztria fővárosa? ', 'Bécs', r'^(Bécs|Wien)$'),
        SzovegesKerdes('Melyik rajzfilmben szerepel Gombóc Artúr? ','Pom Pom meséi', r'^Pom[ -]?[Pp]om( [Mm]eséi)?$'),
        SzamKerdes('Hány fokon forr a viz? ', 100),
        SzovegesKerdes('Barack angolul? ', 'peach', r'^(peach|apricot)$'),
        SzovegesKerdes('Mi a Verne vezetéknevű Francia iró keresztneve? ', 'Jules', r'^(Jules|Gyula)$'),
        ]
        self.i = 0 #kerdes sorszáma
        return self
    
    def __next__(self):
        if self.i < len(self.kerdesek_es_helyes_valaszok):
            kerdes = self.kerdesek_es_helyes_valaszok[self.i]
            self.i += 1
            return kerdes
        else:
            raise StopIteration
        

kerdesek_szama, pontszam = 0, 0

for kerdes in Kerdesek():
    kerdesek_szama +=1
    if kerdes.kerdest_feltesz():
        pontszam +=1



print(f'Eredmeny: {100 * pontszam / kerdesek_szama:.3g} %')