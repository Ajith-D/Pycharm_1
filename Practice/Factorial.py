import math
def fact(num):
    f = math.factorial(num)
    return f
print(fact(6))

l = [1, 2, 3, 4, 5, 6, 4, 7, 8, 1, 9, 2]
print(list(map(fact, l)))

for i in range(1, 11):
    product = math.factorial(i)
    print(product)