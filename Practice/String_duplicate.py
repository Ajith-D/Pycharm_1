str = "geeksforgeeks"
p = " "

for char in str:
    if char not in p:
        p = p + char
print(p)
