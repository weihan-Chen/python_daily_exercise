def search_n(s, c, n):
    size = 0
    for i, x in enumerate(s):
        if x == c:
            size += 1
        if size == n:
            return i
    return i


print(search_n('fdasadfadf', 'a', 3))
print(search_n("fdasadfadf", "a", 30))