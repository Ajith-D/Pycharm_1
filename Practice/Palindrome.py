l = int(input('Enter: '))
reverse = int(str(l)[::-1])
if l == reverse:
    print('Palindrome')
else:
    print('Not Palindrome')