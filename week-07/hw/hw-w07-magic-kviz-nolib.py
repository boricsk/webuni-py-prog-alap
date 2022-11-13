from datetime import datetime
#from lib_kviz import *
import os
#import unidecode
from difflib import SequenceMatcher
import re
from abc import ABC, abstractmethod
import random

kerdesek_szama = helyes_valaszok = pont = 0

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

class Kerdes(ABC):
    pont = 0
    def __init__(self, kerdes, helyes_valasz) -> None:
        self.kerdes = kerdes
        self.helyes_valasz = helyes_valasz
            
    def kerdest_feltesz(self):
        valasz = input(self.kerdes + ' ')
        helyes_e, plussz_info = self._valaszt_kiertekel(valasz)
        if helyes_e:
            print('A válasz helyes')
        else:
            print(f'A valasz helytelen, a helyes valasz : {self.helyes_valasz} . {plussz_info}')
        return helyes_e
        
    @abstractmethod
    def _valaszt_kiertekel(self, valasz):
        pass

class SzovegesKerdes(Kerdes):
    
    def __init__(self, kerdes, helyes_valasz, minta) -> None:
        super().__init__(kerdes, helyes_valasz)
        self.minta = minta
    
    def _valaszt_kiertekel(self, valasz):
        if bool(re.search(self.minta, valasz)):
            SzovegesKerdes.pont += 5
            return True, 'A valasz helyes!'
        elif 0.75 < SequenceMatcher(None, valasz, self.helyes_valasz).ratio() < 0.99:
            SzovegesKerdes.pont += 2
            return True, f'A válasz majdnem jó. A helyes válasz {self.helyes_valasz} lett volna. Mivel 75 % -on belül voltál jutalmad 2 pont.'
        else:
            return False, 'A válasz helytelen!'
        
        
class SzamKerdes(Kerdes):
    def _valaszt_kiertekel(self, valasz):
        valasz_szam = int(valasz)
        if valasz_szam == self.helyes_valasz:
            SzamKerdes.pont +=5
            
            return True, ''
        else:
            elteres = abs(valasz_szam - self.helyes_valasz) / self.helyes_valasz * 100
            if elteres <= 2:
                SzamKerdes.pont += 4
                return False, f'A válasz helytelen. Az eltérés : {str(round(elteres, 3))} %. Mivel 2 százalékon belül voltál. A jutalmad 4 pont.'
            elif elteres <=3 and elteres > 2:
                SzamKerdes.pont += 3
                return False, f'A válasz helytelen. Az eltérés : {str(round(elteres, 3))} %. Mivel 2-3 százalék között voltál. A jutalmad 3 pont.'
            elif elteres <=4 and elteres > 3:
                SzamKerdes.pont += 2
                return False, f'A válasz helytelen. Az eltérés : {str(round(elteres, 3))} %. Mivel 3-4 százalék között voltál. A jutalmad 2 pont.'
            else:
                return False, f'A válasz helytelen. Az eltérés : {str(round(elteres, 3))} %. Mivel 4 százalékon kívül voltál sajna nem jár pont.'
            

class KerdesekType1:
    
    def __iter__(self):
        self.kerdesek_es_valaszok = [
            SzovegesKerdes('Itt volt Magyarország első egyeteme. :','Pécs', r'^P[eé]cs$'),
            SzovegesKerdes('Itt gyóntak az árpád házi királyok. :','Báta', r'^B[aá]ta$'),
            SzovegesKerdes('1687 Augusztusában itt mértek döntő vereséget a török seregre. :', 'Nagyharsány', r'^Nagyhars[aá]ny$'),
            SzovegesKerdes('Melyik várost viseli a "Koronázóváros" címet? :','Székesfehérvár', r'^Sz[eé]kesfeh[eé]rv[aá]r$'),
            SzovegesKerdes('Mi ausztria fővárosa? :','Bécs', r'^(B[eé]cs|Wien)$'),
            SzovegesKerdes('Ki játszotta a Bodie-t és a Doyle-t a The Professionals-ban? :','Lewis Collins és Martin Shaw', r'^(Lewis Collins( és |,| |, | ,){1}Martin Shaw)$'),
            SzovegesKerdes('Paul Hunn milyen rekordot állított fel, amelynél 118.1 decibelt regisztráltak? ','A leghangosabb böfögés', r'^[Aa] leghangosabb (b[oö]f[oö]g[eé]s|b[uü]fiz[eé]s|b[oö]ffent[eé]s){1}$'),
            SzamKerdes('Mennyi a Föld-Hold távolsága kilóméterben? :',384400),
            SzamKerdes('Mekkora a Föld átmérője kilóméterben? :',12742),
            SzamKerdes('Az Aranybulla kiadásának éve :',1222),
            SzamKerdes('A HTTP protokol alapértelmezés szerint ezen a porton kommunikál :',80),
                    
            ]
        self.kerdessorszam = 0
        
        return self
    def __next__(self):
        if self.kerdessorszam < len(self.kerdesek_es_valaszok):
            kerdes = self.kerdesek_es_valaszok[self.kerdessorszam]
            self.kerdessorszam += 1
            return kerdes
        else:
            raise StopIteration

class TopScore:
    @staticmethod
    def topScoreWrite(normal, felsorol, tipp):
        TopScores = [normal, felsorol, tipp]
        TopScoreFile = open('kviz.dat','w')
        for elem in TopScores:
            print(elem, file=TopScoreFile)
        TopScoreFile.close()

    @staticmethod
    def topScoreRead():
        TopScores = []
        TopScoreFile = open('kviz.dat','r')
        for sor in TopScoreFile:
            TopScores.append(sor.strip())
        TopScoreFile.close()
        return TopScores

class PrintResults:
    @staticmethod
    def results(pont, kerdesek_sz, eltelt_ido, helyes_valaszok):
        print('')
        print('------------------------------------------------')
        print(f'Eredmeny: {str(100 * helyes_valaszok // kerdesek_sz)} %')
        print(f'A helyes válaszok száma: {str(helyes_valaszok)} volt.')
        print(f'A kérdések száma: {str(kerdesek_sz)} volt.')
        print(f'A pontszámod : {str(pont)}')
        print(f'A megoldási idő :{eltelt_ido}')
        print('------------------------------------------------')
        
class FelsorolKviz:
    @staticmethod
    def felsorol_kviz():
        fels_pont, fels_beirt_valasz, talalatok = 0, set(), set()
        TopScoreFelsorol = TopScore.topScoreRead()
        for fels_kerdes, fels_valasz in felsorol_kerdesek_valaszok:
            fels_beirt_valasz.clear()
            jo_valaszok = set(fels_valasz)
            print(f'A kérdés : {fels_kerdes}')
            start = datetime.now()
            while True:
                user_valasz = input('Kérem a válaszokat (vagy vége) ')
                if bool(re.search(r'^[Vv][eé]ge$',user_valasz)):
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
                TopScore.topScoreWrite(TopScoreFelsorol[0], fels_pont, TopScoreFelsorol[2])
            fels_beirt_valasz.clear()
            talalatok.clear()

class TippelosKviz:
    def tippelos_kviz():
        tipp_pont, jo_valaszok, tipp_valaszlehetoseg, tipp_kerdesek_szama, TopScoreFelsorol = 0, 0, 4, 5, TopScore.topScoreRead()    
        
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
            valasz = input('> ')
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
            TopScore.topScoreWrite(TopScoreFelsorol[0], TopScoreFelsorol[1], tipp_pont)


if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print('')
print(f'---------------------------------------------------------------')
print(f'1 - Normál kvíz.')
print(f'2 - Felsorolásos kvíz.')
print(f'3 - Tippelős kvíz. (Európa tavainak területét kell eltalálnod.)')
print(f'---------------------------------------------------------------')
mode = input('Kérem válasszon kvíztipust. :')

if mode == '1':
    start = datetime.now()
   
    for kerdes in KerdesekType1():
        kerdesek_szama +=1
        
        if kerdes.kerdest_feltesz():
            helyes_valaszok +=1
    
    pont = SzamKerdes.pont + SzovegesKerdes.pont
    
    PrintResults.results(pont, kerdesek_szama, datetime.now() - start, helyes_valaszok)
    
    TopScoreNormal = TopScore.topScoreRead()
    if pont > int(TopScoreNormal[0]):
        print('Gratulálunk, rekordot döntöttél!!')
        TopScore.topScoreWrite(pont, TopScoreNormal[1],TopScoreNormal[2])

elif mode == '2':
    FelsorolKviz.felsorol_kviz()
elif mode == '3':
    TippelosKviz.tippelos_kviz()
