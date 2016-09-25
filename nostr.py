n = int(input())
s = list(input())
t = 1154
sum = 0
for i in s:
        sum+=ord(i.lower())
i=1
while i>0:
        if sum<t:
                i=0
                break
        elif sum/i==t or sum/i>t and sum/i<t*2:
                break        

        i+=1
print(i)
