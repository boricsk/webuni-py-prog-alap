
import random

probak_szama = 100000
sikeres_kilepesek_szama = 0
for i in range(probak_szama):
    
    for j in range(3):
        if random.randint(1, 6) == 6:
            sikeres_kilepesek_szama += 1
            break
print(sikeres_kilepesek_szama / probak_szama)

#bő 40% esélye van egy játékosnak arra, hogy sikeresen kilépjen, ha 3-at dobhat

összes = 0
kilepesek = 0
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            összes += 1
            if i == 6 or j == 6 or k == 6: # vagy if 6 in [i, j, k]
                kilepesek +=1
print(kilepesek / összes)

# ez a pontos értéke.