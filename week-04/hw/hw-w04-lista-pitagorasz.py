
def pitagorasziharmas(max):
    eredmeny = []
    for x in range(1, max + 1):
        for y in range(x, max + 1):
            for z in range(y, max + 1):
                if x * x + y * y == z * z and x % 3 !=0 and y % 4 !=0 and z % 5 !=0:
                    eredmeny.append((x, y, z))
    return eredmeny

print(pitagorasziharmas(120))