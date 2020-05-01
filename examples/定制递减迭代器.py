'''
@Description:
@Author: weihan-Chen
@Github: https://github.com/weihan-Chen
@Date: 2020-05-01 23:41:28
@LastEditTime: 2020-05-01 23:53:34
'''


# 编写一个迭代器，通过循环语句，实现对某个正整数的依次递减1，直到0.
class Descend():
    def __init__(self, N):
        self.N = N
        self.a = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.a < self.N:
            self.N -= 1
            return self.N
        raise StopIteration


descend_iter = Descend(10)
print(list(descend_iter))
