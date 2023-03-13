
for i in range(int(input())):
    string=input()
    state=True
    upper_count = 0
    number_count = 0

    if len(string)!=10:
        print('Invalid')
        state=False
        continue


    for word in string:
        # print(word)
        if word.isupper(): upper_count+=1
        if not word.isalnum():
            # print("Invalid")
            state=False
            break
        if word.isdigit(): number_count+=1
        if string.count(word)>1:
            # print("Invalid")
            state=False
            break
        if state==False: break
    # print(number_count)
    if i+1==68:
        print(upper_count, number_count)
    if upper_count>=2 and number_count>=3 and state==True:
        print(i+1, "Valid")
    else:
        print(i+1, "Invalid")



