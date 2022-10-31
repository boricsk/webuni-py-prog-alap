def fibonacci(n):
    a, b = 0, 1
    for _ in range(n): # mivel az i nem használatos, lehet _ helyettesiteni
        a, b = b, b + a # a temp változók ki lehet ezzel kerülni.
    return a
    

for i in range(10):
    print(i, fibonacci(i))