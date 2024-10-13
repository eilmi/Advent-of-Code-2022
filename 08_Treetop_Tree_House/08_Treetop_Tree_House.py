import numpy as np

f = open("input.txt").readlines() #importing input text file

grid=[]
for lines in f: # creating array of array
    row=[]  
    for number in lines.strip():
        row.append(number) # appending height of tree to row

    grid.append(row) # append the whole row to the grid of trees

a= np.array(grid) # converting into numpy array
xdim,ydim=a.shape # getting dimensions of the forest

tree_counter=0 #keeps track of trees found to be visable

for x in range(1,xdim-1): # running for every tree inside the forest (exluding first and last row and column)
    for y in range(1,ydim-1):

        topmax=int(max(a[x,0:y])) #get height of biggest tree looking at the top
        bottommax=int(max(a[x,y+1:])) #get height of biggest tree looking at the bottom
        leftmax=int(max(a[0:x,y]))
        rightmax=int(max(a[x+1:,y]))

        height = int(a[x][y]) #get height of current tree
        if (height>topmax or height>bottommax or height > leftmax or height > rightmax):
            #print("seeable tree found")
            tree_counter+=1 

tree_counter+=2*xdim+2*(ydim-2) # add outer rows and columns (where all trees are visable)

print("Part one: "+str(tree_counter))

### Part two ###

def calc_viewing_dist(val,array):
    result = 1
    for line_of_sight in array: # run for all 4 directions
        view_dist=0
        for tree_height in line_of_sight: #iterate over all trees in current direction
            view_dist+=1
            if tree_height>=val: # if tree is too high limit of viewing distance in this direction is reached
                break
        result*=view_dist # calculate the score

    return result

best_score=0

for x in range(1,xdim-1):
    for y in range(1,ydim-1):
        # flipping is needed on top and left list because you are looking against the natural list order
        best_score=max(calc_viewing_dist(a[x,y],[np.flip(a[x,0:y]),a[x,y+1:],np.flip(a[0:x,y]),a[x+1:,y]]),best_score)

print("Part two: "+str(best_score))
