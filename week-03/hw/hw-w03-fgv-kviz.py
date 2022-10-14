import time
kerdesek_szama = 0
pontszam = 0

kerdesek = ['Itt volt Magyarország első egyeteme. ',
            'Itt gyóntak az árpád házi királyok. ',
            '1687 Augusztusában itt mértek döntő vereséget a török seregre. ',
            'Melyik várost viseli a "Koronázóváros" címet? ',
            'Melyik várost viseli a "Leghűségesebb város" címet? ']

helyes_valaszok = ['Pécs',
                   'Báta',
                   'Nagyharsány',
                   'Székesfehérvár',
                   'Sopron']

def kerdes_feltesz(kerdes, helyes_valasz):
    valasz = input(kerdes)
    if valasz == helyes_valasz:
        print('A válasz helyes.')
        return True
    else:
        print('A válasz helytelen.')
        return False

def results(pont, kerdesek_sz, eltelt_ido):
    print('Eredmeny: ' + str(100 * pont / kerdesek_sz) + '%')
    print('A kérdések száma ' + str(kerdesek_sz) + ' volt.')
    print('A pontszámod : ' + str(pont))
    print('A megoldási idő :' +str(eltelt_ido) + ' sec')

start = time.time()
    
for i in range(len(kerdesek)):
    kerdesek_szama +=1
    if kerdes_feltesz(kerdesek[i],helyes_valaszok[i]):
        pontszam += 1    
   
end = time.time()

results(pontszam, kerdesek_szama, end - start)