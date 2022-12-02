f = open("input.txt").readlines()

caloriesperelf=[]
t=0
for i in f:
    i=i.strip()
    if i=="":
        caloriesperelf.append(t)
        t=0
        continue
    t=t+int(i)

print("Part one:",max(caloriesperelf))


caloriesperelf.sort(reverse=True)
print("Part two:",sum(caloriesperelf[0:3]))
    
