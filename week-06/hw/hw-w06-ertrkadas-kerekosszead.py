def kerek_osszead(a, b):
    c = a + b
    if round(c, 5) != round(c, 13):

        return round(c, 5), True
    else:

        return c, False
    
print(kerek_osszead(0.00010, 0.000005))