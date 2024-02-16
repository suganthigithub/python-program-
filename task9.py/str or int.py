#lambda func to check every element of a list is an integer or string

test_list=[[5,6,3],["Gfg",3,"is"],[9,"best",4]]

print("original list:"+str(test_list))

res=reduce(lambda acc, sublist:acc+[elem for elem in sublist if is instance(elem,str)],test_list,[])
print ("the string instances:"+str(res))
         
res=reduce(lambda acc, sublist:acc+[elem for elem in sublist if is instance(elem,int)],test_list,[])
print ("the string instances:"+str(res1))

         




