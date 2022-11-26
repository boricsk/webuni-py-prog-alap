with open('./week-09/kerdesek.txt', encoding='utf-8') as kerdesek:
    kerdesek = kerdesek.readlines()

with open('./week-09/helyes_valaszok.txt', encoding='utf-8') as valaszok:
    helyes_valaszok = valaszok.readlines()
    
for kerdes, helyes_valasz in zip(kerdesek, helyes_valaszok):
    valasz = input(kerdes.strip() + ' ')
    if valasz == helyes_valasz.strip():
        print('A válasz helyes!')
    else:
        print('A válasz helytelen')
        
