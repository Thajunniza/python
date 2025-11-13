""" 
# Array Traversal that means iterating array
# to access all the elements of array
"""

from array import array
import numpy as np

def traverseArray(ar):
    for i in ar:
        print(i)
    
arr = array('i',[10,20,30])
traverseArray(arr)

##array module supports only one string-related typecode:
arr1 = array('u', ['H', 'E', 'L', 'L', 'O'])
traverseArray(arr1)

## so use numpy for string
arr2 = np.array(['Sunday','Monday','Tuesday','Wednesday'])
traverseArray(arr2)

