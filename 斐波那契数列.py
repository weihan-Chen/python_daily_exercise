# 生成斐波那契数列

import numpy

N = 20
a = numpy.zeros((N, 1))
a[0] = a[1] = 1
for num in range(2, N):
    a[num] = a[num - 2] + a[num - 1]
    print(a[num], end='')
