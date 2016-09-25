import math
n = int(input())
data = list(map(int, input().split()))
weight = list(map(int, input().split()))
wm = list(zip(data, weight))
wmp = []
for i in range(len(wm)):
	wmp.append(wm[i][0]*wm[i][1])
wmean  = sum(wmp)/sum(weight)

print(round(wmean,1))
