n = int(input())
a = list(map(int, input().split()))
imin = {}
imax = {}
 
for i in range(n):
  if not a[i] in imin:
    imin[a[i]] = i
  imax[a[i]] = i
 
v = list(imax.values())
v.sort()
l = len(v)
 
def cnt(l, v, m):
  i = 0
  k = l-1
  if v[i] > m:
    return l
  if v[k] <= m:
    return 0
  while k - i > 1:
    next = (i + k)//2
    if v[next] > m:
      k = next
    else:
      i = next
  return l-k
  
count = 0
for i in imin:
  m = imin[i]
  count += cnt(l, v, m)
print(count)  
      

