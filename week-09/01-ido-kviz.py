#Dátumos kviz kerdesek bevezetése
import datetime

kerdeksek = [
    ('Mikor született Petőfi Sándor', '1823-01-01'),
    ('Mikor történt az első holdraszállás', '1969-07-20'),
    ('Mikor kiáltottá ki Mo-n a köztársaságot', '1989-10-23')
]

print('A válaszokat EEEE-HH-NN formában kérem!')
for kerdes, helyes_valasz in kerdeksek:
    valasz = input(kerdes)
    valasz_datum = datetime.date.fromisoformat(valasz)
    helyes_datum = datetime.date.fromisoformat(helyes_valasz)
    elteres_nap = (valasz_datum - helyes_datum).days
    if elteres_nap == 0:
        print('A válasz helyes!')
    else:
        print(f'A válasz helytelen, a helyes válasz : {helyes_valasz} az eltérés {elteres_nap}')

