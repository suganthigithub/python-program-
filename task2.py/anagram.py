#program that a string and return true if it an anagram and another string,false otherwise

str1=input("enter string1")
str2=input("enter string2")

if len(str1)!=len(str2):
    print("false anagram")

else:
    if sorted(str1)==sorted(str2):
        print ("true anagram")
    else:
        print("false anagram")    
