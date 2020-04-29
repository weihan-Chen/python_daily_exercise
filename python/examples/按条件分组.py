def bif_by(lst, f):
    return [[x for x in lst if f(x)], [x for x in lst if not f(x)]]


if __name__ == '__main__':
    records = [25, 89, 31, 34]
    records = bif_by(records, lambda x: x < 80)
    print(records)
