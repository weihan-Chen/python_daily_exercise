import re
s = 'This module provides regular expression matching operation similar to those found in Perl'
pat = r'\s+'
r = re.split(pat, s)
print(r)

# 或者
r2 = s.split(' ')
print(r2)

# 对于split不行的情况，用正则
s = 'This,,,   module ; \t   provides || regular ; '
words = re.split(r'[,\s;|]+', s)
words = [i for i in words if len(i) > 0]
print(words)
