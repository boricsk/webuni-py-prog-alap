from datetime import datetime

from lib_kviz import *

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

def kerdest_feltesz(kerdes, helyes_valasz, tipus):
    
    valasz = input(kerdes)
    global pont
    if tipus == 1:
        if valasz == helyes_valasz:
            print('A valasz helyes')
            pont += 5
            return True
        else:
            print('A válasz helytelen')
            return False
    elif tipus == 2:
        valasz_szam = int(valasz)
        if valasz_szam == helyes_valasz:
            print('A valasz helyes')
            pont += 5
            return True
        else:
            elteres = abs(valasz_szam - helyes_valasz) / helyes_valasz * 100
            if elteres <= 2:
                pont += 4
                print('A válasz helytelen. Az eltérés : ', str(round(elteres, 3)), ' %. Mivel 2 százalékon belül voltál. A jutalmad 4 pont.')
                return False
            elif elteres <=3 and elteres > 2:
                pont += 3
                print('A válasz helytelen. Az eltérés : ', str(round(elteres, 3)), ' %. Mivel 2-3 százalék között voltál. A jutalmad 3 pont.')
                return False
            elif elteres <=4 and elteres > 3:
                pont += 2
                print('A válasz helytelen. Az eltérés : ', str(round(elteres, 3)), ' %. Mivel 3-4 százalék között voltál. A jutalmad 2 pont.')
                return False
            else:
                print('A válasz helytelen. Az eltérés : ', str(round(elteres, 3)), ' %. Mivel 4 százalékon kívül voltál sajna nem jár pont.')
                return False


print('')
print('---------------------')
print('1 - Normál kvíz. ',str(len(kerdesek_es_valaszok)), 'kérdés.')
print('2 - Felsorolásos kvíz.', fels_get_len(), 'kérdés.')
print('---------------------')
mode = input('Kérem válasszon kvíztipust. :')

if mode == '1':
    start = datetime.now()
        
    for tipus, kerdes, valasz in kerdesek_es_valaszok:
        kerdesek_szama +=1
        if kerdest_feltesz(kerdes, valasz, tipus):
            helyes_valaszok +=1
    
    results(pont, kerdesek_szama, datetime.now() - start, helyes_valaszok)
    TopScoreNormal = topScoreRead()
    if pont > int(TopScoreNormal[0]):
        print('Gratulálunk, rekordot döntöttél!!')
        topScoreWrite(pont, TopScoreNormal[1])
elif mode == '2':
    felsorol_kviz()
