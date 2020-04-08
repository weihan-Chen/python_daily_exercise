N = 100
primes = []
for number in range(2, N + 1):
    count = 0
    for divisor in range(number - 1, 1, -1):
        if number % divisor == 0:
            count += 1
    if count == 0:
        primes.append(number)
print(primes)
