import random
df = open("sowpods.txt")
x = list(map(str,df.read().split()))
n = len(x)
r = int(input("Enter Number of words:"))
for i in range(r):
	rand = random.randrange(0,n)
	print(str(i+1)+"." + x[rand])

