#Az alapmuveletek enum tipusuak lesznek
from enum import Enum, auto

class Muvelet(Enum):
    PLUSZ = auto()
    MINUSZ = auto()
    SZOROZ = auto()
    OSZT = auto()

class MuveletKivetel(Exception):
    pass

def vegrehajt(a, muvelet, b):
    if type(a) is not int or type(b) is not int:
        raise MuveletKivetel('Hibás paraméter!')
    match muvelet:
        case Muvelet.PLUSZ: return a + b
        case Muvelet.MINUSZ: return a - b
        case Muvelet.SZOROZ: return a * b
        case Muvelet.OSZT: 
            if b == 0:
                raise MuveletKivetel('Osztás nullával!')
            return a // b

try:
    print(vegrehajt(3, Muvelet.OSZT, 0))
except MuveletKivetel as e:
    print(f'Hiba történt! {e}')
    
try:
    print(vegrehajt(3, Muvelet.PLUSZ, 'cica'))
except MuveletKivetel as e:
    print(f'Hiba történt! {e}')