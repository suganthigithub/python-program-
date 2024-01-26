#list in two different list

input=list(map(int,input("enter the number list:").split()))
evenlist=[]
oddlist=[]
for val in input:
    if(val%2==0):
        evenlist.append(val)
    else:
        oddlist.append(val)

print("even list:",end="")
print(*evenlist)

print("odd list:",odd="")
print(*oddlist)            