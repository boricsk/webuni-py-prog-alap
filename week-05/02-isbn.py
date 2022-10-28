def isbn(isbn):
    try:
        csak_szamjegy = isbn.replace('-','').replace(' ','')
        if len(csak_szamjegy) != 13:
            return False
        paros_index = [int(szamjegy) for szamjegy in csak_szamjegy[::2]]
        #print('Paros indexuek :', paros_index)
        paratlan_index = [3 * int(szamjegy) for szamjegy in csak_szamjegy[1::2]]
        #print('Paratlan indexuek :', paratlan_index)
        osszeg = sum(paratlan_index) + sum(paros_index)
        return osszeg % 10 == 0
             
    except:
        return False

print(isbn('978-1-86197-876-9')) #True
print(isbn('978-1-86197-876-5'))
print(isbn('978-1-86197-8768-5'))
print(isbn('978-1-86197-876A-5'))