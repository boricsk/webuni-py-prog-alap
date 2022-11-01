#Mekkor a valószínűsége, hogy két kocka használatával az összeg 7 lesz.

import random

probak_szama = 1000000
rablasok_szama = 0
for i in range(probak_szama):
    kocka1 = random.randint(1,6)
    kocka2 = random.randint(1,6)
    if kocka1 + kocka2 == 7:
        rablasok_szama += 1
        
print(rablasok_szama / probak_szama)