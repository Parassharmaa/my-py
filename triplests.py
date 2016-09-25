trip1 = list(map(int, input().split()))
trip2 = list(map(int, input().split()))
alice = 0
bob = 0
for i in range(len(trip1)):
    if trip1[i]<trip2[i]:
        bob+=1
    elif trip1[i]>trip2[i]:
        alice+=1
        
print(str(alice)+" " + str(bob))
