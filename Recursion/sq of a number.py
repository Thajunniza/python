
"""
Square of the number
--------------------------------
Give the Square of number

Examples
--------
Input: 2  -> Output: 4
Input: 3  -> Output: 9
Input: 4  -> Output: 16

Approach
--------
1. Use Recurvise method
2. USe formula n^2 = (n-1)^2 + 2n -1
"""
class Solution():
    def getSq(self,n):
        return n * n
    
    def getSq_rec(self,n):
        if n == 0:
            return 0
        return self.getSq_rec(n-1) + ( 2 * n) - 1
    
## Test Results
sol = Solution()
nums = [2,3,4,5]
for n in nums:
    print(f"Square of {n} = {sol.getSq_rec(n)}")
    if sol.getSq(n) == sol.getSq_rec(n):
        print("PASS")
    else:
        print("FAIL")
