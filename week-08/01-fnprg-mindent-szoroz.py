# multipy_all([1,2,3])(2) -> [2,4,6] Curring-el kell megcsinálni

def mindent_szoroz(lista):
    def szoroz(n):
        return list(map(lambda x: x*n, lista)) # át kell listává alakítani
    return szoroz # zárojel nélkul kell hivni. igy a lista [2,3,5] lesz a "lista" a 2 pedig az n
    

print(mindent_szoroz([2,3,5])(2))

'''
map listaképzése a 2 paraméterben megadott listának annak a funkciónak a használatával ami a lambda után van.

'''