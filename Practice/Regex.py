import re

para = 'Hi, This is Ajith, Hi Iam Studying Python Advanced developer at Atomz research, Iam going for an IT Job'
# To find all words
print(re.findall('Hi', para))

x = re.search('Ajith', para)
print(x.start())

# To substitute
print(re.sub('Ajith', 'Ajith D', para))

# Set of characters
para = 'Hi, This is Ajith, Iam Studying Python Advanced developer at Aatomz research my number is 9876543234'
print(re.findall("[0-9]", para))

# Wildcard
print(re.findall('A...h', para))

# Start with ^
print(re.findall('^Hi', para))

# End with $
print(re.findall('234$', para))

# Zero or more occurrence *
print(re.findall('Hi.*g', para))

# Specified number {}
print(re.findall('A.{3}h', para))

