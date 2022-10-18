"""
Az egész oldalhosszuságú derékszögű háromszöget oldalhosszaiból álló számhármasok. A pitagorasz tétel
értelmében akkor pitagoraszi számhármas az x, y, z ha igaz hogy x2 + y2 = z2 (Diofantoszi egyenlet)
"""

def pitagorasziharmas(max):
    eredmeny = []
    for x in range(1, max + 1):
        for y in range(x, max + 1):
            for z in range(y, max + 1):
                if x * x + y * y == z * z:
                    eredmeny.append((x, y, z))
    return eredmeny

print(pitagorasziharmas(20))