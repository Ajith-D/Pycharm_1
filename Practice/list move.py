list = [1, 2, 3, 0, 3, 0, 7, 9]

for i in list:
    if i == 0:
        list.remove(i)
        list.append(i)

print(list)