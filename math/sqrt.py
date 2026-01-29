class Solution():
    def getsqrt(self,n):
        res = n
        i = 1
        while True:
            if ( i * i) <= n:
                res = i
            else:
                break
            i += 1
        
        return res


## Test Case
sol = Solution()
prb = [[4,2],[25,5],[30,5],[100,10],[1,1]]
for c in prb:
    print(f"The sqrt of {c[0]} : {sol.getsqrt(c[0])}")
    print(f"Expected: {c[1]}")
    print("-" * 10)
