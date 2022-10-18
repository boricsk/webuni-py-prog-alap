kerdesek_szama = 0
pontszam = 0
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
            print('A valasz helyes')
            return True
        else:
            print('A válasz helytelen')
            return False
    elif tipus == 2:
        valasz_szam = int(valasz)
        if valasz_szam == helyes_valasz:
            print('A valasz helyes')
            return True
        else:
            print('A válasz helytelen. Az eltérés : ', str(valasz_szam - helyes_valasz))
            return False

# for i in range(len(kerdesek_es_helyes_valaszok)):
#     kerdesek_szama +=1
#     if kerdest_feltesz(kerdesek_es_helyes_valaszok[i][0], kerdesek_es_helyes_valaszok[i][1]):
#         pontszam +=1

#Egy elegánsabb megoldás

for tipus, kerdes, valasz in kerdesek_es_helyes_valaszok:
    kerdesek_szama +=1
    if kerdest_feltesz(kerdes, valasz, tipus):
        pontszam +=1
    
szazalek = str(100 * pontszam / kerdesek_szama)
print('Eredmeny: ' + szazalek + '%')