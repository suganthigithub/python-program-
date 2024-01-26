# find happy number in given python list

n=int(input("enter the number:"))
x=n
while x>1000:
    sum=0
    while x>0:
        r=x%1000
        sum=sum+(r**2)
        x=x//1000
    x=sum
if x==1:
    print(n,"is a happy number")
else:
    print(n,"is not happy number")            
