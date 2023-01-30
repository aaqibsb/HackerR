import re

l=[]
for _ in range(int(input())):
    num=input()
    pattern=re.search(r'^(?!.*(\d)(-?\1){3})[456][0-9]{3}.?[0-9]{4}.?[0-9]{4}.?[0-9]{4}$',num)
    # matches=pattern.finditer(num)
    if pattern:
        l.append("Valid")
    else:
        l.append("Invalid")

print('\n'.join(l))
    # for match in matches:
    # print(pattern)
