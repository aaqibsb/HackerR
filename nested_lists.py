marksheet = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    marksheet.append([name,score])

print(marksheet)
score=sorted({s[1] for s in marksheet})
print(score)
result=sorted(s[0] for s in marksheet if s[1]==score[1])
print(result)
print("\n".join(result))