def score_mean(lst):
    lst.sort()
    lst = lst[1:(len(lst) - 1)]
    return round(sum(lst) / len(lst), 1)


if __name__ == '__main__':
    lst = input('scores:')
    print(score_mean(lst))
