import re

def integerCheck(number):
    return bool(re.search(r'^[0-9]*$', str(number)))

def floatCheck(number):
    return bool(re.search(r'^[0-9]*[\.][0-9]*$', str(number)))

def creditCardCheck(number):
    return bool(re.search(r'^(([0-9][0-9][0-9][0-9]+[-]){3}[0-9][0-9][0-9][0-9])|[0-9]{16}$', number))

print(integerCheck(1234567890))
print(integerCheck(1234567890.34))

print(floatCheck(1234567890))
print(floatCheck(1234567890.34))

print(creditCardCheck('1234-5678-1234-1234'))
print(creditCardCheck('134-5678-1234-1234'))
print(creditCardCheck('1234567890ABCDEF'))
print(creditCardCheck('1234567890123456'))