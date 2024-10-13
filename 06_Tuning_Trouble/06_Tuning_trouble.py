f = open("input.txt").readlines()[0]

def find_index(length):
    for i in range(3,len(f)): # iterate over whole message
        history=[]
        for x in range(0,length):
            history.append(f[i-x]) # create array over last "length" message characters
        seen = set()
        uniq = [x for x in history if x not in seen and not seen.add(x)] #remove duplicates
        if len(uniq)==length: # check if length is correct
            return i+1

print("Part one: "+str(find_index(4)))
print("Part one: "+str(find_index(14)))
#1139 is too lowc