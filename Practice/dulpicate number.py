list = [1, 2, 5, 2, 1, 6, 7, 1, 5, 8, 9, 10, 4]
r = []

for char in list:
    if char not in r:
        r.append(char)
print(r)