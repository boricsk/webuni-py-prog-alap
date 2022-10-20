#Adott egy számokból álló halmaz és meg kell határozni, hogy mindegyik elem különbözik-e
from datetime import datetime
def mind_kulonbozo1(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j]:
                return False
    return True

def mind_kulonbozo2(lista):
    rendezett = sorted(lista)
    for i in range(len(rendezett)-1):
        if rendezett[i] == rendezett[i+1]:
            return False
    return True

def mind_kulonbozo3(lista): # az az alapelv, hogy a halmazzá alakítás után a duplikációk kikerűltek. Ha a két adathalmaz hossza egyenlő nincs két egyforma eleme
    halmaz = set(lista)
    if len(lista) == len(halmaz):
        return True
    else:
        return False

def mind_kulonbozo4(lista): # az az alapelv, hogy a halmazzá alakítás után a duplikációk kikerűltek. Ha a két adathalmaz hossza egyenlő nincs két egyforma eleme
    return len(lista) == len(set(lista))
    

print(mind_kulonbozo1([1,2,3,4,5]))
print(mind_kulonbozo1([1,2,3,4,1]))

lista = [i for i in range(10000000)]
start = datetime.now()
print(mind_kulonbozo4(lista))
print('A műveleti idő :', datetime.now() - start)