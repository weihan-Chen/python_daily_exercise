def filter_false(lst):
    return list(filter(bool, lst))


if __name__ == '__main__':
    # 示例
    r = filter_false([None, 0, False, '', [], 'ok', [1, 2]])
    print(r)
