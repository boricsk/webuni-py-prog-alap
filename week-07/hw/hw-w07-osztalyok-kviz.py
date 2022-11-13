from datetime import datetime
from lib_kviz import *
import os
import unidecode
from difflib import SequenceMatcher
import re
from abc import ABC, abstractmethod

kerdesek_szama = helyes_valaszok = pont = 0

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
            print(SzovegesKerdes.pont)
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
            


kerdesek_es_valaszok = [
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

def egyszerusit(szoveg):
    return unidecode.unidecode(szoveg)

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
   
    for kerdes in kerdesek_es_valaszok:
        kerdesek_szama +=1
        
        if kerdes.kerdest_feltesz():
            helyes_valaszok +=1
    
    pont = SzamKerdes.pont + SzovegesKerdes.pont
    
    results(pont, kerdesek_szama, datetime.now() - start, helyes_valaszok)
    
    TopScoreNormal = topScoreRead()
    if pont > int(TopScoreNormal[0]):
        print('Gratulálunk, rekordot döntöttél!!')
        topScoreWrite(pont, TopScoreNormal[1],TopScoreNormal[2])

elif mode == '2':
    felsorol_kviz()
elif mode == '3':
    tippelos_kviz()
