class HexAritm:
    def __init__(self, hexadecimalis):
        self.hexadecimalis = hexadecimalis
    
    def __str__(self):
        return self.hexadecimalis
    
    def __add__(self, masik):
        return hex(self.hexadecimalis + masik.hexadecimalis)
    def __sub__(self, masik):
        return hex(self.hexadecimalis - masik.hexadecimalis)
    def __mul__(self, masik):
        return hex(self.hexadecimalis * masik.hexadecimalis)
    def __mod__(self, masik):
        return hex(self.hexadecimalis % masik.hexadecimalis)
    def __truediv__(self, masik):
        return hex(self.hexadecimalis // masik.hexadecimalis)

print(HexAritm(0xAF) + HexAritm(0xC))
print(HexAritm(0xAF) - HexAritm(0xC))
print(HexAritm(0xAF) * HexAritm(0xC))
print(HexAritm(0xAF) % HexAritm(0xC))
print(HexAritm(0xAF) / HexAritm(0xC))