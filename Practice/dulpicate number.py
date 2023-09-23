list = [2, 1, 4, 5, 7, 8, 9, 1, 3, 1, 10]
r = []

for i in list:
    if i not in r:
        r.append(i)
print(r)