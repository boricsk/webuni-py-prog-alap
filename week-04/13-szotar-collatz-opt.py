"""
Megvalósítás fgv formában.
Adott n-ig megnézzük melyik értékre a leghosszab a sorozat, ill. ,elyik a legmagasabb elért érték
Gyorsítótárazás (ha már valamit kiszámoltunk akkor elmentjük)
Rekurzív megvalósítás

"""
from datetime import datetime

collatz_gyorsitotar = {}

def collatz_lepeseket_szamol(n):
    max_ertek = n
    lepesek_szama = 0
    if n in collatz_gyorsitotar:
        return collatz_gyorsitotar[n] #igazából lassabb lett :D mert csak a végeredmény van elmentve.
    while n != 1:
        lepesek_szama += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = n *3 + 1
            if n > max_ertek:
                max_ertek = n
    eredmeny = (lepesek_szama, max_ertek)
    collatz_gyorsitotar[n] = eredmeny
    return eredmeny

def collatz_lepeseket_szamol_rek(n,maximalis=0):
    if n in collatz_gyorsitotar:
        return collatz_gyorsitotar[n]
    if n == 1:
        eredmeny = (0,1)
        return eredmeny
    else:
        if n % 2 == 0:
            kovetkezo_kollatz_eredmeny = collatz_lepeseket_szamol_rek(n // 2)
        else:
            kovetkezo_szam = 3*n + 1
            kovetkezo_kollatz_eredmeny =collatz_lepeseket_szamol_rek(kovetkezo_szam,max(maximalis, kovetkezo_szam))
    eredmeny = kovetkezo_kollatz_eredmeny[0] + 1 , max(maximalis, kovetkezo_kollatz_eredmeny[1])
    collatz_gyorsitotar[n] = eredmeny
    return eredmeny

def leghosszab_legmagasabb_collatz_ertek(n):
    leghosszabb = (1,0,1)
    legmagasabb = (1,0,1)
    for i in range(1,n):
        aktualis_eredmeny = collatz_lepeseket_szamol_rek(i)
        if aktualis_eredmeny[0] > leghosszabb[1]:
            leghosszabb = (i, aktualis_eredmeny[0], aktualis_eredmeny[1])
        if aktualis_eredmeny[1] > legmagasabb[2]:
            legmagasabb = (i, aktualis_eredmeny[0], aktualis_eredmeny[1])
    return leghosszabb, legmagasabb
    
# for i in range(1,21):
#     print(i, collatz_lepeseket_szamol(i))

start = datetime.now()
print(leghosszab_legmagasabb_collatz_ertek(100000))
print(datetime.now()-start)