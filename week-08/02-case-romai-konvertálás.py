def romai_konvertal(szam):
        
        def szamjegyet_konvertal(szamjegy, egyesek, otosok, tizesek):
            match szamjegy:
                case n if 0 <= n <= 3: return szamjegy * egyesek
                case 4: return egyesek + otosok
                case n if 5 <= n <= 8: return otosok + (szamjegy - 5) * egyesek
                case 9: return egyesek + tizesek
                   
        if type(szam) is not int or szam < 1 or szam > 3999:
            return f'Nem lehet római számmá konvertálni : {szam}'
        
        ezresek = (szam // 1000) * 'M'
        szazasok = szamjegyet_konvertal((szam // 100) % 10,'C', 'D', 'M' )
        tizesek = szamjegyet_konvertal((szam // 10) % 10, 'X', 'L', 'C')
        egyesek = szamjegyet_konvertal((szam % 10), 'I', 'V', 'X')
        return ezresek + szazasok + tizesek + egyesek
    
print(romai_konvertal(1984))