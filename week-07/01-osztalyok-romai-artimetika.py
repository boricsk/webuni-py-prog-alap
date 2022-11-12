import re

class RomaiAritmatika:
    @staticmethod
    def osszead(romai1, romai2):
        arab1 = RomaiAritmatika.arabszammakonvertal(romai1)
        arab2 = RomaiAritmatika.arabszammakonvertal(romai2)
        eredmeny = arab1 + arab2
        eredmeny_romai = RomaiAritmatika.romai_konvertal(eredmeny)
        return eredmeny_romai
    
    @staticmethod
    def kivon(romai1, romai2):
        arab1 = RomaiAritmatika.arabszammakonvertal(romai1)
        arab2 = RomaiAritmatika.arabszammakonvertal(romai2)
        eredmeny = arab1 - arab2
        eredmeny_romai = RomaiAritmatika.romai_konvertal(eredmeny)
        return eredmeny_romai
    
    @staticmethod
    def szoroz(romai1, romai2):
        arab1 = RomaiAritmatika.arabszammakonvertal(romai1)
        arab2 = RomaiAritmatika.arabszammakonvertal(romai2)
        eredmeny = arab1 * arab2
        eredmeny_romai = RomaiAritmatika.romai_konvertal(eredmeny)
        return eredmeny_romai
    
    @staticmethod
    def oszt(romai1, romai2):
        arab1 = RomaiAritmatika.arabszammakonvertal(romai1)
        arab2 = RomaiAritmatika.arabszammakonvertal(romai2)
        eredmeny = arab1 // arab2
        eredmeny_romai = RomaiAritmatika.romai_konvertal(eredmeny)
        return eredmeny_romai
    
    @staticmethod
    def maradekoszt(romai1, romai2):
        arab1 = RomaiAritmatika.arabszammakonvertal(romai1)
        arab2 = RomaiAritmatika.arabszammakonvertal(romai2)
        eredmeny = arab1 % arab2
        eredmeny_romai = RomaiAritmatika.romai_konvertal(eredmeny)
        return eredmeny_romai
    
    @staticmethod
    def arabszammakonvertal(romai):
        if not bool(re.search(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', romai)):
            return(f'Hibás Római szám : {romai}')
        
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

    @staticmethod
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
            return f'Nem lehet római számmá konvertálni : {szam}'
        
        ezresek = (szam // 1000) * 'M'
        szazasok = szamjegyet_konvertal((szam // 100) % 10,'C', 'D', 'M' )
        tizesek = szamjegyet_konvertal((szam // 10) % 10, 'X', 'L', 'C')
        egyesek = szamjegyet_konvertal((szam % 10), 'I', 'V', 'X')
        return ezresek + szazasok + tizesek + egyesek

print(RomaiAritmatika.osszead('XIV', 'VIII'))
print(RomaiAritmatika.kivon('XIV', 'VIII'))
print(RomaiAritmatika.szoroz('XIV', 'VIII'))
print(RomaiAritmatika.oszt('XIV', 'VIII'))
print(RomaiAritmatika.maradekoszt('XIV', 'VIII'))