import re
n = int(input())
number = []
for _ in range(n):
    number.append(input())
print(number)

for i in number:
    match = re.search(r'^[789]\d{9}$',i)
    if match:
        print("YES")
    else:
        print("NO")

