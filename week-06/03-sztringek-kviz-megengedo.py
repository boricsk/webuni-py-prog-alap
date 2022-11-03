import unidecode
from difflib import SequenceMatcher

def egyszerusit(szoveg):
    return szoveg.strip()\
        .lower()\
        .replace('á', 'a')\
        .replace('é', 'e')\
        .replace('ö', 'o')\
        .replace('ő', 'o')\
        .replace('ú', 'u')\
        .replace('ű', 'u')\
        .replace('ü', 'u')\
        .replace('ó', 'o')

def egyszerusit2(szoveg):
    return unidecode.unidecode(szoveg)

valasz = input('Mi Olaszország fővárosa? ')
helyes_valasz = 'Róma'

if egyszerusit2(valasz) == egyszerusit2(helyes_valasz):
    print('A válasz helyes.')
elif SequenceMatcher(None, valasz, helyes_valasz).ratio() >= 0.55: #a None mindíg kell az elejére
    print('A válasz majdnam jó.')
else:
    print(f'A válasz helytelen, a helyes válasz {helyes_valasz} lett volna.')