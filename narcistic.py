p = int(input("Enter power:"))
for i in range(10**(p-1),10**p+1):
    s=0
    j=str(i)
    for k in j:
        k=int(k)
        s+=k**p
    if s==i:
        print(i)
        break
