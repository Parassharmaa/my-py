import itertools as it
n = int(input())
arr = []
for i in range(1,n+1):
    arr.append(i)
permute = list(it.permutations(arr))
    
c = 0

for i in range(0,len(permute)-1):
    for j in range(0,3):
        if permute[i][j]&permute[i][j+1]==permute[i][j]:
            c+=1
print(c)
