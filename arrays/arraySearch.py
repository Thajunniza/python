""" 
Array Searching
Linear Search
"""

import array
# Linear Search
def linearSearch(arr,target):
    for n in range(len(arr)):
        if arr[n] == target:
            return n
    return -1
        

arr1 = array.array('i',[2,4,8,10,13])
print(linearSearch(arr1,2))