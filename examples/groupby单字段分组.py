'''
@Description:groupby 单字段分组
@Author: weihan-Chen
@Github: https://github.com/weihan-Chen
@Date: 2020-04-29 16:15:22
@LastEditTime: 2020-04-29 16:28:41
'''
from itertools import groupby
# 天气记录：
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
# 按照天气字段weather分组汇总：
for k, items in groupby(a, key=lambda x: x['weather']):
    print(k)
# 输出结果看出，分组失败！原因：分组前必须按照分组字段排序，这个很坑~
# 修改代码：
a.sort(key=lambda x: x['weather'])
for k, items in groupby(a, key=lambda x: x['weather']):
    print(k)
    for i in items:
        print(i)
