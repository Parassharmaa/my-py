def mul(s):
	l = len(s)
	for i in range(2, l):
		if l%i==0:
			return(i)
			break
	else:
		return 1
			
s = input("Input String:")
n = mul(s)
sd = []
for i in range(0,len(s), n):
	sd.append(s[i:i+n])
sd.sort()
for i in sd:
	print(i)

