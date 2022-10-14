def romai_konvertal(n):
    
    def szamjegyet_konvertal(szamjegy, egyesek, otosok, tizesek):
        if szamjegy <= 3:
            return szamjegy * egyesek
        elif szamjegy == 4:
            return egyesek + otosok
        elif szamjegy <= 8:
            return otosok + (szamjegy - 5) * egyesek
        else:
            return egyesek + tizesek
    
    ezresek = (n // 1000) * 'M'
    szazasok = szamjegyet_konvertal((n // 100) % 10,'C', 'D', 'M' )
    tizesek = szamjegyet_konvertal((n // 10) % 10, 'X', 'L', 'C')
    egyesek = szamjegyet_konvertal((n % 10), 'I', 'V', 'X')
    return ezresek + szazasok + tizesek + egyesek


print(romai_konvertal(6999))
