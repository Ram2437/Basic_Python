s = '100 NORTH MAIN ROAD'
print(s.replace('ROAD', 'RD'))

se = '100 NORTH BROAD ROAD'
print(se.replace('ROAD', 'RD'))
r = se[: -4] + se[-4: ].replace('ROAD', 'RDD')
print(r)

# A simple regular expression program
import re
x = re.sub('ROAD$', 'RD.', se)                  # $ represents the end of tbe string
print(x)
print('*******************')

e = '100 BROAD'                                 # Here, i wanted to match only the full string and not the part of it
x = re.sub('ROAD$', 'RD.', e)
print(x)
t = re.sub('\bROAD$','RD', e)
print(t)
t = re.sub(r'\bROAD$','RD', e)                  # r tells Python that nothing in this string should be escaped
print(t)

st = '100 BROAD ROAD APT. 3'
t = re.sub(r'\bROAD\b','RD', st)
print(t)
print('*******************')

pattern = '^M?M?M?$'
re.search(pattern, 'MMM')
# print(pattern)