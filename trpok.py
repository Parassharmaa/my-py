n = int(input())

arr = list(map(int, input().split()))

dist = len(list(set(arr)))

subArray = []

for i in range(len(arr)):
    j=0
    while j!=len(arr):
        subArray.append(arr[i:i+j])
        j+=1
c=0    
for d in range(len(subArray)):
    if dist  == len(list(set(subArray[d]))):
                   c+=1

print(c)
