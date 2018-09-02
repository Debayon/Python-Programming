def intreverse(n):
    rn = 0
    i=0
    while(n>0):
        rn = rn*10 + n%10
        i=i+1
        n=int(n/10)
    return rn

print(intreverse(1010))
