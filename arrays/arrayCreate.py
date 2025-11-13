"""
Array Creation using List
this is not real array as you can store diff data elements
"""
arr = [10,20,30,"Thaj"]
print(arr)

"""
# Using array Module
# true array type that stores only one data type.
#syntax
from array import array
arr = array(typecode, elements)

"""
from array import array
arr1 = array('i',[1,2,3,4])
print(arr1)
print(arr1[2])

""" 
# Using NumPy module
"""
import numpy as np
arr2 = np.array([1,2,3,4],dtype="i")
print(arr2)

#Create 2D array / matrix
arr3 = np.array([[1,1],[1,2],[2,1],[2,2]])
print(arr3)
print(arr3[0])
print(arr3[0][1])

#Create array of zeros or ones
arrZero = np.zeros(5)
print(arrZero)
# Create array of Ones
arrOnes =np.ones(5)
print(arrOnes)

# Array with range
arrRange = np.arange(0,100,5) #(start,stop,step)
print(arrRange)


"""
## Output
[10, 20, 30, 'Thaj']
array('i', [1, 2, 3, 4])
3
[1 2 3 4]
[[1 1]
 [1 2]
 [2 1]
 [2 2]]
[1 1]
1
[0. 0. 0. 0. 0.]
[1. 1. 1. 1. 1.]
[ 0  5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95]
 
"""