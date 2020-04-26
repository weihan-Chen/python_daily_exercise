from time import strptime

struct_time = strptime('2019-12-22 10:10:08', "%Y-%m-%d %H:%M:%S")
print(struct_time)  # struct_time 类型就是time 中的一个类
