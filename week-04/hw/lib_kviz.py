
def results(pont, kerdesek_sz, eltelt_ido, helyes_valaszok):
    print('')
    print('------------------------------------------------')
    print('Eredmeny: ' + str(100 * helyes_valaszok // kerdesek_sz) + '%')
    print('A helyes válaszok száma: ' + str(helyes_valaszok) + ' volt.')
    print('A kérdések száma: ' + str(kerdesek_sz) + ' volt.')
    print('A pontszámod : ' + str(pont))
    print('A megoldási idő :', eltelt_ido)
    print('------------------------------------------------')