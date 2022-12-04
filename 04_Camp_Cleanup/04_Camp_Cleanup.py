f = open("input.txt").readlines()

tu=0

for i in f:
    i=i.strip()
    x=(i.split(','))
    felf=x[0].split('-')
    self=x[1].split('-')

    #print(self,felf)

    if int(felf[0])<=int(self[0]):
        if int(felf[1])>=int(self[1]):
            tu+=1
            #print(felf,self)
            continue
    if int(felf[0])>=int(self[0]):
        if int(self[1])>=int(felf[1]):
            #print(felf,self)
            tu+=1


print(tu)

def createarray(st,en):
    ar=[]
    for i in range(int(st),int(en)+1,1):
        ar.append(i)
    return ar

ti=0

for i in f:
    i=i.strip()
    x=(i.split(','))
    felf=x[0].split('-')
    self=x[1].split('-')

    ar1=createarray(felf[0],felf[1])
    ar2=createarray(self[0],self[1])

    tt=set(ar1).intersection(ar2)
    if len(tt)>0:
        ti+=1

print((ti))
