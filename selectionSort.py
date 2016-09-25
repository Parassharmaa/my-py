n, x  = map(int, input().split())

arr = list(map(int, input().split()))
temp = 0

for i in range(n-1):
	if(i+1==x):
		break
	mins = i
	for j in range(i+1,n):
		if(arr[mins]>arr[j]):
			temp = arr[j]
			arr[j] = arr[mins]
			arr[mins] = temp
for ele in arr:
	print(ele, end=" ")
			
