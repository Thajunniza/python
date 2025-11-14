""" 
2 D Array Searching
Linear Search
"""

import numpy as np
twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

## Time Complexity : O(n^2)
## space Complexity: O(1)
def linearSearch(arr,target):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if(arr[i][j] == target):
                return 'The value is located in index: ' + str(i) + ' ' + str(j)
            
    return 'The element not found'

print(linearSearch(twoDArray,14))
print(linearSearch(twoDArray,17))
print(linearSearch(twoDArray,50))