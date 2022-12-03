f = open("input.txt").readlines()

su=0

def getprio(c):
    if c.islower():
        return ord(c)-96
    else:
        return ord(c)-64+26


## Part one
for i in f:
    i=i.strip()
    l=int(len(i)/2)
    fh=i[0:l]
    sh=i[l:]

    for x in fh:
        if x in sh:
            su+=getprio(x)
            break

print("part one:",su)

## Part two
su=0
for i in range (0,len(f),3):
    x=f[i:i+3]
    for t in x[0].strip():
        if t in x[1] and t in x[2]:
            su+=getprio(t)
            break

print("part two:",su)