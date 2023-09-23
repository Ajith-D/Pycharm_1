import math
num = int(input('Enter: '))

def fac(num):
    product = math.factorial(num)
    return product
print(fac(num))

l = [1, 2, 3, 4, 5, 6]

print(list(map(fac, l)))