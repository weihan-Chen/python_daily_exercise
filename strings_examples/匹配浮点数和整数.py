import re
s = '一共20行代码运行时间 13.59s'
pat1 = r'\d+\.?\d+'
pat2 = r'\d+\.\d+|\d+'
r1 = re.findall(pat1, s)
r2 = re.findall(pat2, s)
print(r1)
print(r2)
