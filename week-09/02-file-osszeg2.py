with open('./week-09/szamok2.txt') as szamokfile, open('eredmeny2.txt','w') as eredmenyfile:
    for i in range(int(szamokfile.readline().strip())):
        osszeg = 0
        for j in range(int(szamokfile.readline().strip())):
            osszeg += int(szamokfile.readline().strip())
        print(osszeg, file=eredmenyfile)
            