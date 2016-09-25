n = int(input())

arr = list(map(int, input().split()))
pair = []
for i in range(0,len(arr)):
    for j in range(i):
        pair.append(set([arr[i], arr[j]]))
