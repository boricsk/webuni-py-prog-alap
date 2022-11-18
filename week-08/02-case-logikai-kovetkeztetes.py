#Implikáció (következtetés) https://hu.wikipedia.org/wiki/Implik%C3%A1ci%C3%B3
#Ha akkor... hoz hasonlít (Ha esik az eső, akkor az út vizes.) visszavele nem érvényes.
#Csak akkor hamis ha a igaz és b hamis.
'''
Igazságtábla
p   q   p->q
0   0   1
0   1   1
1   0   0
1   1   1
'''

def kovetkeztet(premissza, konkluzio):
    match premissza, konkluzio:
        case True, True: return True
        case True, False : return False
        case False, True: return True
        case False, False: return True

def kovetkeztet2(premissza, konkluzio):
    match premissza, konkluzio:
        case True, True: return True
        case True, False : return False
        case False, _: return True

def kovetkeztet3(premissza, konkluzio):
    match premissza, konkluzio:
        case True, False : return False
        case _ , _ : return True


print(kovetkeztet(True, True))
print(kovetkeztet(True, False))
print(kovetkeztet(False, True))
print(kovetkeztet(False, False))

print(kovetkeztet2(True, True))
print(kovetkeztet2(True, False))
print(kovetkeztet2(False, True))
print(kovetkeztet2(False, False))

print(kovetkeztet3(True, True))
print(kovetkeztet3(True, False))
print(kovetkeztet3(False, True))
print(kovetkeztet3(False, False))