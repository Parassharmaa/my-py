x , y = 0,0;

c = input()

for i in c:
	if i=="L":
		x-=1
	elif i=="R":
		x+=1
	elif i=="U":
		y+=1
	else:
		y-=1
print("%d %d" %(x, y))
