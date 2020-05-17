import re
total=0
for x in re.findall('[0-9]+',(open('texto12.01.txt')).read()):
    total=total+int(x)
print(total)


import re
print(sum([int(x) for x in re.findall('[0-9]+',(open('texto12.01.txt')).read())]))
