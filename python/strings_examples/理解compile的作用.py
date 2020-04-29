import re
pat = re.compile('\W+')  # \W匹配不是数字和字母的字符
has_special_chars = pat.search('ed#2@edc')
if has_special_chars:
    print(f'str contains special characters:{has_special_chars.group(0)}')
