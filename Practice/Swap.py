# Swap means interchanging the value
x = 22
y = 33
x, y = y, x
print('x=', x)
print('y=', y)

# Swapping first and last elements

l = [1, 2, 3, 4, 5, 6]

l[0], l[-1] = l[-1], l[0]
print(l)

l[0], l[2] = l[2], l[0]
print(l)