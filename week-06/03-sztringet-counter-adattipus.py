from collections import Counter


szöveg = """
Nem minden fajta szarka farka tarkabarka, csak a tarka farkú szarka fajta tarkabarka, 
mert ha minden fajta szarka farka tarkabarka volna, akkor minden szarka fajta tarkabarka 
farkú szarka fajta volna.
"""


print(Counter(szöveg.lower().replace(',','').replace('.','').split()))