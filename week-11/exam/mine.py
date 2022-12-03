import random
from datetime import datetime
import os
from time import *

mineField = [['.' for i in range(10)] for j in range(10)]
userField = [['.' for i in range(10)] for j in range(10)]
minesCoordinates = []
score, difficulty, x, y = 0, 0, 0, 0

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print('Aknakereső játék. Egy 10X10 mátrixban véletlenszerűen vannak az aknák elrejtve.')
print('A feladat, hogy az összes aknamentes területet megtaláld a koordináták megadásával.')
print('Ha "T" jelenik meg akkor találtál egy aknamentes mezőt, ezért jár a pont.')
print('Ha "K" jelenik meg akkor találtál egy aknamentes mezőt viszont a közelben akna van.')
print('Ha "C" jelenik meg akkor megtaláltad a cheat mezőt, ezért extra pont jár és felfedünk egy aknát is.')
print('___________________________________________________________________________________________________')
print('')

while difficulty == 0:
    difficulty = int(input('Nehézségi fok 1-100 > '))

for i in range(difficulty): # difficultly
    xRandom = random.randint(0,9)
    yRandom = random.randint(0,9)
    minesCoordinates.append([xRandom,yRandom])
    mineField[xRandom][yRandom] = 'M'

mineField[random.randint(0,9)][random.randint(0,9)] = 'C'

start = datetime.now()

while True:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
    print('A pontszámod : ',score)
    print('A játékban eltöltött idő : ',datetime.now()-start)
    print('Nehézség : ',difficulty)
    print('Az utolsó koordináták : ', y, ' : ',x)
    print('')
    for sor in userField:
        print(*sor)
    # print('')
    # for sor in mineField:
    #     print(*sor)

    y = int(input('x > '))
    x = int(input('y > '))
    
    if mineField[x][y] == 'M':
        print('Aknára léptél!')
        print('')
        for sor in mineField:
            print(*sor)
        break
    elif mineField[x][y] == 'C':
        userField[minesCoordinates[0][0]][minesCoordinates[0][1]] = 'M'
        userField[x][y] = 'C'
        score += 50
    elif userField[x][y] != '.':
        print('Ez a koordináta már volt!')
        sleep(2)
        continue
    else:
        userField[x][y] = 'T'
        mineField[x][y] = 'T'
        score += 10
        
        count = 0
        
        for xk,yk in minesCoordinates:
            if (x + 1 == xk and y + 1 == yk) or (x == xk and y + 1 == yk) or (x + 1 == xk and y == yk) or (x == xk and y - 1 == yk) or (x-1 == xk and y == yk) or (x-1 == xk and y-1 == yk):
                userField[x][y] = 'K'
                mineField[x][y] = 'T'
        
        for i in range(10):
            for j in range(10):
                if mineField[i][j] == '.':
                    count += 1
        
        if count == 0:
            print('Gratulálunk! Nyertél!')
            print('A pontszámod : ',score)
            print('A játékban eltöltött idő : ',datetime.now()-start)
            print('Nehézség : ',difficulty)
            break
