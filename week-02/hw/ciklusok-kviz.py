import time
kerdesek_szama = 0
pontszam = 0

start = time.time()

kerdesek = ['Itt volt Magyarország első egyeteme. ',
            'Itt gyóntak az árpád házi királyok.  ',
            '1687 Augusztusában itt mértek döntő vereséget a török seregre. ',
            'Melyik várost viseli a "Koronázóváros" címet? ',
            'Melyik várost viseli a "Leghűségesebb város" címet? ']

helyes_valaszok = ['Pécs',
                   'Báta',
                   'Nagyharsány',
                   'Székesfehérvár',
                   'Sopron']

for i in range(len(kerdesek)):
    valasz = input(kerdesek[i])
    kerdesek_szama +=1
    helyes_valasz = helyes_valaszok[i]
    if valasz == helyes_valasz:
        print('A valasz helyes')
        pontszam +=1
    else:
        print('A válasz helytelen')

end = time.time()

print('Eredmeny: ' + str(100 * pontszam / kerdesek_szama) + ' %')
print('A kérdések száma ' + str(kerdesek_szama) + ' volt.')
print('A pontszámod : ' + str(pontszam))
print('A megoldási idő :' +str(end - start) + ' sec')