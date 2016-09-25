t = int(input())


def flip(n):
    n = list(str(n))
    i = 0
    j = len(n)-1

    while(i<=j):
        n[i], n[j] = n[j], n[i]
        i+=1
        j-=1
    n = int(''.join(n))
    return n
        
while(t):
    n1, n2  = map(int, input().split())
    r = flip(flip(n1)+flip(n2))
    print(r)
    t-=1
