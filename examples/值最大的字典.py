def max_paris(dic):
    if len(dic) == 0:
        return dic
    max_val = max(map(lambda v: v[1], dic.items()))  # get maximum values
    return [item for item in dic.items() if item[1] == max_val]


# example
r = max_paris({'a': -10, 'b': 5, 'c': 3, 'd': 5})
print(r)
