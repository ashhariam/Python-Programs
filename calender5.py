list = []
import calendar as c
for i in c.day_name:
    i = i.lower()
    list.append(i)
    if 'w' not in i:
        print(i)