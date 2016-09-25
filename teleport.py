n = int(input())

arr = list(map(int, input().split()))

s, e = map(int, input().split())

if arr[s]<=len(arr):
    print("YES")
else:
    print("NO")
