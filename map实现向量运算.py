lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [3, 4, 5, 6, 3, 2]
lst3 = list(map(lambda x, y: x * y + 1, lst1, lst2))
print(lst3)
