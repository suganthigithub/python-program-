##progam to find duplicate from the list##


l=[1,1,2,3,4,4,5,5,6,7,8,9]
uniquelist =[]
deplist =[]
for i in l:
    if i not in uniquelist:
        uniquelist.append(i)
    elif i not in deplist:
        deplist.append(i)
print(deplist)            