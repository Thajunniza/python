
"""
Power of the number
--------------------------------
Give the Power of number
Where you need two inputs base and exponent
for eg 2 to power of 3 = 8
where 2 is base and power is 3

Examples
--------
Input: 2 ** 3  -> Output: 8
Input: 3 ** 2  -> Output: 9
Input: 4 ** 5  -> Output: 1024

Approach
--------
1. Use Recurvise method
"""
class Solution():
    def getPower(self,n,e):
        return n ** e
    
    def getPower_rec(self,n,e):
        if e == 0:
            return 1
        num = self.getPower_rec(n,e-1)
        return n * num
    
## Test Results
sol = Solution()
nums = [(2,3),(3,2),(4,5)]
for n,e in nums:
    print(f"Power of ({n},{e}) = {sol.getPower_rec(n,e)}")
    if sol.getPower(n,e) == sol.getPower_rec(n,e):
        print("PASS")
    else:
        print("FAIL")
