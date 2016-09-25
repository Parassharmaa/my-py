t = int(input())

while(t):
    s = list(input())
    s = [ord(x) for x in s]
    sn = []
    for i in range(len(s)-1):
        if(abs(s[i]-s[i+1])==25):
            sn.append(1)
        else:
            sn.append(abs(s[i]-s[i+1]))
    if(set(sn)=={1}):
        print("YES")
    else:
        print("NO")
    t-=1
