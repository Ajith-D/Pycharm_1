tamil = ['Ajith', 'Bala', 'kavin', 'Anbu']
english = ['Ben', 'Ajith', 'kavin','sathish']
maths = ['Ajith', 'Anbu', 'pavithra', 'Ben']
science = ['Aravind', 'Ajith', 'Geetha', 'sathish']
social = ['kavin', 'pavithra', 'Ajith', 'Geetha']

sTamil = set(tamil)
sEnglish = set(english)
smaths = set(maths)
sScience = set(science)
sSocial = set(social)

# Union - To merge
print(sTamil.union(smaths, sEnglish))

# Intersection - To find common on the list
print(sTamil.intersection(sSocial, sScience))

# Difference - It will check whether value already there or not
print(sEnglish.difference(smaths))

