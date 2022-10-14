
def nyari_olimpia(ev):
    evt = ev - 2
    if (ev == 2021 or ev >= 1896 and ev <=2016 and ev % 4 == 0 and ev != 1916 and ev != 1940 and ev != 1944):
        return True 
    else:
        return False

while True:
    ev1 = int(input('Kérem az évet : (0 = Kilép) '))
    if ev1 == 0:
        break
    print(ev1, str(nyari_olimpia(ev1)))