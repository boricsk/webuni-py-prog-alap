import datetime

def palindrom_e(idoertek):    
    ido_str = str(idoertek).replace('-','').replace(' ', '').replace(':','')[::-1]
    try:
        palindrom_ido = datetime.datetime(int(ido_str[:4]), int(ido_str[4:6]), int(ido_str[6:8]), int(ido_str[8:10]), int(ido_str[10:12]), int(ido_str[12:]))
        return idoertek == palindrom_ido
    except:
        return False

start = datetime.datetime(2022,1,1,0,0,0)
end = datetime.datetime(2022,12,31,23,59,59)

while start < end:
    if palindrom_e(start):
        print(f'Találat > {start}')
    start += datetime.timedelta(seconds=1)