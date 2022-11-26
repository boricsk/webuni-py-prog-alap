from datetime import datetime
from enum import Enum, auto
import random, re, json
import os

class UserInputError(Exception): pass

kerdesek_szama, helyes_valaszok, pont = 0,0,0

def checkFileLocation(file):
    if os.path.isfile(file):
        return True
    else:
        print(f'A játék nem folytatható, mert az adatfile {file} hiányzik.')
        exit()

def tippelos_kviz():
    tipp_pont, jo_valaszok, tipp_valaszlehetoseg, tipp_kerdesek_szama, TopScoreFelsorol = 0, 0, 4, 5, topScoreRead()    
   
    dataFile = './week-09/hw/europa-tavai.json'
    if checkFileLocation(dataFile):
        with open('europa-tavai.json', encoding='utf-8') as TippelosFile:
            europa_tavai_json = json.load(TippelosFile)
            europa_tavai_terulet = dict(europa_tavai_json)
    
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
        topScoreWrite(TopScoreFelsorol[0], TopScoreFelsorol[1], tipp_pont, TopScoreFelsorol[3])

def felsorol_kviz():
        fels_pont, fels_beirt_valasz, talalatok = 0, set(), set()
        TopScoreFelsorol = topScoreRead()
        felsorolDataFile = './week-09/hw/felsorol-kviz.json'
        if checkFileLocation(felsorolDataFile):
            with open(felsorolDataFile,encoding='utf-8') as felsorolDataFile:
                felsorol_kerdesek_es_valaszok_json = json.load(felsorolDataFile)
                
        for felsKvizAdatok in felsorol_kerdesek_es_valaszok_json:
            fels_beirt_valasz.clear()
            
            jo_valaszok = set(felsKvizAdatok['valasz'])
            print(f"A kérdés : {felsKvizAdatok['kerdes']}")
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
                    
                    case n if n in felsKvizAdatok['valasz']:
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
                topScoreWrite(TopScoreFelsorol[0], fels_pont, TopScoreFelsorol[2],TopScoreFelsorol[3])
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

def topScoreWrite(normal, felsorol, tipp, datum):
    TopScores = [normal, felsorol, tipp, datum]
    TopScoreFile = open('./week-09/hw/kviz.dat','w')
    for elem in TopScores:
        print(elem, file=TopScoreFile)
    TopScoreFile.close()

def topScoreRead():
    TopScores = []
    TopScoreFile = open('./week-09/hw/kviz.dat','r')
    for sor in TopScoreFile:
        TopScores.append(sor.strip())
    TopScoreFile.close()
    return TopScores

def kerdest_feltesz(kerdes, helyes_valasz, tipus):
    while True:
        valasz = input(kerdes)
        match tipus:
            case 'SZOVEG':
                break
            case 'EGESZ_SZAM':
                try:
                    if valasz.isdigit():
                        break
                    else:
                        raise UserInputError(f'Hibás bevitel!')
                except UserInputError as e:
                    print(f'Hiba : {e}')
            case 'TIZEDES_SZAM':
                try:
                    valasz_float = float(valasz)
                    break
                except Exception as e:
                    print(f'Beviteli Hiba : {e}')
   
    global pont
    match tipus:
        case 'SZOVEG':
            if valasz == helyes_valasz:
                pont += 5
                return True, 'A valasz helyes'
            else:
                return False, 'A válasz helytelen'

        case 'EGESZ_SZAM':
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
        case 'TIZEDES_SZAM':
            tolerancia = 0.05
            #valasz_float = float(valasz)
            if helyes_valasz - tolerancia < valasz_float < helyes_valasz + tolerancia:
                pont += 5
                return True, 'A válsaz helyes!'
            else:
                return False, 'A válasz helytelen! A helyes válasz ' + str(helyes_valasz) + ' lett volna.'

def datum_kviz():
    running = False
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
    datum_pont, datum_kerdesek_szama, jo_valaszok_szama, valasz, topScoreDate = 0,0,0,'',topScoreRead()
    start = datetime.now()
    print('A válaszokat EEEE-HH-NN kérem!')
    
    try:
        with open('./week-09/hw/datum-kerdes.kviz', encoding='utf-8') as datum_kerdesek_file:
            datum_kerdesek = datum_kerdesek_file.readlines()
        running = True
    except Exception as e:
        print(f'Hiba a kérdéseket tartalmazó file megnyitásakor! {e}')
    
    try:
        with open('./week-09/hw/datum-valasz.kviz', encoding='utf-8') as datum_valasz_file:
            datum_valasz = datum_valasz_file.readlines()
        running = True
    except Exception as e:
        print(f'Hiba a válaszokat tartalmazó file megnyitásakor! {e}')
    
    datum_kerdesek_szama = len(datum_kerdesek)
    
    for kerdes, helyes_valasz in zip(datum_kerdesek, datum_valasz):
        
        while running:
            valasz = input(kerdes.strip() + ' ')
            if bool(re.search(r'^[0-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]$',valasz.strip())):
                break
            else:
                print('A válasz formátuma nem megfelelő!')
            
            
        valasz_datum = datetime.fromisoformat(valasz.strip())
        helyes_datum = datetime.fromisoformat(helyes_valasz.strip())
        elteres = (helyes_datum - valasz_datum).days
        if elteres == 0:
            print('A válasz helyes!')
            datum_pont += 10
            jo_valaszok_szama += 1
        else:
            print(f'A válasz helytelen! A helyes válasz : {helyes_datum}. Az eltérés : {elteres}')
    
    results(datum_pont, datum_kerdesek_szama, datetime.now()-start, jo_valaszok_szama)
    if datum_pont > int(topScoreDate[3]):
        print('Gratulálunk, rekordot döntöttél!!')
        topScoreWrite(topScoreDate[0], topScoreDate[1],topScoreDate[2], datum_pont)
        

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print('')
print('---------------------------------------------------------------')
print('1 - Normál kvíz.')
print('2 - Felsorolásos kvíz.')
print('3 - Tippelős kvíz. (Európa tavainak területét kell eltalálnod.)')
print('4 - Dátum kvíz.')
print('---------------------------------------------------------------')
while True:
    mode = input('Kérem válasszon kvíztipust. :')
    try:
        if mode in ['1', '2', '3', '4']:
            break
        else:
            raise UserInputError(f'Hibás adatbevitel!')
    except UserInputError as e:
        print(f'Hiba : {e}')
    

match mode:
    case '1':
        start = datetime.now()
        NormalDataFile = './week-09/hw/normal-kviz.json'
        if checkFileLocation(NormalDataFile):
            with open(NormalDataFile, encoding='utf-8') as NormalDataFile:
                kerdesek_es_valaszok_json = json.load(NormalDataFile)
                    
        for normalKvizAdatok in kerdesek_es_valaszok_json:
            kerdesek_szama +=1
            helyes_e, valasz_szöveg = kerdest_feltesz(normalKvizAdatok['kerdes'], normalKvizAdatok['valasz'], normalKvizAdatok['KerdesTipus'])
            print(valasz_szöveg)
            if helyes_e:
                helyes_valaszok +=1
    
        results(pont, kerdesek_szama, datetime.now() - start, helyes_valaszok)
        TopScoreNormal = topScoreRead()
        if pont > int(TopScoreNormal[0]):
            print('Gratulálunk, rekordot döntöttél!!')
            topScoreWrite(pont, TopScoreNormal[1],TopScoreNormal[2],TopScoreNormal[3])
    
    case '2': felsorol_kviz()
    case '3': tippelos_kviz()
    case '4': datum_kviz()

