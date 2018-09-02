def matched(s):
    stack=[]
    sp=0 #stack_pointer
    count=0
    for i in s:
        if(i==')' and count==0):
            return False
        elif(i=='('):
            #stack.insert(sp,)
            count+=1
        elif(i==')'):
            count-=1
    if(count==0):
        return True
    else:
        return False

i=matched("zb%78")
print(i)

