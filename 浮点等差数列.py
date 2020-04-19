def rang(start, stop, n):
    start, stop, n = float('%.2f' % start), float('%.2f' % stop), int('%.d' % n)
    step = (stop - start) / n
    lst = [start]
    while n > 0:
        start, n = start + step, n - 1
        lst.append(round((start), 2))
    return lst


if __name__ == '__main__':
    # example
    print(rang(1, 8, 10))
