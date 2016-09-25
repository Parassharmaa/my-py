import math


def checkPrime(p):
    if p < 2:
        return False
    for j in range(2,int(math.sqrt(p)) + 1):
        if p%j==0:
            return False
    return True
t = int(input())
mlist = []
while(t):
        n = int(input())
        nlist = list(map(int,input().split()))
        nlist = nlist[:n]
        plist = [i for i in nlist if checkPrime(i)]
        for i in range(len(plist)):
            for j in range(len(plist)):
                mlist.append(plist[i]*plist[j])
        if len(plist)==0:
            print(-1)
        else:
            print(max(mlist))
        t-=1
