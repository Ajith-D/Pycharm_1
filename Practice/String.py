colours = ['red', 'blue', 'green']

colours.insert(2, 'white')
print(colours)

word = 'hi this is ajith from pondicherry'
# To Make 1st word capital
print(word.capitalize())

# To make all the first word caps
print(word.title())

#to split the words
print(word.split())

# To join the splitted words
print(''.join(word))

# To cancel the extra spaces
para = '    This is a sentence'
print(para.strip())

# To count the specific word or character
text: str = 'Ajith is a python developer and know to code'
print(text.count('a'))

# To convert a string value to the collection of code
print(text.encode())