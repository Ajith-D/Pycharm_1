list = [1, 2, 3, 4, 5, 6, 4, 7, 8, 1, 9, 2]
r = []

for char in list:
    if char not in r:
        r.append(char)
print(r)

num = int(input('Enter: '))

