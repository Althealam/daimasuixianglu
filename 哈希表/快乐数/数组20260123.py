class Solution:
    def isHappy(self, n: int) -> bool:
        set_n = set()
        while n not in set_n:
            set_n.add(n)
            if n==1:
                return True
            n = self.get_new_n(n)
        return False
    
    def get_new_n(self, n):
        ans = 0
        for i in str(n):
            ans+=int(i)**2
        return ans
