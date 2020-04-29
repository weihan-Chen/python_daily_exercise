'''
@Description:Counter 对象间可以做数学运算
@Author: weihan-Chen
@Github: https://github.com/weihan-Chen
@Date: 2020-04-29 14:59:45
@LastEditTime: 2020-04-29 16:05:14
'''
from collections import Counter
a = ['apple', 'orange', 'computer', 'orange']
b = ['computer', 'orange']

ca = Counter(a)
cb = Counter(b)
print(ca + cb)


# 进一步抽象，实现多个列表内元素的个数统计
def sumc(*c):
    if len(c) < 1:
        return
    mapc = map(Counter, c)
    s = Counter([])
    for ic in mapc:
        s += ic
    return s


print(sumc((a, b, ['abc'], ['face', 'computer'])))
