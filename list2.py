l=[]
for _ in range(int(input())):
    query=input().split()
    if query[0]=="pop" or query[0]=="sort" or query[0]=="reverse":
        eval("l."+query[0]+"()")
    elif query[0]=="insert":
        # print("none")
        eval("l." + query[0] + "(int(query[1]),int(query[2]))")
    elif query[0]=="append" or query[0]=="remove":
        eval("l." + query[0] + "(int(query[1]))")
    else:
        print(l)
