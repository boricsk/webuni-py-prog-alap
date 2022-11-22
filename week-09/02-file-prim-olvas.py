with open('primek.txt') as primekfile:
    primek_str = primekfile.read()
    primek = [int(prim_str) for prim_str in primek_str.split()]

print(primek)