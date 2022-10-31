"""
x = negyzetgyok(n)
x*x = n
x*x - n = 0

f(x) = x*x - n
f'(x) = 2x

x(n + 1) = xn - f(x) / f'(x)
x(n + 1) = xn - (x*x) - n /2x
"""

from re import X


def newton_negyzetgyok(n):
    x = n
    while x*x - n > 0.0000000001:
        x = x - (x*x -n) / (2*x)
    return x

print(newton_negyzetgyok(2))