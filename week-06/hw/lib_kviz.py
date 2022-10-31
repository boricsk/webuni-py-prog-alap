from datetime import datetime
import random

felsorol_kerdesek_valaszok = [
    ('Sorolja fel a naprendszer bolygóit. ',{'merkur', 'vénusz','föld', 'mars', 'jupiter', 'szaturnusz', 'neptunusz', 'uránusz', 'plútó'}),
    ('Sorolja fel a nemesgázok neveit. ',{'argon','hélium', 'neon', 'kripton', 'xenon', 'radon'}),
]
europa_tavai_terulet = {
        'Ladoga': 17700,
        'Onyega': 9894,
        'Kuybyshev': 6450,
        'Vänern': 5655,
        'Rybinsk': 4580,
        'Saimaa': 4377,
        'Csúd': 3555,
        'Tsimlyansk': 2702,
        'Kremenchuk':2250,
        'Kakhovka:':2155,
        'Vättern': 1893,
        'Szaratov': 1831,
        'Gorkij': 1591,
        'Suur-Saimaa': 1377,
        'Beloye': 1290,
        'Vygozero': 1250,
        'Mälaren': 1140,
        'IJsselmeer': 1100,
        'Päijänne': 1081,
        'Inari': 1040,
        'Kijev': 992,
        'Topozero': 986,
        'Ilmen': 982,
        'Sevan-tó': 940,
        'Segozero:': 906,
        'Pielinen': 894,
        'Oulujärvi': 887,
        'Imandra': 876,
        'Pihlajavesi': 713,
        'Pihkva': 710,
        'Markermeert': 700,
        'Vaskapuk': 700,
        'Kaniv': 675,
        'Pyaozero': 659,
        'Kovdozero': 608,
        'Mingachevir': 605,
        'Orivesi': 601,
        'Balaton': 592,
        'Genf': 581,
        'Dnyiprodzerzsinszk': 567,
        'Haukivesi': 562,
        'Constance': 541,
        'Keitele': 494,
        'Hjälmaren': 485,
        'Kallavesi': 473,
        'Storsjön': 464,
        'Puruvesi': 421,
        'Vozhe': 416,
        'Razelm': 415,
        'Kubenskoye': 407,
        'Lough Neagh': 388,
        'Sheksninskoye': 380,
        'Shkodra': 370,
        'Garda': 370,
        'Mjøsa':365,
        'Pyhäselkä': 361,
        'Ohrid': 358,
        'Lacha': 356,
        'Siljan': 354,
        'Manych-Gudilo': 344,
        'Puula': 330,
        'Torneträsk': 330,
        'Ivankovo': 327,
        'Vodlozero': 322,
        'Lokka': 315,
        'Umbozero': 313,
        'Neusiedl': 315,
        'Höytiäinen': 282,
        'Nagy Prespa': 273,
        'Võrtsjärv': 270,
        'Syamozero': 265,
        'Akkajaure': 261,
        'Közép-Kuyto': 257,
}

def fels_get_len():
    return str(len(felsorol_kerdesek_valaszok))

def tippelos_kviz():
    tipp_pont, jo_valaszok, tipp_valaszlehetoseg, tipp_kerdesek_szama, TopScoreFelsorol = 0, 0, 4, 5, topScoreRead()    
    
    for tavak in random.sample(list(europa_tavai_terulet.keys()), tipp_kerdesek_szama):
        helyes_valasz = europa_tavai_terulet[tavak]
        helytelen_valaszok = list(europa_tavai_terulet.values())
        helytelen_valaszok.remove(helyes_valasz)
        
        kivalasztott_tavak = random.sample(helytelen_valaszok,3)
        kivalasztott_tavak.append(helyes_valasz)
        random.shuffle(kivalasztott_tavak)
        
        kivalasztott_tavak_szotar = {chr(ord('A')+i): kivalasztott_tavak[i] for i in range(tipp_valaszlehetoseg)}
        print('Mekkora a '+ tavak + ' tó területe?')
        
        for betu, terulet in kivalasztott_tavak_szotar.items():
            print('    '+betu+'. '+str(terulet))
        valasz = input('> ')
        valasz_terulet = str(kivalasztott_tavak_szotar[valasz.upper()])
        if valasz_terulet == str(helyes_valasz):
            print('A válasz helyes.')
            tipp_pont += 10
            jo_valaszok += 1
        else:
            print('A válasz helytelen. A jó válasz a(az) '+str(helyes_valasz)+'.')
    
    print('Eredmény :'+str(100*jo_valaszok/tipp_kerdesek_szama)+' %.')
    print('A pontszámod :', tipp_pont)
    
    if tipp_pont > int(TopScoreFelsorol[2]):
        print('Gratulálunk! Rekordot döntöttél!')
        topScoreWrite(TopScoreFelsorol[0], TopScoreFelsorol[1], tipp_pont)
        

def felsorol_kviz():
        fels_pont, fels_beirt_valasz = 0, set()
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
                topScoreWrite(TopScoreFelsorol[0], fels_pont, TopScoreFelsorol[2])
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

def topScoreWrite(normal, felsorol, tipp):
    TopScores = [normal, felsorol, tipp]
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
   
    