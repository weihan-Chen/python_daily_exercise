# 读取文本，选出数字

s = open('/tmp/Strings.txt')
words = s.read()
s.close
digits = ''
for word in words:
    if word.isdigit():
        digits += word
print(digits)
