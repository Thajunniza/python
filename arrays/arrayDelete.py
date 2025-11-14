"""
Array Deletion 
Time Complexity : O(n)
Space Complexity: O(1)
"""


import array


arr = array.array('i',[10,20,30,40,50])
arr.remove(10)
print(arr)

arr.remove(30)
print(arr)

arr.remove(50)
print(arr)