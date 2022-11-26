import json
N = 100
prim_e = (N + 1) * [True]
prim_e[0:1] = 2 *[False] #Az első 2 beállítása False-ra

for i in range(2, int(N ** 0.5) + 1):
    for j in range(2 * i, N + 1, i):
        prim_e[j] = False
        
#print(prim_e)

primek = []
for i in range(N + 1):
    if prim_e[i]:
        primek.append(i)

#print(primek)

with open('./week-09/primek.json', 'w') as primekfile:
    json.dump(primek, primekfile)
    #primekfile.write(' '.join([str(prim) for prim in primek]))
    
with open('./week-09/primek.json') as primek_file:
    primek = json.load(primek_file)

print(primek)