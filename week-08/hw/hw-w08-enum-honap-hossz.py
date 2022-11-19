from enum import Enum, auto

class Honapok(Enum):
    JANUAR = auto()
    FEBTUAR = auto()
    MARCIUS = auto()
    APRILIS = auto()
    MAJUS = auto()
    JUNIUS = auto()
    JULIUS = auto()
    AUGUSZTUS = auto()
    SZEPTEMBER = auto()
    OKTOBER = auto()
    NOVEMBER = auto()
    DECEMBER = auto()
    
def honapok_hossza(honap):
    match honap:
        case Honapok.JANUAR|Honapok.MARCIUS|Honapok.MAJUS|Honapok.JUNIUS|Honapok.AUGUSZTUS|Honapok.OKTOBER|Honapok.DECEMBER: return 31
        case Honapok.FEBTUAR: return 31
        case _ : return 30

for i in Honapok:
    print(i.name, ' ', honapok_hossza(i))