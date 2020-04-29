from random import uniform, gauss
print([(uniform(0, 10), uniform(0, 10)) for _ in range(10)])

x = range(10)
y = [2 * xi + 1 + gauss(0, 1) for xi in x]
points = list(zip(x, y))
print(points)
