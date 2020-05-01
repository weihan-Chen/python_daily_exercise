'''
@Description:
@Author: weihan-Chen
@Github: https://github.com/weihan-Chen
@Date: 2020-05-01 12:53:00
@LastEditTime: 2020-05-01 13:06:29
'''
from math import ceil


def divide_iter(lst, n):
    if n <= 0:
        yield lst
        return
    i, div = 0, ceil(len(lst) / n)
    while i < n:
        yield lst[i * div:(i + 1) * div]
        i = i + 1


print(list(divide_iter([1, 2, 3, 4, 5], 0)))
print(list(divide_iter([1, 2, 3, 4, 5], 2)))
