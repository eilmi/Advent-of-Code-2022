f = open("input.txt").readlines()[0]

def find_index(length):
    for i in range(3,len(f)):
        history=[]
        for x in range(0,length):
            history.append(f[i-x])
        seen = set()
        uniq = [x for x in history if x not in seen and not seen.add(x)]
        if len(uniq)==length:
            return i+1

print("Part one: "+str(find_index(4)))
print("Part one: "+str(find_index(14)))
#1139 is too lowc