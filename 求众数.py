def top1(lst):
    return max(lst, default='列表为空', key=lambda v: lst.count(v))


if __name__ == '__main__':
    # 示例
    lst = [1, 3, 3, 2, 1, 1, 2]
    r = top1(lst)
    print(f'{lst}中出现次数最多的元素为：{r}')
