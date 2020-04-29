from random import randint, sample
lst = [randint(0, 50) for _ in range(100)]
print(lst[:5])
lst_example = sample(lst, 10)
print(lst_example)
