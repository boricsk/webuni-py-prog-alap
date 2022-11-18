def szokoev(ev):
    print(ev)
    if ev % 4 !=0:
        print('nem szökőév')
    elif ev % 400 == 0:
        print('szökőév')
    elif ev % 100 == 0:
        print('nem szökőév')
    else:
        print('szökőév')

def szokoev2(ev):
    match ev:
        case n if n % 4 != 0: return False
        case n if n % 400 == 0: return True # ha a feltétel teljesül nem megy tovább
        case n if n % 100 == 0: return False
        case _: return True
        
print(szokoev2(int(input('Kérem az évet: '))))