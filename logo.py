from collections import Counter

string=Counter(input())
print(string)
res=list(sorted(list(string.items()),key=lambda c: (-c[1],c[0])))
print(res)
for char,count in res[:3]:
    print(char, count)
