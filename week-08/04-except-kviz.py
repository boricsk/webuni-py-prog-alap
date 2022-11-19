while True:
    try:
        valasz_str = input('Melyik évben vezették be a Gergely naptárat? ') #az input mindig szöveget olvas
        valasz_szam = int(valasz_str)
        break
    except Exception as e:
        print(f'Hiba történt! {e}')
        
helyes_valasz = 1582
elteres_szam = valasz_szam - helyes_valasz
elteres_str = str(elteres_szam)
print('Eltérés :' + elteres_str)
