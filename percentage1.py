l=[]
dict={}
for _ in range(int(input())):
    l=input().split()
    dict.update({l[0]:list(map(float,(l[1:])))})
query=input()
if query in dict:
    print("{:.2f}".format(sum(dict[query])/len(dict[query])))

