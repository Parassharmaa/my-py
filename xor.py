import itertools as it

n, nx = map(int, input().split())

a = list(map(int, input().split()))
p = list(set(it.permutations(a,nx)))

px = []

for i in p:
    sumx = sum(i)%10
    px.append(sumx)

print(max(px))

