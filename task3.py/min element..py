#minimum element in rated and shorted list#


def minelement(list):
    min=list[0]
    for ele in list:
        if ele<min:
      min=ele
    return min
 list=[100,8,4,68,20]

 print("smallest element of list:",minelement(list))   