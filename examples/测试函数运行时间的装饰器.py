'''
@Description:
@Author: weihan-Chen
@Github: https://github.com/weihan-Chen
@Date: 2020-05-01 17:10:58
@LastEditTime: 2020-05-01 17:32:33
'''
# 测试函数执行时间的装饰器示例
import time


def timing_func(fn):
    def wrapper():
        start = time.time()
        fn()  # 执行传入的fn参数
        stop = time.time()
        return (stop - start)

    return wrapper


@timing_func
def test_list_append():
    lst = []
    for i in range(0, 100000):
        lst.append(i)


@timing_func
def test_list_compre():
    [i for i in range(0, 100000)]  # 列表生成式


a = test_list_append()
c = test_list_compre()
print("test list append time:", a)
print("test list comprehension time:", c)
print("append/compre:", round(a / c, 4))
