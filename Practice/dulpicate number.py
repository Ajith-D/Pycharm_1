list = [1, 2, 1, 4, 5, 1, 6, 8, 9, 2, 3, 10]
r = []

for char in list:
    if char not in r:
        r.append(char)
print(r)