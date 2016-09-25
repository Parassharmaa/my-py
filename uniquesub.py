t = int(input())
while(t):
    n = int(input())
    arr=  list(map(int, input().split()))
    r = 0
    for i in range(0,n):
        for j in range(i+1, n+1):
            if j-i==len(set(arr[i:j])):
            	r+=j-i
    print(r)
    t-=1

