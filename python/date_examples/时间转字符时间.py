from time import strftime, localtime
print(localtime())  # 这是输入的时间
print(strftime("%m-%d-%Y %H:%M:%S", localtime()))  # 转化为定制的格式
