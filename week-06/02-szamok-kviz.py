helyes_valasz = 9.8
tolerancia = 0.04
valasz = float(input('Mekkora a gravitációs gyorsulás értéke? [m/s^2] '))
if helyes_valasz - tolerancia < valasz < helyes_valasz + tolerancia:
    print('Válasz helyes')
else:
    print('A válasz helytelen. A helyes válasz', helyes_valasz, ' lett volna.')
# a floatot érdemes határok között kezelni.