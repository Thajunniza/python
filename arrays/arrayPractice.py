from array import *

# 1. Create an array and traverse. 
print("Step 1: Create an array and traverse")
my_array = array('i',[1,2,3,4,5])
for i in my_array:
    print (i)

# 2. Access individual elements through indexes
print("Step 2: Access individual elements through indexes")
print(f"Value of second index: {my_array[2]}")

# 3. Append any value to the array using append() method
print("Step 3: Append any value")
my_array.append(6)
print(my_array)

# 4. Insert value in an array using insert() method
print("Step 4:Insert value")
my_array.insert(2,10)
print(my_array)

# 5. Extend python array using extend() method
print("Step 5: Extend python with another array ie more than one value")
arr1 = array('i',[5,10,20])
my_array.extend(arr1)
print(my_array)

# 6. Add items from list into array using fromlist() method
print("Step 6:Add items from list")
lis = [2,4,5,8]
my_array.fromlist(lis)
print(my_array)

# 7. Remove any array element using remove() method
print("Step 7: Remove any array")
my_array.remove(2)
print(my_array)

# 8. Remove last array element using pop() method
print("Step 8: Remove last array element")
my_array.pop()
print(my_array)

# 9. Fetch any element through its index using index() method
print("Step 9: Fetch any element through its index")
print(my_array.index(5))

# 10. Reverse a python array using reverse() method
print("Step 10: Reverse an array")
my_array.reverse()
print(my_array)

# 11. Get array buffer information through buffer_info() method
print("Step 11")
print(my_array.buffer_info())

# 12. Check for number of occurrences of an element using count() method
print("Step 12:Check for number of occurrences of an element")
print(my_array.count(10))
print(my_array.count(11))

# 13. Convert array to string using tostring() method
print("Step 13: Convert array to string")
# arrStr = my_array.tostring()

# 14. Convert array to a python list with same elements using tolist() method
print("Step 14:Convert array to a python list")
arrlist = my_array.tolist()
print(arrlist)

# 16. Slice Elements from an array
print("Step 16")
print(my_array[2:8:2])
print(my_array[len(my_array):0:-1])
