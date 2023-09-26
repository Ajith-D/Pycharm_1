import math
num = int(input('Enter: '))

def fact(num):
    product = math.factorial(num)
    return product
print(fact(num))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(fact, l)))


for i in range(1, 11):
    product = math.factorial(i)
    print(product)