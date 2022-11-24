
import json
with open('morze.json') as morzeFile:
    morzekódok = json.load(morzeFile)

karakter_morze_atalakito = dict(morzekódok)
morze_karakter_atalakito = {morzekód[1]: morzekód[0] for morzekód in morzekódok} #megcseréli a karaktert a morzekóddal.

def morze_kodol(szoveg):
    kodolt_szoveg = ''
    for karakter in szoveg:
        kodolt_szoveg += karakter_morze_atalakito[karakter] + ' ' 
    return kodolt_szoveg.strip() #a string elejéről és végéről leszedi a szóközöket.

def morze_dekodol(kodolt):
    eredmeny = ''
    for kod in kodolt.split(): #a szoközöknél darabolja fel a sztringet
        eredmeny += morze_karakter_atalakito[kod]
    return eredmeny

kodolt = morze_kodol('HELLOVILAG')
print(kodolt)
dekodolt = morze_dekodol(kodolt)
print(dekodolt)
