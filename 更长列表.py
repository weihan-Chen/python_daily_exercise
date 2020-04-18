def max_length(*lst):
    return max(*lst, key=lambda v: len(v))


if __name__ == '__main__':
    r = max_length([1,2,3],[4,5,6,7],[8])
    print(f'更长的列表是{r}')
