import os


def find_file(work_dir, extension='jpg'):
    lst = []
    for filename in os.listdir(work_dir):
        print(filename)
        splits = os.path.splitext(filename)
        ext = splits[1]
        if ext == '.' + extension:
            lst.append(filename)
    return lst


work_dir = 'D:/chenw/Documents/学习资料/第六学期/音频声学/音频声学笔记/'
extension = 'md'
r = find_file(work_dir, extension)
print(r)
