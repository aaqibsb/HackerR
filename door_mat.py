r,col=input().split()
r=int(r)
col=int(col)
a='.|.'
i=(r-1)//2
c=1
ai=1
if col%2!=0 and r%2!=0:
    while c!=i+1:
        print(''.ljust((col-3*ai)//2,'-'),end=a*ai)
        print(''.rjust((col-3*ai)//2,'-'))
        ai+=2
        c+=1
    print('WELCOME'.center(col,'-'))
    while c!=1:
        ai -= 2
        print(''.ljust((col-3*ai)//2,'-'),end=a*ai)
        print(''.rjust((col-3*ai)//2,'-'))
        c-=1


else:
    print("Invalid")