# array.insert(index,value)

from array import array
arr = array("i",[1,2,3,4])
arr.insert(0,0)
print(arr)
arr.insert(len(arr),5)
print(arr)

""" 
Insert in NumPy Array
NumPy arrays have fixed size, so insertion creates a new array.
"""
import numpy as np
arr1 = np.array([1,2,3,4])
print(arr1)
arr2 = np.insert(arr1,len(arr1),10)
print(arr2)





