#matek.py
def kerek_osszead(a, b):
    c = a + b
    if round(c, 6) == round(c, 9):
        return round(c, 6)
    else:
        return c

def kerek_kivon(a, b):
    c = a - b
    if round(c, 6) == round(c, 9):
        return round(c, 6)
    else:
        return c
    
def kerek_szoroz(a, b):
    c = a * b
    if round(c, 6) == round(c, 9):
        return round(c, 6)
    else:
        return c