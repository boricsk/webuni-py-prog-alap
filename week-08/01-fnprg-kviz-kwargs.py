import re

kerdesek_szama, pontszam = 0, 0
#Listák összevonása és a kérdéstípus bevezetése
#1 tipus szöveg, 2 tipus pedig a szám lesz

kerdesek_es_helyes_valaszok = [
            (1,'Mi Ausztria fővárosa? ','Bécs', r'^(Bécs|Wien)$'),
            (1,'Melyik rajzfilmben szerepel Gombóc Artúr? ','Pom Pom meséi', r'^Pom[ -]?[Pp]om( [Mm]eséi)?$'),
            (2,'Hány fokon forr a viz? ', 100, r''),
            (1,'Barack angolul? ', 'peach', r'^(peach|apricot)$'),
            (1,'Mi a Verne vezetéknevű Francia iró keresztneve? ', 'Jules', r'^(Jules|Gyula)$'),
            ]



def kerdest_feltesz(tipus, kerdes, **kwargs):
    valasz = input(kerdes)
    if tipus == 1:
        if bool(re.search(kwargs['minta'], valasz)):
            return True, 'A valasz helyes'
        else:
            return False, 'A válasz helytelen'
    elif tipus == 2:
        valasz_szam = int(valasz)
        helyes_valasz = kwargs['helyes_valasz']
        if valasz_szam == helyes_valasz:
            return True, 'A valasz helyes'
        else:
            return False, f'A válasz helytelen. Az eltérés : {valasz_szam - helyes_valasz}' 
        

for tipus, kerdes, valasz, minta in kerdesek_es_helyes_valaszok:
    kerdesek_szama +=1
    if tipus == 1:                                                 #kwargs név   hivo adat
        helyes_e, szoveges_valasz = kerdest_feltesz(tipus, kerdes, helyes_valasz=valasz, minta=minta) #kwargs hivas
    elif tipus == 2:
        helyes_e, szoveges_valasz = kerdest_feltesz(tipus, kerdes, helyes_valasz=valasz)
        
    print(szoveges_valasz)
    if helyes_e:
        pontszam +=1
    

print(f'Eredmeny: {100 * pontszam / kerdesek_szama:.3g} %')