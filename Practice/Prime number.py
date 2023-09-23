l = int(input('Enter: '))
h = int(input('Enter: '))

for i in range(l , h + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)