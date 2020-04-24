'''
批量修改文件后缀
本例子使用Python 的os 模块和argparse 模块，将工作目录work_dir 下所
有后缀名为old_ext 的文件修改为后缀名为new_ext
通过本例子，大家将会大概清楚argparse 模块的主要用法。
'''
import argparse
import os


# 定义脚本参数
def get_parser():
    parser = argparse.ArgumentParser(description='工作目录中文件后缀名修改')
    parser.add_argument('work_dir',
                        metavar='WORK_DIR',
                        type=str,
                        nargs=1,
                        help='修改后缀名后的文件目录')
    parser.add_argument('old_ext',
                        metavar='OLD_EXT',
                        type=str,
                        nargs=1,
                        help='原来的后缀')
    parser.add_argument('new_ext',
                        metavar='NEW_EXT',
                        type=str,
                        nargs=1,
                        help='新的后缀')
    return parser


# 后缀名批量修改
def batch_rename(work_dir, old_ext, new_ext):
    '''
    传递当前目录，原来的后缀名，新的后缀名后，批量重命名后缀名
    '''
    for filename in os.listdir(work_dir):
        # 获取得到文件后缀
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        # 定位后缀名为 old_ext 的文件
        if old_ext == file_ext:
            # 修改后文件的完整名称
            newfile = split_file[0] + new_ext
            # 实现重命名操作
            os.rename(os.path.join(work_dir, filename),
                      os.path.join(work_dir, newfile))
    print('rename completed!')
    print(os.listdir(work_dir))


# 实现 main
def main():
    # 命令行参数
    parser = get_parser()
    args = vars(parser.parse_args())
    # 从命令行参数中依次解析出参数
    work_dir = args['work_dir'][0]
    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = '.' + old_ext
    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext
    batch_rename(work_dir, old_ext, new_ext)


if __name__ == '__name__':
    main()
