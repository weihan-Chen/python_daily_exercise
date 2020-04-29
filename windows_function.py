'''
@Description:
@Author: weihan-Chen
@Github: https://github.com/weihan-Chen
@Date: 2020-04-14 01:25:49
@LastEditTime: 2020-04-26 14:41:36
'''

# 窗函数
import numpy as np
# import scipy.signal as sp
import matplotlib.pyplot as plt

nuttall_min3_coeff = np.array([0.4243801, 0.4973406, 0.0782793],
                              dtype=np.float32)


def nuttall(M, coeff, sym):
    if M < 1:
        return np.array([], dtype=np.float32)
    if M == 1:
        return np.ones(1, dtype=np.float32)
    odd = bool(M % 2)
    if not sym and not odd:
        M = M + 1
    n = np.arange(0, M)
    sign_list = [-1.0, 1.0]
    w = coeff[0]
    for (i, x) in enumerate(coeff[1:]):
        sign = sign_list[i % 2]
        w += sign * x * np.cos((i + 1) * 2.0 * np.pi * n / (M - 1))
    if not sym and not odd:
        w = w[:-1]
    return w


def test_window(x):
    (n, ) = x.shape
    log_magn = np.log(np.abs(np.fft.rfft(x, n=n * 1000)) * 2 / n + 1e-8)
    plt.subplot(1, 2, 1)
    plt.title("Window")
    plt.plot(x)
    plt.subplot(1, 2, 2)
    plt.title("Window Lobes")
    plt.plot(np.arange(n * 1000 // 2 + 1) / 1000, log_magn)
    plt.show()


test_window(nuttall(100, nuttall_min3_coeff, sym=True))
