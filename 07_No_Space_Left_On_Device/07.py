f = open("input.txt").readlines()
folder_size=0
directory_tree=[]
folderpath=""

# 
for line in f:
    if line.startswith('$'): #is command
        if line.startswith("$ cd"):
            directory_tree.append([folderpath,folder_size])
            folder_size=0
            argument = line.split("$ cd")[1].strip()
            if argument.startswith('/'): #absolute cd
                folderpath=argument
            elif argument=="..": #go to parent folder
                #print(folderpath.rsplit("/",2))
                folderpath=str(folderpath.rsplit("/",2)[0])+"/"
            else: # relative cd
                folderpath+=argument+"/"
            #print("changing to: "+folderpath)
    
    else: #is not command -> must be output of ls command
        ft = line.split(" ")[0] # split at spaces to get filesize
        if (ft.isnumeric()): # ignore dirs in ls command
            #print("File size is:"+str(ft))
            folder_size+=int(ft)
            pass

directory_tree.append([folderpath,folder_size]) # add last searched directory tree

## remove duplicates ##

new_dir_tree=[]
already_searched_dirs=[]
for x in directory_tree:
    if x[0] in already_searched_dirs:
        continue
    else:
        already_searched_dirs.append(x[0])
        new_dir_tree.append(x)

#print(new_dir_tree)


def calc_folder_size(path):
    """
    calculate folder size by summing up the size of every subfolder 
    """
    size=0
    for x in new_dir_tree:
        if(x[0].startswith(path)): #check if folder has same beginning path than to be searched path
            size+=x[1]
    
    return size


## Sum up all folders smaller than 100000 ##
folder_size_sum=0
for x in new_dir_tree:
    tmp = calc_folder_size(x[0])
    if (tmp<=100000):
        folder_size_sum+=tmp
print("Part one: "+str(folder_size_sum))

##### Part two #####

total_used_space=calc_folder_size("/")
#print(total_used_space)
to_be_deleted=30000000-(70000000-total_used_space)

#print(to_be_deleted) # size of directory to be deleted


## calculate folders big enough to solve the space problem ##
available_folders=[]
for x in new_dir_tree:
    tmp = calc_folder_size(x[0])
    if (tmp>=to_be_deleted):
        available_folders.append([x[0],tmp])

#print(available_folders)

## find smallest of these folders ##
min_folder_size=calc_folder_size("/")
for x in available_folders:
    if x[1]<min_folder_size:
        min_folder_size=x[1]

print("Part two: "+str(min_folder_size))
