marksheet=[]
for _ in range(int(input())):
    name=str(input())
    score=float(input())
    marksheet.append([name,score])
second_highest=sorted(list(set([score for name,score in marksheet])))[1]
print(second_highest)
res="\n".join(sorted(a for a,b in marksheet if b==second_highest))
print(res)