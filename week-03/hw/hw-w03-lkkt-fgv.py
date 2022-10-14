def lnko(a,b):
    
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def lkkt(a,b):
    return (a*b) // lnko(a,b)

a = int(input('Kérek egy számot! '))
b = int(input('Kérek egy másikat is '))

print(a, 'és', b, 'legkisebb közös többszöröse : ', lkkt(a, b))