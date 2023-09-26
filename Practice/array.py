import numpy as np

my = np.array([0, 1, 2, 3, 4, 5])
print(my)

# To convert a list to array
list = [1, 4, 7, 9, 11]
a_list = np.array(list)
print(type(a_list))

# To sum two different array
a = np.array([1, 2, 4])
b = np.array([3, 6, 9])
print(a + b)

# Index
print(a[1])
print(b[1])

# creating two dimensional array
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = np.array(l)
print(arr)

# 2D array
arr = np.zeros((5, 3))
print(arr)

# creating array within interval
arr = np.arange(0, 20, 2)
print(arr)

# re-shaping the above arange
print(np.arange(0, 20, 2).reshape(5, 2))

#Creating two arrays
arr1 = np.array([[1,2,3,4], [2,3,7,11]])
arr2 = np.array([[1,3,5,7], [2,4,6,8]])

#Concatenating both arrays
print(np.concatenate((arr1, arr2)))