import os, psutil
from datetime import datetime

class Kor:
    PI = 3.1415927
    def __init__(self, r) -> None:
        self.r = r
    
    def terulet(self):
        return self.r ** 2 * Kor.PI
    
    def kerulet(self):
        return 2 * self.r * Kor.PI

kor = Kor(10)
print(kor.terulet())
print(kor.kerulet())

#Mi van ha sok kör van

start = datetime.now()
korok = [Kor(10) for i in range(1_000_000)]
print(sum([kor.terulet() for kor in korok]))
print(sum([kor.kerulet() for kor in korok]))
print(datetime.now() - start)

print(f'Memória igény : {psutil.Process(os.getpid()).memory_info().rss:,d} byte')

#Opt 1. Kiszámoljuk a konstruktorban a teruletet és a keruletet. (Megnőtt a memóriahsználat és a futási idő is)
class Kor1:
    PI = 3.1415927
    def __init__(self, r) -> None:
        self.r = r
        self._terulet = self.r ** 2 * Kor.PI
        self._kerulet = 2 * self.r * Kor.PI
    
    def terulet(self):
        return self._terulet
    
    def kerulet(self):
        return self._kerulet

kor1 = Kor1(10)
start = datetime.now()
korok = [Kor1(10) for i in range(1_000_000)]
print()
print(sum([kor1.terulet() for kor1 in korok]))
print(sum([kor1.kerulet() for kor1 in korok]))
print(datetime.now() - start)

print(f'Memória igény 2: {psutil.Process(os.getpid()).memory_info().rss:,d} byte')

#Gyorsítótárazás, azaz, ha még 1x ugyanazt számoljuk akkor nem számoljuk, hanem kiszedjük a gyorsítótárból.
class Kor2:
    PI = 3.1415927
    gyorsitotar = {}
    def __new__(cls, *args, **kwargs):
        sugar = args[0]
        if sugar not in Kor2.gyorsitotar:
            peldany = super(Kor2, cls).__new__(cls) #pélányosítás
            Kor2.gyorsitotar[sugar] = peldany #a létrehozott példány gyorsítótárazása
        return Kor2.gyorsitotar[sugar]
    
    
    def __init__(self, r) -> None:
        self.r = r
        self._terulet = self.r ** 2 * Kor.PI
        self._kerulet = 2 * self.r * Kor.PI
    
    def terulet(self):
        return self._terulet
    
    def kerulet(self):
        return self._kerulet
    
kor2 = Kor2(10)
start = datetime.now()
korok = [Kor2(10) for i in range(1_000_000)]
print()
print(sum([kor2.terulet() for kor2 in korok]))
print(sum([kor2.kerulet() for kor2 in korok]))
print(datetime.now() - start)
print(f'Memória igény 3: {psutil.Process(os.getpid()).memory_info().rss:,d} byte')