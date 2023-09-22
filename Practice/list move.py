list = [1, 2, 3, 0, 8, 7, 0, 10]

for item in list:
    if item == 0:
        list.remove(item)
        list.append(item)
print(list
      )