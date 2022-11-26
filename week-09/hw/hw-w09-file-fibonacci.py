def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# for i in range(10):
#     print(i, fibonacci(i))

def fibonacci_gyors(n):
    fibonacci_szam = (n + 1) * [None]
    
    def fib_rekurziv(x):
        if fibonacci_szam[x] is not None:
            return fibonacci_szam[x]
        else:
            if x <= 1:
                eredmeny = x
            else:
                eredmeny = fib_rekurziv(x - 1) + fib_rekurziv(x - 2)
            fibonacci_szam[x] = eredmeny
            return eredmeny
    return fib_rekurziv(n)
    
 
# for i in range(50):
#     print(i, fibonacci_gyors(i))

def fibonacci_gyors2(n):
    fibonacci_szam = (n + 1) * [None]
    
    def fib_rekurziv(x):
        if fibonacci_szam[x] is None:
            fibonacci_szam[x] = x if x <= 1 else fib_rekurziv(x - 1) + fib_rekurziv(x - 2)
        return fibonacci_szam[x]
    return fib_rekurziv(n)
    
with open('./week-09/hw/fibonacci.txt','w', encoding='utf-8') as fibofile:
    for i in range(50):
        print(i, fibonacci_gyors2(i), file=fibofile)
        
with open('./week-09/hw/fibonacci.txt', encoding='utf-8') as fibofile:
    fib_kiir = fibofile.read()
print(fib_kiir)