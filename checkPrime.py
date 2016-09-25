print("Input Range:")

r1, r2 = map(int, input().split())

c = 0
for i in range(r1, r2):
    if i > 1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            c+=1
print("There are %d prime number betweeen %d and %d" % (c, r1, r2))
