#Az előző algoritmus kiszámolja annyiszor ahányszor meghivjuk a metódust ugyanazzal a paraméterrel. hogyan lehetne optimalizálni?
#1. megoldas, ah elmentjuk a terulet, kerulet erteket a konstruktorban
#2. megoldás amikor a self-ekben lévő a, és b-t iktatjuk ki úgy, hogy az osztály konstruktorában számoltatok.
#3. megoldás, amikor kiszedem az absztrakt metódusokat, és ott definiálom a visszatérési értéket, igy a gyerek osztályokban felesleges a terület
#kerulet fvg, mert az os osztalyban levo fgv-k végzik el a retunt.

from abc import ABC, abstractmethod
import math

class NegativSzam(Exception): pass

class Sikidom(ABC):
    #önmagában nem példányosítható, mert nem tudnánk mi az a _terulet és _kerulet.
    def terulet(self):
        return self._terulet
    
    
    def kerulet(self):
        return self._kerulet

#optimalizált, mert elmenti a kiszámolt értéket valahova
class Teglalap(Sikidom):
    def __init__(self, a, b) -> None:
        #self.a = a
        #self.b = b
        #self._terulet = self.a * self.b
        #self._kerulet = 2 * (self.a + self.b)
        if a <= 0 or b <=0:
            raise NegativSzam('Hibás hívás, a paraméterek nem lehetnek negatív számok!')
        self._terulet = a * b
        self._kerulet = 2 * (a + b)
    

class Negyzet(Teglalap):
    def __init__(self, a) -> None:
        super().__init__(a, a)

class Kor(Sikidom):
    PI = 3.1415927
    def __init__(self, r) -> None:
        if r <= 0:
            raise NegativSzam('Hibás hívás, a paraméterek nem lehetnek negatív számok!')
        self._terulet = r ** 2 * Kor.PI
        self._kerulet = 2 * r * Kor.PI
    
    
try:
    teglalap = Teglalap(-3, 4)
    print(teglalap.terulet())
    print(teglalap.kerulet())
except NegativSzam as e:
    print(f'Hiba : {e}')

try:
    negyzet = Negyzet(3)
    print(negyzet.terulet())
    print(negyzet.kerulet())
except NegativSzam as e:
    print(f'Hiba : {e}')

try:
    kor = Kor(3)
    print(kor.terulet())
    print(kor.kerulet())
except NegativSzam as e:
    print(f'Hiba : {e}')