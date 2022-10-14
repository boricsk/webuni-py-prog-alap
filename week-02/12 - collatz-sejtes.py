n = 35647
print('n :' + str(n))
lepesek = 0
max_ertek = 0

while n != 1:
    lepesek += 1
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
        if n > max_ertek:
            max_ertek = n

print('Lepesek :' + str(lepesek))
print('Max érték :' + str(max_ertek))