import itertools


def primes():
    num = 1
    while True:
        num += 1
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            yield num


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
