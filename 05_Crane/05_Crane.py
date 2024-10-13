import numpy as np



f = open("input.txt").readlines()

last_line_of_mountain=0
column=[]
for index,line in enumerate(f):
    if line.strip()[0]=="1":
        last_line_of_mountain=index
        break
    row=[]
    for char in line:
        row.append(char)
    column.append(row)
    pass

matrix = np.char.strip(np.array(column))

new_grid=[]

for i in range(1,len(row),4):
    new_array = np.delete(matrix[:,i], np.where(matrix[:,i] == ""))
    new_grid.append(new_array   )


#print(new_grid)

part_one_grid=new_grid.copy()
for command in f[last_line_of_mountain+2:]:
    #print(command)
    tmp = (command.strip()).split(" ")

    nr_of_cranes= int(tmp[1])
    src = int(tmp[3])-1
    dst = int(tmp[5])-1

    part_one_grid[dst] = np.insert(part_one_grid[dst],0,np.flip(part_one_grid[src][0:nr_of_cranes]))
    part_one_grid[src] = part_one_grid[src][nr_of_cranes:]

    #print(new_grid)

st=""
for i in part_one_grid:
    st+=i[0]

print("Part one: "+st)



### exactly the same without flipping the array ###
part_two_grid=new_grid.copy()

for command in f[last_line_of_mountain+2:]:
    #print(command)
    tmp = (command.strip()).split(" ")

    nr_of_cranes= int(tmp[1])
    src = int(tmp[3])-1
    dst = int(tmp[5])-1

    part_two_grid[dst] = np.insert(part_two_grid[dst],0,part_two_grid[src][0:nr_of_cranes])
    part_two_grid[src] = part_two_grid[src][nr_of_cranes:]



st=""
for i in part_two_grid:
    st+=i[0]

print("Part two: "+st)