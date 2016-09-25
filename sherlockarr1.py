t = int(input())
while t>0:
    flag=0
    sm=0
    left=0
    n = int(input())
    lis = list(map(int,input().split(' ')))
    sm = sum(lis)
    for i in range(n):
        sm = sm - lis[i]

        if left==sm:
            flag=1
            break
        left = left + lis[i]
    if flag:
        print("YES")
    else:
        print("NO")
    t-=1
