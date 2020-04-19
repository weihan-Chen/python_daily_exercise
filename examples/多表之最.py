def max_lists(*lst):
    return max(max(*lst, key=lambda v: max(v)))


if __name__ == '__main__':
    r = max_lists([1, 2, 3], [6, 7, 8], [4, 5])
    print(r)
