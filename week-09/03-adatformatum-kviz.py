#A kviz JSON-osítása
import json

with open('kviz.json', encoding='utf-8') as kerdesek_file:
    kerdesek = json.load(kerdesek_file)

for kerdes_helyes_valas in kerdesek:
    print(kerdes_helyes_valas)
    valasz = input(kerdes_helyes_valas['kérdés'])
    helyes_valasz = kerdes_helyes_valas['valasz']
    if valasz == helyes_valasz:
        print('A válasz helyes!')
    else:
        print(f'A válasz helytelen, a helyes válasz . {helyes_valasz}')
    