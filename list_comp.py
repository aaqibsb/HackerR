x = int(input())
y = int(input())
z = int(input())
n = int(input())

l=[[x1,y1,z1] for x1 in range(0,x+1) for y1 in range(0,y+1) for z1 in range(0,z+1) if (x1+y1+z1)!=n]
print(l)