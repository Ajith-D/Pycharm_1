name = 'Ajith Dhanasekaran'

print(name[::-1])

#Reversing string without affecting special characters
input = 'abc/de*fg^ij'

# Converting into list
l = list(input)

i = 0
j = len(l)-1

while i<j:
    if not l[i].isalpha():
        i += 1
    elif not l[j].isalpha():
        j -= 1
    else:
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1

out = ''.join(l)
print(out)

colours = ['red', 'blue', 'green']
print(''.join(colours))
