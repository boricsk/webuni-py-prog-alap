"""
Feladat: 
Adott egy számlista és egy szám. A listában van-e olyan számpár, amelynek az összege a megadott szám.
Ha van adjuk vissza. Ha több is van akkor azt adjuk vissza amelynél a második elem indexe a kisebb.
Példa :
[6,3,1,4,2] a megadott szám : 5. Két megoldása van 3 + 2 és 1 + 4. Az elvárt az 1 + 4 mert a 4 indexe kisebb mint a 2 indexe
A lista mérete 10 millió elem kell hogy legyen és a futási idő nem lehet több mint 10 sec.
"""
from datetime import datetime

def osszeget_keres(lista, osszeg):
    for i in range(1, len(lista)):
        for j in range(i):
            if lista[i] + lista[j] == osszeg:
                return lista[j], lista[i]
    return None

def osszeget_keres2(lista, osszeg):
    halmaz = set()
    for elem in lista:
        if osszeg - elem in halmaz:
            return osszeg - elem, elem
        halmaz.add(elem)

print(osszeget_keres2([6,3,1,4,2],5))

start = datetime.now()
print(osszeget_keres2([2 * i for i in range(10_000_000)],5))
print(datetime.now()-start)