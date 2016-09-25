import math

n, k  = map(int, input().split())

ways = 1

if (k<n):
	t= math.factorial(n)/(math.factorial(k)*math.factorial(n-k))


ways+=t
print(int(ways))
