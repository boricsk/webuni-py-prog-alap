def teli_olimpia(ev):
    evt = ev - 2
    if ev > 2022:
        print('Nem tudjuk'); return False
    elif (ev < 1924):
        print('Nem volt még Téli Olimpia.'); return False
    elif (ev % 4 == 0 and ev >= 1924 and ev <= 1992 and ev != 1940 and ev != 1944) or (ev >= 1994 and evt % 4 == 0):
        return True  
    else:
        return False

while True:
    ev1 = int(input('Kérem az évet : (0 = Kilép) '))
    if ev1 == 0:
        break
    print(ev1, str(teli_olimpia(ev1)))