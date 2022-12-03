def digital_root(n):
    while n > 9:
        n = sum(map(int,str(n)))
    return n

digital_root(1639)

print(list(map(int,str(123))))