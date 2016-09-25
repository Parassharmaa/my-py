numbero  = input()

ans = list(map(int, numbero))
ans = sorted(ans)
i=0
while(ans[0]==0):
    if(i==len(ans)-1):
        break
    ans[i]=ans[i+1]
    ans[i+1]=0
    i+=1


for i in ans:
    print(i, end="")
