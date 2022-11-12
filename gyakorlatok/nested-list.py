osztaly,pontszam, names = [], [], []

for _ in range(int(input('Tanulok szama :'))):
    name = input("Név :")
    score = float(input('Pontszám :'))
    student = [name, score]
    osztaly.append([name,score])
    if score not in pontszam:
        pontszam.append(score)

pontszam.sort()

for i in range(len(osztaly)):
    if osztaly[i][1] == pontszam[1]:
        names.append(osztaly[i][0])

names.sort()
for n in names:
    print(n)