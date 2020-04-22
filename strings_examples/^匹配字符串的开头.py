import re
s = 'This module provides regular expression matching operations similar to those found in Prel'
pat = r'^[emrt]'
r = re.findall(pat, s)
print(r)
