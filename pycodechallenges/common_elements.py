#!/usr/bin/python3
# written by: atholcomb
# common_elements.py

def commonElements(listA, listB):
    result = set() # create a set with only unique values
    
    for item in listA:
        if item in listB:
            result.add(item) # add the correct value to the set
    
    return list(result) # convert the set into a list for ouput




print(commonElements([-1, 3, 4, 6, 7, 9], [1, 3]))
print(commonElements([1, 3, 4, 6, 7, 9], [1, 2, 3, 4, 7, 10]))
print(commonElements([1, 2, 2, 2, 3, 4, 5], [1, 2, 4, 5]))
print(commonElements([1, 2, 3, 4, 5], [10, 12, 13, 15]))
