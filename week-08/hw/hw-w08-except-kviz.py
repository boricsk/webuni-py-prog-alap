from datetime import datetime
from enum import Enum, auto
import random, re
import os

class KerdesTipus(Enum):
    SZOVEG = auto()
    EGESZ_SZAM = auto()
    TIZEDES_SZAM = auto()
    
class UserInputError(Exception): pass

kerdesek_szama = helyes_valaszok = pont = 0

kerdesek_es_valaszok = [
            (KerdesTipus.SZOVEG, 'Itt volt Magyarország első egyeteme. :','Pécs'),
            (KerdesTipus.SZOVEG, 'Itt gyóntak az árpád házi királyok. :','Báta'),
            (KerdesTipus.SZOVEG, '1687 Augusztusában itt mértek döntő vereséget a török seregre. :', 'Nagyharsány'),
            (KerdesTipus.SZOVEG, 'Melyik várost viseli a "Koronázóváros" címet? :','Székesfehérvár'),
            (KerdesTipus.SZOVEG, 'Melyik várost viseli a "Leghűségesebb város" címet? :','Sopron'),
            (KerdesTipus.EGESZ_SZAM, 'Mennyi a Föld-Hold távolsága kilóméterben? :',384400),
            (KerdesTipus.EGESZ_SZAM, 'Mekkora a Föld átmérője kilóméterben? :',12742),
            (KerdesTipus.EGESZ_SZAM, 'Az Aranybulla kiadásának éve :',1222),
            (KerdesTipus.EGESZ_SZAM, 'A HTTP protokol alapértelmezés szerint ezen a porton kommunikál :',80),
            (KerdesTipus.TIZEDES_SZAM, 'Mekkora a nehézségi gyorsulás értéke a Földön? :',9.81),
            (KerdesTipus.TIZEDES_SZAM, 'Mekkora a pi értéke ? :',3.14),
            (KerdesTipus.TIZEDES_SZAM, 'Mekkora a nehézségi gyorsulás értéke a Holdon? :',1.6),
            (KerdesTipus.TIZEDES_SZAM, 'Mekkora a nehézségi gyorsulás értéke a Marson? :',3.69),
            
            ]

felsorol_kerdesek_valaszok = [
    ('Sorolja fel a naprendszer bolygóit. ', {'merkur', 'vénusz','föld', 'mars', 'jupiter', 'szaturnusz', 'neptunusz', 'uránusz', 'plútó'}),
    
    ('Sorolja fel a nemesgázok neveit. ', {'argon','hélium', 'neon', 'kripton', 'xenon', 'radon'}),
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
        print(f'Mekkora a {tavak} tó területe?')
        
        for betu, terulet in kivalasztott_tavak_szotar.items():
            print(f'    {betu}.  {str(terulet)}')
        while True:
            valasz = input('> ')
            try:
                if valasz not in ['a', 'b', 'c', 'd','A', 'B', 'C', 'D']:
                    raise UserInputError('Hibás adatbevitel!')
                else:
                    break
            except UserInputError as e:
                print(f'Hiba : {e}')
        
        valasz_terulet = str(kivalasztott_tavak_szotar[valasz.upper()])
        if valasz_terulet == str(helyes_valasz):
            print('A válasz helyes.')
            tipp_pont += 10
            jo_valaszok += 1
        else:
            print(f'A válasz helytelen. A jó válasz a(az) {str(helyes_valasz)}.')
    
    print(f'Eredmény : {str(100*jo_valaszok/tipp_kerdesek_szama)} %.')
    print(f'A pontszámod : {tipp_pont}')
    
    if tipp_pont > int(TopScoreFelsorol[2]):
        print('Gratulálunk! Rekordot döntöttél!')
        topScoreWrite(TopScoreFelsorol[0], TopScoreFelsorol[1], tipp_pont)
        

def felsorol_kviz():
        fels_pont, fels_beirt_valasz, talalatok = 0, set(), set()
        TopScoreFelsorol = topScoreRead()
        for fels_kerdes, fels_valasz in felsorol_kerdesek_valaszok:
            fels_beirt_valasz.clear()
            jo_valaszok = set(fels_valasz)
            print(f'A kérdés : {fels_kerdes}')
            start = datetime.now()
            while True:
                user_valasz = input('Kérem a válaszokat (vagy vége) ')
                match user_valasz:
                    case n if bool(re.search(r'^[Vv][eé]ge$',user_valasz)):
                        break
                    
                    case '':
                        continue
                    
                    case n if n in fels_beirt_valasz:
                        print('Ez már volt!')
                    
                    case n if n in fels_valasz:
                        print('A válasz helyes!')
                        fels_pont +=1
                    
                    case _ : print('A válasz hibás!')

                fels_beirt_valasz.add(user_valasz)
                talalatok = jo_valaszok.intersection(fels_beirt_valasz)
                ido = datetime.now()-start
            if bool(talalatok):
                print('')
                print('Találatok : ' + ' ,'.join(talalatok))
                print(f'Találati arány : {str(100 * len(talalatok) // len(jo_valaszok))} % ')
                print('Hiányzó elemek : '+ ', '.join(jo_valaszok.difference(fels_beirt_valasz)))
                print('Hibás tippek : ', ', '.join(fels_beirt_valasz.difference(jo_valaszok)))
                print(f'A pontszámod : {str(fels_pont)}')
                print(f'A megoldási idő : {ido}')
                print('')
            
            if fels_pont > int(TopScoreFelsorol[1]):
                print('Gratulálunk! Rekordot döntöttél!')
                topScoreWrite(TopScoreFelsorol[0], fels_pont, TopScoreFelsorol[2])
            fels_beirt_valasz.clear()
            talalatok.clear()

def results(pont, kerdesek_sz, eltelt_ido, helyes_valaszok):
    print('')
    print('------------------------------------------------')
    print(f'Eredmeny: {str(100 * helyes_valaszok // kerdesek_sz)} %')
    print(f'A helyes válaszok száma: {str(helyes_valaszok)} volt.')
    print(f'A kérdések száma: {str(kerdesek_sz)} volt.')
    print(f'A pontszámod : {str(pont)}')
    print(f'A megoldási idő :{eltelt_ido}')
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

def kerdest_feltesz(kerdes, helyes_valasz, tipus):
    while True:
        valasz = input(kerdes)
        match tipus:
            case KerdesTipus.SZOVEG:
                break
            case KerdesTipus.EGESZ_SZAM:
                try:
                    if valasz.isdigit():
                        break
                    else:
                        raise UserInputError(f'Hibás bevitel!')
                except UserInputError as e:
                    print(f'Hiba : {e}')
            case KerdesTipus.TIZEDES_SZAM:
                try:
                    valasz_float = float(valasz)
                    break
                except Exception as e:
                    print(f'Beviteli Hiba : {e}')
   
    global pont
    match tipus:
        case KerdesTipus.SZOVEG:
            if valasz == helyes_valasz:
                pont += 5
                return True, 'A valasz helyes'
            else:
                return False, 'A válasz helytelen'

        case KerdesTipus.EGESZ_SZAM:
            valasz_szam = int(valasz)
            if valasz_szam == helyes_valasz:
                pont += 5
                return True, 'A valasz helyes'
            else:
                elteres = abs(valasz_szam - helyes_valasz) / helyes_valasz * 100
            match elteres:
                case n if 0 <= n <= 2:
                    pont += 4
                    return False, f'A válasz helytelen. Az eltérés : {str(round(elteres, 3))} %. Mivel 2 százalékon belül voltál. A jutalmad 4 pont.'   
                case n if 2 < n <= 3:
                    pont += 3
                    return False, f'A válasz helytelen. Az eltérés : {str(round(elteres, 3))} %. Mivel 2-3 százalék között voltál. A jutalmad 3 pont.'
                case n if 3 < n <= 4:
                    pont += 2
                    return False, f'A válasz helytelen. Az eltérés : {str(round(elteres, 3))} %. Mivel 3-4 százalék között voltál. A jutalmad 2 pont.'
                case n if n > 4:
                    return False, f'A válasz helytelen. Az eltérés : {str(round(elteres, 3))} %. Mivel 4 százalékon kívül voltál sajna nem jár pont.'
        case KerdesTipus.TIZEDES_SZAM:
            tolerancia = 0.05
            #valasz_float = float(valasz)
            if helyes_valasz - tolerancia < valasz_float < helyes_valasz + tolerancia:
                pont += 5
                return True, 'A válsaz helyes!'
            else:
                return False, 'A válasz helytelen! A helyes válasz ' + str(helyes_valasz) + ' lett volna.'

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print('')
print('---------------------------------------------------------------')
print('1 - Normál kvíz. ',str(len(kerdesek_es_valaszok)), 'kérdés.')
print('2 - Felsorolásos kvíz.', fels_get_len(), 'kérdés.')
print('3 - Tippelős kvíz. (Európa tavainak területét kell eltalálnod.)')
print('---------------------------------------------------------------')
while True:
    mode = input('Kérem válasszon kvíztipust. :')
    try:
        if mode in ['1', '2', '3']:
            break
        else:
            raise UserInputError(f'Hibás adatbevitel!')
    except UserInputError as e:
        print(f'Hiba : {e}')
    

match mode:
    case '1':
        start = datetime.now()
        
        for tipus, kerdes, valasz in kerdesek_es_valaszok:
            kerdesek_szama +=1
            helyes_e, valasz_szöveg = kerdest_feltesz(kerdes, valasz, tipus)
            print(valasz_szöveg)
        if helyes_e:
            helyes_valaszok +=1
    
        results(pont, kerdesek_szama, datetime.now() - start, helyes_valaszok)
        TopScoreNormal = topScoreRead()
        if pont > int(TopScoreNormal[0]):
            print('Gratulálunk, rekordot döntöttél!!')
            topScoreWrite(pont, TopScoreNormal[1],TopScoreNormal[2])
    
    case '2': felsorol_kviz()
    case '3': tippelos_kviz()

