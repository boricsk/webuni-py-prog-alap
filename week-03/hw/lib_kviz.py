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
    print('A megoldási idő :' +str(round(eltelt_ido, 3)) + ' sec')