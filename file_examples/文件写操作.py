# 写入文件信息
# example 1
# w写入，如果文件存在，则清空内容后写入，不存在则创建
f1 = open(r'./daily_exercise/file_examples/test.txt', 'w', encoding='utf-8')
print(f1.write('测试文件写入'))
f1.close

# example 2
# a写入，文件存在，则在文件内容后追加写入，不存在则创建
f2 = open(r'./daily_exercise/file_examples/test.txt', 'a', encoding='utf-8')
print(f2.write('测试文件写入'))
f2.close

# example 3
# with 关键字系统会自动关闭文件和处理异常
with open(r'./daily_exercise/file_examples/test.txt', 'w') as f3:
    print(f3.write('hello world'))
