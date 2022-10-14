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

szokoev(int(input('Kérem az évet: ')))