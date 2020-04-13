from operator import add, sub


def add_or_sub(a, b, operator):
    return (add if operator == '+' else sub)(a, b)


print(add_or_sub(1, 2, '-'))
