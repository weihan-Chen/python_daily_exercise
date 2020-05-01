'''
@Description:
@Author: weihan-Chen
@Github: https://github.com/weihan-Chen
@Date: 2020-04-30 23:19:52
@LastEditTime: 2020-04-30 23:41:26
'''
# 注意到sort 和groupby 所用的key 函数，除了lambda 写法外，还有一种简写，就是使用itemgetter：
from operator import itemgetter
from itertools import groupby
a = [{
    'date': '2019-12-15',
    'weather': 'cloud'
}, {
    'date': '2019-12-13',
    'weather': 'sunny'
}, {
    'date': '2019-12-14',
    'weather': 'cloud'
}]
a.sort(key=itemgetter("weather"))
for k, items in groupby(a, key=itemgetter("weather")):
    print(k)
    for i in items:
        print(i)
# itemgetter 是一个类，itemgetter('weather') 返回一个可调用的对象，它的参数可有多个：
a.sort(key=itemgetter("weather", "date"))
for k, items in groupby(a, key=itemgetter("weather")):
    print(k)
    for i in items:
        print(i)
