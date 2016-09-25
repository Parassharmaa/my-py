n = int(input())

d = list(map(int, input().split()))
d.sort()
dd = {}
for i in d:
	try:
		dd[i]+=1
	except:
		dd[i]=1

m = max(dd.values())

for i in dd:
    if dd[i]==m:
        r = i
       cod
print(r)
		
