f = open("input.txt").readlines()

playercount=0
playercount2=0
oppos=["A","B","C"]
playerpos=["X","Y","Z"]

## Part one
for i in f:

    ##Part one
    op=oppos.index(i[0])
    pl=playerpos.index(i[2])

    playercount+=pl+1

    if (pl==op):
        playercount+=3
    if (((op+1)%3)==pl):
        playercount+=6


    ##Part two
    if pl==0:
        playercount2+=(op-1)%3+1
    if pl==1:
        playercount2+=3+op+1
    if pl==2:
        playercount2+=6+(op+1)%3+1


print("part one:",playercount)
print("part one:",playercount2)