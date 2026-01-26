class Solution():
    def print_name(self,n,name):
        for _ in range(n):
            print(name)
    
    def print_name_rec(self,n,name):
        if n == 0:
            return
        self.print_name_rec(n-1,name)
        
        print(f"{n}:{name}")




#Test Run
s = Solution()
s.print_name(5,"Thaj")
s.print_name_rec(5,"Zayd")
        