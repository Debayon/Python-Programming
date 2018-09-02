def valley(l):
    list_len = len(l)
    i=0
    flag = True
    while(i<list_len-1):
        if(l[i]<=l[i+1]):
            if(i<1):
                flag = False
            elif(l[i]==l[i+1]):
                flag = False
            break
        i+=1
    j = i
    if(flag == True):
        while (j < list_len - 1):
            if(l[j]>=l[j+1]):
                flag = False
                break
            j+=1
        if(j-i+1 < 2):
            flag = False

    return flag

l=[3,3,2,1,2]
i = valley(l)
print(i)