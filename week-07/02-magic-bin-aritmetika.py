class Binaris:
    def __init__(self, binaris):
        self.binaris = binaris

    def __str__(self):#ha nem valósitod meg az str-t akkor a print esetén az objektum tulajdonságait fogja kiirni.
        return self.binaris
    
    def __lshift__(self, bitek_szama):
        return self.binaris + bitek_szama * '0'
    
    def __rshift__(self, bitek_szama):
        if len(self.binaris) < bitek_szama:
            return ''
        else:
            return self.binaris[:-bitek_szama]
    
    def __and__(self, masik):
        binaris1, binaris2 = Binaris._kiegeszit(self.binaris, masik.binaris)  #ezt miért kell?? masik-al is jó.
        print('> ', masik)
        return ''.join(['1' if binaris1[i] == '1' and binaris2[i] == '1' else '0' for i in range(len(binaris1))])
    
    def __or__(self, masik):
        binaris1, binaris2 = Binaris._kiegeszit(self.binaris, masik.binaris)  #ezt miért kell?? masik-al is jó.
        print('> ', masik)
        return ''.join(['1' if binaris1[i] == '1' or binaris2[i] == '1' else '0' for i in range(len(binaris1))])
    
    def __xor__(self, masik):
        binaris1, binaris2 = Binaris._kiegeszit(self.binaris, masik.binaris)  #ezt miért kell?? masik-al is jó.
        print('> ', masik)
        return ''.join(['1' if binaris1[i] != binaris2[i] else '0' for i in range(len(binaris1))])
    
    def __invert__(self):
        return ''.join(['1' if self.binaris[i] == '0' else '0' for i in range(len(self.binaris))])
    
    
    @staticmethod #ha a hossz nem egyenlő
    def _kiegeszit(binaris1, binaris2):
        if len(binaris1) == len(binaris2):
            return binaris1, binaris2
        elif len(binaris1) > len(binaris2):
            return binaris1, (len(binaris1)-len(binaris2)) * '0' + binaris2
        else:
            return (len(binaris2)-len(binaris1)) * '0' + binaris1, binaris2
            
        

print(Binaris('101010') << 3)
print(Binaris('101010') >> 3)
print(Binaris._kiegeszit('101010', '1100'))
print(Binaris('1100') & Binaris('1010'))
print(Binaris('1100') | Binaris('1010'))
print(Binaris('1100') ^ Binaris('1010'))
print(~Binaris('110010110'))