arr = list(map(int, input().split()))
n = len(arr)
temp = 0
c=0
for i in range(n-1):
	for j in range(n-1-i):
		if(arr[j]>arr[j+1]):
			temp = arr[j]
			arr[j]=arr[j+1]
			arr[j+1] = temp
			c+=1
			

print("Swaps:" + str(c))
print("Sorted Array:" ,end=" ")
for ele in arr:
    print(ele, end=" ")
