# write a program that a take a string and return the no of unique characters in it

str=input("enter string")
print(str)
l=list(str)
print(l)
freq=[l.count(ele) for ele in l]
print(freq) 
d=dict(zip(l,freq))
print(d )