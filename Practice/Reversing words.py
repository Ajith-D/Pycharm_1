str = 'This is Ajith Dhanasekaran'
l = str.split()[::-1]
out = []

for i in l:
    if i not in out:
        out.append(i)
print(' '.join(out))