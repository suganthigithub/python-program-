str=input("enter the string:")
rev_str=""

for char in str:
    rev_str=char+rev_str

if str==rev_str:
    print(str,"is a palindrome")

else:
    print(str,"is not a palindrome")   