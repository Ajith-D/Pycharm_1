list = [1, 2, 3, 0, 2, 5, 0, 7, 6]

for i in list:
    if i == 0:
        list.remove(i)
        list.append(i)
print(list)