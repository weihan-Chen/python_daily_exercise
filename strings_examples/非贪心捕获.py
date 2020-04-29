'''
仅添加一个问号(?)，得到结果完全不同，这是非贪心匹配，通过这个例子体会贪心和
非贪心的匹配的不同。
'''
import re
content = '<h>ddedadsad</h><div>graph</div>bb<div>math</div>cc'
pat = re.compile(r'<div>(.*?)</div>')
m = re.findall(pat, content)
print(m)
