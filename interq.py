n  = int(input())

data  = list(map(int, input().split()))
freq = list(map(int, input().split()))
dataSet = [str(data[i]).split()* freq[i] for i in range(len(freq))]
dataSet = sum(dataSet,[])
dataSet = [int(i) for i in dataSet]
data = dataSet

data = sorted(data)
n = len(data)
if(n%2==0):
    median = (data[int(n/2)-1]+data[int(n/2)])/2
    lr = data[:int(n/2)]
    n1 = len(lr)
    ur = data[-int(n-n/2):]
    n2 = len(ur)
else:
    median = data[int(n/2)]
    lr = data[:int(n/2)]
    n1 = len(lr)
    ur = data[-int(n-n/2):]
    n2 = len(ur)

if n1%2==0:
    q1 = (lr[int(n1/2)-1]+lr[int(n1/2)])/2
else:
    q1 = lr[int(n1/2)]
if n2%2==0:
    q3 = (ur[int(n2/2)-1]+ur[int(n2/2)])/2
else:
    q3 = ur[int(n2/2)]

iqr =round(float(q3-q1)c,1)

print(iqr)
