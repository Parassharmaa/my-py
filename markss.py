
n, x = map(int, input().split())
ms = []
for _ in range(x):
    ms.append(list(map(float, input().split())))

nms = list(zip(*ms))

avg   = []

for i in range(len(nms)):
    avg.append(sum(nms[i])/x)
for r in avg:
    print("%.1f" %r)
