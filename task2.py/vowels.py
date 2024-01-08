# To calculate the vowels
sentance=input("enter the sentance:")
string= sentance.lower()
print(string)
count=0
vowels=("a","e","i","o","u")
for char in string:
    if char in vowels:
        count=count+1

print("number of vowels in the given sentance is:",count)  