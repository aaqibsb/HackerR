import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    print(s)
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print(L[:0:-1])
print(L)
print('\n'.join(L[:0:-1]+L))