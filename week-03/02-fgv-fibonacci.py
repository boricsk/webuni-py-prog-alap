from re import A


def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, b + a
    return a
    

for i in range(10):
    print(i, fibonacci(i))