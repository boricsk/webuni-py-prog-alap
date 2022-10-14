n = 25
isPrim = True
for i in range(2, n):
    if n % i == 0:
        isPrim = False
        break
    
print(isPrim)

#a fenti lassú, de elég csak a négyzetgyökéig menni.

n = 25
isPrim = True
i = 2
while i * i <= n:
    if n % i == 0:
        isPrim = False
        break
    i =+ 1

print(isPrim)
