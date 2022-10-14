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
    valasz = input(kerdesek[i])
    kerdesek_szama +=1
    helyes_valasz = helyes_valaszok[i]
    if valasz == helyes_valasz:
        print('A valasz helyes')
        pontszam +=1
    else:
        print('A válasz helytelen')
    


szazalek = str(100 * pontszam / kerdesek_szama)
print('Eredmeny: ' + szazalek + '%')