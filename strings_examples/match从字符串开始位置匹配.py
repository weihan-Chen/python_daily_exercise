import re
mystr = 'This'
pat = re.compile('hi')
s1 = pat.match(mystr)
s2 = pat.match(mystr, 1)
print(s1)
print(s2)

s3 = pat.search(mystr)
print(s3)
'''
re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，而 re.search 匹配整个字符串，直到找到一个匹配。
'''
