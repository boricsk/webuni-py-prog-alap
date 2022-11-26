# https://hu.wikipedia.org/wiki/Goldbach-sejt%C3%A9s

from datetime import datetime

primek = set()
nem_primek = set()

def prim_e(n):
    i = 2
    if n in primek:
        return True
    if n in nem_primek:
        return False
    
    while i*i <= n:
        if n % i ==0:
            nem_primek.add(n)
            return False
        i +=1
    primek.add(n)
    return True

def goldbach_par(n):
    for i in range(2, n // 2 + 1):
        if prim_e(i) and prim_e(n-i):
            return i, n-i
    return None

def goldbach_max(n):
    megoldas = (0,0,0)
    for i in range(4, n, 2):
        akt_megoldas = goldbach_par(i)
        if akt_megoldas[0] > megoldas[1]:
            megoldas = i, akt_megoldas[0], akt_megoldas[1]
    return megoldas

# for i in range(20):
#     if prim_e(i):
#         print(i)

# for i in range(4, 20, 2):
#     print(i, goldbach_par(i))

start = datetime.now()
print(goldbach_max(100))
print(datetime.now()-start)