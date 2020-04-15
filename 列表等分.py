from math import ceil


def divide(lst, size):
    if size <= 0:
        return lst
    return[
        lst[i * size:(i + 1) * size] for i in range(0, ceil(len(lst) / size))
    ]


if __name__ == '__main__':
    lst = list(input('list:'))
    size = int(input('size:'))
    lst = divide(lst, size)
    print(lst)
