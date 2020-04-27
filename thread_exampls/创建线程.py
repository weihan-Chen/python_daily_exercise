import threading
# 创建一个名称为my_thread 的线程：
my_thread = threading.Thread(name='my_thread')


# 创建线程的目的是告诉它帮助我们做些什么，做些什么通过参数target 传入，参数类型为callable，函数就是可调用的：
def print_i(i):
    print('print i:%d' % i)


my_thread = threading.Thread(target=print_i, args=(1, ))

# my_thread 线程已经全副武装，但是我们得按下发射按钮，启动start()，它才开始真正起飞。
my_thread.start()
