import re
s = 'That'
pat = r't'
r = re.findall(pat, s, re.I)
print(r)
