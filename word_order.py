from collections import Counter
chars=[]
for _ in range(int(input())):
    chars.append(input())

res1=Counter(chars).values()
res2=Counter(chars).keys()
print(len(res2))
for i in res1:
    print(i,end=" ")

# for i in res1:
#     print(res1[i])

'''
sort="".join(chars)

sort=Counter(sort).items()
print(sort)
'''