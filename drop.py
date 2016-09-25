n, D, R = map(int, input().split())

hcount=0

while(n):
    x, y = map(int, input().split())
    if D>=x and D>=y and D>=R:
        hcount+=1
    n-=1
hcount = float(hcount)
print("%.4f" % hcount)
