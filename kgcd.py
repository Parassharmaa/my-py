from math import gcd

def kgcd(a, b):
    while (a>0 and b>0):
        a-=b
        a,b = b,a
    return a+b


t = int(input())

while(t):
    n = int(input())
    count = 0
    for i in range(1,n+1):
       for j in range(1,n+1): 
            if kgcd(i,j) == gcd(i,j):
                count+=1
        
    print(count)
    t-=1
