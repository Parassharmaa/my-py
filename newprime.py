n = int(input())
s = list(map(int, input().split()))
r = []

for i in s:
	count = 0
	for j in s:
		if i%j==0:
			count+=1
	if(count==1):
		r.append(i)
for i in r:
    print(i, end=' ')
