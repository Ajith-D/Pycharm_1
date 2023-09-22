list = [1, 2, 5, 3, 8, 9, 1, 3, 2, 6]
r = []
for char in list:
    if char not in r:
        r.append(char)

print(r)