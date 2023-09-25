# Find top 5 largest numbers
list = [1, 2, 3, 0, 3, 0, 7, 9]

list.sort(reverse=True)

# To print 1st 5 numbers
print(list[:5])

# To print last 5 numbers
print(list[-5:])

# To find the largest number
print(max(list))