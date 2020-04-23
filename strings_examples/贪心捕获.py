'''
(.*)表示捕获任意多个字符，尽可能多的匹配字符
'''
import re
content = '<h>ddedadsad</h><div>graph</div>bb<div>math</div>cc'
pat = re.compile(r'<div>(.*)</div>')
m = re.findall(pat, content)
print(m)
