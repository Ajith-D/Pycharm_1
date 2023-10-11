import math

def fac(num):
    product = math.factorial(num)
    return product
print(fac(6))

l = [1, 2, 3, 4, 5, 6, 4, 7, 8, 1, 9, 2]
print(list(map(fac, l)))

for i in range(0, 11):
    product = math.factorial(i)
    print(product)