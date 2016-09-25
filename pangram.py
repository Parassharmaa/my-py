def checkPan(s):
    alphaT= sum([i for i in range(97,123)]) + 32 
    s = [i.lower() for i in s]
    s = list(set(s))
    sn = sum([ord(i) for i in s])
    if sn==alphaT:
        return("pangram")
    else:
        return("not pangram")

print(checkPan("hdkahkey"))
