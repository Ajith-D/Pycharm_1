def vowel(word):
    vow = ['a', 'e', 'i', 'o', 'u']
    for char in vow:
        if char in word:
            return True
    return False
print(vowel('Ajith'))


def div(num):
    if num%2 == 0 and num%3 == 0:
        return True
    return False
print(div(6))
