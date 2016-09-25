t = int(input())

while t:
    stringg = input()
    strrev = stringg[::-1]
    c = 1
    for i in range(1,len(stringg)-1):
        if abs(ord(stringg[i])-ord(stringg[i-1])) ==  abs(ord(strrev[i])-ord(strrev[i-1])):
            c+=1
    if int(len(stringg)-1)==c:
        print("Funny")
    else:
        print("Not Funny")
    t-=1
