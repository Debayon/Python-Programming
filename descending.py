def descending(l):
    i = len(l)
    j = 0
    flag = True
    while(j<i-1):
        if(l[j]<l[j+1]):
            flag = False
            break
        j+=1
    return flag

l = [19,17,18,7]
i = descending(l)
print(i)