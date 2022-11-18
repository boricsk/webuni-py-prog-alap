#https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

def egy(muvelet = None): return 1 if muvelet is None else muvelet(1)
def ketto(muvelet = None): return 2 if muvelet is None else muvelet(2)
def harom(muvelet = None): return 3 if muvelet is None else muvelet(3)
def negy(muvelet = None): return 4 if muvelet is None else muvelet(4)
def ot(muvelet = None): return 5 if muvelet is None else muvelet(5)
def hat(muvelet = None): return 6 if muvelet is None else muvelet(6)
def het(muvelet = None): return 7 if muvelet is None else muvelet(7)
def nyolc(muvelet = None): return 8 if muvelet is None else muvelet(8)
def kilenc(muvelet = None): return 9 if muvelet is None else muvelet(9)
def nulla(muvelet = None): return 0 if muvelet is None else muvelet(0)

def meg(ertek) : return lambda x: x + ertek()
def minusz(ertek) : return lambda x: x - ertek()
def szorozva(ertek) : return lambda x: x * ertek()
def osztva(ertek) : return lambda x: x // ertek()

print(het(szorozva(ot)))
print(negy(meg(kilenc)))
print(nyolc(minusz(harom)))
print(hat(szorozva(ketto)))
print(nyolc(osztva(harom)))

'''
print(het(szorozva(ot)))

Jobbról balra megy a kiértékelés, az ot eredménye 5 lesz, mert nincs paramétere (muvelet is none = true)
Jön a szorozva(5) olyan fgv az eredménye, aminek 1 paramétere van és visszatér annak 5X
def szorozva_ot(x):
    return x * 5

A het(szorozva(5))
'''