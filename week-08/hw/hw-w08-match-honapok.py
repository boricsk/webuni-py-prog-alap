def honapok_hossza(honap):
    match honap:
        case 1|3|5|7|8|10|12: return 31
        case 2: return 28
        case _ : return 30

for i in range(1,13):
    print(i, ' ', honapok_hossza(i))
       