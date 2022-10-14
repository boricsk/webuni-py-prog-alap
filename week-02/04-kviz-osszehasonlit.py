kerdesek_szama = 0
pontszam = 0

valasz = input('Mi Magyarország fővárosa? ')
helyes_valasz = 'Budapest'
kerdesek_szama +=1
if valasz == helyes_valasz:
    print('A valasz helyes')
    pontszam +=1
else:
    print('A válasz helytelen')

valasz = input('Hogy hivjuk azt az állatot aminek ormánya van? ')
helyes_valasz = 'Elefánt'
kerdesek_szama +=1
if valasz == helyes_valasz:
    print('A valasz helyes')
    pontszam +=1
else:
    print('A válasz helytelen')

valasz = input('Hány fokon forr a viz? ')
helyes_valasz = '100'
kerdesek_szama +=1
if valasz == helyes_valasz:
    print('A valasz helyes')
    pontszam +=1
else:
    print('A válasz helytelen')

valasz = input('Alma angolul? ')
helyes_valasz = 'Apple'
kerdesek_szama +=1
if valasz == helyes_valasz:
    print('A valasz helyes')
    pontszam +=1
else:
    print('A válasz helytelen')

valasz = input('Petőfi? ')
helyes_valasz = 'Sándor'
kerdesek_szama +=1
if valasz == helyes_valasz:
    print('A valasz helyes')
    pontszam +=1
else:
    print('A válasz helytelen')

szazalek = str(100 * pontszam / kerdesek_szama)
print('Eredmeny: ' + szazalek + '%')