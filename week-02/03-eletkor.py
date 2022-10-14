nev = input('Hogy hívnak? ')
szuletesi_ev_str = input('Melyik évben szulettel? ')
szuletesi_ev_int = int(szuletesi_ev_str)
idei_ev_str = input('Melyik ev van most? ')
idei_ev_int = int(idei_ev_str)
eletkor_int = idei_ev_int - szuletesi_ev_int
eletkor_str = str(eletkor_int)
print(nev + ', te idén ' + eletkor_str + ' éves vagy.')

#rövidítés

print(input('Hogy hívnak? ') + ', te idén ' + str(int(input('Melyik ev van most? ')) - int(input('Melyik évben szulettel? '))) + ' éves vagy.')