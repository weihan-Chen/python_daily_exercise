import re
s = 'i love python very much'
pat = 'python'
r = re.search(pat, s)
print(r.span())
