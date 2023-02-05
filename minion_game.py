string=input()
vowels="AEIOU"
stuart=0
kevin=0

for i in range(len(string)):
    if string[i] in vowels:
        kevin+=len(string)-i
    else:
        stuart+=len(string)-i

if kevin>stuart:
    print("Kevin "+str(kevin))
elif kevin<stuart:
    print("Stuart " + str(stuart))
else:
    print("Draw")