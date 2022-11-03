kerdesek_szama, pontszam = 0, 0
#Listák összevonása és a kérdéstípus bevezetése
#1 tipus szöveg, 2 tipus pedig a szám lesz

kerdesek_es_helyes_valaszok = [
            (1,'Mi Magyarország fővárosa? ','Budapest'),
            (1,'Hogy hivjuk azt az állatot aminek ormánya van? ','Elefánt'),
            (2,'Hány fokon forr a viz? ', 100),
            (1,'Alma angolul? ', 'Apple'),
            (1,'Petőfi? ', 'Sándor'),
            ]



def kerdest_feltesz(kerdes, helyes_valasz, tipus):
    valasz = input(kerdes)
    if tipus == 1:
        if valasz == helyes_valasz:
            return True, 'A valasz helyes'
        else:
            return False, 'A válasz helytelen'
    elif tipus == 2:
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

for tipus, kerdes, valasz in kerdesek_es_helyes_valaszok:
    kerdesek_szama +=1
    helyes_e, szoveges_valasz = kerdest_feltesz(kerdes, valasz, tipus)
    print(szoveges_valasz)
    if helyes_e:
        pontszam +=1
    

print(f'Eredmeny: {100 * pontszam / kerdesek_szama:.3g} %')