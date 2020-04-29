import os


# 创建文件夹
def mkdir(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)


# 读取文件信息
def openfile(filename):
    f = open(filename)
    fllist = f.read()
    f.close()
    return fllist
