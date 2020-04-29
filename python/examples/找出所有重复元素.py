'''
@Description:
@Author: weihan-Chen
@Github: https://github.com/weihan-Chen
@Date: 2020-04-29 10:01:41
@LastEditTime: 2020-04-29 10:10:34
'''
from collections import Counter


def find_all_duplicates(lst):
    c = Counter(lst)
    print(c)
    return list(filter(lambda k: c[k] > 1, c))


print(find_all_duplicates([1, 2, 2, 3, 3, 3]))
