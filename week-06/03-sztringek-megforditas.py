def megfordit(szoveg):
    eredmeny =[]
    for char in szoveg:
        eredmeny.append(char)
    eredmeny.reverse()
    return ''.join(eredmeny)

print(megfordit('mozi'))

def megfordit2(szoveg2):
    return ''.join(reversed([karakter for karakter in szoveg2]))

print(megfordit2('mozi'))