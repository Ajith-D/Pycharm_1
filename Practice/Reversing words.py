str = 'This is Ajith Dhanasekaran'
l = str.split()[::-1]
r = []

for char in l:
    r.append(char)
print(' '.join(r))