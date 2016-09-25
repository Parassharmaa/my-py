def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

n = int(input())

c = 0
for i in range(2,3001):
    if isprime(i):
        c+=1
    if c==n:
        print(i)
        break
