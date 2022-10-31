
def boborekrendezes_orig(szamok):
    tortent_valtozas = True
    while tortent_valtozas:
        tortent_valtozas = False
        for i in range(len(szamok)-1):
            if szamok[i] > szamok[i+1]:
                temp = szamok[i]
                szamok[i] = szamok[i+1]
                szamok[i+1] = temp
                tortent_valtozas = True
                
def boborekrendezes(szamok):
    tortent_valtozas = True
    while tortent_valtozas:
        tortent_valtozas = False
        for i in range(len(szamok)-1):
            if szamok[i] > szamok[i+1]:
                szamok[i], szamok[i+1], tortent_valtozas  = szamok[i+1], szamok[i], True

szam = [2,4,6,2,3,9,8,1,4,1,7,5,4,2,9,6,8,5]

print(szam)
boborekrendezes(szam)
print(szam)