from enum import Enum, auto

class HomersekletSkala(Enum):
    KELVIN = auto()
    CELSIUS = auto()
    FARENHEIT = auto()

class Homerseklet:
    def __init__(self, ertek, skala) -> None:
        self.ertek = ertek
        self.skala = skala
    
    def __str__(self) -> str:
        return f'{self.ertek:.4g} °{self.skala.name.title()}'


def konvertal(homerseklet: Homerseklet, cel:Homerseklet):
    KELVIN_CELSIUS_ELT = 273.15
    match homerseklet.skala, cel:
        case HomersekletSkala.KELVIN, HomersekletSkala.KELVIN: 
            return Homerseklet(homerseklet.ertek, cel)
        case HomersekletSkala.KELVIN, HomersekletSkala.CELSIUS: 
            return Homerseklet(homerseklet.ertek - KELVIN_CELSIUS_ELT, cel)
        case HomersekletSkala.KELVIN, HomersekletSkala.FARENHEIT: 
            return Homerseklet((homerseklet.ertek - KELVIN_CELSIUS_ELT) * 9 / 5 + 32, cel)
        case HomersekletSkala.CELSIUS, HomersekletSkala.KELVIN: 
            return Homerseklet(homerseklet.ertek + KELVIN_CELSIUS_ELT, cel)
        case HomersekletSkala.CELSIUS, HomersekletSkala.CELSIUS: 
            return Homerseklet(homerseklet.ertek, cel)
        case HomersekletSkala.CELSIUS, HomersekletSkala.FARENHEIT: 
            return Homerseklet(homerseklet.ertek * 9/5 + 32, cel)
        case HomersekletSkala.FARENHEIT, HomersekletSkala.KELVIN: 
            return Homerseklet((homerseklet.ertek - 32) * 5/9 + KELVIN_CELSIUS_ELT, cel)
        case HomersekletSkala.FARENHEIT, HomersekletSkala.CELSIUS: 
            return Homerseklet((homerseklet.ertek - 32) * 5/9, cel)
        case HomersekletSkala.FARENHEIT, HomersekletSkala.FARENHEIT: 
            return Homerseklet(homerseklet.ertek, cel)
        



print(konvertal(Homerseklet(300, HomersekletSkala.KELVIN), HomersekletSkala.KELVIN))
print(konvertal(Homerseklet(300, HomersekletSkala.KELVIN), HomersekletSkala.CELSIUS))
print(konvertal(Homerseklet(300, HomersekletSkala.KELVIN), HomersekletSkala.FARENHEIT))

print(konvertal(Homerseklet(20, HomersekletSkala.CELSIUS), HomersekletSkala.KELVIN))
print(konvertal(Homerseklet(20, HomersekletSkala.CELSIUS), HomersekletSkala.CELSIUS))
print(konvertal(Homerseklet(20, HomersekletSkala.CELSIUS), HomersekletSkala.FARENHEIT))

print(konvertal(Homerseklet(70, HomersekletSkala.FARENHEIT), HomersekletSkala.KELVIN))
print(konvertal(Homerseklet(70, HomersekletSkala.FARENHEIT), HomersekletSkala.CELSIUS))
print(konvertal(Homerseklet(70, HomersekletSkala.FARENHEIT), HomersekletSkala.FARENHEIT))