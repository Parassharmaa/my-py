sets, days = map(int, input().split())
stones = list(map(int, input().split()))
while days:
    r1, r2 = map(int, input().split())    
    win=0
    for i in stones[(r1-1):r2]:
        si=i
        while si!=0:
            si = si//2
            win+=1
            
    if win%2==0:
        print("Hacker")
    else:
        print("Mishki")
    days-=1
             
    
						 
