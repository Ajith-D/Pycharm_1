import re

para = 'Hi, This is Ajith, Iam Studying Python Advanced developer at Atomz research, Iam going for an IT Job'

print(re.findall('Hi', para))

x = re.search('Ajith', para)
print(x.start())

print(re.sub('Ajith', 'D Ajith', para))

# Set of characters
para = 'Hi, This is Ajith, Iam Studying Python Advanced developer at Atomz research my number is 9876543234'
print(re.findall("[0-9]", para))

# Wildcard