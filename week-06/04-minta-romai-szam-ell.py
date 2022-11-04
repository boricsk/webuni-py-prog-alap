import re


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
            


print(arabszammakonvertal('MCMLXXXIV'))
print(arabszammakonvertal('I'))
print(arabszammakonvertal('XXV'))
print(arabszammakonvertal('MIM'))
print(arabszammakonvertal('CXI'))
print(arabszammakonvertal('XI'))
print(arabszammakonvertal('IX'))
print(arabszammakonvertal('IIII'))
print(arabszammakonvertal('KAKA'))
