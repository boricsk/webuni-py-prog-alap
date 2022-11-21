import datetime
#2021-12-02

def palindrom_e(datum):
    
    datum_str = str(datum).replace('-','')[::-1]
    try:
        palindrom_datum = datetime.date(int(datum_str[:4]), int(datum_str[4:6]), int(datum_str[6:]))
        return datum == palindrom_datum
    except:
        return False

aktualis = datetime.date.today()
palindrom_napok_szama = 0
while palindrom_napok_szama < 20:
    if palindrom_e(aktualis):
        print(aktualis)
        palindrom_napok_szama += 1
    aktualis += datetime.timedelta(days=1)
