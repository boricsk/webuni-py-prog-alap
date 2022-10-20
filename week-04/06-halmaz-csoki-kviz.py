csokolade_fajtak = {
    'kerek',
    'szögletes',
    'hosszú',
    'rövid',
    'gömbölyű',
    'lapos',
    'tömör',
    'lapos',
    'lyukas',
    'csomagolt',
    'meztelen',
    'egész',
    'megkezdett',
    'tavalyi',
    'édes',
    'keserű',
    'csöves',
    'mogyorós',
    'tej',
    'likőrös',
    'idei',
    
}

print('Milyen fajta csokoládét szeret Gombóc Artúr?')
beirt_csokifajtak = set()
while True:
    csokolade = input('Csokoládé fajta (vagy vége)')
    if csokolade == 'vege':
        break
    elif csokolade == '':
        continue
    elif csokolade in beirt_csokifajtak:
        print('Ez már volt!')
    elif csokolade in csokolade_fajtak:
        print('Helyes')
    else:
        print('Hibás!')
    beirt_csokifajtak.add(csokolade)

eltalalt_csokifajtak = csokolade_fajtak.intersection(beirt_csokifajtak)
print('Eltalált csokifajták : ' + ', '.join(eltalalt_csokifajtak))
print('Találati arány : ' + str(100 * len(eltalalt_csokifajtak) / len(csokolade_fajtak)) + '% ')
print('Hiányzó csoki fajták : '+ ', '.join(csokolade_fajtak.difference(beirt_csokifajtak)))
print('Hibás tippek :', ', '.join(beirt_csokifajtak.difference(csokolade_fajtak)))
