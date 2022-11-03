from datetime import datetime
from lib_kviz import *
import os
import unidecode
from difflib import SequenceMatcher

kerdesek_szama = helyes_valaszok = pont = 0

kerdesek_es_valaszok = [
            (1, 'Itt volt Magyarország első egyeteme. :','Pécs'),
            (1, 'Itt gyóntak az árpád házi királyok. :','Báta'),
            (1, '1687 Augusztusában itt mértek döntő vereséget a török seregre. :', 'Nagyharsány'),
            (1, 'Melyik várost viseli a "Koronázóváros" címet? :','Székesfehérvár'),
            (1, 'Melyik várost viseli a "Leghűségesebb város" címet? :','Sopron'),
            (2, 'Mennyi a Föld-Hold távolsága kilóméterben? :',384400),
            (2, 'Mekkora a Föld átmérője kilóméterben? :',12742),
            (2, 'Az Aranybulla kiadásának éve :',1222),
            (2, 'A HTTP protokol alapértelmezés szerint ezen a porton kommunikál :',80),
            
            ]

def egyszerusit(szoveg):
    return unidecode.unidecode(szoveg)

def kerdest_feltesz(kerdes, helyes_valasz, tipus):
    
    valasz = input(kerdes)
    global pont
    if tipus == 1:
        if egyszerusit(valasz) == egyszerusit(helyes_valasz):
            pont += 5
            return True, 'A valasz helyes!'
        elif 0.75 < SequenceMatcher(None, valasz, helyes_valasz).ratio() < 0.99:
            pont += 2
            return True, f'A válasz majdnem jó. A helyes válasz {helyes_valasz} lett volna. Mivel 75 % -on belül voltál jutalmad 2 pont.'
        else:
            return False, 'A válasz helytelen!'
    elif tipus == 2:
        valasz_szam = int(valasz)
        if valasz_szam == helyes_valasz:
            pont += 5
            return True, 'A valasz helyes'
        else:
            elteres = abs(valasz_szam - helyes_valasz) / helyes_valasz * 100
            if elteres <= 2:
                pont += 4
                return False, f'A válasz helytelen. Az eltérés : {str(round(elteres, 3))} %. Mivel 2 százalékon belül voltál. A jutalmad 4 pont.'
            elif elteres <=3 and elteres > 2:
                pont += 3
                return False, f'A válasz helytelen. Az eltérés : {str(round(elteres, 3))} %. Mivel 2-3 százalék között voltál. A jutalmad 3 pont.'
            elif elteres <=4 and elteres > 3:
                pont += 2
                return False, f'A válasz helytelen. Az eltérés : {str(round(elteres, 3))} %. Mivel 3-4 százalék között voltál. A jutalmad 2 pont.'
            else:
                return False, f'A válasz helytelen. Az eltérés : {str(round(elteres, 3))} %. Mivel 4 százalékon kívül voltál sajna nem jár pont.'

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print('')
print('---------------------------------------------------------------')
print(f'1 - Normál kvíz. {str(len(kerdesek_es_valaszok))} kérdés.')
print(f'2 - Felsorolásos kvíz. {fels_get_len()} kérdés.')
print('3 - Tippelős kvíz. (Európa tavainak területét kell eltalálnod.)')
print('---------------------------------------------------------------')
mode = input('Kérem válasszon kvíztipust. :')

if mode == '1':
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
elif mode == '2':
    felsorol_kviz()
elif mode == '3':
    tippelos_kviz()
