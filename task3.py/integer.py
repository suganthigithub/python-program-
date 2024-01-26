#sum of first and last digit of integer


num=int(input("enter the number:"))
last=num%10
while num!=0:
    first=num%10
    num=num//10
sum=last+first
print("the sum of last and first digit is:",sum)    