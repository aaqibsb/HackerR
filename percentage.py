n = int(input())
student_marks = {}
for _ in range(n):
    line = input().split()
    name, scores = line[0], line[1:]
    scores = list(map(float, scores))
    student_marks[name] = scores
# print(line)

query_name=input()
for i in student_marks:
    if i==query_name:
        average=sum(student_marks[i])/len(student_marks[i])
print("{:.2f}".format(average))

