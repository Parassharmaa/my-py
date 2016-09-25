from math import sqrt
n = int(input())
data = list(map(int, input().split()))

mean = sum(data)/n

print(round(sqrt(sum([(x-mean)**2 for x in data])/n),1))
