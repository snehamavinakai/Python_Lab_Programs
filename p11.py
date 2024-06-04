import re

pattern_a = r'b[aiu]t'
pattern_b = r'^\w+\s\w+$'
pattern_c= r'^\w+,\s[a-zA-Z]$'

sample_strings = ["bat","bit","but","hat","hut","John Doe","Alice Johnson","Smith, J","Brow, A"]

print("Matching a pattern: ")
for string in sample_strings:
    if re.match(pattern_a,string):
        print(f'Matched {string}')

print("Matching b pattern: ")
for string in sample_strings:
    if re.match(pattern_b,string):
        print(f'Matched {string}')

print("Matching c pattern: ")
for string in sample_strings:
    if re.match(pattern_c,string):
        print(f'Matched {string}')