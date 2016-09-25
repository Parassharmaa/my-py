import itertools as it

s = list(input())

def up(t):
    r = []
    for i in range(65, ord(t)+1):
        r.append(chr(i))
    return(r)
def low(t):
    r = []
    for i in range(97, ord(t)+1):
        r.append(chr(i))
    return(r)
        
def num(t):
    r = []
    for i in range(0,int(t)+1):
        r.append(str(i))
    return(r)

for i in range(len(s)):
    if s[i].isupper():
        s[i] = up(s[i])
    elif s[i].islower():
        s[i] = low(s[i])
    elif s[i].isdecimal():
        s[i] = num(s[i])

s = it.chain.from_iterable(s)

print(''.join(s))

