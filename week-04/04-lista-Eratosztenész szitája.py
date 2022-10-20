"""
A probléma : https://hu.wikipedia.org/wiki/Eratoszthen%C3%A9sz_szit%C3%A1ja
"""

N = 120
prim_e = (N + 1) * [True]
prim_e[0:1] = 2 *[False] #Az első 2 beállítása False-ra

for i in range(2, int(N ** 0.5) + 1):
    for j in range(2 * i, N + 1, i):
        prim_e[j] = False
        
print(prim_e)

primek = []
for i in range(N + 1):
    if prim_e[i]:
        primek.append(i)

print(primek)