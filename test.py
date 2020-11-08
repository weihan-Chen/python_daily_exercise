'''
Author: weihan-Chen
Github: https://github.com/weihan-Chen
Date: 2020-10-10 11:23:35
LastEditors: weihan-Chen
LastEditTime: 2020-11-09 00:39:26
Description: 
'''

import math
from matplotlib import pyplot as plt

t_0 = 0
y_0 = 1
tau = 0.1
i = 1
solve = []
Euler = []
t = []
while i < 100:
    if i == 1:
        y_n = y_0
        t_n = t_0
    Euler.append(y_n)
    solve.append(math.exp(t_n))
    t.append(t_n)
    func = y_n
    y_n = y_n + tau * func
    t_n = t_n + tau
    i += 1

plt.plot(t, Euler, c='green', label=' Euler method')
plt.plot(t, solve, c='red', label=' accuracy')
plt.fill_between(t, solve, Euler, facecolor='blue', alpha=0.2)
plt.title('Euler method', fontsize=19)
plt.xlabel('t', fontsize=19)
plt.ylabel('y', fontsize=19)
plt.legend()
plt.show()
