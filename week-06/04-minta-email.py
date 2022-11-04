r'[a-z][A-Z]@[a-z][A-Z]'

import re

def emailCheck(email):
    return  bool(re.search(r'[a-zA-Z0-9_.+-]+@([a-zA-Z0-9-]+\.)+[a-z]{2,4}' , email))

print(emailCheck('borics.krisztian@gmail.com'))

print(emailCheck('borics.krisztian.gmail.com'))
print(emailCheck('borics.krisztian@.gmail.com'))
print(emailCheck('@borics.krisztian.gmail.com'))
print(emailCheck('borics.krisztian.gmail.com@'))