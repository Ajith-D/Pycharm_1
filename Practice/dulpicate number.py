list = [1, 2, 3, 4, 5, 6, 4, 7, 8, 1, 9, 2]
r = []

for i in list:
    if i not in r:
        r.append(i)
print(r)