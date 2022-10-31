"""
Gererálni fogja a vérdéseket és a válaszokat. A kerdesek es valaszok szotarban lesznek. Kivaleóaszt egy kerdest és a hozza tartozo jo valaszt, valamint még 3 rossz valaszt
ezeket keveri. Ezt fogja kiirna a, b, c, d valasz lehetosegek formajaban, es ebbol kell valasztani.
"""

import random

országok_fővárosai = {
    'Albánia': 'Tirana',
    'Andorra': 'Andorra la Vella',
    'Ausztria': 'Bécs',
    'Belgium': 'Brüsszel',
    'Bosznia-Hercegovina': 'Szarajevó',
    'Bulgária': 'Szófia',
    'Csehország': 'Prága',
    'Dánia': 'Koppenhága',
    'Egyesült Királyság': 'London',
    'Észtország': 'Tallinn',
    'Fehéroroszország': 'Minszk',
    'Finnország': 'Helsinki',
    'Franciaország': 'Párizs',
    'Görögország': 'Athén',
    'Hollandia': 'Amszterdam',
    'Horvátország': 'Zágráb',
    'Írország': 'Dublin',
    'Izland': 'Reykjavík',
    'Lengyelország': 'Varsó',
    'Lettország': 'Riga',
    'Liechtenstein': 'Vaduz',
    'Litvánia': 'Vilnius',
    'Luxemburg': 'Luxembourg',
    'Észak-Macedónia': 'Szkopje',
    'Magyarország': 'Budapest',
    'Málta': 'Valletta',
    'Moldova': 'Chișinău',
    'Monaco': 'Monaco',
    'Montenegró': 'Podgorica',
    'Németország': 'Berlin',
    'Norvégia': 'Oslo',
    'Portugália': 'Lisszabon',
    'Románia': 'Bukarest',
    'Olaszország': 'Róma',
    'Oroszország': 'Moszkva',
    'San Marino': 'San Marino',
    'Svédország': 'Stockholm',
    'Svájc': 'Bern',
    'Szerbia': 'Belgrád',
    'Szlovákia': 'Pozsony',
    'Szlovénia': 'Ljubljana',
    'Spanyolország': 'Madrid',
    'Törökország': 'Ankara',
    'Ukrajna': 'Kijev',
    'Vatikán': 'Vatikán',
}

kerdesek_szama = 5
válaszlehetoseg = 4
pontszam = 0

for orszag in random.sample(list(országok_fővárosai.keys()),kerdesek_szama): #listává kell alakitani, mert a keys egy halmaz.
    helyes_valasz = országok_fővárosai[orszag]
    helytelen_valaszok = list(országok_fővárosai.values())
    helytelen_valaszok.remove(helyes_valasz)
    kivalasztott_fovarosok = random.sample(helytelen_valaszok,3)
    kivalasztott_fovarosok.append(helyes_valasz)
    random.shuffle(kivalasztott_fovarosok)
    kivalasztott_fovarosok_szotar = {chr(ord('A') + i): kivalasztott_fovarosok[i] for i in range(válaszlehetoseg)}
    print('Mi '+orszag+' fővárosa?')
    for betu, fovaros in kivalasztott_fovarosok_szotar.items():
        print('    '+betu+'. '+fovaros)
    valasz = input('> ')
    valasz_fovaros = kivalasztott_fovarosok_szotar[valasz.upper()]
    if valasz_fovaros == helyes_valasz:
        print('A válasz helyas.')
        pontszam += 1
    else:
        print('A válasz helytelen. A helyes válasz '+ helyes_valasz + ' lett volna.')

print('Eredmény :'+str(100*pontszam/kerdesek_szama)+' %.')
