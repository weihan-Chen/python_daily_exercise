import re
s = 'This module provides regular expression matching operation similar to those found in Perl'
pat = r'\s?([a-zA-Z]+)'
r = re.findall(pat, s)
print(r)
