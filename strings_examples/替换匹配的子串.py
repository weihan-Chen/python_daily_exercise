import re
content = 'hello 12345, hello 456321'
pat = re.compile(r'\d+')
m = pat.sub('666', content)
print(m)
