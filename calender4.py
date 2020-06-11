list = []
import calendar as c
for i in c.day_name:
    i = i.lower()
    list.append(i)
    if 't' in i and 'a' in i:
        print(i)
