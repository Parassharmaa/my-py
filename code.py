t = int(input())

while t:
	n = int(input())
	code = list(map(int, input().split()))
	ans = code[0]
	for i in code:
		ans = gcd(ans,i)
	print(ans)
	t-=1
