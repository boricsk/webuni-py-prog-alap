# valasz_str = input('Melyik évben vezették be a Gergely naptárat? ') #az input mindig szöveget olvas
# valasz_szam = int(valasz_str)
# helyes_valasz = 1582
# elteres_szam = valasz_szam - helyes_valasz
# elteres_str = str(elteres_szam)
# print('Eltérés :' + elteres_str)

# egysoros megoldás

#valasz_szam = int(input('Melyik évben vezették be a Gergely naptárat? '))

print('Eltérés :' + str(int(input('Melyik évben vezették be a Gergely naptárat? ')) - 1582))

#A változókat behejettesítgetjük, ez a funkcionális programozásnál lényeges, azaz minnél kevesebb változó legyen.


