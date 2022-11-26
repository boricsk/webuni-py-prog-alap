'''
https://api.worldbank.org/v2/country/hu?format=json
A legtöbb adatszolgáltató szervezet 2féle formában szolgáltat adatokat.
1. megnyitod az oldalt és ott vannak az adatok, ez a végső formátum
2. webszolg keresztül, ilyenkor az adatletöltő tovább fogja dolgozni az adatokat általában
A linken a világbank Magyarországra vonatkozó lekérdezése van.

'''
import json

with open('./week-09/vilagbank-hu.json', encoding='utf-8') as vilagbankFile:
    vilagbank_hu =json.load(vilagbankFile)

print(vilagbank_hu[1][0]['incomeLevel']['value']) # JSON adatok kibontása.