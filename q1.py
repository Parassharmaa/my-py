import math

def prime(n):
    if n < 2:
        return False
    for j in range(2,int(math.sqrt(n)) + 1):
        if n%j==0:
            return False
    return True

rg = int(input())
till  = int(input())
p1 = []
pn = []
for i in range(rg):
    if (prime(i) and i>=2):
        p1.append(i)
    else:
        continue
 
l1 = len(p1)
pnnn = {}
for j in range(l1):
    for i in range(till):
        r1 = 2*p1[j]+1
        pn.append(r1)
        for k in range(len(pn)):
            if prime(pn[k]):
                pnnn[p1[j]]= True
            else:
                pnnn[p1[j]] = False
                break
for it in p1:
    if pnnn[it]:
        print(str(it) + " ", end="")
