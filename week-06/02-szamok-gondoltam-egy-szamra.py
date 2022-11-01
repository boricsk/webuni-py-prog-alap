import random
max = 100
szam = random.randint(1, max)
print('Gondoltam egy számra 1 és ', max, ' között, találd ki!')
tippek_szama = 0
while True:
    tippek_szama += 1
    tipp = int(input('Tipp > '))
    if szam == tipp:
        print('Eltaláltad!')
        print('A tippek száma : ', tippek_szama)
        break
    elif szam > tipp:
        print('A szám nagyobb.')
    else:
        print('A szám kisebb.')

# optimális esetben a tippek száma az log2(max)