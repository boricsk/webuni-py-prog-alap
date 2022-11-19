import re

class RomaiKivetel(Exception):
    pass


def arabszammakonvertal(romai):
    if type(romai) is not str or not bool(re.search(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', romai)):
        raise RomaiKivetel(f'Hibás Római szám : {romai}')
    
    romai_szamertekek ={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #végig kell menni a szamjegyeken az utolso elottiig. meg kell nézni, h a kovetkezo szam nagyobb-e vagy kisseb-e mint az aktualis
    #ha nagyobb hozza kell adni, ha kissebb akkor ki kell vonni.
    #példa: 
    #M a C nél nagyobb, tehát M-et hozzáadunk (1000)
    #C kisseb az M nél, ezért 100-at ki kell vonni (900)
    #M nagyobb mint az L ezért + 1000 (1900)
    #L nagyobb mint X ezér +50 (1950)
    #X egyenlő X ekkor is hozzáadás van 3x 10 et (1980)
    #I kissebb mint V kivon 1-et (1979)
    #A V-t (utolsó mindenkép hozzá kell adni) (1984)
    
    erdmeny = 0
    for i in range(len(romai)-1):
        aktualis = romai_szamertekek[romai[i]] # a romai szamertekekbol mutatja az arab megfelelőt
        kovetkezo = romai_szamertekek[romai[i+1]]
        if aktualis<kovetkezo:
            erdmeny -= aktualis
        else:
            erdmeny += aktualis
    erdmeny += romai_szamertekek[romai[-1]] #utolső érték hozzáadáas
    return erdmeny


def romai_konvertal(szam):
    
    def szamjegyet_konvertal(szamjegy, egyesek, otosok, tizesek):
        if szamjegy <= 3:
            return szamjegy * egyesek
        elif szamjegy == 4:
            return egyesek + otosok
        elif szamjegy <= 8:
            return otosok + (szamjegy - 5) * egyesek
        else:
            return egyesek + tizesek
    
    if type(szam) is not int or szam < 1 or szam > 3999:
        raise RomaiKivetel(f'Nem lehet római számmá konvertálni : {szam}')
    
    ezresek = (szam // 1000) * 'M'
    szazasok = szamjegyet_konvertal((szam // 100) % 10,'C', 'D', 'M' )
    tizesek = szamjegyet_konvertal((szam // 10) % 10, 'X', 'L', 'C')
    egyesek = szamjegyet_konvertal((szam % 10), 'I', 'V', 'X')
    return ezresek + szazasok + tizesek + egyesek

def vegrehajt(muvelet):
    romai1, muveleti_jel, romai2 = muvelet.split() # a bemenet felbontása
    jel_muvelet = {
        '+': lambda r1, r2 : romai_konvertal(arabszammakonvertal(r1) + arabszammakonvertal(r2)),
        '-': lambda r1, r2 : romai_konvertal(arabszammakonvertal(r1) - arabszammakonvertal(r2)),
        '*': lambda r1, r2 : romai_konvertal(arabszammakonvertal(r1) * arabszammakonvertal(r2)),
        '/': lambda r1, r2 : romai_konvertal(arabszammakonvertal(r1) // arabszammakonvertal(r2)),
        '%': lambda r1, r2 : romai_konvertal(arabszammakonvertal(r1) % arabszammakonvertal(r2)),
    }
    return jel_muvelet[muveleti_jel](romai1,romai2)

# print(vegrehajt('XIV + VIII'))
# print(vegrehajt('XIV - VIII'))
# print(vegrehajt('XIV * VIII'))
# print(vegrehajt('XIV / VIII'))
# print(vegrehajt('XIV % VIII'))

for arab in [1984, 5000, 1984.5, 'kutya', None]:
    
    try:
        print(romai_konvertal(arab))
    except RomaiKivetel as e:
        print(f'Hiba : {e}')

for romai in ['MCMLXXXIV', 'MIM', 'macska', 123, None]:
    try:
        print(arabszammakonvertal(romai))
    except RomaiKivetel as e:
        print(f'Hiba : {e}')