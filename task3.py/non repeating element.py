# pyhton progam for non repeating element in given list of integer#

def suman_common_element(data):
    result={}
    for element in data:
      result[element] =result.get(element,0) +1
    return max (result, key=result.get)

data =input ("enter the string:")
print ("the most freqent character in the string is:",suman_common_element(data))         