t = int(input())
rsum =[]
lsum = []
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    if n==1:
            print("YES")
            break
    for i in range(len(arr)-1):
        rsum.append(sum(arr[i+1:]))
        lsum.append(sum(arr[-(i+1):]))
    st = 0
    for i in range(len(lsum)):
        if(lsum[i]==rsum[i]):
            st = 1
        else:
            continue
    if st==1:
        print("YES")
    else:
        print("NO")
    t-=1


