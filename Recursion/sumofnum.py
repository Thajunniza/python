class Solution():
    def sum_num(self,n):
        result = 0
        i = 1
        while i <= n:
            result += i
            i += 1
        return result
    

    def sum_num_rec(self,n):
        if n == 0:
            return 0
        num = self.sum_num_rec(n-1)
        return n + num


##Test Case
s = Solution()
print(s.sum_num(5))
print(s.sum_num_rec(5))