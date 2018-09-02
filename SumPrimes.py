def isPrime(n) :
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
    if (n % 2 == 0 or n % 3 == 0) :
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True

def sumprimes(l):
    sum=0
    for i in l:
        check=isPrime(i)
        if(check==True):
            sum+=i;
    return sum

print(sumprimes([-3,1,6]))