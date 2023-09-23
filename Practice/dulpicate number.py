list = [1, 2, 3, 2, 4, 5, 6, 7]
r = []

for i in list:
    if i not in r:
        r.append(i)
print(r)