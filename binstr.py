def rotate(l,n):
    l = l[n:]+l[:n]
    return l

def rrt(l):
    l = rotate(l,1)
    l = list(l)
    return l

def bint(l):
    l = ''.join(l)
    l = int(l,2)
    return l
    
t = int(input())
while(t):
    c = 0
    n = int(input())
    s = list(input())
    st = s
    for i in range(n):
        st = rrt(st)
        if bint(st)%2!=0:
        	c+=1
    print(c)
    t-=1
        
