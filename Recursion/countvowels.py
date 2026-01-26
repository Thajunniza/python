class Solution:
    def count_vowels(self,s):
        vowel = {'a','e','i','o','u'}
        count = 0
        for c in s:
            if c in vowel:
                count += 1
        return count
    
    def count_vowel_rec(self,s):
        vowel = {'a','e','i','o','u'}
        n = len(s)
        val = 0
        if n == 0:
            return 0
        if s[0] in vowel:
            val = 1
        count = self.count_vowel_rec(s[1:])
        return val + count
    

## Test case
sol = Solution()
print(sol.count_vowels("Thajunniza"))
print(sol.count_vowel_rec("Thajunniza"))