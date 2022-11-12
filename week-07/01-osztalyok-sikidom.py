from abc import ABC, abstractmethod
import math

class Sikidom(ABC):
    @abstractmethod
    def terulet(self):
        pass
    
    @abstractmethod
    def kerulet(self):
        pass


class Teglalap(Sikidom):
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    
    def terulet(self):
        return self.a * self.b
    
    def kerulet(self):
        return 2 * (self.a + self.b)

class Negyzet(Teglalap):
    def __init__(self, a) -> None:
        super().__init__(a, a)

class Kor(Sikidom):
    PI = 3.1415927
    def __init__(self, r) -> None:
        self.r = r
    
    def terulet(self):
        return self.r ** 2 * Kor.PI
    
    def kerulet(self):
        return 2 * self.r * Kor.PI
    
teglalap = Teglalap(3, 4)
print(teglalap.terulet())
print(teglalap.kerulet())


negyzet = Negyzet(3)

print(negyzet.terulet())
print(negyzet.kerulet())

kor = Kor(3)

print(kor.terulet())
print(kor.kerulet())