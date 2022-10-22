from datetime import datetime
from turtle import width

felsorol_kerdesek_valaszok = [
    ('Sorolja fel a naprendszer bolygóit. ',{'merkur', 'vénusz','föld', 'mars', 'jupiter', 'szaturnusz', 'neptunusz', 'uránusz', 'plútó'}),
    ('Sorolja fel a nemesgázok neveit. ',{'argon','hélium', 'neon', 'kripton', 'xenon', 'radon'}),
]

def fels_get_len():
    return str(len(felsorol_kerdesek_valaszok))

def felsorol_kviz():
        fels_pont = 0
        fels_beirt_valasz = set()
        TopScoreFelsorol = topScoreRead()
        for fels_kerdes, fels_valasz in felsorol_kerdesek_valaszok:
            fels_beirt_valasz.clear()
            jo_valaszok = set(fels_valasz)
            print('A kérdés : ',fels_kerdes)
            start = datetime.now()
            while True:
                user_valasz = input('Kérem a válaszokat kisbetűvel (vagy vége) ')
                if user_valasz == 'vége':
                    break
                elif user_valasz == '':
                    continue
                elif user_valasz in fels_beirt_valasz:
                    print('Ez már volt.')
                elif user_valasz in fels_valasz:
                    print('A válasz helyes!')
                    fels_pont += 1
                else:
                    print('A válasz hibás!')
                fels_beirt_valasz.add(user_valasz)
                talalatok = jo_valaszok.intersection(fels_beirt_valasz)
                ido = datetime.now()-start
            print('')
            print('Találatok : ' + ' ,'.join(talalatok))
            print('Találati arány : ', str(100 * len(talalatok) // len(jo_valaszok)) + '% ')
            print('Hiányzó elemek : '+ ', '.join(jo_valaszok.difference(fels_beirt_valasz)))
            print('Hibás tippek : ', ', '.join(fels_beirt_valasz.difference(jo_valaszok)))
            print('A pontszámod : ',str(fels_pont))
            print('A megoldási idő : ',ido)
            print('')
            if fels_pont > int(TopScoreFelsorol[1]):
                print('Gratulálunk! Rekordot döntöttél!')
                topScoreWrite(TopScoreFelsorol[0], fels_pont)
            fels_beirt_valasz.clear()
            talalatok.clear()

def results(pont, kerdesek_sz, eltelt_ido, helyes_valaszok):
    print('')
    print('------------------------------------------------')
    print('Eredmeny: ' + str(100 * helyes_valaszok // kerdesek_sz) + '%')
    print('A helyes válaszok száma: ' + str(helyes_valaszok) + ' volt.')
    print('A kérdések száma: ' + str(kerdesek_sz) + ' volt.')
    print('A pontszámod : ' + str(pont))
    print('A megoldási idő :', eltelt_ido)
    print('------------------------------------------------')

def topScoreWrite(normal, felsorol):
    TopScores = [normal, felsorol]
    TopScoreFile = open('kviz.dat','w')
    for elem in TopScores:
        print(elem, file=TopScoreFile)
    TopScoreFile.close()

def topScoreRead():
    TopScores = []
    TopScoreFile = open('kviz.dat','r')
    for sor in TopScoreFile:
        TopScores.append(sor.strip())
    TopScoreFile.close()
    return TopScores
   
    