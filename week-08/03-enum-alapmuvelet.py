#Az alapmuveletek enum tipusuak lesznek
from enum import Enum, auto

class Muvelet(Enum):
    PLUSZ = auto()
    MINUSZ = auto()
    SZOROZ = auto()
    OSZT = auto()

def vegrehajt(a, muvelet, b):
    match muvelet:
        case Muvelet.PLUSZ: return a + b
        case Muvelet.MINUSZ: return a - b
        case Muvelet.SZOROZ: return a * b
        case Muvelet.OSZT: return a // b

print(vegrehajt(3, Muvelet.PLUSZ, 2))