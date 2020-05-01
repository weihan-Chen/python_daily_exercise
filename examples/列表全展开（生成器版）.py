'''
@Description:
@Author: weihan-Chen
@Github: https://github.com/weihan-Chen
@Date: 2020-05-01 17:02:59
@LastEditTime: 2020-05-01 17:09:26
'''
# 多层列表展开成单层列表
a = [1, 2, [3, 4, [5, 6], 7], 8, ["python", 6], 9]


def expand(lst):
    for i in lst:
        if type(i) == list:
            yield from expand(i)
        else:
            yield i


print(list(expand(a)))
