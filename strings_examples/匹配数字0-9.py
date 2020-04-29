import re
s = '一共20行代码运行时间13.59s'
pat = r'\d+'  # +表示匹配数字
r = re.findall(pat, s)
print(r)
