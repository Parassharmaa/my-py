n, k, m = map(int, input().split())
j = 0
jsum = []
for i in range(n):
        jsum.append(j**k)
        j+=1
rsum  = sum(jsum)
r = rsum%m


print(r)
