from lib_kviz import kerdest_feltesz

kerdesek_szama = 0
pontszam = 0

kerdesek = ['Mi Magyarország fővárosa? ',
            'Hogy hivjuk azt az állatot aminek ormánya van? ',
            'Hány fokon forr a viz? ',
            'Alma angolul? ',
            'Petőfi? ']

helyes_valaszok = ['Budapest',
                   'Elefánt',
                   '100',
                   'Apple',
                   'Sándor']


for i in range(len(kerdesek)):
    kerdesek_szama +=1
    if kerdest_feltesz(kerdesek[i], helyes_valaszok[i]):
        pontszam +=1
    
szazalek = str(100 * pontszam / kerdesek_szama)
print('Eredmeny: ' + szazalek + '%')