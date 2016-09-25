t  = int(input())

while(t):
    st, l, u = map(str, input().split())
    l = int(l)
    u = int(u)
	
    sta = [ ord(x) for x in st]
    sta1 = sorted(sta[l:(u+1)], reverse=True)
    sta[l:(u+1)] = sta1
    for ic in sta:
        print(chr(ic), end="")
    print("")                 
    t-=1
	
