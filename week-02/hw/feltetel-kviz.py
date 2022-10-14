import time
kerdesek_szama = pontszam = 0

kerdesek_szama +=1; start = time.time()
if input('Itt volt Magyarország első egyeteme. ') == 'Pécs':
    print('A valasz helyes'); pontszam +=1
else:
    print('A válasz helytelen')

kerdesek_szama +=1
if input('Itt gyóntak az árpád házi királyok. ') == 'Báta':
    print('A valasz helyes'); pontszam +=1
else:
    print('A válasz helytelen')

kerdesek_szama +=1
if input('1687 Augusztusában itt mértek döntő vereséget a török seregre. ') == 'Nagyharsány':
    print('A valasz helyes'); pontszam +=1
else:
    print('A válasz helytelen')

kerdesek_szama +=1
if input('Melyik várost viseli a "Koronázóváros" címet? ') == 'Székesfehérvár':
    print('A valasz helyes'); pontszam +=1
else:
    print('A válasz helytelen')
    
kerdesek_szama +=1
if input('Melyik várost viseli a "Leghűségesebb város" címet? ') == 'Sopron':
    print('A valasz helyes'); pontszam +=1
else:
    print('A válasz helytelen')

end = time.time()

print('Eredmeny: ' + str(100 * pontszam / kerdesek_szama) + ' %')
print('A kérdések száma ' + str(kerdesek_szama) + ' volt.')
print('A pontszámod : ' + str(pontszam))
print('A megoldási idő :' +str(end - start) + ' sec')