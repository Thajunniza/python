""" 
Inserting values in to 2D array
2 ways
Adding column
Adding row
Time Complexity: O(mn)
Space Complexity:O(mn)
"""
import numpy as np
twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)
## Adding Row
# np.insert(arr,index,values,axis(0,1))
# axis 0 ->Row  1->Column
new2DArrayCol = np.insert(twoDArray,0,[[1,2,3,4]],axis=1)
print(new2DArrayCol)

#Adding Row
new2DArrRow = np.insert(twoDArray,2,[[1,2,3,4]],0)
print(new2DArrRow)

## Adding row or column at the end of array
## using append function
print("Append Array")
new2DArrCol1 = np.append(twoDArray,twoDArray,axis=1)
print(new2DArrCol1)
new2DArrRow1 = np.append(twoDArray,[[1,2,3,4]],0)
print(new2DArrRow1)
