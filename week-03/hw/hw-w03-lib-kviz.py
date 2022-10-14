import time
from lib_kviz import *

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

start = time.time()
    
for i in range(len(kerdesek)):
    kerdesek_szama +=1
    if kerdes_feltesz(kerdesek[i],helyes_valaszok[i]):
        pontszam += 1    
   
end = time.time()

results(pontszam, kerdesek_szama, end - start)