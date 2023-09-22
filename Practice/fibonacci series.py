num  = int(input('Enter: '))
a = 0
b = 1
s = 0

for x in range(num):
    print(s, end=" ")
    s = a + b
    b = a
    a = s