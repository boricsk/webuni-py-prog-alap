class IPKivetel(Exception): pass
class NemString(IPKivetel): pass
class NemNegyReszbolAll(IPKivetel): pass
class NemSzam(IPKivetel): pass
class IntervallumHiba(IPKivetel): pass

def ip_ellenoriz(ip):
    if type(ip) is not str:
        raise NemString()
    szam_tomb = ip.split('.')
    if len(szam_tomb) != 4:
        raise NemNegyReszbolAll()
    for szam_string in szam_tomb:
        if not szam_string.isdigit():
            raise NemSzam()
        szam = int(szam_string)
        if not 0 <= szam <= 255:
            raise IntervallumHiba()
        
for ip in [
    None,
    '172162541',
    '0.0.0.alma',
    '0.0.0.0',
    '255.255.255.255',
    '255.255.255.255.3',
    '172.15.254.1',
    '127.0.0.1',
    '192.168.1.01',
    '0.1.2',
    '192.168.1.256',
    '1,1,1,1'
]:
    try:
        ip_ellenoriz(ip)
        print(ip, 'OK')
    except IPKivetel as e:
        print(ip, e.__class__.__name__)