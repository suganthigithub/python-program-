#find sub list is sum equal to zero#
list_1=(4,2,-3,1,6)
sub_list=[]

for i in list_1:
    sub_list.append(i)
    if sum (sub_list)==sum(list_1):
        sub_list.remove(i)
    for i in list_1:
        if sum(sub_list) == sum(list_1):
            sub_list.remove(i)

print(sub_list)            
