def szamjegyosszeg(szam):
    osszeg = 0
    while szam > 0:
        osszeg += szam % 10
        szam //= 10
    
    if osszeg <= 9:
        return osszeg
    else:
        return(szamjegyosszeg(osszeg))

print(szamjegyosszeg(12345))
    