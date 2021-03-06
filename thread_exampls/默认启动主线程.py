'''
@Description:
@Author: weihan-Chen
@Github: https://github.com/weihan-Chen
@Date: 2020-04-26 23:45:40
@LastEditTime: 2020-04-28 01:46:32
'''
import threading

# threading 的类方法current_thread() 返回当前线程：
t = threading.current_thread()
print(t)
# 所以，验证了程序默认是在MainThread 中执行。
# t.getName() 获得这个线程的名字，其他常用方法，ident() 获得线程id, is_alive() 判断线程是否存活等。
print(t.getName())
print(t.ident)
print(t.is_alive())
