import time
j=[]
t1 = time.time() 
for i in range(100000000):
    j.append(i)    
t2 = time.time()
print("Time taken: "+str(t2-t1)+"s")

