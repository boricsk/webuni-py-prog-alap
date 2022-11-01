import random

random.seed(1)
ossz = 10000000
belul = 0
for _ in range(ossz):
    x = random.random()
    y = random.random()
    if x ** 2 + y ** 2 <=1:
        belul += 1
print(4 * belul / ossz)
