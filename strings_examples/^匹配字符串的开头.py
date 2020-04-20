import re
s = 'This module provides regular expression matching operations similar to those found in Prel'
pat = r'^[emrt]'  # TODO 弄明白正则表达式
r = re.findall(pat, s)
print(r)
