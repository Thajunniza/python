"""
2 dimensional array has two index
a[i][j] 
"""

import numpy as np
twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])


## Access Array
#Time Complexity: O(1)
#Space Complexity: O(1)
def accessElement(arr,row,col):
    if row >= len(arr) or col >= len(arr[0]):
        print("Incorrect index")
    else:
        print(arr[row][col])

accessElement(twoDArray,1,2)
accessElement(twoDArray,2,3)
accessElement(twoDArray,4,3)

## Travese Array to access all the array elements
## Time Complexity : O(n^2)
## space Complexity: O(1)
print(twoDArray)
def traverseArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j],end=" ")
        print("")

traverseArray(twoDArray)