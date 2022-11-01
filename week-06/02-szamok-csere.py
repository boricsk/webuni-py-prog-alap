from tkinter import E


a = 10
b = 12

print(a, b)

temp = a
a = b
b = temp

print(a, b)

c = 10
d = 12

c,d = d,c
print(c,d)

e = 10
f = 12

e^=f #A
f^=e #B
e^=f #c
print(e,f)

"""
e f A e f B e f C e f
0 0 | 0 0 | 0 0 | 0 0
0 1 | 1 1 | 1 0 | 1 0
1 0 | 1 0 | 1 1 | 0 1
1 1 | 0 1 | 0 1 | 1 1
"""