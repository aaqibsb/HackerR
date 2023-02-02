n = int(input())
list=[]
def operation(list):
    query=input().split()
    # print(query)
    if 'insert' in query:
         list.insert(int(query[1]),int(query[2]))
    elif 'print' in query:
         print(list)
    elif 'remove' in query:
         list.remove(int(query[1]))
    elif 'append' in query:
         list.append(int(query[1]))
    elif 'sort' in query:
         list.sort()
    elif 'pop' in query:
         list.pop()
    elif 'reverse' in query:
         list.reverse()
    else:
        return "Wrong Input"

for i in range(n):
    operation(list)