# take strings and return the most frequent charater in it

my_string =input("enter string:")

my_counter ={}
for letter in my_string:
    if letter in my_counter:
        my_counter[letter]+=1
    else:
        my_counter[letter]=1    

max_key =max(my_counter,key=my_counter.get) 

print(f"character:{max_key} has most frequency of : {my_counter[max_key]}")       