"""
SYNTAX
for variable in sequence:
    # code to run each time

"""

"""
Example 1 — Loop over a String
Each Character iterates
"""
print("Iterating String")
word = "Thajunniza"
for ch in word:
    print(ch)
    
"""
Example 2 — Loop over a List
Each row iterates
"""
print("Array of Numbers")
fruits =["Apple","Banana","Pear"]
for fruit in fruits:
    print(fruit)
print("Array of Numbers")
evenList = [2,4,6,8,10]
for n in evenList:
    print(n)    
    
"""
Example 3 — Using range()
range(start, stop, step) is often used to loop over a series of numbers.
start - starting numberof seq - default 0
stop - ending number of seq - no default its mandatory
step - increment/decrement between the iteration(eg:1 or -1) default 1
# Note: stop value is exclusive, meaning the loop runs until (stop - 1)
"""    
# Range without start and step so it will take default(5)
print("Range with only stop value where start and step is default (5)")
for i in range(5):
    print(i)

# Range with start and end and stop is default(5,10)
print("Range with start and end with stop default (5,10)")
for i in range(5,10):
    print(i) 

#Range with start,end and step (10,50,5)
print("Range with start ,stop and end (10,50,5)")
for i in range(5,50,5):
    print(i)       

# Range with Decrement  (5,0,-1)
print("Range with Decrement with  (5,0,-1)")
for i in range(5,0,-1):
    print(i)
    
"""
## Output
Iterating String
T
h
a
j
u
n
n
i
z
a
Array of Numbers
Apple
Banana
Pear
Array of Numbers
2
4
6
8
10
Range with only stop value where start and step is default (5)
0
1
2
3
4
Range with start and end with stop default (5,10)
5
6
7
8
9
Range with start ,stop and end (10,50,5)
5
10
15
20
25
30
35
40
45
Range with Decrement with  (5,0,-1)
5
4
3
2
1
"""    