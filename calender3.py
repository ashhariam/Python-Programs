list = []
import calendar as c
for i in c.day_abbr:
    list.append(i[-3::1])
    print(list)