# Filter function
def vowel(word):
    vow = ['a', 'e', 'i', 'o', 'u']
    for char in vow:
        if char in word:
            return True
    return False
print(vowel('Ajith'))

words = ['Ajith', 'Dry', 'gym', 'Ball', 'Zlm']
print(list(filter(vowel, words)))

def div(num):
    if num%2 == 0 and num%3 == 0:
        return True
    return False
print(div(6))

# Map function
def cube(num):
    return num ** 3
print(cube(6))

c = [1, 2, 3, 4, 5, 6]
print(list(map(cube, c)))