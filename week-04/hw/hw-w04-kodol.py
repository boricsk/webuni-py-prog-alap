

kodok = {chr(i) : str(i+9657) for i in range(65,91)}
dekodok = {str(i+9657) : chr(i) for i in range(65,91)}

def kodol(szöveg):
    kodolt_szöveg = ''
    for karakter in szöveg:
        kodolt_szöveg += kodok[karakter] + ' '
    return kodolt_szöveg.strip()

def dekodol(szoveg):
    dekodolt_szoveg = ''
    for kod in szoveg.split():
        dekodolt_szoveg += dekodok[kod]
    return dekodolt_szoveg

kodolt = kodol('HELLO')
print(kodolt)
dekodolt = dekodol(kodolt)
print(dekodolt)