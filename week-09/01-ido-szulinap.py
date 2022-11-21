#Hányszor esett a szülinapom vasárnapra?
import datetime
eredmeny = 0
for ev in range(1976, 2022):
    szulinap = datetime.date(ev, 3, 30)
    if szulinap.isoweekday() == 7:
        eredmeny += 1

print(eredmeny)