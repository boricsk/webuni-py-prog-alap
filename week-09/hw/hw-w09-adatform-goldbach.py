# https://hu.wikipedia.org/wiki/Goldbach-sejt%C3%A9s

from datetime import datetime
import json, os

primek = set()
nem_primek = set()
akt_megoldas_json = {}

goldbachDataFile = './week-09/hw/goldbach.json'
if os.path.isfile(goldbachDataFile):
    with open(goldbachDataFile) as goldbachData:
        akt_megoldas_json = json.load(goldbachData)
else:
    akt_megoldas_json = {}

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
    global akt_megoldas_json
    megoldas = {'prim 1': 0, 'prim 2': 0} #(0,0,0)
    for i in range(4, n, 2):
        if i in akt_megoldas_json:
            if akt_megoldas_json['prim 1'] > akt_megoldas_json['prim 2']:
                return akt_megoldas_json[i]
        else:
            akt_megoldas = goldbach_par(i)
            akt_megoldas_json[i] = {'prim 1': akt_megoldas[0], 'prim 2': akt_megoldas[1]} # i lesz a kulcs a prim 1 és 2 pedig az adatok
            if akt_megoldas[0] > megoldas['prim 1']:
                megoldas = {'prim 1': akt_megoldas[0], 'prim 2': akt_megoldas[1]}
                #print(akt_megoldas_json)
    return i, megoldas

# for i in range(20):
#     if prim_e(i):
#         print(i)

# for i in range(4, 20, 2):
#     print(i, goldbach_par(i))

start = datetime.now()
print(goldbach_max(100))
with open('./week-09/hw/goldbach.json',mode='w') as goldbachDataW:
    json.dump(akt_megoldas_json, goldbachDataW, indent=4)
print(datetime.now()-start)