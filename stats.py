from collections import Counter
n = int(input())

data = list(map(int, input().split()))

mean = sum(data)/n

data1 = sorted(data)

mid = n/2

if n%2==0:
    median = (data1[int(mid)-1]+data1[int(mid)])/2.0
else:
    median = data1[int(mid+1)]
    
for x, y in sorted(Counter(data).items(), key=lambda x: (-x[1], x[0]))[:1]:
    mode = x
print("%.1f" % mean)
print(median)
print(mode)
