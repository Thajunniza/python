"""
2 D Array Deletion 
Time Complexity : O(n) - Because NumPy creates a completely new array after removing the row/column/element.
Space Complexity: O(n) - Because it allocates a new array to store the result.

np.delete(arr, obj, axis=None)
# Parameters:
#   arr  : ndarray
#          The input array from which you want to delete elements.
#
#   obj  : int, slice, or list
#          The index (or indices) of the elements you want to delete.
#
#   axis : int or None
#          The axis along which deletion happens.
#          
#          axis = 0  → delete a row
#          axis = 1  → delete a column
#          axis = None → delete elements from the flattened array
#
# Returns:
#   new_array : ndarray
#               A new array with the specified elements removed.
#               (Original array stays unchanged)

"""

import numpy as np
twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)

new2DArr = np.delete(twoDArray,0,axis=0)
print(new2DArr)

new2DArr = np.delete(twoDArray,0,axis=1)
print(new2DArr)