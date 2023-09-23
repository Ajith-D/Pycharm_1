import math


def fact(num):
    factorial = math.factorial(num)
    return factorial


print(fact(1))

l = [10, 3, 4, 5, 6, 7]

print(list(map(fact, l)))
