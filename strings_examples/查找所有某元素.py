import re
s = '山东省潍坊市青州第1中学高三1班'
pat = '1'
r = re.finditer(pat, s)
for i in r:
    print(i)
