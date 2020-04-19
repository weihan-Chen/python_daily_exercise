# 返回字典d前n个最大值对应的键
from heapq import nlargest


def topn_dict(d, n):
    return nlargest(n, d, key=lambda k: d[k])


# example
print(topn_dict({'a': 10, 'b': 8, 'c': 9, 'd': 10}, 3))
