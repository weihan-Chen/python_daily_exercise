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
# TODO continue this py
