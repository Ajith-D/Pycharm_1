def vowels(word):
    vow = ['a', 'e', 'i', 'o', 'u']
    for char in vow:
        if char in word:
            return True
    return False

words = ['Ajith', 'Dry', 'Gym', 'ball']
print(list(filter(vowels, words)))