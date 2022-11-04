import re

def ipCheck(ip):
    return bool(re.search(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip))


print(ipCheck('192.168.1.3'))
print(ipCheck('192.168.1.300'))
print(ipCheck('255.255.255.255'))
print(ipCheck('192.168.1.1'))
print(ipCheck('192.168.1.3'))
print(ipCheck('192.168.1.3.0'))
print(ipCheck('192.168.1'))
print(ipCheck('192,168.1.3'))
print(ipCheck('192..168.1.3'))

