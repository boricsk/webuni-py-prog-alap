with open('./week-09/szamok.txt') as szamokfile:
    szamok_lista = szamokfile.readlines()

with open('./week-09/eredmeny.txt', 'w') as eredmenyfile:
    for szamok_str in szamok_lista:
        print(sum([int(szam_str) for szam_str in szamok_str.strip().split()]),file=eredmenyfile)