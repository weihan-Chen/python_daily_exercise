from itertools import chain
a = [1, 3, 5, 6]
b = [2, 4, 6]
for i in chain(a, b):
    print(i)
