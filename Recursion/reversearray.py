class Solution:
    def reverse_array(self,arr):
        def helper(l,r):
            if l > r :
                return
            arr[l],arr[r] = arr[r],arr[l]
            helper(l+1,r-1)
        helper(0,len(arr)-1)
        return arr
    
## Test Case
s = Solution()
print(s.reverse_array([1,2,3,4,5]))
