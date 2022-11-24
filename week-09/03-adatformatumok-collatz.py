"""
Megvalósítás fgv formában.
Adott n-ig megnézzük melyik értékre a leghosszab a sorozat, ill. ,elyik a legmagasabb elért érték
Gyorsítótárazás (ha már valamit kiszámoltunk akkor elmentjük)
Rekurzív megvalósítás
Lemetjük fileba akkor nem előről fogja kezdeni.
"""
from datetime import datetime
import json
import os

collatzGyorsitotarFile = 'collatz.json'
if os.path.isfile(collatzGyorsitotarFile):
    with open(collatzGyorsitotarFile) as CollatzFile1:
        collatz_gyorsitotar = json.load(CollatzFile1)
else:
    collatz_gyorsitotar = {}


def collatz_lepeseket_szamol_rek(n,maximalis=0):
    if n in collatz_gyorsitotar:
        return collatz_gyorsitotar[n]
    if n == 1:
        eredmeny = {'hossz': 0,'max':1}
        return eredmeny
    else:
        if n % 2 == 0:
            kovetkezo_kollatz_eredmeny = collatz_lepeseket_szamol_rek(n // 2)
        else:
            kovetkezo_szam = 3*n + 1
            kovetkezo_kollatz_eredmeny =collatz_lepeseket_szamol_rek(kovetkezo_szam,max(maximalis, kovetkezo_szam))
    eredmeny = {'hossz':kovetkezo_kollatz_eredmeny['hossz'] + 1 , 'max':max(maximalis, kovetkezo_kollatz_eredmeny['max'])}
    collatz_gyorsitotar[n] = eredmeny
    return eredmeny

def leghosszab_legmagasabb_collatz_ertek(n):
    leghosszabb = {'hossz': 1,'ertek': 0,'max': 1}
    legmagasabb = {'hossz': 1,'ertek': 0,'max': 1}
    for i in range(1,n):
        aktualis_eredmeny = collatz_lepeseket_szamol_rek(i)
        if aktualis_eredmeny['hossz'] > leghosszabb['hossz']:
            leghosszabb = {'ertek': i, 'hossz': aktualis_eredmeny['hossz'], 'max': aktualis_eredmeny['max']}
        if aktualis_eredmeny['max'] > legmagasabb['max']:
            legmagasabb = {'ertek': i, 'hossz': aktualis_eredmeny['hossz'], 'max': aktualis_eredmeny['max']}
    return leghosszabb, legmagasabb
    
# for i in range(1,21):
#     print(i, collatz_lepeseket_szamol(i))

start = datetime.now()
print(leghosszab_legmagasabb_collatz_ertek(20))
print(datetime.now()-start)

with open('collatz.json','w') as collatzFile:
    json.dump(collatz_gyorsitotar, collatzFile, indent=4) # lehet formázni
