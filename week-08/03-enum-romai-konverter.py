from enum import Enum, auto

class RomaiSzam(Enum):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
    
def romai_konvertal(szam):
        
        def szamjegyet_konvertal(szamjegy, egyesek, otosok, tizesek):
            match szamjegy:
                case n if 0 <= n <= 3: return szamjegy * egyesek
                case 4: return egyesek + otosok
                case n if 5 <= n <= 8: return otosok + (szamjegy - 5) * egyesek
                case 9: return egyesek + tizesek
                   
        if type(szam) is not int or szam < 1 or szam > 3999:
            return f'Nem lehet római számmá konvertálni : {szam}'
        
        ezresek = (szam // 1000) * RomaiSzam.M.name # a nevére van szükség
        szazasok = szamjegyet_konvertal((szam // 100) % 10, RomaiSzam.C.name, RomaiSzam.D.name, RomaiSzam.M.name )
        tizesek = szamjegyet_konvertal((szam // 10) % 10, RomaiSzam.X.name, RomaiSzam.L.name, RomaiSzam.C.name)
        egyesek = szamjegyet_konvertal((szam % 10), RomaiSzam.I.name, RomaiSzam.V.name, RomaiSzam.X.name)
        return ezresek + szazasok + tizesek + egyesek
    
print(romai_konvertal(1984))